

# 分布式ID生成器

## 场景

有时我们需要能够生成类似MySQL自增ID这样不断增大，同时又不会重复的id。以支持业务中的高并发场景。比较典型的，电商促销时，短时间内会有大量的订单涌入到系统，比如每秒10w+。明星出轨时，会有大量热情的粉丝发微博以表心意，同样会在短时间内产生大量的消息。

在插入数据库之前，我们需要给这些消息、订单先打上一个ID，然后再插入到我们的数据库。对这个id的要求是希望其中能带有一些时间信息，这样即使我们后端的系统对消息进行了分库分表，也能够以时间顺序对这些消息进行排序。

## worker_id分配

timestamp，datacenter_id，worker_id和sequence_id这四个字段中，timestamp和sequence_id是由程序在运行期生成的。但datacenter_id和worker_id需要我们在部署阶段就能够获取得到，并且一旦程序启动之后，就是不可更改的了（想想，如果可以随意更改，可能被不慎修改，造成最终生成的id有冲突）。

## 开源实现

### 标准snowflake实现

github.com/bwmarrin/snowflake 是一个相当轻量化的snowflake的Go实现

```
package main

import (
    "fmt"
    "os"

    "github.com/bwmarrin/snowflake"
)

func main() {
    n, err := snowflake.NewNode(1)
    if err != nil {
        println(err)
        os.Exit(1)
    }

    for i := 0; i < 3; i++ {
        id := n.Generate()
        fmt.Println("id", id)
        fmt.Println(
            "node: ", id.Node(),
            "step: ", id.Step(),
            "time: ", id.Time(),
            "\n",
        )
    }
}
```

### sonyflake

"github.com/sony/sonyflake"

sonyflake是Sony公司的一个开源项目，基本思路和snowflake差不多，不过位分配上稍有不同，

```
package main

import (
    "fmt"
    "os"
    "time"

    "github.com/sony/sonyflake"
)

func getMachineID() (uint16, error) {
    var machineID uint16
    var err error
    machineID = readMachineIDFromLocalFile()
    if machineID == 0 {
        machineID, err = generateMachineID()
        if err != nil {
            return 0, err
        }
    }

    return machineID, nil
}

func checkMachineID(machineID uint16) bool {
    saddResult, err := saddMachineIDToRedisSet()
    if err != nil || saddResult == 0 {
        return true
    }

    err := saveMachineIDToLocalFile(machineID)
    if err != nil {
        return true
    }

    return false
}

func main() {
    t, _ := time.Parse("2006-01-02", "2018-01-01")
    settings := sonyflake.Settings{
        StartTime:      t,
        MachineID:      getMachineID,
        CheckMachineID: checkMachineID,
    }

    sf := sonyflake.NewSonyflake(settings)
    id, err := sf.NextID()
    if err != nil {
        fmt.Println(err)
        os.Exit(1)
    }

    fmt.Println(id)
}
```

# 分布式锁

## 基于Redis的setnx

通过代码和执行结果可以看到，我们远程调用setnx运行流程上和单机的trylock非常相似，如果获取锁失败，那么相关的任务逻辑就不应该继续向前执行。

setnx很适合在高并发场景下，用来争抢一些“唯一”的资源。
比如交易撮合系统中卖家发起订单，而多个买家会对其进行并发争抢。
这种场景我们没有办法依赖具体的时间来判断先后，因为不管是用户设备的时间，
还是分布式场景下的各台机器的时间，都是没有办法在合并后保证正确的时序的。
哪怕是我们同一个机房的集群，不同的机器的系统时间可能也会有细微的差别。
所以，我们需要依赖于这些请求到达Redis节点的顺序来做正确的抢锁操作。
如果用户的网络环境比较差，那也只能自求多福了。

```
package main

import (
    "fmt"
    "sync"
    "time"

    "github.com/go-redis/redis"
)

func incr() {
    client := redis.NewClient(&redis.Options{
        Addr:     "localhost:6379",
        Password: "", // no password set
        DB:       0,  // use default DB
    })

    var lockKey = "counter_lock"
    var counterKey = "counter"

    // lock
    resp := client.SetNX(lockKey, 1, time.Second*5)
    lockSuccess, err := resp.Result()

    if err != nil || !lockSuccess {
        fmt.Println(err, "lock result: ", lockSuccess)
        return
    }

    // counter ++
    getResp := client.Get(counterKey)
    cntValue, err := getResp.Int64()
    if err == nil || err == redis.Nil {
        cntValue++
        resp := client.Set(counterKey, cntValue, 0)
        _, err := resp.Result()
        if err != nil {
            // log err
            println("set value error!")
        }
    }
    println("current counter is ", cntValue)

    delResp := client.Del(lockKey)
    unlockSuccess, err := delResp.Result()
    if err == nil && unlockSuccess > 0 {
        println("unlock success!")
    } else {
        println("unlock failed", err)
    }
}

func main() {
    var wg sync.WaitGroup
    for i := 0; i < 10; i++ {
        wg.Add(1)
        go func() {
            defer wg.Done()
            incr()
        }()
    }
    wg.Wait()
}
```

