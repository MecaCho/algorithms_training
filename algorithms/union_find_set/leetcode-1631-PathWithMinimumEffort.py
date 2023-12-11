# encoding=utf8


'''
1631. Path With Minimum Effort
You are a hiker preparing for an upcoming hike. You are given heights, a 2D array of size rows x columns, where heights[row][col] represents the height of cell (row, col). You are situated in the top-left cell, (0, 0), and you hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e., 0-indexed). You can move up, down, left, or right, and you wish to find a route that requires the minimum effort.

A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.

Return the minimum effort required to travel from the top-left cell to the bottom-right cell.



Example 1:



Input: heights = [[1,2,2],[3,8,2],[5,3,5]]
Output: 2
Explanation: The route of [1,3,5,3,5] has a maximum absolute difference of 2 in consecutive cells.
This is better than the route of [1,2,2,2,5], where the maximum absolute difference is 3.
Example 2:



Input: heights = [[1,2,3],[3,8,4],[5,3,5]]
Output: 1
Explanation: The route of [1,2,3,4,5] has a maximum absolute difference of 1 in consecutive cells, which is better than route [1,3,5,3,5].
Example 3:


Input: heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
Output: 0
Explanation: This route does not require any effort.


Constraints:

rows == heights.length
columns == heights[i].length
1 <= rows, columns <= 100
1 <= heights[i][j] <= 106


1631. 最小体力消耗路径
你准备参加一场远足活动。给你一个二维 rows x columns 的地图 heights ，其中 heights[row][col] 表示格子 (row, col) 的高度。
一开始你在最左上角的格子 (0, 0) ，且你希望去最右下角的格子 (rows-1, columns-1) （注意下标从 0 开始编号）。
你每次可以往 上，下，左，右 四个方向之一移动，你想要找到耗费 体力 最小的一条路径。

一条路径耗费的 体力值 是路径上相邻格子之间 高度差绝对值 的 最大值 决定的。

请你返回从左上角走到右下角的最小 体力消耗值 。



示例 1：



输入：heights = [[1,2,2],[3,8,2],[5,3,5]]
输出：2
解释：路径 [1,3,5,3,5] 连续格子的差值绝对值最大为 2 。
这条路径比路径 [1,2,2,2,5] 更优，因为另一条路径差值最大值为 3 。
示例 2：



输入：heights = [[1,2,3],[3,8,4],[5,3,5]]
输出：1
解释：路径 [1,2,3,4,5] 的相邻格子差值绝对值最大为 1 ，比路径 [1,3,5,3,5] 更优。
示例 3：


输入：heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
输出：0
解释：上图所示路径不需要消耗任何体力。


提示：

rows == heights.length
columns == heights[i].length
1 <= rows, columns <= 100
1 <= heights[i][j] <= 106



'''

# solutions


