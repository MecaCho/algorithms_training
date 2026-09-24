# encoding=utf8

'''
3550. Smallest Index With Digit Sum Equal to Index
You are given an integer array nums.

Return the smallest index i such that the sum of the digits of nums[i] is equal to i.

If no such index exists, return -1.

 

Example 1:

Input: nums = [1,3,2]
Output: 2
Explanation:
For nums[2] = 2, the sum of digits is 2, which is equal to index i = 2. Thus, the output is 2.

Example 2:

Input: nums = [1,10,11]
Output: 1
Explanation:
For nums[1] = 10, the sum of digits is 1 + 0 = 1, which is equal to index i = 1.
For nums[2] = 11, the sum of digits is 1 + 1 = 2, which is equal to index i = 2.
Since index 1 is the smallest, the output is 1.

Example 3:

Input: nums = [1,2,3]
Output: -1
Explanation:
Since no index satisfies the condition, the output is -1.

 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 1000


3550. 数位和等于下标的最小下标
给你一个整数数组 nums 。

返回满足 nums[i] 的数位和（每一位数字相加求和）等于 i 的 最小 下标 i 。

如果不存在满足要求的下标，返回 -1 。

 

示例 1：

输入：nums = [1,3,2]
输出：2
解释：
nums[2] = 2 ，其数位和等于 2 ，与其下标 i = 2 相等。因此，输出为 2 。

示例 2：

输入：nums = [1,10,11]
输出：1
解释：
nums[1] = 10 ，其数位和等于 1 + 0 = 1 ，与其下标 i = 1 相等。
nums[2] = 11 ，其数位和等于是 1 + 1 = 2 ，与其下标 i = 2 相等。
由于下标 1 是满足要求的最小下标，输出为 1 。

示例 3：

输入：nums = [1,2,3]
输出：-1
解释：
由于不存在满足要求的下标，输出为 -1 。

 

提示：

1 <= nums.length <= 100
0 <= nums[i] <= 1000
'''


class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i, x in enumerate(nums):
            s = 0
            while x > 0:
                s += x % 10
                x //= 10
            if s == i:
                return i
        return -1


# golang solution

'''
func smallestIndex(nums []int) int {
	for i, x := range nums {
		s := 0
		for x > 0 {
			s += x % 10
			x /= 10
		}
		if s == i {
			return i
		}
	}
	return -1
}
'''
