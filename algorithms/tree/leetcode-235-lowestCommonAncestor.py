'''
235. Lowest Common Ancestor of a Binary Search Tree
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Given binary search tree:  root = [6,2,8,0,4,7,9,null,null,3,5]


 

Example 1:

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.
Example 2:

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
 

Note:

All of the nodes' values will be unique.
p and q are different and both values will exist in the BST.

235. 二叉搜索树的最近公共祖先
给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

例如，给定如下二叉搜索树:  root = [6,2,8,0,4,7,9,null,null,3,5]



 

示例 1:

输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
输出: 6 
解释: 节点 2 和节点 8 的最近公共祖先是 6。
示例 2:

输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
输出: 2
解释: 节点 2 和节点 4 的最近公共祖先是 2, 因为根据定义最近公共祖先节点可以为节点本身。
 

说明:

所有节点的值都是唯一的。
p、q 为不同节点且均存在于给定的二叉搜索树中。
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        val_root = root.val
        p_val = min(p.val, q.val)
        q_val = max(p.val, q.val)
        if val_root > q_val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif val_root < p_val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root


# 迭代
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution1(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # val_root = root.val
        p_val = min(p.val, q.val)
        q_val = max(p.val, q.val)
        # if val_root > q_val:
        #     return self.lowestCommonAncestor(root.left, p, q)
        # elif val_root < p_val:
        #     return self.lowestCommonAncestor(root.right, p, q)
        # else:
        #     return root

        while root:
            val_root = root.val
            if val_root > q_val:
                root = root.left
            elif val_root < p_val:
                root = root.right
            else:
                return root


'''
题解
我们来复习一下二叉搜索树（BST）的性质：

节点 NN 左子树上的所有节点的值都小于等于节点 NN 的值
节点 NN 右子树上的所有节点的值都大于等于节点 NN 的值
左子树和右子树也都是 BST
方法一 （递归）
思路

节点 pp，qq 的最近公共祖先（LCA）是距离这两个节点最近的公共祖先节点。在这里 最近 考虑的是节点的深度。下面这张图能帮助你更好的理解 最近 这个词的含义。



笔记：pp 和 qq 其中的一个在 LCA 节点的左子树上，另一个在 LCA 节点的右子树上。

也有可能是下面这种情况：



算法

从根节点开始遍历树
如果节点 pp 和节点 qq 都在右子树上，那么以右孩子为根节点继续 1 的操作
如果节点 pp 和节点 qq 都在左子树上，那么以左孩子为根节点继续 1 的操作
如果条件 2 和条件 3 都不成立，这就意味着我们已经找到节 pp 和节点 qq 的 LCA 了
JavaPython
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # Value of current node or parent node.
        parent_val = root.val

        # Value of p
        p_val = p.val

        # Value of q
        q_val = q.val

        # If both p and q are greater than parent
        if p_val > parent_val and q_val > parent_val:    
            return self.lowestCommonAncestor(root.right, p, q)
        # If both p and q are lesser than parent
        elif p_val < parent_val and q_val < parent_val:    
            return self.lowestCommonAncestor(root.left, p, q)
        # We have found the split point, i.e. the LCA node.
        else:
            return root
复杂度分析

时间复杂度：O(N)O(N)
其中 NN 为 BST 中节点的个数，在最坏的情况下我们可能需要访问 BST 中所有的节点。

空间复杂度：O(N)O(N)
所需开辟的额外空间主要是递归栈产生的，之所以是 NN 是因为 BST 的高度为 NN。

方法二 （迭代）
算法

这个方法跟方法一很接近。唯一的不同是，我们用迭代的方式替代了递归来遍历整棵树。由于我们不需要回溯来找到 LCA 节点，所以我们是完全可以不利用栈或者是递归的。实际上这个问题本身就是可以迭代的，我们只需要找到分割点就可以了。这个分割点就是能让节点 pp 和节点 qq 不能在同一颗子树上的那个节点，或者是节点 pp 和节点 qq 中的一个，这种情况下其中一个节点是另一个节点的父亲节点。

JavaPython
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        # Value of p
        p_val = p.val

        # Value of q
        q_val = q.val

        # Start from the root node of the tree
        node = root

        # Traverse the tree
        while node:

            # Value of current node or parent node.
            parent_val = node.val

            if p_val > parent_val and q_val > parent_val:    
                # If both p and q are greater than parent
                node = node.right
            elif p_val < parent_val and q_val < parent_val:
                # If both p and q are lesser than parent
                node = node.left
            else:
                # We have found the split point, i.e. the LCA node.
                return node
复杂度分析

时间复杂度：O(N)O(N)
其中 NN 为 BST 中节点的个数，在最坏的情况下我们可能需要遍历 BST 中所有的节点。

空间复杂度：O(1)O(1)

'''