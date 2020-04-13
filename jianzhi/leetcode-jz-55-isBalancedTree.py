'''
面试题55 - II. 平衡二叉树
输入一棵二叉树的根节点，判断该树是不是平衡二叉树。如果某二叉树中任意节点的左右子树的深度相差不超过1，那么它就是一棵平衡二叉树。



示例 1:

给定二叉树 [3,9,20,null,null,15,7]

    3
   / \
  9  20
    /  \
   15   7
返回 true 。

示例 2:

给定二叉树 [1,2,2,3,3,null,null,4,4]

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
返回 false 。



限制：

1 <= 树的结点个数 <= 10000
注意：本题与主站 110 题相同：https://leetcode-cn.com/problems/balanced-binary-tree/

# https://leetcode-cn.com/problems/ping-heng-er-cha-shu-lcof/
'''




# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.res = True
        def deepth(root):
            if not root:
                return 0
            left = deepth(root.left)
            right = deepth(root.right)
            if abs(left-right) > 1:
                self.res = False
            return max(left, right) + 1
        deepth(root)
        return self.res

#     class Solution(object):
#     def isBalanced(self, root):
#         """
#         :type root: TreeNode
#         :rtype: bool
#         """
#             def recur(root):
#             if not root: return 0
#             left = recur(root.left)
#             if left == -1: return -1
#             right = recur(root.right)
#             if right == -1: return -1
#             return max(left, right) + 1 if abs(left - right) <= 1 else -1
#
#         return recur(root) != -1
#
