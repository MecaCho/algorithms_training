'''
276. Paint Fence
There is a fence with n posts, each post can be painted with one of the k colors.

You have to paint all the posts such that no more than two adjacent fence posts have the same color.

Return the total number of ways you can paint the fence.

Note:
n and k are non-negative integers.

Example:

Input: n = 3, k = 2
Output: 6
Explanation: Take c1 as color 1, c2 as color 2. All possible ways are:

            post1  post2  post3
 -----      -----  -----  -----
   1         c1     c1     c2
   2         c1     c2     c1
   3         c1     c2     c2
   4         c2     c1     c1
   5         c2     c1     c2
   6         c2     c2     c1

276. 栅栏涂色
有 k 种颜色的涂料和一个包含 n 个栅栏柱的栅栏，每个栅栏柱可以用其中一种颜色进行上色。

你需要给所有栅栏柱上色，并且保证其中相邻的栅栏柱 最多连续两个 颜色相同。然后，返回所有有效涂色的方案数。

注意:
n 和 k 均为非负的整数。

示例:

输入: n = 3，k = 2
输出: 6
解析: 用 c1 表示颜色 1，c2 表示颜色 2，所有可能的涂色方案有:

            柱 1    柱 2   柱 3
 -----      -----  -----  -----
   1         c1     c1     c2
   2         c1     c2     c1
   3         c1     c2     c2
   4         c2     c1     c1
   5         c2     c1     c2
   6         c2     c2     c1
'''



class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n < 2:
            return k
        if n == 2:
            return k*k
        dp = [0, k, k*k]
        for i in range(3, n+1):
            dp.append((k-1)*(dp[i-1] + dp[i-2]))
        return dp[-1]

if __name__ == '__main__':
    demo = Solution()
    res = demo.numWays(9,2)
    print(res)

# tips
'''
本来应该是dp[n][k]这种二维形式的动规，其状态转移方程为:
dp[n][i]+=dp[n-1][j] 其中 j!=i 这里是和前一种有不一样的颜色
dp[n][i]+=dp[n-2][j] 其中 j!=i 这里是和前一种一样，那么就必须和前前面的一种不一样

然后我们发现对于第n个栅栏，涂颜色i时少加了dp[n-1][i]和dp[n-2][i]，所以涂所有的颜色时总的少加了sum[n-1]+sum[n-2]，其中sum[n]表示第n个栅栏总的合法图颜色总数
这样二维dp就成了一维

也就是sum[n]=(k-1)(sum[n-1]+sum[n-2])

'''
