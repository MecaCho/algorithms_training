# encoding=utf8

'''
662. Maximum Width of Binary Tree
Given the root of a binary tree, return the maximum width of the given tree.

The maximum width of a tree is the maximum width among all levels.

The width of one level is defined as the length between the end-nodes (the leftmost and rightmost non-null nodes), where the null nodes between the end-nodes that would be present in a complete binary tree extending down to that level are also counted into the length calculation.

It is guaranteed that the answer will in the range of a 32-bit signed integer.

 

Example 1:


Input: root = [1,3,2,5,3,null,9]
Output: 4
Explanation: The maximum width exists in the third level with length 4 (5,3,null,9).
Example 2:


Input: root = [1,3,2,5,null,null,9,6,null,7]
Output: 7
Explanation: The maximum width exists in the fourth level with length 7 (6,null,null,null,null,null,7).
Example 3:


Input: root = [1,3,2,5]
Output: 2
Explanation: The maximum width exists in the second level with length 2 (3,2).
 

Constraints:

The number of nodes in the tree is in the range [1, 3000].
-100 <= Node.val <= 100

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def max_depth(root):
            return max(max_depth(root.left), max_depth(root.right))+1 if root else 0

        height = max_depth(root)
        vals = [[2**height-1, 0] for i in range(height)]

        # (0, 0)
        # (1,0) (1,1)
        # (2, 0), (2, 1), (2, 2), (2,3)
        # 3 0,1,2,3,4,5,6,7
        def traversal(root, r, c):
            if not root:
                return
            if c < vals[r][0]:
                vals[r][0] = c
            if c > vals[r][1]:
                vals[r][1] = c
            traversal(root.left, r+1, 2*c)
            traversal(root.right, r+1, 2*c+1)

        traversal(root, 0, 0)

        return max(val[1]-val[0]+1 for val in vals)

      
