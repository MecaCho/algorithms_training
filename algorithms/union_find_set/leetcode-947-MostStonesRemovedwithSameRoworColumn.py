# encoding=utf8

'''
947. Most Stones Removed with Same Row or Column
On a 2D plane, we place n stones at some integer coordinate points. Each coordinate point may have at most one stone.

A stone can be removed if it shares either the same row or the same column as another stone that has not been removed.

Given an array stones of length n where stones[i] = [xi, yi] represents the location of the ith stone, return the largest possible number of stones that can be removed.



Example 1:

Input: stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
Output: 5
Explanation: One way to remove 5 stones is as follows:
1. Remove stone [2,2] because it shares the same row as [2,1].
2. Remove stone [2,1] because it shares the same column as [0,1].
3. Remove stone [1,2] because it shares the same row as [1,0].
4. Remove stone [1,0] because it shares the same column as [0,0].
5. Remove stone [0,1] because it shares the same row as [0,0].
Stone [0,0] cannot be removed since it does not share a row/column with another stone still on the plane.
Example 2:

Input: stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
Output: 3
Explanation: One way to make 3 moves is as follows:
1. Remove stone [2,2] because it shares the same row as [2,0].
2. Remove stone [2,0] because it shares the same column as [0,0].
3. Remove stone [0,2] because it shares the same row as [0,0].
Stones [0,0] and [1,1] cannot be removed since they do not share a row/column with another stone still on the plane.
Example 3:

Input: stones = [[0,0]]
Output: 0
Explanation: [0,0] is the only stone on the plane, so you cannot remove it.


Constraints:

1 <= stones.length <= 1000
0 <= xi, yi <= 104
No two stones are at the same coordinate point.


947. 移除最多的同行或同列石头
n 块石头放置在二维平面中的一些整数坐标点上。每个坐标点上最多只能有一块石头。

如果一块石头的 同行或者同列 上有其他石头存在，那么就可以移除这块石头。

给你一个长度为 n 的数组 stones ，其中 stones[i] = [xi, yi] 表示第 i 块石头的位置，返回 可以移除的石子 的最大数量。



示例 1：

输入：stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
输出：5
解释：一种移除 5 块石头的方法如下所示：
1. 移除石头 [2,2] ，因为它和 [2,1] 同行。
2. 移除石头 [2,1] ，因为它和 [0,1] 同列。
3. 移除石头 [1,2] ，因为它和 [1,0] 同行。
4. 移除石头 [1,0] ，因为它和 [0,0] 同列。
5. 移除石头 [0,1] ，因为它和 [0,0] 同行。
石头 [0,0] 不能移除，因为它没有与另一块石头同行/列。
示例 2：

输入：stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
输出：3
解释：一种移除 3 块石头的方法如下所示：
1. 移除石头 [2,2] ，因为它和 [2,0] 同行。
2. 移除石头 [2,0] ，因为它和 [0,0] 同列。
3. 移除石头 [0,2] ，因为它和 [0,0] 同行。
石头 [0,0] 和 [1,1] 不能移除，因为它们没有与另一块石头同行/列。
示例 3：

输入：stones = [[0,0]]
输出：0
解释：[0,0] 是平面上唯一一块石头，所以不可以移除它。


提示：

1 <= stones.length <= 1000
0 <= xi, yi <= 104
不会有两块石头放在同一个坐标点上
'''


class Solution(object):
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        length_stone = len(stones)
        ufs_length = 20000
        p = [i for i in range(ufs_length)]

        def find(x):
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]

        def union(x, y):
            px = find(x)
            py = find(y)
            if px != py:
                p[px] = py

        for x, y in stones:
            union(x, y + 10000)

        return len(stones) - len({find(x) for x, _ in stones})



# solution


