# encoding=utf8

'''
805. Split Array With Same Average
You are given an integer array nums.

You should move each element of nums into one of the two arrays A and B such that A and B are non-empty, and average(A) == average(B).

Return true if it is possible to achieve that and false otherwise.

Note that for an array arr, average(arr) is the sum of all the elements of arr over the length of arr.

 

Example 1:

Input: nums = [1,2,3,4,5,6,7,8]
Output: true
Explanation: We can split the array into [1,4,5,8] and [2,3,6,7], and both of them have an average of 4.5.
Example 2:

Input: nums = [3,1]
Output: false
 

Constraints:

1 <= nums.length <= 30
0 <= nums[i] <= 104
'''

# tips

'''
动态规划 + 位运算优化。

令 sum 和 n 分别为数组 nums 的和与元素个数，sumA 和 k 为数组 A 的和与元素个数。

根据题目要求 sumA / k = (sum - sumA) / (n - k)，可推得：sumA = sum * k / n。

那么我们可以将题目转化为：从 nums 中选 k 个数，使这 k 个数的和为 sum * k / n。

我们可以用动态规划，令 dp[s][x] 表示是否能从 nums 中选 x 个数使它们的和为 s。

那么状态转移关系为：如果能从 nums 中选 x 个数使它们的和为 s，那么可以再加上一个 nums 中的数 num，即从 nums 中选 x + 1 个数使它们的和为 s + num。

if (dp[s][x] == true) 
    dp[s + num][x + 1] = true;
'''

class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        n = len(nums)
        m = n // 2
        s = sum(nums)
        if all(s * i % n for i in range(1, m + 1)):
            return False

        dp = [set() for _ in range(m + 1)]
        dp[0].add(0)
        for num in nums:
            for i in range(m, 0, -1):
                for x in dp[i - 1]:
                    curr = x + num
                    if curr * n == s * i:
                        return True
                    dp[i].add(curr)
        return False

