


## 常见语法题目 一

### 1、下面代码能运行吗？为什么。

```go
type Param map[string]interface{}

type Show struct {
	Param
}

func main1() {
	s := new(Show)
	s.Param["RMB"] = 10000
}
```

**解析**

共发现两个问题：

1. `main` 函数不能加数字。
2. `new` 关键字无法初始化 `Show` 结构体中的 `Param` 属性，所以直接对 `s.Param` 操作会出错。

### 2、请说出下面代码存在什么问题。

```go
type student struct {
	Name string
}

func zhoujielun(v interface{}) {
	switch msg := v.(type) {
	case *student, student:
		msg.Name
	}
}
```

**解析：**

golang中有规定，`switch type`的`case T1`，类型列表只有一个，那么`v := m.(type)`中的`v`的类型就是T1类型。

如果是`case T1, T2`，类型列表中有多个，那`v`的类型还是多对应接口的类型，也就是`m`的类型。

所以这里`msg`的类型还是`interface{}`，所以他没有`Name`这个字段，编译阶段就会报错。具体解释见： <https://golang.org/ref/spec#Type_switches>

### 3、写出打印的结果。

```go
type People struct {
	name string `json:"name"`
}

func main() {
	js := `{
		"name":"11"
	}`
	var p People
	err := json.Unmarshal([]byte(js), &p)
	if err != nil {
		fmt.Println("err: ", err)
		return
	}
	fmt.Println("people: ", p)
}
```

**解析：**

按照 golang 的语法，小写开头的方法、属性或 `struct` 是私有的，同样，在`json` 解码或转码的时候也无法上线私有属性的转换。

题目中是无法正常得到`People`的`name`值的。而且，私有属性`name`也不应该加`json`的标签。


### 4、下面的代码是有问题的，请说明原因。

```go
type People struct {
	Name string
}

func (p *People) String() string {
	return fmt.Sprintf("print: %v", p)
}

func main() {
 	p := &People{}
	p.String()
}
```

**解析：**

在golang中`String() string` 方法实际上是实现了`String`的接口的，该接口定义在`fmt/print.go`  中：

```go
type Stringer interface {
	String() string
}
```

在使用 `fmt` 包中的打印方法时，如果类型实现了这个接口，会直接调用。而题目中打印 `p` 的时候会直接调用 `p` 实现的 `String()` 方法，然后就产生了循环调用。


### 5、请找出下面代码的问题所在。

```go
func main() {
	ch := make(chan int, 1000)
	go func() {
		for i := 0; i < 10; i++ {
			ch <- i
		}
	}()
	go func() {
		for {
			a, ok := <-ch
			if !ok {
				fmt.Println("close")
				return
			}
			fmt.Println("a: ", a)
		}
	}()
	close(ch)
	fmt.Println("ok")
	time.Sleep(time.Second * 100)
}
```


**解析：**

在 golang 中 `goroutine` 的调度时间是不确定的，在题目中，第一个写 `channel` 的 `goroutine` 可能还未调用，
或已调用但没有写完时直接 `close` 管道，可能导致写失败，既而出现 `panic` 错误。



### 6、请说明下面代码书写是否正确。

```go
var value int32

func SetValue(delta int32) {
	for {
		v := value
		if atomic.CompareAndSwapInt32(&value, v, (v+delta)) {
			break
		}
	}
}
```


    
**解析：**

`atomic.CompareAndSwapInt32` 函数不需要循环调用。


### 7、下面的程序运行后为什么会爆异常。

```go
type Project struct{}

func (p *Project) deferError() {
	if err := recover(); err != nil {
		fmt.Println("recover: ", err)
	}
}

func (p *Project) exec(msgchan chan interface{}) {
	for msg := range msgchan {
		m := msg.(int)
		fmt.Println("msg: ", m)
	}
}

func (p *Project) run(msgchan chan interface{}) {
	for {
		defer p.deferError()
		go p.exec(msgchan)
		time.Sleep(time.Second * 2)
	}
}

func (p *Project) Main() {
	a := make(chan interface{}, 100)
	go p.run(a)
	go func() {
		for {
			a <- "1"
			time.Sleep(time.Second)
		}
	}()
	time.Sleep(time.Second * 100000000000000)
}

func main() {
	p := new(Project)
	p.Main()
}
```

**解析：**