## 基于ZooKeeper

基于ZooKeeper的锁与基于Redis的锁的不同之处在于Lock成功之前会一直阻塞，
这与我们单机场景中的mutex.Lock很相似。

其原理也是基于临时Sequence节点和watch API，例如我们这里使用的是/lock节点。
Lock会在该节点下的节点列表中插入自己的值，只要节点下的子节点发生变化，就会通知所有watch该节点的程序。
这时候程序会检查当前节点下最小的子节点的id是否与自己的一致。如果一致，说明加锁成功了。

这种分布式的阻塞锁比较适合分布式任务调度场景，但不适合高频次持锁时间短的抢锁场景。
按照Google的Chubby论文里的阐述，基于强一致协议的锁适用于粗粒度的加锁操作。
这里的粗粒度指锁占用时间较长。我们在使用时也应思考在自己的业务场景中使用是否合适。

```
package main

import (
    "time"

    "github.com/samuel/go-zookeeper/zk"
)

func main() {
    c, _, err := zk.Connect([]string{"127.0.0.1"}, time.Second) //*10)
    if err != nil {
        panic(err)
    }
    l := zk.NewLock(c, "/lock", zk.WorldACL(zk.PermAll))
    err = l.Lock()
    if err != nil {
        panic(err)
    }
    println("lock succ, do your business logic")

    time.Sleep(time.Second * 10)

    // do some thing
    l.Unlock()
    println("unlock succ, finish business logic")
}
```

## 基于etcd

etcd中没有像ZooKeeper那样的Sequence节点。
所以其锁实现和基于ZooKeeper实现的有所不同。在上述示例代码中使用的etcdsync的Lock流程是：

1.先检查/lock路径下是否有值，如果有值，说明锁已经被别人抢了
2.如果没有值，那么写入自己的值。写入成功返回，说明加锁成功。写入时如果节点被其它节点写入过了，那么会导致加锁失败，这时候到 3
watch /lock下的事件，此时陷入阻塞
3.当/lock路径下发生事件时，当前进程被唤醒。检查发生的事件是否是删除事件（说明锁被持有者主动unlock），或者过期事件（说明锁过期失效）。如果是的话，那么回到 1，走抢锁流程。
值得一提的是，在etcdv3的API中官方已经提供了可以直接使用的锁API，读者可以查阅etcd的文档做进一步的学习。

```
package main

import (
    "log"

    "github.com/zieckey/etcdsync"
)

func main() {
    m, err := etcdsync.New("/lock", 10, []string{"http://127.0.0.1:2379"})
    if m == nil || err != nil {
        log.Printf("etcdsync.New failed")
        return
    }
    err = m.Lock()
    if err != nil {
        log.Printf("etcdsync.Lock failed")
        return
    }

    log.Printf("etcdsync.Lock OK")
    log.Printf("Get the lock. Do something here.")

    err = m.Unlock()
    if err != nil {
        log.Printf("etcdsync.Unlock failed")
    } else {
        log.Printf("etcdsync.Unlock OK")
    }
}
```

## 如何选择合适的锁

业务还在单机就可以搞定的量级时，那么按照需求使用任意的单机锁方案就可以。

如果发展到了分布式服务阶段，但业务规模不大，qps很小的情况下，使用哪种锁方案都差不多。
如果公司内已有可以使用的ZooKeeper、etcd或者Redis集群，那么就尽量在不引入新的技术栈的情况下满足业务需求。

业务发展到一定量级的话，就需要从多方面来考虑了。
首先是你的锁是否在任何恶劣的条件下都不允许数据丢失，如果不允许，那么就不要使用Redis的setnx的简单锁。

对锁数据的可靠性要求极高的话，那只能使用etcd或者ZooKeeper这种通过一致性协议保证数据可靠性的锁方案。
但可靠的背面往往都是较低的吞吐量和较高的延迟。
需要根据业务的量级对其进行压力测试，以确保分布式锁所使用的etcd或ZooKeeper集群可以承受得住实际的业务请求压力。
需要注意的是，etcd和Zookeeper集群是没有办法通过增加节点来提高其性能的。
要对其进行横向扩展，只能增加搭建多个集群来支持更多的请求。
这会进一步提高对运维和监控的要求。多个集群可能需要引入proxy，没有proxy那就需要业务去根据某个业务id来做分片。如果业务已经上线的情况下做扩展，还要考虑数据的动态迁移。这些都不是容易的事情。

