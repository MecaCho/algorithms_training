# encoding=utf8

'''
230. Kth Smallest Element in a BST
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

 

Example 1:


Input: root = [3,1,4,null,2], k = 1
Output: 1
Example 2:


Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
 

Constraints:

The number of nodes in the tree is n.
1 <= k <= n <= 104
0 <= Node.val <= 104
 

Follow up: If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?



230. 二叉搜索树中第K小的元素
给定一个二叉搜索树的根节点 root ，和一个整数 k ，请你设计一个算法查找其中第 k 个最小元素（从 1 开始计数）。

 

示例 1：


输入：root = [3,1,4,null,2], k = 1
输出：1
示例 2：


输入：root = [5,3,6,2,4,null,null,1], k = 3
输出：3
 

 

提示：

树中的节点数为 n 。
1 <= k <= n <= 104
0 <= Node.val <= 104
 

进阶：如果二叉搜索树经常被修改（插入/删除操作）并且你需要频繁地查找第 k 小的值，你将如何优化算法？
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        # stack = [(0, root)]
        # while stack:
        #     c, node = stack.pop()
        #     if not node:
        #         continue
        #     if c == 1:
        #         k -= 1
        #         if k == 0:
        #             return node.val
        #     else:
        #         stack.append((0, node.right))
        #         stack.append((1, node))
        #         stack.append((0, node.left))

        # Runtime: 32 ms, faster than 99.19% of Python online submissions for Kth Smallest Element in a BST.
        # Memory Usage: 20.7 MB, less than 53.08% of Python online submissions for Kth Smallest Element in a BST.

        self.k = k
        self.res = None

        def dfs(root):
            if not root:
                return
            dfs(root.left)
            self.k -= 1
            if self.k == 0:
                self.res = root.val
                return
            dfs(root.right)

        dfs(root)
        return self.res
# Runtime: 52 ms, faster than 50.67% of Python online submissions for Kth Smallest Element in a BST.
# Memory Usage: 20.7 MB, less than 37.76% of Python online submissions for Kth Smallest Element in a BST.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
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
                stack.append((0, node.right))
                stack.append((1, node))
                stack.append((0, node.left))
