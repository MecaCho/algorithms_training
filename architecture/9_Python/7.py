
class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution(object):

    def __init__(self):
        pass


    def tree_nodes(self, root):
        self.vals = []

        def dfs(root, deepth):
            if not root:
                return
            if not self.vals or len(self.vals) < deepth +1:
                self.vals.append([root.val])
            else:
                self.vals[deepth].append(root.val)
            dfs(root.left, deepth + 1)
            dfs(root.right, deepth + 1)

        dfs(root, 0)

        res = []
        for i in range(len(self.vals)):
            if i % 2 == 0:
                res.extend(self.vals[i])
            else:
                res.extend(self.vals[i][::-1])
        return res


if __name__ == '__main__':
    demo = Solution()
    node = TreeNode(1)
    node1 = TreeNode(2)
    node2 = TreeNode(3)
    node.left = node1
    node.right = node2
    res = demo.tree_nodes(node)
    print(res)

# [1], [2,3], [4,5,6]