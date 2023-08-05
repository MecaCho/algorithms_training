# encoding

'''
21. 合并两个有序链表
将两个升序链表合并为一个新的升序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。

示例：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4

21. Merge Two Sorted Lists
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
'''


# 递归
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # if not l1:
        #     return l2
        # if not l2:
        #     return l1
        # if l1.val <= l2.val:
        #     l1.next = self.mergeTwoLists(l1.next, l2)
        #     return l1
        # elif l1.val > l2.val:
        #     l2.next = self.mergeTwoLists(l1, l2.next)
        #     return l2

        if l1 and l2:
            if l1.val < l2.val:
                l1.next = self.mergeTwoLists(l1.next, l2)
                return l1
            else:
                l2.next = self.mergeTwoLists(l1, l2.next)
                return l2
        return l1 if not l2 else l2


# 迭代
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution1(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1
        pre = ListNode(0)
        cur = pre
        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next

        cur.next = l1 if l1 else l2
        return pre.next




# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        new_head = ListNode(0)
        dummy = new_head
        head1 = list1
        head2 = list2
        while head1 or head2:
            value = 0
            if head1 and head2:
                if head1.val < head2.val:
                    value = head1.val 
                    head1 = head1.next
                else:
                    value = head2.val
                    head2 = head2.next
            elif head1:
                value = head1.val
                head1 = head1.next
            else:
                value = head2.val
                head2 = head2.next
            new_node = ListNode(val=value)
            new_head.next = new_node
            new_head = new_head.next
        # print(dummy)
        return dummy.next

