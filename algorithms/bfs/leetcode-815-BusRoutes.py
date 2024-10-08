# encoding=utf8

'''
815. Bus Routes

You are given an array routes representing bus routes where routes[i] is a bus route that the ith bus repeats forever.

For example, if routes[0] = [1, 5, 7], this means that the 0th bus travels in the sequence 1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1 -> ... forever.
You will start at the bus stop source (You are not on any bus initially), and you want to go to the bus stop target. You can travel between bus stops by buses only.

Return the least number of buses you must take to travel from source to target. Return -1 if it is not possible.

 

Example 1:

Input: routes = [[1,2,7],[3,6,7]], source = 1, target = 6
Output: 2
Explanation: The best strategy is take the first bus to the bus stop 7, then take the second bus to the bus stop 6.
Example 2:

Input: routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]], source = 15, target = 12
Output: -1
 

Constraints:

1 <= routes.length <= 500.
1 <= routes[i].length <= 105
All the values of routes[i] are unique.
sum(routes[i].length) <= 105
0 <= routes[i][j] < 106
0 <= source, target < 106


815. 公交路线

给你一个数组 routes ，表示一系列公交线路，其中每个 routes[i] 表示一条公交线路，第 i 辆公交车将会在上面循环行驶。

例如，路线 routes[0] = [1, 5, 7] 表示第 0 辆公交车会一直按序列 1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1 -> ... 这样的车站路线行驶。
现在从 source 车站出发（初始时不在公交车上），要前往 target 车站。 期间仅可乘坐公交车。

求出 最少乘坐的公交车数量 。如果不可能到达终点车站，返回 -1 。

 

示例 1：

输入：routes = [[1,2,7],[3,6,7]], source = 1, target = 6
输出：2
解释：最优策略是先乘坐第一辆公交车到达车站 7 , 然后换乘第二辆公交车到车站 6 。 
示例 2：

输入：routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]], source = 15, target = 12
输出：-1
 

提示：

1 <= routes.length <= 500.
1 <= routes[i].length <= 105
routes[i] 中的所有值 互不相同
sum(routes[i].length) <= 105
0 <= routes[i][j] < 106
0 <= source, target < 106
'''


class Solution(object):
    def numBusesToDestination(self, routes, source, target):
        """
        :type routes: List[List[int]]
        :type source: int
        :type target: int
        :rtype: int
        """
        # djikstra
        egges = collections.defaultdict(list)
        for id, route in enumerate(routes):
            for i in range(len(route)-1):
                egges[route[i]].append((id, route[i+1]))
                egges[route[i+1]].append((id, route[i]))

        visted = set()
        q = [(0, source, -1)]
        while q:
            d, local, id = heapq.heappop(q)
            if (local, id) in visted:
                continue
            if local == target:
                return d
            visted.add((local, id))
            for route_id, v in egges[local]:
                heapq.heappush(q, (d+(0 if id == route_id else 1), v, route_id))

        return -1


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:

        stop_to_buses = defaultdict(list)
        for i, route in enumerate(routes):
            for x in route:
                stop_to_buses[x].append(i)


        if source not in stop_to_buses or target not in stop_to_buses:

            return -1 if source != target else 0

        # BFS
        dis = {source: 0}
        q = deque([source])
        while q:
            x = q.popleft()  # 当前在车站 x
            dis_x = dis[x]
            for i in stop_to_buses[x]:  # 遍历所有经过车站 x 的公交车 i
                if routes[i]:
                    for y in routes[i]:  # 遍历公交车 i 的路线
                        if y not in dis:  # 没有访问过车站 y
                            dis[y] = dis_x + 1  # 从 x 站上车然后在 y 站下车
                            q.append(y)
                    routes[i] = None  # 标记 routes[i] 遍历过

        return dis.get(target, -1)
