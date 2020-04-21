
'''
99. 二叉树的右视图
给定一棵二叉树，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。

示例:

输入: [1,2,3,null,5,null,4]
输出: [1, 3, 4]
解释:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---

199. Binary Tree Right Side View
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution1(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.vals = []
        def dfs(root, deep):
            if not root:
                return
            if not self.vals or len(self.vals) == deep:
                self.vals.append([root.val])
            elif len(self.vals) >= deep+1:
                self.vals[deep].append(root.val)
            dfs(root.left, deep+1)
            dfs(root.right, deep+1)
        dfs(root, 0)
        return [val[-1] for val in self.vals]


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.vals = []
        def dfs(root, deep):
            if not root:
                return
            if len(self.vals) <= deep:
                self.vals.append(root.val)
            else:
                self.vals[deep] = root.val
            dfs(root.left, deep+1)
            dfs(root.right, deep+1)
        dfs(root, 0)
        # return [val[-1] for val in self.vals]
        return self.vals
