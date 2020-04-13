'''
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
