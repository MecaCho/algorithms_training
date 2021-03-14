# encoding=utf8

'''
706. Design HashMap
Design a HashMap without using any built-in hash table libraries.

Implement the MyHashMap class:

MyHashMap() initializes the object with an empty map.
void put(int key, int value) inserts a (key, value) pair into the HashMap. If the key already exists in the map, update the corresponding value.
int get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.


Example 1:

Input
["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
[[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
Output
[null, null, null, 1, -1, null, 1, null, -1]

Explanation
MyHashMap myHashMap = new MyHashMap();
myHashMap.put(1, 1); // The map is now [[1,1]]
myHashMap.put(2, 2); // The map is now [[1,1], [2,2]]
myHashMap.get(1);    // return 1, The map is now [[1,1], [2,2]]
myHashMap.get(3);    // return -1 (i.e., not found), The map is now [[1,1], [2,2]]
myHashMap.put(2, 1); // The map is now [[1,1], [2,1]] (i.e., update the existing value)
myHashMap.get(2);    // return 1, The map is now [[1,1], [2,1]]
myHashMap.remove(2); // remove the mapping for 2, The map is now [[1,1]]
myHashMap.get(2);    // return -1 (i.e., not found), The map is now [[1,1]]


Constraints:

0 <= key, value <= 106
At most 104 calls will be made to put, get, and remove.


Follow up: Please do not use the built-in HashMap library.


706. 设计哈希映射
不使用任何内建的哈希表库设计一个哈希映射（HashMap）。

实现 MyHashMap 类：

MyHashMap() 用空映射初始化对象
void put(int key, int value) 向 HashMap 插入一个键值对 (key, value) 。如果 key 已经存在于映射中，则更新其对应的值 value 。
int get(int key) 返回特定的 key 所映射的 value ；如果映射中不包含 key 的映射，返回 -1 。
void remove(key) 如果映射中存在 key 的映射，则移除 key 和它所对应的 value 。


示例：

输入：
["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
[[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
输出：
[null, null, null, 1, -1, null, 1, null, -1]

解释：
MyHashMap myHashMap = new MyHashMap();
myHashMap.put(1, 1); // myHashMap 现在为 [[1,1]]
myHashMap.put(2, 2); // myHashMap 现在为 [[1,1], [2,2]]
myHashMap.get(1);    // 返回 1 ，myHashMap 现在为 [[1,1], [2,2]]
myHashMap.get(3);    // 返回 -1（未找到），myHashMap 现在为 [[1,1], [2,2]]
myHashMap.put(2, 1); // myHashMap 现在为 [[1,1], [2,1]]（更新已有的值）
myHashMap.get(2);    // 返回 1 ，myHashMap 现在为 [[1,1], [2,1]]
myHashMap.remove(2); // 删除键为 2 的数据，myHashMap 现在为 [[1,1]]
myHashMap.get(2);    // 返回 -1（未找到），myHashMap 现在为 [[1,1]]


提示：

0 <= key, value <= 106
最多调用 104 次 put、get 和 remove 方法


进阶：你能否不使用内置的 HashMap 库解决此问题？

'''


class MyHashMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = [-1] * 1000001


    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: None
        """
        self.map[key] = value


    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        return self.map[key]


    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: None
        """
        self.map[key] = -1



# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)



# solutions

