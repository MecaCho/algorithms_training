



从系统和应用程序两个角度，来进行性能优化。

从系统的角度来说，主要是对 CPU、内存、网络、磁盘 I/O 以及内核软件资源等进行优化。

而从应用程序的角度来说，主要是简化代码、降低 CPU 使用、减少网络请求和磁盘 I/O，
并借助缓存、异步处理、多进程和多线程等，提高应用程序的吞吐能力。

# CPU 性能工具

## 1.平均负载：

uptime:

top:

/proc/loadavg:

## 2.系统CPU使用率：

vmstat：

mpstat：

top：

sar：

/proc/stat：数据来源，常用于监控

## 3.进程CPU使用率

top/ps/pidstat/htop/atop

## 4.系统上下文切换

vmstat

## 5.进程上下文切换

pidstat

## 6.软中断

top/mpstat

/proc/softirqs

## 7.硬中断

vmstat

/proc/interrupt

## 8.网络

dstat

sar

tcpdump

## 9.IO

dstat

sar

## 10.CPU缓存

perf

## 11.CPU数

lscpu

/proc/cpuinfo

## 12.事件剖析

perf

execsnoop

火焰图

## 13.动态追踪

ftrace

bcc

systemtap

# 内存性能工具

## 1.系统已用、可用、剩余内存

free

vmstat

sar

/proc/meminfo

## 2.进程虚拟内存、常驻内存、共享内存

ps

top

pidstat

/proc/pid/stat

/proc/pid/status

## 3.进程内存分布

pmap

/proc/pid/maps

## 4.进程Swap换出内存

top

/proc/pid/status

## 5.进程缺页异常

ps

top

pidstat

## 6.系统换页情况

sar

## 7.缓存、缓冲区用量

free

vmstat

sar

cachestat

## 8.缓存、缓冲区命中率

cachetop

## 9.SWAP已用空间和剩余空间

free

sar

## 10.SWAP换入换出

vmstat

sar

## 11.内存泄露检测

memleak

valgrind

## 12.指定文件的缓存大小

pcstat

# 磁盘IO性能工具

## 1.文件系统空间容量、使用量以及剩余空间；索引节点容量、使用量以及剩余量

df

## 2.页缓存和可回收Slab缓存

/proc/meminfo

sar

vmstat

## 3.缓冲区

/proc/meminfo

sar

vmstat

## 4.目录项、索引节点、文件系统缓存

/proc/slabinfo

slabtop

## 5.磁盘IO使用率、IOPS、吞吐量、响应时间、IO平均大小及等待队列长度

iostat

sar

dstat

/proc/diskstats

## 6.进程IO大小以及IO延迟

pidstat

iotop

## 7.块设备IO事件跟踪

blktrace

## 8.进程IO系统调用跟踪

starce

perf

trace

## 9.进程块设备IO大小跟踪

biosnoop

biotop

## 10.动态追踪

ftrace

bcc

systemtap


# 网络性能工具

## 1.吞吐量（BPS）

sar

nethogs

iftop

/proc/net/dev

## 2.吞吐量（PPS）

sar

/proc/net/dev

## 3.网络连接数

netstat

ss

## 4.网络错误数

netstat

sar

## 5.网络延迟

ping

hping3

## 6.连接跟踪数

conntrack

/proc/sys/net/netfilter/nf_conntrack_count

/proc/sys/net/netfilter/nf_conntrack_max

## 7.路由

mtr

traceroute

route

## 8.DNS

dig

nslookup

## 9.防火墙和NAT

iptables

## 10.网卡选项

ethtool

## 11.网络抓包

tcpdump

wireshark

## 12.动态追踪

ftrace

bcc

systemtap


# 示例

- uptime

```
 uptime
 21:01:33 up 322 days, 19:48,  3 users,  load average: 0.00, 0.01, 0.09
```

- top

