# encoding=utf8

'''
3841. Palindromic Path Queries in a Tree
You are given an undirected tree with n nodes labeled 0 to n - 1. This is represented by a 2D array edges of length n - 1, where edges[i] = [ui, vi] indicates an undirected edge between nodes ui and vi.

You are also given a string s of length n consisting of lowercase English letters, where s[i] represents the character assigned to node i.

You are also given a string array queries, where each queries[i] is either:

- "update ui c": Change the character at node ui to c. Formally, update s[ui] = c.
- "query ui vi": Determine whether the string formed by the characters on the unique path from ui to vi (inclusive) can be rearranged into a palindrome.

Return a boolean array answer, where answer[j] is true if the jth query of type "query ui vi" can be rearranged into a palindrome, and false otherwise.

 

Example 1:

Input: n = 3, edges = [[0,1],[1,2]], s = "aac", queries = ["query 0 2","update 1 b","query 0 2"]
Output: [true,false]
Explanation:
- "query 0 2": Path 0 → 1 → 2 gives "aac", which can be rearranged to form "aca", a palindrome. Thus, answer[0] = true.
- "update 1 b": Update node 1 to 'b', now s = "abc".
- "query 0 2": Path characters are "abc", which cannot be rearranged to form a palindrome. Thus, answer[1] = false.
Thus, answer = [true, false].

Example 2:

Input: n = 4, edges = [[0,1],[0,2],[0,3]], s = "abca", queries = ["query 1 2","update 0 b","query 2 3","update 3 a","query 1 3"]
Output: [false,false,true]
Explanation:
- "query 1 2": Path 1 → 0 → 2 gives "bac", which cannot be rearranged to form a palindrome. Thus, answer[0] = false.
- "update 0 b": Update node 0 to 'b', now s = "bbca".
- "query 2 3": Path 2 → 0 → 3 gives "cba", which cannot be rearranged to form a palindrome. Thus, answer[1] = false.
- "update 3 a": Update node 3 to 'a', s = "bbca".
- "query 1 3": Path 1 → 0 → 3 gives "bba", which can be rearranged to form "bab", a palindrome. Thus, answer[2] = true.
Thus, answer = [false, false, true].

 

Constraints:

1 <= n == s.length <= 5 * 10^4
edges.length == n - 1
edges[i] == [ui, vi]
0 <= ui, vi <= n - 1
s consists of lowercase English letters.
The input is generated such that edges represents a valid tree.
1 <= queries.length <= 5 * 10^4
queries[i] = "update ui c" or "query ui vi"
0 <= ui, vi <= n - 1
c is a lowercase English letter.


3841. 查询树上回文路径
给你一棵包含 n 个节点的无向树，节点编号从 0 到 n - 1。树由一个长度为 n - 1 的二维数组 edges 表示，其中 edges[i] = [ui, vi] 表示节点 ui 和 vi 之间存在一条无向边。

另给你一个长度为 n 且由小写英文字母组成的字符串 s，其中 s[i] 表示分配给节点 i 的字符。

还给你一个字符串数组 queries，其中每个 queries[i] 为以下形式之一：

- "update ui c"：将节点 ui 处的字符更改为 c。正式地，更新 s[ui] = c。
- "query ui vi"：判断从 ui 到 vi 的 唯一 路径（含两端点）上的字符所组成的字符串，是否可以 重新排列 成一个 回文串 。

返回一个布尔数组 answer，如果第 i 个类型为 "query ui vi" 的查询可以重新排列成 回文串 ，则 answer[i] 为 true，否则为 false。

回文串 是指正读和反读都相同的字符串。

 

示例 1：

输入： n = 3, edges = [[0,1],[1,2]], s = "aac", queries = ["query 0 2","update 1 b","query 0 2"]
输出： [true,false]
解释：
- "query 0 2"：路径 0 → 1 → 2 得到的字符串是 "aac"，可以重新排列形成 "aca"，这是一个回文串。因此，answer[0] = true。
- "update 1 b"：将节点 1 更新为 'b'，现在 s = "abc"。
- "query 0 2"：路径上的字符为 "abc"，无法重新排列形成回文串。因此，answer[1] = false。
因此，answer = [true, false]。

示例 2：

输入： n = 4, edges = [[0,1],[0,2],[0,3]], s = "abca", queries = ["query 1 2","update 0 b","query 2 3","update 3 a","query 1 3"]
输出： [false,false,true]
解释：
- "query 1 2"：路径 1 → 0 → 2 得到的字符串是 "bac"，无法重新排列形成回文串。因此，answer[0] = false。
- "update 0 b"：将节点 0 更新为 'b'，现在 s = "bbca"。
- "query 2 3"：路径 2 → 0 → 3 得到的字符串是 "cba"，无法重新排列形成回文串。因此，answer[1] = false。
- "update 3 a"：将节点 3 更新为 'a'，s = "bbca"。
- "query 1 3"：路径 1 → 0 → 3 得到的字符串是 "bba"，可以重新排列形成 "bab"，这是一个回文串。因此，answer[2] = true。
因此，answer = [false, false, true]。

 

提示：

1 <= n == s.length <= 5 * 10^4
edges.length == n - 1
edges[i] == [ui, vi]
0 <= ui, vi <= n - 1
s 由小写英文字母组成。
输入生成的 edges 表示一棵有效的树。
1 <= queries.length <= 5 * 10^4
queries[i] = "update ui c" 或 "query ui vi"
0 <= ui, vi <= n - 1
c 是一个小写英文字母。
'''


