
'''
面试题32 - I. 从上到下打印二叉树
从上到下打印出二叉树的每个节点，同一层的节点按照从左到右的顺序打印。



例如:
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回：

[3,9,20,15,7]


提示：

节点总数 <= 1000
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
        :rtype: List[int]
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
        nums = []
        # print(res)
        for l in res:
            nums.extend(l)
        return nums