'''
207. 课程表
你这个学期必须选修 numCourse 门课程，记为 0 到 numCourse-1 。

在选修某些课程之前需要一些先修课程。 例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们：[0,1]

给定课程总量以及它们的先决条件，请你判断是否可能完成所有课程的学习？



示例 1:

输入: 2, [[1,0]]
输出: true
解释: 总共有 2 门课程。学习课程 1 之前，你需要完成课程 0。所以这是可能的。
示例 2:

输入: 2, [[1,0],[0,1]]
输出: false
解释: 总共有 2 门课程。学习课程 1 之前，你需要先完成​课程 0；并且学习课程 0 之前，你还应先完成课程 1。这是不可能的。


提示：

输入的先决条件是由 边缘列表 表示的图形，而不是 邻接矩阵 。详情请参见图的表示法。
你可以假定输入的先决条件中没有重复的边。
1 <= numCourses <= 10^5

207. Course Schedule
There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?



Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.


Constraints:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
1 <= numCourses <= 10^5
'''

import collections


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        edges = collections.defaultdict(list)

        for i in range(len(prerequisites)):
            info = prerequisites[i]
            edges[info[1]].append(info[0])

        self.res = []
        self.invalid = False
        visited = [0 for _ in range(numCourses)]

        def dfs(u):
            visited[u] = 1
            for v in edges[u]:
                if visited[v] == 0:
                    dfs(v)
                    if self.invalid:
                        return
                elif visited[v] == 1:
                    self.invalid = True
                    return
            visited[u] = 2
            self.res.append(u)


        for i in range(numCourses):
            if not visited[i] and not self.invalid:
                dfs(i)
            if self.invalid:
                return False

        return True


class Solution1(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = collections.defaultdict(list)
        in_degree = [0 for _ in range(numCourses)]
        for k, v in prerequisites:
            graph[v].append(k)
            in_degree[k] += 1

        q = [i for i in range(len(in_degree)) if in_degree[i] == 0]

        count = 0

        while q:
            node = q.pop(0)

            for v in graph[node]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    q.append(v)
            count += 1

        return count == numCourses

# tips

'''
This problem is equivalent to finding if a cycle exists in a directed graph. If a cycle exists, no topological ordering exists and therefore it will be impossible to take all courses.

Topological Sort via DFS - A great video tutorial (21 minutes) on Coursera explaining the basic concepts of Topological Sort.

Topological sort could also be done via BFS.
'''


'''
解题思路：
本题可约化为： 课程安排图是否是 有向无环图(DAG)。即课程间规定了前置条件，但不能构成任何环路，否则课程前置条件将不成立。
思路是通过 拓扑排序 判断此课程安排图是否是 有向无环图(DAG) 。 拓扑排序原理： 对 DAG 的顶点进行排序，使得对每一条有向边 (u, v)(u,v)，均有 uu（在排序记录中）比 vv 先出现。亦可理解为对某点 vv 而言，只有当 vv 的所有源点均出现了，vv 才能出现。
通过课程前置条件列表 prerequisites 可以得到课程安排图的 邻接表 adjacency，以降低算法时间复杂度，以下两种方法都会用到邻接表。
方法一：入度表（广度优先遍历）
算法流程：
统计课程安排图中每个节点的入度，生成 入度表 indegrees。
借助一个队列 queue，将所有入度为 00 的节点入队。
当 queue 非空时，依次将队首节点出队，在课程安排图中删除此节点 pre：
并不是真正从邻接表中删除此节点 pre，而是将此节点对应所有邻接节点 cur 的入度 -1−1，即 indegrees[cur] -= 1。
当入度 -1−1后邻接节点 cur 的入度为 00，说明 cur 所有的前驱节点已经被 “删除”，此时将 cur 入队。
在每次 pre 出队时，执行 numCourses--；
若整个课程安排图是有向无环图（即可以安排），则所有节点一定都入队并出队过，即完成拓扑排序。换个角度说，若课程安排图中存在环，一定有节点的入度始终不为 00。
因此，拓扑排序出队次数等于课程个数，返回 numCourses == 0 判断课程是否可以成功安排。
复杂度分析：
时间复杂度 O(N + M)O(N+M)： 遍历一个图需要访问所有节点和所有临边，NN 和 MM 分别为节点数量和临边数量；
空间复杂度 O(N + M)O(N+M)： 为建立邻接表所需额外空间，adjacency 长度为 NN ，并存储 MM 条临边的数据。

代码：
python
from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegrees = [0 for _ in range(numCourses)]
        adjacency = [[] for _ in range(numCourses)]
        queue = deque()
        # Get the indegree and adjacency of every course.
        for cur, pre in prerequisites:
            indegrees[cur] += 1
            adjacency[pre].append(cur)
        # Get all the courses with the indegree of 0.
        for i in range(len(indegrees)):
            if not indegrees[i]: queue.append(i)
        # BFS TopSort.
        while queue:
            pre = queue.popleft()
            numCourses -= 1
            for cur in adjacency[pre]:
                indegrees[cur] -= 1
                if not indegrees[cur]: queue.append(cur)
        return not numCourses
方法二：深度优先遍历
原理是通过 DFS 判断图中是否有环。

算法流程：
借助一个标志列表 flags，用于判断每个节点 i （课程）的状态：
未被 DFS 访问：i == 0；
已被其他节点启动的 DFS 访问：i == -1；
已被当前节点启动的 DFS 访问：i == 1。
对 numCourses 个节点依次执行 DFS，判断每个节点起步 DFS 是否存在环，若存在环直接返回 FalseFalse。DFS 流程；
终止条件：
当 flag[i] == -1，说明当前访问节点已被其他节点启动的 DFS 访问，无需再重复搜索，直接返回 TrueTrue。
当 flag[i] == 1，说明在本轮 DFS 搜索中节点 i 被第 22 次访问，即 课程安排图有环 ，直接返回 FalseFalse。
将当前访问节点 i 对应 flag[i] 置 11，即标记其被本轮 DFS 访问过；
递归访问当前节点 i 的所有邻接节点 j，当发现环直接返回 FalseFalse；
当前节点所有邻接节点已被遍历，并没有发现环，则将当前节点 flag 置为 -1−1 并返回 TrueTrue。
若整个图 DFS 结束并未发现环，返回 TrueTrue。
复杂度分析：
时间复杂度 O(N + M)O(N+M)： 遍历一个图需要访问所有节点和所有临边，NN 和 MM 分别为节点数量和临边数量；
空间复杂度 O(N + M)O(N+M)： 为建立邻接表所需额外空间，adjacency 长度为 NN ，并存储 MM 条临边的数据。

1 / 10

代码：
python
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(i, adjacency, flags):
            if flags[i] == -1: return True
            if flags[i] == 1: return False
            flags[i] = 1
            for j in adjacency[i]:
                if not dfs(j, adjacency, flags): return False
            flags[i] = -1
            return True

        adjacency = [[] for _ in range(numCourses)]
        flags = [0 for _ in range(numCourses)]
        for cur, pre in prerequisites:
            adjacency[pre].append(cur)
        for i in range(numCourses):
            if not dfs(i, adjacency, flags): return False
        return True

'''