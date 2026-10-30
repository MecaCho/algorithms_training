# encoding=utf8

'''
3970. Shortest Path With At Most K Consecutive Identical Characters
You are given an integer n representing the number of nodes in a directed weighted graph, numbered from 0 to n - 1. This is represented by a 2D integer array edges, where edges[i] = [ui, vi, wi] represents a directed edge from node ui to node vi with weight wi.

You are also given a string labels of length n, where labels[i] is the character assigned to node i, and an integer k.

Return the minimum total edge weight of a path from node 0 to node n - 1 such that the concatenation of the labels of the nodes along the path contains at most k consecutive identical characters. If no valid path exists, return -1.

 

Example 1:

Input: n = 3, edges = [[0,1,1],[1,2,1],[0,2,3]], labels = "aab", k = 1
Output: 3
Explanation:
The optimal valid path from node 0 to node 2 is as follows:
- Use edges[2] = [0, 2, 3] to reach node 2 with a weight wi = 3.
The corresponding concatenation of labels is "ab", which satisfies at most k = 1 consecutive identical characters. Thus, the answer is 3.

Example 2:

Input: n = 3, edges = [[0,1,1],[1,2,1],[0,2,3]], labels = "aab", k = 2
Output: 2
Explanation:
The optimal valid path from node 0 to node 2 is as follows:
- Use edges[0] = [0, 1, 1] to reach node 1 with weight wi = 1.
- Use edges[1] = [1, 2, 1] to reach node 2 with weight wi = 1.
The corresponding concatenation of labels is "aab", which satisfies at most k = 2 consecutive identical characters. Thus, the answer is 2.

Example 3:

Input: n = 3, edges = [[0,1,1],[1,2,1]], labels = "aaa", k = 2
Output: -1
Explanation:
There is no valid path from node 0 to node 2 that satisfies at most k = 2 consecutive identical characters. Thus, the answer is -1.

 

Constraints:

1 <= n == labels.length <= 5 * 10^4
0 <= edges.length <= 5 * 10^4
edges[i] == [ui, vi, wi]
0 <= ui, vi <= n - 1
ui != vi
1 <= wi <= 10^4
labels consists of lowercase English letters
1 <= k <= 50


3970. 最多 K 个连续相同字符的最短路径
给你一个整数 n，表示一个 有向加权 图中的节点数量，节点编号从 0 到 n - 1。该图由二维数组 edges 表示，其中 edges[i] = [ui, vi, wi] 表示一条从节点 ui 指向节点 vi、权重为 wi 的有向边。

另给定一个长度为 n 的字符串 labels，其中 labels[i] 是分配给节点 i 的字符，以及一个整数 k。

返回一条从节点 0 到节点 n - 1 的路径的 最小总边权 ，并要求该路径上所有节点标签按顺序 拼接 后，最多包含 k 个 连续相同 字符。如果不存在有效路径，返回 -1。

 

示例 1：

输入： n = 3, edges = [[0,1,1],[1,2,1],[0,2,3]], labels = "aab", k = 1
输出： 3
解释：
从节点 0 到节点 2 的最优有效路径如下：
- 使用 edges[2] = [0, 2, 3] 到达节点 2，边权 wi = 3。
对应的标签拼接结果为 "ab"，满足最多有 k = 1 个连续相同字符。因此答案为 3。

示例 2：

输入： n = 3, edges = [[0,1,1],[1,2,1],[0,2,3]], labels = "aab", k = 2
输出： 2
解释：
从节点 0 到节点 2 的最优有效路径如下：
- 使用 edges[0] = [0, 1, 1] 到达节点 1，边权 wi = 1。
- 使用 edges[1] = [1, 2, 1] 到达节点 2，边权 wi = 1。
对应的标签拼接结果为 "aab"，满足最多有 k = 2 个连续相同字符。因此答案为 2。

示例 3：

输入： n = 3, edges = [[0,1,1],[1,2,1]], labels = "aaa", k = 2
输出： -1
解释：
不存在从节点 0 到节点 2 的有效路径，使其满足最多有 k = 2 个连续相同字符。因此答案为 -1。

 

提示：

1 <= n == labels.length <= 5 * 10^4
0 <= edges.length <= 5 * 10^4
edges[i] == [ui, vi, wi]
0 <= ui, vi <= n - 1
ui != vi
1 <= wi <= 10^4
labels 由小写英文字母组成
1 <= k <= 50
'''