'''
把二维坐标平面上的石头想象成图的顶点，如果两个石头横坐标相同、或者纵坐标相同，在它们之间形成一条边。



根据可以移除石头的规则：如果一块石头的 同行或者同列 上有其他石头存在，那么就可以移除这块石头。可以发现：一定可以把一个连通图里的所有顶点根据这个规则删到只剩下一个顶点。

为什么这么说呢？既然这些顶点在一个连通图里，可以通过遍历的方式（深度优先遍历或者广度优先遍历）遍历到这个连通图的所有顶点。那么就可以按照遍历的方式 逆向 移除石头，最后只剩下一块石头。所以：最多可以移除的石头的个数 = 所有石头的个数 - 连通分量的个数。

题目没有让我们给出具体移除石头的方案，可以考虑使用并查集。

方法：并查集
删到最后，留在图中的顶点一定位于不同的行和不同的列。因此，并查集里的元素是 描述「横坐标」和「纵坐标」的数值。因此我们需要遍历数组 stones，将每个 stone 的横坐标和纵坐标在并查集中进行合并。理解合并的语义十分重要。

「合并」的语义
「合并」的语义是：所有横坐标为 x 的石头和所有纵坐标为 y 的石头都属于同一个连通分量。

并查集里如何区分横纵坐标
然而会遇到这样一个问题：石头的位置是「有序数对（二维）」，并查集的底层是「一维数组」，我们在并查集里应该如何区分横纵坐标呢？

例如：如果一块石头的坐标为 [3, 3] ，那么所有横坐标为 3 的石头和所有纵坐标为 3 的石头都在一个连通分量中，但是我们需要在并查集里区分「横坐标」和「纵坐标」，它们在并查集里不能相等，根据题目的提示 0 <= x_i, y_i <= 10^40<=x 
i
​	
 ,y 
i
​	
 <=10 
4
 ，可以把其中一个坐标 映射 到另一个与 [0, 10000] 不重合的区间，可以的做法是把横坐标全部减去 1000010000 或者全部加上 1000010000 ，或者按位取反。

在并查集里我们需要维护连通分量的个数，新创建顶点的时候连通分量加 11；合并不在同一个连通分量中的两个并查集的时候，连通分量减 11。

参考代码：

Java

import java.util.HashMap;
import java.util.Map;

public class Solution {

    public int removeStones(int[][] stones) {
        UnionFind unionFind = new UnionFind();

        for (int[] stone : stones) {
            // 下面这三种写法任选其一
            // unionFind.union(~stone[0], stone[1]);
            // unionFind.union(stone[0] - 10000, stone[1]);
            unionFind.union(stone[0] + 10000, stone[1]);
        }
        return stones.length - unionFind.getCount();
    }

    private class UnionFind {

        private Map<Integer, Integer> parent;
        private int count;

        public UnionFind() {
            this.parent = new HashMap<>();
            this.count = 0;
        }

        public int getCount() {
            return count;
        }

        public int find(int x) {
            if (!parent.containsKey(x)) {
                parent.put(x, x);
                count++;
            }

            if (x != parent.get(x)) {
                parent.put(x, find(parent.get(x)));
            }
            return parent.get(x);
        }

        public void union(int x, int y) {
            int rootX = find(x);
            int rootY = find(y);
            if (rootX == rootY) {
                return;
            }

            parent.put(rootX, rootY);
            count--;
        }
    }
}
复杂度分析：

时间复杂度：O(n \log(A))O(nlog(A))，其中 nn 为石子的数量，AA 是数组 stones 里横纵坐标不同值的总数；
空间复杂度：O(A)O(A)，并查集的底层哈希表的长度为 AA。

作者：LeetCode
链接：https://leetcode-cn.com/problems/most-stones-removed-with-same-row-or-column/solution/947-yi-chu-zui-duo-de-tong-xing-huo-tong-ezha/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''


# solutions

'''
方法一：深度优先搜索
思路及解法

我们将这个二维平面抽象为图，把石子看作「点」，石子间的同行或同列关系看作「边」。如果两个石子同属某一行或某一列，我们就认为这两个石子之间有一条边。由题意可知，对于任意一个点，只要有点和它相连，我们就可以将其删除。

显然，对于任意一个连通图，我们总可以通过调整节点的删除顺序，把这个连通图中删到只剩下一个节点。本题中我们不需要关注如何安排删除顺序，只需要了解这个性质即可。

拓展：对于希望进一步拓展的同学，这里给出一个方法：从连通块中处理出任意一个生成树，该生成树的以任意一点为根节点的后序遍历均为可行解。

这样我们只需要统计整张图中有多少个极大连通子图（也叫做连通块或连通分量）即可。最终能够留下来的点的数量，即为连通块的数量。我们用总点数减去连通块的数量，即可知道我们可以删去的点的最大数量。

在实际代码实现中，我们首先枚举计算任意两点间的连通性，然后使用深度优先搜索的方式计算连通块的数量即可。

代码

C++JavaGolangPython3C

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        edge = collections.defaultdict(list)
        for i, (x1, y1) in enumerate(stones):
            for j, (x2, y2) in enumerate(stones):
                if x1 == x2 or y1 == y2:
                    edge[i].append(j)
        
        def dfs(x: int):
            vis.add(x)
            for y in edge[x]:
                if y not in vis:
                    dfs(y)
        
        vis = set()
        num = 0
        for i in range(n):
            if i not in vis:
                num += 1
                dfs(i)
        
        return n - num
复杂度分析

