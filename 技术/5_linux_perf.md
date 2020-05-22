



# 性能问题排查思路    


有监控的情况下，首先去看看监控大盘，看看有没有异常报警，如果初期还没有监控的情况我会按照下面步骤去看看系统层面有没有异常    
1、我首先会去看看系统的平均负载，使用top或者htop命令查看,平均负载体现的是系统的一个整体情况，他应该是cpu、内存、磁盘性能的一个综合，一般是平均负载的值大于机器cpu的核数，这时候说明机器资源已经紧张了
2、平均负载高了以后，接下来就要看看具体是什么资源导致，我首先会在top中看cpu每个核的使用情况，如果占比很高，那瓶颈应该是cpu,接下来就要看看是什么进程导致的
3、如果cpu没有问题，那接下来我会去看内存，首先是用free去查看内存的是用情况，但不直接看他剩余了多少，还要结合看看cache和buffer，然后再看看具体是什么进程占用了过高的内存，我也是是用top去排序
4、内存没有问题的话就要去看磁盘了，磁盘我用iostat去查看，我遇到的磁盘问题比较少
5、还有就是带宽问题，一般会用iftop去查看流量情况，看看流量是否超过的机器给定的带宽
6、涉及到具体应用的话，就要根据具体应用的设定参数来查看，比如连接数是否查过设定值等
7、如果系统层各个指标查下来都没有发现异常，那么就要考虑外部系统了，比如数据库、缓存、存储等

# 怎么理解“平均负载”？

```
uptime
15:02  up 9 days, 15:35, 12 users, load averages: 2.09 2.05 2.01


02:34:03              //当前时间
up 2 days, 20:14      //系统运行时间
1 user                //正在登录用户数
最后三个数字呢，依次则是过去 1 分钟、5 分钟、15 分钟的平均负载（Load Average）

man uptime
UPTIME(1)                 BSD General Commands Manual                UPTIME(1)

NAME
     uptime -- show how long system has been running

SYNOPSIS
     uptime

DESCRIPTION
     The uptime utility displays the current time, the length of time the system has been up, the number of users, and the load average
     of the system over the last 1, 5, and 15 minutes.

SEE ALSO
     w(1)

HISTORY
     The uptime command appeared in 3.0BSD.

BSD                             April 18, 1994                             BSD
```

平均负载是指单位时间内，系统处于可运行状态和不可中断状态的平均进程数，也就是平均活跃进程数，它和 CPU 使用率并没有直接关系

- 可运行状态的进程:       
 
是指正在使用 CPU 或者正在等待 CPU 的进程，也就是我们常用 ps 命令看到的，
处于 R 状态（Running 或 Runnable）的进程。

- 不可中断状态的进程:    

则是正处于内核态关键流程中的进程，并且这些流程是不可打断的，比如最常见的是等待硬件设备的 I/O 响应，
也就是我们在 ps 命令中看到的 D 状态（Uninterruptible Sleep，也称为 Disk Sleep）的进程。

比如，当一个进程向磁盘读写数据时，为了保证数据的一致性，在得到磁盘回复前，它是不能被其他进程或者中断打断的，这个时候的进程就处于不可中断状态。
如果此时的进程被打断了，就容易出现磁盘数据与进程数据不一致的问题。

不可中断状态实际上是系统对进程和硬件设备的一种保护机制。

```

# 关于grep和wc的用法请查询它们的手册或者网络搜索
$ grep 'model name' /proc/cpuinfo | wc -l
2
```

- 平均负载为多少时合理:    

平均负载最理想的情况是等于 CPU 个数。

平均的是活跃进程数，那么最理想的，就是每个 CPU 上都刚好运行着一个进程，这样每个 CPU 都得到了充分利用。

- 在实际生产环境中，平均负载多高时，需要我们重点关注呢？

当平均负载高于 CPU 数量 70% 的时候，你就应该分析排查负载高的问题了。一旦负载过高，就可能导致进程响应变慢，进而影响服务的正常功能。


- 平均负载与 CPU 使用率的关系？

平均负载包括正在使用 CPU 的进程，还包括等待 CPU 和等待 I/O 的进程。

1。CPU 密集型进程，使用大量 CPU 会导致平均负载升高，此时这两者是一致的；

2。I/O 密集型进程，等待 I/O 也会导致平均负载升高，但 CPU 使用率不一定很高；

3。大量等待 CPU 的进程调度也会导致平均负载升高，此时的 CPU 使用率也会比较高。

## 测试

1。大量进程

