


# goconvey

是一款针对Golang的测试框架，可以管理和运行测试用例，同时提供了丰富的断言函数，并支持很多 Web 界面特性。

GoConvey 网站 : http://smartystreets.github.io/goconvey/

GoConvey 是个相当不错的 Go 测试工具，支持 go test。可直接在终端窗口和浏览器上使用。

特点：

直接与 go test 集成
巨大的回归测试套件
可读性强的色彩控制台输出
完全自动化的 Web UI
测试代码生成器
桌面提醒（可选）
自动在终端中运行自动测试脚本
可立即在 Sublime Text 中打开测试问题对应的代码行 (some assembly required)


# GoStub


# GoMock



---
layout: post
title:  "给go代码工程配置代码静态检查及gometalinte"
date:   2017-12-15 22:42:59
categories: Go
---

# go code check and Test

## code static check

### go lint

golint是类似javascript中的jslint的工具，主要功能就是检测代码中不规范的地方。golint用于检测go代码。

- golint 会检测的方面：

1.变量名规范

2.变量的声明，像var str string = "test"，会有警告，应该var str = "test"

3.大小写问题，大写导出包的要有注释

4.x += 1 应该 x++

etc.

such as:
```
golint ./pkg/...           
pkg/model/env.go:66:7: exported const CreateProject should have comment or be unexported
```

how to use:

```
#export GOPROXY=https://goproxy.io
#go get -u golang.org/x/lint/golint
#GOLINT_PATH=$(go list -f {{.Target}} golang.org/x/lint/golint)
#cp $GOLINT_PATH /usr/local/bin/
cd go-project
rm -rf vendor
golint ./... > golint.report
```


### go vet

Vet examines Go source code and reports suspicious constructs, such as Printf calls whose arguments do not align with the format string.
Vet uses heuristics that do not guarantee all reports are genuine problems, but it can find errors not caught by the compilers.
检查Go语言源代码并且报告可疑的代码编写问题。
比如，在调用 Printf 函数时没有传入格式化字符串，以及某些不标准的方法签名，等等。
该命令使用试探性的手法检查错误，因此并不能保证报告的问题确实需要解决。
但是，它确实能够找到一些编译器没有捕捉到的错误。

例如：

```
go vet ./pkg/...
# go-project/pkg/common
pkg/common/common_request.go:59:2: Infof format %s has arg 1000 of wrong type int
```

how to use:

```
go vet ./...
```

### go cov

检查代码测试覆盖率

```
go test -coverprofile=cover.out && go tool cover -html=cover.out
```

### gocyclo

检查圈复杂度


```
gocyclo -top 20 ./pkg
```

### gometalinter

- 在Jenkins代码静态检查门禁中使用gometalinter

Jenkins 从 Gitlab 上拉取最新代码

编译项目，下载  gometalinter ：https://github.com/alecthomas/gometalinter

执行 gometalinter 命令，进行源码分析，生成 xml 格式的 checkstyle 报告

在 Jenkins 上查看 checkstyle 报告

```
go get github.com/alecthomas/gometalinter
gometalinter --install --update
gometalinter ./pkg/...
```


## 基准测试+功能测试+单元测试覆盖率

go test -v -cover -short -bench .

```
TEMP file :  /var/folders/j4/11rjs5s96cb_1dywr9bgc4xh0000gn/T/
2019/07/22 19:47:35 This is NEW version : 1.0.0
=== RUN   TestGetVersion
v1
--- PASS: TestGetVersion (0.00s)
=== RUN   TestLongTimeTestCase
--- SKIP: TestLongTimeTestCase (0.00s)
	main_test.go:30: Skip test when test in short mode.
=== RUN   TestParallel1
=== RUN   TestParallel2
--- PASS: TestParallel1 (1.00s)
	main_test.go:41: test parallel 1
--- PASS: TestParallel2 (1.00s)
	main_test.go:50: test parallel 2
goos: darwin
goarch: amd64
pkg: app_sample
BenchmarkGetVersion-4      	2000000000	         0.43 ns/op
BenchmarkUnmarshalJSON-4   	  200000	      9842 ns/op
BenchmarkDecodeJSON-4      	  200000	      8511 ns/op
PASS
coverage: 31.8% of statements
ok  	app_sample	5.808s
```

