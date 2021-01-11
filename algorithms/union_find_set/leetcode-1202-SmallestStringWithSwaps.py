# encoding=utf8

'''
1202. Smallest String With Swaps
You are given a string s, and an array of pairs of indices in the string pairs where pairs[i] = [a, b] indicates 2 indices(0-indexed) of the string.

You can swap the characters at any pair of indices in the given pairs any number of times.

Return the lexicographically smallest string that s can be changed to after using the swaps.



Example 1:

Input: s = "dcab", pairs = [[0,3],[1,2]]
Output: "bacd"
Explaination:
Swap s[0] and s[3], s = "bcad"
Swap s[1] and s[2], s = "bacd"
Example 2:

Input: s = "dcab", pairs = [[0,3],[1,2],[0,2]]
Output: "abcd"
Explaination:
Swap s[0] and s[3], s = "bcad"
Swap s[0] and s[2], s = "acbd"
Swap s[1] and s[2], s = "abcd"
Example 3:

Input: s = "cba", pairs = [[0,1],[1,2]]
Output: "abc"
Explaination:
Swap s[0] and s[1], s = "bca"
Swap s[1] and s[2], s = "bac"
Swap s[0] and s[1], s = "abc"


Constraints:

1 <= s.length <= 10^5
0 <= pairs.length <= 10^5
0 <= pairs[i][0], pairs[i][1] < s.length
s only contains lower case English letters.

1202. 交换字符串中的元素
给你一个字符串 s，以及该字符串中的一些「索引对」数组 pairs，其中 pairs[i] = [a, b] 表示字符串中的两个索引（编号从 0 开始）。

你可以 任意多次交换 在 pairs 中任意一对索引处的字符。

返回在经过若干次交换后，s 可以变成的按字典序最小的字符串。



示例 1:

输入：s = "dcab", pairs = [[0,3],[1,2]]
输出："bacd"
解释：
交换 s[0] 和 s[3], s = "bcad"
交换 s[1] 和 s[2], s = "bacd"
示例 2：

输入：s = "dcab", pairs = [[0,3],[1,2],[0,2]]
输出："abcd"
解释：
交换 s[0] 和 s[3], s = "bcad"
交换 s[0] 和 s[2], s = "acbd"
交换 s[1] 和 s[2], s = "abcd"
示例 3：

输入：s = "cba", pairs = [[0,1],[1,2]]
输出："abc"
解释：
交换 s[0] 和 s[1], s = "bca"
交换 s[1] 和 s[2], s = "bac"
交换 s[0] 和 s[1], s = "abc"


提示：

1 <= s.length <= 10^5
0 <= pairs.length <= 10^5
0 <= pairs[i][0], pairs[i][1] < s.length
s 中只含有小写英文字母
'''


class Solution(object):
    def smallestStringWithSwaps(self, s, pairs):
        """
        :type s: str
        :type pairs: List[List[int]]
        :rtype: str
        """
        # 建图
        graph = [[] for _ in range(len(s))]
        visited = [0] * len(s)
        for x, y in pairs:
            graph[x].append(y)
            graph[y].append(x)

        res = list(s)
        for i in range(len(s)):
            if not visited[i]:
                # 获取连通节点
                connected_nodes = []
                self.dfs(connected_nodes, graph, visited, i)
                # 重新赋值
                indices = sorted(connected_nodes)
                string = sorted(res[node] for node in connected_nodes)
                for j, ch in zip(indices, string):
                    res[j] = ch

        return "".join(res)

    def dfs(self, res, graph, visited, x):
        for neighbor in graph[x]:
            if not visited[neighbor]:
                visited[neighbor] = 1
                res.append(neighbor)
                self.dfs(res, graph, visited, neighbor)


# solutions

