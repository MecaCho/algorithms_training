# encoding=utf8


'''
783. 二叉搜索树节点最小距离
给定一个二叉搜索树的根节点 root，返回树中任意两节点的差的最小值。



示例：

输入: root = [4,2,6,1,3,null,null]
输出: 1
解释:
注意，root是树节点对象(TreeNode object)，而不是数组。

给定的树 [4,2,6,1,3,null,null] 可表示为下图:

          4
        /   \
      2      6
     / \
    1   3

最小的差值是 1, 它是节点1和节点2的差值, 也是节点3和节点2的差值。


注意：

二叉树的大小范围在 2 到 100。
二叉树总是有效的，每个节点的值都是整数，且不重复。
本题与 530：https://leetcode-cn.com/problems/minimum-absolute-difference-in-bst/ 相同

783. Minimum Distance Between BST Nodes
Given a Binary Search Tree (BST) with the root node root, return the minimum difference between the values of any two different nodes in the tree.

Example :

Input: root = [4,2,6,1,3,null,null]
Output: 1
Explanation:
Note that root is a TreeNode object, not an array.

The given tree [4,2,6,1,3,null,null] is represented by the following diagram:

          4
        /   \
      2      6
     / \
    1   3

while the minimum difference in this tree is 1, it occurs between node 1 and node 2, also between node 3 and node 2.
Note:

The size of the BST will be between 2 and 100.
The BST is always valid, each node's value is an integer, and each node's value is different.
This question is the same as 530: https://leetcode.com/problems/minimum-absolute-difference-in-bst/
'''




# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.vals = []
        self.min_int = float("inf")
        def traversal(root):
            if not root:
                return
            traversal(root.left)
            self.vals.append(root.val)
            traversal(root.right)
        traversal(root)
        # print(self.vals)
        for i in range(1, len(self.vals)):
            self.min_int = min(self.min_int, self.vals[i]- self.vals[i-1])
        return self.min_int



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution20210413(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        stack = [(0, root)]

        res = float("inf")
        pre = None

        while stack:
            flag, node = stack.pop()
            if node:
                if flag == 0:
                    stack.append((0, node.right))
                    stack.append((1, node))
                    stack.append((0, node.left))
                elif flag == 1:
                    res = min(res, node.val - pre) if pre is not None else res
                    pre = node.val

        return res



'''
方法一：排序【通过】
思路和算法

将树中所有节点的值写入数组，之后将数组排序。依次计算相邻数之间的差值，找出其中最小的值。

JavaPython
class Solution(object):
    def minDiffInBST(self, root):
        vals = []
        def dfs(node):
            if node:
                vals.append(node.val)
                dfs(node.left)
                dfs(node.right)

        dfs(root)
        vals.sort()
        return min(vals[i+1] - vals[i]
                   for i in xrange(len(vals) - 1))
复杂度分析

时间复杂度：O(N \log N)O(NlogN)，其中 NN 是树中节点的个数，其为排序所消耗的时间。

空间复杂度：O(N)O(N)，其为 vals 的大小。

方法二：中序遍历【通过】
思路和算法

在二叉搜索树中，中序遍历会将树中节点按数值大小顺序输出。只需要遍历计算相邻数的差值，取其中最小的就可以了。

JavaPython
class Solution(object):
    def minDiffInBST(self, root):
        def dfs(node):
            if node:
                dfs(node.left)
                self.ans = min(self.ans, node.val - self.prev)
                self.prev = node.val
                dfs(node.right)

        self.prev = float('-inf')
        self.ans = float('inf')
        dfs(root)
        return self.ans
复杂度分析

时间复杂度：O(N)O(N)，其中 NN 为树中节点的个数。

空间复杂度：O(H)O(H)，其中 HH 为树的高度，其为递归调用 dfs 产生函数栈的大小。

作者：LeetCode
链接：https://leetcode-cn.com/problems/minimum-distance-between-bst-nodes/solution/er-cha-sou-suo-shu-jie-dian-zui-xiao-ju-chi-by-lee/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
