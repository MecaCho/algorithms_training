# encoding=utf8

'''
628. 三个数的最大乘积
给定一个整型数组，在数组中找出由三个数组成的最大乘积，并输出这个乘积。

示例 1:

输入: [1,2,3]
输出: 6
示例 2:

输入: [1,2,3,4]
输出: 24
注意:

给定的整型数组长度范围是[3,104]，数组中所有的元素范围是[-1000, 1000]。
输入的数组中任意三个数的乘积不会超出32位有符号整数的范围。

628. Maximum Product of Three Numbers
Given an integer array, find three numbers whose product is maximum and output the maximum product.

Example 1:

Input: [1,2,3]
Output: 6


Example 2:

Input: [1,2,3,4]
Output: 24


Note:

The length of the given array will be in range [3,104] and all elements are in the range [-1000, 1000].
Multiplication of any three numbers in the input won't exceed the range of 32-bit signed integer.
'''


class Solution20210120(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return max(nums[-1]*nums[-2]*nums[-3], nums[0]*nums[1]*nums[2], nums[0]*nums[1]*nums[-1])



class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # max_val = 0
        # cur_val = nums[0]*nums[1]
        # pre = 1
        # for i in range(2, len(nums)):
        #     cur_val = nums[i]*cur_val / pre
        #     pre = nums[i-2]
        #     if cur_val > max_val:
        #         max_val = cur_val
        if len(nums) < 3:
            return 0
        nums = sorted(nums)
        return max(nums[-1]*nums[-2]*nums[-3], nums[0]*nums[1]*nums[-1])

# golang

'''
func maximumProduct(nums []int) int {

	sort.Ints(nums)

	length := len(nums)

	max_Product := nums[length-1] * nums[length-2] * nums[length-3]

	max_Product1 := nums[0] * nums[1] * nums[length-1]

	if max_Product > max_Product1{
		return max_Product
	}

	return max_Product1

}
'''
