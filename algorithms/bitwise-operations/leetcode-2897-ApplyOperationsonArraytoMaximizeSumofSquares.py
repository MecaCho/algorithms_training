# encoding=utf8

'''
2897. Apply Operations on Array to Maximize Sum of Squares
You are given a 0-indexed integer array nums and a positive integer k.

You can do the following operation on the array any number of times:

Choose any two distinct indices i and j and simultaneously update the values of nums[i] to (nums[i] AND nums[j]) and nums[j] to (nums[i] OR nums[j]). Here, OR denotes the bitwise OR operation, and AND denotes the bitwise AND operation.
You have to choose k elements from the final array and calculate the sum of their squares.

Return the maximum sum of squares you can achieve.

Since the answer can be very large, return it modulo 10^9 + 7.

 

Example 1:

Input: nums = [2,6,5,8], k = 2
Output: 261
Explanation: We can do the following operations on the array:
- Choose i = 0 and j = 3, then change nums[0] to (2 AND 8) = 0 and nums[3] to (2 OR 8) = 10. The resulting array is nums = [0,6,5,10].
- Choose i = 2 and j = 3, then change nums[2] to (5 AND 10) = 0 and nums[3] to (5 OR 10) = 15. The resulting array is nums = [0,6,0,15].
We can choose the elements 15 and 6 from the final array. The sum of squares is 15^2 + 6^2 = 261.
It can be shown that this is the maximum value we can get.

Example 2:

Input: nums = [4,5,4,7], k = 3
Output: 90
Explanation: We do not need to apply any operations.
We can choose the elements 7, 5, and 4 with a sum of squares: 7^2 + 5^2 + 4^2 = 90.
It can be shown that this is the maximum value we can get.

 

Constraints:

1 <= k <= nums.length <= 10^5
1 <= nums[i] <= 10^9


2897. 对数组执行操作使平方和最大
给你一个下标从 0 开始的整数数组 nums 和一个 正 整数 k 。

你可以对数组执行以下操作 任意次 ：

选择两个互不相同的下标 i 和 j ， 同时 将 nums[i] 更新为 (nums[i] AND nums[j]) 且将 nums[j] 更新为 (nums[i] OR nums[j]) ， OR 表示按位 或 运算， AND 表示按位 与 运算。
你需要从最终的数组里选择 k 个元素，并计算它们的 平方 之和。

请你返回你可以得到的 最大 平方和。

由于答案可能会很大，将答案对 10^9 + 7 取余 后返回。

 

示例 1：

输入：nums = [2,6,5,8], k = 2
输出：261
解释：我们可以对数组执行以下操作：
- 选择 i = 0 和 j = 3 ，同时将 nums[0] 变为 (2 AND 8) = 0 且 nums[3] 变为 (2 OR 8) = 10 ，结果数组为 nums = [0,6,5,10] 。
- 选择 i = 2 和 j = 3 ，同时将 nums[2] 变为 (5 AND 10) = 0 且 nums[3] 变为 (5 OR 10) = 15 ，结果数组为 nums = [0,6,0,15] 。
从最终数组里选择元素 15 和 6 ，平方和为 15^2 + 6^2 = 261 。
261 是可以得到的最大结果。

示例 2：

输入：nums = [4,5,4,7], k = 3
输出：90
解释：不需要执行任何操作。
选择元素 7 ，5 和 4 ，平方和为 7^2 + 5^2 + 4^2 = 90 。
90 是可以得到的最大结果。

 

提示：

1 <= k <= nums.length <= 10^5
1 <= nums[i] <= 10^9
'''


class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        MOD = 1_000_000_007
        cnt = [0] * 30
        for x in nums:
            for i in range(30):
                if (x >> i) & 1:
                    cnt[i] += 1

        ans = 0
        for _ in range(k):
            val = 0
            for i in range(30):
                if cnt[i] > 0:
                    val |= 1 << i
                    cnt[i] -= 1
            ans = (ans + val * val) % MOD

        return ans


# golang solution

'''
func maxSum(nums []int, k int) int {
	const mod = 1_000_000_007
	cnt := [30]int{}
	for _, x := range nums {
		for i := 0; i < 30; i++ {
			if (x>>i)&1 == 1 {
				cnt[i]++
			}
		}
	}

	ans := 0
	for ; k > 0; k-- {
		val := 0
		for i := 0; i < 30; i++ {
			if cnt[i] > 0 {
				val |= 1 << i
				cnt[i]--
			}
		}
		ans = (ans + int(int64(val)*int64(val)%mod)) % mod
	}
	return ans
}
'''

# solutions

'''
思路和算法：

方法：按位统计 + 贪心构造

1. 操作的本质分析（按位独立性）：
   考虑操作对于二进制中某一特定位 bit 的影响：
   - 若 nums[i] 和 nums[j] 在该位上同为 1，则与运算结果为 1，或运算结果为 1，该位上的 1 的总数不变；
   - 若 nums[i] 和 nums[j] 在该位上同为 0，则与运算结果为 0，或运算结果为 0，该位上的 1 的总数不变；
   - 若一个为 1 一个为 0，则与运算为 0，或运算为 1，该位上的 1 被转移到了 nums[j] 上，总数同样不变。
   由此可见：
   - 每次操作本质上是将某一个数的二进制位 1“流动/汇聚”到另一个数上；
   - 在整个数组中，二进制每一个位上的 1 的总个数是绝对不变量（守恒）。

2. 贪心策略（平方和最大化）：
   题目要求从数组中挑选 k 个数使得其平方和最大。
   根据柯西不等式或简单的代数性质：
   设两数 a > b，若我们将 b 的一部分转移给 a，变为 a + c 与 b - c（c > 0），则：
   (a + c)^2 + (b - c)^2 = a^2 + b^2 + 2c(a - b) + 2c^2 > a^2 + b^2。
   也就是说，数值分布越两极分化、大数越大，平方和就越大。
   因此，最优策略是尽可能将每一位的 1“集中”在最大的几个数中：
   - 贪心地构造第 1 个数：只要某一位上还有 1（cnt[i] > 0），就给该数分配该位的 1；
   - 构造第 2 个数：继续在剩余的 1 中尽可能给该数分配二进制位；
   - ...重复构造出最大的 k 个数。

3. 算法实现细节：
   - 由于 1 <= nums[i] <= 10^9 < 2^30，二进制至多只有 30 位（bit 0 到 bit 29）；
   - 用长度为 30 的数组 cnt 统计所有数字在每个二进制位上 1 的出现频次；
   - 循环 k 次，每次构造一个数 val：若 cnt[i] > 0，则令 val |= 1 << i 并将 cnt[i] 减 1；
   - 累加 val^2 并对 10^9 + 7 取模。

复杂度分析：
- 时间复杂度：O(n * C + k * C)，其中 n 是数组 nums 的长度，k 是选取的数字个数，C = 30 是二进制的最大位数。统计 1 的个数需 O(n * C)，贪心构造 k 个数字需 O(k * C)，由于 C 是常数（30），总时间复杂度为 O(n + k)。
- 空间复杂度：O(C) = O(1)，仅需维护长度为 30 的位计数数组 cnt。
'''

