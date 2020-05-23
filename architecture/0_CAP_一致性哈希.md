

# 一致性哈希-Consistent Hashing


## 背景

一致性哈希算法在1997年由麻省理工学院的Karger等人在解决分布式Cache中提出的，
设计目标是为了解决因特网中的热点(Hot spot)问题，初衷和CARP十分类似。
一致性哈希修正了CARP使用的简单哈希算法带来的问题，
使得DHT可以在P2P环境中真正得到应用。
但现在一致性hash算法在分布式系统中也得到了广泛应用

- memcached缓存数据库

在计算一致性hash时采用如下步骤：

1。首先求出memcached服务器（节点）的哈希值，并将其配置到0～2^32的圆（continuum）上。
2。然后采用同样的方法求出存储数据的键的哈希值，并映射到相同的圆上。
3。然后从数据映射到的位置开始顺时针查找，将数据保存到找到的第一个服务器上。如果超过2^32仍然找不到服务器，就会保存到第一台memcached服务器上。

良好的分布式cahce系统中的一致性hash算法应该满足以下几个方面：

平衡性(Balance)

单调性(Monotonicity)

分散性(Spread)

负载(Load)

平滑性(Smoothness)

## 原理

一致性哈希算法（Consistent Hashing）最早在论文《Consistent Hashing and Random Trees: Distributed Caching Protocols for Relieving Hot Spots on the World Wide Web》中被提出。
简单来说，一致性哈希将整个哈希值空间组织成一个虚拟的圆环，
如假设某哈希函数H的值空间为0-2^32-1（即哈希值是一个32位无符号整形）




