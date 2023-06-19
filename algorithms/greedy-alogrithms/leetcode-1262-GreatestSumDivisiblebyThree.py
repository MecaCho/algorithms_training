# encoding=utf8

'''
1262. Greatest Sum Divisible by Three
Given an integer array nums, return the maximum possible sum of elements of the array such that it is divisible by three.

 

Example 1:

Input: nums = [3,6,5,1,8]
Output: 18
Explanation: Pick numbers 3, 6, 1 and 8 their sum is 18 (maximum sum divisible by 3).
Example 2:

Input: nums = [4]
Output: 0
Explanation: Since 4 is not divisible by 3, do not pick any number.
Example 3:

Input: nums = [1,2,3,4,4]
Output: 12
Explanation: Pick numbers 1, 3, 4 and 4 their sum is 12 (maximum sum divisible by 3).
 

Constraints:

1 <= nums.length <= 4 * 104
1 <= nums[i] <= 104

'''

class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        ones, twos = [], []
        all_sum = 0
        for i in range(len(nums)):
            t = nums[i] % 3
            if t == 1:
                ones.append(nums[i])
            elif t == 2:
                twos.append(nums[i])

            all_sum += nums[i]
        sum_ = len(ones) + 2*len(twos)

        if sum_ % 3 == 1:
            ones.sort()
            twos.sort()
            if len(ones) < 1:
                return all_sum - twos[0] - twos[1]
            if len(twos) > 1 and  twos[0] + twos[1] < ones[0]:
                all_sum -= twos[0] + twos[1]
            else:
                all_sum -= ones[0]
        elif sum_ % 3 == 2:
            ones.sort()
            twos.sort()
            if len(twos) < 1:
                return all_sum - ones[0] - ones[1]
            if len(ones) > 1 and ones[0] + ones[1] < twos[0]:
                all_sum -= ones[0] + ones[1]
            else:
                all_sum -= twos[0]
        return all_sum
