'''
111. Minimum Depth of Binary Tree
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.

111. 二叉树的最小深度
给定一个二叉树，找出其最小深度。

最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

说明: 叶子节点是指没有子节点的节点。

示例:

给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回它的最小深度  2.
'''



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def deep_trave(root):
            if not root:
                return 0
            if not root.left:
                return deep_trave(root.right) + 1
            if not root.right:
                return deep_trave(root.left) + 1
            return min(deep_trave(root.left), deep_trave(root.right)) + 1
        return deep_trave(root)


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution1(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if not root.left:
            return self.minDepth(root.right) + 1
        if not root.right:
            return self.minDepth(root.left) + 1
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1


# solutions

'''
树的定义

首先，定义树节点结构 TreeNode 。

JavaPython

// Definition for a binary tree node.
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

最直接的思路就是递归。

我们用深度优先搜索来解决这个问题。

JavaPython

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        children = [root.left, root.right]
        # if we're at leaf node
        if not any(children):
            return 1

        min_depth = float('inf')
        for c in children:
            if c:
                min_depth = min(self.minDepth(c), min_depth)
        return min_depth + 1
复杂度分析

时间复杂度：我们访问每个节点一次，时间复杂度为 O(N)O(N) ，其中 NN 是节点个数。
空间复杂度：最坏情况下，整棵树是非平衡的，例如每个节点都只有一个孩子，递归会调用 NN （树的高度）次，因此栈的空间开销是 O(N)O(N) 。但在最好情况下，树是完全平衡的，高度只有 \log(N)log(N)，因此在这种情况下空间复杂度只有 O(\log(N))O(log(N)) 。
方法二：深度优先搜索迭代
我们可以利用栈将上述解法中的递归变成迭代。

想法是对于每个节点，按照深度优先搜索的策略访问，同时在访问到叶子节点时更新最小深度。

我们从一个包含根节点的栈开始，当前深度为 1 。

然后开始迭代：弹出当前栈顶元素，将它的孩子节点压入栈中。当遇到叶子节点时更新最小深度。

JavaPython

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        else:
            stack, min_depth = [(1, root),], float('inf')

        while stack:
            depth, root = stack.pop()
            children = [root.left, root.right]
            if not any(children):
                min_depth = min(depth, min_depth)
            for c in children:
                if c:
                    stack.append((depth + 1, c))

        return min_depth
复杂度分析

时间复杂度：每个节点恰好被访问一遍，复杂度为 O(N)O(N)。
空间复杂度：最坏情况下我们会在栈中保存整棵树，此时空间复杂度为 O(N)O(N)。
方法二：广度优先搜索迭代
深度优先搜索方法的缺陷是所有节点都必须访问到，以保证能够找到最小深度。因此复杂度是 O(N)O(N) 。

一个优化的方法是利用广度优先搜索，我们按照树的层去迭代，第一个访问到的叶子就是最小深度的节点，这样就不用遍历所有的节点了。

JavaPython

from collections import deque
class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        else:
            node_deque = deque([(1, root),])

        while node_deque:
            depth, root = node_deque.popleft()
            children = [root.left, root.right]
            if not any(children):
                return depth
            for c in children:
                if c:
                    node_deque.append((depth + 1, c))
复杂度分析

时间复杂度：最坏情况下，这是一棵平衡树，我们需要按照树的层次一层一层的访问完所有节点，除去最后一层的节点。这样访问了 N/2N/2 个节点，因此复杂度是 O(N)O(N)。
空间复杂度：和时间复杂度相同，也是 O(N)O(N)。

作者：LeetCode
链接：https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/solution/er-cha-shu-de-zui-xiao-shen-du-by-leetcode/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''