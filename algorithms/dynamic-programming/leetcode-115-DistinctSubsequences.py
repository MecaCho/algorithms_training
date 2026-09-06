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

---

### 动态规划 (Dynamic Programming)

设字符串 `s` 的长度为 $m$，字符串 `t` 的长度为 $n$。

#### 1. 状态定义
设 `dp[i][j]` 表示：字符串 `s` 的前 `i` 个字符 `s[0..i-1]` 中，能构成字符串 `t` 的前 `j` 个字符 `t[0..j-1]` 的不同子序列个数。

#### 2. 边界条件
- `dp[i][0] = 1`（对于任意 $0 \le i \le m$）：空字符串 `t` 是任意字符串前缀的子序列，且只有 1 种选取方式（什么都不选）。
- `dp[0][j] = 0`（对于任意 $1 \le j \le n$）：空字符串 `s` 无法构成非空字符串 `t` 的子序列。

#### 3. 状态转移方程
对于第 $i$ 个字符 $s[i-1]$ 和第 $j$ 个字符 $t[j-1]$：

1. **若 $s[i-1] == t[j-1]$**：
   当前字符匹配，此时有 2 种选择：
   - 使用 $s[i-1]$ 匹配 $t[j-1]$：方案数加 $dp[i-1][j-1]$。
   - 不使用 $s[i-1]$（丢弃该字符），继续用 $s[0..i-2]$ 匹配 $t[0..j-1]$：方案数加 $dp[i-1][j]$。
   $$\text{dp}[i][j] = \text{dp}[i-1][j-1] + \text{dp}[i-1][j]$$

2. **若 $s[i-1] \neq t[j-1]$**：
   无法用 $s[i-1]$ 匹配 $t[j-1]$，只能舍弃 $s[i-1]$：
   $$\text{dp}[i][j] = \text{dp}[i-1][j]$$

---

### 复杂度分析

- **时间复杂度**：$\mathcal{O}(m \times n)$，其中 $m$ 和 $n$ 分别为 `s` 和 `t` 的长度。双重循环遍历状态矩阵。
- **空间复杂度**：$\mathcal{O}(m \times n)$，需要维度的二维 DP 数组（可通过一维滚动数组进一步优化至 $\mathcal{O}(n)$）。

---
'''

