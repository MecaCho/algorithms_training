# 进程&线程

task_struct就是 Linux 内核对于一个进程的描述，也可以称为"进程描述符"

```
struct task_struct {
    // 进程状态
    long              state;
    // 虚拟内存结构体
    struct mm_struct  *mm;
    // 进程号
    pid_t              pid;
    // 指向父进程的指针
    struct task_struct __rcu  *parent;
    // 子进程列表
    struct list_head        children;
    // 存放文件系统信息的指针
    struct fs_struct        *fs;
    // 一个数组，包含该进程打开的文件指针
    struct files_struct        *files;
};
```

mm指向的是进程的虚拟内存，也就是载入资源和可执行文件的地方；
files指针指向一个数组，这个数组里装着所有该进程打开的文件的指针----文件描述符

无论线程还是进程，都是用task_struct结构表示的，唯一的区别就是共享的数据区域不同。

# 文件描述符

文件描述符在形式上是一个非负整数。
实际上，它是一个指针(索引)，指向内核为每一个进程所维护的该进程打开文件的记录表。
当程序打开一个现有文件或者创建一个新文件时，内核向进程返回一个文件描述符。
在程序设计中，一些涉及底层的程序编写往往会围绕着文件描述符展开。
文件描述符这一概念往往只适用于UNIX、Linux这样的操作系统。

每个Unix进程（除了可能的守护进程）应均有三个标准的POSIX文件描述符，对应于三个标准流：

0	Standard input	STDIN_FILENO	stdin

1	Standard output	STDOUT_FILENO	stdout

2	Standard error	STDERR_FILENO	stderr

一个进程会从files[0]读取输入，将输出写入files[1]，将错误信息写入files[2]

每个进程被创建时，files的前三位被填入默认值，分别指向标准输入流、标准输出流、标准错误流。
我们常说的「文件描述符」就是指这个文件指针数组的索引，
所以程序的文件描述符默认情况下 0 是输入，1 是输出，2 是错误。

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

以烧水（wait for data）----喝水（copy data from kernel to user）为例

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

用户进程发出read操作时，如果kernel中的数据还没有准备好，
那么它并不会block用户进程，而是立刻返回一个error;
用户进程需要不断的主动询问kernel数据好了没有

- 同步多路I/O复用

![io_blocking](architecture/img/io_multiplexing.png)

同时烧好多壶水，那你就在看电视的间隙去看看哪壶水开了（等待多个资源），
哪一壶开了就先倒哪一壶，这样就加快了烧水的速度，这就是同步多路 I/O 复用

select/epoll的优势并不是对于单个连接能处理得更快，
而是在于能处理更多的连接。

单个process就可以同时处理多个网络连接的IO。
它的基本原理就是select，poll，epoll这个function会不断的轮询所负责的所有socket，
当某个socket有数据到达了，就通知用户进程

I/O 多路复用的特点是通过一种机制一个进程能同时等待多个文件描述符，
而这些文件描述符（套接字描述符）其中的任意一个进入读就绪状态，
select()函数就可以返回。

- 信号驱动I/O

![io_blocking](architecture/img/io_signal.png)

给水壶加一个报警器（信号），只要水开了就马上去倒水，这就是信号驱动 I/O

- 异步 I/O

![io_blocking](architecture/img/io_asynchronous.png)

发明一个智能水壶，在水烧好后自动就可以把水倒好，这就是异步 I/O

用户进程发起read操作之后，立刻就可以开始去做其它的事,
kernel完成后会给用户进程发送一个signal，告诉它read操作完成了

# 总结

![io_blocking](architecture/img/io_5_all.png)

# IO多路复用：select、poll、epoll详解

I/O多路复用就是通过一种机制，一个进程可以监视多个描述符，
一旦某个描述符就绪（一般是读就绪或者写就绪），
能够通知程序进行相应的读写操作

## select

`int select (int n, fd_set *readfds, fd_set *writefds, fd_set *exceptfds, struct timeval *timeout);`

调用后select函数会阻塞，直到有描述副就绪（有数据可读、可写、或者有except），
或者超时（timeout指定等待时间，如果立即返回设为null即可），函数返回。
当select函数返回后，可以 通过遍历fdset，来找到就绪的描述符。

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

epoll使用一个文件描述符管理多个描述符，将用户关系的文件描述符的事件存放到内核的一个事件表中，
这样在用户空间和内核空间的copy只需一次。

```
int epoll_create(int size)；//创建一个epoll的句柄，size用来告诉内核这个监听的数目一共有多大
int epoll_ctl(int epfd, int op, int fd, struct epoll_event *event)；
int epoll_wait(int epfd, struct epoll_event * events, int maxevents, int timeout);
```

int epoll_create(int size);
创建一个epoll的句柄，size用来告诉内核这个监听的数目一共有多大

当创建好epoll句柄后，它就会占用一个fd值，在linux下查看/proc/进程id/fd/


int epoll_ctl(int epfd, int op, int fd, struct epoll_event *event)；
对指定描述符fd执行op操作:
添加EPOLL_CTL_ADD，删除EPOLL_CTL_DEL，修改EPOLL_CTL_MOD。
分别添加、删除和修改对fd的监听事件


int epoll_wait(int epfd, struct epoll_event * events, int maxevents, int timeout);
等待epfd上的io事件，最多返回maxevents个事件。

epoll_pwait(4, [], 128, 0, NULL, 0)     = 0

# 

redis
nginx
netty

strace -ff -o ./xxxx python server



# DMA缓冲区

1. 内核分配一个主内存地址段（DMA缓冲区)，网卡设备可以在DMA缓冲区中读写数据
2. 当来了一个网络包，网卡将网络包写入DMA缓冲区，写完后通知CPU产生硬中断
3. 硬中断处理程序锁定当前DMA缓冲区，然后将网络包拷贝到另一块内存区，清空并解锁当前DMA缓冲区，
然后通知软中断去处理网络包。
-----
当发送数据包时，与上述相反。链路层将数据包封装完毕后，放入网卡的DMA缓冲区，并调用系统硬中断，通知网卡从缓冲区读取并发送数据。

我们通常使用带宽、吞吐量、延时等指标，来衡量网络的性能；相应的，你可以用 ifconfig、netstat、ss、sar、ping 等工具，来查看这些网络的性能指标。



