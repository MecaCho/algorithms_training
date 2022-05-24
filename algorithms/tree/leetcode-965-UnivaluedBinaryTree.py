# encoding=utf8

'''
965. Univalued Binary Tree
A binary tree is uni-valued if every node in the tree has the same value.

Given the root of a binary tree, return true if the given tree is uni-valued, or false otherwise.

 

Example 1:


Input: root = [1,1,1,1,1,null,1]
Output: true
Example 2:


Input: root = [2,2,2,5,2]
Output: false
 

Constraints:

The number of nodes in the tree is in the range [1, 100].
0 <= Node.val < 100
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # def traversal(root):
        stack = [(root, 0)]
        vals = None
        while stack:
            # print(stack)
            node, flag = stack.pop()
            if node:
                if flag:
                    if vals is None:
                        vals = node.val
                    elif node.val != vals:
                        return False
                else:
                    stack.append((node.left, 0))
                    stack.append((node, 1))
                    stack.append((node.right, 0))
        return True
                


