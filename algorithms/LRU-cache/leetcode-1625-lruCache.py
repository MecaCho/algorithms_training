'''
面试题 16.25. LRU缓存
设计和构建一个“最近最少使用”缓存，该缓存会删除最近最少使用的项目。缓存应该从键映射到值(允许你插入和检索特定键对应的值)，并在初始化时指定最大容量。当缓存被填满时，它应该删除最近最少使用的项目。

它应该支持以下操作： 获取数据 get 和 写入数据 put 。

获取数据 get(key) - 如果密钥 (key) 存在于缓存中，则获取密钥的值（总是正数），否则返回 -1。
写入数据 put(key, value) - 如果密钥不存在，则写入其数据值。当缓存容量达到上限时，它应该在写入新数据之前删除最近最少使用的数据值，从而为新的数据值留出空间。

示例:

LRUCache cache = new LRUCache( 2 /* 缓存容量 */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // 返回  1
cache.put(3, 3);    // 该操作会使得密钥 2 作废
cache.get(2);       // 返回 -1 (未找到)
cache.put(4, 4);    // 该操作会使得密钥 1 作废
cache.get(1);       // 返回 -1 (未找到)
cache.get(3);       // 返回  3
cache.get(4);       // 返回  4

面试题 16.25. LRU Cache LCCI
Design and build a "least recently used" cache, which evicts the least recently used item. The cache should map from keys to values (allowing you to insert and retrieve a value associ­ated with a particular key) and be initialized with a max size. When it is full, it should evict the least recently used item.

You should implement following operations:  get and put.

Get a value by key: get(key) - If key is in the cache, return the value, otherwise return -1.
Write a key-value pair to the cache: put(key, value) - If the key is not in the cache, then write its value to the cache. Evict the least recently used item before writing if necessary.

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
'''


import collections

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.vals = collections.OrderedDict()
        self.capacity = capacity


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        res = self.vals.get(key)

        if res:
            self.vals[key] = res

        return res


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        res = self.get(key)

        if not res:
            if len(self.vals.keys()) >= self.capacity:
                # self.vals[key] = value
            # else:
            #     self.vals.popitem()
                self.vals.popitem(last=False)
            self.vals[key] = value




# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# tips

'''
首先明确问题。你到底想要什么功能？
什么数据结构对查找最有用？维护元素顺序最有用的数据结构是什么？
散列表和双向链表都很有用。你能把这两者结合起来吗？
'''