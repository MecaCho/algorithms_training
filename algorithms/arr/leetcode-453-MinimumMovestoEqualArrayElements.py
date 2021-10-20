# encoding=utf8

'''
453. Minimum Moves to Equal Array Elements
Given an integer array nums of size n, return the minimum number of moves required to make all array elements equal.

In one move, you can increment n - 1 elements of the array by 1.

 

Example 1:

Input: nums = [1,2,3]
Output: 3
Explanation: Only three moves are needed (remember each move increments two elements):
[1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]
Example 2:

Input: nums = [1,1,1]
Output: 0
 

Constraints:

n == nums.length
1 <= nums.length <= 105
-109 <= nums[i] <= 109
The answer is guaranteed to fit in a 32-bit integer.

453. 最小操作次数使数组元素相等
给你一个长度为 n 的整数数组，每次操作将会使 n - 1 个元素增加 1 。返回让数组所有元素相等的最小操作次数。

 

示例 1：

输入：nums = [1,2,3]
输出：3
解释：
只需要3次操作（注意每次操作会增加两个元素的值）：
[1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]
示例 2：

输入：nums = [1,1,1]
输出：0
 

提示：

n == nums.length
1 <= nums.length <= 105
-109 <= nums[i] <= 109
答案保证符合 32-bit 整数
'''

# golang solution

'''
func minMoves(nums []int) int {
	minNum := nums[0]
	for i := 1; i < len(nums);i++{
		if nums[i] < minNum{
			minNum = nums[i]
		}
	}
	res := 0
	for i := 0;i < len(nums);i++{
		res += nums[i] - minNum
	}
	return res
}
'''

