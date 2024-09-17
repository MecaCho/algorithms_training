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