模拟的是 8 个进程：

```
$ stress -c 8 --timeout 600
```

平均负载:

```shell script
$ uptime
...,  load average: 7.97, 5.93, 3.02
```

进程的情况:
```
# 间隔5秒后输出一组数据
$ pidstat -u 5 1
```

2.I/O 密集型进程

```shell script
$ stress -i 1 --timeout 600
watch -d uptime
mpstat -P ALL 5 1
pidstat -u 5 1
```

3.CPU 密集型进程

```

$ stress --cpu 1 --timeout 600

# -d 参数表示高亮显示变化的区域
$ watch -d uptime

$ mpstat -P ALL 5

$ pidstat -u 5 1

```

# system call

在用户空间和内核空间之间，有一个叫做Syscall(系统调用, system call)的中间层，是连接用户态和内核态的桥梁。
这样即提高了内核的安全型，也便于移植，只需实现同一套接口即可。
Linux系统，用户空间通过向内核空间发出Syscall，产生软中断，从而让程序陷入内核态，执行相应的操作

系统调用是从一个应用程序到内核的函数调用。
出于安全考虑，它们使用了特定的机制，实际上你只是调用了内核的 API。“ 
系统调用(system call)”这个术语指的是
调用由内核提供的特定功能（比如，系统调用 open()）或者是调用途径。
你也可以简称为：syscall

# CPU 上下文切换是什么意思？

每个任务运行前，CPU 都需要知道任务从哪里加载、又从哪里开始运行，
也就是说，需要系统事先帮它设置好 CPU 寄存器和程序计数器（Program Counter，PC）。

CPU 寄存器，是 CPU 内置的容量小、但速度极快的内存。
而程序计数器，则是用来存储 CPU 正在执行的指令位置、或者即将执行的下一条指令位置。
它们都是 CPU 在运行任何任务前，必须的依赖环境，因此也被叫做 CPU 上下文。

CPU 上下文切换，就是先把前一个任务的 CPU 上下文（也就是 CPU 寄存器和程序计数器）保存起来，
然后加载新任务的上下文到这些寄存器和程序计数器，最后再跳转到程序计数器所指的新位置，运行新任务。

## 任务    

任务就是进程，或者说任务就是线程。是的，进程和线程正是最常见的任务。但是除此之外，还有没有其他的任务呢？

硬件通过触发信号，会导致中断处理程序的调用，也是一种常见的任务。

所以，根据任务的不同，CPU 的上下文切换就可以分为几个不同的场景，也就是进程上下文切换、线程上下文切换以及中断上下文切换。

### 进程上下文切换    

进程既可以在用户空间运行，又可以在内核空间中运行。进程在用户空间运行时，被称为进程的用户态，
而陷入内核空间的时候，被称为进程的内核态。

从用户态到内核态的转变，需要通过系统调用来完成。
比如，当我们查看文件内容时，就需要多次系统调用来完成：
首先调用 open() 打开文件，然后调用 read() 读取文件内容，
并调用 write() 将内容写到标准输出，最后再调用 close() 关闭文件。

系统调用过程通常称为特权模式切换，而不是上下文切换。
但实际上，系统调用过程中，CPU 的上下文切换还是无法避免的。

进程切换时才需要切换上下文，换句话说，只有在进程调度的时候，才需要切换上下文。Linux 为每个 CPU 都维护了一个就绪队列，将活跃进程（即正在运行和正在等待 CPU 的进程）按照优先级和等待 CPU 的时间排序，然后选择最需要 CPU 的进程，也就是优先级最高和等待 CPU 时间最长的进程来运行。

- 进程在什么时候才会被调度到 CPU 上运行呢？

0。进程执行完终止了，它之前使用的 CPU 会释放出来，这个时候再从就绪队列里，拿一个新的进程过来运行。

1。为了保证所有进程可以得到公平调度，CPU 时间被划分为一段段的时间片，这些时间片再被轮流分配给各个进程。这样，当某个进程的时间片耗尽了，就会被系统挂起，切换到其它正在等待 CPU 的进程运行。

2。进程在系统资源不足（比如内存不足）时，要等到资源满足后才可以运行，这个时候进程也会被挂起，并由系统调度其他进程运行。

3。当进程通过睡眠函数 sleep 这样的方法将自己主动挂起时，自然也会重新调度。

4。当有优先级更高的进程运行时，为了保证高优先级进程的运行，当前进程会被挂起，由高优先级进程来运行。

5。发生硬件中断时，CPU 上的进程会被中断挂起，转而执行内核中的中断服务程序。

