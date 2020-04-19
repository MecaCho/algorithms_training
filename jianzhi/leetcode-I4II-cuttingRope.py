'''

'''


class Solution(object):
    def cuttingRope(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1 for i in range(n+1)]

        for i in range(1, n+1):
            for j in range(1, i):
                dp[i] = max(dp[i], dp[i-j]*j, (i-j)*j)
        # print(dp)
        return dp[-1] % 1000000007