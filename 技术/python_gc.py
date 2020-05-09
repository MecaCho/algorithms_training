# -*-coding=UTF-8-*-
import os
import psutil


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

# initial memory used: 5.90625 MB
# after a created memory used: 316.81640625 MB
# finished memory used: 240.51953125 MB


def func():
    show_memory_info('initial')
    global a
    a = [i for i in range(10000000)]
    show_memory_info('after a created')

func()
show_memory_info('finished')

########## 输出 ##########

# initial memory used: 48.88671875 MB
# after a created memory used: 433.94921875 MB
# finished memory used: 433.94921875 MB

# initial memory used: 5.90234375 MB
# after a created memory used: 268.28125 MB
# finished memory used: 289.06640625 MB

# initial memory used: 289.06640625 MB
# after a created memory used: 360.22265625 MB
# finished memory used: 360.22265625 MB


def func():
    show_memory_info('initial')
    a = [i for i in derange(10000000)]
    show_memory_info('after a created')
    return a

a = func()
show_memory_info('finished')

########## 输出 ##########

# initial memory used: 47.96484375 MB
# after a created memory used: 434.515625 MB
# finished memory used: 434.515625 MB


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

