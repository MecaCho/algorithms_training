


1. select是随机的还是顺序的?     
select会随机选择一个可用通道做收发操作

2. Go语言局部变量分配在栈还是堆？    
Go语言编译器会自动决定把一个变量放在栈还是放在堆，编译器会做逃逸分析，
当发现变量的作用域没有跑出函数范围，就可以在栈上，反之则必须分配在堆。
一个函数内局部变量，不管是不是动态new出来的，它会被分配在堆还是栈，是由编译器做逃逸分析之后做出的决定。

3. 简述一下你对Go垃圾回收机制的理解?    
v1.1 STW    
v1.3 Mark STW, Sweep 并行    
v1.5 三色标记法    
v1.8 hybrid write barrier(混合写屏障：优化STW)    

4. 简述一下golang的协程调度原理?    
M(machine): 代表着真正的执行计算资源，可以认为它就是os thread（系统线程）。
P(processor): 表示逻辑processor，是线程M的执行的上下文。
G(goroutine): 调度系统的最基本单位goroutine，存储了goroutine的执行stack信息、goroutine状态以及goroutine的任务函数等。


5. 介绍下 golang 的 runtime 机制?    

Runtime 负责管理任务调度，垃圾收集及运行环境。同时，Go提供了一些高级的功能，
如goroutine, channel, 以及Garbage collection。这些高级功能需要一个runtime的支持. 
runtime和用户编译后的代码被linker静态链接起来，形成一个可执行文件。
这个文件从操作系统角度来说是一个user space的独立的可执行文件。 

从运行的角度来说，这个文件由2部分组成，一部分是用户的代码，另一部分就是runtime。
runtime通过接口函数调用来管理goroutine, channel及其他一些高级的功能。
从用户代码发起的调用操作系统API的调用都会被runtime拦截并处理。

Go runtime的一个重要的组成部分是goroutine scheduler。负责追踪，调度每个goroutine运行，
实际上是从应用程序的process所属的thread pool中分配一个thread来执行这个goroutine。
因此，和java虚拟机中的Java thread和OS thread映射概念类似，每个goroutine只有分配到一个OS thread才能运行。

6. 如何获取 go 程序运行时的协程数量, gc 时间, 对象数, 堆栈信息?

调用接口 runtime.ReadMemStats 可以获取以上所有信息, 注意: 调用此接口会触发 STW(Stop The World)

参考: https://golang.org/pkg/runtime/#ReadMemStats

如果需要打入到日志系统, 可以使用 go 封装好的包, 输出 json 格式. 参考:

https://golang.org/pkg/expvar/
http://blog.studygolang.com/2017/06/expvar-in-action/
更深入的用法就是将得到的运行时数据导入到 ES 内部, 然后使用 Kibana 做 golang 的运行时监控, 可以实时获取到运行的信息(堆栈, 对象数, gc 时间, goroutine, 总内存使用等等), 具体信息可以看 ReadMemStats 的那个结构体

7. 介绍下你平时都是怎么调试 golang 的 bug 以及性能问题的?   
 
panic 调用栈    
pprof    
火焰图(配合压测)        
使用go run -race 或者 go build -race 来进行竞争检测        
查看系统 磁盘IO/网络IO/内存占用/CPU 占用(配合压测)        


8. 简单介绍下 golang 中 make 和 new 的区别    
- make:

make也是用于内存分配的，但是和new不同，它只用于chan、map以及切片的内存创建，
而且它返回的类型就是这三个类型本身，而不是他们的指针类型，因为这三种类型就是引用类型，所以就没有必要返回他们的指针了。
注意，因为这三种类型是引用类型，所以必须得初始化，但是不是置为零值，这个和new是不一样的。
```
func make(t Type, size ...IntegerType) Type
```

- new:

它只接受一个参数，这个参数是一个类型，分配好内存后，返回一个指向该类型内存地址的指针。
同时请注意它同时把分配的内存置为零，也就是类型的零值。

