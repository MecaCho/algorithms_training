# encoding=utf8

'''
334. Increasing Triplet Subsequence
Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.

Formally the function should:

Return true if there exists i, j, k
such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.
Note: Your algorithm should run in O(n) time complexity and O(1) space complexity.

Example 1:

Input: [1,2,3,4,5]
Output: true
Example 2:

Input: [5,4,3,2,1]
Output: false


334. 递增的三元子序列
给定一个未排序的数组，判断这个数组中是否存在长度为 3 的递增子序列。

数学表达式如下:

如果存在这样的 i, j, k,  且满足 0 ≤ i < j < k ≤ n-1，
使得 arr[i] < arr[j] < arr[k] ，返回 true ; 否则返回 false 。
说明: 要求算法的时间复杂度为 O(n)，空间复杂度为 O(1) 。

示例 1:

输入: [1,2,3,4,5]
输出: true
示例 2:

输入: [5,4,3,2,1]
输出: false
'''



class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 3:
            return False
        min_vals = []
        vals = []
        for i in range(len(nums)):
            if nums[i] not in vals:
                vals.append(nums[i])
            if not min_vals or nums[i] > min_vals[-1]:
                min_vals.append(nums[i])
                if len(min_vals) >=3:
                    return True
            else:
                j = len(min_vals) - 1
                while j >= 0 and min_vals[j] >= nums[i]:
                    j -= 1
                if j + 1 <= len(min_vals) - 1:
                    min_vals[j + 1] = nums[i]
        return False


class Solution1(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 3:
            return False
        left = []
        min_val = nums[0]

        for i in range(len(nums)):
            if nums[i] > min_val:
                left.append(min_val)
            else:
                min_val = nums[i]
                left.append(None)

        right = []
        max_val = nums[-1]
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] < max_val:
                right.append(max_val)
            else:
                max_val = nums[i]
                right.append(None)
        # print(left, right[::-1])

        for i in range(len(nums)):
            if left[i] is not None and right[len(nums) - 1 - i] is not None:
                return True
        return False


# 动态规划
class Solution2(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        length = len(nums)
        dp = [1] * length
        for i in range(length):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[j] + 1, dp[i])
        return max(dp) >= 3 if length > 2 else False


# 2022.01.12 solution

class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(set(nums)) < 3:
            return False
        min_num = nums[0]
        left = [0]
        for i in range(1, len(nums)):
            if nums[i] > min_num:
                left.append(1)
            else:
                min_num = nums[i]
                left.append(0)

        max_num = nums[-1]
        right  = [0]*len(nums)
        for i in range(len(nums)-2, -1, -1):
            if nums[i] < max_num:
                right[i] = 1
            else:
                max_num = nums[i]
                right[i] = 0
        # print(left, right)
        for i in range(len(nums)):
            if left[i] + right[i] == 2:
                return True

        return False

