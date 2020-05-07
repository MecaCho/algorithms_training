'''
687. 最长同值路径
给定一个二叉树，找到最长的路径，这个路径中的每个节点具有相同值。 这条路径可以经过也可以不经过根节点。

注意：两个节点之间的路径长度由它们之间的边数表示。

示例 1:

输入:

              5
             / \
            4   5
           / \   \
          1   1   5
输出:

2
示例 2:

输入:

              1
             / \
            4   5
           / \   \
          4   4   5
输出:

2
注意: 给定的二叉树不超过10000个结点。 树的高度不超过1000。


687. Longest Univalue Path
Given a binary tree, find the length of the longest path where each node in the path has the same value. This path may or may not pass through the root.

The length of path between two nodes is represented by the number of edges between them.



Example 1:

Input:

              5
             / \
            4   5
           / \   \
          1   1   5
Output: 2



Example 2:

Input:

              1
             / \
            4   5
           / \   \
          4   4   5
Output: 2



Note: The given binary tree has not more than 10000 nodes. The height of the tree is not more than 1000.
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        def dfs(root, val, deepth):
            # deepth计算路径，f父节点，跟父节点相同就+1，不同就剪枝
            if root:
                root_val = root.val
                left = dfs(root.left, root_val, deepth)
                right = dfs(root.right, root_val, deepth)
                self.res = max(self.res, left + right)
                if val == root_val:
                    return max(left, right) + 1
            return 0

        dfs(root, None, 0)
        return self.res
        # # self.vals = []
        # # def dfs(root, res):
        # #     if not root:
        # #         return res
        # #     else:
        # #         root_val = root.val
        # #         left = dfs(root.left, [])
        # #         right = dfs(root.right, [])
        # #         tmp = left + [root_val] + right
        # #         self.vals.append(tmp)
        # #         return tmp
        # # dfs(root, [])
        # # print(self.vals)
        # # return max([len(i) for i in self.vals if len(set(i)) == 1])

        # self.count = 0
        # self.max_deepth = 0
        # def dfs(root, deepth):
        #     if not root:
        #         return deepth
        #     else:
        #         root_val = root.val

        #         left_deepth = 0
        #         if root.left and root.left.val == root_val:
        #             left_deepth = dfs(root.left, deepth) + 1
        #         else:
        #             left_deepth = dfs(root.left, 0)

        #         right_deepth = 0
        #         if root.right and root.right.val == root_val:
        #             right_deepth = dfs(root.right, deepth) + 1
        #         else:
        #             right_deepth = dfs(root.right, 0)

        #         print(root_val, self.max_deepth, right_deepth, left_deepth)
        #         self.max_deepth = max([self.max_deepth, right_deepth+left_deepth])
        #         return max(right_deepth, left_deepth)

        # dfs(root, 0)
        # # print(self.count)
        # return self.max_deepth

'''
方法：递归
思路

我们可以将任何路径（具有相同值的节点）看作是最多两个从其根延伸出的箭头。

具体地说，路径的根将是唯一节点，因此该节点的父节点不会出现在该路径中，而箭头将是根在该路径中只有一个子节点的路径。

然后，对于每个节点，我们想知道向左延伸的最长箭头和向右延伸的最长箭头是什么？我们可以用递归来解决这个问题。

算法

令 arrow_length(node) 为从节点 node 延伸出的最长箭头的长度。如果 node.Left 存在且与节点 node 具有相同的值，则该值就会是 1 + arrow_length(node.left)。在 node.right 存在的情况下也是一样。

当我们计算箭头长度时，候选答案将是该节点在两个方向上的箭头之和。我们将这些候选答案记录下来，并返回最佳答案。

JavaPython
class Solution(object):
    def longestUnivaluePath(self, root):
        self.ans = 0

        def arrow_length(node):
            if not node: 
                return 0
            left_length = arrow_length(node.left)
            right_length = arrow_length(node.right)
            left_arrow = right_arrow = 0
            if node.left and node.left.val == node.val:
                left_arrow = left_length + 1
            if node.right and node.right.val == node.val:
                right_arrow = right_length + 1
            self.ans = max(self.ans, left_arrow + right_arrow)
            return max(left_arrow, right_arrow)

        arrow_length(root)
        return self.ans
复杂度分析

时间复杂度：O(N)O(N)，其中 NN 是树中节点数。我们处理每个节点一次。

空间复杂度：O(H)O(H)，其中 HH 是树的高度。我们的递归调用栈可以达到 HH 层的深度。

作者：LeetCode
链接：https://leetcode-cn.com/problems/longest-univalue-path/solution/zui-chang-tong-zhi-lu-jing-by-leetcode/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''