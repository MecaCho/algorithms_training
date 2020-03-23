'''
面试题 02.02. Kth Node From End of List LCCI
Implement an algorithm to find the kth to last element of a singly linked list. Return the value of the element.

Note: This problem is slightly different from the original one in the book.

Example:

Input:  1->2->3->4->5 和 k = 2
Output:  4
Note:

k is always valid.
'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def kthToLast(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: int
        """
        val_list = []
        while head:
            val_list.append(head.val)
            head = head.next
        return val_list[-k]

    
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution1(object):
    def kthToLast(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: int
        """
        # val_list = []
        # while head:
        #     val_list.append(head.val)
        #     head = head.next
        # return val_list[-k]
        fast = head
        slow = head
        while k > 0:
            if not fast:
                return -1
            k -= 1
            fast = fast.next
        while fast:
            fast = fast.next
            slow = slow.next
        return slow.val if slow else -1

