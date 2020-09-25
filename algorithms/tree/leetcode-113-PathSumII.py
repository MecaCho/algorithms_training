
'''
113. 路径总和 II
给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。

说明: 叶子节点是指没有子节点的节点。

示例:
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
返回:

[
   [5,4,11,2],
   [5,8,4,5]
]

113. Path Sum II
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:

[
   [5,4,11,2],
   [5,8,4,5]
]
'''






# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        self.res = []
        def dfs(root, res, target):
            if not root.left and not root.right:
                if target == root.val:
                    self.res.append(res+[root.val])

            if root.left:
                dfs(root.left, res+[root.val], target-root.val)
            if root.right:
                dfs(root.right, res+[root.val], target-root.val)
        if root:
            dfs(root, [], sum)
        return self.res


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution20200926(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        self.vals = []
        def dfs(root, path, target):
            if not root:
                return
            else:
                if root.left is None and root.right is None:
                    if target == root.val:
                        self.vals.append(path+[root.val])
                    return
            dfs(root.left, path+[root.val], target-root.val)
            dfs(root.right, path+[root.val], target-root.val)
        dfs(root, [], sum)
        return self.vals

