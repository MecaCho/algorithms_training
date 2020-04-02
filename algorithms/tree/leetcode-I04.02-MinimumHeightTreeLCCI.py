

'''
面试题 04.02. 最小高度树
给定一个有序整数数组，元素各不相同且按升序排列，编写一个算法，创建一棵高度最小的二叉搜索树。

示例:
给定有序数组: [-10,-3,0,5,9],

一个可能的答案是：[0,-3,9,-10,null,5]，它可以表示下面这个高度平衡二叉搜索树：

          0 
         / \ 
       -3   9 
       /   / 
     -10  5 
     
面试题 04.02. Minimum Height Tree LCCI
Given a sorted (increasing order) array with unique integer elements, write an algo­rithm to create a binary search tree with minimal height.

Example:

Given sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5]，which represents the following tree: 

          0 
         / \ 
       -3   9 
       /   / 
     -10  5 

'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        mid = len(nums) / 2
        new_node = TreeNode(nums[mid])
        new_node.left = self.sortedArrayToBST(nums[:mid])
        new_node.right = self.sortedArrayToBST(nums[mid+1:])
        return new_node
