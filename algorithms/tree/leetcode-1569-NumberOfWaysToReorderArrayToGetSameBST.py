# encoding=utf8

'''
1569. Number of Ways to Reorder Array to Get Same BST
Given an array nums that represents a permutation of integers from 1 to n. We are going to construct a binary search tree (BST) by inserting the elements of nums in order into an initially empty BST. Find the number of different ways to reorder nums so that the constructed BST is identical to that formed from the original array nums.

For example, given nums = [2,1,3], we will have 2 as the root, 1 as a left child, and 3 as a right child. The array [2,3,1] also yields the same BST but [3,2,1] yields a different BST.

Return the number of ways to reorder nums such that the BST formed is identical to the original BST formed from nums.

Since the answer may be very large, return it modulo 10^9 + 7.

 

Example 1:

Input: nums = [2,1,3]
Output: 1
Explanation: We can reorder nums to be [2,3,1] which will yield the same BST. There are no other ways to reorder nums which will yield the same BST.

Example 2:

Input: nums = [3,4,5,1,2]
Output: 5
Explanation: The following 5 arrays will yield the same BST: 
[3,1,2,4,5]
[3,1,4,2,5]
[3,1,4,5,2]
[3,4,1,2,5]
[3,4,1,5,2]

Example 3:

Input: nums = [1,2,3]
Output: 0
Explanation: There are no other orderings of nums that will yield the same BST.

 

Constraints:

1 <= nums.length <= 1000
1 <= nums[i] <= nums.length
All integers in nums are distinct.


1569. 将子数组重新排序得到同一个二叉搜索树的方案数
给你一个数组 nums 表示 1 到 n 的一个排列。我们按照元素在 nums 中的顺序依次插入一个初始为空的二叉搜索树（BST）。请你找出有多少种对 nums 重新排序的方式，使得重新构建的 BST 与基于原始数组 nums 构建的 BST 相同。

例如，如果 nums = [2,1,3]，我们得到一棵 2 为根，1 为左子节点，3 为右子节点的树。数组 [2,3,1] 也能得到相同的 BST，但 [3,2,1] 会得到一棵不同的 BST 。

请你返回对 nums 重新排序后可以得到相同 BST 的方案数。

由于答案可能会很大，请你将它对 10^9 + 7 取余后返回。

 

示例 1：

输入：nums = [2,1,3]
输出：1
解释：我们将 nums 重排为 [2,3,1] 也能得到相同的 BST。没有其他得到相同 BST 的方案了。

示例 2：

输入：nums = [3,4,5,1,2]
输出：5
解释：下面 5 个数组会得到相同的 BST：
[3,1,2,4,5]
[3,1,4,2,5]
[3,1,4,5,2]
[3,4,1,2,5]
[3,4,1,5,2]

示例 3：

输入：nums = [1,2,3]
输出：0
解释：没有其他能得到相同的 BST 的方案了。

 

提示：

1 <= nums.length <= 1000
1 <= nums[i] <= nums.length
nums 中所有数 互不相同 。
'''


class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        MOD = 1_000_000_007

        def dfs(arr: List[int]) -> int:
            if len(arr) <= 2:
                return 1

            root = arr[0]
            left = [x for x in arr[1:] if x < root]
            right = [x for x in arr[1:] if x > root]

            m, k = len(left), len(right)
            # 从 m + k 个位置中选出 m 个位置放置左子树节点，其余 k 个位置放置右子树节点
            ways = math.comb(m + k, m) % MOD
            return (ways * dfs(left) % MOD * dfs(right)) % MOD

        # 题目要求重新排序的不同方案数，需排除初始给定的序列本身
        return (dfs(nums) - 1 + MOD) % MOD


# golang solution