class FenwickTree:
    """基于按位异或的树状数组（Binary Indexed Tree）"""

    def __init__(self, size: int):
        self.n = size
        self.tree = [0] * (size + 1)

    def update(self, i: int, val: int) -> None:
        while i <= self.n:
            self.tree[i] ^= val
            i += i & -i

    def query(self, i: int) -> int:
        res = 0
        while i > 0:
            res ^= self.tree[i]
            i -= i & -i
        return res


class Solution:
    def palindromePath(
        self, n: int, edges: List[List[int]], s: str, queries: List[str]
    ) -> List[bool]:
        # 1. 建图
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        parent = [0] * n
        depth = [0] * n
        tin = [0] * n
        tout = [0] * n

        # 2. BFS 预处理父节点与深度，避免递归深度过大
        q = [0]
        visited = [False] * n
        visited[0] = True
        head = 0
        while head < len(q):
            u = q[head]
            head += 1
            for v in g[u]:
                if not visited[v]:
                    visited[v] = True
                    parent[v] = u
                    depth[v] = depth[u] + 1
                    q.append(v)

        # 3. 显式栈迭代 DFS 计算子树欧拉序区间 [tin[u], tout[u]]
        stack = [0]
        edge_idx = [0] * n
        timer = 1
        tin[0] = timer

        while stack:
            u = stack[-1]
            if edge_idx[u] < len(g[u]):
                v = g[u][edge_idx[u]]
                edge_idx[u] += 1
                if v != parent[u]:
                    timer += 1
                    tin[v] = timer
                    stack.append(v)
            else:
                tout[u] = timer
                stack.pop()

        # 4. 倍增法（Binary Lifting）预处理 LCA 表
        m = n.bit_length()
        up = [parent[:]]
        for j in range(1, m):
            prev = up[-1]
            up.append([prev[prev[i]] for i in range(n)])

        def lca(u: int, v: int) -> int:
            if depth[u] < depth[v]:
                u, v = v, u
            d = depth[u] - depth[v]
            j = 0
            while d:
                if d & 1:
                    u = up[j][u]
                d >>= 1
                j += 1
            if u == v:
                return u
            for j in range(m - 1, -1, -1):
                if up[j][u] != up[j][v]:
                    u = up[j][u]
                    v = up[j][v]
            return up[0][u]

        # 5. 树状数组维护每个节点到根路径字符异或掩码（差分区间异或）
        node_mask = [1 << (ord(c) - ord("a")) for c in s]
        ft = FenwickTree(n + 2)
        for u in range(n):
            ft.update(tin[u], node_mask[u])
            ft.update(tout[u] + 1, node_mask[u])

        # 6. 处理查询与更新
        ans = []
        for q_str in queries:
            parts = q_str.split()
            if parts[0] == "update":
                u = int(parts[1])
                new_mask = 1 << (ord(parts[2]) - ord("a"))
                if new_mask != node_mask[u]:
                    delta = node_mask[u] ^ new_mask
                    ft.update(tin[u], delta)
                    ft.update(tout[u] + 1, delta)
                    node_mask[u] = new_mask
            else:
                u = int(parts[1])
                v = int(parts[2])
                w = lca(u, v)
                # 路径字符掩码 = pref[u] ^ pref[v] ^ node_mask[w]
                mask = ft.query(tin[u]) ^ ft.query(tin[v]) ^ node_mask[w]
                # 回文充要条件：出现奇数次的字符最多 1 个，即二进制掩码中 1 的个数 <= 1
                ans.append((mask & (mask - 1)) == 0)

        return ans


