
# 网络IO模型

阻塞/非阻塞&&同步/异步
是针对IO请求的两个阶段来说的：即等待资源阶段和使用资源阶段


## 阻塞/非阻塞----等待IO资源（wait for data)

比如等待网络传输数据可用的过程

- 阻塞。

指的是在数据不可用时I/O请求一直阻塞，直到数据返回；

- 非阻塞

指的是数据不可用时I/O请求立即返回，直到被通知资源可用为止。



## 同步/异步----使用IO资源（copy data from kernel to user）

比如从网络上接收到数据，并且拷贝到应用程序的缓冲区里面

- 同步。

指的是I/O请求在读取或者写入数据时会阻塞，直到读取或者写入数据完成；

- 异步

指的是I/O请求在读取或者写入数据时立即返回，
当操作系统处理完成I/O请求并且将数据拷贝到用户提供的缓冲区后，
再通知应用I/O请求执行完成。

## 五种IO模型

- 同步阻塞I/O（blocking IO）

![io_blocking](architecture/img/io_blocking.png)

一直等着（等待资源）水烧开，然后倒水（使用资源）

Linux默认情况下所有的socket都是blocking；
当用户进程调用了recvfrom这个系统调用，

wait for data:

kernel就开始了IO的第一个阶段：准备数据（对于网络IO来说，很多时候数据在一开始还没有到达。

copy data from kernel to user:

当kernel一直等到数据准备好了，它就会将数据从kernel中拷贝到用户内存，然后kernel返回结果，用户进程才解除block的状态，重新运行起来。

- 同步非阻塞I/O

![io_blocking](architecture/img/io_noblocking.png)

在烧水的时候躺在沙发上看会儿电视（不再时时刻刻等待资源），但是还是要时不时地去看看水开了没有，一旦水开了，马上去倒水（使用资源）

- 同步多路I/O复用

![io_blocking](architecture/img/io_multiplexing.png)

同时烧好多壶水，那你就在看电视的间隙去看看哪壶水开了（等待多个资源），
哪一壶开了就先倒哪一壶，这样就加快了烧水的速度，这就是同步多路 I/O 复用

select/epoll的优势并不是对于单个连接能处理得更快，
而是在于能处理更多的连接。

- 信号驱动I/O

![io_blocking](architecture/img/io_signal.png)

给水壶加一个报警器（信号），只要水开了就马上去倒水，这就是信号驱动 I/O

- 异步 I/O

![io_blocking](architecture/img/io_asynchronous.png)

发明一个智能水壶，在水烧好后自动就可以把水倒好，这就是异步 I/O



# 总结

![io_blocking](architecture/img/io_5_all.png)

# IO多路复用：select、poll、epoll详解

I/O多路复用就是通过一种机制，一个进程可以监视多个描述符，
一旦某个描述符就绪（一般是读就绪或者写就绪），
能够通知程序进行相应的读写操作

## select

`int select (int n, fd_set *readfds, fd_set *writefds, fd_set *exceptfds, struct timeval *timeout);`

调用后select函数会阻塞，直到有描述副就绪（有数据 可读、可写、或者有except），或者超时（timeout指定等待时间，如果立即返回设为null即可），函数返回。当select函数返回后，可以 通过遍历fdset，来找到就绪的描述符。

优点：
几乎在所有的平台上支持

缺点：单个进程能够监视的文件描述符的数量存在最大限制，在Linux上一般为1024
## poll

`int poll (struct pollfd *fds, unsigned int nfds, int timeout);`

poll返回后，需要轮询pollfd来获取就绪的描述符。

select和poll都需要在返回后，通过遍历文件描述符来获取已经就绪的socket。
事实上，同时连接的大量客户端在一时刻可能只有很少的处于就绪状态，
因此随着监视的描述符数量的增长，其效率也会线性下降。

## epoll

epoll是在2.6内核中提出的，是之前的select和poll的增强版本



# DMA缓冲区

1. 内核分配一个主内存地址段（DMA缓冲区)，网卡设备可以在DMA缓冲区中读写数据
2. 当来了一个网络包，网卡将网络包写入DMA缓冲区，写完后通知CPU产生硬中断
3. 硬中断处理程序锁定当前DMA缓冲区，然后将网络包拷贝到另一块内存区，清空并解锁当前DMA缓冲区，
然后通知软中断去处理网络包。
-----
当发送数据包时，与上述相反。链路层将数据包封装完毕后，放入网卡的DMA缓冲区，并调用系统硬中断，通知网卡从缓冲区读取并发送数据。

我们通常使用带宽、吞吐量、延时等指标，来衡量网络的性能；相应的，你可以用 ifconfig、netstat、ss、sar、ping 等工具，来查看这些网络的性能指标。