## 只运行基准测试

go test -run x -bench .

```
TEMP file :  /var/folders/j4/11rjs5s96cb_1dywr9bgc4xh0000gn/T/
2019/07/22 19:19:54 This is NEW version : 1.0.0
goos: darwin
goarch: amd64
pkg: app_sample
BenchmarkGetVersion-4   	2000000000	         0.34 ns/op
PASS
ok  	app_sample	0.731s

```

## 性能测试

```
go test -bench=Parallel -blockprofile=prof.block

```

### Race Detector(竞态分析）

Go程序中竞态就是当多个goroutine并发 访问某共享数据且未使用同步机制时，且至少一个goroutine进行了写操作

```
go test -v -race
1、使用channel
2、使用Mutex
3、使用atomic
```



### CPU Profiling

```
go test -v -run=^$ -bench=.
go test -v -run=^$ -bench=^Benchmark$ -benchtime=2s -cpuprofile=prof.cpu
go tool pprof step2.test prof.cpu
(pprof) top
(pprof) top –cum
```

### Mem Profiling

```
go test -v -run=^$ -bench=^BenchmarkHi$ -benchtime=2s -memprofile=prof.mem
go tool pprof –alloc_space step3.test prof.mem
(pprof) top
(pprof) top -cum
```

### Benchcmp

```
golang.org/x/tools中有一个工具：benchcmp，可以给出两次bench的结果对比。

github.com/golang/tools是golang.org/x/tools的一个镜像。安装benchcmp步骤：

1、go get -u github.com/golang/tools
2、mkdir -p $GOPATH/src/golang.org/x
3、mv $GOPATH/src/github.com/golang/tools $GOPATH/src/golang.org/x
4、go install golang.org/x/tools/cmd/benchcmp

go test -bench=. -memprofile=prof.mem | tee mem.3
go test -bench=. -memprofile=prof.mem | tee mem.4

benchcmp step3/mem.3 step4/mem.4

```

## api压力测试

### wrk

#### 安装：

- Mac
```
brew install wrk
```

- ubuntu

```
sudo apt-get install build-essential libssl-dev git
git clone http://luajit.org/git/luajit-2.0.git
cd luajit
make && sudo make install

git clone https://github.com/wg/wrk.git
cd wrk

make
# move the executable to somewhere in your PATH
sudo cp wrk /usr/local/bin
```

#### 测试

用4个线程来模拟1000个并发连接，整个测试持续30秒，连接超时30秒，打印出请求的延迟统计信息。

```
wrk -t4 -c1000 -d30s -T30s --latency http://127.0.0.1:8092/v1/projects

```

结果：

```
Running 30s test @ http://127.0.0.1:8092/v1/projects
  4 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     1.36ms    2.17ms  32.16ms   83.98%
    Req/Sec     4.76k     4.27k   13.63k    48.25%
  Latency Distribution
     50%  176.00us
     75%    1.90ms
     90%    4.81ms
     99%    8.39ms
  568862 requests in 30.04s, 64.56MB read
  Non-2xx or 3xx responses: 568862
Requests/sec:  18934.28
Transfer/sec:      2.15MB
```

使用脚本

wrk -t4 -c100 -d30s -T30s --script=post.lua --latency
```
-- example HTTP POST script which demonstrates setting the
-- HTTP method, body, and adding a header

wrk.method = "POST"
wrk.body   = "foo=bar&baz=quux"
wrk.headers["Content-Type"] = "application/x-www-form-urlencoded"
```


