# encoding=utf8
from typing import List

'''
1477. Find Two Non-overlapping Sub-arrays Each With Target Sum
You are given an array of integers arr and an integer target.

You have to find two non-overlapping sub-arrays of arr each with a sum equal target. There can be multiple answers so you have to find an answer where the sum of the lengths of the two sub-arrays is minimum.

Return the minimum sum of the lengths of the two required sub-arrays, or return -1 if you cannot find such two sub-arrays.

 

Example 1:

Input: arr = [3,2,2,4,3], target = 3
Output: 2
Explanation: Only two sub-arrays have sum = 3 ([3] and [3]). The sum of their lengths is 2.

Example 2:

Input: arr = [7,3,4,7], target = 7
Output: 2
Explanation: Although we have three non-overlapping sub-arrays of sum = 7 ([7], [3,4] and [7]), but we will choose the first and third sub-arrays as the sum of their lengths is 2.

Example 3:

Input: arr = [4,3,2,6,2,3,4], target = 6
Output: -1
Explanation: We have only one sub-array of sum = 6.

 

Constraints:

1 <= arr.length <= 10^5
1 <= arr[i] <= 1000
1 <= target <= 10^8


1477. 找两个和为目标值且不重叠的子数组
给你一个整数数组 arr 和一个整数值 target 。

请你在 arr 中找 两个互不重叠的子数组 且它们的和都等于 target 。可能会有多种方案，请你返回满足要求的两个子数组长度和的 最小值 。

请返回满足要求的最小长度和，如果无法找到这样的两个子数组，请返回 -1 。

 

示例 1：

输入：arr = [3,2,2,4,3], target = 3
输出：2
解释：只有两个子数组和为 3 （[3] 和 [3]）。它们的长度和为 2 。

示例 2：

输入：arr = [7,3,4,7], target = 7
输出：2
解释：尽管我们有 3 个互不重叠的子数组和为 7 （[7], [3,4] 和 [7]），但我们会选择第一个和第三个子数组，因为它们的长度和 2 是最小值。

示例 3：

输入：arr = [4,3,2,6,2,3,4], target = 6
输出：-1
解释：我们只有一个和为 6 的子数组。

示例 4：

输入：arr = [5,5,4,4,5], target = 3
输出：-1
解释：我们无法找到和为 3 的子数组。

示例 5：

输入：arr = [3,1,1,1,5,1,2,1], target = 3
输出：3
解释：注意子数组 [1,2] 和 [2,1] 不能成为一个方案因为它们重叠了。

 

提示：

1 <= arr.length <= 10^5
1 <= arr[i] <= 1000
1 <= target <= 10^8
'''


class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        INF = float("inf")
        # min_len[i] 表示在 arr[0 ... i-1] 前缀范围内，和为 target 的最短子数组长度
        min_len = [INF] * (n + 1)
        ans = INF

        l = 0
        cur_sum = 0
        for r in range(n):
            cur_sum += arr[r]
            while cur_sum > target:
                cur_sum -= arr[l]
                l += 1

            min_len[r + 1] = min_len[r]
            if cur_sum == target:
                length = r - l + 1
                # 若当前窗口左侧存在和为 target 的合法子数组，尝试更新全局最小长度和
                if min_len[l] != INF:
                    ans = min(ans, length + min_len[l])
                min_len[r + 1] = min(min_len[r + 1], length)

        return -1 if ans == INF else ans


class SolutionHashMap:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        INF = float("inf")
        prefix_map = {0: 0}
        min_len = [INF] * (n + 1)
        ans = INF
        cur_sum = 0

        for i, val in enumerate(arr, 1):
            cur_sum += val
            min_len[i] = min_len[i - 1]
            if cur_sum - target in prefix_map:
                j = prefix_map[cur_sum - target]
                length = i - j
                if min_len[j] != INF:
                    ans = min(ans, length + min_len[j])
                min_len[i] = min(min_len[i], length)
            prefix_map[cur_sum] = i

        return -1 if ans == INF else ans


# golang solution

