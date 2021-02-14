# encoding=utf8

'''
765. Couples Holding Hands
N couples sit in 2N seats arranged in a row and want to hold hands. We want to know the minimum number of swaps so that every couple is sitting side by side. A swap consists of choosing any two people, then they stand up and switch seats.

The people and seats are represented by an integer from 0 to 2N-1, the couples are numbered in order, the first couple being (0, 1), the second couple being (2, 3), and so on with the last couple being (2N-2, 2N-1).

The couples' initial seating is given by row[i] being the value of the person who is initially sitting in the i-th seat.

Example 1:

Input: row = [0, 2, 1, 3]
Output: 1
Explanation: We only need to swap the second (row[1]) and third (row[2]) person.
Example 2:

Input: row = [3, 2, 0, 1]
Output: 0
Explanation: All couples are already seated side by side.
Note:

len(row) is even and in the range of [4, 60].
row is guaranteed to be a permutation of 0...len(row)-1.


765. 情侣牵手
N 对情侣坐在连续排列的 2N 个座位上，想要牵到对方的手。 计算最少交换座位的次数，以便每对情侣可以并肩坐在一起。 一次交换可选择任意两人，让他们站起来交换座位。

人和座位用 0 到 2N-1 的整数表示，情侣们按顺序编号，第一对是 (0, 1)，第二对是 (2, 3)，以此类推，最后一对是 (2N-2, 2N-1)。

这些情侣的初始座位  row[i] 是由最初始坐在第 i 个座位上的人决定的。

示例 1:

输入: row = [0, 2, 1, 3]
输出: 1
解释: 我们只需要交换row[1]和row[2]的位置即可。
示例 2:

输入: row = [3, 2, 0, 1]
输出: 0
解释: 无需交换座位，所有的情侣都已经可以手牵手了。
说明:

len(row) 是偶数且数值在 [4, 60]范围内。
可以保证row 是序列 0...len(row)-1 的一个全排列。
'''


class Solution(object):
    def minSwapsCouples(self, row):
        """
        :type row: List[int]
        :rtype: int
        """
        res = 0

        for i in range(0, len(row), 2):
            p1 = row[i]
            p2 = p1 + 1 if p1 % 2 == 0 else p1 - 1
            if row[i + 1] != p2:
                j = row.index(p2)
                row[i + 1], row[j] = row[j], row[i + 1]
                res += 1

        return res


# solutions

'''
方法一：并查集
假定第一对情侣的男生与第二对情侣的女生坐在了一起，而第二对情侣的男生与第三对情侣的女生坐在了一起。根据题意，要想让第二对情侣之间能够成功牵手，要么交换第一对情侣的男生与第二对情侣的男生，要么交换第二对情侣的女生与第三对情侣的女生。

既然存在这两种交换方式，那么有必要两种方式都考虑吗？答案是无需都考虑。不难注意到，无论采用了两种交换方式中的哪一种，最后的结局都是「第二对情侣坐在了一起，且第一对情侣的男生与第三对情侣的女生坐在了一起」，因此两种交换方式是等价的。

因此，我们将 NN 对情侣看做图中的 NN 个节点；对于每对相邻的位置，如果是第 ii 对与第 jj 对坐在了一起，则在 ii 号节点与 jj 号节点之间连接一条边，代表需要交换这两对情侣的位置。

如果图中形成了一个大小为 kk 的环：i \rightarrow j \rightarrow k \rightarrow \ldots \rightarrow l \rightarrow ii→j→k→…→l→i，则我们沿着环的方向，先交换 i,ji,j 的位置，再交换 j,kj,k 的位置，以此类推。在进行了 k-1k−1 次交换后，这 kk 对情侣就都能够彼此牵手了。

故我们只需要利用并查集求出图中的每个连通分量；对于每个连通分量而言，其大小减 11 就是需要交换的次数。

C++JavaGolangCJavaScript

type unionFind struct {
    parent, size []int
    setCount     int // 当前连通分量数目
}

func newUnionFind(n int) *unionFind {
    parent := make([]int, n)
    size := make([]int, n)
    for i := range parent {
        parent[i] = i
        size[i] = 1
    }
    return &unionFind{parent, size, n}
}

func (uf *unionFind) find(x int) int {
    if uf.parent[x] != x {
        uf.parent[x] = uf.find(uf.parent[x])
    }
    return uf.parent[x]
}

func (uf *unionFind) union(x, y int) {
    fx, fy := uf.find(x), uf.find(y)
    if fx == fy {
        return
    }
    if uf.size[fx] < uf.size[fy] {
        fx, fy = fy, fx
    }
    uf.size[fx] += uf.size[fy]
    uf.parent[fy] = fx
    uf.setCount--
}

func minSwapsCouples(row []int) int {
    n := len(row)
    uf := newUnionFind(n / 2)
    for i := 0; i < n; i += 2 {
        uf.union(row[i]/2, row[i+1]/2)
    }
    return n/2 - uf.setCount
}
复杂度分析

时间复杂度：O(N \log N)O(NlogN)，其中 NN 为情侣的总数。这里的并查集使用了路径压缩，但是没有使用按秩合并，最坏情况下的时间复杂度是 O(N \log N)O(NlogN)，平均情况下的时间复杂度依然是 O(N \alpha (N))O(Nα(N))，其中 \alphaα 为阿克曼函数的反函数，\alpha (N)α(N) 可以认为是一个很小的常数。

空间复杂度：O(N)O(N)。

方法二：广度优先搜索
我们也可以通过广度优先搜索的方式，求解图中的连通分量。

起初，我们将每个节点都标记为「未访问」，并遍历图中的每个节点。如果发现一个「未访问」的节点，就从该节点出发，沿着图中的边，将其余的「未访问」的节点都标记为「已访问」，并同时统计标记的次数。当遍历过程终止时，标记的数量次数即为连通分量的大小。

C++JavaGolangCJavaScript

func minSwapsCouples(row []int) (ans int) {
    n := len(row)
    graph := make([][]int, n/2)
    for i := 0; i < n; i += 2 {
        l, r := row[i]/2, row[i+1]/2
        if l != r {
            graph[l] = append(graph[l], r)
            graph[r] = append(graph[r], l)
        }
    }
    vis := make([]bool, n/2)
    for i, vs := range vis {
        if !vs {
            vis[i] = true
            cnt := 0
            q := []int{i}
            for len(q) > 0 {
                cnt++
                v := q[0]
                q = q[1:]
                for _, w := range graph[v] {
                    if !vis[w] {
                        vis[w] = true
                        q = append(q, w)
                    }
                }
            }
            ans += cnt - 1
        }
    }
    return
}
复杂度分析

时间复杂度：O(N)O(N)，其中 NN 为情侣的总数。每个节点最多只被标记 11 次。

空间复杂度：O(N)O(N)，其中 NN 为情侣的总数。为队列的开销。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/couples-holding-hands/solution/qing-lu-qian-shou-by-leetcode-solution-bvzr/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
