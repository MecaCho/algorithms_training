
'''
112. 路径总和
给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。

说明: 叶子节点是指没有子节点的节点。

示例:
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
返回 true, 因为存在目标和为 22 的根节点到叶子节点的路径 5->4->11->2。

112. Path Sum
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
'''




# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        self.res = False

        def dfs(root, target):
            if not root.left and not root.right:
                if root.val == target:
                    self.res = True
            if root.left:
                dfs(root.left, target - root.val)
            if root.right:
                dfs(root.right, target - root.val)

        if not root:
            return False
        dfs(root, sum)
        return self.res


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution1(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        def dfs(root, target):
            if not root:
                return
            if root.val == target:
                return True
            dfs(root.left, target - root.val)
            dfs(root.right, target - root.val)
        return dfs(root, sum) is True
        # self.res = False
        # def dfs(root, target):
        #     if not root.left and not root.right:
        #         if root.val == target:
        #             self.res = True
        #     if root.left:
        #         dfs(root.left, target-root.val)
        #     if root.right:
        #         dfs(root.right, target-root.val)
        # if not root:
        #     return False
        # dfs(root, sum)
        # return self.res


class Solution2(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        if not root.left and not root.right and root.val == sum:
            return True
        return self.hasPathSum(root.left, sum-root.val) or self.hasPathSum(root.right, sum-root.val)

# golang

'''
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func hasPathSum(root *TreeNode, sum int) bool {

    if root == nil{
        return false
    }
    if root.Left == nil && root.Right == nil && root.Val == sum{
        return true
    }

    return hasPathSum(root.Left, sum-root.Val) || hasPathSum(root.Right, sum-root.Val)

}
'''
