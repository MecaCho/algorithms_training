# encoding=utf8

'''
457. Circular Array Loop
You are playing a game involving a circular array of non-zero integers nums. Each nums[i] denotes the number of indices forward/backward you must move if you are located at index i:

If nums[i] is positive, move nums[i] steps forward, and
If nums[i] is negative, move nums[i] steps backward.
Since the array is circular, you may assume that moving forward from the last element puts you on the first element, and moving backwards from the first element puts you on the last element.

A cycle in the array consists of a sequence of indices seq of length k where:

Following the movement rules above results in the repeating index sequence seq[0] -> seq[1] -> ... -> seq[k - 1] -> seq[0] -> ...
Every nums[seq[j]] is either all positive or all negative.
k > 1
Return true if there is a cycle in nums, or false otherwise.

 

Example 1:

Input: nums = [2,-1,1,2,2]
Output: true
Explanation:
There is a cycle from index 0 -> 2 -> 3 -> 0 -> ...
The cycle's length is 3.
Example 2:

Input: nums = [-1,2]
Output: false
Explanation:
The sequence from index 1 -> 1 -> 1 -> ... is not a cycle because the sequence's length is 1.
By definition the sequence's length must be strictly greater than 1 to be a cycle.
Example 3:

Input: nums = [-2,1,-1,-2,-2]
Output: false
Explanation:
The sequence from index 1 -> 2 -> 1 -> ... is not a cycle because nums[1] is positive, but nums[2] is negative.
Every nums[seq[j]] must be either all positive or all negative.
 

Constraints:

1 <= nums.length <= 5000
-1000 <= nums[i] <= 1000
nums[i] != 0
 

Follow up: Could you solve it in O(n) time complexity and O(1) extra space complexity?

457. 环形数组是否存在循环
存在一个不含 0 的 环形 数组 nums ，每个 nums[i] 都表示位于下标 i 的角色应该向前或向后移动的下标个数：

如果 nums[i] 是正数，向前 移动 nums[i] 步
如果 nums[i] 是负数，向后 移动 nums[i] 步
因为数组是 环形 的，所以可以假设从最后一个元素向前移动一步会到达第一个元素，而第一个元素向后移动一步会到达最后一个元素。

数组中的 循环 由长度为 k 的下标序列 seq ：

遵循上述移动规则将导致重复下标序列 seq[0] -> seq[1] -> ... -> seq[k - 1] -> seq[0] -> ...
所有 nums[seq[j]] 应当不是 全正 就是 全负
k > 1
如果 nums 中存在循环，返回 true ；否则，返回 false 。

 

示例 1：

输入：nums = [2,-1,1,2,2]
输出：true
解释：存在循环，按下标 0 -> 2 -> 3 -> 0 。循环长度为 3 。
示例 2：

输入：nums = [-1,2]
输出：false
解释：按下标 1 -> 1 -> 1 ... 的运动无法构成循环，因为循环的长度为 1 。根据定义，循环的长度必须大于 1 。
示例 3:

输入：nums = [-2,1,-1,-2,-2]
输出：false
解释：按下标 1 -> 2 -> 1 -> ... 的运动无法构成循环，因为 nums[1] 是正数，而 nums[2] 是负数。
所有 nums[seq[j]] 应当不是全正就是全负。
 

提示：

1 <= nums.length <= 5000
-1000 <= nums[i] <= 1000
nums[i] != 0
 

进阶：你能设计一个时间复杂度为 O(n) 且额外空间复杂度为 O(1) 的算法吗？
'''