'''
前言
近 6 天的第三道并查集题目，对于连通性问题，图的三种常用解法都适用，今天来做一个比较。

思路
根据题目描述，我们可以任意次交换pairs中任意一对索引处的字符，也就是说pairs中任意一对索引是相互连通的，于是联想到连通性问题。

我们就可以找出每一块连通分量的所有字符，排序后再放回原来的字符串，就是最后的答案。

三种解法的不同点就在于如何找到每一块连通分量，其余部分基本相同。

方法一 深度优先搜索 DFS
我们首先根据pairs对索引建图，可以用字典也可以用数组。然后采用DFS获取每一块连通分量的索引，再排序赋值即可。

python

class Solution:
    def dfs(self,res,graph,visited,x):
        for neighbor in graph[x]:
            if not visited[neighbor]:
                visited[neighbor] = 1
                res.append(neighbor)
                self.dfs(res,graph,visited,neighbor)
    
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        # 建图
        graph = [[] for _ in range(len(s))]
        visited = [0] * len(s)
        for x,y in pairs:
            graph[x].append(y)
            graph[y].append(x)
        
        res = list(s)
        for i in range(len(s)):
            if not visited[i]:
                # 获取连通节点
                connected_nodes = []
                self.dfs(connected_nodes,graph,visited,i)
                # 重新赋值
                indices = sorted(connected_nodes)
                string = sorted(res[node] for node in connected_nodes)
                for j,ch in zip(indices,string):
                    res[j] = ch
            
        return "".join(res)
方法二 宽度优先搜索 BFS
把DFS的部分换成BFS即可。

python

class Solution:
    def bfs(self,res,graph,visited,x):
        queue = collections.deque([x])
        visited[x] = 1
        res.append(x)
        
        while queue:
            cur_node = queue.popleft()
            for neighbor in graph[cur_node]:
                if visited[neighbor]:
                    continue
                visited[neighbor] = 1
                res.append(neighbor)
                queue.append(neighbor)
    
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        # 建图
        graph = [[] for _ in range(len(s))]
        visited = [0] * len(s)
        for x,y in pairs:
            graph[x].append(y)
            graph[y].append(x)
        
        res = list(s)
        for i in range(len(s)):
            if not visited[i]:
                # 获取联通节点
                connected_nodes = []
                self.bfs(connected_nodes,graph,visited,i)
                # 重新赋值
                indices = sorted(connected_nodes)
                string = sorted(res[node] for node in connected_nodes)
                for j,ch in zip(indices,string):
                    res[j] = ch
            
        return "".join(res)
方法三 并查集
还是先建图，不过这里跟之前的不一样，用的是合并节点的方法。后面相同。
有关并查集的详细解释和代码模板可以参考这篇题解，多图详解并查集。

python

class UnionFind:
    def __init__(self,s):
        self.father = {i:i for i in range(len(s))}
        
    def find(self,x):
        root = x
        
        while self.father[root] != root:
            root = self.father[root]
        
        # 路径压缩
        while x != root:
            original_father = self.father[x]
            self.father[x] = root
            x = original_father
        
        return root
    
    def merge(self,x,y):
        root_x,root_y = self.find(x),self.find(y)
        
        if root_x != root_y:
            self.father[root_x] = root_y
            

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        # 并查集建图
        uf = UnionFind(s)
        for x,y in pairs:
            uf.merge(x,y)
        # 获取联通节点
        connected_components = collections.defaultdict(list)
        for node in range(len(s)):
            connected_components[uf.find(node)].append(node)
        
        res = list(s)
        # 重新赋值
        for nodes in connected_components.values():
            indices = nodes
            string = sorted(res[node] for node in nodes)
            for i,ch in zip(indices,string):
                res[i] = ch
        return "".join(res)
效率表现
时间：BFS 优于 DFS 优于 并查集。这道题目因为不是在线的场景，并查集 的优势并没有体现出来。
空间：BFS 基本等于 并查集，但优于 DFS。这是因为 DFS 有额外的递归开销。

作者：MiloMusiala
链接：https://leetcode-cn.com/problems/smallest-string-with-swaps/solution/python-bing-cha-ji-dfsbfssan-chong-jie-f-yy89/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
