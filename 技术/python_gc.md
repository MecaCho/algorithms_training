
# 内存泄露

速度越快的存储器，单位价格也越昂贵。因此，妥善利用好每一寸高速存储器的空间，永远是系统设计的一个核心。


Python 程序在运行的时候，需要在内存中开辟出一块空间，用于存放运行时产生的临时变量；计算完成后，再将结果输出到永久性存储器中。如果数据量过大，内存空间管理不善就很容易出现 OOM（out of memory），俗称爆内存，程序可能被操作系统中止。

对于服务器，这种设计为永不中断的系统来说，
内存管理则显得更为重要，不然很容易引发内存泄漏。

## 什么是内存泄漏呢？

1.这里的泄漏，并不是说你的内存出现了信息安全问题，被恶意程序利用了，而是指程序本身没有设计好，
导致程序未能释放已不再使用的内存。

2.内存泄漏也不是指你的内存在物理上消失了，而是意味着代码在分配了某段内存后，
因为设计错误，失去了对这段内存的控制，从而造成了内存的浪费。


# python垃圾回收机制

## 计数引用

Python 中一切皆对象。
因此，你所看到的一切变量，本质上都是对象的一个指针。
那么，怎么知道一个对象，是否永远都不能被调用了呢？非常直观的一个想法，
就是当这个对象的引用计数（指针数）为 0 的时候，说明这个对象永不可达，
自然它也就成为了垃圾，需要被回收。

```python

import os
import psutil

# 显示当前 python 程序占用的内存大小
def show_memory_info(hint):
    pid = os.getpid()
    p = psutil.Process(pid)
    
    info = p.memory_full_info()
    memory = info.uss / 1024. / 1024
    print('{} memory used: {} MB'.format(hint, memory))

def func():
    show_memory_info('initial')
    a = [i for i in range(10000000)]
    show_memory_info('after a created')

func()
show_memory_info('finished')

########## 输出 ##########

# initial memory used: 47.19140625 MB
# after a created memory used: 433.91015625 MB
# finished memory used: 48.109375 MB
```

# 引用计数机制

```python

import sys

a = []

# 两次引用，一次来自 a，一次来自 getrefcount
print(sys.getrefcount(a))

def func(a):
    # 四次引用，a，python 的函数调用栈，函数参数，和 getrefcount
    print(sys.getrefcount(a))

func(a)

# 两次引用，一次来自 a，一次来自 getrefcount，函数 func 调用已经不存在
print(sys.getrefcount(a))

########## 输出 ##########

# 2
# 4
# 2
```

在函数调用发生的时候，会产生额外的两次引用，一次来自函数栈，另一个是函数参数。

```python

import sys

a = []

print(sys.getrefcount(a)) # 两次

b = a

print(sys.getrefcount(a)) # 三次

c = b
d = b
e = c
f = e
g = d

print(sys.getrefcount(a)) # 八次

########## 输出 ##########

# 2
# 3
# 8
```

手动释放内存

```python

import gc

show_memory_info('initial')

a = [i for i in range(10000000)]

show_memory_info('after a created')

del a
gc.collect()

show_memory_info('finish')
print(a)

########## 输出 ##########

# initial memory used: 48.1015625 MB
# after a created memory used: 434.3828125 MB
# finish memory used: 48.33203125 MB
# 
# ---------------------------------------------------------------------------
# NameError                                 Traceback (most recent call last)
# <ipython-input-12-153e15063d8a> in <module>
#      11 
#      12 show_memory_info('finish')
# ---> 13 print(a)
# 
# NameError: name 'a' is not defined
```

# 循环引用

```python

def func():
    show_memory_info('initial')
    a = [i for i in range(10000000)]
    b = [i for i in range(10000000)]
    show_memory_info('after a, b created')
    a.append(b)
    b.append(a)

func()
show_memory_info('finished')

########## 输出 ##########

# initial memory used: 47.984375 MB
# after a, b created memory used: 822.73828125 MB
# finished memory used: 821.73046875 MB


import gc

def func():
    show_memory_info('initial')
    a = [i for i in range(10000000)]
    b = [i for i in range(10000000)]
    show_memory_info('after a, b created')
    a.append(b)
    b.append(a)

func()
gc.collect()
show_memory_info('finished')

########## 输出 ##########

# initial memory used: 49.51171875 MB
# after a, b created memory used: 824.1328125 MB
# finished memory used: 49.98046875 MB
```

