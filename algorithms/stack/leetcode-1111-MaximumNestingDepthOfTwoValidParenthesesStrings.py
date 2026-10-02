# encoding=utf8

'''
1111. Maximum Nesting Depth of Two Valid Parentheses Strings
A string is a valid parentheses string (denoted VPS) if and only if it consists of "(" and ")" characters only, and:

It is the empty string, or
It can be written as AB (A concatenated with B), where A and B are VPS's, or
It can be written as (A), where A is a VPS.
We can similarly define the nesting depth depth(S) of any VPS S as follows:

depth("") = 0
depth(A + B) = max(depth(A), depth(B)), where A and B are VPS's
depth("(" + A + ")") = 1 + depth(A), where A is a VPS.
For example,  "", "()()", and "()(()())" are VPS's (with nesting depths 0, 1, and 2), and ")(" and "(()" are not VPS's.

Given a VPS seq, split it into two disjoint subsequences A and B, such that A and B are VPS's (and A.length + B.length = seq.length). The subsequences may not necessarily be contiguous.

For example, for the sequence 123456789, one possible split is:

A = {1, 3, 5, 7, 9},

B = {2, 4, 6, 8}.

This corresponds to the output [0, 1, 0, 1, 0, 1, 0, 1, 0] where 0 indicates membership in A and 1 indicates membership in B.

Now choose any such A and B such that max(depth(A), depth(B)) is the minimum possible value.

Return an answer array (of length seq.length) that encodes such a choice of A and B: answer[i] = 0 if seq[i] is part of A, else answer[i] = 1. Note that even though multiple answers may exist, you may return any of them.

 

Example 1:

Input: seq = "(()())"
Output: [0,1,1,1,1,0]

Example 2:

Input: seq = "()(())()"
Output: [0,0,0,1,1,0,1,1]

 

Constraints:

1 <= seq.size <= 10000


1111. 有效括号的嵌套深度
有效括号字符串 仅由 "(" 和 ")" 构成，并符合下述几个条件之一：

空字符串
连接，可以记作 AB（A 与 B 连接），其中 A 和 B 都是有效括号字符串
嵌套，可以记作 (A)，其中 A 是有效括号字符串
类似地，我们可以定义任意有效括号字符串 s 的 嵌套深度 depth(S)：

s 为空时，depth("") = 0
s 为 A 与 B 连接时，depth(A + B) = max(depth(A), depth(B))，其中 A 和 B 都是有效括号字符串
s 为嵌套情况，depth("(" + A + ")") = 1 + depth(A)，其中 A 是有效括号字符串
例如：""，"()()"，和 "()(()())" 都是有效括号字符串，嵌套深度分别为 0，1，2，而 ")(" 和 "(()" 都不是有效括号字符串。

给你一个有效括号字符串 seq，将其分成两个不相交的子序列 A 和 B，且 A 和 B 满足有效括号字符串的定义（注意：A.length + B.length = seq.length）。

现在，你需要从中选出 任意 一组有效括号字符串 A 和 B，使 max(depth(A), depth(B)) 的可能取值最小。

返回长度为 seq.length 答案数组 answer ，选择 A 还是 B 的编码规则是：如果 seq[i] 是 A 的一部分，那么 answer[i] = 0。否则，answer[i] = 1。即便有多个满足要求的答案存在，你也只需返回 一个。

 

示例 1：

输入：seq = "(()())"
输出：[0,1,1,1,1,0]

示例 2：

输入：seq = "()(())()"
输出：[0,0,0,1,1,0,1,1]
解释：本示例答案不唯一。
按此输出 A = "()()", B = "()()", max(depth(A), depth(B)) = 1，它们的深度最小。
像 [1,1,1,0,0,1,1,1] 也是正确结果，其中 A = "()()()", B = "()", max(depth(A), depth(B)) = 1 。

 

提示：

1 <= seq.size <= 10000
'''


class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        ans = [0] * len(seq)
        d = 0
        for i, c in enumerate(seq):
            if c == '(':
                ans[i] = d & 1
                d += 1
            else:
                d -= 1
                ans[i] = d & 1
        return ans


# golang solution

'''
func maxDepthAfterSplit(seq string) []int {
	n := len(seq)
	ans := make([]int, n)
	d := 0
	for i, c := range seq {
		if c == '(' {
			ans[i] = d & 1
			d++
		} else {
			d--
			ans[i] = d & 1
		}
	}
	return ans
}
'''



