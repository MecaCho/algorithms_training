'''
298. 二叉树最长连续序列
给你一棵指定的二叉树，请你计算它最长连续序列路径的长度。

该路径，可以是从某个初始结点到树中任意结点，通过「父 - 子」关系连接而产生的任意路径。

这个最长连续的路径，必须从父结点到子结点，反过来是不可以的。

示例 1：

输入:

   1
    \
     3
    / \
   2   4
        \
         5

输出: 3

解析: 当中，最长连续序列是 3-4-5，所以返回结果为 3
示例 2：

输入:

   2
    \
     3
    /
   2
  /
 1

输出: 2

解析: 当中，最长连续序列是 2-3。注意，不是 3-2-1，所以返回 2。

298. Binary Tree Longest Consecutive Sequence
Given a binary tree, find the length of the longest consecutive sequence path.

The path refers to any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The longest consecutive path need to be from parent to child (cannot be the reverse).

Example 1:

Input:

   1
    \
     3
    / \
   2   4
        \
         5

Output: 3

Explanation: Longest consecutive sequence path is 3-4-5, so return 3.
Example 2:

Input:

   2
    \
     3
    /
   2
  /
 1

Output: 2

Explanation: Longest consecutive sequence path is 2-3, not 3-2-1, so return 2.
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_length = 0
        def dfs(root, val, l):
            if not root:
                return
            if val is not None and root.val == val + 1:
                l += 1
            else:
                l = 1
            self.max_length = max(l, self.max_length)
            dfs(root.left, root.val, l)
            dfs(root.right, root.val, l)
        dfs(root, None, 1)
        return self.max_length


'''
方法 1：自顶向下深度优先搜索
算法

一个自顶向下的搜索方法与中序遍历类似。我们用一个变量 length 保存当前连续的路径长度并将这个变量沿着树传递。当我们遍历的时候，我们比较当前节点和父节点是否是连续的。如果不是，我们将长度重置为 1 。

Java

private int maxLength = 0;
public int longestConsecutive(TreeNode root) {
    dfs(root, null, 0);
    return maxLength;
}

private void dfs(TreeNode p, TreeNode parent, int length) {
    if (p == null) return;
    length = (parent != null && p.val == parent.val + 1) ? length + 1 : 1;
    maxLength = Math.max(maxLength, length);
    dfs(p.left, p, length);
    dfs(p.right, p, length);
}
我们也可以选择不把 maxLength 作为全局变量：

Java

public int longestConsecutive(TreeNode root) {
    return dfs(root, null, 0);
}

private int dfs(TreeNode p, TreeNode parent, int length) {
    if (p == null) return length;
    length = (parent != null && p.val == parent.val + 1) ? length + 1 : 1;
    return Math.max(length, Math.max(dfs(p.left, p, length),
                                     dfs(p.right, p, length)));
}
复杂度分析

时间复杂度： O(n)O(n) 。

时间复杂度与中序遍历 nn 个节点的二叉树相同。

空间复杂度： O(n)O(n) 。

额外使用的空间源于回溯导致的栈空间。对于一个严重偏斜的二叉树，回溯会达到 nn 层的深度。

方法 2：自底向上深度优先搜索
算法

自底向上的方法与后序遍历类似。我们将从当前节点开始的连续路径长度返回给它的父节点。父节点来判断它的值是否能被添加进这个连续路径里。

Java

private int maxLength = 0;
public int longestConsecutive(TreeNode root) {
    dfs(root);
    return maxLength;
}

private int dfs(TreeNode p) {
    if (p == null) return 0;
    int L = dfs(p.left) + 1;
    int R = dfs(p.right) + 1;
    if (p.left != null && p.val + 1 != p.left.val) {
        L = 1;
    }
    if (p.right != null && p.val + 1 != p.right.val) {
        R = 1;
    }
    int length = Math.max(L, R);
    maxLength = Math.max(maxLength, length);
    return length;
}
复杂度分析

时间复杂度： O(n)O(n) 。

时间复杂度与后续遍历二叉树一样都是 O(n)O(n) 。

空间复杂度： O(n)O(n) 。

递归在调用栈的时候会使用额外的空间。对于一棵严重偏斜的二叉树，递归的深度最多达到 nn 层。

作者：LeetCode
链接：https://leetcode-cn.com/problems/binary-tree-longest-consecutive-sequence/solution/er-cha-shu-zui-chang-lian-xu-xu-lie-by-leetcode/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''