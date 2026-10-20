# encoding=utf8

'''
3886. Sum of Sortable Integers
You are given an integer array nums of length n.

An integer k is called sortable if k divides n and you can sort nums in non-decreasing order by sequentially performing the following operations:

    Partition nums into consecutive subarrays of length k.
    Cyclically rotate each subarray independently any number of times to the left or to the right.

Return an integer denoting the sum of all possible sortable integers k.

 

Example 1:

Input: nums = [3,1,2]
Output: 3
Explanation:
For n = 3, possible divisors are 1 and 3.
For k = 1: each subarray has one element. No rotation can sort the array.
For k = 3: the single subarray [3, 1, 2] can be rotated once to produce [1, 2, 3], which is sorted.
Only k = 3 is sortable. Hence, the answer is 3.

Example 2:

Input: nums = [7,6,5]
Output: 0
Explanation:
For n = 3, possible divisors are 1 and 3.
For k = 1: each subarray has one element. No rotation can sort the array.
For k = 3: the single subarray [7, 6, 5] cannot be rotated into non-decreasing order.
No k is sortable. Hence, the answer is 0.

Example 3:

Input: nums = [5,8]
Output: 3
Explanation:
For n = 2, possible divisors are 1 and 2.
Since [5, 8] is already sorted, every divisor is sortable. Hence, the answer is 1 + 2 = 3.

 

Constraints:

1 <= n == nums.length <= 10^5
1 <= nums[i] <= 10^5


3886. 可排序整数求和
给你一个长度为 n 的整数数组 nums。

如果一个整数 k 满足以下条件，则称其为 可排序整数：k 是 n 的 因数，且可以通过依次执行以下操作将 nums 排序为 非递减顺序：

    将 nums 划分为长度为 k 的 连续子数组。
    独立地对每个子数组进行循环移动（左移或右移任意次数）。

返回所有可能的可排序整数 k 的和。

子数组 是数组中的一个连续、非空元素序列。

 

示例 1：

输入：nums = [3,1,2]
输出：3
解释：
对于 n = 3，可能的因数是 1 和 3。
对于 k = 1：每个子数组都只有一个元素。无法通过移动使数组排序。
对于 k = 3：单个子数组 [3, 1, 2] 可以通过旋转一次得到 [1, 2, 3]，从而将数组排序。
只有 k = 3 可排序，因此答案是 3。

示例 2：

输入：nums = [7,6,5]
输出：0
解释：
对于 n = 3，可能的因数是 1 和 3。
对于 k = 1：每个子数组都只有一个元素。无法通过移动使数组排序。
对于 k = 3：单个子数组 [7, 6, 5] 无法通过任何移动排序为非递减顺序。
没有任何可排序的 k，因此答案是 0。

示例 3：

输入：nums = [5,8]
输出：3
解释：
对于 n = 2，可能的因数是 1 和 2。
由于 [5, 8] 本身已经有序，每个因数都可排序。因此答案是 1 + 2 = 3。

 

提示：

1 <= n == nums.length <= 10^5
1 <= nums[i] <= 10^5
'''


class Solution:
    def sortableIntegers(self, nums: List[int]) -> int:
        n = len(nums)

        # 前缀最大值：pref_max[i] 表示 nums[0..i-1] 的最大值，pref_max[0] = 0
        pref_max = [0] * (n + 1)
        for i, x in enumerate(nums):
            pref_max[i + 1] = max(pref_max[i], x)

        # 后缀最小值：suff_min[i] 表示 nums[i..n-1] 的最小值，suff_min[n] = inf
        suff_min = [10**9] * (n + 1)
        for i in range(n - 1, -1, -1):
            suff_min[i] = min(nums[i], suff_min[i + 1])

        # 前缀相邻严格下降对计数：pref_drop[i] 表示 nums[0..i] 中相邻满足 nums[j-1] > nums[j] 的次数
        pref_drop = [0] * n
        for i in range(1, n):
            pref_drop[i] = pref_drop[i - 1] + (1 if nums[i - 1] > nums[i] else 0)

        def check(k: int) -> bool:
            for start in range(0, n, k):
                end = start + k - 1
                # 统计当前长度为 k 的块内的环形下降次数
                # 块内部相邻下降次数
                drops = pref_drop[end] - pref_drop[start]
                # 块首尾循环接缝处下降（首尾相接）
                if nums[end] > nums[start]:
                    drops += 1
                # 条件 1：块内环形严格下降次数不超过 1 次，才存在循环位移使其非递减
                # 条件 2：块与块之间的有序性，前一个块的最大值（等价于前缀最大值）不超过后续所有元素的最小值
                if drops > 1 or pref_max[start] > suff_min[start]:
                    return False
            return True

        ans = 0
        i = 1
        while i * i <= n:
            if n % i == 0:
                if check(i):
                    ans += i
                other = n // i
                if i != other and check(other):
                    ans += other
            i += 1

        return ans


