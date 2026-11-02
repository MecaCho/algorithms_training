# encoding=utf8

'''
462. Minimum Moves to Equal Array Elements II
Given an integer array nums of size n, return the minimum number of moves required to make all array elements equal.

In one move, you can increment or decrement an element of the array by 1.

Test cases are designed so that the answer will fit in a 32-bit integer.

 

Example 1:

Input: nums = [1,2,3]
Output: 2
Explanation:
Only two moves are needed (remember each move increments or decrements one element):
[1,2,3]  =>  [2,2,3]  =>  [2,2,2]
Example 2:

Input: nums = [1,10,2,9]
Output: 16
 

Constraints:

n == nums.length
1 <= nums.length <= 105
-109 <= nums[i] <= 109

462. 最小操作次数使数组元素相等 II

给你一个长度为 n 的整数数组 nums ，返回使所有数组元素相等需要的最小操作数。

在一次操作中，你可以使数组中的一个元素加 1 或者减 1 。

测试用例经过设计以使答案在 32 位 整数范围内。



示例 1：

输入：nums = [1,2,3]
输出：2
解释：
只需要两次操作（每次操作指南使一个元素加 1 或减 1）：
[1,2,3]  =>  [2,2,3]  =>  [2,2,2]

示例 2：

输入：nums = [1,10,2,9]
输出：16



提示：

    n == nums.length
    1 <= nums.length <= 105
    -109 <= nums[i] <= 109
'''

# golang

'''
func minMoves2(nums []int) int {

	abs := func(a int)int{
		if a < 0{
			return -a
		}
		return a
	}
	sort.Ints(nums)
	res := 0
    x := nums[len(nums)/2]
	for _, num := range nums{
		res += abs(num-x)
	}
	return res

}
'''

