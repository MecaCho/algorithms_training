# encoding=utf8

'''
915. Partition Array into Disjoint Intervals
Given an integer array nums, partition it into two (contiguous) subarrays left and right so that:

Every element in left is less than or equal to every element in right.
left and right are non-empty.
left has the smallest possible size.
Return the length of left after such a partitioning.

Test cases are generated such that partitioning exists.

 

Example 1:

Input: nums = [5,0,3,8,6]
Output: 3
Explanation: left = [5,0,3], right = [8,6]
Example 2:

Input: nums = [1,1,1,0,6,12]
Output: 4
Explanation: left = [1,1,1,0], right = [6,12]
 

Constraints:

2 <= nums.length <= 105
0 <= nums[i] <= 106
There is at least one valid answer for the given input.
'''

class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        min_v = [nums[-1]]
        n = len(nums)
        for i in range(n-2, -1, -1):
            if nums[i] < min_v[-1]:
                min_v.append(nums[i])
            else:
                min_v.append(min_v[-1])
        max_v = nums[0]
        for i in range(1, n):
            if max_v <= min_v[n-i-1]:
                return i
            if max_v < nums[i]:
                max_v = nums[i]
        return -1
      
