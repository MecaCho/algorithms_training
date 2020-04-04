
'''
460. LFU缓存
设计并实现最不经常使用（LFU）缓存的数据结构。它应该支持以下操作：get 和 put。

get(key) - 如果键存在于缓存中，则获取键的值（总是正数），否则返回 -1。
put(key, value) - 如果键不存在，请设置或插入值。当缓存达到其容量时，它应该在插入新项目之前，使最不经常使用的项目无效。在此问题中，当存在平局（即两个或更多个键具有相同使用频率）时，最近最少使用的键将被去除。

进阶：
你是否可以在 O(1) 时间复杂度内执行两项操作？

示例：

LFUCache cache = new LFUCache( 2 /* capacity (缓存容量) */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // 返回 1
cache.put(3, 3);    // 去除 key 2
cache.get(2);       // 返回 -1 (未找到key 2)
cache.get(3);       // 返回 3
cache.put(4, 4);    // 去除 key 1
cache.get(1);       // 返回 -1 (未找到 key 1)
cache.get(3);       // 返回 3
cache.get(4);       // 返回 4

460. LFU Cache
Design and implement a data structure for Least Frequently Used (LFU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reaches its capacity, it should invalidate the least frequently used item before inserting a new item. For the purpose of this problem, when there is a tie (i.e., two or more keys that have the same frequency), the least recently used key would be evicted.

Note that the number of times an item is used is the number of calls to the get and put functions for that item since it was inserted. This number is set to zero when the item is removed.

 

Follow up:
Could you do both operations in O(1) time complexity?

 

Example:

LFUCache cache = new LFUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.get(3);       // returns 3.
cache.put(4, 4);    // evicts key 1.
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
'''



import operator

class Node(object):
    def __init__(self, value, last_get, frq, key):
        self.value = value
        self.key = key
        self.last_get = last_get
        self.frq = frq


class LFUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.values = {}
        self.time_ = 0
        self.remain = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        self.time_ += 1
        if key not in self.values:
            return -1
        else:
            value = self.values[key]
            value.frq += 1
            value.last_get = self.time_
            self.values[key] = value
            return self.values[key].value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        self.time_ += 1
        v = Node(value, self.time_, 1, key)
        if key in self.values:
            v = self.values.pop(key)
            v.value = value
            v.frq += 1
        else:
            if self.remain <= 0:
                if not self.values:
                    return
                values = sorted(self.values.values(), key=operator.attrgetter("frq", "last_get"))
                self.values.pop(values[0].key)
            else:
                self.remain -= 1
        self.values[key] = v


        # Your LFUCache object will be instantiated and called as such:
        # obj = LFUCache(capacity)
        # param_1 = obj.get(key)
        # obj.put(key,value)
