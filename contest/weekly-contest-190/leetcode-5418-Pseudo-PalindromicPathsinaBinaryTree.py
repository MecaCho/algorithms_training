
'''
5418. 二叉树中的伪回文路径
给你一棵二叉树，每个节点的值为 1 到 9 。我们称二叉树中的一条路径是 「伪回文」的，当它满足：路径经过的所有节点值的排列中，存在一个回文序列。

请你返回从根到叶子节点的所有路径中 伪回文 路径的数目。



示例 1：



输入：root = [2,3,1,3,1,null,1]
输出：2
解释：上图为给定的二叉树。总共有 3 条从根到叶子的路径：红色路径 [2,3,3] ，绿色路径 [2,1,1] 和路径 [2,3,1] 。
     在这些路径中，只有红色和绿色的路径是伪回文路径，因为红色路径 [2,3,3] 存在回文排列 [3,2,3] ，绿色路径 [2,1,1] 存在回文排列 [1,2,1] 。
示例 2：



输入：root = [2,1,1,1,3,null,null,null,null,null,1]
输出：1
解释：上图为给定二叉树。总共有 3 条从根到叶子的路径：绿色路径 [2,1,1] ，路径 [2,1,3,1] 和路径 [2,1] 。
     这些路径中只有绿色路径是伪回文路径，因为 [2,1,1] 存在回文排列 [1,2,1] 。
示例 3：

输入：root = [9]
输出：1


提示：

给定二叉树的节点数目在 1 到 10^5 之间。
节点值在 1 到 9 之间。


5418. Pseudo-Palindromic Paths in a Binary Tree
Given a binary tree where node values are digits from 1 to 9. A path in the binary tree is said to be pseudo-palindromic if at least one permutation of the node values in the path is a palindrome.

Return the number of pseudo-palindromic paths going from the root node to leaf nodes.



Example 1:



Input: root = [2,3,1,3,1,null,1]
Output: 2
Explanation: The figure above represents the given binary tree. There are three paths going from the root node to leaf nodes: the red path [2,3,3], the green path [2,1,1], and the path [2,3,1]. Among these paths only red path and green path are pseudo-palindromic paths since the red path [2,3,3] can be rearranged in [3,2,3] (palindrome) and the green path [2,1,1] can be rearranged in [1,2,1] (palindrome).
Example 2:



Input: root = [2,1,1,1,3,null,null,null,null,null,1]
Output: 1
Explanation: The figure above represents the given binary tree. There are three paths going from the root node to leaf nodes: the green path [2,1,1], the path [2,1,3,1], and the path [2,1]. Among these paths only the green path is pseudo-palindromic since [2,1,1] can be rearranged in [1,2,1] (palindrome).
Example 3:

Input: root = [9]
Output: 1


Constraints:

The given binary tree will have between 1 and 10^5 nodes.
Node values are digits from 1 to 9.
'''


import collections

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def pseudoPalindromicPaths (self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.vals = []
        def dfs(root, res):
            if not root:
                return
            res.append(root.val)
            if not root.left and not root.right:
                self.vals.append(res)
                return
            new_res = res[:]
            if root.left:
                dfs(root.left, res[:])
                # return
            if root.right:
                dfs(root.right, new_res)
        def isPalindrom(s):
            hash_map = collections.defaultdict(int)
            for c in s:
                hash_map[c] += 1
            num = 0
            for k, v in hash_map.items():
                if v % 2== 1:
                    num += 1
            if num > 1:
                return False
            return True
        dfs(root, [])
        # print(self.vals)
        res = 0
        for val in self.vals:
            if isPalindrom(val):
                res += 1
        return res

import math

if __name__ == '__main__':
    res = "111".rjust(8, "0")
    print(res)
    print(int(math.log(1000, 2)))
    a = 9
    print(bin(a), a.bit_length())
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class SolutionNum2(object):
    def pseudoPalindromicPaths (self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        r = [0]
        s = set()
        def toggle(elem):
            if elem in s: s.remove(elem)
            else: s.add(elem)
        def dfs(u):
            if not u: return
            toggle(u.val)
            if not u.left and not u.right and len(s) <= 1: r[0] += 1
            if u.left: dfs(u.left)
            if u.right: dfs(u.right)
            toggle(u.val)
        dfs(root)
        return r[0]

# tips

'''
Note that the node values of a path form a palindrome if at most one digit has an odd frequency (parity).

Use a Depth First Search (DFS) keeping the frequency (parity) of the digits. Once you are in a leaf node check if at most one digit has an odd frequency (parity).
'''