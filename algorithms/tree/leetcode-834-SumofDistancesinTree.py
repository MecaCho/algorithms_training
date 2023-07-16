# encoding=utf8

'''
834. Sum of Distances in Tree
An undirected, connected tree with N nodes labelled 0...N-1 and N-1 edges are given.

The ith edge connects nodes edges[i][0] and edges[i][1] together.

Return a list ans, where ans[i] is the sum of the distances between node i and all other nodes.

Example 1:

Input: N = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
Output: [8,12,6,10,10,10]
Explanation:
Here is a diagram of the given tree:
  0
 / \
1   2
   /|\
  3 4 5
We can see that dist(0,1) + dist(0,2) + dist(0,3) + dist(0,4) + dist(0,5)
equals 1 + 1 + 2 + 2 + 2 = 8.  Hence, answer[0] = 8, and so on.
Note: 1 <= N <= 10000

834. 树中距离之和
给定一个无向、连通的树。树中有 N 个标记为 0...N-1 的节点以及 N-1 条边 。

第 i 条边连接节点 edges[i][0] 和 edges[i][1] 。

返回一个表示节点 i 与其他所有节点距离之和的列表 ans。

示例 1:

输入: N = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
输出: [8,12,6,10,10,10]
解释:
如下为给定的树的示意图：
  0
 / \
1   2
   /|\
  3 4 5

我们可以计算出 dist(0,1) + dist(0,2) + dist(0,3) + dist(0,4) + dist(0,5)
也就是 1 + 1 + 2 + 2 + 2 = 8。 因此，answer[0] = 8，以此类推。
说明: 1 <= N <= 10000
'''

import collections


class Solution(object):
    def sumOfDistancesInTree(self, N, edges):
        """
        :type N: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        tree = collections.defaultdict(set)
        res = [0] * N
        count = [1] * N
        for i, j in edges:
            tree[i].add(j)
            tree[j].add(i)

        def dfs(root, pre):
            for i in tree[root]:
                if i != pre:
                    dfs(i, root)
                    count[root] += count[i]
                    res[root] += res[i] + count[i]

        def dfs2(root, pre):
            for i in tree[root]:
                if i != pre:
                    res[i] = res[root] - count[i] + N - count[i]
                    dfs2(i, root)
        dfs(0, -1)
        dfs2(0, -1)
        return res


# solution

'''
Preword

Well, another long solution.
what I am always trying is to:

let you understand my solution (with my poor explanation)
prevent from reading my codes

Intuition

What if given a tree, with a certain root 0?
In O(N) we can find sum of distances in tree from root and all other nodes.
Now for all N nodes?
Of course, we can do it N times and solve it in O(N^2).
C++ and Java may get accepted luckily, but it's not what we want.

When we move our root from one node to its connected node,
one part of nodes get closer, one the other part get further.

If we know exactly how many nodes in both parts, we can solve this problem.

With one single traversal in tree, we should get enough information for it and
don't need to do it again and again.


Explanation

Let's solve it with node 0 as root.

Initial an array of hashset tree, tree[i] contains all connected nodes to i.
Initial an array count, count[i] counts all nodes in the subtree i.
Initial an array of res, res[i] counts sum of distance in subtree i.

Post order dfs traversal, update count and res:
count[root] = sum(count[i]) + 1
res[root] = sum(res[i]) + sum(count[i])

Pre order dfs traversal, update res:
When we move our root from parent to its child i, count[i] points get 1 closer to root, n - count[i] nodes get 1 futhur to root.
res[i] = res[root] - count[i] + N - count[i]

return res, done.


Time Complexity:

dfs: O(N) time
dfs2: O(N) time
'''
