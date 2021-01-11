# encoding=utf8

'''
547. Number of Provinces
There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.



Example 1:


Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2
Example 2:


Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3


Constraints:

1 <= n <= 200
n == isConnected.length
n == isConnected[i].length
isConnected[i][j] is 1 or 0.
isConnected[i][i] == 1
isConnected[i][j] == isConnected[j][i]


547. 省份数量
有 n 个城市，其中一些彼此相连，另一些没有相连。如果城市 a 与城市 b 直接相连，且城市 b 与城市 c 直接相连，那么城市 a 与城市 c 间接相连。

省份 是一组直接或间接相连的城市，组内不含其他没有相连的城市。

给你一个 n x n 的矩阵 isConnected ，其中 isConnected[i][j] = 1 表示第 i 个城市和第 j 个城市直接相连，而 isConnected[i][j] = 0 表示二者不直接相连。

返回矩阵中 省份 的数量。



示例 1：


输入：isConnected = [[1,1,0],[1,1,0],[0,0,1]]
输出：2
示例 2：


输入：isConnected = [[1,0,0],[0,1,0],[0,0,1]]
输出：3


提示：

1 <= n <= 200
n == isConnected.length
n == isConnected[i].length
isConnected[i][j] 为 1 或 0
isConnected[i][i] == 1
isConnected[i][j] == isConnected[j][i]
'''


class UnionFind(object):
    def __init__(self, n):
        self.parents = range(n)

    def find(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, a, b):
        root1 = self.find(a)
        root2 = self.find(b)
        if root1 != root2:
            self.parents[root1] = root2


class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        length = len(isConnected)
        UnionFindSet = UnionFind(length)

        for i in range(length):
            for j in range(i + 1, len(isConnected[0])):
                if isConnected[i][j] == 1:
                    UnionFindSet.union(i, j)
        print(UnionFindSet.parents)

        return sum([1 for i in range(length) if i == UnionFindSet.parents[i]])


if __name__ == '__main__':
    demo = Solution()
    is_connecteds = [[[1, 1, 0], [1, 1, 0], [0, 0, 1]],[[1, 0, 0], [0, 1, 0], [0, 0, 1]]]
    for isConnected in is_connecteds:
        res = demo.findCircleNum(isConnected)
        print(res)


# solutions

'''
前言
可以把 nn 个城市和它们之间的相连关系看成图，城市是图中的节点，相连关系是图中的边，给定的矩阵 \textit{isConnected}isConnected 即为图的邻接矩阵，省份即为图中的连通分量。

计算省份总数，等价于计算图中的连通分量数，可以通过深度优先搜索或广度优先搜索实现，也可以通过并查集实现。

方法一：深度优先搜索
深度优先搜索的思路是很直观的。遍历所有城市，对于每个城市，如果该城市尚未被访问过，则从该城市开始深度优先搜索，通过矩阵 \textit{isConnected}isConnected 得到与该城市直接相连的城市有哪些，这些城市和该城市属于同一个连通分量，然后对这些城市继续深度优先搜索，直到同一个连通分量的所有城市都被访问到，即可得到一个省份。遍历完全部城市以后，即可得到连通分量的总数，即省份的总数。

JavaJavaScriptC++GolangCPython3

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(i: int):
            for j in range(provinces):
                if isConnected[i][j] == 1 and j not in visited:
                    visited.add(j)
                    dfs(j)

        provinces = len(isConnected)
        visited = set()
        circles = 0

        for i in range(provinces):
            if i not in visited:
                dfs(i)
                circles += 1

        return circles
复杂度分析

时间复杂度：O(n^2)O(n
2
 )，其中 nn 是城市的数量。需要遍历矩阵 nn 中的每个元素。

空间复杂度：O(n)O(n)，其中 nn 是城市的数量。需要使用数组 \textit{visited}visited 记录每个城市是否被访问过，数组长度是 nn，递归调用栈的深度不会超过 nn。

方法二：广度优先搜索
也可以通过广度优先搜索的方法得到省份的总数。对于每个城市，如果该城市尚未被访问过，则从该城市开始广度优先搜索，直到同一个连通分量中的所有城市都被访问到，即可得到一个省份。

JavaJavaScriptC++GolangCPython3

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        provinces = len(isConnected)
        visited = set()
        circles = 0

        for i in range(provinces):
            if i not in visited:
                Q = collections.deque([i])
                while Q:
                    j = Q.popleft()
                    visited.add(j)
                    for k in range(provinces):
                        if isConnected[j][k] == 1 and k not in visited:
                            Q.append(k)
                circles += 1

        return circles
复杂度分析

时间复杂度：O(n^2)O(n
2
 )，其中 nn 是城市的数量。需要遍历矩阵 \textit{isConnected}isConnected 中的每个元素。

空间复杂度：O(n)O(n)，其中 nn 是城市的数量。需要使用数组 \textit{visited}visited 记录每个城市是否被访问过，数组长度是 nn，广度优先搜索使用的队列的元素个数不会超过 nn。

方法三：并查集
计算连通分量数的另一个方法是使用并查集。初始时，每个城市都属于不同的连通分量。遍历矩阵 \textit{isConnected}isConnected，如果两个城市之间有相连关系，则它们属于同一个连通分量，对它们进行合并。

遍历矩阵 \textit{isConnected}isConnected 的全部元素之后，计算连通分量的总数，即为省份的总数。

JavaJavaScriptC++GolangCPython3

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def find(index: int) -> int:
            if parent[index] != index:
                parent[index] = find(parent[index])
            return parent[index]

        def union(index1: int, index2: int):
            parent[find(index1)] = find(index2)

        provinces = len(isConnected)
        parent = list(range(provinces))

        for i in range(provinces):
            for j in range(i + 1, provinces):
                if isConnected[i][j] == 1:
                    union(i, j)

        circles = sum(parent[i] == i for i in range(provinces))
        return circles
复杂度分析

时间复杂度：O(n^2 \log n)O(n
2
 logn)，其中 nn 是城市的数量。需要遍历矩阵 \textit{isConnected}isConnected 中的所有元素，时间复杂度是 O(n^2)O(n
2
 )，如果遇到相连关系，则需要进行 22 次查找和最多 11 次合并，一共需要进行 2n^22n
2
  次查找和最多 n^2n
2
  次合并，因此总时间复杂度是 O(2n^2 \log n^2)=O(n^2 \log n)O(2n
2
 logn
2
 )=O(n
2
 logn)。这里的并查集使用了路径压缩，但是没有使用按秩合并，最坏情况下的时间复杂度是 O(n^2 \log n)O(n
2
 logn)，平均情况下的时间复杂度依然是 O(n^2 \alpha (n))O(n
2
 α(n))，其中 \alphaα 为阿克曼函数的反函数，\alpha (n)α(n) 可以认为是一个很小的常数。

空间复杂度：O(n)O(n)，其中 nn 是城市的数量。需要使用数组 \textit{parent}parent 记录每个城市所属的连通分量的祖先。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/number-of-provinces/solution/sheng-fen-shu-liang-by-leetcode-solution-eyk0/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
