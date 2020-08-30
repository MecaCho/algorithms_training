'''
841. Keys and Rooms
There are N rooms and you start in room 0.  Each room has a distinct number in 0, 1, 2, ..., N-1, and each room may have some keys to access the next room.

Formally, each room i has a list of keys rooms[i], and each key rooms[i][j] is an integer in [0, 1, ..., N-1] where N = rooms.length.  A key rooms[i][j] = v opens the room with number v.

Initially, all the rooms start locked (except for room 0).

You can walk back and forth between rooms freely.

Return true if and only if you can enter every room.

Example 1:

Input: [[1],[2],[3],[]]
Output: true
Explanation:
We start in room 0, and pick up key 1.
We then go to room 1, and pick up key 2.
We then go to room 2, and pick up key 3.
We then go to room 3.  Since we were able to go to every room, we return true.
Example 2:

Input: [[1,3],[3,0,1],[2],[0]]
Output: false
Explanation: We can't enter the room with number 2.
Note:

1 <= rooms.length <= 1000
0 <= rooms[i].length <= 1000
The number of keys in all rooms combined is at most 3000.

841. 钥匙和房间
有 N 个房间，开始时你位于 0 号房间。每个房间有不同的号码：0，1，2，...，N-1，并且房间里可能有一些钥匙能使你进入下一个房间。

在形式上，对于每个房间 i 都有一个钥匙列表 rooms[i]，每个钥匙 rooms[i][j] 由 [0,1，...，N-1] 中的一个整数表示，其中 N = rooms.length。 钥匙 rooms[i][j] = v 可以打开编号为 v 的房间。

最初，除 0 号房间外的其余所有房间都被锁住。

你可以自由地在房间之间来回走动。

如果能进入每个房间返回 true，否则返回 false。

示例 1：

输入: [[1],[2],[3],[]]
输出: true
解释:
我们从 0 号房间开始，拿到钥匙 1。
之后我们去 1 号房间，拿到钥匙 2。
然后我们去 2 号房间，拿到钥匙 3。
最后我们去了 3 号房间。
由于我们能够进入每个房间，我们返回 true。
示例 2：

输入：[[1,3],[3,0,1],[2],[0]]
输出：false
解释：我们不能进入 2 号房间。
提示：

1 <= rooms.length <= 1000
0 <= rooms[i].length <= 1000
所有房间中的钥匙数量总计不超过 3000。

'''


class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        visited = [0 for i in range(len(rooms))]

        def dfs(idx):
            if visited[idx]:
                return
            visited[idx] = 1
            for i in rooms[idx]:
                dfs(i)

        # print(visited)
        dfs(0)
        return sum(visited) == len(visited)


# solutions

'''
前言
当 xx 号房间中有 yy 号房间的钥匙时，我们就可以从 xx 号房间去往 yy 号房间。如果我们将这 nn 个房间看成有向图中的 nn 个节点，那么上述关系就可以看作是图中的 xx 号点到 yy 号点的一条有向边。

这样一来，问题就变成了给定一张有向图，询问从 00 号节点出发是否能够到达所有的节点。

方法一：深度优先搜索
思路及解法

我们可以使用深度优先搜索的方式遍历整张图，统计可以到达的节点个数，并利用数组 \textit{vis}vis 标记当前节点是否访问过，以防止重复访问。

代码

C++JavaCPython3Golang

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        def dfs(x: int):
            vis.add(x)
            nonlocal num
            num += 1
            for it in rooms[x]:
                if it not in vis:
                    dfs(it)
        
        n = len(rooms)
        num = 0
        vis = set()
        dfs(0)
        return num == n
复杂度分析

时间复杂度：O(n+m)O(n+m)，其中 nn 是房间的数量，mm 是所有房间中的钥匙数量的总数。

空间复杂度：O(n)O(n)，其中 nn 是房间的数量。主要为栈空间的开销。

方法二：广度优先搜索
思路及解法

我们也可以使用广度优先搜索的方式遍历整张图，统计可以到达的节点个数，并利用数组 \textit{vis}vis 标记当前节点是否访问过，以防止重复访问。

代码

C++JavaCPython3Golang

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        num = 0
        vis = {0}
        que = collections.deque([0])

        while que:
            x = que.popleft()
            num += 1
            for it in rooms[x]:
                if it not in vis:
                    vis.add(it)
                    que.append(it)
        
        return num == n
复杂度分析

时间复杂度：O(n+m)O(n+m)，其中 nn 是房间的数量，mm 是所有房间中的钥匙数量的总数。

空间复杂度：O(n)O(n)，其中 nn 是房间的数量。主要为队列的开销。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/keys-and-rooms/solution/yao-chi-he-fang-jian-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''