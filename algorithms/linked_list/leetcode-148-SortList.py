
'''
148. 排序链表
在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。

示例 1:

输入: 4->2->1->3
输出: 1->2->3->4
示例 2:

输入: -1->5->3->4->0
输出: -1->0->3->4->5

148. Sort List
Sort a linked list in O(n log n) time using constant space complexity.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4
Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5
'''




# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def merge_list(self, l1, l2):
        # print(l1, l2)
        if l1 and l2:
            if l1.val < l2.val:
                l1.next = self.merge_list(l1.next, l2)
                return l1
            else:
                l2.next = self.merge_list(l1, l2.next)
                return l2
        return l1 if not l2 else l2


    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        fast = head.next
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None
        # print(mid, head)
        right = self.sortList(mid)
        left = self.sortList(head)

        res = self.merge_list(left, right)
        # print(res)
        return res