一旦出现上下文切换的性能问题，它们就是幕后凶手。

### 线程上下文切换

线程是调度的基本单位，而进程则是资源拥有的基本单位。

所谓内核中的任务调度，实际上的调度对象是线程；
而进程只是给线程提供了虚拟内存、全局变量等资源。
所以，对于线程和进程，我们可以这么理解：
- 当进程只有一个线程时，可以认为进程就等于线程。
- 当进程拥有多个线程时，这些线程会共享相同的虚拟内存和全局变量等资源。
这些资源在上下文切换时是不需要修改的。
- 另外，线程也有自己的私有数据，比如栈和寄存器等，这些在上下文切换时也是需要保存的。


线程的上下文切换其实就可以分为两种情况：    
第一种， 前后两个线程属于不同进程。
此时，因为资源不共享，所以切换过程就跟进程上下文切换是一样。
第二种，前后两个线程属于同一个进程。此时，因为虚拟内存是共享的，
所以在切换时，虚拟内存这些资源就保持不动，只需要切换线程的私有数据、寄存器等不共享的数据。

虽然同为上下文切换，但同进程内的线程切换，要比多进程间的切换消耗更少的资源，
而这，也正是多线程代替多进程的一个优势。

### 中断上下文切换    

为了快速响应硬件的事件，中断处理会打断进程的正常调度和执行，
转而调用中断处理程序，响应设备事件。
而在打断其他进程时，就需要将进程当前的状态保存下来，
这样在中断结束后，进程仍然可以从原来的状态恢复运行。

跟进程上下文不同，中断上下文切换并不涉及到进程的用户态。
所以，即便中断过程打断了一个正处在用户态的进程，
也不需要保存和恢复这个进程的虚拟内存、全局变量等用户态资源。
中断上下文，其实只包括内核态中断服务程序执行所必需的状态，
包括 CPU 寄存器、内核堆栈、硬件中断参数等。

对同一个 CPU 来说，中断处理比进程拥有更高的优先级，所以中断上下文切换并不会与进程上下文切换同时发生。
同样道理，由于中断会打断正常进程的调度和执行，所以大部分中断处理程序都短小精悍，以便尽可能快的执行结束。


### 总结

CPU 上下文切换，是保证 Linux 系统正常工作的核心功能之一，一般情况下不需要我们特别关注。

但过多的上下文切换，会把 CPU 时间消耗在寄存器、内核栈以及虚拟内存等数据的保存和恢复上，从而缩短进程真正运行的时间，
导致系统的整体性能大幅下降。


## 怎么查看系统的上下文切换情况？

vmstat 是一个常用的系统性能分析工具，主要用来分析系统的内存使用情况，也常用来分析 CPU 上下文切换和中断的次数。

```shell script

# 每隔5秒输出1组数据
$ vmstat 5
procs -----------memory---------- ---swap-- -----io---- -system-- ------cpu-----
 r  b   swpd   free   buff  cache   si   so    bi    bo   in   cs us sy id wa st
 0  0      0 7005360  91564 818900    0    0     0     0   25   33  0  0 100  0  0
```

cs（context switch）是每秒上下文切换的次数。

in（interrupt）则是每秒中断的次数。

r（Running or Runnable）是就绪队列的长度，也就是正在运行和等待 CPU 的进程数。

b（Blocked）则是处于不可中断睡眠状态的进程数。


要想查看每个进程的详细情况，就需要使用我们前面提到过的 pidstat 了。给它加上 -w 选项，你就可以查看每个进程上下文切换的情况了。

```shell script

# 每隔5秒输出1组数据
$ pidstat -w 5
Linux 4.15.0 (ubuntu)  09/23/18  _x86_64_  (2 CPU)

08:18:26      UID       PID   cswch/s nvcswch/s  Command
08:18:31        0         1      0.20      0.00  systemd
08:18:31        0         8      5.40      0.00  rcu_sched
...
```

cswch ，表示每秒自愿上下文切换（voluntary context switches）的次数    
所谓自愿上下文切换，是指进程无法获取所需资源，导致的上下文切换。
比如说， I/O、内存等系统资源不足时，就会发生自愿上下文切换。

nvcswch ，表示每秒非自愿上下文切换（non voluntary context switches）的次数    
而非自愿上下文切换，则是指进程由于时间片已到等原因，被系统强制调度，进而发生的上下文切换。
比如说，大量进程都在争抢 CPU 时，就容易发生非自愿上下文切换。