# golang solution

'''
type fenwickTree struct {
	n    int
	tree []int
}

func newFenwickTree(n int) *fenwickTree {
	return &fenwickTree{
		n:    n,
		tree: make([]int, n+1),
	}
}

func (ft *fenwickTree) update(i, val int) {
	for i <= ft.n {
		ft.tree[i] ^= val
		i += i & -i
	}
}

func (ft *fenwickTree) query(i int) int {
	res := 0
	for i > 0 {
		res ^= ft.tree[i]
		i -= i & -i
	}
	return res
}

func palindromePath(n int, edges [][]int, s string, queries []string) []bool {
	g := make([][]int, n)
	for _, e := range edges {
		u, v := e[0], e[1]
		g[u] = append(g[u], v)
		g[v] = append(g[v], u)
	}

	parent := make([]int, n)
	depth := make([]int, n)
	tin := make([]int, n)
	tout := make([]int, n)

	// BFS 处理 parent 和 depth
	q := []int{0}
	visited := make([]bool, n)
	visited[0] = true
	head := 0
	for head < len(q) {
		u := q[head]
		head++
		for _, v := range g[u] {
			if !visited[v] {
				visited[v] = true
				parent[v] = u
				depth[v] = depth[u] + 1
				q = append(q, v)
			}
		}
	}

	// 迭代 DFS 记录欧拉序入出时间戳
	stack := []int{0}
	edgeIdx := make([]int, n)
	timer := 1
	tin[0] = timer

	for len(stack) > 0 {
		u := stack[len(stack)-1]
		if edgeIdx[u] < len(g[u]) {
			v := g[u][edgeIdx[u]]
			edgeIdx[u]++
			if v != parent[u] {
				timer++
				tin[v] = timer
				stack = append(stack, v)
			}
		} else {
			tout[u] = timer
			stack = stack[:len(stack)-1]
		}
	}

	// 倍增表 LCA
	m := 0
	for (1 << m) <= n {
		m++
	}
	up := make([][]int, m)
	up[0] = make([]int, n)
	copy(up[0], parent)
	for j := 1; j < m; j++ {
		up[j] = make([]int, n)
		for i := 0; i < n; i++ {
			up[j][i] = up[j-1][up[j-1][i]]
		}
	}

	lca := func(u, v int) int {
		if depth[u] < depth[v] {
			u, v = v, u
		}
		d := depth[u] - depth[v]
		for j := 0; d > 0; j++ {
			if d&1 == 1 {
				u = up[j][u]
			}
			d >>= 1
		}
		if u == v {
			return u
		}
		for j := m - 1; j >= 0; j-- {
			if up[j][u] != up[j][v] {
				u = up[j][u]
				v = up[j][v]
			}
		}
		return up[0][u]
	}

	nodeMask := make([]int, n)
	for i := 0; i < n; i++ {
		nodeMask[i] = 1 << int(s[i]-'a')
	}

	ft := newFenwickTree(n + 2)
	for u := 0; u < n; u++ {
		ft.update(tin[u], nodeMask[u])
		ft.update(tout[u]+1, nodeMask[u])
	}

	var ans []bool
	for _, qStr := range queries {
		parts := strings.Split(qStr, " ")
		if parts[0] == "update" {
			u, _ := strconv.Atoi(parts[1])
			newMask := 1 << int(parts[2][0]-'a')
			if newMask != nodeMask[u] {
				delta := nodeMask[u] ^ newMask
				ft.update(tin[u], delta)
				ft.update(tout[u]+1, delta)
				nodeMask[u] = newMask
			}
		} else {
			u, _ := strconv.Atoi(parts[1])
			v, _ := strconv.Atoi(parts[2])
			w := lca(u, v)
			mask := ft.query(tin[u]) ^ ft.query(tin[v]) ^ nodeMask[w]
			ans = append(ans, (mask&(mask-1)) == 0)
		}
	}

	return ans
}
'''

