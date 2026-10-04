# encoding=utf8

'''
678. Valid Parenthesis String
Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.

The following rules define a valid string:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".

 

Example 1:

Input: s = "()"
Output: true

Example 2:

Input: s = "(*)"
Output: true

Example 3:

Input: s = "(*))"
Output: true

Example 4:

Input: s = "("
Output: false

 

Constraints:

1 <= s.length <= 100
s[i] is '(', ')' or '*'.


678. 有效的括号字符串
给你一个只包含三种字符的字符串，支持的字符类型分别是 '('、')' 和 '*'。请你检验这个字符串是否为有效字符串，如果是 有效 字符串返回 true。

有效 字符串符合如下规则：

任何左括号 '(' 必须有相应的右括号 ')'。
任何右括号 ')' 必须有相应的左括号 '('。
左括号 '(' 必须在对应的右括号之前 ')'。
'*' 可以被视为单个右括号 ')'，或单个左括号 '('，或一个空字符串 ""。

 

示例 1：

输入：s = "()"
输出：true

示例 2：

输入：s = "(*)"
输出：true

示例 3：

输入：s = "(*))"
输出：true

示例 4：

输入：s = "("
输出：false

 

提示：

1 <= s.length <= 100
s[i] 为 '('、')' 或 '*'
'''


class Solution:
    def checkValidString(self, s: str) -> bool:
        # min_count: 将 '*' 尽可能视为 ')' 或空串时，未匹配左括号的最少数量
        # max_count: 将 '*' 尽可能视为 '(' 时，未匹配左括号的最多数量
        min_count = max_count = 0
        for c in s:
            if c == '(':
                min_count += 1
                max_count += 1
            elif c == ')':
                min_count -= 1
                max_count -= 1
            else:  # c == '*'
                min_count -= 1
                max_count += 1

            if max_count < 0:
                # 即使把所有 '*' 都当成左括号，右括号依然过多
                return False
            if min_count < 0:
                # 未匹配左括号的数量不能小于 0
                min_count = 0

        return min_count == 0


class SolutionStack:
    def checkValidString(self, s: str) -> bool:
        left_stack = []
        star_stack = []
        for i, c in enumerate(s):
            if c == '(':
                left_stack.append(i)
            elif c == '*':
                star_stack.append(i)
            else:
                if left_stack:
                    left_stack.pop()
                elif star_stack:
                    star_stack.pop()
                else:
                    return False

        while left_stack and star_stack:
            if left_stack[-1] > star_stack[-1]:
                return False
            left_stack.pop()
            star_stack.pop()

        return len(left_stack) == 0


# golang solution

'''
// 方法一：贪心区间计数（O(1) 空间）
func checkValidString(s string) bool {
	minCount, maxCount := 0, 0
	for _, c := range s {
		if c == '(' {
			minCount++
			maxCount++
		} else if c == ')' {
			minCount--
			maxCount--
		} else { // c == '*'
			minCount--
			maxCount++
		}

		if maxCount < 0 {
			return false
		}
		if minCount < 0 {
			minCount = 0
		}
	}
	return minCount == 0
}

// 方法二：双栈法（O(n) 空间）
func checkValidStringStack(s string) bool {
	leftStack := []int{}
	starStack := []int{}
	for i, c := range s {
		if c == '(' {
			leftStack = append(leftStack, i)
		} else if c == '*' {
			starStack = append(starStack, i)
		} else {
			if len(leftStack) > 0 {
				leftStack = leftStack[:len(leftStack)-1]
			} else if len(starStack) > 0 {
				starStack = starStack[:len(starStack)-1]
			} else {
				return false
			}
		}
	}

	for len(leftStack) > 0 && len(starStack) > 0 {
		if leftStack[len(leftStack)-1] > starStack[len(starStack)-1] {
			return false
		}
		leftStack = leftStack[:len(leftStack)-1]
		starStack = starStack[:len(starStack)-1]
	}

	return len(leftStack) == 0
}
'''

# solutions

'''
思路和算法：

方法一：贪心维护未匹配左括号数量范围（推荐，O(1) 空间）
1. 核心观察：
   每个星号 '*' 可以充当三种角色：
   - 充当 '('，使未匹配左括号数加 1；
   - 充当 ')'，使未匹配左括号数减 1；
   - 充当空字符 ""，对未匹配左括号数不产生影响。
   因此，在遍历过程中，未匹配的左括号数量不是一个固定值，而是一个连续区间 [min_count, max_count]。
   - min_count 表示在所有可能选择下，未匹配左括号的最少数量；
   - max_count 表示在所有可能选择下，未匹配左括号的最多数量。

2. 状态转移：
   从左往右遍历字符串 s：
   - 遇到 '('：min_count += 1, max_count += 1；
   - 遇到 ')'：min_count -= 1, max_count -= 1；
   - 遇到 '*'：min_count -= 1（视为右括号或空串）, max_count += 1（视为左括号）。
   每次转移后：
   - 若 max_count < 0：说明哪怕把所有的 '*' 全都当成左括号，右括号依然过剩，此时必无解，直接返回 False；
   - 若 min_count < 0：由于未匹配左括号数量不能为负（多出来的右括号可以通过把部分 '*' 转为空串来抵消），将 min_count 重置为 0。

3. 结果判断：
   遍历结束后，若 min_count == 0，说明存在某种括号分配方案使得未匹配左括号恰好为 0，返回 True；否则返回 False。

复杂度分析：
- 时间复杂度：O(n)，其中 n 为字符串 s 的长度。仅需线性遍历一次。
- 空间复杂度：O(1)，仅使用常数个计数变量。


方法二：双栈法（Stack，O(n) 空间）
1. 使用两个栈 left_stack 和 star_stack，分别存储 '(' 和 '*' 的下标。
2. 从左到右遍历字符串：
   - 遇到 '('，下标压入 left_stack；
   - 遇到 '*'，下标压入 star_stack；
   - 遇到 ')'，优先消耗真实的左括号（弹出 left_stack）；若没有左括号，再消耗星号（弹出 star_stack）；若两个栈均为空，说明有多余右括号，直接返回 False。
3. 遍历完后匹配剩余的左括号：
   - 剩余的左括号必须由位于其右侧的星号 '*' 来充当 ')' 匹配；
   - 比较两个栈顶下标：若 left_stack[-1] > star_stack[-1]，说明左括号出现在星号右侧，无法匹配，返回 False；
   - 否则两者均弹出。
4. 若 left_stack 最终为空，则说明全部匹配成功，返回 True。

复杂度分析：
- 时间复杂度：O(n)，每个元素最多入栈出栈各一次。
- 空间复杂度：O(n)，栈存储元素下标。
'''

