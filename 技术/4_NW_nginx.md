

# Nginx 是如何实现高并发的?

异步，非阻塞，使用了epoll 和大量的底层代码优化。

nginx采用一个master进程，多个woker进程的模式:    
master进程主要负责收集、分发请求。每当一个请求过来时，master就拉起一个worker进程负责处理这个请求。
同时master进程也负责监控woker的状态，保证高可靠性
woker进程一般设置为跟cpu核心数一致。nginx的woker进程在同一时间可以处理的请求数只受内存限制，可以处理多个请求。

# 为什么 Nginx 不使用多线程?    

Apache: 创建多个进程或线程，而每个进程或线程都会为其分配 cpu 和内存(线程要比进程小的多，所以worker支持比perfork高的并发)，并发过大会耗光服务器资源。

Nginx: 采用单线程来异步非阻塞处理请求(管理员可以配置Nginx主进程的工作进程的数量)(epoll)，不会为每个请求分配cpu和内存资源，节省了大量资源，同时也减少了大量的CPU的上下文切换。所以才使得Nginx支持更高的并发。


# Nginx常见的优化配置有哪些?

1.调整worker_processes

指Nginx要生成的worker数量,最佳实践是每个CPU运行1个工作进程。

了解系统中的CPU核心数，输入:    
```
$ grep processor / proc / cpuinfo | wc -l

```

2.最大化worker_connectionsNginx

Web服务器可以同时提供服务的客户端数。与worker_processes结合使用时，获得每秒可以服务的最大客户端数

最大客户端数/秒=工作进程*工作者连接数为了最大化Nginx的全部潜力，应将工作者连接设置为核心一次可以运行的允许的最大进程数1024。

3.启用Gzip压缩

压缩文件大小，减少了客户端http的传输带宽，因此提高了页面加载速度

4.为静态文件启用缓存

为静态文件启用缓存，以减少带宽并提高性能，可以添加下面的命令，限定计算机缓存网页的静态文件

5.Timeouts

keepalive连接减少了打开和关闭连接所需的CPU和网络开销

6.禁用access_logs

访问日志记录，它记录每个nginx请求，因此消耗了大量CPU资源，从而降低了nginx性能。

完全禁用访问日志记录
```
access_log off;

```


如果必须具有访问日志记录，则启用访问日志缓冲
```
access_log /var/log/nginx/access.log= 16k

```


