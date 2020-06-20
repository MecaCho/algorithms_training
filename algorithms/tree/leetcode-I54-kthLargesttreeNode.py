'''
面试题54. 二叉搜索树的第k大节点
给定一棵二叉搜索树，请找出其中第k大的节点。

 

示例 1:

输入: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
输出: 4
示例 2:

输入: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
输出: 4
 

限制：

1 ≤ k ≤ 二叉搜索树元素个数
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthLargest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        def travelsal_tree(root):
            if not root:
                return []
            return travelsal_tree(root.left) + [root.val] + travelsal_tree(root.right)
        val_list = travelsal_tree(root)
        return val_list[::-1][k-1]


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution0(object):
    def kthLargest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        # def travelsal_tree(root):
        #     if not root:
        #         return []
        #     return travelsal_tree(root.left) + [root.val] + travelsal_tree(root.right)
        # val_list = travelsal_tree(root)
        # return val_list[::-1][k-1]


        # self.k = k
        # self.res = None

        # def dfs(root):
        #     if not root:
        #         return
        #     dfs(root.right)
        #     self.k -= 1
        #     if self.k == 0:
        #         self.res = root.val
        #         return
        #     dfs(root.left)

        # dfs(root)
        # return self.res


        # def kthSmallest(root, k):
        # stack = []
        # while root or stack:
        #     while root:
        #         stack.append(root)
        #         root = root.left
        #     root = stack.pop()
        #     k -= 1
        #     if k == 0:
        #         return root.val
        #     root = root.right

        stack = [(0, root)]

        while stack:
            c, node = stack.pop()
            if not node:
                continue
            if c == 1:
                k -= 1
                if k == 0:
                    return node.val
            else:
                stack.append((0, node.left))
                stack.append((1, node))
                stack.append((0, node.right))
