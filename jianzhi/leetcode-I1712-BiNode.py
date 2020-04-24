'''
面试题 17.12. BiNode LCCI
The data structure TreeNode is used for binary tree, but it can also used to represent a single linked list (where left is null, and right is the next node in the list). Implement a method to convert a binary search tree (implemented with TreeNode) into a single linked list. The values should be kept in order and the operation should be performed in place (that is, on the original data structure).

Return the head node of the linked list after converting.

Note: This problem is slightly different from the original one in the book.



Example:

Input:  [4,2,5,1,3,null,6,0]
Output:  [0,null,1,null,2,null,3,null,4,null,5,null,6]
Note:

The number of nodes will not exceed 100000.

面试题 17.12. BiNode
二叉树数据结构TreeNode可用来表示单向链表（其中left置空，right为下一个链表节点）。实现一个方法，把二叉搜索树转换为单向链表，要求值的顺序保持不变，转换操作应是原址的，也就是在原始的二叉搜索树上直接修改。

返回转换后的单向链表的头节点。

注意：本题相对原题稍作改动



示例：

输入： [4,2,5,1,3,null,6,0]
输出： [0,null,1,null,2,null,3,null,4,null,5,null,6]
提示：

节点数量不会超过 100000。
'''



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def convertBiNode(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None

        self.head, self.pre = None, None
        def mid_travelsal(root):
            if not root:
                return
            mid_travelsal(root.left)
            if not self.head:
                self.head = self.pre if self.pre else root

            root.left = None
            if self.pre:
                self.pre.right = root
            self.pre = root
            mid_travelsal(root.right)

        mid_travelsal(root)

        return self.head
