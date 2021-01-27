# encoding=utf8

'''
1579. Remove Max Number of Edges to Keep Graph Fully Traversable
Alice and Bob have an undirected graph of n nodes and 3 types of edges:

Type 1: Can be traversed by Alice only.
Type 2: Can be traversed by Bob only.
Type 3: Can by traversed by both Alice and Bob.
Given an array edges where edges[i] = [typei, ui, vi] represents a bidirectional edge of type typei between nodes ui and vi, find the maximum number of edges you can remove so that after removing the edges, the graph can still be fully traversed by both Alice and Bob. The graph is fully traversed by Alice and Bob if starting from any node, they can reach all other nodes.

Return the maximum number of edges you can remove, or return -1 if it's impossible for the graph to be fully traversed by Alice and Bob.



Example 1:



Input: n = 4, edges = [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]
Output: 2
Explanation: If we remove the 2 edges [1,1,2] and [1,1,3]. The graph will still be fully traversable by Alice and Bob. Removing any additional edge will not make it so. So the maximum number of edges we can remove is 2.
Example 2:



Input: n = 4, edges = [[3,1,2],[3,2,3],[1,1,4],[2,1,4]]
Output: 0
Explanation: Notice that removing any edge will not make the graph fully traversable by Alice and Bob.
Example 3:



Input: n = 4, edges = [[3,2,3],[1,1,2],[2,3,4]]
Output: -1
Explanation: In the current graph, Alice cannot reach node 4 from the other nodes. Likewise, Bob cannot reach 1. Therefore it's impossible to make the graph fully traversable.




Constraints:

1 <= n <= 10^5
1 <= edges.length <= min(10^5, 3 * n * (n-1) / 2)
edges[i].length == 3
1 <= edges[i][0] <= 3
1 <= edges[i][1] < edges[i][2] <= n
All tuples (typei, ui, vi) are distinct.


1579. 保证图可完全遍历
Alice 和 Bob 共有一个无向图，其中包含 n 个节点和 3  种类型的边：

类型 1：只能由 Alice 遍历。
类型 2：只能由 Bob 遍历。
类型 3：Alice 和 Bob 都可以遍历。
给你一个数组 edges ，其中 edges[i] = [typei, ui, vi] 表示节点 ui 和 vi 之间存在类型为 typei 的双向边。请你在保证图仍能够被 Alice和 Bob 完全遍历的前提下，找出可以删除的最大边数。如果从任何节点开始，Alice 和 Bob 都可以到达所有其他节点，则认为图是可以完全遍历的。

返回可以删除的最大边数，如果 Alice 和 Bob 无法完全遍历图，则返回 -1 。



示例 1：



输入：n = 4, edges = [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]
输出：2
解释：如果删除 [1,1,2] 和 [1,1,3] 这两条边，Alice 和 Bob 仍然可以完全遍历这个图。再删除任何其他的边都无法保证图可以完全遍历。所以可以删除的最大边数是 2 。
示例 2：



输入：n = 4, edges = [[3,1,2],[3,2,3],[1,1,4],[2,1,4]]
输出：0
解释：注意，删除任何一条边都会使 Alice 和 Bob 无法完全遍历这个图。
示例 3：



输入：n = 4, edges = [[3,2,3],[1,1,2],[2,3,4]]
输出：-1
解释：在当前图中，Alice 无法从其他节点到达节点 4 。类似地，Bob 也不能达到节点 1 。因此，图无法完全遍历。


提示：

1 <= n <= 10^5
1 <= edges.length <= min(10^5, 3 * n * (n-1) / 2)
edges[i].length == 3
1 <= edges[i][0] <= 3
1 <= edges[i][1] < edges[i][2] <= n
所有元组 (typei, ui, vi) 互不相同
'''


class UnionFind(object):
    def __init__(self, n):
        self.p = [i  for i in range(n)]

    def find(self, x):
        px = self.p[x]
        if px != x:
            px = self.find(self.p[px])
        return px

    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px != py:
            self.p[px] = py
            return False
        return True

    def get_count(self):
        res =  sum([1 if i == self.p[i] else 0 for i in range(len(self.p))])
        return res


