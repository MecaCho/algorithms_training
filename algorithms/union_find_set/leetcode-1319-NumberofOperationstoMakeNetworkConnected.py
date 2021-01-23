# encoding=utf8


'''
1319. Number of Operations to Make Network Connected
There are n computers numbered from 0 to n-1 connected by ethernet cables connections forming a network where connections[i] = [a, b] represents a connection between computers a and b. Any computer can reach any other computer directly or indirectly through the network.

Given an initial computer network connections. You can extract certain cables between two directly connected computers, and place them between any pair of disconnected computers to make them directly connected. Return the minimum number of times you need to do this in order to make all the computers connected. If it's not possible, return -1.



Example 1:



Input: n = 4, connections = [[0,1],[0,2],[1,2]]
Output: 1
Explanation: Remove cable between computer 1 and 2 and place between computers 1 and 3.
Example 2:



Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]
Output: 2
Example 3:

Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2]]
Output: -1
Explanation: There are not enough cables.
Example 4:

Input: n = 5, connections = [[0,1],[0,2],[3,4],[2,3]]
Output: 0


Constraints:

1 <= n <= 10^5
1 <= connections.length <= min(n*(n-1)/2, 10^5)
connections[i].length == 2
0 <= connections[i][0], connections[i][1] < n
connections[i][0] != connections[i][1]
There are no repeated connections.
No two computers are connected by more than one cable.


1319. 连通网络的操作次数
用以太网线缆将 n 台计算机连接成一个网络，计算机的编号从 0 到 n-1。线缆用 connections 表示，其中 connections[i] = [a, b] 连接了计算机 a 和 b。

网络中的任何一台计算机都可以通过网络直接或者间接访问同一个网络中其他任意一台计算机。

给你这个计算机网络的初始布线 connections，你可以拔开任意两台直连计算机之间的线缆，并用它连接一对未直连的计算机。请你计算并返回使所有计算机都连通所需的最少操作次数。如果不可能，则返回 -1 。



示例 1：



输入：n = 4, connections = [[0,1],[0,2],[1,2]]
输出：1
解释：拔下计算机 1 和 2 之间的线缆，并将它插到计算机 1 和 3 上。
示例 2：



输入：n = 6, connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]
输出：2
示例 3：

输入：n = 6, connections = [[0,1],[0,2],[0,3],[1,2]]
输出：-1
解释：线缆数量不足。
示例 4：

输入：n = 5, connections = [[0,1],[0,2],[3,4],[2,3]]
输出：0


提示：

1 <= n <= 10^5
1 <= connections.length <= min(n*(n-1)/2, 10^5)
connections[i].length == 2
0 <= connections[i][0], connections[i][1] < n
connections[i][0] != connections[i][1]
没有重复的连接。
两台计算机不会通过多条线缆连接。
'''


