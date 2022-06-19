# encoding=utf8

'''
508. Most Frequent Subtree Sum
Given the root of a tree, you are asked to find the most frequent subtree sum. The subtree sum of a node is defined as the sum of all the node values formed by the subtree rooted at that node (including the node itself). So what is the most frequent subtree sum value? If there is a tie, return all the values with the highest frequency in any order.

Examples 1
Input:

  5
 /  \
2   -3
return [2, -3, 4], since all the values happen only once, return all of them in any order.
Examples 2
Input:

  5
 /  \
2   -5
return [2], since 2 happens twice, however -5 only occur once.
Note: You may assume the sum of values in any subtree is in the range of 32-bit signed integer.

508. 出现次数最多的子树元素和
给你一个二叉树的根结点，请你找出出现次数最多的子树元素和。一个结点的「子树元素和」定义为以该结点为根的二叉树上所有结点的元素之和（包括结点本身）。

你需要返回出现次数最多的子树元素和。如果有多个元素出现的次数相同，返回所有出现次数最多的子树元素和（不限顺序）。



示例 1：
输入:

  5
 /  \
2   -3
返回 [2, -3, 4]，所有的值均只出现一次，以任意顺序返回所有值。

示例 2：
输入：

  5
 /  \
2   -5
返回 [2]，只有 2 出现两次，-5 只出现 1 次。



提示： 假设任意子树元素和均可以用 32 位有符号整数表示。
'''





# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        self.vals = defaultdict(int)
        def dfs(root, res):
            if not root:
                return res
            else:
                root_val = root.val
                left = dfs(root.left, 0)
                right = dfs(root.right, 0)
                # print(root_val, left, right)
                self.vals[left+right+root_val] += 1
                # self.vals[left] += 1
                # self.vals[right] += 1
                return left+right+root_val

        dfs(root, 0)
        # print(self.vals)
        max_val = max(self.vals.values())
        return [k for k, v in self.vals.items() if v == max_val]
      
      
      
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.vals = {}
        def dfs(root):
            if not root:
                return 0

            val = root.val
            left_sum = dfs(root.left)
            right_sum = dfs(root.right)

            key = val+left_sum+right_sum
            if key in self.vals:
                self.vals[key] += 1
            else:
                self.vals[key] = 1
            return key

        dfs(root)
        # print(self.vals)
        max_val = max(self.vals.values())
        return [k for k,v in self.vals.items() if v == max_val] 

