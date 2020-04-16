
'''
面试题32 - III. 从上到下打印二叉树 III
请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。



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
  [20,9],
  [15,7]
]


提示：

节点总数 <= 1000
通过次数8,894提交次数14,907
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
        res = []
        def dfs(root, deep):
            if not root:
                return
            if len(res) < deep + 1:
                res.append([])

            res[deep].append(root.val)
            dfs(root.left, deep+1)
            dfs(root.right, deep+1)
        dfs(root, 0)
        # nums = []
        # print(res)
        for i in range(len(res)):
            # l = res[i] if i % 2 == 0 else res[i][::-1]
            if i % 2 == 1:
                res[i] = res[i][::-1]

        return res