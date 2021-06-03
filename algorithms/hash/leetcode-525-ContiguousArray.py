# encoding=utf8


'''
525. Contiguous Array

Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

 

Example 1:

Input: nums = [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
Example 2:

Input: nums = [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.


525. 连续数组

给定一个二进制数组 nums , 找到含有相同数量的 0 和 1 的最长连续子数组，并返回该子数组的长度。

 

示例 1:

输入: nums = [0,1]
输出: 2
说明: [0, 1] 是具有相同数量0和1的最长连续子数组。
示例 2:

输入: nums = [0,1,0]
输出: 2
说明: [0, 1] (或 [1, 0]) 是具有相同数量0和1的最长连续子数组。
 

提示：

1 <= nums.length <= 105
nums[i] 不是 0 就是 1
'''


class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        map = {0: -1}
        counter = 0
        res = 0
        for i in range(len(nums)):
            if nums[i]:
                counter += 1
            else:
                counter -= 1
            
            if map.get(counter) is None:
                map[counter] = i
            else:
                pre_index = map[counter]
                res = max(res, i-pre_index)

        return res


