# encoding=utf8

'''
1302. Deepest Leaves Sum
Given the root of a binary tree, return the sum of values of its deepest leaves.
 

Example 1:


Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
Output: 15
Example 2:

Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
Output: 19
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
1 <= Node.val <= 100
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        max_depth = 0

        sums = defaultdict(int)
        def traversal(root, depth):
            if not root:
                return
            sums[depth] += root.val
            traversal(root.left, depth+1)
            traversal(root.right, depth+1)
        traversal(root, 0)
        return sums[max(sums.keys())]

