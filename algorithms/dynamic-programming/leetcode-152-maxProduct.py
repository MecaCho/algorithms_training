'''
152. Maximum Product Subarray
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

152. 乘积最大子数组
给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字）。

 

示例 1:

输入: [2,3,-2,4]
输出: 6
解释: 子数组 [2,3] 有最大乘积 6。
示例 2:

输入: [-2,0,-1]
输出: 0
解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。
'''


# 动态规划
class Solution1(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_val = nums[0]
        min_val = nums[0]

        dp = [[nums[0],nums[0]]]
        res = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < 0:
                min_val = min(dp[i-1][1] * nums[i], nums[i])
                max_val = max(dp[i-1][0] * nums[i], nums[i])
            else:
                min_val = min(dp[i-1][0] * nums[i], nums[i])
                max_val = max(dp[i-1][1] * nums[i], nums[i])
            res = max(res, max([min_val, max_val]))
            dp.append([min_val, max_val])
        # print(dp)
        return res

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums1 = nums[::-1]
        for i in range(1, len(nums)):
            nums[i] *= nums[i-1] or 1
            nums1[i] *= nums1[i-1] or 1
        return max(max(nums), max(nums1))

if __name__ == '__main__':
    demo = Solution()
    print(demo.maxProduct([1, 2, 3, 4, 0, -9, 8]))
