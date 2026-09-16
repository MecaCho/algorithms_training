# encoding=utf8

'''
1621. Number of Sets of K Non-Overlapping Line Segments
Given n points on a 1-D plane, where the ith point (from 0 to n-1) is at x = i, find the number of ways we can draw exactly k non-overlapping line segments such that each segment covers two or more points. The endpoints of each segment must have integral coordinates. The k line segments do not have to cover all n points, and they are allowed to share endpoints.

Return the number of ways we can draw k non-overlapping line segments. Since this number can be huge, return it modulo 10^9 + 7.

 

Example 1:

Input: n = 4, k = 2
Output: 5
Explanation: The two line segments are shown in red and blue.
The image above shows the 5 different ways {(0,2),(2,3)}, {(0,1),(1,3)}, {(0,1),(2,3)}, {(1,2),(2,3)}, {(0,1),(1,2)}.

Example 2:

Input: n = 3, k = 1
Output: 3
Explanation: The 3 ways are {(0,1)}, {(0,2)}, {(1,2)}.

Example 3:

Input: n = 30, k = 7
Output: 796297179
Explanation: The total number of possible ways to draw 7 line segments is 3796297200. Taking this number modulo 10^9 + 7 gives us 796297179.

 

Constraints:

2 <= n <= 1000
1 <= k <= n-1


1621. 大小为 K 的不重叠线段的数目
给你一维空间的 n 个点，其中第 i 个点（编号从 0 到 n-1）位于 x = i 处，请你找到 恰好 k 个不重叠 线段且每个线段至少覆盖两个点的方案数。线段的两个端点必须都是 整数坐标 。这 k 个线段不需要全部覆盖全部 n 个点，且它们的端点 可以 重合。

请你返回 k 个不重叠线段的方案数。由于答案可能很大，请将结果对 10^9 + 7 取余 后返回。

 

示例 1：

输入：n = 4, k = 2
输出：5
解释：
如图所示，两个线段分别用红色和蓝色标出。
上图展示了 5 种不同的方案 {(0,2),(2,3)}，{(0,1),(1,3)}，{(0,1),(2,3)}，{(1,2),(2,3)}，{(0,1),(1,2)} 。

示例 2：

输入：n = 3, k = 1
输出：3
解释：总共有 3 种不同的方案 {(0,1)}, {(0,2)}, {(1,2)} 。

示例 3：

输入：n = 30, k = 7
输出：796297179
解释：画 7 条线段的总方案数为 3796297200 种。将这个数对 10^9 + 7 取余得到 796297179 。

示例 4：

输入：n = 5, k = 3
输出：7

示例 5：

输入：n = 3, k = 2
输出：1

 

提示：

2 <= n <= 1000
1 <= k <= n-1
'''


class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 1_000_000_007
        # 组合数学等价变换: C(n + k - 1, 2k)
        return math.comb(n + k - 1, 2 * k) % MOD


class SolutionDP:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 1_000_000_007
        # f[j]: 未处于线段延伸状态，形成 j 条线段的方案数
        # g[j]: 正处于某条线段延伸状态，正在/已经形成第 j 条线段的方案数
        f = [0] * (k + 1)
        g = [0] * (k + 1)
        f[0] = 1
        for i in range(1, n):
            new_f = [0] * (k + 1)
            new_g = [0] * (k + 1)
            for j in range(k + 1):
                new_f[j] = (f[j] + g[j]) % MOD
                new_g[j] = g[j]
                if j > 0:
                    new_g[j] = (new_g[j] + f[j - 1] + g[j - 1]) % MOD
            f, g = new_f, new_g
        return (f[k] + g[k]) % MOD


# golang solution

'''
// 方法一：组合数学 O(k) 时间 O(1) 空间
func numberOfSets(n int, k int) int {
	const mod = 1000000007
	total := n + k - 1
	m := 2 * k
	if m > total {
		return 0
	}

	num, den := 1, 1
	for i := 1; i <= m; i++ {
		num = (num * (total - i + 1)) % mod
		den = (den * i) % mod
	}

	powMod := func(base, exp int) int {
		res := 1
		base %= mod
		for exp > 0 {
			if exp%2 == 1 {
				res = (res * base) % mod
			}
			base = (base * base) % mod
			exp /= 2
		}
		return res
	}

	return (num * powMod(den, mod-2)) % mod
}

// 方法二：动态规划 O(n*k) 时间 O(k) 空间
func numberOfSetsDP(n int, k int) int {
	const mod = 1000000007
	f := make([]int, k+1)
	g := make([]int, k+1)
	f[0] = 1
	for i := 1; i < n; i++ {
		newF := make([]int, k+1)
		newG := make([]int, k+1)
		for j := 0; j <= k; j++ {
			newF[j] = (f[j] + g[j]) % mod
			newG[j] = g[j]
			if j > 0 {
				newG[j] = (newG[j] + f[j-1] + g[j-1]) % mod
			}
		}
		f, g = newF, newG
	}
	return (f[k] + g[k]) % mod
}
'''

