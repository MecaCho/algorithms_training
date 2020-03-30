
'''

912. 排序数组
给定一个整数数组 nums，将该数组升序排列。

 

示例 1：

输入：[5,2,3,1]
输出：[1,2,3,5]
示例 2：

输入：[5,1,1,2,0,0]
输出：[0,0,1,1,2,5]
 

提示：

1 <= A.length <= 10000
-50000 <= A[i] <= 50000

912. Sort an Array
Given an array of integers nums, sort the array in ascending order.

 

Example 1:

Input: nums = [5,2,3,1]
Output: [1,2,3,5]
Example 2:

Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]
 

Constraints:

1 <= nums.length <= 50000
-50000 <= nums[i] <= 50000
'''





class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return nums
        # left = []
        # right = []
        # for num in nums[1:]:
        #     if num > nums[0]:
        #         right.append(num)
        #     else:
        #         left.append(num)
        # return self.sortArray(left) + [nums[0]] + self.sortArray(right)
        return self.sortArray([i for i in nums[1:] if i < nums[0]]) + [nums[0]] + self.sortArray([i for i in nums[1:] if i >= nums[0]])
        # return sorted(nums)

