# encoding=utf8

'''
3600. Maximize Spanning Tree Stability with Upgrades

You are given an integer n, representing n nodes numbered from 0 to n - 1 and a list of edges, where edges[i] = [ui, vi, si, musti]:

    ui and vi indicates an undirected edge between nodes ui and vi.
    si is the strength of the edge.
    musti is an integer (0 or 1). If musti == 1, the edge must be included in the spanning tree. These edges cannot be upgraded.

You are also given an integer k, the maximum number of upgrades you can perform. Each upgrade doubles the strength of an edge, and each eligible edge (with musti == 0) can be upgraded at most once.

The stability of a spanning tree is defined as the minimum strength score among all edges included in it.

Return the maximum possible stability of any valid spanning tree. If it is impossible to connect all nodes, return -1.

Note: A spanning tree of a graph with n nodes is a subset of the edges that connects all nodes together (i.e. the graph is connected) without forming any cycles, and uses exactly n - 1 edges.

 

Example 1:

Input: n = 3, edges = [[0,1,2,1],[1,2,3,0]], k = 1

Output: 2

Explanation:

    Edge [0,1] with strength = 2 must be included in the spanning tree.
    Edge [1,2] is optional and can be upgraded from 3 to 6 using one upgrade.
    The resulting spanning tree includes these two edges with strengths 2 and 6.
    The minimum strength in the spanning tree is 2, which is the maximum possible stability.

Example 2:

Input: n = 3, edges = [[0,1,4,0],[1,2,3,0],[0,2,1,0]], k = 2

Output: 6

Explanation:

    Since all edges are optional and up to k = 2 upgrades are allowed.
    Upgrade edges [0,1] from 4 to 8 and [1,2] from 3 to 6.
    The resulting spanning tree includes these two edges with strengths 8 and 6.
    The minimum strength in the tree is 6, which is the maximum possible stability.

Example 3:

Input: n = 3, edges = [[0,1,1,1],[1,2,1,1],[2,0,1,1]], k = 0

Output: -1

Explanation:

    All edges are mandatory and form a cycle, which violates the spanning tree property of acyclicity. Thus, the answer is -1.

 

Constraints:

    2 <= n <= 105
    1 <= edges.length <= 105
    edges[i] = [ui, vi, si, musti]
    0 <= ui, vi < n
    ui != vi
    1 <= si <= 105
    musti is either 0 or 1.
    0 <= k <= n
    There are no duplicate edges.
'''

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.components = n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        
        if rootX == rootY:
            return False
        
        if self.rank[rootX] < self.rank[rootY]:
            self.parent[rootX] = rootY
        elif self.rank[rootX] > self.rank[rootY]:
            self.parent[rootY] = rootX
        else:
            self.parent[rootY] = rootX
            self.rank[rootX] += 1
        
        self.components -= 1
        return True

class Solution:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        # Separate edges for easier handling if needed, but we can filter on the fly
        # Determine the search range for binary search
        # Minimum possible strength is 1, maximum is 2 * 10^5
        low = 1
        high = 2 * 10**5 
        ans = -1
        
        # Pre-check connectivity with all edges (ignoring weights) to quickly return -1 if impossible?
        # Not strictly necessary as the binary search will handle it, but good for optimization.
        # However, the mandatory cycle constraint is specific.
        
        def can_achieve(target):
            uf = UnionFind(n)
            upgrades_used = 0
            edges_count = 0
            
            # 1. Process Mandatory Edges
            for u, v, s, must in edges:
                if must == 1:
                    if s < target:
                        return False # Mandatory edge too weak and cannot be upgraded
                    if not uf.union(u, v):
                        return False # Cycle detected among mandatory edges
                    edges_count += 1
            
            # 2. Prepare Optional Edges
            optional_no_upgrade = []
            optional_need_upgrade = []
            
            for u, v, s, must in edges:
                if must == 0:
                    if s >= target:
                        optional_no_upgrade.append((u, v))
                    elif 2 * s >= target:
                        optional_need_upgrade.append((u, v))
                    # else: edge is too weak even with upgrade
            
            # 3. Greedily add optional edges without upgrade
            for u, v in optional_no_upgrade:
                if uf.union(u, v):
                    edges_count += 1
            
            # 4. Greedily add optional edges with upgrade
            for u, v in optional_need_upgrade:
                if uf.union(u, v):
                    edges_count += 1
                    upgrades_used += 1
                    if upgrades_used > k:
                        # We exceeded budget, but maybe we already formed a tree?
                        # No, we need to finish connecting. If we exceed k before finishing, it's fail.
                        # But wait, we might have finished connecting before this specific edge.
                        # The check should be after the loop or carefully inside.
                        # Actually, if we increment and it becomes > k, we can't use this edge.
                        # But maybe we don't need this edge if the tree is already complete.
                        # The condition "if uf.union" ensures we only count necessary edges.
                        # So if we are here, we needed this edge to connect components.
                        # Thus, if upgrades_used > k, we fail.
                        pass 
            
            if upgrades_used > k:
                return False
                
            # Check if full spanning tree is formed (n-1 edges)
            # Alternatively check uf.components == 1
            if edges_count == n - 1:
                return True
            
            return False

        while low <= high:
            mid = (low + high) // 2
            if can_achieve(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
                
        return ans

