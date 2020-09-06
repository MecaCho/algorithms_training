'''

107. Binary Tree Level Order Traversal II
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]

107. 二叉树的层次遍历 II
给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）

例如：
给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其自底向上的层次遍历为：

[
  [15,7],
  [9,20],
  [3]
]

'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        def deep_traversal(root, deepth=0, res=[]):
            if not root:
                return
            if not res:
                res = [[root.val]]
            else:
                if len(res) < deepth + 1:
                    res.append([root.val])
                else:
                    res[deepth].append(root.val)
            deep_traversal(root.left, deepth + 1, res)
            deep_traversal(root.right, deepth + 1, res)
            return res
        res = deep_traversal(root, 0, res)
        return res[::-1] if res else []



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution1(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.vals  = []
        def dfs(root, deepth):
            if not root:
                return
            if deepth < len(self.vals):
                self.vals[deepth].append(root.val)
            else:
                self.vals.append([root.val])
            dfs(root.left, deepth+1)
            dfs(root.right, deepth+1)

        dfs(root, 0)

        return self.vals[::-1]