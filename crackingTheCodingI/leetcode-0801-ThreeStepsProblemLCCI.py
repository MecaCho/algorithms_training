'''
面试题 08.01. 三步问题
三步问题。有个小孩正在上楼梯，楼梯有n阶台阶，小孩一次可以上1阶、2阶或3阶。实现一种方法，计算小孩有多少种上楼梯的方式。结果可能很大，你需要对结果模1000000007。

示例1:

 输入：n = 3 
 输出：4
 说明: 有四种走法
示例2:

 输入：n = 5
 输出：13
提示:

n范围在[1, 1000000]之间


面试题 08.01. Three Steps Problem LCCI
A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3 steps at a time. Implement a method to count how many possible ways the child can run up the stairs. The result may be large, so return it modulo 1000000007.

Example1:

 Input: n = 3 
 Output: 4
Example2:

 Input: n = 5
 Output: 13
Note:

1 <= n <= 1000000
'''



class Solution(object):
    def waysToStep(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1, 2, 4]
        for i in range(3, n):
            res = (dp[i-1] + dp[i-2] + dp[i-3]) % 1000000007
            dp.append(res)
        return dp[n-1] % 1000000007