# Python 使用标记清除（mark-sweep）算法和分代收集（generational），来启用针对循环引用的自动垃圾回收

先来看标记清除算法。我们先用图论来理解不可达的概念。
对于一个有向图，如果从一个节点出发进行遍历，并标记其经过的所有节点；
那么，在遍历结束后，所有没有被标记的节点，我们就称之为不可达节点。
显而易见，这些节点的存在是没有任何意义的，自然的，我们就需要对它们进行垃圾回收。
当然，每次都遍历全图，对于 Python 而言是一种巨大的性能浪费。
所以，在 Python 的垃圾回收实现中，mark-sweep 使用双向链表维护了一个数据结构，
并且只考虑容器类的对象（只有容器类对象才有可能产生循环引用）。
具体算法这里我就不再多讲了，毕竟我们的重点是关注应用。而分代收集算法，则是另一个优化手段。
Python 将所有对象分为三代。
刚刚创立的对象是第 0 代；经过一次垃圾回收后，依然存在的对象，便会依次从上一代挪到下一代。
而每一代启动自动垃圾回收的阈值，则是可以单独指定的。
当垃圾回收器中新增对象减去删除对象达到相应的阈值时，就会对这一代对象启动垃圾回收。
事实上，分代收集基于的思想是，新生的对象更有可能被垃圾回收，而存活更久的对象也有更高的概率继续存活。
因此，通过这种做法，可以节约不少计算量，从而提高 Python 的性能。

# 调试内存泄漏

不过，虽然有了自动回收机制，但这也不是万能的，难免还是会有漏网之鱼
。内存泄漏是我们不想见到的，而且还会严重影响性能。
有没有什么好的调试手段呢？答案当然是肯定的，接下来我就为你介绍一个“得力助手”。
它就是 objgraph，一个非常好用的可视化引用关系的包。
在这个包中，我主要推荐两个函数，第一个是 show_refs()，它可以生成清晰的引用关系图。
通过下面这段代码和生成的引用调用图，你能非常直观地发现，有两个 list 互相引用，
说明这里极有可能引起内存泄露。这样一来，再去代码层排查就容易多了。

```python

import objgraph

a = [1, 2, 3]
b = [4, 5, 6]

a.append(b)
b.append(a)

objgraph.show_refs([a])


import objgraph

a = [1, 2, 3]
b = [4, 5, 6]

a.append(b)
b.append(a)

objgraph.show_backrefs([a])
```

# 总结

垃圾回收是 Python 自带的机制，用于自动释放不会再用到的内存空间；
引用计数是其中最简单的实现，不过切记，这只是充分非必要条件，
    因为循环引用需要通过不可达判定，来确定是否可以回收；
Python 的自动回收算法包括标记清除和分代收集，主要针对的是循环引用的垃圾收集；
调试内存泄漏方面， objgraph 是很好的可视化分析工具。

# 思考
你能否自己实现一个垃圾回收判定算法呢？我的要求很简单，输入是一个有向图，
给定起点，表示程序入口点；给定有向边，输出不可达节点。

事实上算法可以写的很简单，这是个很经典的 dfs （深度优先搜索）遍历，从起点开始遍历，对遍历到的节点做个记号。
遍历完成后，再对所有节点扫一遍，没有被做记号的，就是需要垃圾回收的。


分代收集算法中每一代都有一个默认阈值，超过指定阈值之后就会启动垃圾回收。
如果垃圾回收启动太频繁，会造成程序性能低下，分代收集也是为了提高性能，因此不立刻回收没关系，
只要一定时间或者一定阈值之后回收都没问题。
内存泄漏是这部分内存永远不再被回收，越攒越多，直到撑爆内存。