时间复杂度：O(n^2)O(n 
2
 )，其中 nn 为石子的数量。我们需要枚举计算任意两个石子是否在同行或同列，建图时间复杂度 O(n^2)O(n 
2
 )，同时我们需要通过深度优先搜索计算连通块数量，每一个点和每一条边都被枚举一次，时间复杂度 O(n+m)O(n+m)。其中 mm 是边数，可以保证 m < n^2m<n 
2
 。因此总时间复杂度为 O(n^2)O(n 
2
 )。

空间复杂度：O(n^2)O(n 
2
 )。最坏情况下任意两点都相连，用来保存连通属性的边集数组将会达到 O(n^2)O(n 
2
 ) 的大小。

方法二：优化建图 + 深度优先搜索
思路及解法

注意到方法一中，建图的效率太过低下，我们考虑对其优化。

注意到任意两点间之间直接相连与间接相连并无影响，即我们只关注两点间的连通性，而不关注具体如何联通。因此考虑对于拥有 kk 个石子的任意一行或一列，我们都恰使用 k-1k−1 条边进行连接。这样我们就可以将边数从 O(n^2)O(n 
2
 ) 的数量级降低到 O(n)O(n)。

这样，我们首先利用哈希表存储每一行或每一列所拥有的石子，然后分别处理每一行或每一列的连通属性即可。

注意到每一个石子的横坐标与纵坐标的范围均在 [1,10^4][1,10 
4
 ]，因此在实际代码中，我们可以使用同一张哈希表，只需要令纵坐标加 10^410 
4
 ，以区别横坐标与纵坐标即可。

代码

C++JavaGolangPython3

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        edge = collections.defaultdict(list)
        rec = collections.defaultdict(list)
        for i, (x, y) in enumerate(stones):
            rec[x].append(i)
            rec[y + 10000].append(i)
        
        for vec in rec.values():
            k = len(vec)
            for i in range(1, k):
                edge[vec[i - 1]].append(vec[i])
                edge[vec[i]].append(vec[i - 1])
        
        def dfs(x: int):
            vis.add(x)
            for y in edge[x]:
                if y not in vis:
                    dfs(y)
        
        vis = set()
        num = 0
        for i in range(n):
            if i not in vis:
                num += 1
                dfs(i)
        
        return n - num
复杂度分析

时间复杂度：O(n)O(n)，其中 nn 为石子的数量。任意一个石子至多只有四条边与其相连，且至多被遍历一次。

空间复杂度：O(n)O(n)。任意一个石子至多只有四条边与其相连，用来保存连通属性的边集数组至多只会达到 O(n)O(n) 的大小。

方法三：优化建图 + 并查集
思路及解法

我们也可以变换思路，在方法一与方法二中，我们维护的是石子，实际上我们也可以直接维护石子所在的行与列。

实际操作时，我们直接将每一个石子的行与列进行合并即可，可以理解为，每一个点不是与其他所有点进行连接，而是连接到自己所在的行与列上，由行与列进行合并。

同时，既然我们只关注连通性本身，我们就可以利用并查集维护连通性。在实际代码中，我们以哈希表为底层数据结构实现父亲数组 ff，最后哈希表中所有的键均为出现过的行与列，我们计算有多少行与列的父亲恰为自己，即可知道连通块的数量。

代码

C++JavaGolangPython3C

class DisjointSetUnion:
    def __init__(self):
        self.f = dict()
        self.rank = dict()
    
    def find(self, x: int) -> int:
        if x not in self.f:
            self.f[x] = x
            self.rank[x] = 1
            return x
        if self.f[x] == x:
            return x
        self.f[x] = self.find(self.f[x])
        return self.f[x]
    
    def unionSet(self, x: int, y: int):
        fx, fy = self.find(x), self.find(y)
        if fx == fy:
            return
        if self.rank[fx] < self.rank[fy]:
            fx, fy = fy, fx
        self.rank[fx] += self.rank[fy]
        self.f[fy] = fx

    def numberOfConnectedComponent(self) -> int:
        return sum(1 for x, fa in self.f.items() if x == fa)


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        dsu = DisjointSetUnion()
        for x, y in stones:
            dsu.unionSet(x, y + 10000)
        return len(stones) - dsu.numberOfConnectedComponent()
复杂度分析

时间复杂度：O(n\alpha(n))O(nα(n))，其中 nn 为石子的数量。\alphaα 是反 \text{Ackerman}Ackerman 函数。

空间复杂度：O(n)O(n)。空间为并查集和哈希表的开销。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/most-stones-removed-with-same-row-or-column/solution/yi-chu-zui-duo-de-tong-xing-huo-tong-lie-m50r/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
