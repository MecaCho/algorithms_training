


# Linux内存是怎么工作的？

内存主要用来存储系统和应用程序的指令、数据、缓存等。

存映射，其实就是将虚拟内存地址映射到物理内存地址。
为了完成内存映射，内核为每个进程都维护了一张页表，记录虚拟地址与物理地址的映射关系


## 如何查看内存使用情况

free 

```shell script

# 注意不同版本的free输出可能会有所不同
$  free -m
              total        used        free      shared  buff/cache   available
Mem:            991         260         180           0         550         584
Swap:             0           0           0
```

第一列，total 是总内存大小；

第二列，used 是已使用内存的大小，包含了共享内存；

第三列，free 是未使用内存的大小；

第四列，shared 是共享内存的大小；

第五列，buff/cache 是缓存和缓冲区的大小；

最后一列，available 是新进程可用内存的大小。

最后一列的可用内存 available 。
available 不仅包含未使用内存，还包括了可回收的缓存，
所以一般会比未使用内存更大。
不过，并不是所有缓存都可以回收，因为有些缓存可能正在使用中。

top

```
top - 22:55:06 up 271 days, 10:08,  1 user,  load average: 0.08, 0.03, 0.05
Tasks:  77 total,   2 running,  75 sleeping,   0 stopped,   0 zombie
%Cpu(s):  0.7 us,  0.7 sy,  0.0 ni, 98.7 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
KiB Mem :  1014904 total,   184212 free,   267396 used,   563296 buff/cache
KiB Swap:        0 total,        0 free,        0 used.   598592 avail Mem 

  PID USER      PR  NI    VIRT    RES    SHR S %CPU %MEM     TIME+ COMMAND                                                                                                                                                   
 1524 root      10 -10  124236   8256   5176 S  1.3  0.8 400:36.63 AliYunDun                                                                                                                                                 
 5107 mysql     20   0  987560 114048   2296 S  0.3 11.2  61:44.96 mysqld                                                                                                                                                    
 9112 redis     20   0  142960   1124     56 S  0.3  0.1  34:16.73 redis-server                                                                                                                                              
24349 root      20   0  162024   2248   1552 R  0.3  0.2   0:00.01 top                                                                                                                                                       
    1 root      20   0  190976   3056   1660 S  0.0  0.3   4:10.73 systemd       
```

VIRT 是进程虚拟内存的大小，只要是进程申请过的内存，即便还没有真正分配物理内存，也会计算在内。

RES 是常驻内存的大小，也就是进程实际使用的物理内存大小，但不包括 Swap 和共享内存。

SHR 是共享内存的大小，比如与其他进程共同使用的共享内存、加载的动态链接库以及程序的代码段等。

%MEM 是进程使用物理内存占系统总内存的百分比。



# 怎么理解内存中的Buffer和Cache？

## free 数据的来源

```

buffers
              Memory used by kernel buffers (Buffers in /proc/meminfo)

       cache  Memory used by the page cache and slabs (Cached and SReclaimable in /proc/meminfo)

       buff/cache
              Sum of buffers and cache
```

从 free 的手册中，你可以看到 buffer 和 cache 的说明。

Buffers 是内核缓冲区用到的内存，对应的是 /proc/meminfo 中的 Buffers 值。

Cache 是内核页缓存和 Slab 用到的内存，对应的是 /proc/meminfo 中的 Cached 与 SReclaimable 之和。


## proc 文件系统

