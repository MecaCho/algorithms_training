'''
1509. Minimum Difference Between Largest and Smallest Value in Three Moves
Given an array nums, you are allowed to choose one element of nums and change it by any value in one move.

Return the minimum difference between the largest and smallest value of nums after perfoming at most 3 moves.



Example 1:

Input: nums = [5,3,2,4]
Output: 0
Explanation: Change the array [5,3,2,4] to [2,2,2,2].
The difference between the maximum and minimum is 2-2 = 0.
Example 2:

Input: nums = [1,5,0,10,14]
Output: 1
Explanation: Change the array [1,5,0,10,14] to [1,1,0,1,1].
The difference between the maximum and minimum is 1-0 = 1.
Example 3:

Input: nums = [6,6,0,1,1,4,6]
Output: 2
Example 4:

Input: nums = [1,5,6,14,15]
Output: 1


Constraints:

1 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9


1509. 三次操作后最大值与最小值的最小差
给你一个数组 nums ，每次操作你可以选择 nums 中的任意一个元素并将它改成任意值。

请你返回三次操作后， nums 中最大值与最小值的差的最小值。



示例 1：

输入：nums = [5,3,2,4]
输出：0
解释：将数组 [5,3,2,4] 变成 [2,2,2,2].
最大值与最小值的差为 2-2 = 0 。
示例 2：

输入：nums = [1,5,0,10,14]
输出：1
解释：将数组 [1,5,0,10,14] 变成 [1,1,0,1,1] 。
最大值与最小值的差为 1-0 = 1 。
示例 3：

输入：nums = [6,6,0,1,1,4,6]
输出：2
示例 4：

输入：nums = [1,5,6,14,15]
输出：1


提示：

1 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
'''


class Solution(object):
    def minDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) <= 4:
            return 0
        nums.sort()
        length = len(nums)
        return min(nums[length-4] - nums[0], nums[length-3] - nums[1], nums[length-2] - nums[2], nums[length-1] - nums[3])




# class Solution(object):
#     def minDifference(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#
#         if len(nums) <= 4:
#             return 0
#         nums.sort()
#         length = len(nums)
#
#         if len(nums) >= 6:
#             return min(nums[length-4] - nums[0], nums[length-3] - nums[1], nums[length-2] - nums[2], nums[length-1] - nums[3])
#         else:
#             res = float("inf")
#             for i in range(1, length):
#                 res = min(nums[i] - nums[i-1], res)
#             return res


