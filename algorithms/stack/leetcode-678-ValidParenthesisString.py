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