'''
前言
我们可以将本题抽象成如下的一个图论模型：

我们将地图中的每一个格子看成图中的一个节点；

我么将两个相邻（左右相邻或者上下相邻）的两个格子对应的节点之间连接一条无向边，边的权值为这两个格子的高度差的绝对值；

我们需要找到一条从左上角到右下角的最短路径，其中一条路径的长度定义为其经过的所有边权的最大值。

由于地图是二维的，我们需要给每个格子对应的节点赋予一个唯一的节点编号。如果地图的行数为 mm，列数为 nn，那么位置为 (i, j)(i,j) 的格子对应的编号为 i \times n + ji×n+j，这样 ,mn,mn 个格子的编号一一对应着 [0, mn)[0,mn) 范围内的所有整数。当然，如果读者使用的语言支持对二元组进行哈希计算、作为下标访问等，则不需要这一步操作。

本篇题解中会介绍三种不同的解决方法。

方法一：二分查找
思路与算法

我们可以将这个问题转化成一个「判定性」问题，即：

是否存在一条从左上角到右下角的路径，其经过的所有边权的最大值不超过 xx？

这个判定性问题解决起来并不复杂，我们只要从左上角开始进行深度优先搜索或者广度优先搜索，在搜索的过程中只允许经过边权不超过 xx 的边，搜索结束后判断是否能到达右下角即可。

随着 xx 的增大，原先可以经过的边仍然会被保留，因此如果当 x=x_0x=x
0
​
  时，我们可以从左上角到达右下角，那么当 x > x_0x>x
0
​
  时同样也可以可行的。因此我们可以使用二分查找的方法，找出满足要求的最小的那个 xx 值，记为 x_\textit{ans}x
ans
​
 ，那么：

当 x < x_\textit{ans}x<x
ans
​
 ，我们无法从左上角到达右下角；

当 x \geq x_\textit{ans}x≥x
ans
​
 ，我们可以从左上角到达右下角。

由于格子的高度范围为 [1, 10^6][1,10
6
 ]，因此我们可以 [0, 10^6-1][0,10
6
 −1] 的范围内对 xx 进行二分查找。在每一步查找的过程中，我们使用进行深度优先搜索或者广度优先搜索判断是否可以从左上角到达右下角，并根据判定结果更新二分查找的左边界或右边界即可。

代码

下面的代码中使用的是广度优先搜索。

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        left, right, ans = 0, 10**6 - 1, 0

        while left <= right:
            mid = (left + right) // 2
            q = collections.deque([(0, 0)])
            seen = {(0, 0)}

            while q:
                x, y = q.popleft()
                for nx, ny in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                    if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in seen and abs(heights[x][y] - heights[nx][ny]) <= mid:
                        q.append((nx, ny))
                        seen.add((nx, ny))

            if (m - 1, n - 1) in seen:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans
        
复杂度分析

时间复杂度：O(mn \log C)O(mnlogC)，其中 mm 和 nn 分别是地图的行数和列数，CC 是格子的最大高度，在本题中 CC 不超过 10^6106。我们需要进行 O(\log C)O(logC) 次二分查找，每一步查找的过程中需要使用广度优先搜索，在 O(mn)O(mn) 的时间判断是否可以从左上角到达右下角，因此总时间复杂度为 O(mn \log C)O(mnlogC)。

空间复杂度：O(mn)O(mn)，即为广度优先搜索中使用的队列需要的空间。

方法二：并查集
思路与算法

我们将这 mnmn 个节点放入并查集中，实时维护它们的连通性。

由于我们需要找到从左上角到右下角的最短路径，因此我们可以将图中的所有边按照权值从小到大进行排序，并依次加入并查集中。
当我们加入一条权值为 xx 的边之后，如果左上角和右下角从非连通状态变为连通状态，那么 xx 即为答案。

代码


# 并查集模板
class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.size = [1] * n
        self.n = n
        # 当前连通分量数目
        self.setCount = n

    def findset(self, x: int) -> int:
        if self.parent[x] == x:
            return x
        self.parent[x] = self.findset(self.parent[x])
        return self.parent[x]

    def unite(self, x: int, y: int) -> bool:
        x, y = self.findset(x), self.findset(y)
        if x == y:
            return False
        if self.size[x] < self.size[y]:
            x, y = y, x
        self.parent[y] = x
        self.size[x] += self.size[y]
        self.setCount -= 1
        return True

    def connected(self, x: int, y: int) -> bool:
        x, y = self.findset(x), self.findset(y)
        return x == y

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        edges = list()
        for i in range(m):
            for j in range(n):
                iden = i * n + j
                if i > 0:
                    edges.append((iden - n, iden, abs(heights[i][j] - heights[i - 1][j])))
                if j > 0:
                    edges.append((iden - 1, iden, abs(heights[i][j] - heights[i][j - 1])))

        edges.sort(key=lambda e: e[2])

        uf = UnionFind(m * n)
        ans = 0
        for x, y, v in edges:
            uf.unite(x, y)
            if uf.connected(0, m * n - 1):
                ans = v
                break

        return ans
复杂度分析

时间复杂度：O(mn \log(mn))O(mnlog(mn))，其中 mm 和 nn 分别是地图的行数和列数。
图中的边数为 O(mn)O(mn)，因此排序的时间复杂度为 O(mn \log (mn))O(mnlog(mn))。
并查集的时间复杂度为 O(mn \cdot \alpha(mn))O(mn⋅α(mn))，其中 \alphaα 为阿克曼函数的反函数。
由于后者在渐进意义下小于前者，因此总时间复杂度为 O(mn \log(mn))O(mnlog(mn))。

空间复杂度：O(mn)O(mn)，即为存储所有边以及并查集需要的空间。

方法三：最短路
思路与算法

「最短路径」使得我们很容易想到求解最短路径的 \texttt{Dijkstra}Dijkstra 算法，然而本题中对于「最短路径」的定义不是其经过的所有边权的和，而是其经过的所有边权的最大值，那么我们还可以用 \texttt{Dijkstra}Dijkstra 算法进行求解吗？

答案是可以的。\texttt{Dijkstra}Dijkstra 算法本质上是一种启发式搜索算法，它是 \texttt{A*}A* 算法在启发函数 h \equiv 0h≡0 时的特殊情况。读者可以参考 A* search algorithm，Consistent heuristic，Admissible heuristic 深入了解 \texttt{Dijkstra}Dijkstra 算法的本质。

下面给出 \texttt{Dijkstra}Dijkstra 算法的可行性证明，需要读者对 \texttt{A*}A* 算法以及其可行性条件有一定的掌握。

证明

定义加法运算 a \oplus b = \max (a,b)a⊕b=max(a,b)，显然 \oplus⊕ 满足交换律和结合律。那么如果一条路径上的边权分别为 e_0, e_1, \cdots, e_ke
0
​
 ,e
1
​
 ,⋯,e
k
​
 ，那么 e_0 \oplus e_1 \oplus \cdots \oplus e_ke
0
​
 ⊕e
1
​
 ⊕⋯⊕e
k
​
  即为这条路径的长度。

在 \texttt{Dijkstra}Dijkstra 算法中 h \equiv 0h≡0，对于图中任意的无向边 x \leftrightarrow yx↔y，由于 e_{x, y} \geq 0e
x,y
​
 ≥0，那么 h(x)=0\leq e_{x,y} \oplus h(y)h(x)=0≤e
x,y
​
 ⊕h(y) 恒成立，其中 e_{x, y}e
x,y
​
  表示边权。因此启发函数 hh 和加法运算 \oplus⊕ 满足三角不等式，是 consistent heuristic 的，可以使用 \texttt{Dijkstra}Dijkstra 算法求出最短路径。

代码

C++JavaPython3Golang

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        q = [(0, 0, 0)]
        dist = [0] + [float("inf")] * (m * n - 1)
        seen = set()

        while q:
            d, x, y = heapq.heappop(q)
            iden = x * n + y
            if iden in seen:
                continue
            if (x, y) == (m - 1, n - 1):
                break

            seen.add(iden)
            for nx, ny in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if 0 <= nx < m and 0 <= ny < n and max(d, abs(heights[x][y] - heights[nx][ny])) <= dist[nx * n + ny]:
                    dist[nx * n + ny] = max(d, abs(heights[x][y] - heights[nx][ny]))
                    heapq.heappush(q, (dist[nx * n + ny], nx, ny))

        return dist[m * n - 1]
复杂度分析

时间复杂度：O(mn \log(mn))O(mnlog(mn))，其中 mm 和 nn 分别是地图的行数和列数。对于节点数为 n_0n
0
​
 ，边数为 m_0m
0
​
  的图，使用优先队列优化的 \texttt{Dijkstra}Dijkstra 算法的时间复杂度为 O(m_0 \log m_0)O(m
0
​
 logm
0
​
 )。由于图中的边数为 O(mn)O(mn)，带入即可得到时间复杂度 O(mn \log(mn))O(mnlog(mn))。

空间复杂度：O(mn)O(mn)，即为 \texttt{Dijkstra}Dijkstra 算法需要使用的空间。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/path-with-minimum-effort/solution/zui-xiao-ti-li-xiao-hao-lu-jing-by-leetc-3q2j/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
