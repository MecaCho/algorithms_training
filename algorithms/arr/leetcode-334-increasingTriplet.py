

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
