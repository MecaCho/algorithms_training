
'''
面试题32 - II. 从上到下打印二叉树 II
从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，每一层打印到一行。



例如:
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：

[
  [3],
  [9,20],
  [15,7]
]


提示：

节点总数 <= 1000
注意：本题与主站 102 题相同：https://leetcode-cn.com/problems/binary-tree-level-order-traversal/
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.res = []
        def dfs(root, deep):
            if not root:
                return []
            if not self.res:
                self.res = [[root.val]]
            else:
                if len(self.res) < deep + 1:
                    self.res.append([root.val])
                else:
                    self.res[deep].append(root.val)
            dfs(root.left, deep + 1)
            dfs(root.right, deep + 1)

        dfs(root, 0)
        return self.res