# solutions

'''
思路和算法：
1. 回文串判定的位运算建模：
   - 字符串中各个字符经过重新排列后能构成回文串的充要条件是：出现奇数次的字符个数至多为 1。
   - 由于只有 26 种小写英文字母，可以使用一个 26 位的二进制整数 mask 记录各字符出现次数的奇偶性：
     * 第 c 位为 1 表示字母 (chr(c + 'a')) 出现奇数次；为 0 表示偶数次。
   - 掩码中 1 的个数最多为 1 个，利用经典的消除最低位 1 的操作判定：(mask & (mask - 1)) == 0。

2. 树上路径前缀异或与最近公共祖先（LCA）：
   - 设 pref(x) 表示根节点到节点 x 的唯一简单路径上所有节点字符掩码的异或和。
   - 对于查询路径 u 到 v，设 w = LCA(u, v)：
     * 根节点到 parent[w] 的部分在 pref(u) 和 pref(v) 中均计算了 1 次，异或时恰好相互抵消；
     * 节点 w 在 pref(u) 和 pref(v) 中各包含了一次，故在 pref(u) ^ pref(v) 中被抵消；
     * 因此，u 到 v 路径上的实际字符掩码总和为：
       pathMask = pref(u) ^ pref(v) ^ node_mask[w]。

3. 动态更新与子树欧拉序（DFS 序 + 树状数组）：
   - 当节点 u 的字符发生改变（异或变量 delta = old_mask ^ new_mask）时：
     * 只有以 u 为根的整棵子树中的节点，其到根路径才包含节点 u；
     * 因此，更新节点 u 对应对 u 的子树内所有节点的 pref 值执行异或 delta 操作；
   - 利用树的 DFS 进入时间戳 tin[u] 与离开时间戳 tout[u]，以 u 为根的子树节点在 DFS 序上恰好构成一段连续闭区间 [tin[u], tout[u]]；
   - 对连续区间的异或增加，利用差分树状数组（Fenwick Tree）维护：
     * 区间修改 [tin[u], tout[u]] 异或 delta：在树状数组中 update(tin[u], delta) 与 update(tout[u] + 1, delta)；
     * 单点查询 pref(x)：直接查询前缀异或 query(tin[x])。

4. 复杂度与规模保障：
   - 树节点数 n <= 5 * 10^4，查询与更新总数 q <= 5 * 10^4；
   - DFS 序与倍增 LCA 表预处理时间为 O(n log n)；
   - 单次 update 操作：树状数组区间修改耗时 O(log n)；
   - 单次 query 操作：LCA 倍增查询 O(log n)，树状数组点查 O(log n)；
   - 采用迭代式 BFS/DFS 避免了极端退化链树下的系统递归栈溢出风险。

复杂度分析：
- 时间复杂度：O((n + q) log n)，其中 n 是树节点数，q 是查询与更新的总次数。倍增表预处理 O(n log n)，后续每次查询和修改均为 O(log n)。
- 空间复杂度：O(n log n)，主要为倍增 LCA 表 up 占用的空间，以及邻接表与树状数组占用的 O(n) 空间。
'''

