# encoding=utf8

'''
705. Design HashSet
Design a HashSet without using any built-in hash table libraries.

Implement MyHashSet class:

void add(key) Inserts the value key into the HashSet.
bool contains(key) Returns whether the value key exists in the HashSet or not.
void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.


Example 1:

Input
["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
[[], [1], [2], [1], [3], [2], [2], [2], [2]]
Output
[null, null, null, true, false, null, true, null, false]

Explanation
MyHashSet myHashSet = new MyHashSet();
myHashSet.add(1);      // set = [1]
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(1); // return True
myHashSet.contains(3); // return False, (not found)
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(2); // return True
myHashSet.remove(2);   // set = [1]
myHashSet.contains(2); // return False, (already removed)


Constraints:

0 <= key <= 106
At most 104 calls will be made to add, remove, and contains.


Follow up: Could you solve the problem without using the built-in HashSet library?


705. 设计哈希集合
不使用任何内建的哈希表库设计一个哈希集合（HashSet）。

实现 MyHashSet 类：

void add(key) 向哈希集合中插入值 key 。
bool contains(key) 返回哈希集合中是否存在这个值 key 。
void remove(key) 将给定值 key 从哈希集合中删除。如果哈希集合中没有这个值，什么也不做。

示例：

输入：
["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
[[], [1], [2], [1], [3], [2], [2], [2], [2]]
输出：
[null, null, null, true, false, null, true, null, false]

解释：
MyHashSet myHashSet = new MyHashSet();
myHashSet.add(1);      // set = [1]
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(1); // 返回 True
myHashSet.contains(3); // 返回 False ，（未找到）
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(2); // 返回 True
myHashSet.remove(2);   // set = [1]
myHashSet.contains(2); // 返回 False ，（已移除）


提示：

0 <= key <= 106
最多调用 104 次 add、remove 和 contains 。


进阶：你可以不使用内建的哈希集合库解决此问题吗？
'''


class MyHashSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.vals = set()


    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        self.vals.add(key)


    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        if key in self.vals:
            self.vals.remove(key)


    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        return key in self.vals



# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)


# solutions

'''
概述
为了实现哈希集合这一数据结构，有以下几个关键问题需要解决：

哈希函数：能够将集合中任意可能的元素映射到一个固定范围的整数值，并将该元素存储到整数值对应的地址上。
冲突处理：由于不同元素可能映射到相同的整数值，因此需要在整数值出现「冲突」时，需要进行冲突处理。总的来说，有以下几种策略解决冲突：
链地址法：为每个哈希值维护一个链表，并将具有相同哈希值的元素都放入这一链表当中。
开放地址法：当发现哈希值 hh 处产生冲突时，根据某种策略，从 hh 出发找到下一个不冲突的位置。例如，一种最简单的策略是，不断地检查 h+1,h+2,h+3,\ldotsh+1,h+2,h+3,… 这些整数对应的位置。
再哈希法：当发现哈希冲突后，使用另一个哈希函数产生一个新的地址。
扩容：当哈希表元素过多时，冲突的概率将越来越大，而在哈希表中查询一个元素的效率也会越来越低。因此，需要开辟一块更大的空间，来缓解哈希表中发生的冲突。
以上内容读者可以自行翻阅数据结构的教材，本题解不再阐述，而是直接给出一个最简单的哈希表实现。

方法一：链地址法
设哈希表的大小为 \textit{base}base，则可以设计一个简单的哈希函数：\text{hash}(x) = x \bmod \textit{base}hash(x)=xmodbase。

我们开辟一个大小为 \textit{base}base 的数组，数组的每个位置是一个链表。当计算出哈希值之后，就插入到对应位置的链表当中。

由于我们使用整数除法作为哈希函数，为了尽可能避免冲突，应当将 \textit{base}base 取为一个质数。在这里，我们取 \textit{base}=769base=769。



代码

C++JavaJavaScriptGolangC

const base = 769

type MyHashSet struct {
    data []list.List
}

func Constructor() MyHashSet {
    return MyHashSet{make([]list.List, base)}
}

func (s *MyHashSet) hash(key int) int {
    return key % base
}

func (s *MyHashSet) Add(key int) {
    if !s.Contains(key) {
        h := s.hash(key)
        s.data[h].PushBack(key)
    }
}

func (s *MyHashSet) Remove(key int) {
    h := s.hash(key)
    for e := s.data[h].Front(); e != nil; e = e.Next() {
        if e.Value.(int) == key {
            s.data[h].Remove(e)
        }
    }
}

func (s *MyHashSet) Contains(key int) bool {
    h := s.hash(key)
    for e := s.data[h].Front(); e != nil; e = e.Next() {
        if e.Value.(int) == key {
            return true
        }
    }
    return false
}
复杂度分析

时间复杂度：O(\frac{n}{b})O( 
b
n
​	
 )。其中 nn 为哈希表中的元素数量，bb 为链表的数量。假设哈希值是均匀分布的，则每个链表大概长度为 \frac{n}{b} 
b
n
​	
 。

空间复杂度：O(n+b)O(n+b)。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/design-hashset/solution/she-ji-ha-xi-ji-he-by-leetcode-solution-xp4t/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
