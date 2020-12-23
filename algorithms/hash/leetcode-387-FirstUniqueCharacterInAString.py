# encoding=utf8

'''
387. 字符串中的第一个唯一字符
给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。

案例:

s = "leetcode"
返回 0.

s = "loveleetcode",
返回 2.
 

注意事项：您可以假定该字符串只包含小写字母。

387. First Unique Character in a String
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.


'''

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: str
        """
        letters='abcdefghijklmnopqrstuvwxyz'
        indexs = [s.index(l) for l in letters if s.count(l) == 1]
        return s[min(indexs)] if indexs else " "

class Solution1(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: str
        """
        hash_map = {}
        import collections
        counter = collections.Counter(s)
        for c in s:
            if counter[c] == 1:
                return c
        return " "


class Solution2(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        key_dict = {}

        for key in s:
            if key in key_dict:
                key_dict[key] += 1
            else:
                key_dict[key] = 1

        for i in range(len(s)):
            if key_dict[s[i]] == 1:
                return i
        return -1


import collections
class Solution20201223(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        # dict_c = [0]*26
        # for i in range(len(s)):
        #     index = ord(s[i]) - ord("a")
        #     if dict_c[index] == 0:
        #         dict_c[index] = i
        counter_c = collections.Counter(s)
        for i in range(len(s)):
            c = s[i]
            if counter_c[c] == 1:
                return i
        return -1


# solution

'''
方法一：使用哈希表存储频数
思路与算法

我们可以对字符串进行两次遍历。

在第一次遍历时，我们使用哈希映射统计出字符串中每个字符出现的次数。在第二次遍历时，我们只要遍历到了一个只出现一次的字符，那么就返回它的索引，否则在遍历结束后返回 -1−1。

代码

C++JavaPython3JavaScriptGolangC

class Solution:
    def firstUniqChar(self, s: str) -> int:
        frequency = collections.Counter(s)
        for i, ch in enumerate(s):
            if frequency[ch] == 1:
                return i
        return -1
复杂度分析

时间复杂度：O(n)O(n)，其中 nn 是字符串 ss 的长度。我们需要进行两次遍历。

空间复杂度：O(|\Sigma|)O(∣Σ∣)，其中 \SigmaΣ 是字符集，在本题中 ss 只包含小写字母，因此 |\Sigma| \leq 26∣Σ∣≤26。我们需要 O(|\Sigma|)O(∣Σ∣) 的空间存储哈希映射。

方法二：使用哈希表存储索引
思路与算法

我们可以对方法一进行修改，使得第二次遍历的对象从字符串变为哈希映射。

具体地，对于哈希映射中的每一个键值对，键表示一个字符，值表示它的首次出现的索引（如果该字符只出现一次）或者 -1−1（如果该字符出现多次）。当我们第一次遍历字符串时，设当前遍历到的字符为 cc，如果 cc 不在哈希映射中，我们就将 cc 与它的索引作为一个键值对加入哈希映射中，否则我们将 cc 在哈希映射中对应的值修改为 -1−1。

在第一次遍历结束后，我们只需要再遍历一次哈希映射中的所有值，找出其中不为 -1−1 的最小值，即为第一个不重复字符的索引。如果哈希映射中的所有值均为 -1−1，我们就返回 -1−1。

代码

C++JavaPython3JavaScriptGolangC

class Solution:
    def firstUniqChar(self, s: str) -> int:
        position = dict()
        n = len(s)
        for i, ch in enumerate(s):
            if ch in position:
                position[ch] = -1
            else:
                position[ch] = i
        first = n
        for pos in position.values():
            if pos != -1 and pos < first:
                first = pos
        if first == n:
            first = -1
        return first
复杂度分析

时间复杂度：O(n)O(n)，其中 nn 是字符串 ss 的长度。第一次遍历字符串的时间复杂度为 O(n)O(n)，第二次遍历哈希映射的时间复杂度为 O(|\Sigma|)O(∣Σ∣)，由于 ss 包含的字符种类数一定小于 ss 的长度，因此 O(|\Sigma|)O(∣Σ∣) 在渐进意义下小于 O(n)O(n)，可以忽略。

空间复杂度：O(|\Sigma|)O(∣Σ∣)，其中 \SigmaΣ 是字符集，在本题中 ss 只包含小写字母，因此 |\Sigma| \leq 26∣Σ∣≤26。我们需要 O(|\Sigma|)O(∣Σ∣) 的空间存储哈希映射。

方法三：队列
思路与算法

我们也可以借助队列找到第一个不重复的字符。队列具有「先进先出」的性质，因此很适合用来找出第一个满足某个条件的元素。

具体地，我们使用与方法二相同的哈希映射，并且使用一个额外的队列，按照顺序存储每一个字符以及它们第一次出现的位置。当我们对字符串进行遍历时，设当前遍历到的字符为 cc，如果 cc 不在哈希映射中，我们就将 cc 与它的索引作为一个二元组放入队尾，否则我们就需要检查队列中的元素是否都满足「只出现一次」的要求，即我们不断地根据哈希映射中存储的值（是否为 -1−1）选择弹出队首的元素，直到队首元素「真的」只出现了一次或者队列为空。

在遍历完成后，如果队列为空，说明没有不重复的字符，返回 -1−1，否则队首的元素即为第一个不重复的字符以及其索引的二元组。

小贴士

在维护队列时，我们使用了「延迟删除」这一技巧。也就是说，即使队列中有一些字符出现了超过一次，但它只要不位于队首，那么就不会对答案造成影响，我们也就可以不用去删除它。只有当它前面的所有字符被移出队列，它成为队首时，我们才需要将它移除。

代码

C++JavaPython3JavaScriptGolangC

class Solution:
    def firstUniqChar(self, s: str) -> int:
        position = dict()
        q = collections.deque()
        n = len(s)
        for i, ch in enumerate(s):
            if ch not in position:
                position[ch] = i
                q.append((s[i], i))
            else:
                position[ch] = -1
                while q and position[q[0][0]] == -1:
                    q.popleft()
        return -1 if not q else q[0][1]
复杂度分析

时间复杂度：O(n)O(n)，其中 nn 是字符串 ss 的长度。遍历字符串的时间复杂度为 O(n)O(n)，而在遍历的过程中我们还维护了一个队列，由于每一个字符最多只会被放入和弹出队列最多各一次，因此维护队列的总时间复杂度为 O(|\Sigma|)O(∣Σ∣)，由于 ss 包含的字符种类数一定小于 ss 的长度，因此 O(|\Sigma|)O(∣Σ∣) 在渐进意义下小于 O(n)O(n)，可以忽略。

空间复杂度：O(|\Sigma|)O(∣Σ∣)，其中 \SigmaΣ 是字符集，在本题中 ss 只包含小写字母，因此 |\Sigma| \leq 26∣Σ∣≤26。我们需要 O(|\Sigma|)O(∣Σ∣) 的空间存储哈希映射以及队列。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/first-unique-character-in-a-string/solution/zi-fu-chuan-zhong-de-di-yi-ge-wei-yi-zi-x9rok/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''