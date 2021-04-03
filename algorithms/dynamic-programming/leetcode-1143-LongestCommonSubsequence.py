# encoding=utf8


'''
1143. Longest Common Subsequence
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.



Example 1:

Input: text1 = "abcde", text2 = "ace"
Output: 3
Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.


Constraints:

1 <= text1.length, text2.length <= 1000
text1 and text2 consist of only lowercase English characters.



1143. 最长公共子序列
给定两个字符串 text1 和 text2，返回这两个字符串的最长 公共子序列 的长度。如果不存在 公共子序列 ，返回 0 。

一个字符串的 子序列 是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。

例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。
两个字符串的 公共子序列 是这两个字符串所共同拥有的子序列。



示例 1：

输入：text1 = "abcde", text2 = "ace"
输出：3
解释：最长公共子序列是 "ace" ，它的长度为 3 。
示例 2：

输入：text1 = "abc", text2 = "abc"
输出：3
解释：最长公共子序列是 "abc" ，它的长度为 3 。
示例 3：

输入：text1 = "abc", text2 = "def"
输出：0
解释：两个字符串没有公共子序列，返回 0 。


提示：

1 <= text1.length, text2.length <= 1000
text1 和 text2 仅由小写英文字符组成。
'''



class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        m, n = len(text1), len(text2)
        dp = [[0 for i in range(n+1)] for j in range(m+1)]

        for i in range(1, m+1):
            for j in range(1, n+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        return dp[-1][-1]


# solutions

'''
方法一：动态规划
最长公共子序列问题是典型的二维动态规划问题。

假设字符串 \textit{text}_1text 
1
​	
  和 \textit{text}_2text 
2
​	
  的长度分别为 mm 和 nn，创建 m+1m+1 行 n+1n+1 列的二维数组 \textit{dp}dp，其中 \textit{dp}[i][j]dp[i][j] 表示 \textit{text}_1[0:i]text 
1
​	
 [0:i] 和 \textit{text}_2[0:j]text 
2
​	
 [0:j] 的最长公共子序列的长度。

上述表示中，\textit{text}_1[0:i]text 
1
​	
 [0:i] 表示 \textit{text}_1text 
1
​	
  的长度为 ii 的前缀，\textit{text}_2[0:j]text 
2
​	
 [0:j] 表示 \textit{text}_2text 
2
​	
  的长度为 jj 的前缀。

考虑动态规划的边界情况：

当 i=0i=0 时，\textit{text}_1[0:i]text 
1
​	
 [0:i] 为空，空字符串和任何字符串的最长公共子序列的长度都是 00，因此对任意 0 \le j \le n0≤j≤n，有 \textit{dp}[0][j]=0dp[0][j]=0；

当 j=0j=0 时，\textit{text}_2[0:j]text 
2
​	
 [0:j] 为空，同理可得，对任意 0 \le i \le m0≤i≤m，有 \textit{dp}[i][0]=0dp[i][0]=0。

因此动态规划的边界情况是：当 i=0i=0 或 j=0j=0 时，\textit{dp}[i][j]=0dp[i][j]=0。

当 i>0i>0 且 j>0j>0 时，考虑 \textit{dp}[i][j]dp[i][j] 的计算：

当 \textit{text}_1[i-1]=\textit{text}_2[j-1]text 
1
​	
 [i−1]=text 
2
​	
 [j−1] 时，将这两个相同的字符称为公共字符，考虑 \textit{text}_1[0:i-1]text 
1
​	
 [0:i−1] 和 \textit{text}_2[0:j-1]text 
2
​	
 [0:j−1] 的最长公共子序列，再增加一个字符（即公共字符）即可得到 \textit{text}_1[0:i]text 
1
​	
 [0:i] 和 \textit{text}_2[0:j]text 
2
​	
 [0:j] 的最长公共子序列，因此 \textit{dp}[i][j]=\textit{dp}[i-1][j-1]+1dp[i][j]=dp[i−1][j−1]+1。

当 \textit{text}_1[i-1] \ne \textit{text}_2[j-1]text 
1
​	
 [i−1] 

​	
 =text 
2
​	
 [j−1] 时，考虑以下两项：

\textit{text}_1[0:i-1]text 
1
​	
 [0:i−1] 和 \textit{text}_2[0:j]text 
2
​	
 [0:j] 的最长公共子序列；

\textit{text}_1[0:i]text 
1
​	
 [0:i] 和 \textit{text}_2[0:j-1]text 
2
​	
 [0:j−1] 的最长公共子序列。

要得到 \textit{text}_1[0:i]text 
1
​	
 [0:i] 和 \textit{text}_2[0:j]text 
2
​	
 [0:j] 的最长公共子序列，应取两项中的长度较大的一项，因此 \textit{dp}[i][j]=\max(\textit{dp}[i-1][j],\textit{dp}[i][j-1])dp[i][j]=max(dp[i−1][j],dp[i][j−1])。

由此可以得到如下状态转移方程：

\textit{dp}[i][j] = \begin{cases} \textit{dp}[i-1][j-1]+1, & \textit{text}_1[i-1]=\textit{text}_2[j-1] \\ \max(\textit{dp}[i-1][j],\textit{dp}[i][j-1]), & \textit{text}_1[i-1] \ne \textit{text}_2[j-1] \end{cases}
dp[i][j]={ 
dp[i−1][j−1]+1,
max(dp[i−1][j],dp[i][j−1]),
​	
  
text 
1
​	
 [i−1]=text 
2
​	
 [j−1]
text 
1
​	
 [i−1] 

​	
 =text 
2
​	
 [j−1]
​	
 

最终计算得到 \textit{dp}[m][n]dp[m][n] 即为 \textit{text}_1text 
1
​	
  和 \textit{text}_2text 
2
​	
  的最长公共子序列的长度。



JavaJavaScriptGolangPython3C++C

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        return dp[m][n]
复杂度分析

时间复杂度：O(mn)O(mn)，其中 mm 和 nn 分别是字符串 \textit{text}_1text 
1
​	
  和 \textit{text}_2text 
2
​	
  的长度。二维数组 \textit{dp}dp 有 m+1m+1 行和 n+1n+1 列，需要对 \textit{dp}dp 中的每个元素进行计算。

空间复杂度：O(mn)O(mn)，其中 mm 和 nn 分别是字符串 \textit{text}_1text 
1
​	
  和 \textit{text}_2text 
2
​	
  的长度。创建了 m+1m+1 行 n+1n+1 列的二维数组 \textit{dp}dp。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/longest-common-subsequence/solution/zui-chang-gong-gong-zi-xu-lie-by-leetcod-y7u0/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
