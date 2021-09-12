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
 

Constraints:

1 <= s.length <= 100
s[i] is '(', ')' or '*'.
'''

class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l_stack = []
        s_stack = []
        for i in range(len(s)):
            if s[i] == "(":
                l_stack.append(i)
            elif s[i] == "*":
                s_stack.append(i)
            elif len(l_stack) > 0:
                l_stack.pop()
            elif len(s_stack) > 0:
                s_stack.pop()
            else:
                return False

        l = len(l_stack) - 1
        s = len(s_stack) - 1

        if s < l:
            return False
        while s >= 0 and l >= 0:
            if l_stack[l] > s_stack[s]:
                s -= 1
            else:
                s -= 1
                l -= 1

        return l < 0

# golang solution

'''
func checkValidString(s string) bool {
	minCount, maxCount := 0, 0
	for _, ch := range s {
		if string(ch) == "(" {
			minCount++
			maxCount++
		} else if string(ch) == ")" {
			minCount--
			maxCount--
            if maxCount < 0{
                return false
            }
		} else {
			minCount--
			maxCount++
		}
		if minCount < 0{
			minCount = 0
		}
	}
	return minCount == 0
}
'''
