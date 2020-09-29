'''
145. 二叉树的后序遍历
给定一个二叉树，返回它的 后序 遍历。

示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [3,2,1]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？

145. Binary Tree Postorder Traversal
Given a binary tree, return the postorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [3,2,1]
Follow up: Recursive solution is trivial, could you do it iteratively?

'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val] if root else []


#  迭代

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution1(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val] if root else []

        stack_t = [root]

        res = []

        while stack_t:
            node = stack_t.pop()
            if node:
                res.append(node.val)
                if node.left:
                    stack_t.append(node.left)
                if node.right:
                    stack_t.append(node.right)
        return res[::-1]


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution20200929(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val] if root else []

        stack = []
        stack.append((0, root))
        vals = []
        while stack:
            flag, node = stack.pop()
            if node:
                if flag:
                    vals.append(node.val)
                else:
                    stack.append((1, node))
                    stack.append((0, node.right))
                    stack.append((0, node.left))

        return vals


# solutions

'''
如何遍历一棵树
有两种通用的遍历树的策略：

深度优先搜索（DFS）

在这个策略中，我们采用深度作为优先级，以便从跟开始一直到达某个确定的叶子，然后再返回根到达另一个分支。

深度优先搜索策略又可以根据根节点、左孩子和右孩子的相对顺序被细分为先序遍历，中序遍历和后序遍历。

宽度优先搜索（BFS）

我们按照高度顺序一层一层的访问整棵树，高层次的节点将会比低层次的节点先被访问到。

下图中的顶点按照访问的顺序编号，按照 1-2-3-4-5 的顺序来比较不同的策略。



本问题就是用宽度优先搜索遍历来划分层次：[[1], [2, 3], [4, 5]]。

方法 1：迭代
算法

首先，定义树的存储结构 TreeNode。

JavaPython

class TreeNode(object):
    """ Definition of a binary tree node."""
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
从根节点开始依次迭代，弹出栈顶元素输出到输出列表中，然后依次压入它的所有孩子节点，按照从上到下、从左至右的顺序依次压入栈中。

因为深度优先搜索后序遍历的顺序是从下到上、从左至右，所以需要将输出列表逆序输出。

JavaPython

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []

        stack, output = [root, ], []
        while stack:
            root = stack.pop()
            output.append(root.val)
            if root.left is not None:
                stack.append(root.left)
            if root.right is not None:
                stack.append(root.right)
                
        return output[::-1]
复杂度分析

时间复杂度：访问每个节点恰好一次，因此时间复杂度为 O(N)O(N)，其中 NN 是节点的个数，也就是树的大小。
空间复杂度：取决于树的结构，最坏情况需要保存整棵树，因此空间复杂度为 O(N)O(N)。

作者：LeetCode
链接：https://leetcode-cn.com/problems/binary-tree-postorder-traversal/solution/er-cha-shu-de-hou-xu-bian-li-by-leetcode/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
