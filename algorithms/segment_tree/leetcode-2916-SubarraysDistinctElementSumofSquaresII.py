# encoding=utf8

'''
2916. Subarrays Distinct Element Sum of Squares II
You are given a 0-indexed integer array nums.

The distinct count of a subarray of nums is defined as:

    Let nums[i..j] be a subarray of nums consisting of all the indices from i to j such that 0 <= i <= j < nums.length. Then the number of distinct values in nums[i..j] is called the distinct count of nums[i..j].

Return the sum of the squares of distinct counts of all subarrays of nums.

Since the answer may be very large, return it modulo 10^9 + 7.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,2,1]
Output: 15
Explanation: Six possible subarrays are:
[1]: 1 distinct value
[2]: 1 distinct value
[1]: 1 distinct value
[1,2]: 2 distinct values
[2,1]: 2 distinct values
[1,2,1]: 2 distinct values
The sum of the squares of the distinct counts in all subarrays is equal to 1^2 + 1^2 + 1^2 + 2^2 + 2^2 + 2^2 = 15.

Example 2:

Input: nums = [2,2]
Output: 3
Explanation: Three possible subarrays are:
[2]: 1 distinct value
[2]: 1 distinct value
[2,2]: 1 distinct value
The sum of the squares of the distinct counts in all subarrays is equal to 1^2 + 1^2 + 1^2 = 3.

 

Constraints:

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^5


2916. 子数组不同元素数目的平方和 II
给你一个下标从 0 开始的整数数组 nums 。

定义 nums 一个子数组的 不同计数 值如下：
令 nums[i..j] 表示 nums 中所有下标在 i 到 j 范围内的元素构成的子数组（满足 0 <= i <= j < nums.length ）。那么 nums[i..j] 的 不同计数 就是 nums[i..j] 中不同整数的数目。

请你返回 nums 所有子数组的 不同计数 的 平方和 。

由于答案可能会很大，请你将它对 10^9 + 7 取余后返回。

子数组是数组中一段连续 非空 的元素序列。

 

示例 1：

输入：nums = [1,2,1]
输出：15
解释：六个子数组分别为：
[1]：1 个不同的值
[2]：1 个不同的值
[1]：1 个不同的值
[1,2]：2 个不同的值
[2,1]：2 个不同的值
[1,2,1]：2 个不同的值
不同计数的平方和为 1^2 + 1^2 + 1^2 + 2^2 + 2^2 + 2^2 = 15 。

示例 2：

输入：nums = [2,2]
输出：3
解释：三个子数组分别为：
[2]：1 个不同的值
[2]：1 个不同的值
[2,2]：1 个不同的值
不同计数的平方和为 1^2 + 1^2 + 1^2 = 3 。

 

提示：

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^5
'''


class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 1_000_000_007
        n = len(nums)

        # 4 * n 线段树数组维护区间一次和与平方和
        tree_sum1 = [0] * (4 * n + 5)
        tree_sum2 = [0] * (4 * n + 5)
        tree_lazy = [0] * (4 * n + 5)

        def apply(o: int, l: int, r: int, val: int) -> None:
            length = r - l + 1
            tree_sum2[o] = (tree_sum2[o] + 2 * val * tree_sum1[o] + val * val * length) % MOD
            tree_sum1[o] = (tree_sum1[o] + val * length) % MOD
            tree_lazy[o] = (tree_lazy[o] + val) % MOD

        def push_down(o: int, l: int, r: int) -> None:
            if tree_lazy[o]:
                mid = (l + r) >> 1
                apply(o << 1, l, mid, tree_lazy[o])
                apply(o << 1 | 1, mid + 1, r, tree_lazy[o])
                tree_lazy[o] = 0

        def update(o: int, l: int, r: int, ql: int, qr: int) -> None:
            if ql <= l and r <= qr:
                apply(o, l, r, 1)
                return
            push_down(o, l, r)
            mid = (l + r) >> 1
            if ql <= mid:
                update(o << 1, l, mid, ql, qr)
            if qr > mid:
                update(o << 1 | 1, mid + 1, r, ql, qr)
            tree_sum1[o] = (tree_sum1[o << 1] + tree_sum1[o << 1 | 1]) % MOD
            tree_sum2[o] = (tree_sum2[o << 1] + tree_sum2[o << 1 | 1]) % MOD

        last_pos = {}
        ans = 0
        for j, x in enumerate(nums):
            # x 上一次出现位置为 last_pos.get(x, -1)，对应 1-based 下标区间 [last + 2, j + 1]
            l = last_pos.get(x, -1) + 2
            r = j + 1
            update(1, 1, n, l, r)
            ans = (ans + tree_sum2[1]) % MOD
            last_pos[x] = j

        return ans


# golang solution

