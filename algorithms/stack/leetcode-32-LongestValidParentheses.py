# encoding=utf8

'''
32. Longest Valid Parentheses
Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses substring.

 

Example 1:

Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".

Example 2:

Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".

Example 3:

Input: s = ""
Output: 0

 

Constraints:

0 <= s.length <= 3 * 10^4
s[i] is '(', or ')'.


32. 最长有效括号
给你一个只包含 '(' 和 ')' 的字符串，找出最长有效（格式正确且连续）括号子串的长度。

 

示例 1：

输入：s = "(()"
输出：2
解释：最长有效括号子串是 "()"

示例 2：

输入：s = ")()())"
输出：4
解释：最长有效括号子串是 "()()"

示例 3：

输入：s = ""
输出：0

 

提示：

0 <= s.length <= 3 * 10^4
s[i] 为 '(' 或 ')'
'''


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        max_len = 0
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    max_len = max(max_len, i - stack[-1])
        return max_len


class SolutionDP:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        dp = [0] * n
        max_len = 0
        for i in range(1, n):
            if s[i] == ')':
                if s[i - 1] == '(':
                    dp[i] = (dp[i - 2] if i >= 2 else 0) + 2
                elif i - dp[i - 1] > 0 and s[i - dp[i - 1] - 1] == '(':
                    dp[i] = dp[i - 1] + 2 + (dp[i - dp[i - 1] - 2] if i - dp[i - 1] >= 2 else 0)
                max_len = max(max_len, dp[i])
        return max_len


class SolutionGreedy:
    def longestValidParentheses(self, s: str) -> int:
        left = right = max_len = 0
        for c in s:
            if c == '(':
                left += 1
            else:
                right += 1
            if left == right:
                max_len = max(max_len, 2 * right)
            elif right > left:
                left = right = 0

        left = right = 0
        for c in reversed(s):
            if c == '(':
                left += 1
            else:
                right += 1
            if left == right:
                max_len = max(max_len, 2 * left)
            elif left > right:
                left = right = 0

        return max_len


# golang solution

'''
// 方法一：栈
func longestValidParentheses(s string) int {
	maxAns := 0
	stack := []int{-1}
	for i := 0; i < len(s); i++ {
		if s[i] == '(' {
			stack = append(stack, i)
		} else {
			stack = stack[:len(stack)-1]
			if len(stack) == 0 {
				stack = append(stack, i)
			} else {
				length := i - stack[len(stack)-1]
				if length > maxAns {
					maxAns = length
				}
			}
		}
	}
	return maxAns
}

// 方法二：动态规划
func longestValidParenthesesDP(s string) int {
	maxAns := 0
	n := len(s)
	dp := make([]int, n)
	for i := 1; i < n; i++ {
		if s[i] == ')' {
			if s[i-1] == '(' {
				if i >= 2 {
					dp[i] = dp[i-2] + 2
				} else {
					dp[i] = 2
				}
			} else if i-dp[i-1] > 0 && s[i-dp[i-1]-1] == '(' {
				if i-dp[i-1] >= 2 {
					dp[i] = dp[i-1] + dp[i-dp[i-1]-2] + 2
				} else {
					dp[i] = dp[i-1] + 2
				}
			}
			if dp[i] > maxAns {
				maxAns = dp[i]
			}
		}
	}
	return maxAns
}

// 方法三：正反双向贪心扫描（O(1) 空间）
func longestValidParenthesesGreedy(s string) int {
	left, right, maxLen := 0, 0, 0
	for i := 0; i < len(s); i++ {
		if s[i] == '(' {
			left++
		} else {
			right++
		}
		if left == right {
			if 2*right > maxLen {
				maxLen = 2 * right
			}
		} else if right > left {
			left, right = 0, 0
		}
	}

	left, right = 0, 0
	for i := len(s) - 1; i >= 0; i-- {
		if s[i] == '(' {
			left++
		} else {
			right++
		}
		if left == right {
			if 2*left > maxLen {
				maxLen = 2 * left
			}
		} else if left > right {
			left, right = 0, 0
		}
	}
	return maxLen
}
'''

# solutions

'''
思路和算法：

方法一：栈（Stack）
1. 维护栈底元素为“当前最后一个未匹配的右括号的下标”。
   栈内其余元素记录尚未匹配的左括号下标。
2. 初始时向栈中压入 -1 作为哨兵。
3. 遍历字符串：
   - 遇到 '('，将其下标 i 入栈；
   - 遇到 ')'，先弹出栈顶元素：
     - 若弹出后栈为空，说明该 ')' 没有匹配的 '('，将其下标 i 入栈作为新的基准（即最后一个未匹配右括号下标）；
     - 若弹出后栈不为空，则当前有效括号子串长度为 i - stack[-1]，更新最大长度。
复杂度分析：
- 时间复杂度：O(n)，单次线性遍历。
- 空间复杂度：O(n)，栈的最大深度为 n。

方法二：动态规划（Dynamic Programming）
1. 状态定义：dp[i] 表示以下标 i 结尾的最长有效括号子串长度。
2. 只有以 ')' 结尾的子串才可能有效，因此当 s[i] == ')' 时转移：
   - 若 s[i - 1] == '('，形如 "...()"：
     dp[i] = (dp[i - 2] if i >= 2 else 0) + 2
   - 若 s[i - 1] == ')'，形如 "...))"：
     如果与当前 ')' 匹配的位置 pre = i - dp[i - 1] - 1 存在且 s[pre] == '('：
     dp[i] = dp[i - 1] + 2 + (dp[pre - 1] if pre >= 1 else 0)
3. 遍历更新 dp[i] 的最大值。
复杂度分析：
- 时间复杂度：O(n)，遍历一次字符串。
- 空间复杂度：O(n)，dp 数组占用 O(n) 空间。

方法三：双向遍历计数器（贪心 / 常数额外空间）
1. 从左向右遍历，维护 left 和 right 计数器：
   - 当 left == right 时，更新 max_len = max(max_len, 2 * right)；
   - 当 right > left 时，说明右括号过多，无法成为有效子串的前缀，重置 left = right = 0。
2. 仅从左向右会漏掉左括号始终多于右括号的情况（例如 "(()"），因此再从右向左逆向遍历一遍：
   - 当 left == right 时，更新 max_len = max(max_len, 2 * left)；
   - 当 left > right 时，重置 left = right = 0。
复杂度分析：
- 时间复杂度：O(n)，正向反向各遍历一次。
- 空间复杂度：O(1)，仅使用常数个计数器变量。
'''