'''
// 方法一：滑动窗口 + 动态规划
func minSumOfLengths(arr []int, target int) int {
	n := len(arr)
	const inf = 1 << 30
	// minLen[i] 表示在 arr[0 ... i-1] 中和为 target 的子数组的最小长度
	minLen := make([]int, n+1)
	for i := range minLen {
		minLen[i] = inf
	}

	ans := inf
	l := 0
	curSum := 0

	min := func(a, b int) int {
		if a < b {
			return a
		}
		return b
	}

	for r := 0; r < n; r++ {
		curSum += arr[r]
		for curSum > target {
			curSum -= arr[l]
			l++
		}
		minLen[r+1] = minLen[r]
		if curSum == target {
			length := r - l + 1
			// 如果在左侧（下标小于 l 的前缀中）存在和为 target 的子数组，更新最小长度和
			if minLen[l] != inf {
				ans = min(ans, length+minLen[l])
			}
			minLen[r+1] = min(minLen[r+1], length)
		}
	}

	if ans == inf {
		return -1
	}
	return ans
}

// 方法二：前缀和 + 哈希表 + 动态规划
func minSumOfLengthsHash(arr []int, target int) int {
	n := len(arr)
	const inf = 1 << 30
	minLen := make([]int, n+1)
	for i := range minLen {
		minLen[i] = inf
	}

	pos := make(map[int]int)
	pos[0] = 0
	ans := inf
	curSum := 0

	min := func(a, b int) int {
		if a < b {
			return a
		}
		return b
	}

	for i := 1; i <= n; i++ {
		curSum += arr[i-1]
		minLen[i] = minLen[i-1]
		if j, ok := pos[curSum-target]; ok {
			length := i - j
			if minLen[j] != inf {
				ans = min(ans, length+minLen[j])
			}
			minLen[i] = min(minLen[i], length)
		}
		pos[curSum] = i
	}

	if ans == inf {
		return -1
	}
	return ans
}
'''

# solutions

'''
思路和算法：

方法一：滑动窗口 + 动态规划（最优解）

1. 单调性与滑动窗口：
   题目中给出条件 1 <= arr[i] <= 1000，所有元素均为正整数。
   正整数意味着前缀和具有严格单调递增的性质。
   当使用双指针 [l, r] 维护窗口和 cur_sum 时：
   - 右指针 r 向右移动，窗口和单调递增；
   - 当 cur_sum > target 时，左指针 l 向右移动，窗口和单调递减；
   - 当 cur_sum == target 时，说明子数组 arr[l ... r] 的和恰好为 target，其长度为 length = r - l + 1。
   因为元素全为正数，以固定右端点 r 结尾且和为 target 的子数组至多只有一个。

2. 互不重叠约束与动态规划数组：
   我们要求找两个“互不重叠”的子数组。
   当我们在当前位置以 arr[l ... r] 作为一个子数组时，另一个子数组必须完全位于当前子数组的左侧，即必须在下标范围 [0 ... l - 1] 内部。
   因此，我们维护一个数组 min_len，其中 min_len[i] 表示在 arr[0 ... i-1]（即前 i 个元素）中已找到的和为 target 的子数组的最小长度：
   - 如果当前找到了合法子数组 arr[l ... r]，且 min_len[l] != INF，说明在其左侧至少存在一个和为 target 的子数组，此时我们可以配对，得到长度和：
     length + min_len[l]
     用其更新全局最优答案 ans = min(ans, length + min_len[l])。
   - 然后更新截至当前右端点的前缀最小长度：
     min_len[r + 1] = min(min_len[r], length)；
   - 若当前窗口和不为 target，则继承前缀最优值：
     min_len[r + 1] = min_len[r]。

3. 初始条件与边界：
   - 初始化 min_len 数组全为正无穷（INF）。
   - 初始化 ans = INF。
   - 遍历结束后，若 ans 仍为 INF，说明无法找到两个不重叠的子数组，返回 -1；否则返回 ans。

复杂度分析：
- 时间复杂度：O(n)，左右指针 l 和 r 在整个遍历过程中至多各自移动 n 次，每个元素进出窗口各一次，状态更新时间为 O(1)。
- 空间复杂度：O(n)，需要一个长度为 n + 1 的数组 min_len 记录前缀最优解。

---

方法二：前缀和 + 哈希表 + 动态规划

1. 若元素包含 0 或负数（本题为正整数，此方法作为通用泛化思路）：
   不能直接使用滑动窗口的双指针，但可以使用前缀和哈希表记录每个前缀和首次/最近出现的下标。
   对于当前前缀和 cur_sum，若 cur_sum - target 在哈希表中存在下标 j，则区间 arr[j ... i-1] 和为 target，长度为 i - j。
   同样利用 min_len[j] 进行配对更新：
   ans = min(ans, (i - j) + min_len[j])。

复杂度分析：
- 时间复杂度：O(n)，哈希表单次查询与插入平均复杂度为 O(1)。
- 空间复杂度：O(n)，哈希表与 DP 数组空间。
'''

