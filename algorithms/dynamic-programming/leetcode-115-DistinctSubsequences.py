# encoding=utf8


'''
115. Distinct Subsequences
Given two strings s and t, return the number of distinct subsequences of s which equals t.

A string's subsequence is a new string formed from the original string by deleting some (can be none) of the characters without disturbing the remaining characters' relative positions. (i.e., "ACE" is a subsequence of "ABCDE" while "AEC" is not).

It is guaranteed the answer fits on a 32-bit signed integer.



Example 1:

Input: s = "rabbbit", t = "rabbit"
Output: 3
Explanation:
As shown below, there are 3 ways you can generate "rabbit" from S.
rabbbit
rabbbit
rabbbit
Example 2:

Input: s = "babgbag", t = "bag"
Output: 5
Explanation:
As shown below, there are 5 ways you can generate "bag" from S.
babgbag
babgbag
babgbag
babgbag
babgbag


Constraints:

0 <= s.length, t.length <= 1000
s and t consist of English letters.


115. 不同的子序列
给定一个字符串 s 和一个字符串 t ，计算在 s 的子序列中 t 出现的个数。

字符串的一个 子序列 是指，通过删除一些（也可以不删除）字符且不干扰剩余字符相对位置所组成的新字符串。（例如，"ACE" 是 "ABCDE" 的一个子序列，而 "AEC" 不是）

题目数据保证答案符合 32 位带符号整数范围。



示例 1：

输入：s = "rabbbit", t = "rabbit"
输出：3
解释：
如下图所示, 有 3 种可以从 s 中得到 "rabbit" 的方案。
(上箭头符号 ^ 表示选取的字母)
rabbbit
^^^^ ^^
rabbbit
^^ ^^^^
rabbbit
^^^ ^^^
示例 2：

输入：s = "babgbag", t = "bag"
输出：5
解释：
如下图所示, 有 5 种可以从 s 中得到 "bag" 的方案。
(上箭头符号 ^ 表示选取的字母)
babgbag
^^ ^
babgbag
^^    ^
babgbag
^    ^^
babgbag
  ^  ^^
babgbag
    ^^^


提示：

0 <= s.length, t.length <= 1000
s 和 t 由英文字母组成
'''



class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        m, n = len(s), len(t)
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(m):
            dp[i][0] = 1

        for i in range(1, m+1):
            for j in range(1, n+1):
                if j > i:
                    continue

                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]

        return dp[m][n]


# solutions

'''
1： 为啥状态方程这样对？ 2：怎么想到这样的状态方程？

我个人习惯dp[i][j] 表示为s[0-i] 和t[0-j]均闭区间的子序列个数，但这样不能表示s和t空串的情况

所以声明 int[][] dp = new int[m + 1][n + 1]; 这样dp[0][x]可以表示s为空串，dp[x][0]同理。

先不扣初始化的细节，假设dp[i][j] 就是s[i] 和t[j] 索引的元素子序列数量

1：为啥状态方程是： s[i] == t[j] 时 dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

s[i] != t[j] 时 dp[i][j] = dp[i-1][j]

先看s[i] == t[j] 时，以s = "rara" t = "ra" 为例，当i = 3, j = 1时，s[i] == t[j]。

此时分为2种情况，s串用最后一位的a + 不用最后一位的a。

如果用s串最后一位的a,那么t串最后一位的a也被消耗掉，此时的子序列其实=dp[i-1][j-1]

如果不用s串最后一位的a，那就得看"rar"里面是否有"ra"子序列的了，就是dp[i-1][j]

所以 dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

再看s[i] != t[j] 比如 s = "rarb" t = "ra" 还是当i = 3, j = 1时，s[i] != t[j]

此时显然最后的b想用也用不上啊。所以只能指望前面的"rar"里面是否有能匹配"ra"的

所以此时dp[i][j] = dp[i-1][j]

2: 怎么想到这样状态方程的？

一点个人经验，见过的很多2个串的题，大部分都是dp[i][j] 分别表示s串[0...i] 和t串[0...j]怎么怎么样 然后都是观察s[i]和t[j]分等或者不等的情况 而且方程通常就是 dp[i-1][j-1] 要么+ 要么 || dp[i-1][j]类似的

类似的题比如有 10：正则表达式匹配 44：通配符匹配 编辑距离 1143：最长公共子序列等等的 还有几道想不起来了

class Solution {
    public int numDistinct(String s, String t) {
        int m = s.length(), n = t.length();
        int[][] dp = new int[m + 1][n + 1];
        for (int i = 0; i <= m; i++)
            dp[i][0] = 1;

        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (j > i)
                    continue;
                if (s.charAt(i - 1) == t.charAt(j - 1)) {
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j];
                } else {
                    dp[i][j] = dp[i - 1][j];
                }
            }
        }
        return dp[m][n];
    }
}
'''


