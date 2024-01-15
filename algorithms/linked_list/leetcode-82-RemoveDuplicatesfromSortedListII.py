# encoding=utf8


'''
82. 删除排序链表中的重复元素 II
给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。

示例 1:

输入: 1->2->3->3->4->4->5
输出: 1->2->5
示例 2:

输入: 1->1->1->2->3
输出: 2->3

82. Remove Duplicates from Sorted List II
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

Return the linked list sorted as well.

Example 1:

Input: 1->2->3->3->4->4->5
Output: 1->2->5
Example 2:

Input: 1->1->1->2->3
Output: 2->3
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        dummy_node = ListNode(0)
        dummy_node.next = head
        head = dummy_node
        while head.next and head.next.next:
            loc = head.next
            flag = False
            while loc and loc.next and loc.val == loc.next.val:
                flag = True
                loc = loc.next
            if flag:
                head.next = loc.next
            else:
                head = head.next
        return dummy_node.next


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution1(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = None

        res = ListNode(0)
        res.next = head

        head = res
        while head.next and head.next.next:
            flag = False
            while head.next and head.next.next and head.next.val == head.next.next.val:
                flag = True
                head.next.next = head.next.next.next
            if flag:
                head.next = head.next.next
            else:
                head = head.next
        return res.next



# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution20210325(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy_node = ListNode(0)
        dummy_node.next = head
        head = dummy_node

        while head.next and head.next.next:
            flag = False
            while head.next and head.next.next and head.next.val == head.next.next.val:
                head.next.next = head.next.next.next
                flag = True
            if flag:
                head.next = head.next.next
            else:
                head = head.next
        return dummy_node.next



# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution20210325_1(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = ListNode(0)
        dummy_node = pre
        pre.next = head

        while pre.next and pre.next.next:
            flag = False
            while pre.next and pre.next.next and pre.next.val == pre.next.next.val:
                pre.next.next = pre.next.next.next
                flag = True
            if flag:
                pre.next = pre.next.next
            else:
                pre = pre.next
        return dummy_node.next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode(0, head)
        pre = res
        pre_val = None
        while head:
            if pre_val is None:
                if (head.next is None or head.next.val != head.val):
                    pre.next = head
                    pre = pre.next
            else:
                if (head.val != pre_val and (head.next is None or head.next.val != head.val)):
                    pre.next = head
                    pre = pre.next
                    # print(head.val, head.next)
            pre_val = head.val
            head = head.next
        pre.next = None
        return res.next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode(101, head)
        pre = res
        pre_val = 101
        while head:
            if head.val != pre_val and (head.next is None or head.next.val != head.val):
                pre.next = head
                pre = pre.next
            pre_val = head.val
            head = head.next
        pre.next = None
        return res.next



# solutions

'''
方法一：一次遍历
思路与算法

由于给定的链表是排好序的，因此重复的元素在链表中出现的位置是连续的，因此我们只需要对链表进行一次遍历，就可以删除重复的元素。由于链表的头节点可能会被删除，因此我们需要额外使用一个哑节点（dummy node）指向链表的头节点。

具体地，我们从指针 \textit{cur}cur 指向链表的哑节点，随后开始对链表进行遍历。如果当前 \textit{cur.next}cur.next 与 \textit{cur.next.next}cur.next.next 对应的元素相同，那么我们就需要将 \textit{cur.next}cur.next 以及所有后面拥有相同元素值的链表节点全部删除。我们记下这个元素值 xx，随后不断将 \textit{cur.next}cur.next 从链表中移除，直到 \textit{cur.next}cur.next 为空节点或者其元素值不等于 xx 为止。此时，我们将链表中所有元素值为 xx 的节点全部删除。

如果当前 \textit{cur.next}cur.next 与 \textit{cur.next.next}cur.next.next 对应的元素不相同，那么说明链表中只有一个元素值为 \textit{cur.next}cur.next 的节点，那么我们就可以将 \textit{cur}cur 指向 \textit{cur.next}cur.next。

当遍历完整个链表之后，我们返回链表的的哑节点的下一个节点 \textit{dummy.next}dummy.next 即可。

细节

需要注意 \textit{cur.next}cur.next 以及 \textit{cur.next.next}cur.next.next 可能为空节点，如果不加以判断，可能会产生运行错误。

代码

注意下面 \texttt{C++}C++ 代码中并没有释放被删除的链表节点以及哑节点的空间。如果在面试中遇到本题，读者需要针对这一细节与面试官进行沟通。

C++JavaPython3JavaScriptGolangC

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        
        dummy = ListNode(0, head)

        cur = dummy
        while cur.next and cur.next.next:
            if cur.next.val == cur.next.next.val:
                x = cur.next.val
                while cur.next and cur.next.val == x:
                    cur.next = cur.next.next
            else:
                cur = cur.next

        return dummy.next
复杂度分析

时间复杂度：O(n)O(n)，其中 nn 是链表的长度。

空间复杂度：O(1)O(1)。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list-ii/solution/shan-chu-pai-xu-lian-biao-zhong-de-zhong-oayn/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''

