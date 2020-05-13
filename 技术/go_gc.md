
# go内部内存结构

# 栈

栈存储区，每个Goroutine又一个栈，存储了静态数据，包括函数栈帧、静态结构、原生类型值和指向动态结构的指针。


# Go内存使用----栈与堆



# 实践

## 打开 GC ⽇日志

只要在程序执⾏之前加上环境变量GODEBUG=gctrace=1
如:GODEBUG=gctrace=1 go test -bench=.
GODEBUG=gctrace=1 go run main.go

日志详细信息参考: https://godoc.org/runtime


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

