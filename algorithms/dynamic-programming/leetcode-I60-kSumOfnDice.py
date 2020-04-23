
'''
面试题60. n个骰子的点数
把n个骰子扔在地上，所有骰子朝上一面的点数之和为s。输入n，打印出s的所有可能的值出现的概率。



你需要用一个浮点数数组返回答案，其中第 i 个元素代表这 n 个骰子所能掷出的点数集合中第 i 小的那个的概率。



示例 1:

输入: 1
输出: [0.16667,0.16667,0.16667,0.16667,0.16667,0.16667]
示例 2:

输入: 2
输出: [0.02778,0.05556,0.08333,0.11111,0.13889,0.16667,0.13889,0.11111,0.08333,0.05556,0.02778]


限制：

1 <= n <= 11
'''




class Solution(object):
    def twoSum(self, n):
        """
        :type n: int
        :rtype: List[float]
        """
        # f(n,s)=f(n-1,s-1)+f(n-1,s-2)+f(n-1,s-3)+f(n-1,s-4)+f(n-1,s-5)+f(n-1,s-6)
        # dp = [0, 1,1,1,1,1,1]
        # # dp = [[1 for i in range(6)] for j i range(n)]
        # # for i in range(n, 6*n+1):
        # for k in range(6*n, 6*n):
        #     dp.append(0)
        #     for j in range(6):
        #         if n - j:

        #         dp[k] += dp[k-j]
        self.hash_map = [[None for j in range(6*n+1)] for i in range(n+1)]
        def get_count(n, k):
            if k > 6*n or k < n:
                return 0
            if n <= 1:
                return 1
            tmp = self.hash_map[n][k]
            if tmp is not None:
                return tmp
            count = 0
            for i in range(1, 7, 1):
                count += get_count(n-1, k-i)
            self.hash_map[n][k] = count
            return count

        dp = [1 for _ in range(n)]
        for i in range(n, 6*n+1):
            dp.append(1)
            dp[i] = get_count(n, i)

        res = []
        for i in range(n, 6*n+1):
            res.append(dp[i]*(float(1)/6**n))
        return res
