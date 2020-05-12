
# 海量数据

# 总体解决办法

## 针对时间

可以采用巧妙的算法搭配合适的数据结构，如Bloom filter/Hash/bit-map/堆/数据库或倒排索引/trie树

## 针对空间

大而化小，分而治之（hash映射），各个击破
大而化小，各个击破，缩小规模，逐个解决

## 处理海量数据

1。分而治之/hash映射 + hash统计 + 堆/快速/归并排序；
2。双层桶划分
3。Bloom filter/Bitmap；
4。Trie树/数据库/倒排索引；
5。外排序；
6。分布式处理之Hadoop/Mapreduce。

# questions

## 1。海量日志数据，提取出某日访问百度次数最多的那个IP。

## top K
2。寻找热门查询，300万个查询字符串中统计最热门的10个查询

hashmap + 堆

## 

# ref

https://blog.csdn.net/v_july_v/article/details/7382693
https://blog.csdn.net/v_JULY_v/article/details/6279498