class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        g = [[] for _ in range(n)]
        for u, v, w in edges:
            g[u].append((v, w))

        # dist[u][c] 表示到达节点 u 且当前路径结尾连续相同字符数为 c 时的最小边权和
        dist = [[math.inf] * (k + 1) for _ in range(n)]
        dist[0][1] = 0

        # 优先队列元素为三元组：(当前总距离, 节点编号 u, 结尾连续相同字符数 c)
        pq = [(0, 0, 1)]

        while pq:
            d, u, cur = heappop(pq)
            if u == n - 1:
                return d
            if d > dist[u][cur]:
                continue

            for v, w in g[u]:
                nxt = cur + 1 if labels[v] == labels[u] else 1
                nd = d + w
                if nxt <= k and nd < dist[v][nxt]:
                    dist[v][nxt] = nd
                    heappush(pq, (nd, v, nxt))

        return -1


# golang solution

'''
import (
	"container/heap"
)

type tuple struct {
	d, u, cur int
}

type hp []tuple

func (h hp) Len() int           { return len(h) }
func (h hp) Less(i, j int) bool { return h[i].d < h[j].d }
func (h hp) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }
func (h *hp) Push(v any)        { *h = append(*h, v.(tuple)) }
func (h *hp) Pop() any {
	a := *h
	v := a[len(a)-1]
	*h = a[:len(a)-1]
	return v
}

func shortestPath(n int, edges [][]int, labels string, k int) int {
	type edge struct {
		to, w int
	}

	g := make([][]edge, n)
	for _, e := range edges {
		u, v, w := e[0], e[1], e[2]
		g[u] = append(g[u], edge{v, w})
	}

	const inf = int(1e18)
	dist := make([][]int, n)
	for i := range dist {
		dist[i] = make([]int, k+1)
		for j := range dist[i] {
			dist[i][j] = inf
		}
	}

	dist[0][1] = 0
	pq := &hp{{d: 0, u: 0, cur: 1}}
	heap.Init(pq)

	for pq.Len() > 0 {
		top := heap.Pop(pq).(tuple)
		d, u, cur := top.d, top.u, top.cur

		if u == n-1 {
			return d
		}
		if d > dist[u][cur] {
			continue
		}

		for _, e := range g[u] {
			v, w := e.to, e.w
			nxt := 1
			if labels[v] == labels[u] {
				nxt = cur + 1
			}
			nd := d + w
			if nxt <= k && nd < dist[v][nxt] {
				dist[v][nxt] = nd
				heap.Push(pq, tuple{d: nd, u: v, cur: nxt})
			}
		}
	}

	return -1
}
'''

# solutions

'''
思路和算法：
1. 状态拆分与分层图建模（Dijkstra 最短路）：
   - 问题要求在有向非负权图中求从节点 0 到节点 n - 1 的最短路径。
   - 约束条件：整条路径上拼接的标签字符串中，最多包含 k 个连续相同字符。
   - 若直接在每个节点记录单一的最短路，由于后续能否走入相同标签的邻接点取决于“当前连续相同字符的长度”，局部较长（但不超限）的路径可能会限制后续扩展，反而是局部边权稍大但连续长度较小的路径能成功到达终点。
   - 因此，一个节点不能只用一个距离描述，必须将“到达当前节点时以该节点字符结尾的连续相同字符长度”纳入状态：
     * 状态定义为 (u, cur)，其中 u 表示当前节点编号（0 <= u < n），cur 表示路径末尾连续相同字符的计数（1 <= cur <= k）。
     * 数组 dist[u][cur] 记录从起点 (0, 1) 到达状态 (u, cur) 的最小总边权。

2. 状态转移规则：
   - 初始状态：从节点 0 出发，以 labels[0] 结尾的连续字符个数为 1，故 dist[0][1] = 0，其余状态初始化为无穷大。
   - 转移过程：对于当前出堆状态 (d, u, cur)，遍历 u 的所有出边 (v, w)：
     * 若 labels[v] == labels[u]，连续相同字符增加：nxt = cur + 1；
     * 若 labels[v] != labels[u]，连续相同字符重置：nxt = 1；
     * 合法性检查：若 nxt <= k 且 d + w < dist[v][nxt]，则更新 dist[v][nxt] = d + w 并将 (d + w, v, nxt) 压入小根堆。
   - 贪心终止：由于边权为非负整数，Dijkstra 算法保证第一次从堆顶弹出的节点为 n - 1 的状态对应的距离即为全局最优答案。若堆为空仍未到达节点 n - 1，则说明无解，返回 -1。

复杂度分析：
- 时间复杂度：O(k * (n + m) * log(n * k))，其中 n 是节点数，m 是边数（n, m <= 5 * 10^4），k <= 50。分层图中有效状态数为 n * k，有效边数为 m * k。使用小根堆优化后的 Dijkstra 复杂度为 O(|E| log |V|)，在限制内完全可以在数百毫秒内高效运行。
- 空间复杂度：O(n * k + m)，邻接表占用 O(n + m) 空间，dist 数组和优先队列至多占用 O(n * k) 空间。
'''

