# encoding=utf8

'''
3942. Minimum Operations to Sort a Permutation
You are given an integer array nums of length n, where nums is a permutation of the integers from 0 to n - 1.

You may perform only the following operations:

- Reverse the entire array.
- Rotate Left by One: Move the first element to the end of the array, and rest elements to left by one position.

Return an integer denoting the minimum number of operations required to sort the array in increasing order. If it is not possible to sort the array using only the given operations, return -1.

 

Example 1:

Input: nums = [0,2,1]
Output: 2
Explanation:
- Rotate Left by one: [2, 1, 0]
- Reverse the array: [0, 1, 2]
The array becomes sorted in 2 operations, which is minimal.

Example 2:

Input: nums = [1,0,2]
Output: 2
Explanation:
- Reverse the array: [2, 0, 1]
- Rotate Left by one: [0, 1, 2]
The array becomes sorted in 2 operations, which is minimal.

Example 3:

Input: nums = [2,0,1,3]
Output: -1
Explanation:
It is impossible to reach [0, 1, 2, 3]. Thus, the answer is -1.

 

Constraints:

1 <= n == nums.length <= 10^5
0 <= nums[i] <= n - 1
nums is a permutation of integers from 0 to n - 1.


3942. 排序排列的最少操作数
给你一个长度为 n 的整数数组 nums，其中 nums 是区间 [0..n - 1] 中所有数字的一个排列。

你 只能 执行以下操作：

- 反转 整个数组。
- 左旋一位：将第一个元素移动到数组末尾，其余元素整体向左移动一位。

返回将数组按 递增 顺序排序所需的 最少 操作次数。如果仅使用给定操作无法将数组排序，则返回 -1。

排列 是数组中所有元素的一种重新排列。

 

示例 1：

输入：nums = [0,2,1]
输出：2
解释：
- 左旋一位：[2, 1, 0]
- 反转数组：[0, 1, 2]
数组在 2 次操作后变为有序，这是最少操作次数。

示例 2：

输入：nums = [1,0,2]
输出：2
解释：
- 反转数组：[2, 0, 1]
- 左旋一位：[0, 1, 2]
数组在 2 次操作后变为有序，这是最少操作次数。

示例 3：

输入：nums = [2,0,1,3]
输出：-1
解释：
无法将该数组变为 [0, 1, 2, 3]。因此答案为 -1。

 

提示：

1 <= n == nums.length <= 10^5
0 <= nums[i] <= n - 1
nums 是从 0 到 n - 1 的整数排列。
'''


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        zero = nums.index(0)

        # 检查是否为顺时针环形递增（即 [0, 1, ..., n - 1] 的循环移位）
        ok_clockwise = all(nums[(zero + i) % n] == i for i in range(n))
        # 检查是否为逆时针环形递增（即 [n - 1, ..., 1, 0] 的循环移位）
        ok_counter_clockwise = all(nums[(zero - i) % n] == i for i in range(n))

        ans = float("inf")

        # 情况 1：顺时针方向递增，保持方向不变需要偶数次反转（0 次或 2 次）
        if ok_clockwise:
            # 1.1 直接左旋 zero 次使 0 回到下标 0
            ans = min(ans, zero)
            # 1.2 右旋 (n - zero) 次等价于：反转 -> 左旋 (n - zero) 次 -> 反转，共 1 + (n - zero) + 1 = n - zero + 2 次
            ans = min(ans, n - zero + 2)

        # 情况 2：逆时针方向递增，必须改变方向，需要奇数次反转（1 次反转）
        if ok_counter_clockwise:
            # 2.1 先左旋 (zero + 1) 次让 0 移到末尾，再反转数组：(zero + 1) + 1 = zero + 2 次
            ans = min(ans, zero + 2)
            # 2.2 先反转数组（0 来到 n - 1 - zero 位置），再左旋 (n - 1 - zero) 次让 0 回到开头：1 + (n - 1 - zero) = n - zero 次
            ans = min(ans, n - zero)

        return ans if ans != float("inf") else -1


# golang solution