有一下几个问题：

1. `time.Sleep` 的参数数值太大，超过了 `1<<63 - 1` 的限制。
2. `defer p.deferError()` 需要在协程开始出调用，否则无法捕获 `panic`。


### 8、请说出下面代码哪里写错了

```go
func main() {
	abc := make(chan int, 1000)
	for i := 0; i < 10; i++ {
		abc <- i
	}
	go func() {
		for {
			a := <-abc
			fmt.Println("a: ", a)
		}
	}()
	close(abc)
	fmt.Println("close")
	time.Sleep(time.Second * 100)
}
```

**解析：**

协程可能还未启动，管道就关闭了。


### 9、请说出下面代码，执行时为什么会报错

```go
type Student struct {
	name string
}

func main() {
	m := map[string]Student{"people": {"zhoujielun"}}
	m["people"].name = "wuyanzu"
}

```

**解析：**

`map`中`value`是非指针类型，可以当做一个原子变量，只能统一更改，不能只改`Student`其中一个成员，如果想要更改`Student`其中一个成员，使用`map[string]*Student`.


### 10、请说出下面的代码存在什么问题？

```go
type query func(string) string

func exec(name string, vs ...query) string {
	ch := make(chan string)
	fn := func(i int) {
		ch <- vs[i](name)
	}
	for i, _ := range vs {
		go fn(i)
	}
	return <-ch
}

func main() {
	ret := exec("111", func(n string) string {
		return n + "func1"
	}, func(n string) string {
		return n + "func2"
	}, func(n string) string {
		return n + "func3"
	}, func(n string) string {
		return n + "func4"
	})
	fmt.Println(ret)
}
```

**解析：** 

依据4个goroutine的启动后执行效率，很可能打印111func4，但其他的111func*也可能先执行，exec只会返回一条信息。


### 11、下面这段代码为什么会卡死？

```go
package main

import (
    "fmt"
    "runtime"
)

func main() {
    var i byte
    go func() {
        for i = 0; i <= 255; i++ {
        }
    }()
    fmt.Println("Dropping mic")
    // Yield execution to force executing other goroutines
    runtime.Gosched()
    runtime.GC()
    fmt.Println("Done")
}
```

**解析：**

Golang 中，byte 其实被 alias 到 uint8 上了。所以上面的 for 循环会始终成立，因为 i++ 到 i=255 的时候会溢出，i <= 255 一定成立。

也即是， for 循环永远无法退出，所以上面的代码其实可以等价于这样：
```go
go func() {
    for {}
}
```

正在被执行的 goroutine 发生以下情况时让出当前 goroutine 的执行权，并调度后面的 goroutine 执行：

- IO 操作
- Channel 阻塞
- system call
- 运行较长时间

如果一个 goroutine 执行时间太长，scheduler 会在其 G 对象上打上一个标志（ preempt），
当这个 goroutine 内部发生函数调用的时候，会先主动检查这个标志，如果为 true 则会让出执行权。

main 函数里启动的 goroutine 其实是一个没有 IO 阻塞、没有 Channel 阻塞、没有 system call、没有函数调用的死循环。

也就是，它无法主动让出自己的执行权，即使已经执行很长时间，scheduler 已经标志了 preempt。

而 golang 的 GC 动作是需要所有正在运行 `goroutine` 都停止后进行的。
因此，程序会卡在 `runtime.GC()` 等待所有协程退出。


# a test paper

