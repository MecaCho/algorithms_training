# encoding=utf8

'''
413. Arithmetic Slices
An integer array is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

For example, [1,3,5,7,9], [7,7,7,7], and [3,-1,-5,-9] are arithmetic sequences.
Given an integer array nums, return the number of arithmetic subarrays of nums.

A subarray is a contiguous subsequence of the array.

 

Example 1:

Input: nums = [1,2,3,4]
Output: 3
Explanation: We have 3 arithmetic slices in nums: [1, 2, 3], [2, 3, 4] and [1,2,3,4] itself.
Example 2:

Input: nums = [1]
Output: 0
 

Constraints:

1 <= nums.length <= 5000
-1000 <= nums[i] <= 1000

413. 等差数列划分
如果一个数列 至少有三个元素 ，并且任意两个相邻元素之差相同，则称该数列为等差数列。

例如，[1,3,5,7,9]、[7,7,7,7] 和 [3,-1,-5,-9] 都是等差数列。
给你一个整数数组 nums ，返回数组 nums 中所有为等差数组的 子数组 个数。

子数组 是数组中的一个连续序列。

 

示例 1：

输入：nums = [1,2,3,4]
输出：3
解释：nums 中有三个子等差数组：[1, 2, 3]、[2, 3, 4] 和 [1,2,3,4] 自身。
示例 2：

输入：nums = [1]
输出：0
 

提示：

1 <= nums.length <= 5000
-1000 <= nums[i] <= 1000
'''

# golang solution

'''
func numberOfArithmeticSlices(nums []int) int {
	res := 0
	t := 0
    if len(nums) < 3{
        return 0
    }
	d := nums[1] - nums[0]
	for i := 2; i < len(nums); i++ {
		if nums[i]-nums[i-1] == d {
			t++
		} else {
			t = 0
			d = nums[i] - nums[i-1]
		}
		res += t
	}

	return res
}
'''