### 测试

sysbench 是一个多线程的基准测试工具，一般用来评估不同系统参数下的数据库负载情况

工具 ：     
   
系统负载 ： uptime （ watch -d uptime）看三个阶段平均负载

系统整体情况 ： mpstat （mpstat -p ALL 3） 查看 每个cpu当前的整体状况，可以重点看用户态、内核态、以及io等待三个参数
系统整体的平均上下文切换情况 ： vmstat (vmstat 3) 可以重点看 r （进行或等待进行的进程）、b （不可中断进程/io进程） 、in （中断次数） 、cs（上下文切换次数）
查看详细的上下文切换情况 ： pidstat （pidstat -w(进程切换指标)/-u（cpu使用指标）/-wt(线程上下文切换指标)） 注意看是自愿上下文切换、还是被动上下文切换
io使用情况 ： iostat

模拟场景工具 ：    
stress ： 模拟进程 、 io     
sysbench ： 模拟线程数    

# 某个应用的CPU使用率居然达到100%，我该怎么办？

## CPU 使用率    





# Linux系统调用列表


概览    

一、进程控制：    

fork	创建一个新进程
clone	按指定条件创建子进程
execve	运行可执行文件
exit	中止进程
_exit	立即中止当前进程
getdtablesize	进程所能打开的最大文件数
getpgid	获取指定进程组标识号
setpgid	设置指定进程组标志号
getpgrp	获取当前进程组标识号
setpgrp	设置当前进程组标志号
getpid	获取进程标识号
getppid	获取父进程标识号
getpriority	获取调度优先级
setpriority	设置调度优先级
modify_ldt	读写进程的本地描述表
nanosleep	使进程睡眠指定的时间
nice	改变分时进程的优先级
pause	挂起进程，等待信号
personality	设置进程运行域
prctl	对进程进行特定操作
ptrace	进程跟踪
sched_get_priority_max	取得静态优先级的上限
sched_get_priority_min	取得静态优先级的下限
sched_getparam	取得进程的调度参数
sched_getscheduler	取得指定进程的调度策略
sched_rr_get_interval	取得按RR算法调度的实时进程的时间片长度
sched_setparam	设置进程的调度参数
sched_setscheduler	设置指定进程的调度策略和参数
sched_yield	进程主动让出处理器,并将自己等候调度队列队尾
vfork	创建一个子进程，以供执行新程序，常与execve等同时使用
wait	等待子进程终止
wait3	参见wait
waitpid	等待指定子进程终止
wait4	参见waitpid
capget	获取进程权限
capset	设置进程权限
getsid	获取会晤标识号
setsid	设置会晤标识号

二、文件系统控制

1、文件读写操作    

fcntl	文件控制
open	打开文件
creat	创建新文件
close	关闭文件描述字
read	读文件
write	写文件
readv	从文件读入数据到缓冲数组中
writev	将缓冲数组里的数据写入文件
pread	对文件随机读
pwrite	对文件随机写
lseek	移动文件指针
_llseek	在64位地址空间里移动文件指针
dup	复制已打开的文件描述字
dup2	按指定条件复制文件描述字
flock	文件加/解锁
poll	I/O多路转换
truncate	截断文件
ftruncate	参见truncate
umask	设置文件权限掩码
fsync	把文件在内存中的部分写回磁盘

2、文件系统操作

access	确定文件的可存取性
chdir	改变当前工作目录
fchdir	参见chdir
chmod	改变文件方式
fchmod	参见chmod
chown	改变文件的属主或用户组
fchown	参见chown
lchown	参见chown
chroot	改变根目录
stat	取文件状态信息
lstat	参见stat
fstat	参见stat
statfs	取文件系统信息
fstatfs	参见statfs
readdir	读取目录项
getdents	读取目录项
mkdir	创建目录
mknod	创建索引节点
rmdir	删除目录
rename	文件改名
link	创建链接
symlink	创建符号链接
unlink	删除链接
readlink	读符号链接的值
mount	安装文件系统
umount	卸下文件系统
ustat	取文件系统信息
utime	改变文件的访问修改时间
utimes	参见utime
quotactl	控制磁盘配额




三、系统控制

