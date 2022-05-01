# encoding=utf8

'''
1305. All Elements in Two Binary Search Trees
Given two binary search trees root1 and root2, return a list containing all the integers from both trees sorted in ascending order.

 

Example 1:


Input: root1 = [2,1,4], root2 = [1,0,3]
Output: [0,1,1,2,3,4]
Example 2:


Input: root1 = [1,null,8], root2 = [8,1]
Output: [1,1,8,8]
 

Constraints:

The number of nodes in each tree is in the range [0, 5000].
-105 <= Node.val <= 105
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getAllElements(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: List[int]
        """
        def mid(root, vals):
            if not root:
                return 
            mid(root.left, vals)
            vals.append(root.val)
            mid(root.right, vals)

        nums1, nums2 = [], []
        mid(root1, nums1)
        mid(root2, nums2)
        n1, n2 = len(nums1), len(nums2)
        nums = []
        p1, p2 = 0, 0
        while nums1 or nums2:
            if p1 == n1:
                nums.extend(nums2[p2:])
                break
            if p2 == n2:
                nums.extend(nums1[p1:])
                break
            if nums1[p1] < nums2[p2]:
                nums.append(nums1[p1])
                p1 += 1
            else:
                nums.append(nums2[p2])
                p2 += 1
        return nums
      