# solutions

'''
思路和算法：

方法一：组合数学（隔板法与等价变换）
1. 问题转化：
   我们需要在 0 到 n-1 这 n 个点上选取 k 条线段 (l_1, r_1), (l_2, r_2), ..., (l_k, r_k)。
   满足以下限制条件：
   - 0 <= l_1 < r_1 <= l_2 < r_2 <= ... <= l_k < r_k <= n - 1
   注意：相邻线段端点可以重合，即 r_i <= l_{i+1}；但每条线段至少覆盖两个点，即 l_i < r_i。

2. 将非严格递增转为严格递增（变量代换）：
   观察到严格不等式和非严格不等式交替出现：
   l_1 < r_1 <= l_2 < r_2 <= l_3 < r_3 <= ... <= l_k < r_k
   
   我们引入新的变量 y_1, y_2, ..., y_{2k}：
   对于第 i 条线段（1 <= i <= k）：
   - 令 y_{2i-1} = l_i + (i - 1)
   - 令 y_{2i}   = r_i + (i - 1)
   
   检查各变量间的大小关系：
   - 同一线段内部：y_{2i-1} < y_{2i} 等价于 l_i + (i - 1) < r_i + (i - 1) <=> l_i < r_i（恒成立）
   - 相邻线段之间：y_{2i} < y_{2i+1} 等价于 r_i + (i - 1) < l_{i+1} + i <=> r_i <= l_{i+1}（恒成立）
   
   取值范围：
   - 最小值为 y_1 = l_1 >= 0
   - 最大值为 y_{2k} = r_k + (k - 1) <= (n - 1) + (k - 1) = n + k - 2
   
   也就是说，0 <= y_1 < y_2 < ... < y_{2k} <= n + k - 2。
   这等价于：在集合 {0, 1, 2, ..., n + k - 2} 这 n + k - 1 个连续整数中，选取 2k 个互不相同的数！
   每个选法与原问题的一种合法线段组合一一对应。
   
   因此，总方案数恰好为组合数：
   C(n + k - 1, 2k) % (10^9 + 7)

复杂度分析：
- 时间复杂度：O(k)，计算 C(n + k - 1, 2k) 仅需相乘 2k 项并通过费马小定理求逆元（或 Python math.comb 底层高精度快速乘法）。
- 空间复杂度：O(1)，仅需常数级别的额外空间。

---

方法二：动态规划（前缀状态转移）
1. 状态定义：
   设点为 0, 1, ..., n-1。考虑遍历前 i 个点（0 到 i）：
   - f[j]：使用前 i 个点已经构成了 j 条完整的线段，且第 j 条线段未延伸到点 i（点 i 处于空闲状态）。
   - g[j]：使用前 i 个点构成了 j 条线段，且第 j 条线段正在延伸（点 i 是某条线段的内部点或当前确定的端点）。

2. 状态转移：
   遍历到点 i 时，由前一个点 i-1 转移：
   - 对于 f[j]：
     点 i 没有线段延伸，则前一点可以是结束状态（f[j]），也可以是刚在 i-1 结束了某条线段（g[j]）：
     new_f[j] = f[j] + g[j]
   - 对于 g[j]：
     点 i 处于线段内部/端点，有两种来源：
     1. 从 i-1 继续延伸第 j 条线段：g[j]
     2. 在 i-1 开辟第 j 条新线段（前一点可以是 f[j-1] 或 g[j-1]，因为允许端点重合）：f[j-1] + g[j-1]
     new_g[j] = g[j] + f[j-1] + g[j-1]

3. 初始条件与答案：
   - 初始时 f[0] = 1，其余为 0。
   - 遍历完 n 个点后，答案为 (f[k] + g[k]) % (10^9 + 7)。

复杂度分析：
- 时间复杂度：O(n * k)，两重循环，外层 n-1 次，内层 k 次。
- 空间复杂度：O(k)，使用滚动数组优化空间。
'''

