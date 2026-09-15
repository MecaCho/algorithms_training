# encoding=utf8

'''
2472. Maximum Number of Non-overlapping Palindrome Substrings
You are given a string s and a positive integer k.

Select a set of non-overlapping substrings from the string s that satisfy the following conditions:

The length of each substring is at least k.
Each substring is a palindrome.

Return the maximum number of substrings in an optimal selection.

A substring is a contiguous sequence of characters within a string.

 

Example 1:

Input: s = "abaccdbbd", k = 3
Output: 2
Explanation: We can select the substrings underlined in s = "abaccdbbd". Both "aba" and "dbbd" are palindromes and have a length of at least k = 3.
It can be shown that we cannot find a selection with more than two valid substrings.

Example 2:

Input: s = "adbcda", k = 2
Output: 0
Explanation: There is no palindrome substring of length at least 2 in the string.

 

Constraints:

1 <= k <= s.length <= 2000
s consists of lowercase English letters.


2472. 不重叠回文子字符串的最大数目
给你一个字符串 s 和一个 正 整数 k 。

从字符串 s 中选出一组满足下述条件且 不重叠 的子字符串：

- 每个子字符串的长度 至少 为 k 。
- 每个子字符串是一个 回文串 。

返回最优方案中能选择的子字符串的 最大 数目。

子字符串 是字符串中一个连续的字符序列。

 

示例 1 ：

输入：s = "abaccdbbd", k = 3
输出：2
解释：可以选择 s = "abaccdbbd" 中斜体加粗的子字符串。"aba" 和 "dbbd" 都是回文，且长度至少为 k = 3 。
可以证明，无法选出两个以上的有效子字符串。

示例 2 ：

输入：s = "adbcda", k = 2
输出：0
解释：字符串中不存在长度至少为 2 的回文子字符串。

 

提示：

1 <= k <= s.length <= 2000
s 仅由小写英文字母组成
'''


class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        dp = [0] * (n + 1)

        for i in range(k, n + 1):
            dp[i] = dp[i - 1]
            # 检查以 i-1 结尾且长度为 k 的回文子串 s[i-k:i]
            sub_k = s[i - k : i]
            if sub_k == sub_k[::-1]:
                dp[i] = max(dp[i], dp[i - k] + 1)
            # 检查以 i-1 结尾且长度为 k+1 的回文子串 s[i-k-1:i]
            if i >= k + 1:
                sub_k1 = s[i - k - 1 : i]
                if sub_k1 == sub_k1[::-1]:
                    dp[i] = max(dp[i], dp[i - k - 1] + 1)

        return dp[n]


# golang solution

'''
func maxPalindromes(s string, k int) int {
	n := len(s)
	dp := make([]int, n+1)

	isPalindrome := func(left, right int) bool {
		for left < right {
			if s[left] != s[right] {
				return false
			}
			left++
			right--
		}
		return true
	}

	max := func(a, b int) int {
		if a > b {
			return a
		}
		return b
	}

	for i := k; i <= n; i++ {
		dp[i] = dp[i-1]
		// 检查长度为 k 的回文子串 s[i-k ... i-1]
		if isPalindrome(i-k, i-1) {
			dp[i] = max(dp[i], dp[i-k]+1)
		}
		// 检查长度为 k + 1 的回文子串 s[i-k-1 ... i-1]
		if i >= k+1 && isPalindrome(i-k-1, i-1) {
			dp[i] = max(dp[i], dp[i-k-1]+1)
		}
	}

	return dp[n]
}
'''

# solutions

'''
思路和算法：

方法：动态规划 + 贪心降维（只检查长度为 k 与 k + 1 的回文）

1. 核心性质观察（贪心收缩）：
   假设一个合法的回文子串 P 的长度 L >= k + 2。
   若我们将 P 的首尾各去掉一个字符，得到其内部的子串 P' = P[1 : -1]：
   - 因为 P 是回文串，所以 P' 也必然是回文串；
   - P' 的长度为 L - 2 >= k；
   - P' 的起始下标严格大于 P 的起始下标，结束下标严格小于 P 的结束下标（即 P' 完全包含在 P 内部）。
   
   因此，任何包含长度 >= k + 2 的回文串的最优解，都可以将该回文串替换为其内部中心对齐的更短回文串，而绝不会与其余任何已选出的子串发生重叠。
   递推下去，任意长度 >= k 的回文串都可以收缩为长度恰好为 k（当 L - k 为偶数时）或 k + 1（当 L - k 为奇数时）的回文子串。
   故我们只需考虑长度为 k 和 k + 1 的回文串即可，不需要检查任何更长的回文子串！

2. 状态定义与转移：
   设 dp[i] 表示字符串前缀 s[0 ... i-1]（前 i 个字符）中能够选出的满足条件的不重叠回文子串的最大数目。
   - 基础情况：dp[0] = 0。
   - 转移方程：对于每个位置 i（从 k 遍历到 n）：
     1. 不选取以字符 s[i-1] 结尾的回文子串：
        dp[i] = dp[i-1]
     2. 若 s[i-k : i]（长度为 k）是回文串，则可以从 dp[i-k] 转移过来：
        dp[i] = max(dp[i], dp[i-k] + 1)
     3. 若 i >= k + 1 且 s[i-k-1 : i]（长度为 k+1）是回文串，则可以从 dp[i-k-1] 转移过来：
        dp[i] = max(dp[i], dp[i-k-1] + 1)
   - 最终答案为 dp[n]。

复杂度分析：
- 时间复杂度：O(n * k)，其中 n 为字符串 s 的长度。我们需要遍历 i 从 k 到 n，每次只需验证长度为 k 和 k+1 的两个子串是否为回文（耗时 O(k)）。在题目数据规模 n <= 2000 下，总操作次数最多约 2 * 10^3 * 2000 = 4 * 10^6 次，可以在数毫秒内运行完毕。
- 空间复杂度：O(n)，动态规划数组 dp 的长度为 n + 1。
'''

