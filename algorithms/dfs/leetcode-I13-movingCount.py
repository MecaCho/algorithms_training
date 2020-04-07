

'''
面试题13. 机器人的运动范围
地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。一个机器人从坐标 [0, 0] 的格子开始移动，它每次可以向左、右、上、下移动一格（不能移动到方格外），也不能进入行坐标和列坐标的数位之和大于k的格子。例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。但它不能进入方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？

 

示例 1：

输入：m = 2, n = 3, k = 1
输出：3
示例 1：

输入：m = 3, n = 1, k = 0
输出：1
提示：

1 <= n,m <= 100
0 <= k <= 20
'''






class Solution(object):
    def movingCount(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        def check_sum(n):
            res = 0
            while n:
                res += n % 10
                n /= 10
            return res
        visted = [(0, 0)]
        for i in range(m):
            for j in range(n):
                if check_sum(i) + check_sum(j) <= k and ((i-1, j) in visted or (i, j-1) in visted):
                    visted.append((i, j))
                    # count += 1
        return len(visted)


class Solution1(object):
    def movingCount(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        def check_sum(n):
            res = 0
            while n:
                res += n % 10
                n /= 10
            return res
        def dfs(i, j):
            if i >= m or j >= n or check_sum(i)+check_sum(j) > k:
                return
            visted.append((i, j))
            dfs(i, j+1)
            dfs(i+1, j)
        visted = [(0, 0)]
        dfs(0,0)
        return len(visted)