
linux 常用命令有哪些、分别举例？

```
查看系统默认的最大文件句柄数，系统默认是1024

# ulimit -n

查看当前进程打开了多少句柄数

# lsof -n|awk '{print $2}'|sort|uniq -c|sort -nr|more
```


查询 3306 端口占用情况的 linux 指令如何写？


linux 中查看某个进程的进程号 pid、如何操作呢？


进程通信方式？


进程、线程、协程？


进程调度算法？


Liunx下的 I/O 模型？


用户态、内核态？


如何减少内核态到用户态的拷贝（mmap）？


常用的命令？


查看日志？


# 使用netstat、lsof查看端口占用情况
- netstat

netstat用来查看系统当前系统网络状态信息，包括端口，连接情况等，常用方式如下：

```
netstat -atunlp,各参数含义如下:

-t : 指明显示TCP端口
-u : 指明显示UDP端口
-l : 仅显示监听套接字(LISTEN状态的套接字)
-p : 显示进程标识符和程序名称，每一个套接字/端口都属于一个程序
-n : 不进行DNS解析
-a 显示所有连接的端口
执行后得表格一目了然，就不做截图了，当然，在众多表目中找一个特定得，肯定不那么顺手，一般该指令会遇grep配合使用，比如查找端口22,就用netstat -tunlp | grep 22 或者干脆netstat -an | grep 22就可以了，查看其它端口类似，当然也可以通过端口状态查找即netstat -anp | grep TIME_WAIT，即只会显示含有TIME_WAIT字符串的条目

```

- lsof

lsof的作用是列出当前系统打开文件(list open files)，不过通过-i参数也能查看端口的连接情况，
-i后跟冒号端口可以查看指定端口信息，直接-i是系统当前所有打开的端口

lsof -i:22 #查看22端口连接情况，默认为sshd端口 如下图：
```
[root@iZwz9anui2d9inq5ach3uhZ ~]# lsof -i:22
COMMAND   PID USER   FD   TYPE  DEVICE SIZE/OFF NODE NAME
sshd    12525 root    3u  IPv4 7625600      0t0  TCP iZwz9anui2d9inq5ach3uhZ:ssh->116.24.67.143:igcp (ESTABLISHED)
sshd    14983 root    3u  IPv4 5331725      0t0  TCP *:ssh (LISTEN)
```
查看连接数
可以看到当前通过端口22连接到机器的一共有4个(主机名和ip已打码)，通过该命令就能清楚知道当前端口状态


# 在 shell 下有 A B C D 四个命令，需要先执行 A 再执行 B C 最后执行 D 

  其中, B C 耗时较多， 但是，互不干扰，可以同步执

子进程 和 wait

./A

./B &  # 设为子进程

./C &

wait

./D

wait加参数是等待某个进程结束，不加参数是等待以上所有后台进程结束
```shell script
#!/bin/bash

#
# 异步执行（wait）使用样例-父脚本
#

echo "父脚本：启动子脚本.."
./async-child &

# 通过将shell参数 $! 赋给pid变量，以记录子进程的进程ID
pid=$!  

echo "父脚本：子脚本(PID=${pid})已启动"

echo "父脚本：继续执行中.."
sleep 2

echo "父脚本：暂停执行，等待子脚本执行完毕.."
wait ${pid}

echo "父脚本：子脚本已结束，父脚本继续.."
echo "父脚本：父脚本执行结束。脚本退出！"
```

子脚本：

```shell script
#!/bin/bash

#
# 异步执行（wait）使用样例-子脚本
#

echo "子脚本：正在运行.."
sleep 5
echo "子脚本：子脚本结束。脚本退出！"
```


# 读取配置文件

我现在有个配置文件config，里面内容为
ID=123
IP=192.168.3.154
Name=test
想写个shell脚本，把这几个变量的值给读出来

- sed

第一种方法： 用sed 流处理器，将每行=号和前面的部分去掉，并赋给变量。
```
id=`sed '/^ID=/!d;s/.*=//' urfile`
ip=`sed '/^IP=/!d;s/.*=//' urfile`
name=`sed '/^Name=/!d;s/.*=//' urfile`
echo $id
echo $ip
echo $name
```


- eval 

第二种方法： 使用eval方法解析。
```
while read line;do
    eval "$line"
done < config
echo $ID
echo $IP
echo $Name
```

- source

第三种方法：直接将变量load进环境中成为环境变量。

```
. config
source config
```