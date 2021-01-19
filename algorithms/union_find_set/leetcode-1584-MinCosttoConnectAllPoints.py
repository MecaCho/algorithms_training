# encoding=utf8

'''
1584. Min Cost to Connect All Points
You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.



Example 1:



Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
Output: 20
Explanation:

We can connect the points as shown above to get the minimum cost of 20.
Notice that there is a unique path between every pair of points.
Example 2:

Input: points = [[3,12],[-2,5],[-4,1]]
Output: 18
Example 3:

Input: points = [[0,0],[1,1],[1,0],[-1,1]]
Output: 4
Example 4:

Input: points = [[-1000000,-1000000],[1000000,1000000]]
Output: 4000000
Example 5:

Input: points = [[0,0]]
Output: 0


Constraints:

1 <= points.length <= 1000
-106 <= xi, yi <= 106
All pairs (xi, yi) are distinct.

1584. 连接所有点的最小费用
给你一个points 数组，表示 2D 平面上的一些点，其中 points[i] = [xi, yi] 。

连接点 [xi, yi] 和点 [xj, yj] 的费用为它们之间的 曼哈顿距离 ：|xi - xj| + |yi - yj| ，其中 |val| 表示 val 的绝对值。

请你返回将所有点连接的最小总费用。只有任意两点之间 有且仅有 一条简单路径时，才认为所有点都已连接。



示例 1：



输入：points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
输出：20
解释：

我们可以按照上图所示连接所有点得到最小总费用，总费用为 20 。
注意到任意两个点之间只有唯一一条路径互相到达。
示例 2：

输入：points = [[3,12],[-2,5],[-4,1]]
输出：18
示例 3：

输入：points = [[0,0],[1,1],[1,0],[-1,1]]
输出：4
示例 4：

输入：points = [[-1000000,-1000000],[1000000,1000000]]
输出：4000000
示例 5：

输入：points = [[0,0]]
输出：0


提示：

1 <= points.length <= 1000
-106 <= xi, yi <= 106
所有点 (xi, yi) 两两不同。
'''

class DisjointSetUnion(object):
    def __init__(self, n):
        self.n = n
        self.rank = [1] * n
        self.f = list(range(n))

    def find(self, x):
        if self.f[x] == x:
            return x
        self.f[x] = self.find(self.f[x])
        return self.f[x]

    def unionSet(self, x, y):
        fx, fy = self.find(x), self.find(y)
        if fx == fy:
            return False

        if self.rank[fx] < self.rank[fy]:
            fx, fy = fy, fx

        self.rank[fx] += self.rank[fy]
        self.f[fy] = fx
        return True

class Solution(object):
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        dist = lambda x, y: abs(points[x][0] - points[y][0]) + abs(points[x][1] - points[y][1])

        n = len(points)
        dsu = DisjointSetUnion(n)
        edges = list()

        for i in range(n):
            for j in range(i + 1, n):
                edges.append((dist(i, j), i, j))

        edges.sort()

        ret, num = 0, 1
        for length, x, y in edges:
            if dsu.unionSet(x, y):
                ret += length
                num += 1
                if num == n:
                    break

        return ret




class DisjointSetUnion1(object):
    def __init__(self, n):
        self.n = n
        self.rank = [1] * n
        self.f = list(range(n))

    def find(self, x):
        if self.f[x] == x:
            return x
        self.f[x] = self.find(self.f[x])
        return self.f[x]

    def unionSet(self, x, y):
        fx, fy = self.find(x), self.find(y)
        if fx == fy:
            return False

        if self.rank[fx] < self.rank[fy]:
            fx, fy = fy, fx

        self.rank[fx] += self.rank[fy]
        self.f[fy] = fx
        return True


class Solution1(object):
    def minCostConnectPoints(self, points):
        dist = lambda x, y: abs(points[x][0] - points[y][0]) + abs(points[x][1] - points[y][1])

        n = len(points)
        dsu = DisjointSetUnion(n)
        edges = list()

        for i in range(n):
            for j in range(i + 1, n):
                edges.append((dist(i, j), i, j))

        edges.sort()

        ret, num = 0, 1
        for length, x, y in edges:
            if dsu.unionSet(x, y):
                ret += length
                num += 1
                if num == n:
                    break

        return ret


# solutions

