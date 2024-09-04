# encoding=utf8

'''
2708. Maximum Strength of a Group

You are given a 0-indexed integer array nums representing the score of students in an exam. The teacher would like to form one non-empty group of students with maximal strength, where the strength of a group of students of indices i0, i1, i2, ... , ik is defined as nums[i0] * nums[i1] * nums[i2] * ... * nums[ik​].

Return the maximum strength of a group the teacher can create.

 

Example 1:

Input: nums = [3,-1,-5,2,5,-9]
Output: 1350
Explanation: One way to form a group of maximal strength is to group the students at indices [0,2,3,4,5]. Their strength is 3 * (-5) * 2 * 5 * (-9) = 1350, which we can show is optimal.
Example 2:

Input: nums = [-4,-5,-4]
Output: 20
Explanation: Group the students at indices [0, 1] . Then, we’ll have a resulting strength of 20. We cannot achieve greater strength.
 

Constraints:

1 <= nums.length <= 13
-9 <= nums[i] <= 9
'''



class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        # if len(nums) == 1 and nums[0] < 0:
        #     return nums[0]
        # nums = [num for num in nums if num != 0]
        # if len(nums) < 1:
        #     return 0
        # if len(nums) == 1:
        #     if nums[0] > 0:
        #         return nums[0]
        #     else:
        #         return 0
        
        # if len(nums) == 2:
        #     return nums[0] * nums[1] if nums[0] * nums[1] > 0 else max(nums)
        # total = 1
        # max_neg = -inf
        # for num in nums:
        #     if num == 0:
        #         continue
        #     total *= num
        #     if num < 0 and num > max_neg:
        #         max_neg = num
        # if total < 0:
        #     if total == max_neg:
        #         return 0
        #     total //= max_neg
        # return total

        mn = mx = nums[0]
        for num in nums[1:]:
            mn, mx = min(mn, num, mx*num, mn*num), max(mx, num, mx*num, mn*num)
        return mx