'''
方法一：动态规划
假设字符串 ss 和 tt 的长度分别为 mm 和 nn。如果 tt 是 ss 的子序列，则 ss 的长度一定大于或等于 tt 的长度，即只有当 m \ge nm≥n 时，tt 才可能是 ss 的子序列。如果 m<nm<n，则 tt 一定不是 ss 的子序列，因此直接返回 00。

当 m \ge nm≥n 时，可以通过动态规划的方法计算在 ss 的子序列中 tt 出现的个数。

创建二维数组 \textit{dp}dp，其中 \textit{dp}[i][j]dp[i][j] 表示在 s[i:]s[i:] 的子序列中 t[j:]t[j:] 出现的个数。

上述表示中，s[i:]s[i:] 表示 ss 从下标 ii 到末尾的子字符串，t[j:]t[j:] 表示 tt 从下标 jj 到末尾的子字符串。

考虑动态规划的边界情况：

当 j=nj=n 时，t[j:]t[j:] 为空字符串，由于空字符串是任何字符串的子序列，因此对任意 0 \le i \le m0≤i≤m，有 \textit{dp}[i][n]=1dp[i][n]=1；

当 i=mi=m 且 j<nj<n 时，s[i:]s[i:] 为空字符串，t[j:]t[j:] 为非空字符串，由于非空字符串不是空字符串的子序列，因此对任意 0 \le j<n0≤j<n，有 \textit{dp}[m][j]=0dp[m][j]=0。

当 i<mi<m 且 j<nj<n 时，考虑 \textit{dp}[i][j]dp[i][j] 的计算：

当 s[i]=t[j]s[i]=t[j] 时，\textit{dp}[i][j]dp[i][j] 由两部分组成：

如果 s[i]s[i] 和 t[j]t[j] 匹配，则考虑 t[j+1:]t[j+1:] 作为 s[i+1:]s[i+1:] 的子序列，子序列数为 \textit{dp}[i+1][j+1]dp[i+1][j+1]；

如果 s[i]s[i] 不和 t[j]t[j] 匹配，则考虑 t[j:]t[j:] 作为 s[i+1:]s[i+1:] 的子序列，子序列数为 \textit{dp}[i+1][j]dp[i+1][j]。

因此当 s[i]=t[j]s[i]=t[j] 时，有 \textit{dp}[i][j]=\textit{dp}[i+1][j+1]+\textit{dp}[i+1][j]dp[i][j]=dp[i+1][j+1]+dp[i+1][j]。

当 s[i] \ne t[j]s[i] 

​	
 =t[j] 时，s[i]s[i] 不能和 t[j]t[j] 匹配，因此只考虑 t[j:]t[j:] 作为 s[i+1:]s[i+1:] 的子序列，子序列数为 \textit{dp}[i+1][j]dp[i+1][j]。

因此当 s[i] \ne t[j]s[i] 

​	
 =t[j] 时，有 \textit{dp}[i][j]=\textit{dp}[i+1][j]dp[i][j]=dp[i+1][j]。

由此可以得到如下状态转移方程：

\textit{dp}[i][j] = \begin{cases} \textit{dp}[i+1][j+1]+\textit{dp}[i+1][j], & s[i]=t[j]\\ \textit{dp}[i+1][j], & s[i] \ne t[j] \end{cases}
dp[i][j]={ 
dp[i+1][j+1]+dp[i+1][j],
dp[i+1][j],
​	
  
s[i]=t[j]
s[i] 

​	
 =t[j]
​	
 

最终计算得到 \textit{dp}[0][0]dp[0][0] 即为在 ss 的子序列中 tt 出现的个数。


1 / 24

JavaJavaScriptGolangPython3C++C

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        if m < n:
            return 0
        
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][n] = 1
        
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if s[i] == t[j]:
                    dp[i][j] = dp[i + 1][j + 1] + dp[i + 1][j]
                else:
                    dp[i][j] = dp[i + 1][j]
        
        return dp[0][0]
复杂度分析

时间复杂度：O(mn)O(mn)，其中 mm 和 nn 分别是字符串 ss 和 tt 的长度。二维数组 \textit{dp}dp 有 m+1m+1 行和 n+1n+1 列，需要对 \textit{dp}dp 中的每个元素进行计算。

空间复杂度：O(mn)O(mn)，其中 mm 和 nn 分别是字符串 ss 和 tt 的长度。创建了 m+1m+1 行 n+1n+1 列的二维数组 \textit{dp}dp。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/distinct-subsequences/solution/bu-tong-de-zi-xu-lie-by-leetcode-solutio-urw3/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''