'''
const mod int = 1000000007

type segNode struct {
	sum1 int
	sum2 int
	lazy int
}

type segTree struct {
	tree []segNode
}

func newSegTree(n int) *segTree {
	return &segTree{
		tree: make([]segNode, 4*n+5),
	}
}

func (st *segTree) apply(o, l, r, val int) {
	length := r - l + 1
	st.tree[o].sum2 = (st.tree[o].sum2 + 2*val*st.tree[o].sum1 + val*val%mod*length) % mod
	st.tree[o].sum1 = (st.tree[o].sum1 + val*length) % mod
	st.tree[o].lazy = (st.tree[o].lazy + val) % mod
}

func (st *segTree) pushDown(o, l, r int) {
	if st.tree[o].lazy != 0 {
		mid := (l + r) >> 1
		st.apply(o<<1, l, mid, st.tree[o].lazy)
		st.apply(o<<1|1, mid+1, r, st.tree[o].lazy)
		st.tree[o].lazy = 0
	}
}

func (st *segTree) update(o, l, r, ql, qr int) {
	if ql <= l && r <= qr {
		st.apply(o, l, r, 1)
		return
	}
	st.pushDown(o, l, r)
	mid := (l + r) >> 1
	if ql <= mid {
		st.update(o<<1, l, mid, ql, qr)
	}
	if qr > mid {
		st.update(o<<1|1, mid+1, r, ql, qr)
	}
	st.tree[o].sum1 = (st.tree[o<<1].sum1 + st.tree[o<<1|1].sum1) % mod
	st.tree[o].sum2 = (st.tree[o<<1].sum2 + st.tree[o<<1|1].sum2) % mod
}

func sumCounts(nums []int) int {
	n := len(nums)
	st := newSegTree(n)
	lastPos := make(map[int]int)
	ans := 0

	for j, x := range nums {
		l := 1
		if p, ok := lastPos[x]; ok {
			l = p + 2
		}
		r := j + 1
		st.update(1, 1, n, l, r)
		ans = (ans + st.tree[1].sum2) % mod
		lastPos[x] = j
	}

	return ans
}
'''

# solutions

'''
思路和算法：
1. 问题转化：
   - 记 f(i, j) 为子数组 nums[i..j] (0 <= i <= j) 中不同元素的个数。
   - 目标是求所有子数组不同元素数的平方和：sum_{j=0}^{n-1} sum_{i=0}^j f(i, j)^2。
   - 考虑固定右端点 j，当右端点从 j-1 扩展到 j 时，观察各个左端点 i 的 f(i, j) 相比 f(i, j-1) 的变化：
     * 设 nums[j] 上一次在数组中出现的位置为 last（若未出现过，则 last = -1）。
     * 若左端点 i 满足 i <= last，说明 nums[j] 已经在 nums[i..j-1] 中出现过，包含该元素不会增加不同元素的个数，即 f(i, j) = f(i, j-1)；
     * 若左端点 i 满足 last < i <= j，说明 nums[j] 是区间 nums[i..j] 内首次出现的新元素，因此 f(i, j) = f(i, j-1) + 1（约定 f(j, j-1) = 0）。
   - 由此可知，每次将右端点从 j-1 移动到 j 时，相当于对所有 i in [last + 1, j] 的 f(i, .) 执行了区间加 1 操作。

2. 线段树维护平方和与一次和：
   - 维护一个序列 A，初始时全为 0。
   - 每次将区间 [last + 1, j] 的每个数增加 1，然后求 sum_{i=0}^j A[i]^2。
   - 因为对于 i > j，A[i] 始终为 0，所以 sum_{i=0}^j A[i]^2 恰好等于整个序列的平方和 sum_{i=0}^{n-1} A[i]^2。
   - 当区间内的每个数由 v 变为 v + c 时：
     (v + c)^2 = v^2 + 2*c*v + c^2
     对区间求和：
     sum (v + c)^2 = sum v^2 + 2*c*(sum v) + c^2 * len
     sum (v + c)   = sum v + c * len
   - 因此，线段树的每个节点只需维护两个属性和一个懒标记：
     * sum2：当前区间元素的平方和 sum v^2
     * sum1：当前区间元素的一次和 sum v
     * lazy：区间加法延迟标记
   - 每次区间更新后，线段树根节点的 sum2 即为所有以 j 结尾的子数组不同元素数目的平方和，直接将其累加到总答案中即可。

复杂度分析：
- 时间复杂度：O(n log n)，其中 n 是数组 nums 的长度。共遍历 n 个元素，每次在线段树中进行一次区间修改，耗时 O(log n)。查询只需取根节点的 sum2，耗时 O(1)。总时间复杂度为 O(n log n)。
- 空间复杂度：O(n)，线段树节点数组大小为 4n，哈希表 last_pos 最多存储 n 个不同元素的最近下标，额外空间复杂度为 O(n)。
'''

