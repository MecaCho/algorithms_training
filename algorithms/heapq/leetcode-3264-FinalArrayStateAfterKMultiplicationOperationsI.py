# encoding=utf8

'''
3264. Final Array State After K Multiplication Operations I

You are given an integer array nums, an integer k, and an integer multiplier.

You need to perform k operations on nums. In each operation:

Find the minimum value x in nums. If there are multiple occurrences of the minimum value, select the one that appears first.
Replace the selected minimum value x with x * multiplier.
Return an integer array denoting the final state of nums after performing all k operations.

 

Example 1:

Input: nums = [2,1,3,5,6], k = 5, multiplier = 2

Output: [8,4,6,5,6]

Explanation:

Operation	Result
After operation 1	[2, 2, 3, 5, 6]
After operation 2	[4, 2, 3, 5, 6]
After operation 3	[4, 4, 3, 5, 6]
After operation 4	[4, 4, 6, 5, 6]
After operation 5	[8, 4, 6, 5, 6]
Example 2:

Input: nums = [1,2], k = 3, multiplier = 4

Output: [16,8]

Explanation:

Operation	Result
After operation 1	[4, 2]
After operation 2	[4, 8]
After operation 3	[16, 8]
 

Constraints:

1 <= nums.length <= 100
1 <= nums[i] <= 100
1 <= k <= 10
1 <= multiplier <= 5
给你一个整数数组 nums ，一个整数 k  和一个整数 multiplier 。

你需要对 nums 执行 k 次操作，每次操作中：

找到 nums 中的 最小 值 x ，如果存在多个最小值，选择最 前面 的一个。
将 x 替换为 x * multiplier 。
k 次操作以后，你需要将 nums 中每一个数值对 109 + 7 取余。

请你返回执行完 k 次乘运算以及取余运算之后，最终的 nums 数组。

 

 示例 1：

 输入：nums = [2,1,3,5,6], k = 5, multiplier = 2

 输出：[8,4,6,5,6]

 解释：

 操作   结果
 1 次操作后 [2, 2, 3, 5, 6]
 2 次操作后 [4, 2, 3, 5, 6]
 3 次操作后 [4, 4, 3, 5, 6]
 4 次操作后 [4, 4, 6, 5, 6]
 5 次操作后 [8, 4, 6, 5, 6]
 取余操作后 [8, 4, 6, 5, 6]
 示例 2：

 输入：nums = [100000,2000], k = 2, multiplier = 1000000

 输出：[999999307,999999993]

 解释：

 操作   结果
 1 次操作后 [100000, 2000000000]
 2 次操作后 [100000000000, 2000000000]
 取余操作后 [999999307, 999999993]
  

  提示：

  1 <= nums.length <= 104
  1 <= nums[i] <= 109
  1 <= k <= 109
  1 <= multiplier <= 106

'''
