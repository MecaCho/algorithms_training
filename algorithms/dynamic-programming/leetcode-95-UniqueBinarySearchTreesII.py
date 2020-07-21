'''
95. Unique Binary Search Trees II
Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.

Example:

Input: 3
Output:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
Explanation:
The above output corresponds to the 5 unique BST's shown below:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3


Constraints:

0 <= n <= 8

95. 不同的二叉搜索树 II
给定一个整数 n，生成所有由 1 ... n 为节点所组成的 二叉搜索树 。



示例：

输入：3
输出：
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
解释：
以上的输出对应以下 5 种不同结构的二叉搜索树：

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3


提示：

0 <= n <= 8
'''



# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if not n:
            return []
        def generate(first, last):
            trees = []
            for root in range(first, last+1):
                for left in generate(first, root-1):
                    for right in generate(root+1, last):
                        node = TreeNode(root)
                        node.left = left
                        node.right = right
                        trees += node,
            return trees or [None]
        return generate(1, n)


# solutions

'''
If only LeetCode had a TreeNode(val, left, right) constructor... sigh. Then I wouldn't need to provide my own and my solution would be six lines instead of eleven.

def generateTrees(self, n):
    def node(val, left, right):
        node = TreeNode(val)
        node.left = left
        node.right = right
        return node
    def trees(first, last):
        return [node(root, left, right)
                for root in range(first, last+1)
                for left in trees(first, root-1)
                for right in trees(root+1, last)] or [None]
    return trees(1, n)
Or even just four lines, if it's not forbidden to add an optional argument:

def node(val, left, right):
    node = TreeNode(val)
    node.left = left
    node.right = right
    return node

class Solution:
    def generateTrees(self, last, first=1):
        return [node(root, left, right)
                for root in range(first, last+1)
                for left in self.generateTrees(root-1, first)
                for right in self.generateTrees(last, root+1)] or [None]
Just another version, using loops instead of list comprehension:

def generateTrees(self, n):
    def generate(first, last):
        trees = []
        for root in range(first, last+1):
            for left in generate(first, root-1):
                for right in generate(root+1, last):
                    node = TreeNode(root)
                    node.left = left
                    node.right = right
                    trees += node,
        return trees or [None]
    return generate(1, n)
'''