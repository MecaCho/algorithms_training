'''
279. 完全平方数
给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。

示例 1:

输入: n = 12
输出: 3 
解释: 12 = 4 + 4 + 4.
示例 2:

输入: n = 13
输出: 2
解释: 13 = 4 + 9.

279. Perfect Squares
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
'''



class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        import math
        sqrts = [i*i for i in range(1, int(math.sqrt(n)) + 1)]
        dp = [0]
        for i in range(1, n+1):
            dp.append(i)
            for sqrt_num in sqrts:
                if i - sqrt_num >= 0:
                    dp[i] = min(dp[i], dp[i-sqrt_num] + 1)
        return dp[n]

    
# golang solution

'''
func numSquares(n int) int {
	dp := make([]int, n+1)

	min := func(a, b int) int {
		if a < b {
			return a
		}
		return b
	}

	for i := 1; i <= n; i++ {
		dp[i] = i
		for k := 1; k*k <= i; k++ {
			dp[i] = min(dp[i-k*k]+1, dp[i])
		}
	}
	return dp[n]
}
'''