```
// The new built-in function allocates memory. The first argument is a type,
// not a value, and the value returned is a pointer to a newly
// allocated zero value of that type.
func new(Type) *Type
```

二者都是内存的分配（堆上），但是make只用于slice、map以及channel的初始化（非零值；
而new用于类型的内存分配，并且内存置为零。所以在我们编写程序的时候，就可以根据自己的需要很好的选择了。

make返回的还是这三个引用类型本身；而new返回的是指向类型的指针。


9. 简单说下Golang逃逸分析



10. 无缓冲 Chan 的发送和接收是否同步?

channel无缓冲时，发送阻塞直到数据被接收，接收阻塞直到读到数据。
channel有缓冲时，当缓冲满时发送阻塞，当缓冲空时接收阻塞。

11. Golang通过哪几种方式来实现并发控制,如何优雅的退出goroutine?       
 
1.chan 通过无缓冲通道来实现多 goroutine 并发控制    
2.通过sync包中的WaitGroup 实现并发控制    

退出：        
使用for-range退出    
使用,ok退出    
使用退出通道退出    

12. Golang的interface的特性和技巧,举例一些优雅的实现?

1.空接口（empty interface）    

空接口比较特殊，他不包含任何方法,但是他又可以表示任何类型

golang的所有基础类都实现了空接口，所有我们可以用[]interface表示结构不同的数组

2.接口嵌套接口

3.类型的选择与断言


13. Golang的方法集?    


14. Golang的GMP模型?

M(Work Thread) -- 表示操作系统的线程,它是被操作系统管理的线程,与POSIX中的标准线程非常类似

G(Goroutine) -- 表示Goroutine,每一个Goroutine都包含堆栈,指令指针和其他用于调度的重要信息

P(Processor) -- 表示调度的上下文,它可以被看做一个运行于线程M上的本地调度器

三者关系:

每一个运行的M都必须绑定一个P,线程M创建后会去检查并执行G(goroutine)对象
每一个P保存着一个协程G的队列
除了每个P自身保存的G的队列外,调度器还拥有一个全局的G队列
M从队列中提取G,并执行
P的个数就是GOMAXPROCS(最大256),启动时固定的,一般不修改
M的个数和P的个数不一定一样多(会有休眠的M或P不绑定M) (最大10000)
P是用一个全局数组(255)来保存的,并且维护着一个全局的P空闲链表


15. 用信道实现主程等待协程2s,如果超过2s,主程直接结束(不用sleep)?

```
func main() {
    start := time.Now()
    wait := make(chan int,1)
    go func() {
        fmt.Println("做点东西")
        time.Sleep(1*time.Second)
        wait<-2
    }()
    fmt.Println("这里是主程序")
    select {
    case nums:= <-wait:
        fmt.Println(nums)
    case <-time.After(2*time.Second):
        fmt.Println("2秒后")
    }
    fmt.Println(time.Since(start))
}
```

16.继承多态

“组合优于继承”


关于接口，下面说法正确的是（）
A. 只要两个接口拥有相同的方法列表（次序不同不要紧），那么它们就是等价的，可以相互赋值

B. 如果接口A的方法列表是接口B的方法列表的子集，那么接口B可以赋值给接口A

C. 接口查询是否成功，要在运行期才能够确定

D. 接口赋值是否可行，要在运行期才能够确定

 A B C
 
 
关于GetPodAction定义，下面赋值正确的是（）
type Fragment interface {
        Exec(transInfo *TransInfo) error
}
type GetPodAction struct {
}
func (g GetPodAction) Exec(transInfo *TransInfo) error {
        ...
        return nil
}
Copy
A. var fragment Fragment = new(GetPodAction)

B. var fragment Fragment = GetPodAction

C. var fragment Fragment = &GetPodAction{}

D. var fragment Fragment = GetPodAction{}

还是方法集的问题..

答案: A C D
