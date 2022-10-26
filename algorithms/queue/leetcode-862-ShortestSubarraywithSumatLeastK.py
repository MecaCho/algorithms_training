# encoding=utf8

'''
862. Shortest Subarray with Sum at Least K
Given an integer array nums and an integer k, return the length of the shortest non-empty subarray of nums with a sum of at least k. If there is no such subarray, return -1.

A subarray is a contiguous part of an array.

 

Example 1:

Input: nums = [1], k = 1
Output: 1
Example 2:

Input: nums = [1,2], k = 4
Output: -1
Example 3:

Input: nums = [2,-1,2], k = 3
Output: 3
 

Constraints:

1 <= nums.length <= 105
-105 <= nums[i] <= 105
1 <= k <= 109
'''

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        pre_sum = [0]
        n = len(nums)
        for i in range(n):
            pre_sum.append(pre_sum[-1] + nums[i])
        res = n+1
        q = deque()
        # print(pre_sum)
        for i in range(n+1):
            while q and pre_sum[i] <= pre_sum[q[-1]]:
                q.pop()
            while q and pre_sum[i] - pre_sum[q[0]] >= k:
                res = min(res, i-q[0])
                q.popleft()
            
            q.append(i)
        return res if res < n+1 else -1