# golang solution

'''
func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func sortableIntegers(nums []int) int {
	n := len(nums)
	prefMax := make([]int, n+1)
	for i, x := range nums {
		prefMax[i+1] = max(prefMax[i], x)
	}

	suffMin := make([]int, n+1)
	suffMin[n] = 1000000000
	for i := n - 1; i >= 0; i-- {
		suffMin[i] = min(nums[i], suffMin[i+1])
	}

	prefDrop := make([]int, n)
	for i := 1; i < n; i++ {
		prefDrop[i] = prefDrop[i-1]
		if nums[i-1] > nums[i] {
			prefDrop[i]++
		}
	}

	check := func(k int) bool {
		for start := 0; start < n; start += k {
			end := start + k - 1
			drops := prefDrop[end] - prefDrop[start]
			if nums[end] > nums[start] {
				drops++
			}
			if drops > 1 || prefMax[start] > suffMin[start] {
				return false
			}
		}
		return true
	}

	ans := 0
	for i := 1; i*i <= n; i++ {
		if n%i == 0 {
			if check(i) {
				ans += i
			}
			other := n / i
			if i != other && check(other) {
				ans += other
			}
		}
	}
	return ans
}
'''

# solutions

'''
思路和算法：
1. 问题转化与块内可排序充要条件：
   - 设数组长度为 n，对于 n 的任意因数 k，我们将 nums 划分为 m = n / k 个长度为 k 的连续子数组（块）B_0, B_1, ..., B_{m-1}。
   - 每个子数组 B_t 可以独立进行任意次循环位移。
   - 一个长度为 k 的子数组 B 能够通过循环位移变为非递减数组，当且仅当将 B 首尾相接看作环形数组时，相邻严格下降（即 x > y）的次数至多为 1 次：
     * 若环形下降次数为 0，说明块内所有元素均相等，天然有序；
     * 若环形下降次数恰为 1，在下降断点处切开即为非递减顺序；
     * 若环形下降次数大于等于 2，无论从何处断开线性排列，内部都至少保留一个严格下降位置，故无法排成非递减。

2. 块间全局非递减充要条件：
   - 当每个块 B_t 都通过循环位移变成了非递减序列后，其块首必为该块的最小值 min(B_t)，块尾必为该块的最大值 max(B_t)。
   - 拼接后的整个数组是非递减的，当且仅当对于任意相邻两个块，前一个块的最大值不超过后一个块的最小值，即：
     max(B_{t-1}) <= min(B_t)，对所有 1 <= t < m 成立。
   - 这一性质等价于：对于任意分界点 start = t * k (1 <= t < m)，前缀最大值不大于后缀最小值：
     max(nums[0..start-1]) <= min(nums[start..n-1])。

3. 前缀预处理与 O(1) 块判定：
   - 预处理前缀最大值数组 pref_max，其中 pref_max[i] = max(nums[0..i-1])；
   - 预处理后缀最小值数组 suff_min，其中 suff_min[i] = min(nums[i..n-1])；
   - 预处理前缀相邻下降次数 pref_drop，其中 pref_drop[i] 记录 nums[0..i] 中满足 nums[j-1] > nums[j] 的次数。
   - 这样对于任意块 [start, end] (其中 end = start + k - 1)：
     * 块内部相邻下降次数为 pref_drop[end] - pref_drop[start]；
     * 块末到块首的环形连接下降判断为 1 if nums[end] > nums[start] else 0；
     * 分界线合法性判断直接比较 pref_max[start] <= suff_min[start]。
   - 每个块的校验耗时 O(1)，单次检查 k 的总耗时为 O(n / k)。

4. 枚举因数与复杂度分析：
   - 在 O(sqrt(n)) 内枚举 n 的所有正因数 k；
   - 对每个因数 k 执行 check(k)，耗时 O(n / k)；
   - 所有因数检验耗时总和为 sum_{k|n} (n / k) = sum_{d|n} d = sigma_1(n)（因数和函数）。
   - 在 n <= 10^5 范围内，因数和的最大值为 sigma_1(98280) = 403200，运算量极小，可在毫秒级通过。

复杂度分析：
- 时间复杂度：O(n + sigma_1(n))，其中 n 是数组 nums 的长度，sigma_1(n) 为 n 的所有正因数之和。预处理前缀和与最值数组耗时 O(n)，枚举并检验所有因数总步数为 sigma_1(n) <= 403200。总时间复杂度线性，极端高效。
- 空间复杂度：O(n)，需要大小为 O(n) 的辅助数组存储前缀最大值 pref_max、后缀最小值 suff_min 以及前缀下降统计 pref_drop。
'''