'''
写在前面
根据题意，我们得到了一张 nn 个节点的完全图，任意两点之间的距离均为它们的曼哈顿距离。现在我们需要在这个图中取得一个子图，恰满足子图的任意两点之间有且仅有一条简单路径，且这个子图的所有边的总权值之和尽可能小。

能够满足任意两点之间有且仅有一条简单路径只有树，且这棵树包含 nn 个节点。我们称这棵树为给定的图的生成树，其中总权值最小的生成树，我们称其为最小生成树。

最小生成树有一个非常经典的解法：\text{Kruskal}Kruskal。

方法一：\text{Kruskal}Kruskal 算法
思路及解法

\text{Kruskal}Kruskal 算法是一种常见并且好写的最小生成树算法，由 \text{Kruskal}Kruskal 发明。该算法的基本思想是从小到大加入边，是一个贪心算法。

其算法流程为：

将图 G=\{V,E\}G={V,E} 中的所有边按照长度由小到大进行排序，等长的边可以按任意顺序。

初始化图 G'G 
′
  为 \{V,\varnothing\}{V,∅}，从前向后扫描排序后的边，如果扫描到的边 ee 在 G'G 
′
  中连接了两个相异的连通块,则将它插入 G'G 
′
  中。

最后得到的图 G'G 
′
  就是图 GG 的最小生成树。

在实际代码中，我们首先将这张完全图中的边全部提取到边集数组中，然后对所有边进行排序，从小到大进行枚举，每次贪心选边加入答案。使用并查集维护连通性，若当前边两端不连通即可选择这条边。

代码

C++JavaGolangPython3JavaScriptC

class DisjointSetUnion:
    def __init__(self, n):
        self.n = n
        self.rank = [1] * n
        self.f = list(range(n))
    
    def find(self, x: int) -> int:
        if self.f[x] == x:
            return x
        self.f[x] = self.find(self.f[x])
        return self.f[x]
    
    def unionSet(self, x: int, y: int) -> bool:
        fx, fy = self.find(x), self.find(y)
        if fx == fy:
            return False

        if self.rank[fx] < self.rank[fy]:
            fx, fy = fy, fx
        
        self.rank[fx] += self.rank[fy]
        self.f[fy] = fx
        return True

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        dist = lambda x, y: abs(points[x][0] - points[y][0]) + abs(points[x][1] - points[y][1])

        n = len(points)
        dsu = DisjointSetUnion(n)
        edges = list()

        for i in range(n):
            for j in range(i + 1, n):
                edges.append((dist(i, j), i, j))
        
        edges.sort()
        
        ret, num = 0, 1
        for length, x, y in edges:
            if dsu.unionSet(x, y):
                ret += length
                num += 1
                if num == n:
                    break
        
        return ret
复杂度分析

时间复杂度：O(n^2\log(n))O(n 
2
 log(n))，其中 nn 是节点数。一般 \text{Kruskal}Kruskal 是 O(m\log m)O(mlogm) 的算法，但本题中 m=n^2m=n 
2
 ，因此总时间复杂度为 O(n^2\log(n))O(n 
2
 log(n))。

空间复杂度：O(n^2)O(n 
2
 )，其中 nn 是节点数。并查集使用 O(n)O(n) 的空间，边集数组需要使用 O(n^2)O(n 
2
 ) 的空间。

方法二：建图优化的 \text{Kruskal}Kruskal
思路及解法

方法一中，虽然使用了 \text{Kruskal}Kruskal 算法，但时间复杂度仍然较高，因为本题中的边数是 O(n^2)O(n 
2
 ) 的，所以我们需要想办法将减少边数。为此，我们提出几个结论：

结论一：对于图中的任意三点 A,B,CA,B,C，假设边 AB,AC,BCAB,AC,BC 中 ABAB 为最长边，那么最终答案中必然不包含边 ABAB。

我们利用反证法证明：假设最后答案中包含 ABAB，那么此时 ACAC 与 BCBC 两边中至少有一条边是没有被选用的，我们总可以在保证连通性的情况下，将 ABAB 边替换为 ACAC 与 BCBC 两边中的某一个，使最小生成树的总权值变得更小。

结论二：对于下图中同属同一个区块的任意两点 B,CB,C，AA 为原点，那么 BCBC 不可能为三边中最长边。



图中任意一个区块的两分割线的夹角均为 45^\circ45 
∘
 。

我们以 P1P1 区块为例，假设 B(x_B,y_B),C(x_C,y_C)B(x 
B
​	
 ,y 
B
​	
 ),C(x 
C
​	
 ,y 
C
​	
 )，不失一般性，假设 x_B + y_B \leq x_C + y_Cx 
B
​	
 +y 
B
​	
 ≤x 
C
​	
 +y 
C
​	
 。

因为处于 P1P1 区域，所以有 0 \leq x_B \leq y_B0≤x 
B
​	
 ≤y 
B
​	
 ，0 \leq x_C \leq y_C0≤x 
C
​	
 ≤y 
C
​	
 。所以 BC = |x_B - x_C| + |y_B - y_C|BC=∣x 
B
​	
 −x 
C
​	
 ∣+∣y 
B
​	
 −y 
C
​	
 ∣。

下面我们尝试分类讨论：

当 x_B > x_C, y_B > y_Cx 
B
​	
 >x 
C
​	
 ,y 
B
​	
 >y 
C
​	
 ，这与 x_B + y_B \leq x_C + y_Cx 
B
​	
 +y 
B
​	
 ≤x 
C
​	
 +y 
C
​	
  矛盾。

当 x_B \leq x_C, y_B > y_Cx 
B
​	
 ≤x 
C
​	
 ,y 
B
​	
 >y 
C
​	
 ，此时有 |BC| = x_C - x_B + y_B - y_C∣BC∣=x 
C
​	
 −x 
B
​	
 +y 
B
​	
 −y 
C
​	
 ，|AC| - |BC| = x_C + y_C - x_C + x_B - y_B + y_C = x_B - y_B + 2 \times y_C∣AC∣−∣BC∣=x 
C
​	
 +y 
C
​	
 −x 
C
​	
 +x 
B
​	
 −y 
B
​	
 +y 
C
​	
 =x 
B
​	
 −y 
B
​	
 +2×y 
C
​	
 。由前面各种关系可得 y_B > y_C > x_C > x_By 
B
​	
 >y 
C
​	
 >x 
C
​	
 >x 
B
​	
 。假设 |AC| < |BC|∣AC∣<∣BC∣，即 y_B > 2 \times y_C + x_By 
B
​	
 >2×y 
C
​	
 +x 
B
​	
 ，那么 |AB| = x_B + y_B > 2 \times x_B + 2 \times y_C∣AB∣=x 
B
​	
 +y 
B
​	
 >2×x 
B
​	
 +2×y 
C
​	
 ，|AC| = x_C + y_C < 2 \times y_C < |AB|∣AC∣=x 
C
​	
 +y 
C
​	
 <2×y 
C
​	
 <∣AB∣ 与前提矛盾，故 |AC| \geq |BC|∣AC∣≥∣BC∣；

x_B > x_Cx 
B
​	
 >x 
C
​	
  且 y_B \leq y_Cy 
B
​	
 ≤y 
C
​	
 。与 22 同理；

x_B \leq x_Cx 
B
​	
 ≤x 
C
​	
  且 y_B \leq y_Cy 
B
​	
 ≤y 
C
​	
 。此时显然有 |AB| + |BC| = |AC|∣AB∣+∣BC∣=∣AC∣，即有 |AC| > |BC|∣AC∣>∣BC∣。

综上有 |AC| \geq |BC|∣AC∣≥∣BC∣，这个性质可以从 P1P1 区域推导到其他七个区域。

结论三：假设存在一点 AA 在原点处，那么对于图中的任意一个 45^\circ45 
∘
  区域，我们都至多只选择其中的一个点与 AA 相连，且该点必然为该区域中距离 AA 最近的点。

我们首先利用反证法证明：假设最后答案中包含 ABAB 与 ACAC，且 BB 与 CC 均位于同一个 45^\circ45 
∘
  区域中。那么由结论二可知，BCBC 必不为三边中的最长边。即最长边必然为 ABAB 或 ACAC。由结论一可知，ABAB 与 ACAC 中必然有一个不包含在答案中，这与假设相悖，因此我们最多仅会选择一个点与 AA 相连。

我们进一步思考，既然最多仅会选择一个点与 AA 相连，且三边中的最长边不为 AA 的对边，那么仅有距离 AA 最近的点与 AA 所连的边可能出现在答案中。证毕。

依据结论三我们可以知道，一个点至多连八条边，因此我们至多只需要连出 O(n)O(n) 条边。

细节

为防止重复连边，我们对每一个点只考虑对 P1,P2,P3,P4P1,P2,P3,P4 连边的情况，假设 AA 点坐标为 (x,y)(x,y)，对于这四个点，我们可以概括为：

对于 P1P1 区域的 (x_1,y_1)(x 
1
​	
 ,y 
1
​	
 )，有 x_1 \geq x, y_1 - x_1 \geq y - xx 
1
​	
 ≥x,y 
1
​	
 −x 
1
​	
 ≥y−x，其中最近点的 x_1 + y_1x 
1
​	
 +y 
1
​	
  最小。

对于 P2P2 区域的 (x_2,y_2)(x 
2
​	
 ,y 
2
​	
 )，有 y_2 \geq y, y_2 - x_2 \leq y - xy 
2
​	
 ≥y,y 
2
​	
 −x 
2
​	
 ≤y−x，其中最近点的 x_2 + y_2x 
2
​	
 +y 
2
​	
  最小。

对于 P3P3 区域的 (x_3,y_3)(x 
3
​	
 ,y 
3
​	
 )，有 y_3 \leq y, y_3 + x_3 \geq y + xy 
3
​	
 ≤y,y 
3
​	
 +x 
3
​	
 ≥y+x，其中最近点的 y_3 - x_3y 
3
​	
 −x 
3
​	
  最小。

对于 P4P4 区域的 (x_4,y_4)(x 
4
​	
 ,y 
4
​	
 )，有 x_4 \geq x, y_4 + x_4 \leq y + xx 
4
​	
 ≥x,y 
4
​	
 +x 
4
​	
 ≤y+x，其中最近点的 y_4 - x_4y 
4
​	
 −x 
4
​	
  最小。

这样，我们分别处理每一个区域即可，以 P1P1 区域为例，我们先通过排序使得所有点按照横坐标从大到小排列，然后将每一个点的 y_i - x_iy 
i
​	
 −x 
i
​	
  信息记录，将离散化后记录在数组的下标为 y_i - x_iy 
i
​	
 −x 
i
​	
  的位置中，并利用树状数组维护该数组的前缀最小值。这样我们就可以动态地、单次 O(\log n)O(logn) 地计算每个点的 P1P1 区域所选择的点。

为了提升编码效率，实际代码中我们只实现了 P1P1 区域的算法，对于其它三个区域，我们通过巧妙的坐标变化使其条件变为 P1P1 区域，使得代码能够更加高效地复用。

代码

下面代码中的 \texttt{Python}Python 代码中需要 \texttt{import}import 类型标注中的 \texttt{Tuple}Tuple，当然删去对应部分也可以成功运行。

C++JavaGolangPython3

class DisjointSetUnion:
    def __init__(self, n):
        self.n = n
        self.rank = [1] * n
        self.f = list(range(n))
    
    def find(self, x: int) -> int:
        if self.f[x] == x:
            return x
        self.f[x] = self.find(self.f[x])
        return self.f[x]
    
    def unionSet(self, x: int, y: int) -> bool:
        fx, fy = self.find(x), self.find(y)
        if fx == fy:
            return False

        if self.rank[fx] < self.rank[fy]:
            fx, fy = fy, fx
        
        self.rank[fx] += self.rank[fy]
        self.f[fy] = fx
        return True

class BIT:
    def __init__(self, n):
        self.n = n
        self.tree = [float("inf")] * n
        self.idRec = [-1] * n
        self.lowbit = lambda x: x & (-x)
    
    def update(self, pos: int, val: int, identity: int):
        while pos > 0:
            if self.tree[pos] > val:
                self.tree[pos] = val
                self.idRec[pos] = identity
            pos -= self.lowbit(pos)

    def query(self, pos: int) -> int:
        minval, j = float("inf"), -1
        while pos < self.n:
            if minval > self.tree[pos]:
                minval = self.tree[pos]
                j = self.idRec[pos]
            pos += self.lowbit(pos)
        return j

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        edges = list()

        def build(pos: List[Tuple[int, int, int]]):
            pos.sort()
            a = [y - x for (x, y, _) in pos]
            b = sorted(set(a))
            num = len(b)

            bit = BIT(num + 1)
            for i in range(n - 1, -1, -1):
                poss = bisect.bisect(b, a[i])
                j = bit.query(poss)
                if j != -1:
                    dis = abs(pos[i][0] - pos[j][0]) + abs(pos[i][1] - pos[j][1])
                    edges.append((dis, pos[i][2], pos[j][2]))
                bit.update(poss, pos[i][0] + pos[i][1], i)
        
        def solve():
            pos = [(x, y, i) for i, (x, y) in enumerate(points)]
            build(pos)
            pos = [(y, x, i) for i, (x, y) in enumerate(points)]
            build(pos)
            pos = [(-y, x, i) for i, (x, y) in enumerate(points)]
            build(pos)
            pos = [(x, -y, i) for i, (x, y) in enumerate(points)]
            build(pos)
        
        solve()
        dsu = DisjointSetUnion(n)
        edges.sort()
        
        ret, num = 0, 1
        for length, x, y in edges:
            if dsu.unionSet(x, y):
                ret += length
                num += 1
                if num == n:
                    break
        
        return ret
复杂度分析

时间复杂度：O(n \log n)O(nlogn)，其中 nn 是节点数。预处理建边的时间复杂度为 O(n \log n)O(nlogn)，因为需要排序，以及使用树状数组维护。在只有 O(n)O(n) 条边的情况下，\text{Kruskal}Kruskal 的时间复杂度为 O(n\log n)O(nlogn)，因此总时间复杂度为 O(n \log n)O(nlogn)。

空间复杂度：O(n)O(n)，其中 nn 是节点数。树状数组，并查集、离散化以及边集数组都只使用 O(n)O(n) 的空间。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/min-cost-to-connect-all-points/solution/lian-jie-suo-you-dian-de-zui-xiao-fei-yo-kcx7/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
