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

# solutions

'''
思路和算法：

方法：一次遍历 + 数位和计算

1. 问题分析：
   题目要求找到一个最小下标 i，使得 nums[i] 的各数位之和等于 i 本身。如果不存在这样的下标，返回 -1。

2. 算法步骤：
   - 因为我们需要求的是“最小”下标 i，所以直接从左往右（下标 0 到 n - 1）顺序遍历数组；
   - 对于每个元素 nums[i]：
     - 计算其各位数字之和：通过不断模 10（取出个位）与整除 10（去掉个位）累加得到数位和 s；
     - 比较数位和 s 与当前下标 i：若 s == i，则当前下标 i 即为满足条件的最小下标，直接返回 i；
   - 遍历结束后若未找到满足条件的下标，说明不存在，返回 -1。

复杂度分析：
- 时间复杂度：O(n * d)，其中 n 是数组 nums 的长度，d 是数字的最大位数。在本题中，nums[i] <= 1000，最多 4 位数字（d <= 4），因此求数位和为常数操作，总时间复杂度为 O(n)。
- 空间复杂度：O(1)，只使用了常数个额外变量来维护累加和与下标。
'''

