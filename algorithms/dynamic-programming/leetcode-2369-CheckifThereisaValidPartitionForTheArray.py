# encoding=utf8

'''
2369. Check if There is a Valid Partition For The Array
You are given a 0-indexed integer array nums. You have to partition the array into one or more contiguous subarrays.

We call a partition of the array valid if each of the obtained subarrays satisfies one of the following conditions:

The subarray consists of exactly 2, equal elements. For example, the subarray [2,2] is good.
The subarray consists of exactly 3, equal elements. For example, the subarray [4,4,4] is good.
The subarray consists of exactly 3 consecutive increasing elements, that is, the difference between adjacent elements is 1. For example, the subarray [3,4,5] is good, but the subarray [1,3,5] is not.
Return true if the array has at least one valid partition. Otherwise, return false.

 

Example 1:

Input: nums = [4,4,4,5,6]
Output: true
Explanation: The array can be partitioned into the subarrays [4,4] and [4,5,6].
This partition is valid, so we return true.
Example 2:

Input: nums = [1,1,1,2]
Output: false
Explanation: There is no valid partition for this array.
 

Constraints:

2 <= nums.length <= 105
1 <= nums[i] <= 106
'''

class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        def valid2(nums: List[int]):
            return nums[0] == nums[1]
        def valid3(nums: List[int]):
            return nums[0] == nums[1] == nums[2] or nums[0] + 2 == nums[1] + 1 == nums[2]
        n = len(nums)
        dp = [False]*(n+1)
        dp[-1] = True
        for i in range(1, len(nums)):
            if (valid2(nums[i-1:i+1]) and dp[i-2]) or (i >= 2 and dp[i-3] and valid3(nums[i-2:i+1])):
                dp[i] = True
        return dp[n-1]


