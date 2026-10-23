# encoding=utf8

'''
3644. Maximum K to Sort a Permutation
You are given an integer array nums of length n, where nums is a permutation of the numbers in the range [0..n - 1].

You may swap elements at indices i and j only if nums[i] AND nums[j] == k, where AND denotes the bitwise AND operation and k is a non-negative integer.

Return the maximum value of k such that the array can be sorted in non-decreasing order using any number of such swaps. If nums is already sorted, return 0.

 

Example 1:

Input: nums = [0,3,2,1]
Output: 1
Explanation:
Choose k = 1. Swapping nums[1] = 3 and nums[3] = 1 is allowed since nums[1] AND nums[3] == 1, resulting in a sorted permutation: [0, 1, 2, 3].

Example 2:

Input: nums = [0,1,3,2]
Output: 2
Explanation:
Choose k = 2. Swapping nums[2] = 3 and nums[3] = 2 is allowed since nums[2] AND nums[3] == 2, resulting in a sorted permutation: [0, 1, 2, 3].

Example 3:

Input: nums = [3,2,1,0]
Output: 0
Explanation:
Only k = 0 allows sorting since no greater k allows the required swaps where nums[i] AND nums[j] == k.

 

Constraints:

1 <= n == nums.length <= 10^5
0 <= nums[i] <= n - 1
nums is a permutation of integers from 0 to n - 1.


3644. 排序排列
给你一个长度为 n 的整数数组 nums ，其中 nums 是范围 [0..n - 1] 内所有数字的一个 排列 。

你可以在满足条件 nums[i] AND nums[j] == k 的情况下交换下标 i 和 j 的元素，其中 AND 表示按位与操作， k 是一个 非负整数 。

返回可以使数组按 非递减 顺序排序的最大值 k （允许进行任意次这样的交换）。如果 nums 已经是有序的，返回 0。

排列 是数组所有元素的一种重新排列。

 

示例 1：

输入：nums = [0,3,2,1]
输出：1
解释：
选择 k = 1 。交换 nums[1] = 3 和 nums[3] = 1 ，因为 nums[1] AND nums[3] == 1 ，从而得到一个排序后的排列： [0, 1, 2, 3] 。

示例 2：

输入：nums = [0,1,3,2]
输出：2
解释：
选择 k = 2 。交换 nums[2] = 3 和 nums[3] = 2 ，因为 nums[2] AND nums[3] == 2 ，从而得到一个排序后的排列： [0, 1, 2, 3] 。

示例 3：

输入：nums = [3,2,1,0]
输出：0
解释：
只有当 k = 0 时，才能进行排序，因为没有更大的 k 能够满足 nums[i] AND nums[j] == k 的交换条件。

 

提示：

1 <= n == nums.length <= 10^5
0 <= nums[i] <= n - 1
nums 是从 0 到 n - 1 的一个排列。
'''


class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        # 位运算性质：若错位元素要归位，它参与的任意一次合法交换两数与操作必须等于 k。
        # 即对每一个错位元素 x，必须满足 x & k == k，也就是 k 是每个错位元素的子集（按位与子掩码）。
        # 因此最大可行的 k 必须是所有错位元素的按位与。
        ans = -1
        for i, x in enumerate(nums):
            if i != x:
                ans &= x
        # 若数组本身已经有序，则没有任何错位元素，ans 维持 -1，题目要求返回 0
        return max(ans, 0)


# golang solution

'''
func sortPermutation(nums []int) int {
	ans := -1
	for i, x := range nums {
		if i != x {
			ans &= x
		}
	}
	if ans < 0 {
		return 0
	}
	return ans
}
'''

# solutions

'''
思路和算法：
1. 必要性分析（上界推导）：
   - 目标是将 0 到 n - 1 的排列 nums 排序为非递减顺序（即最终位置 nums[i] = i）。
   - 对于任何满足 nums[i] != i 的元素 x = nums[i]，它当前处于错误的位置，为了最终回到正确位置 x，它必须至少参与一次交换操作。
   - 题目规定只有在 nums[i] AND nums[j] == k 时才能进行交换：
     根据按位与运算的基本性质，若 a AND b == k，则必有 a AND k == k 且 b AND k == k。
     这意味着：参与交换的两个数，在二进制表示中必须包含 k 的所有为 1 的位（即 k 必须是参与交换的每一个数的子掩码 / 子集）。
   - 因为每个错位元素必须至少参与一次交换，所以 k 必须是每一个错位元素的二进制子集。
   - 换言之，k 的所有为 1 的位，在所有错位元素中都必须为 1。
   - 由此可得：k 必然是所有错位元素按位与的一个子掩码，因此 k 的最大可能值为：
     k <= bigwedge_{nums[i] != i} nums[i]

2. 充分性分析（构造证明）：
   - 记 K = bigwedge_{nums[i] != i} nums[i] 为所有错位元素的按位与。
   - 由于每个错位元素 x 都在 [0, n - 1] 范围内，并且 K 是这些元素按位与的结果，显然 0 <= K <= n - 1。
   - 因为 nums 是 [0, n - 1] 的完整排列，所以数值 K 必然在 nums 中出现且唯一。
   - 根据 K 的定义，对于任意错位元素 x，其与 K 的按位与恰好满足：
     x AND K = K
   - 这意味着，元素 K 与每一个错位元素 x 之间都存在一条合法的交换边！
   - 以 K 为“星型中心”（Hub）：
     * 无论错位元素构成了多少个置换环（permutation cycles），所有错位元素均与 K 在交换图上直接连通，构成一个连通块；
     * 在同一个置换连通分量中，通过若干次相邻对换，可以生成该集合的任意排列；
     * 如果 K 本身也是错位元素，直接在连通块内完成置换即可；
     * 如果 K 初始时恰好在正确的位置，我们可以临时借用 K 与其他错位元素交换，完成整个重排后，最后一步将 K 还原回原位。
   - 因此，只要选择 k = K，所有错位元素必定可以被完全排好！
   - 所以最大可行的 k 恰好就是全体错位元素的按位与。

3. 边界情况：
   - 若原数组已经有序（没有错位元素），题目要求直接返回 0。代码中使用 -1 作为初始值，若无错位元素更新则返回 max(ans, 0) = 0。

复杂度分析：
- 时间复杂度：O(n)，其中 n 为排列 nums 的长度。只需要对数组进行单次线性扫描，每次对错位元素执行一次常数时间的位运算，总耗时为 O(n)。
- 空间复杂度：O(1)，仅需维护常数个变量，无需额外的辅助空间。
'''

