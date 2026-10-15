# encoding=utf8

'''
2913. Subarrays Distinct Element Sum of Squares I
You are given a 0-indexed integer array nums.

The distinct count of a subarray of nums is defined as:

Let nums[i..j] be a subarray of nums consisting of all the indices from i to j such that 0 <= i <= j < nums.length. Then the number of distinct values in nums[i..j] is called the distinct count of nums[i..j].
Return the sum of the squares of distinct counts of all subarrays of nums.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,2,1]
Output: 15
Explanation: Six possible subarrays are:
[1]: 1 distinct value
[2]: 1 distinct value
[1]: 1 distinct value
[1,2]: 2 distinct values
[2,1]: 2 distinct values
[1,2,1]: 2 distinct values
The sum of the squares of the distinct counts in all subarrays is equal to 1^2 + 1^2 + 1^2 + 2^2 + 2^2 + 2^2 = 15.

Example 2:

Input: nums = [1,1]
Output: 3
Explanation: Three possible subarrays are:
[1]: 1 distinct value
[1]: 1 distinct value
[1,1]: 1 distinct value
The sum of the squares of the distinct counts in all subarrays is equal to 1^2 + 1^2 + 1^2 = 3.

 

Constraints:

1 <= nums.length <= 100
1 <= nums[i] <= 100


2913. 子数组不同元素数目的平方和 I
给你一个下标从 0 开始的整数数组 nums 。

定义 nums 一个子数组的 不同计数 值如下：
令 nums[i..j] 表示 nums 中所有下标在 i 到 j 范围内的元素构成的子数组（满足 0 <= i <= j < nums.length ），那么我们称子数组 nums[i..j] 中不同值的数目为 nums[i..j] 的不同计数。

请你返回 nums 中所有子数组的 不同计数 的 平方 和。

子数组指的是一个数组里面一段连续 非空 的元素序列。

 

示例 1：

输入：nums = [1,2,1]
输出：15
解释：六个子数组分别为：
[1]: 1 个互不相同的元素。
[2]: 1 个互不相同的元素。
[1]: 1 个互不相同的元素。
[1,2]: 2 个互不相同的元素。
[2,1]: 2 个互不相同的元素。
[1,2,1]: 2 个互不相同的元素。
所有不同计数的平方和为 1^2 + 1^2 + 1^2 + 2^2 + 2^2 + 2^2 = 15 。

示例 2：

输入：nums = [1,1]
输出：3
解释：三个子数组分别为：
[1]: 1 个互不相同的元素。
[1]: 1 个互不相同的元素。
[1,1]: 1 个互不相同的元素。
所有不同计数的平方和为 1^2 + 1^2 + 1^2 = 3 。

 

提示：

1 <= nums.length <= 100
1 <= nums[i] <= 100
'''


class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            distinct_set = set()
            for j in range(i, n):
                distinct_set.add(nums[j])
                cnt = len(distinct_set)
                ans += cnt * cnt
        return ans


# golang solution

'''
func sumCounts(nums []int) int {
	n := len(nums)
	ans := 0
	for i := 0; i < n; i++ {
		seen := make(map[int]struct{})
		for j := i; j < n; j++ {
			seen[nums[j]] = struct{}{}
			cnt := len(seen)
			ans += cnt * cnt
		}
	}
	return ans
}
'''