class Solution(object):
    def maxNumEdgesToRemove(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        ufa = UnionFind(n)
        ufb = UnionFind(n)

        res = 0
        for i in range(len(edges)):
            x, y = edges[i][1]-1, edges[i][2]-1
            if edges[i][0] == 3:
                if ufa.union(x, y):
                    res += 1
                else:
                    ufb.union(x, y)

        for i in range(len(edges)):
            x, y = edges[i][1]-1, edges[i][2]-1

            if edges[i][0] == 1:
                if ufa.union(x, y):
                    res += 1
            elif edges[i][0] == 2:
                if ufb.union(x, y):
                    res += 1

        if ufa.get_count() != 1 or ufb.get_count() != 1:
            return -1
        return res




'''
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
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        ufa, ufb = UnionFind(n), UnionFind(n)
        ans = 0
        
        # 节点编号改为从 0 开始
        for edge in edges:
            edge[1] -= 1
            edge[2] -= 1

        # 公共边
        for t, u, v in edges:
            if t == 3:
                if not ufa.unite(u, v):
                    ans += 1
                else:
                    ufb.unite(u, v)

        # 独占边
        for t, u, v in edges:
            if t == 1:
                # Alice 独占边
                if not ufa.unite(u, v):
                    ans += 1
            elif t == 2:
                # Bob 独占边
                if not ufb.unite(u, v):
                    ans += 1

        if ufa.setCount != 1 or ufb.setCount != 1:
            return -1
        return ans

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/solution/bao-zheng-tu-ke-wan-quan-bian-li-by-leet-mtrw/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''


# solutions

'''
方法一：并查集
思路与算法

我们称类型 1, 2, 31,2,3 的边分别为「Alice 独占边」「Bob 独占边」以及「公共边」。

首先我们需要思考什么样的图是可以被 Alice 和 Bob 完全遍历的。对于 Alice 而言，她可以经过的边是「Alice 独占边」以及「公共边」，由于她需要能够从任意节点到达任意节点，那么就说明：

当图中仅有「Alice 独占边」以及「公共边」时，整个图是连通的，即整个图只包含一个连通分量。

同理，对于 Bob 而言，当图中仅有「Bob 独占边」以及「公共边」时，整个图也要是连通的。

由于题目描述中希望我们删除最多数目的边，这等价于保留最少数目的边。换句话说，我们可以从一个仅包含 nn 个节点（而没有边）的无向图开始，逐步添加边，使得满足上述的要求。

那么我们应该按照什么策略来添加边呢？直觉告诉我们，「公共边」的重要性大于「Alice 独占边」以及「Bob 独占边」，因为「公共边」是 Alice 和 Bob 都可以使用的，而他们各自的独占边却不能给对方使用。「公共边」的重要性也是可以证明的：

对于一条连接了两个不同的连通分量的「公共边」而言，如果我们不保留这条公共边，那么 Alice 和 Bob 就无法往返这两个连通分量，即他们分别需要使用各自的独占边。因此，Alice 需要一条连接这两个连通分量的独占边，Bob 同样也需要一条连接这两个连通分量的独占边，那么一共需要两条边，这就严格不优于直接使用一条连接这两个连通分量的「公共边」了。

因此，我们可以遵从优先添加「公共边」的策略。具体地，我们遍历每一条「公共边」，对于其连接的的两个节点：

如果这两个节点在同一个连通分量中，那么添加这条「公共边」是无意义的；

如果这两个节点不在同一个连通分量中，我们就可以（并且一定）添加这条「公共边」，然后合并这两个节点所在的连通分量。

这就提示了我们使用并查集来维护整个图的连通性，上述的策略只需要用到并查集的「查询」和「合并」这两个最基础的操作。

在处理完了所有的「公共边」之后，我们需要处理他们各自的独占边，而方法也与添加「公共边」类似。我们将当前的并查集复制一份，一份交给 Alice，一份交给 Bob。随后 Alice 不断地向并查集中添加「Alice 独占边」，Bob 不断地向并查集中添加「Bob 独占边」。在处理完了所有的独占边之后，如果这两个并查集都只包含一个连通分量，那么就说明 Alice 和 Bob 都可以遍历整个无向图。

细节

在使用并查集进行合并的过程中，我们每遇到一次失败的合并操作（即需要合并的两个点属于同一个连通分量），那么就说明当前这条边可以被删除，将答案增加 11。

代码

C++JavaPython3JavaScriptGolangC

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
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        ufa, ufb = UnionFind(n), UnionFind(n)
        ans = 0
        
        # 节点编号改为从 0 开始
        for edge in edges:
            edge[1] -= 1
            edge[2] -= 1

        # 公共边
        for t, u, v in edges:
            if t == 3:
                if not ufa.unite(u, v):
                    ans += 1
                else:
                    ufb.unite(u, v)

        # 独占边
        for t, u, v in edges:
            if t == 1:
                # Alice 独占边
                if not ufa.unite(u, v):
                    ans += 1
            elif t == 2:
                # Bob 独占边
                if not ufb.unite(u, v):
                    ans += 1

        if ufa.setCount != 1 or ufb.setCount != 1:
            return -1
        return ans
复杂度分析

时间复杂度：O(m \cdot \alpha(n))O(m⋅α(n))，其中 mm 是数组 \textit{edges}edges 的长度，\alphaα 是阿克曼函数的反函数。

空间复杂度：O(n)O(n)，即为并查集需要使用的空间。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/solution/bao-zheng-tu-ke-wan-quan-bian-li-by-leet-mtrw/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''


