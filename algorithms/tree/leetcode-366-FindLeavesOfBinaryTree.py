'''
366. 寻找二叉树的叶子节点
给你一棵二叉树，请按以下要求的顺序收集它的全部节点：

依次从左到右，每次收集并删除所有的叶子节点
重复如上过程直到整棵树为空


示例:

输入: [1,2,3,4,5]

          1
         / \
        2   3
       / \
      4   5

输出: [[4,5,3],[2],[1]]


解释:

1. 删除叶子节点 [4,5,3] ，得到如下树结构：

          1
         /
        2


2. 现在删去叶子节点 [2] ，得到如下树结构：

          1


3. 现在删去叶子节点 [1] ，得到空树：

          []

366. Find Leaves of Binary Tree
Given a binary tree, collect a tree's nodes as if you were doing this: Collect and remove all leaves, repeat until the tree is empty.



Example:

Input: [1,2,3,4,5]

          1
         / \
        2   3
       / \
      4   5

Output: [[4,5,3],[2],[1]]


Explanation:

1. Removing the leaves [4,5,3] would result in this tree:

          1
         /
        2


2. Now removing the leaf [2] would result in this tree:

          1


3. Now removing the leaf [1] would result in the empty tree:

          []
'''



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.vals = []
        def dfs(root):
            if not root:
                return 0

            h = max(dfs(root.left), dfs(root.right)) + 1
            if not self.vals or len(self.vals) < h:
                self.vals.append([root.val])
            else:
                self.vals[h-1].append(root.val)
            return h

        dfs(root)
        return self.vals


#  tips

'''
根据子树的高度来分组的
'''


