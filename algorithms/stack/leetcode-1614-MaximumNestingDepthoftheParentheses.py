# encoding=utf8

'''
1614. Maximum Nesting Depth of the Parentheses
Given a valid parentheses string s, return the nesting depth of s. The nesting depth is the maximum number of nested parentheses.

 

Example 1:

Input: s = "(1+(2*3)+((8)/4))+1"
Output: 3
Explanation:
Digit 8 is inside of 3 nested parentheses in the string.

Example 2:

Input: s = "(1)+((2))+(((3)))"
Output: 3
Explanation:
Digit 3 is inside of 3 nested parentheses in the string.

Example 3:

Input: s = "()(())((()()))"
Output: 3

 

Constraints:

1 <= s.length <= 100
s consists of digits 0-9 and characters '+', '-', '*', '/', '(', and ')'.
It is guaranteed that parentheses expression s is a VPS.


1614. 括号的最大嵌套深度
给定 有效括号字符串 s ，返回 s 的 嵌套深度 。嵌套深度是嵌套括号的 最大 数量。

 

示例 1：

输入：s = "(1+(2*3)+((8)/4))+1"
输出：3
解释：数字 8 在嵌套的 3 层括号中。

示例 2：

输入：s = "(1)+((2))+(((3)))"
输出：3
解释：数字 3 在嵌套的 3 层括号中。

示例 3：

输入：s = "()(())((()()))"
输出：3

 

提示：

1 <= s.length <= 100
s 由数字 0-9 和字符 '+' 、 '-' 、 '*' 、 '/' 、 '(' 、 ')' 组成
题目数据保证括号字符串 s 是 有效的括号字符串
'''


class Solution:
    def maxDepth(self, s: str) -> int:
        ans = d = 0
        for c in s:
            if c == '(':
                d += 1
                if d > ans:
                    ans = d
            elif c == ')':
                d -= 1
        return ans


# golang solution

'''
func maxDepth(s string) int {
	ans := 0
	d := 0
	for _, c := range s {
		if c == '(' {
			d++
			if d > ans {
				ans = d
			}
		} else if c == ')' {
			d--
		}
	}
	return ans
}
'''

# solutions

'''
思路和算法：

方法：栈思想 / 计数器模拟

1. 问题分析：
   题目保证给定的字符串 s 是一个有效括号表达式（VPS）。
   括号的嵌套深度即在任意时刻未匹配的左括号数量的最大值。
   除了括号之外的数字与算术运算符（如 0-9, '+', '-', '*', '/'）不影响括号的嵌套层次与有效性。

2. 算法设计：
   - 我们可以使用一个栈来维护当前未闭合的左括号，也可以直接用一个整型变量 d 模拟栈的大小（当前嵌套深度）；
   - 维护一个全局最大深度 ans，初始为 0；
   - 从左到右遍历字符串 s 中的每个字符 c：
     - 若 c == '('，表示进入一层新的括号嵌套，当前深度 d 加 1，并更新 ans = max(ans, d)；
     - 若 c == ')'，表示当前层括号闭合，当前深度 d 减 1；
     - 若为其他字符，直接跳过；
   - 遍历完成后返回 ans。

复杂度分析：
- 时间复杂度：O(n)，其中 n 为字符串 s 的长度。只需对字符串进行一次线性扫描。
- 空间复杂度：O(1)，仅需维护常数个计数器变量，不需要额外栈存储空间。
'''

