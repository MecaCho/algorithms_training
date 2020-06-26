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


