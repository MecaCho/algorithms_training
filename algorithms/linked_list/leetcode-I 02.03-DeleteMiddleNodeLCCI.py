
'''
面试题 02.03. 删除中间节点
实现一种算法，删除单向链表中间的某个节点（除了第一个和最后一个节点，不一定是中间节点），假定你只能访问该节点。

 

示例：

输入：单向链表a->b->c->d->e->f中的节点c
结果：不返回任何数据，但该链表变为a->b->d->e->f


面试题 02.03. Delete Middle Node LCCI
Implement an algorithm to delete a node in the middle (i.e., any node but the first and last node, not necessarily the exact middle) of a singly linked list, given only access to that node.

 

Example:

Input: the node c from the linked list a->b->c->d->e->f
Output: nothing is returned, but the new linked list looks like a->b->d->e->f
'''




# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if not node.next:
            node = None
        node.val, node.next = node.next.val, node.next.next
