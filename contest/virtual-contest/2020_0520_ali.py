
'''
在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。

示例 1:

输入: 4->2->1->3
输出: 1->2->3->4
示例 2:

输入: -1->5->3->4->0
输出: -1->0->3->4->5
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def merge_list(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val < l2.val:
            l1.next = self.merge_list(l1.next, l2)
            return l1
        else:
            l2.next = self.merge_list(l1, l2.next)
            return l2

    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        if not head.next.next:
            if head.val <= head.next.val:
                return head
            tmp = head.next
            head.next = None
            tmp.next = head
            return tmp
        fast = head
        slow = ListNode(0)
        slow.next = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # print(fast, slow)
        # return
        tmp = slow.next
        slow.next = None
        mid = tmp
        # print(head, mid)
        # merged = self.merge_list(head, mid)
        # return merged

        l = self.sortList(head)
        # pre = ListNode(0)
        # pre.next = l
        # while l and l.next:
        #     l = l.next
        r = self.sortList(mid)
        # l.next = r
        return self.merge_list(l, r)


'''
全排列 II

给定一个可包含重复数字的序列，返回所有不重复的全排列。

示例:

输入: [1,1,2]
输出:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
'''


class Solution1(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.vals = []

        # length =
        # nums = sorted(nums)[::-1]
        def backtrack(arr, res):
            if not arr:
                if res not in self.vals:
                    self.vals.append(res)
            else:
                insert_num = arr[0]
                pre = None
                for i in range(len(res) + 1):
                    # print(pre, insert_num, res, nums)
                    if not pre or pre != insert_num:
                        backtrack(arr[1:], res[:i] + [insert_num] + res[i:])
                        if i < len(res):
                            pre = res[i]

        backtrack(nums, [])
        return sorted(self.vals)


'''
实现一个 Trie (前缀树)，包含 insert, search, 和 startsWith 这三个操作。

示例:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // 返回 true
trie.search("app");     // 返回 false
trie.startsWith("app"); // 返回 true
trie.insert("app");   
trie.search("app");     // 返回 true
说明:

你可以假设所有的输入都是由小写字母 a-z 构成的。
保证所有输入均为非空字符串。
'''


class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        tree = self.root
        for i in range(len(word)):
            tree = tree.setdefault(word[i], {})
            # if tree is None or not tree.get(word[i]):
            #     tree[word[i]] = {}
            # tree = tree.get(word[i])
        tree["end"] = True
        # print(self.root)

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        tree = self.root
        for w in word:
            tree = tree.get(w)
            if tree is None:
                return False
        if tree.get("end"):
            return True
        return False

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        tree = self.root
        for w in prefix:
            tree = tree.get(w)
            if tree is None:
                return False

        return True

    # Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


if __name__ == '__main__':
    trie = Trie()
    trie.insert("apple")
    trie.insert("app")
    res = trie.search("ap")
    print(res)
    print(trie.search("apple"))
    print(trie.startsWith("appl"))
