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


class Solution202101201(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return max(nums[-1]*nums[-2]*nums[-3], nums[0]*nums[1]*nums[-1])


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


# solutions

'''
方法一：排序
首先将数组排序。

如果数组中全是非负数，则排序后最大的三个数相乘即为最大乘积；如果全是非正数，则最大的三个数相乘同样也为最大乘积。

如果数组中有正数有负数，则最大乘积既可能是三个最大正数的乘积，也可能是两个最小负数（即绝对值最大）与最大正数的乘积。

综上，我们在给数组排序后，分别求出三个最大正数的乘积，以及两个最小负数与最大正数的乘积，二者之间的最大值即为所求答案。

C++JavaGolangCJavaScript

func maximumProduct(nums []int) int {
    sort.Ints(nums)
    n := len(nums)
    return max(nums[0]*nums[1]*nums[n-1], nums[n-3]*nums[n-2]*nums[n-1])
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}
复杂度分析

时间复杂度：O(N\log N)O(NlogN)，其中 NN 为数组长度。排序需要 O(N\log N)O(NlogN) 的时间。

空间复杂度：O(\log N)O(logN)，主要为排序的空间开销。

方法二：线性扫描
在方法一中，我们实际上只要求出数组中最大的三个数以及最小的两个数，因此我们可以不用排序，用线性扫描直接得出这五个数。

C++JavaGolangCJavaScript

func maximumProduct(nums []int) int {
    // 最小的和第二小的
    min1, min2 := math.MaxInt64, math.MaxInt64
    // 最大的、第二大的和第三大的
    max1, max2, max3 := math.MinInt64, math.MinInt64, math.MinInt64

    for _, x := range nums {
        if x < min1 {
            min2 = min1
            min1 = x
        } else if x < min2 {
            min2 = x
        }

        if x > max1 {
            max3 = max2
            max2 = max1
            max1 = x
        } else if x > max2 {
            max3 = max2
            max2 = x
        } else if x > max3 {
            max3 = x
        }
    }

    return max(min1*min2*max1, max1*max2*max3)
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}
复杂度分析

时间复杂度：O(N)O(N)，其中 NN 为数组长度。我们仅需遍历数组一次。

空间复杂度：O(1)O(1)。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/maximum-product-of-three-numbers/solution/san-ge-shu-de-zui-da-cheng-ji-by-leetcod-t9sb/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
