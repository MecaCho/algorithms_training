'''

101. Symmetric Tree
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
 

But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3
 

Note:
Bonus points if you could solve it both recursively and iteratively.


101. 对称二叉树
给定一个二叉树，检查它是否是镜像对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3
但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3
说明:

如果你可以运用递归和迭代两种方法解决这个问题，会很加分。
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # val_list = []
        def dfs(root, res=[]):
            if not root:
                return [None]
            l = dfs(root.left)
            r = dfs(root.right)
            if l or r:
                l = [None] if not l else l
                r = [None] if not r else r
            return l + [root.val] + r

        def root_trave_pre(q, res=[]):
            if not q:
                return []
            l = root_trave_pre(q.left)
            r = root_trave_pre(q.right)
            if not l and r:
                l = [None]
            res =  r + l + [q.val]
            return res

        def root_trave_pro(q, res=[]):
            if not q:
                return []
            l = root_trave_pro(q.left)
            r = root_trave_pro(q.right)
            if not r and l:
                r = [None]
            res =  l + r + [q.val]
            return res

        pre_vals = root_trave_pro(root)
        pro_vals = root_trave_pre(root)
        return pre_vals == pro_vals