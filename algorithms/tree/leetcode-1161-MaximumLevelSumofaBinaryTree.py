# encoding=utf8

'''
1161. Maximum Level Sum of a Binary Tree

Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

Return the smallest level x such that the sum of all the values of nodes at level x is maximal.

 

Example 1:


Input: root = [1,7,0,7,-8,null,null]
Output: 2
Explanation: 
Level 1 sum = 1.
Level 2 sum = 7 + 0 = 7.
Level 3 sum = 7 + -8 = -1.
So we return the level with the maximum sum which is level 2.
Example 2:

Input: root = [989,null,10250,98693,-89388,null,null,null,-32127]
Output: 2
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-105 <= Node.val <= 105

1161. 最大层内元素和

给你一个二叉树的根节点 root。设根节点位于二叉树的第 1 层，而根节点的子节点位于第 2 层，依此类推。

返回总和 最大 的那一层的层号 x。如果有多层的总和一样大，返回其中 最小 的层号 x。

 

示例 1：

输入：root = [1,7,0,7,-8,null,null]
输出：2
解释：
第 1 层各元素之和为 1，
第 2 层各元素之和为 7 + 0 = 7，
第 3 层各元素之和为 7 + -8 = -1，
所以我们返回第 2 层的层号，它的层内元素之和最大。

示例 2：

输入：root = [989,null,10250,98693,-89388,null,null,null,-32127]
输出：2

 

提示：

    树中的节点数在 [1, 104]范围内
    -105 <= Node.val <= 105
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        self.vals = []
        def dfs(root: TreeNode, depth: int) -> int:
            if not root:
                return
            if depth >= len(self.vals):
                self.vals.append([root.val])
            else:
                self.vals[depth].append(root.val)
            dfs(root.left, depth+1)
            dfs(root.right, depth+1)
        dfs(root, 0)
        res = 0
        max_s = -float("inf")
        # print(self.vals)
        for i, vals in enumerate(self.vals):
            if sum(vals) > max_s:
                max_s = sum(vals)
                res = i+1
        return res


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        vals = []
        def dfs(root: TreeNode, depth: int) -> int:
            if not root:
                return
            if depth >= len(vals):
                vals.append(root.val)
            else:
                vals[depth] += root.val
            dfs(root.left, depth+1)
            dfs(root.right, depth+1)
        dfs(root, 0)

        return vals.index(max(vals)) + 1 



