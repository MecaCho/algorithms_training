'''
234. 回文链表
请判断一个链表是否为回文链表。

示例 1:

输入: 1->2
输出: false
示例 2:

输入: 1->2->2->1
输出: true
进阶：
你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？

234. Palindrome Linked List
Easy

3013

347

Add to List

Share
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?


'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return True
        fast, slow = head, head
        pre = ListNode(0)
        pre.next = head

        while fast and fast.next:
            fast = fast.next.next

            tmp = slow.next
            slow.next = pre
            pre = slow

            slow = tmp

        if fast:
            slow = slow.next

        while slow and pre:
            if pre.val != slow.val:
                return False
            slow = slow.next
            pre = pre.next
        return True

# Runtime: 60 ms, faster than 98.24% of Python online submissions for Palindrome Linked List.
# Memory Usage: 31.7 MB, less than 85.78% of Python online submissions for Palindrome Linked List.



# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution1(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return True
        fast, slow = head, head
        pre = None
        while fast and fast.next:
            fast = fast.next.next
            pre, pre.next,slow = slow, pre, slow.next


        if fast:
            slow = slow.next

        while slow and pre:
            if pre.val != slow.val:
                return False
            slow = slow.next
            pre = pre.next
        return True
#     Runtime: 48 ms, faster than 100.00% of Python online submissions for Palindrome Linked List.
#     Memory Usage: 31.7 MB, less than 76.10% of Python online submissions for Palindrome Linked List.