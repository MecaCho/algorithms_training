# encoding=utf8

'''
2089. Find Target Indices After Sorting Array
You are given a 0-indexed integer array nums and a target element target.

A target index is an index i such that nums[i] == target.

Return a list of the target indices of nums after sorting nums in non-decreasing order. If there are no target indices, return an empty list. The returned list must be sorted in increasing order.

 

Example 1:

Input: nums = [1,2,5,2,3], target = 2
Output: [1,2]
Explanation: After sorting, nums is [1,2,2,3,5].
The indices where nums[i] == 2 are 1 and 2.

Example 2:

Input: nums = [1,2,5,2,3], target = 3
Output: [3]
Explanation: After sorting, nums is [1,2,2,3,5].
The index where nums[i] == 3 is 3.

Example 3:

Input: nums = [1,2,5,2,3], target = 5
Output: [4]
Explanation: After sorting, nums is [1,2,2,3,5].
The index where nums[i] == 5 is 4.

 

Constraints:

1 <= nums.length <= 100
1 <= nums[i], target <= 100


2089. 找出数组排序后的目标下标
给你一个下标从 0 开始的整数数组 nums 以及一个目标元素 target 。

目标下标 是一个满足 nums[i] == target 的下标 i 。

将 nums 按 非递减 顺序排序后，返回由 nums 中目标下标组成的列表。如果不存在目标下标，返回一个 空 列表。返回的列表必须按 递增 顺序排列。

 

示例 1：

输入：nums = [1,2,5,2,3], target = 2
输出：[1,2]
解释：排序后，nums 变为 [1,2,2,3,5] 。
满足 nums[i] == 2 的下标是 1 和 2 。

示例 2：

输入：nums = [1,2,5,2,3], target = 3
输出：[3]
解释：排序后，nums 变为 [1,2,2,3,5] 。
满足 nums[i] == 3 的下标是 3 。

示例 3：

输入：nums = [1,2,5,2,3], target = 5
输出：[4]
解释：排序后，nums 变为 [1,2,2,3,5] 。
满足 nums[i] == 5 的下标是 4 。

示例 4：

输入：nums = [1,2,5,2,3], target = 4
输出：[]
解释：nums 中不含值为 4 的元素。

 

提示：

1 <= nums.length <= 100
1 <= nums[i], target <= 100
'''


class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        # 方法一：线性计数法（Counting / 计数排序思想）
        # 非递减排序后，所有严格小于 target 的元素都会排在 target 前面；
        # 所有等于 target 的元素会连续排布。
        less = 0
        count = 0
        for x in nums:
            if x < target:
                less += 1
            elif x == target:
                count += 1
        return list(range(less, less + count))


# golang solution

'''
func targetIndices(nums []int, target int) []int {
	less, count := 0, 0
	for _, x := range nums {
		if x < target {
			less++
		} else if x == target {
			count++
		}
	}

	ans := make([]int, count)
	for i := 0; i < count; i++ {
		ans[i] = less + i
	}
	return ans
}
'''

# solutions

'''
思路和算法：

方法一：线性计数法（最优解）
- 观察非递减排序后数组的性质：
  1. 所有严格小于 target 的元素在排序后一定会位于 target 之前；
  2. 所有等于 target 的元素在排序后一定会连续排列；
  3. 所有严格大于 target 的元素在排序后一定会位于 target 之后。
- 因此，我们不需要对整个数组执行完整的排序操作，只需线性遍历一次数组 nums：
  - 统计严格小于 target 的元素个数 less；
  - 统计等于 target 的元素个数 count。
- 排序后等于 target 的元素所占据的下标区间正好是 [less, less + count - 1]（半开区间 [less, less + count)）。
- 如果 count == 0，说明数组中不存在 target，直接返回空列表；否则返回下标连续升序列表 [less, less + 1, ..., less + count - 1]。

方法二：直接排序法（模拟）
- 直接使用内置排序算法将 nums 进行升序排序；
- 遍历排序后的数组，当下标 i 满足 nums[i] == target 时，将 i 添入答案列表中。

复杂度分析：
- 时间复杂度：
  - 方法一（计数法）：O(n)，其中 n 为 nums 的长度。仅需单次遍历统计 less 和 count，构造结果列表耗时 O(count) <= O(n)。
  - 方法二（排序法）：O(n log n)，主要瓶颈在于数组排序。
- 空间复杂度：
  - 方法一（计数法）：O(1)，除返回值外仅需常数级别的额外变量（less, count）。
  - 方法二（排序法）：O(log n)，为排序所占用的栈空间。
'''

