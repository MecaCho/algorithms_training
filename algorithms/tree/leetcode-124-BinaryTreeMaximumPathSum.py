'''
124. 二叉树中的最大路径和
给定一个非空二叉树，返回其最大路径和。

本题中，路径被定义为一条从树中任意节点出发，达到任意节点的序列。该路径至少包含一个节点，且不一定经过根节点。

示例 1:

输入: [1,2,3]

       1
      / \
     2   3

输出: 6
示例 2:

输入: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

输出: 42

124. Binary Tree Maximum Path Sum
Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6
Example 2:

Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42

'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        self.max_val = -float("inf")
        def max_sum(root):

            if not root:
                return 0

            left_max = max(max_sum(root.left), 0)
            right_max = max(max_sum(root.right), 0)
            root_sum = root.val + left_max + right_max

            self.max_val = max(self.max_val, root_sum)

            return root.val + max(left_max, right_max)

        max_sum(root)
        return self.max_val


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution1(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        max_val = float("-inf")

        global max_val
        def max_sum(root):
            global max_val

            if not root:
                return 0

            left_max = max(max_sum(root.left), 0)
            right_max = max(max_sum(root.right), 0)
            root_sum = root.val + left_max + right_max

            max_val = max(max_val, root_sum)

            return root.val + max(left_max, right_max)

        max_sum(root)
        return max_val

