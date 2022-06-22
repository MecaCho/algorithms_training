# encoding=utf8

'''
513. Find Bottom Left Tree Value
Given the root of a binary tree, return the leftmost value in the last row of the tree.

 

Example 1:


Input: root = [2,1,3]
Output: 1
Example 2:


Input: root = [1,2,3,4,null,5,6,null,null,7]
Output: 7
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.height = 0
        self.val = root.val if root else None
        def dfs(root, height):
            if not root:
                return
            dfs(root.left, height+1)
            dfs(root.right, height+1)
            if height > self.height:
                self.height = height
                self.val = root.val

        dfs(root, 0)
        return self.val