```
top - 21:00:22 up 322 days, 19:47,  3 users,  load average: 0.00, 0.01, 0.10
Tasks: 110 total,   2 running, 108 sleeping,   0 stopped,   0 zombie
%Cpu(s):  0.7 us,  0.7 sy,  0.0 ni, 98.3 id,  0.3 wa,  0.0 hi,  0.0 si,  0.0 st
KiB Mem :  1014904 total,    76404 free,   430480 used,   508020 buff/cache
KiB Swap:        0 total,        0 free,        0 used.   401436 avail Mem 

  PID USER      PR  NI    VIRT    RES    SHR S %CPU %MEM     TIME+ COMMAND                                                                                                      
29973 root      10 -10  125884   9348   5732 S  0.7  0.9 580:53.28 AliYunDun                                                                                                    
    1 root      20   0  125592   3300   1884 S  0.0  0.3   3:46.78 systemd                                                                                                      
    2 root      20   0       0      0      0 S  0.0  0.0   0:00.23 kthreadd                                                                                                     
    3 root      20   0       0      0      0 S  0.0  0.0   1:05.53 ksoftirqd/0                                                                                                  
    5 root       0 -20       0      0      0 S  0.0  0.0   0:00.00 kworker/0:0H                                                                                                 
    7 root      rt   0       0      0      0 S  0.0  0.0   0:00.00 migration/0                                                                                                  
    8 root      20   0       0      0      0 S  0.0  0.0   0:00.00 rcu_bh                                                                                                       
    9 root      20   0       0      0      0 S  0.0  0.0  23:35.75 rcu_sched                                                                                                    
   10 root       0 -20       0      0      0 S  0.0  0.0   0:00.00 lru-add-drain                                                                                                
   11 root      rt   0       0      0      0 S  0.0  0.0   1:38.66 watchdog/0                                                                                                   
   13 root      20   0       0      0      0 S  0.0  0.0   0:00.00 kdevtmpfs   
```

- /proc/loadavg

```
cat /proc/loadavg
0.18 0.37 0.44 1/1558 104635
```

- vmstat

```
vmstat
procs -----------memory---------- ---swap-- -----io---- -system-- ------cpu-----
 r  b   swpd   free   buff  cache   si   so    bi    bo   in   cs us sy id wa st
 1  0 2096124 294244 216552 803648    1    1   178    40    0    0  2  2 96  0  0
```

- mpstat

```
mpstat
Linux 3.10.0-957.21.3.el7.x86_64 (cvm-172_16_30_7)      06/06/2020      _x86_64_        (2 CPU)

09:05:55 PM  CPU    %usr   %nice    %sys %iowait    %irq   %soft  %steal  %guest  %gnice   %idle
09:05:55 PM  all    1.96    0.00    2.03    0.24    0.00    0.05    0.00    0.00    0.00   95.71
```

- sar

```
sar
Linux 3.10.0-957.21.3.el7.x86_64 (qwq)  06/06/2020      _x86_64_        (1 CPU)

12:00:01 AM     CPU     %user     %nice   %system   %iowait    %steal     %idle
12:10:01 AM     all      0.69      0.00      0.44      0.04      0.00     98.83
12:20:01 AM     all      0.85      0.00      0.54      0.01      0.00     98.60
12:30:01 AM     all      0.88      0.00      0.56      0.00      0.00     98.56
12:40:01 AM     all      0.69      0.00      0.45      0.01      0.00     98.85
12:50:01 AM     all      0.76      0.00      0.49      0.01      0.00     98.75
```

- /proc/stat

```
cat /proc/stat
cpu  18698712 2675 14971508 2740704685 199181 0 6036 0 0 0
cpu0 18698712 2675 14971508 2740704685 199181 0 6036 0 0 0
intr 1690872783 53 86 0 0 58 0 3 0 0 0 0 74 15 0 0 0 0 0 0 0 0 0 0 0 2 10519219 161 0 5423 0 6635592 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
ctxt 42347335637
btime 1563556370
processes 640848
procs_running 4
procs_blocked 0
softirq 1144836692 14 767342956 802 21373604 0 0 190 0 0 356119126
```

- vmstat

```
vmstat
procs -----------memory---------- ---swap-- -----io---- -system-- ------cpu-----
 r  b   swpd   free   buff  cache   si   so    bi    bo   in   cs us sy id wa st
 7  0      0  77360  32508 476264    0    0     1     2    1    0  1  1 99  0  0
```

- pidstat

```
pidstat
Linux 3.10.0-957.21.3.el7.x86_64 (qwq)  06/06/2020      _x86_64_        (1 CPU)

10:28:13 PM   UID       PID    %usr %system  %guest    %CPU   CPU  Command
10:28:13 PM     0         1    0.00    0.00    0.00    0.00     0  systemd
10:28:13 PM     0         2    0.00    0.00    0.00    0.00     0  kthreadd
```



