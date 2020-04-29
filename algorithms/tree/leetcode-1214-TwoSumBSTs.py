'''
1214. 查找两棵二叉搜索树之和
给出两棵二叉搜索树，请你从两棵树中各找出一个节点，使得这两个节点的值之和等于目标值 Target。

如果可以找到返回 True，否则返回 False。



示例 1：



输入：root1 = [2,1,4], root2 = [1,0,3], target = 5
输出：true
解释：2 加 3 和为 5 。
示例 2：



输入：root1 = [0,-10,10], root2 = [5,1,7,0,2], target = 18
输出：false


提示：

每棵树上最多有 5000 个节点。
-10^9 <= target, node.val <= 10^9

1214. Two Sum BSTs
Given two binary search trees, return True if and only if there is a node in the first tree and a node in the second tree whose values sum up to a given integer target.



Example 1:



Input: root1 = [2,1,4], root2 = [1,0,3], target = 5
Output: true
Explanation: 2 and 3 sum up to 5.
Example 2:



Input: root1 = [0,-10,10], root2 = [5,1,7,0,2], target = 18
Output: false


Constraints:

Each tree has at most 5000 nodes.
-10^9 <= target, node.val <= 10^9
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def twoSumBSTs(self, root1, root2, target):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :type target: int
        :rtype: bool
        """
        self.res = False
        self.hash_map = {}
        def traversal(root, left, right):
            if not root:
                return
            traversal(root.left, left, right)
            if right:
                if root.val in self.hash_map:
                    self.res = True
                    return
            if left:
                self.hash_map[target-root.val] = root.val
            traversal(root.right, left, right)
        traversal(root1, True, False)
        traversal(root2, False, True)
        return self.res
