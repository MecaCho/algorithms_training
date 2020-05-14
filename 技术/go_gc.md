
# go内部内存结构

# 栈

栈存储区，每个Goroutine有一个栈，存储了静态数据，包括函数栈帧、静态结构、原生类型值和指向动态结构的指针。

# Go内存使用----栈与堆

## 栈

栈由OS自动管理，go不用管

## 堆

- 堆不是由OS管理    
- 具有最大内存空间
- 保存动态数据    
可能会成倍增长，导致程序会随着时间耗尽内存    

随着时间流逝，内存空间变得支离破碎---->GC

# Go内存管理

1。需要内存时自动分配     
2。不需要时GC     
runtime完成，开发人员不必处理

## 1。内存分配

thread local cache：    
使用线程本地缓存来加速小对象分配

维护scan/noscan的span来加速GC

### 根据对象大小决定对象的分配过程：

### Tiny-微小对象，size<16B

mcache微小分配器分配小雨16B的对象

### 小对象， 16B<size<32KB

分配在G运行所在的P的mcache的对应的mspan size class上

### 大对象，>32KB

直接分配在mheap上，如果mheap没有足够的空间则从OS分配一组新的页

## 2。GC

- 释放孤儿对象（不再被栈直接或间接引用）使用的内存    
- Go使用非分代的、并发的、基于三色标记和清除的垃圾回收器（1.12以后） 

### GC触发条件

自动垃圾回收的触发条件有两个：

- 超过内存大小阈值     
- 达到定时时间    
阈值是由一个gcpercent的变量控制的,当新分配的内存占已在使用中的内存的比例超过gcprecent时就会触发。比如一次回收完毕后，内存的使用量为5M，那么下次回收的时机则是内存分配达到10M的时候。也就是说，并不是内存分配越多，垃圾回收频率越高。
如果一直达不到内存大小的阈值呢？这个时候GC就会被定时时间触发，比如一直达不到10M，那就定时（默认2min触发一次）触发一次GC保证资源的回收。

# 实践

## 打开 GC ⽇日志

只要在程序执⾏之前加上环境变量GODEBUG=gctrace=1    
如:GODEBUG=gctrace=1 go test -bench=.    
GODEBUG=gctrace=1 go run main.go

日志详细信息参考: https://godoc.org/runtime     
   gc次数  时间  gc时间占的百分比                                       堆大小--gc开始-gc结束--现存   所有堆大小   用到的processor
gc 2925 @1.879s 3%: 0.002+0.12+0.011 ms clock, 0.038+0.054/0.075/0.12+0.18 ms cpu, 4->4->0 MB, 5 MB goal, 16 P
scvg: 0 MB released    
scvg: inuse: 2, idle: 61, sys: 63, released: 58, consumed: 5 (MB)


## go tool trace 

普通程序输出 trace 信息:

```
package main
import (
"os"
"runtime/trace"
)
func main() {
f, err := os.Create("trace.out") if err != nil {
panic(err) }
defer f.Close()
err = trace.Start(f) if err != nil {
panic(err) }
defer trace.Stop()
     // Your program here
}
```

测试程序输出 trace 信息 :

```
go test -trace trace.out
```


可视化 trace 信息:

```
go tool trace trace.out
```