'''
func minOperations(nums []int) int {
	n := len(nums)
	zero := 0
	for i, x := range nums {
		if x == 0 {
			zero = i
			break
		}
	}

	// 检查顺时针方向是否递增
	checkClockwise := func() bool {
		for i := 0; i < n; i++ {
			if nums[(zero+i)%n] != i {
				return false
			}
		}
		return true
	}

	// 检查逆时针方向是否递增
	checkCounterClockwise := func() bool {
		for i := 0; i < n; i++ {
			if nums[(zero-i+n)%n] != i {
				return false
			}
		}
		return true
	}

	ans := -1

	update := func(val int) {
		if ans == -1 || val < ans {
			ans = val
		}
	}

	if checkClockwise() {
		// 方式 1：直接左旋 zero 次
		update(zero)
		// 方式 2：先反转，左旋 (n - zero) 次，再反转回来：1 + (n - zero) + 1 = n - zero + 2
		update(n - zero + 2)
	}

	if checkCounterClockwise() {
		// 方式 3：先左旋 (zero + 1) 次让 0 到达末尾，再反转数组：(zero + 1) + 1 = zero + 2
		update(zero + 2)
		// 方式 4：先反转数组，再左旋 (n - 1 - zero) 次让 0 到达开头：1 + (n - 1 - zero) = n - zero
		update(n - zero)
	}

	return ans
}
'''

# solutions

'''
思路和算法：
1. 问题本质与置换群视角：
   - 给定操作只有两种：
     * 反转整个数组（记作翻转操作 Rev）
     * 左旋一位（记作旋转操作 Rot_L）
   - 左旋 k 位耗费 k 次操作；
   - 注意到右旋操作与左旋操作的关系：
     Rev(Rot_L(Rev(A))) 恰好等于右旋一位 Rot_R(A)。
     因此，右旋 k 位可以通过：反转 -> 左旋 k 次 -> 反转 完成，总共需要 1 + k + 1 = k + 2 次操作。
   - 由这两种操作生成的置换群是二面体群 D_{2n}，即仅由整个环的旋转和翻转构成。
   - 目标数组为递增排列 [0, 1, 2, ..., n - 1]。
   - 因此，原数组 nums 能否被排成递增序列，充要条件是：nums 在环形结构下必须是一个单调序列！
     即从 0 的位置 zero 开始沿某个方向遍历，必须依次是 0, 1, 2, ..., n - 1。

2. 分类讨论与最少步数推导：
   设 0 在原数组中的下标为 zero。

   情况一：顺时针方向递增（nums[(zero + i) % n] == i）
   - 该排列的方向与目标方向一致，必须包含偶数次反转（0 次或 2 次）。
   - 方式 1（0 次反转）：直接执行左旋 zero 次将 0 移动到下标 0，步数为 zero。
   - 方式 2（2 次反转）：直接将整个环向右旋转 (n - zero) 位，通过「反转 -> 左旋 (n - zero) 次 -> 反转」实现，步数为 n - zero + 2。

   情况二：逆时针方向递增（nums[(zero - i + n) % n] == i）
   - 该排列的方向与目标方向相反，必须包含奇数次反转（最少为 1 次反转）。
   - 方式 3（先旋后翻）：
     先左旋若干次将 0 移动到数组末尾（下标 n - 1），然后反转数组，此时末尾的 0 翻转后来到下标 0，其余元素随之变为升序。
     将 0 从 zero 移动到 n - 1 需要左旋 zero + 1 次（若 zero == n - 1 则无需旋转，步数为 1，该情况被方式 4 覆盖）。
     总步数为 (zero + 1) + 1 = zero + 2。
   - 方式 4（先翻后旋）：
     先执行一次反转，此时原位于 zero 的 0 会移动到下标 n - 1 - zero；
     然后左旋 (n - 1 - zero) 次将 0 移动到下标 0，总步数为 1 + (n - 1 - zero) = n - zero。

   若顺时针与逆时针都不满足，则无法排序，返回 -1。
   若满足，取上述所有可行方案的最小值即可。

复杂度分析：
- 时间复杂度：O(n)，其中 n 为数组 nums 的长度（n <= 10^5）。查找 0 的位置需要 O(n)，验证顺时针和逆时针单调性各需 O(n) 一次遍历，常数级算术计算，总时间复杂度为 O(n)。
- 空间复杂度：O(1)，仅使用常数个局部变量。
'''