```

    一、	选择题
    1.	关于init函数，下面说法正确的是（BD）
    A. main包中，不能有init函数
    B. 程序编译时，先执行导入包的init函数，再执行本包内的init函数
    C. 程序编译时，先执行包内的init函数，再执行本导入包的init函数
    D. 一个包中，可以包含多个init函数


    2.	对于函数定义：
    func add(args ...int) int {
         sum := 0
         for _, arg := range args {
             sum += arg
         }
         return sum
    }
    下面对add函数调用错误的是（C）
    A. add(3,4 )
    B. add(5, 6, 7)
    C. add([]int{3, 4})
    D. add([]int{5, 6, 7}...)

    3.	关于切片的初始化，下面错误的是（D）
    A. s := make([]int, 0)
    B. s := make([]int, 5, 10)
    C. s := []int{1, 2, 3, 4, 5}
    D. s := make([]int)

    4.	关于函数声明，下面语法正确的是（C）
    A. func f(a, b int) (value int, err error)
    B. func f(a int, b int) (value int, err error)
    C. func f(a, b int) (value int, error)
    D. func f(a int, b int) (int, int, error)


    5.	关于channel，下面语法错误的是（D）
    A. var ch chan int
    B. ch := make(chan int)
    C. <- ch
    D. ch <-

    6.	关于无缓冲和有缓冲的channel，下面说法错误的是（ABC）
    A. 无缓冲的channel是默认的缓冲为1的channel
    B. 无缓冲的channel和有缓冲的channel都是同步的
    C. 无缓冲的channel和有缓冲的channel都是非同步的
    D. 无缓冲的channel是同步的，而有缓冲的channel是非同步的

    7.	关于接口，下面说法错误的是（）
    A. 只要两个接口拥有相同的方法列表（次序不同不要紧），那么它们就是等价的，可以相互赋值
    B. 如果接口A的方法列表是接口B的方法列表的子集，那么接口B可以赋值给接口A
    C. 接口查询是否成功，要在运行期才能够确定
    D. 接口赋值是否可行，要在运行期才能够确定

    8.	假设x已声明y未声明，下面语句正确的是（BC）
    A. x, _ := f()
    B. x, _ = f()
    C. x, y := f()
    D. x, y = f()

    二、	代码解析题
    1.	执行以下代码将打印什么？
    package main

    import (
            "fmt"
    )

    func main() {
            s1 := []int{1, 2, 3}
            s2 := make([]int, 3)
            s2 = append(s2, s1...)
            s3 := s1[1:]
            s3 = append(s3, 4)

            for _, v := range s2 {
                    v += 10
            }

            for i := range s2 {
                    s2[i] += 10
            }
            fmt.Println(s2)

            for _, v := range s3 {
                    v += 10
            }

            for i := range s3 {
                    s3[i] += 10
            }
            fmt.Println(s3)
    }
    [10 10 10 11 12 13]
    [12 13 14]

    2.	执行以下代码将打印什么？
    package main

    func f1() {
            defer println("f1-begin")
            f2()
            defer println("f1-end")
    }

    func f2() {
            defer println("f2-begin")
            f3()
            defer println("f2-end")
    }

    func f3() {
            defer println("f3-begin")
            panic(0)
            defer println("f3-end")
    }

    func main() {
            f1()
    }


    3.	解释为什么下面的代码无法编译和修复它。
    package main

    type S struct {
            name string
    }

    func main() {
            m := map[string]S{"x": S{"one"}}
            m["x"].name = "two"
    }

    4.	请修改以下代码以使输出结果按升序排序
    package main

    import (
            "fmt"
    )

    type S struct {
            v int
    }

    func main() {
            s := []S{
            {1}, {3}, {5}, {2}
            }
            }
            // A
            fmt.Printf("%#v", s)
    }

    5.	以下go程序的输出结果是什么？
    // A/a1.go
    package A
    func init() {
        println("a1")
    }
    var A1 = ""

    // A/a2.go
    package A
    func init() {
            println("a2")
    }
    var A2 = ""


    // B/b1.go
    package B
    func init() {
            println("b1")
    }
    var B1 = ""


    // B/b2.go
    package B
    import "github.com/test/A"
    func init() {
            println("b2")
    }
    func f() {
            _ = A.A2
    }
    var B2 = ""


    // C/main.go
    package main
    import (
            "github.com/test/B"
    )
    func main() {
            _ = B.B2
    }


    6.	执行以下代码将打印什么？
    package main

    import (
            "context"
            "fmt"
            "time"
    )

    func main() {
            timeout := 3 * time.Second
            ctx, cancel := context.WithTimeout(context.Background(), timeout)
            defer cancel()

            select {
            case <-time.After(1 * time.Second):
                    fmt.Println("waited for 1 sec")
            case <-time.After(2 * time.Second):
                    fmt.Println("waited for 2 sec")
            case <-time.After(3 * time.Second):
                    fmt.Println("waited for 3 sec")
            case <-ctx.Done():
                    fmt.Println(ctx.Err())
            }
    }


    三、	编程题
    1.	程序设计：生产者ProducerA和ProducerB每隔2秒生成一个整数，每次加1，消费者Comsumer不停获取两个生产者生成的数据，并且打印出来
```
