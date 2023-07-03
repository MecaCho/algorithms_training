# encoding=utf8

'''
445. Add Two Numbers II
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:


Input: l1 = [7,2,4,3], l2 = [5,6,4]
Output: [7,8,0,7]
Example 2:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [8,0,7]
Example 3:

Input: l1 = [0], l2 = [0]
Output: [0]
 

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
 

Follow up: Could you solve it without reversing the input lists?

445. 两数相加 II
给你两个 非空 链表来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储一位数字。将这两数相加会返回一个新的链表。

你可以假设除了数字 0 之外，这两个数字都不会以零开头。



进阶：

如果输入链表不能修改该如何处理？换句话说，你不能对列表中的节点进行翻转。



示例：

输入：(7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 8 -> 0 -> 7
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        vals1, vals2 = [], []
        while l1:
            vals1.append(l1.val)
            l1 = l1.next
        while l2:
            vals2.append(l2.val)
            l2 = l2.next
        pre = 0
        cur = None
        while vals1 or vals2 or pre:
            val1 = vals1.pop() if vals1 else 0
            val2 = vals2.pop() if vals2 else 0
            sum_ = val1 + val2 + pre
            pre = sum_ // 10
            node = ListNode(sum_%10)
            node.next = cur
            cur = node
        return cur




# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        vals1 = []
        while l1:
            vals1.append(l1.val)
            l1 = l1.next

        vals2 = []
        while l2:
            vals2.append(l2.val)
            l2 = l2.next

        res = None
        jin = 0

        r = res
        while vals1 or vals2 or jin:
            value1 = vals1.pop() if vals1 else 0
            value2 = vals2.pop() if vals2 else 0


            node = ListNode(((value1 + value2 + jin) % 10))

            jin = (value1 + value2 + jin) / 10

            node.next = res
            res = node

        return res
