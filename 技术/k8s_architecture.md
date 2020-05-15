

# kube-controller-manager

一系列控制器的集合。
我们可以查看一下 Kubernetes 项目的 pkg/controller 目录：

```

$ cd kubernetes/pkg/controller/
$ ls -d */              
deployment/             job/                    podautoscaler/          
cloud/                  disruption/             namespace/              
replicaset/             serviceaccount/         volume/
cronjob/                garbagecollector/       nodelifecycle/          replication/            statefulset/            daemon/
...
```

实际上，这些控制器之所以被统一放在 pkg/controller 目录下，
就是因为它们都遵循 Kubernetes 项目中的一个通用编排模式，
即：控制循环（control loop）。
```
for {
  实际状态 := 获取集群中对象X的实际状态（Actual State）
  期望状态 := 获取集群中对象X的期望状态（Desired State）
  if 实际状态 == 期望状态{
    什么都不做
  } else {
    执行编排动作，将实际状态调整为期望状态
  }
}
```

在具体实现中，实际状态往往来自于 Kubernetes 集群本身。
比如，kubelet 通过心跳汇报的容器状态和节点状态，或者监控系统中保存的应用监控数据，
或者控制器主动收集的它自己感兴趣的信息，这些都是常见的实际状态的来源。
而期望状态，一般来自于用户提交的 YAML 文件。

比如，Deployment 对象中 Replicas 字段的值。
很明显，这些信息往往都保存在 Etcd 中。
以 Deployment 为例，我和你简单描述一下它对控制器模型的实现：
Deployment 控制器从 Etcd 中获取到所有携带了“app: nginx”标签的 Pod，然后统计它们的数量，
这就是实际状态；
Deployment 对象的 Replicas 字段的值就是期望状态；
Deployment 控制器将两个状态做比较，然后根据比较结果，确定是创建 Pod，
还是删除已有的 Pod（具体如何操作 Pod 对象，我会在下一篇文章详细介绍）。
可以看到，一个 Kubernetes 对象的主要编排逻辑，实际上是在第三步的“对比”阶段完成的。

调谐的最终结果，往往都是对被控制对象的某种写操作。
比如，增加 Pod，删除已有的 Pod，或者更新 Pod 的某个字段。
这也是 Kubernetes 项目“面向 API 对象编程”的一个直观体现。

## 事件驱动与控制器模式    

事件往往是一次性的，如果操作失败比较难处理，但是控制器是循环一直在尝试的，
更符合kubernetes申明式API，最终达到与申明一致;

相当于select和epoll的区别

deployment会创建rs,然后由rs创建pod,所以pod的owner应该是rs