'''
解题思路
今天的题目让我们设计哈希表（HashMap）。HashMap 是指能 O(1)O(1) 时间内进行插入和删除 key-value 对，可以保存不重复元素的一种数据结构。

昨天的每日一题是 705. 设计哈希集合，我在题解 详解 HashSet 的设计：在时间和空间上做权衡 中已经非常详细讲解了哈希集合（HashSet）的设计。本篇题解偷懒，文字部分和昨天题解基本一样。

HashMap 和 HashSet 的区别是 HashMap 保存的每个元素 key-value 对，而 HashSet 保存的是某个元素 key 是否出现过。所以我们把 HashSet 稍作改进即可。

HashMap 是在 时间和空间 上做权衡的经典例子：如果不考虑空间，我们可以直接设计一个超大的数组，使每个key 都有单独的位置，则不存在冲突；如果不考虑时间，我们可以直接用一个无序的数组保存输入，每次查找的时候遍历一次数组。

为了时间和空间上的平衡，HashMap 基于数组实现，并通过 hash 方法求键 key 在数组中的位置，当 hash 后的位置存在冲突的时候，再解决冲突。

设计 hash 函数需要考虑两个问题：

通过 hash 方法把键 key 转成数组的索引：设计合适的 hash 函数，一般都是对分桶数取模 % 。
处理碰撞冲突问题：拉链法 和 线性探测法。
下面我用了两个方法：

超大数组：简便。
拉链法：大多数编程语言选择的方法。
超大数组
能使用超大数组来解决本题是因为输入数据的范围在 0 <= key <= 10^60<=key<=10 
6
  。因此我们只需要 10^6 + 110 
6
 +1大小的数组，就能让每个数据都有一个单独的索引，不会有 key 的碰撞问题。

因为对于 HashMap 来说，每个元素都需要保存 key:value ，因此，我们把数组的元素设计成 int 型，代表的是 value 。以元素作为索引从数组中获取对应位置保存的数字，就是 value。

优点：查找和删除的性能非常快，只用访问 1 次数组；
缺点：使用了非常大的空间，当元素范围很大时，无法使用该方法；当存储的元素个数较少时，性价比极低；需要预知数据的取值范围。
Python

class MyHashMap(object):

    def __init__(self):
        self.map = [-1] * 1000001

    def put(self, key, value):
        self.map[key] = value

    def get(self, key):
        return self.map[key]

    def remove(self, key):
        self.map[key] = -1
时间复杂度：O(1)O(1)
空间复杂度：O(数据范围)O(数据范围)
拉链法
如果在面试中，面试官一定不会满意上面的解法，刷力扣是为了面试，不是为了 AC，所以我们应该写出让面试官满意的代码。那么基于「拉链法」的 HashMap 也务必要掌握。



拉链法是说，我们定义了一个比较小的数组，然后使用 hash 方法来把求出 key 应该出现在数组中的位置；但是由于不同的 key 在求完 hash 之后，可能会存在碰撞冲突，所以数组并不直接保存元素，而是每个位置都指向了一条链表（或数组）用于存储元素。

我们可以看出在查找一个 key 的时候需要两个步骤：① 求hash到数组中的位置；② 在链表中遍历找key。

优点：我们可以把数组大小设计比较合理，从而节省空间；不用预知 key 的范围；方便扩容。
缺点：需要多次访问内存，性能上比超大数组的 HashSet 差；需要设计合理的 hash 方法实现均匀散列；如果链表比较长，则退化成 $$O(N)$$ 的查找；实现比较复杂；
在下面的具体实现中，我把拉链设计成了基于「数组」的实现（也可以基于链表）。此时「拉链数组」有两种设计方法：①定长拉链数组；②不定长拉链数组。

定长拉链数组
这个方法本质上就是把 HashSet 设计成一个 M * NM∗N 的二维数组。第一个维度用于计算 hash 分桶，第二个维度寻找 key 存放具体的位置。用了一个优化：第二个维度的数组只有当需要构建时才会产生，这样可以节省内存。

优点：两个维度都可以直接计算出来，查找和删除只用两次访问内存。
缺点：需要预知数据范围，用于设计第二个维度的数组大小。
Python

class MyHashMap(object):

    def __init__(self):
        self.map = [[-1] * 1000 for _ in range(1001)]

    def put(self, key, value):
        row, col = key // 1000, key % 1000
        self.map[row][col] = value

    def get(self, key):
        row, col = key // 1000, key % 1000
        return self.map[row][col]

    def remove(self, key):
        row, col = key // 1000, key % 1000
        self.map[row][col] = -1
时间复杂度：O(1)O(1)
空间复杂度：O(数据范围)O(数据范围)
不定长拉链数组
不定长的拉链数组是说拉链会根据分桶中的 key 动态增长，更类似于真正的链表。

分桶数一般取质数，这是因为经验上来说，质数个的分桶能让数据更加分散到各个桶中。下面的代码中把分桶数去了 1009，是因为 1009 是大于 1000 的第一个质数。

优点：节省内存，不用预知数据范围；
缺点：在链表中查找元素需要遍历。
Python

class MyHashMap:

    def __init__(self):
        self.buckets = 1009
        self.table = [[] for _ in range(self.buckets)]

    def hash(self, key):
        return key % self.buckets
    
    def put(self, key: int, value: int) -> None:
        hashkey = self.hash(key)
        for item in self.table[hashkey]:
            if item[0] == key:
                item[1] = value
                return
        self.table[hashkey].append([key, value])

    def get(self, key: int) -> int:
        hashkey = self.hash(key)
        for item in self.table[hashkey]:
            if item[0] == key:
                return item[1]
        return -1

    def remove(self, key: int) -> None:
        hashkey = self.hash(key)
        for i, item in enumerate(self.table[hashkey]):
            if item[0] == key:
                self.table[hashkey].pop(i)
                return
时间复杂度：$$O(N/b)$$，N 是元素个数，b 是桶数。
空间复杂度：$$O(N)$$
在实际测试中，发现「不定长拉链数组」法速度最快，我的理解是，大块的内存分配也是需要时间的。因此避免大块的内存分配，也是在节省时间。

刷题心得
从上面的设计上来看，我们发现，设计一个 HashMap 是在时间和空间上寻求平衡的过程。在写本题解前，我复习了《算法 第4版》的散列表章节（293页），非常经典，收获很大。我的题解的内容范围和质量不及《算法 第4版》的十之一二，强烈建议大家通过阅读经典书籍来系统地学习算法。

参考资料：

《算法 第4版》
图源
OK，以上就是 @负雪明烛 写的今天题解的全部内容了，如果你觉得有帮助的话，求赞、求关注、求收藏。如果有疑问的话，请在下面评论，我会及时解答。

关注我，你将不会错过我的精彩动画题解、面试题分享、组队刷题活动，进入主页 @负雪明烛 右侧有刷题组织，从此刷题不再孤单。

祝大家牛年大吉！AC 多多，Offer 多多！我们明天再见！

作者：fuxuemingzhu
链接：https://leetcode-cn.com/problems/design-hashmap/solution/xiang-jie-hashmap-de-she-ji-zai-shi-jian-85k9/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''