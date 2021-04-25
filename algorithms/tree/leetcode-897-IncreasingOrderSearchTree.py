# encoding=utf8


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def inorder(root):

            stack = [(0, root)]
            self.vals = []

            while stack:
                flag, node = stack.pop()
                if node:
                    if flag == 1:
                        self.vals.append(node.val)
                    else:
                        stack.append((0, node.right))
                        stack.append((1, node))
                        stack.append((0, node.left))
            return self.vals

        inorder(root)
        # print(self.vals)
        node = TreeNode(0)
        pre = node
        for i in range(len(self.vals)):
            node.right = TreeNode(self.vals[i])
            node.left = None
            node = node.right
        return pre.right