class Solution(object):
    def makeConnected(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        if len(connections) < n - 1:
            return -1
        self.p = [i for i in range(n)]

        def find(x):
            px = self.p[x]
            if px != x:
                px = find(self.p[px])
            return px

        def union(x, y):
            px = find(x)
            py = find(y)
            if px != py:
                self.p[px] = py

        for con in connections:
            x, y = con[0], con[1]
            union(x, y)

        res = sum([1 if i == self.p[i] else 0 for i in range(n)])

        return res - 1



# solutions


'''
前言
我们首先考虑在什么情况下，不可能将所有计算机进行连接。

当计算机的数量为 nn 时，我们至少需要 n-1n−1 根线才能将它们进行连接。如果线的数量少于 n-1n−1，那么我们无论如何都无法将这 nn 台计算机进行连接。因此如果数组 \textit{connections}connections 的长度小于 n-1n−1，我们可以直接返回 -1−1 作为答案，否则我们一定可以找到一种操作方式。

那么如何计算最少的操作次数呢？我们将这 nn 台计算机看成 nn 个节点，每一条线看成一条无向边。假设这个无向图中有 kk 个「连通分量」，连通分量的定义为：

设集合 VV 为无向图中节点的一个子集，集合 EE 为无向图中所有两个端点都在 VV 中的边。设图 S=(V, E)S=(V,E)，那么 SS 就称为无向图的一个「诱导子图」（或者叫「导出子图」）。「连通分量」是极大的「诱导子图」，这里的「极大」表现在：

VV 中的任意两个节点仅通过 EE 就可以相互到达；

不存在一个不属于 VV 的节点 xx，使得 xx 与 VV 中的某个节点直接相连。

我们可以通过节点集合 VV 唯一地描述一个连通分量：例如在题目给出的样例 11 中，有两个连通分量 \{0, 1, 2\}{0,1,2} 和 \{3\}{3}；样例 22 中，有三个连通分量 \{0, 1, 2, 3\}{0,1,2,3}，\{4\}{4} 和 \{5\}{5}。

如果我们的操作是「添加一根线」而不是「移动一根线」，那么显然只需要添加 k-1k−1 根线就可以将所有计算机进行连接了：例如将编号为 00 的连通分量中的任意一台计算机分别与编号为 1, 2, \cdots, k-11,2,⋯,k−1 的连通分量中的任意一台计算机相连。由于「移动一根线」的操作一定不会优于「添加一根线」，那么我们至少需要移动 k-1k−1 根线，才有可能将所有计算机连接。

那么我们是否可以找到一种移动 k-1k−1 根线的操作方法呢？我们可以发现，mm 台电脑只需要 m-1m−1 根线就可以将它们进行连接。如果一个节点数为 mm 的连通分量中的边数超过 m - 1m−1，就一定可以找到一条多余的边，且移除这条边之后，连通性保持不变。此时，我们就可以用这条边来连接两个连通分量，使得图中连通分量的个数减少 11。

在题目给出的样例 22 中，连通分量 \{0, 1, 2, 3\}{0,1,2,3} 中有 55 条边，大于 m-1=3m−1=3。因此一定可以找到一条多余的边。具体地，该连通分量中的任意一条边被移除后，连通性都保持不变。

注意：并不是在所有的情况下，连通分量中的任意一条边都是可以被移除的，我们只需要保证必定能够找到「一条」多余的边。

因此我们可以设计一个迭代的过程：每次在图中找出一条多余的边，将其断开，并连接图中的两个连通分量。将这个过程重复 k-1k−1 次，最终就可以使得整个图连通。

我们如何保证一定能找出「一条」多余的边呢？我们需要证明的是，在任意时刻，如果图中有 k'k 
′
  个连通分量且 k'>1k 
′
 >1，即整个图还没有完全连通，那么一定存在一个连通分量，使得其有一条多余的边：即它的节点数为 m_im 
i
​	
 ，边数为 e_ie 
i
​	
 ，并且有 e_i > m_i - 1e 
i
​	
 >m 
i
​	
 −1。

我们可以使用反证法来证明上面的结论。假设所有的连通分量都满足 e_i \leq m_i - 1e 
i
​	
 ≤m 
i
​	
 −1，那么：

\begin{cases} e_1 \leq m_1 - 1 \\ e_2 \leq m_2 - 1 \\ \cdots \\ e_{k'} \leq m_{k'} - 1 \end{cases}
⎩
⎪
⎪
⎪
⎪
⎨
⎪
⎪
⎪
⎪
⎧
​	
  
e 
1
​	
 ≤m 
1
​	
 −1
e 
2
​	
 ≤m 
2
​	
 −1
⋯
e 
k 
′
 
​	
 ≤m 
k 
′
 
​	
 −1
​	
 

将这 k'k 
′
  个不等式相加可以得到：

e_1 + \cdots + e_{k'} \leq m_1 + \cdots + m_{k'} - k' = n - k'
e 
1
​	
 +⋯+e 
k 
′
 
​	
 ≤m 
1
​	
 +⋯+m 
k 
′
 
​	
 −k 
′
 =n−k 
′
 

左侧的 e_1 + \cdots + e_{k'}e 
1
​	
 +⋯+e 
k 
′
 
​	
  即为图中的边数，右侧的 m_1 + ... + m_{k'} = nm 
1
​	
 +...+m 
k 
′
 
​	
 =n 即为图中的节点数。由于图中至少有 n-1n−1 条边，那么有：

e_1 + \cdots + e_{k'} \geq n - 1
e 
1
​	
 +⋯+e 
k 
′
 
​	
 ≥n−1

与

e_1 + \cdots + e_{k'} \leq n - k'
e 
1
​	
 +⋯+e 
k 
′
 
​	
 ≤n−k 
′
 

产生了矛盾！因此一定存在一个连通分量，它有一条多余的边。

统计图中连通分量数的方法有很多，本篇题解中我们给出深度优先搜索和并查集两种方法。

方法一：深度优先搜索
思路与算法

我们可以使用深度优先搜索来得到图中的连通分量数。

具体地，初始时所有节点的状态均为「待搜索」。我们每次选择一个「待搜索」的节点，从该节点开始进行深度优先搜索，并将所有搜索到的节点的状态更改为「已搜索」，这样我们就找到了一个连通分量。

代码

C++JavaPython3JavaScriptGolangC

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1
        
        edges = collections.defaultdict(list)
        for x, y in connections:
            edges[x].append(y)
            edges[y].append(x)
        
        seen = set()

        def dfs(u: int):
            seen.add(u)
            for v in edges[u]:
                if v not in seen:
                    dfs(v)
        
        ans = 0
        for i in range(n):
            if i not in seen:
                dfs(i)
                ans += 1
        
        return ans - 1
复杂度分析

时间复杂度：O(n+m)O(n+m)，其中 mm 是数组 \textit{connections}connections 的长度。

空间复杂度：O(n+m)O(n+m)，其中 O(m)O(m) 为存储所有边需要的空间，O(n)O(n) 为深度优先搜索中使用的栈空间。

方法二：并查集
我们可以使用并查集来得到图中的连通分量数。

并查集本身就是用来维护连通性的数据结构。如果其包含 nn 个节点，那么初始时连通分量数为 nn，每成功进行一次合并操作，连通分量数就会减少 11。

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
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1
        
        uf = UnionFind(n)
        for x, y in connections:
            uf.unite(x, y)
        
        return uf.setCount - 1
复杂度分析

时间复杂度：O(m \cdot \alpha(n))O(m⋅α(n))，其中 mm 是数组 \textit{connections}connections 的长度，\alphaα 是阿克曼函数的反函数。

空间复杂度：O(n)O(n)，即为并查集需要使用的空间。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/number-of-operations-to-make-network-connected/solution/lian-tong-wang-luo-de-cao-zuo-ci-shu-by-leetcode-s/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''

