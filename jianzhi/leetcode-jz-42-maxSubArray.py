'''
面试题42. 连续子数组的最大和
输入一个整型数组，数组里有正数也有负数。数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。

要求时间复杂度为O(n)。



示例1:

输入: nums = [-2,1,-3,4,-1,2,1,-5,4]
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。


提示：

1 <= arr.length <= 10^5
-100 <= arr[i] <= 100
注意：本题与主站 53 题相同：https://leetcode-cn.com/problems/maximum-subarray/
'''


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return -2147483648
        cur = -float("inf")
        max_sum = -float("inf")
        for num in nums:
            if cur < 0 and num > cur:
                cur = num
            else:
                cur += num
            max_sum = max(max_sum, cur)
        return max_sum


class Solution_(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return -2147483648
        cur = -float("inf")
        max_sum = -float("inf")
        for num in nums:
            if cur < 0:
                cur = num
            else:
                cur += num
            max_sum = max(max_sum, cur)
        return max_sum

# golang solution

'''
func maxSubArray(nums []int) int {
	if len(nums) < 1{
		return -2147483648
	}
	
	max := func(a, b int) int{
		if a > b{
			return a
		}
		return b
	}
	

	cur, res := nums[0], nums[0]
	for i := 1; i < len(nums); i++{
		num := nums[i]
		if cur < 0{
			cur = num
		}else {
			cur += num
		}
		res = max(cur, res)
	}
	return res
}
'''
