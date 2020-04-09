

'''
面试题 16.17. 连续数列
给定一个整数数组（有正数有负数），找出总和最大的连续数列，并返回总和。

示例：

输入： [-2,1,-3,4,-1,2,1,-5,4]
输出： 6
解释： 连续子数组 [4,-1,2,1] 的和最大，为 6。
进阶：

如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。

面试题 16.17. Contiguous Sequence LCCI
You are given an array of integers (both positive and negative). Find the contiguous sequence with the largest sum. Return the sum.

Example:

Input:  [-2,1,-3,4,-1,2,1,-5,4]
Output:  6
Explanation:  [4,-1,2,1] has the largest sum 6.
Follow Up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
'''


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return -2147483648
        cur = [nums[0]]
        max_sum = nums[0]
        for i in range(1, len(nums)):
            recent = sum(cur)
            if recent < 0:
                cur = [nums[i]]
            else:
                cur.append(nums[i])

            max_sum = max(max_sum, sum(cur))
        return max_sum
