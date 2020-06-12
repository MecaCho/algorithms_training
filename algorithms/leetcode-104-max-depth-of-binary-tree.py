'''
104. 二叉树的最大深度
给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

说明: 叶子节点是指没有子节点的节点。

示例：
给定二叉树 [3,9,20,null,null,15,7]，

    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3 。

104. Maximum Depth of Binary Tree
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# 递归

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1 if root else 0


# 迭代

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution1(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # stack = []
        # if root:
        #     stack.append((1, root))
        # deepth = 0
        # while stack:
        #     cur, node = stack.pop()
        #     deepth = max(deepth, cur)
        #     if node.left:
        #         stack.append((cur+1, node.left))
        #     if node.right:
        #         stack.append((cur+1, node.right))
        # return deepth


# solutions

'''
树的定义

首先，给出我们将要使用的树的结点 TreeNode 的定义。

JavaPython

  /* Definition for a binary tree node. */
  public class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode(int x) {
      val = x;
    }
  }
方法一：递归
算法


1 / 10

直观的方法是通过递归来解决问题。在这里，我们演示了 DFS（深度优先搜索）策略的示例。

JavaPython

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """ 
        if root is None: 
            return 0 
        else: 
            left_height = self.maxDepth(root.left) 
            right_height = self.maxDepth(root.right) 
            return max(left_height, right_height) + 1 
复杂度分析

时间复杂度：我们每个结点只访问一次，因此时间复杂度为 O(N)O(N)，
其中 NN 是结点的数量。
空间复杂度：在最糟糕的情况下，树是完全不平衡的，例如每个结点只剩下左子结点，递归将会被调用 NN 次（树的高度），因此保持调用栈的存储将是 O(N)O(N)。但在最好的情况下（树是完全平衡的），树的高度将是 \log(N)log(N)。因此，在这种情况下的空间复杂度将是 O(\log(N))O(log(N))。
方法二：迭代
我们还可以在栈的帮助下将上面的递归转换为迭代。

我们的想法是使用 DFS 策略访问每个结点，同时在每次访问时更新最大深度。

所以我们从包含根结点且相应深度为 1 的栈开始。然后我们继续迭代：将当前结点弹出栈并推入子结点。每一步都会更新深度。

JavaPython

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """ 
        stack = []
        if root is not None:
            stack.append((1, root))
        
        depth = 0
        while stack != []:
            current_depth, root = stack.pop()
            if root is not None:
                depth = max(depth, current_depth)
                stack.append((current_depth + 1, root.left))
                stack.append((current_depth + 1, root.right))
        
        return depth
复杂度分析

时间复杂度：O(N)O(N)。
空间复杂度：O(N)O(N)。

作者：LeetCode
链接：https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/solution/er-cha-shu-de-zui-da-shen-du-by-leetcode/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''