'''
const mod int = 1000000007

func numOfWays(nums []int) int {
	n := len(nums)
	// 预处理组合数 C(i, j) = C(i-1, j-1) + C(i-1, j)
	c := make([][]int, n+1)
	for i := 0; i <= n; i++ {
		c[i] = make([]int, i+1)
		c[i][0] = 1
		c[i][i] = 1
		for j := 1; j < i; j++ {
			c[i][j] = (c[i-1][j-1] + c[i-1][j]) % mod
		}
	}

	var dfs func(arr []int) int
	dfs = func(arr []int) int {
		if len(arr) <= 2 {
			return 1
		}
		root := arr[0]
		var left, right []int
		for _, x := range arr[1:] {
			if x < root {
				left = append(left, x)
			} else {
				right = append(right, x)
			}
		}
		m, k := len(left), len(right)
		ways := c[m+k][m]
		return ways * dfs(left) % mod * dfs(right) % mod
	}

	return (dfs(nums) - 1 + mod) % mod
}
'''

# solutions

'''
思路和算法：
1. 二叉搜索树（BST）性质与插入顺序：
   - 当按照数组顺序依次将元素插入到空的 BST 中时，数组的第一个元素 nums[0] 必然成为整棵树的根节点。
   - 所有小于 nums[0] 的元素都会被插入到左子树中，所有大于 nums[0] 的元素都会被插入到右子树中。
   - 并且，左子树中所有元素之间的相对插入次序，决定了左子树的结构；右子树中所有元素之间的相对插入次序，决定了右子树的结构。
   - 关键观察：左子树的所有元素与右子树的所有元素之间可以任意交叉混排（交错插入），只要它们各自内部的相对顺序保持不变，构建出的二叉搜索树形态就完全相同！

2. 组合计数与分治递归：
   - 设当前子树序列为 arr，长度为 L = len(arr)。根节点为 arr[0]。
   - 根据与根节点的大小关系将 arr[1:] 划分为：
     * left：小于根节点的元素序列（设长度为 m = len(left)）
     * right：大于根节点的元素序列（设长度为 k = len(right)）
   - 在除去根节点后的剩余 m + k 个位置中，任选 m 个位置放置 left 中的元素，其余 k 个位置放置 right 中的元素。
     每一种位置分配方案都是合法的，并且 left 和 right 内部相对顺序各自固定。因此交错重排的方式共有 C(m + k, m) 种。
   - 由乘法原理，以 arr 为节点的 BST 构建方案数为：
     dfs(arr) = C(m + k, m) * dfs(left) * dfs(right) % MOD
   - 递归基：
     当序列长度 <= 2 时，无论是一个节点、两个节点还是空节点，唯一的相对顺序只有 1 种，返回 1。
   - 排除自身：
     题目要求求“重新排序的方式数”（different ways to reorder），因此需要排除初始输入序列本身，最终答案为 (dfs(nums) - 1 + MOD) % MOD。

3. 补充：树拓扑序定理 / 树形钩子公式（Hook-Length Formula for Trees）：
   - 该问题等价于求外向树（Out-Tree，父节点指向子节点）的拓扑排序方案数（Linear Extensions of Poset）。
   - 由树的钩子定理，一个 n 节点有向树满足父节点排在子节点前面的排列总数严格等于：
     n! / prod_{u in T} size(u)
     其中 size(u) 为以 u 为根的子树节点个数。
   - 本题直接采用基于子树划分的分治递归更直观，由于 n <= 1000，使用杨辉三角预处理组合数或内置组合函数 math.comb 计算组合数极为高效。

复杂度分析：
- 时间复杂度：O(n^2)，其中 n 为数组 nums 的长度（n <= 1000）。
  * 预处理杨辉三角组合数耗时 O(n^2)。
  * 分治递归过程中，每一层遍历当前序列元素划分为 left 和 right，最坏情况下（树退化为单链）递归深度为 O(n)，总比较与划分次数为 sum_{i=1}^n i = O(n^2)；最好/平均情况下（树较为平衡）递归深度为 O(log n)，划分次数为 O(n log n)。
  * 综合时间复杂度为 O(n^2)。
- 空间复杂度：O(n^2) 或 O(n)。
  * Go 语言中预处理二维组合数表耗费 O(n^2) 空间；Python 中若借助 math.comb 则无需存表。
  * 递归栈深度及切片存储在最坏情况下为 O(n)（通过设置系统递归深度限制确保不溢出）。
'''