ioctl	I/O总控制函数
_sysctl	读/写系统参数
acct	启用或禁止进程记账
getrlimit	获取系统资源上限
setrlimit	设置系统资源上限
getrusage	获取系统资源使用情况
uselib	选择要使用的二进制函数库
ioperm	设置端口I/O权限
iopl	改变进程I/O权限级别
outb	低级端口操作
reboot	重新启动
swapon	打开交换文件和设备
swapoff	关闭交换文件和设备
bdflush	控制bdflush守护进程
sysfs	取核心支持的文件系统类型
sysinfo	取得系统信息
adjtimex	调整系统时钟
alarm	设置进程的闹钟
getitimer	获取计时器值
setitimer	设置计时器值
gettimeofday	取时间和时区
settimeofday	设置时间和时区
stime	设置系统日期和时间
time	取得系统时间
times	取进程运行时间
uname	获取当前UNIX系统的名称、版本和主机等信息
vhangup	挂起当前终端
nfsservctl	对NFS守护进程进行控制
vm86	进入模拟8086模式
create_module	创建可装载的模块项
delete_module	删除可装载的模块项
init_module	初始化模块
query_module	查询模块信息
*get_kernel_syms	取得核心符号,已被query_module代替


四、内存管理

brk	改变数据段空间的分配
sbrk	参见brk
mlock	内存页面加锁
munlock	内存页面解锁
mlockall	调用进程所有内存页面加锁
munlockall	调用进程所有内存页面解锁
mmap	映射虚拟内存页
munmap	去除内存页映射
mremap	重新映射虚拟内存地址
msync	将映射内存中的数据写回磁盘
mprotect	设置内存映像保护
getpagesize	获取页面大小
sync	将内存缓冲区数据写回硬盘
cacheflush	将指定缓冲区中的内容写回磁盘


五、网络管理

getdomainname	取域名
setdomainname	设置域名
gethostid	获取主机标识号
sethostid	设置主机标识号
gethostname	获取本主机名称
sethostname	设置主机名称


六、socket控制

socketcall	socket系统调用
socket	建立socket
bind	绑定socket到端口
connect	连接远程主机
accept	响应socket连接请求
send	通过socket发送信息
sendto	发送UDP信息
sendmsg	参见send
recv	通过socket接收信息
recvfrom	接收UDP信息
recvmsg	参见recv
listen	监听socket端口
select	对多路同步I/O进行轮询
shutdown	关闭socket上的连接
getsockname	取得本地socket名字
getpeername	获取通信对方的socket名字
getsockopt	取端口设置
setsockopt	设置端口参数
sendfile	在文件或端口间传输数据
socketpair	创建一对已联接的无名socket


七、用户管理

getuid	获取用户标识号
setuid	设置用户标志号
getgid	获取组标识号
setgid	设置组标志号
getegid	获取有效组标识号
setegid	设置有效组标识号
geteuid	获取有效用户标识号
seteuid	设置有效用户标识号
setregid	分别设置真实和有效的的组标识号
setreuid	分别设置真实和有效的用户标识号
getresgid	分别获取真实的,有效的和保存过的组标识号
setresgid	分别设置真实的,有效的和保存过的组标识号
getresuid	分别获取真实的,有效的和保存过的用户标识号
setresuid	分别设置真实的,有效的和保存过的用户标识号
setfsgid	设置文件系统检查时使用的组标识号
setfsuid	设置文件系统检查时使用的用户标识号
getgroups	获取后补组标志清单
setgroups	设置后补组标志清单


八、进程间通信

ipc	进程间通信总控制调用

1、信号    

sigaction	设置对指定信号的处理方法
sigprocmask	根据参数对信号集中的信号执行阻塞/解除阻塞等操作
sigpending	为指定的被阻塞信号设置队列
sigsuspend	挂起进程等待特定信号
signal	参见signal
kill	向进程或进程组发信号
*sigblock	向被阻塞信号掩码中添加信号,已被sigprocmask代替
*siggetmask	取得现有阻塞信号掩码,已被sigprocmask代替
*sigsetmask	用给定信号掩码替换现有阻塞信号掩码,已被sigprocmask代替
*sigmask	将给定的信号转化为掩码,已被sigprocmask代替
*sigpause	作用同sigsuspend,已被sigsuspend代替
sigvec	为兼容BSD而设的信号处理函数,作用类似sigaction
ssetmask	ANSI C的信号处理函数,作用类似sigaction

2、消息    

msgctl	消息控制操作
msgget	获取消息队列
msgsnd	发消息
msgrcv	取消息

3、管道    

pipe	创建管道

4、信号量    

semctl	信号量控制
semget	获取一组信号量
semop	信号量操作

5、共享内存    

shmctl	控制共享内存
shmget	获取共享内存
shmat	连接共享内存
shmdt	拆卸共享内存




