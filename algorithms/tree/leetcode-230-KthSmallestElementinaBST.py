'''

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