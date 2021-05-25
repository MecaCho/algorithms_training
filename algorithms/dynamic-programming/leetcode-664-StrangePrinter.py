# encoding=utf8



'''
664. Strange Printer

There is a strange printer with the following two special properties:

The printer can only print a sequence of the same character each time.
At each turn, the printer can print new characters starting from and ending at any place and will cover the original existing characters.
Given a string s, return the minimum number of turns the printer needed to print it.

 

Example 1:

Input: s = "aaabbb"
Output: 2
Explanation: Print "aaa" first and then print "bbb".
Example 2:

Input: s = "aba"
Output: 2
Explanation: Print "aaa" first and then print "b" from the second place of the string, which will cover the existing character 'a'.
 

Constraints:

1 <= s.length <= 100
s consists of lowercase English letters.


664. 奇怪的打印机

有台奇怪的打印机有以下两个特殊要求：

打印机每次只能打印由 同一个字符 组成的序列。
每次可以在任意起始和结束位置打印新字符，并且会覆盖掉原来已有的字符。
给你一个字符串 s ，你的任务是计算这个打印机打印它需要的最少打印次数。

 
示例 1：

输入：s = "aaabbb"
输出：2
解释：首先打印 "aaa" 然后打印 "bbb"。
示例 2：

输入：s = "aba"
输出：2
解释：首先打印 "aaa" 然后在第二个位置打印 "b" 覆盖掉原来的字符 'a'。
 

提示：

1 <= s.length <= 100
s 由小写英文字母组成
'''


class Solution(object):
    def strangePrinter(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [[1 if i==j else float("inf") for i in range(n)] for j in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i][j-1]
                else:
                    for k in range(i, j):
                        dp[i][j] = min(dp[i][j], dp[i][k]+dp[k+1][j])

        return dp[0][n-1]
       
# golang solution

'''go
func strangePrinter(s string) int {
	n := len(s)
	dp := make([][]int, n)
	for i := 0; i < n; i++ {
		dp[i] = make([]int, n)
	}
	min := func(a, b int) int {
		if a < b {
			return a
		}
		return b
	}
	for i := n - 1; i >= 0; i-- {
		dp[i][i] = 1
		for j := i + 1; j < n; j++ {
			dp[i][j] = math.MaxInt32
			dp[j][j] = 1
			if s[i] == s[j] {
				dp[i][j] = dp[i][j-1]
			} else {
				for k := i; k < j; k++ {
					dp[i][j] = min(dp[i][j], dp[i][k]+dp[k+1][j])
				}
			}
		}
	}

	return dp[0][n-1]
}
'''
       
# solutions

'''
方法一：动态规划
思路及算法

我们可以使用动态规划解决本题，令 f[i][j]f[i][j] 表示打印完成区间 [i,j][i,j] 的最少操作数。

当我们尝试计算出 f[i][j]f[i][j] 时，需要考虑两种情况：

s[i]=s[j]s[i]=s[j]，即区间两端的字符相同，那么当我们打印左侧字符 s[i]s[i] 时，可以顺便打印右侧字符 s[j]s[j]，这样我们即可忽略右侧字符对该区间的影响，只需要考虑如何尽快打印完区间 [i,j-1][i,j−1] 即可，即此时有 f[i][j]=f[i][j-1]f[i][j]=f[i][j−1]。
我们无需关心区间 [i,j-1][i,j−1] 的具体打印方案，因为我们总可以第一步完成 s[i]s[i] 的打印，此时可以顺便完成 s[j]s[j] 的打印，不会影响打印完成区间 [i,j-1][i,j−1] 的最少操作数。
s[i] \neq s[j]s[i] 

​	
 =s[j]，即区间两端的字符不同，那么我们需要分别完成该区间的左右两部分的打印。我们记两部分分别为区间 [i,k][i,k] 和区间 [k+1,j][k+1,j]（其中 i \leq k < ji≤k<j），此时 f[i][j]=\min_{k=i}^{j-1}{f[i][k]+f[k+1][j]}f[i][j]=min 
k=i
j−1
​	
 f[i][k]+f[k+1][j]。
总结状态转移方程为：

dp[i][j] = dp[i][j-1] (s[i] == s[j])
dp[i][j] = min(dp[i][j], dp[i][k]+dp[k+1][j]) (s[i] != s[j],k in range(i, j))


边界条件为 f[i][i]=1f[i][i]=1，对于长度为 11 的区间，需要打印 11 次。最后的答案为 f[0][n-1]f[0][n−1]。

注意到 f[i][j]f[i][j] 的计算需要用到 f[i][k]f[i][k] 和 f[k+1][j]f[k+1][j]（其中 i\leq k< ji≤k<j）。为了保证动态规划的计算过程满足无后效性，在实际代码中，我们需要改变动态规划的计算顺序，从大到小地枚举 ii，并从小到大地枚举 jj，这样可以保证当计算 f[i][j]f[i][j] 时，f[i][k]f[i][k] 和 f[k+1][j]f[k+1][j] 都已经被计算过。

代码

C++JavaC#JavaScriptGolangC

func strangePrinter(s string) int {
    n := len(s)
    f := make([][]int, n)
    for i := range f {
        f[i] = make([]int, n)
    }
    for i := n - 1; i >= 0; i-- {
        f[i][i] = 1
        for j := i + 1; j < n; j++ {
            if s[i] == s[j] {
                f[i][j] = f[i][j-1]
            } else {
                f[i][j] = math.MaxInt64
                for k := i; k < j; k++ {
                    f[i][j] = min(f[i][j], f[i][k]+f[k+1][j])
                }
            }
        }
    }
    return f[0][n-1]
}

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}
复杂度分析

时间复杂度：O(n^3)O(n3)，其中 nn 是字符串的长度。

空间复杂度：O(n^2)O(n2)，其中 nn 是字符串的长度。我们需要保存所有 n^2n2个状态。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/strange-printer/solution/qi-guai-de-da-yin-ji-by-leetcode-solutio-ogbu/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''

