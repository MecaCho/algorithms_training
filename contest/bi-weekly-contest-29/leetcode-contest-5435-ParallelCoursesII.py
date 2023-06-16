# encoding=utf8

'''
1494. Parallel Courses II
Given the integer n representing the number of courses at some university labeled from 1 to n, and the array dependencies where dependencies[i] = [xi, yi]  represents a prerequisite relationship, that is, the course xi must be taken before the course yi.  Also, you are given the integer k.

In one semester you can take at most k courses as long as you have taken all the prerequisites for the courses you are taking.

Return the minimum number of semesters to take all courses. It is guaranteed that you can take all courses in some way.



Example 1:



Input: n = 4, dependencies = [[2,1],[3,1],[1,4]], k = 2
Output: 3
Explanation: The figure above represents the given graph. In this case we can take courses 2 and 3 in the first semester, then take course 1 in the second semester and finally take course 4 in the third semester.
Example 2:



Input: n = 5, dependencies = [[2,1],[3,1],[4,1],[1,5]], k = 2
Output: 4
Explanation: The figure above represents the given graph. In this case one optimal way to take all courses is: take courses 2 and 3 in the first semester and take course 4 in the second semester, then take course 1 in the third semester and finally take course 5 in the fourth semester.
Example 3:

Input: n = 11, dependencies = [], k = 2
Output: 6


Constraints:

1 <= n <= 15
1 <= k <= n
0 <= dependencies.length <= n * (n-1) / 2
dependencies[i].length == 2
1 <= xi, yi <= n
xi != yi
All prerequisite relationships are distinct, that is, dependencies[i] != dependencies[j].
The given graph is a directed acyclic graph.

1494. 并行课程 II
给你一个整数 n 表示某所大学里课程的数目，编号为 1 到 n ，数组 dependencies 中， dependencies[i] = [xi, yi]  表示一个先修课的关系，也就是课程 xi 必须在课程 yi 之前上。同时你还有一个整数 k 。

在一个学期中，你 最多 可以同时上 k 门课，前提是这些课的先修课在之前的学期里已经上过了。

请你返回上完所有课最少需要多少个学期。题目保证一定存在一种上完所有课的方式。



示例 1：



输入：n = 4, dependencies = [[2,1],[3,1],[1,4]], k = 2
输出：3
解释：上图展示了题目输入的图。在第一个学期中，我们可以上课程 2 和课程 3 。然后第二个学期上课程 1 ，第三个学期上课程 4 。
示例 2：



输入：n = 5, dependencies = [[2,1],[3,1],[4,1],[1,5]], k = 2
输出：4
解释：上图展示了题目输入的图。一个最优方案是：第一学期上课程 2 和 3，第二学期上课程 4 ，第三学期上课程 1 ，第四学期上课程 5 。
示例 3：

输入：n = 11, dependencies = [], k = 2
输出：6


提示：

1 <= n <= 15
1 <= k <= n
0 <= dependencies.length <= n * (n-1) / 2
dependencies[i].length == 2
1 <= xi, yi <= n
xi != yi
所有先修关系都是不同的，也就是说 dependencies[i] != dependencies[j] 。
题目输入的图是个有向无环图。
'''


import collections


class Solution(object):
    def minNumberOfSemesters(self, n, dependencies, k):
        """
        :type n: int
        :type dependencies: List[List[int]]
        :type k: int
        :rtype: int
        """
        graph = collections.defaultdict(list)
        in_degree = [0 for i in range(n+1)]
        out_degree = [0 for i in range(n+1)]

        for key, v in dependencies:
            graph[key].append(v)
            in_degree[v] += 1
            out_degree[key] += 1

        q = [i+1 for i in range(n) if in_degree[i+1]==0]
        q.sort(key=lambda x: -out_degree[x])

        res = 0
        visited = set()

        while q:
            q_len = len(q)

            q.sort(key=lambda x: -out_degree[x])
            for i in range(min(q_len, k)):
                node = q.pop(0)
                visited.add(node)

                for v in graph[node]:
                    in_degree[v] -= 1
                    if in_degree[v] == 0:
                        q.append(v)

            res += 1

        return res + (n - len(visited)) / k

