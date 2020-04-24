'''
65. 有效数字
验证给定的字符串是否可以解释为十进制数字。

例如:

"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
" -90e3   " => true
" 1e" => false
"e3" => false
" 6e-1" => true
" 99e2.5 " => false
"53.5e93" => true
" --6 " => false
"-+3" => false
"95a54e53" => false

说明: 我们有意将问题陈述地比较模糊。在实现代码之前，你应当事先思考所有可能的情况。这里给出一份可能存在于有效十进制数字中的字符列表：

数字 0-9
指数 - "e"
正/负号 - "+"/"-"
小数点 - "."
当然，在输入中，这些字符的上下文也很重要。

更新于 2015-02-10:
C++函数的形式已经更新了。如果你仍然看见你的函数接收 const char * 类型的参数，请点击重载按钮重置你的代码。

65. Valid Number
Validate if a given string can be interpreted as a decimal number.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
" -90e3   " => true
" 1e" => false
"e3" => false
" 6e-1" => true
" 99e2.5 " => false
"53.5e93" => true
" --6 " => false
"-+3" => false
"95a54e53" => false

Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up front before implementing one. However, here is a list of characters that can be in a valid decimal number:

Numbers 0-9
Exponent - "e"
Positive/negative sign - "+"/"-"
Decimal point - "."
Of course, the context of these characters also matters in the input.

Update (2015-02-10):
The signature of the C++ function had been updated. If you still see your function signature accepts a const char * argument, please click the reload button to reset your code definition.
'''

import re


class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        try:
            float(s)
            return True
        except:
            return False
        # return bool(re.match(r"[+-]?([0-9]+|[\.]?[0-9]*)([0-9]+|[\.]?[0-9]+[e]?[+-]?[0-9]*)", str(s).strip()))


class Solution1(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # "-1E-16"
        return bool(re.match(r"^[-+]?(\.\d+|\d+\.?\d*)([eE][-+]?\d+)?$", s.strip()))



if __name__ == '__main__':
    s = "123e10"
    import string
    print(s.isnumeric())
    res = re.match(r' *[+-]?([0-9]+(\.[0-9]*)?|\.[0-9]+)(e[+-]?[0-9]+)? *$', s)
    print(res)

    demo = Solution1()
    for s in ["+100", "5e2", "-123", "3.1416", "0123", "-1E-16", " ", "12e", "1a3.14", "1.2.3", "+-5", "12e+5.4"]:
        print(s, demo.isNumber(s))



'''
方法一：逻辑判断法
使用3个标志位met_dot, met_e, met_digit来分别标记是否遇到了“.”,“e/E”和任何0-9的数字。
当然首先要去掉首位的空格。

代码
class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        met_dot = met_e = met_digit = False
        for i, char in enumerate(s):
            if char in ('+', '-'):
                if i > 0 and s[i-1] != 'e' and s[i-1] != 'E':
                    return False
            elif char == '.':
                if met_dot or met_e: 
                    return False
                met_dot = True
            elif char == 'e' or char == 'E':
                if met_e or not met_digit:
                    return False
                met_e, met_digit = True, False # e后必须接，所以这时重置met_digit为False,以免e为最后一个char
            elif char.isdigit():
                met_digit = True
            else:
                return False
        return met_digit
方法二：拆分法
可以写成 A[.[B]][e/EC], 即有整数存在时，和无整数存在时的 .B[e/EC]。
A为数值整数部分（可以有正负号的整数），B为紧跟着小数点的为数值的小数部分（无正负号的整数），
C为紧跟着e/E为数值的指数部分（可以有正负号的整数）。
整体的逻辑为：
1.因为[e/EC]可存在可不存在，影响最小，所以一开始我们就可以先搞定C：
如果e/E存在则C为isInteger()扫描后的返回值，不然就为True（所有的返回我们都带上and C）
2.如果存在小数点：
(1)如果A不存在则B必须存在：
如果B不存在：return False
否则return B and C
(2)如果B存在：
return A and B and C
否则return A and C
3.如果不存在小数点：
return A and C

代码
class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip()
        if not s: return False
        dot_pos = s.find(".")
        e, E = s.find("e"), s.find("E")
        e_pos =  e if e != -1 else E
        if e_pos != -1 and e_pos < dot_pos: return False # e/E后不能有小数
        C = self.isInteger(s, e_pos+1, len(s)-1) if e_pos != -1 else True
        if dot_pos != -1:
            B = self.isUnsignedInteger(s, dot_pos+1, e_pos-1 if (e_pos != -1) else (len(s)-1))
            if dot_pos == 0 or (dot_pos == 1 and s[0] in ("+", "-")): # 如果A不存在，B必须存在
                if dot_pos == len(s)-1 or dot_pos + 1 == e_pos: return False # 如果B不存在
                return B and C
            A = self.isInteger(s, 0, dot_pos-1)
            if not(dot_pos == len(s)-1 or dot_pos + 1 == e_pos): # 如果B存在
                return A and B and C
            return A and C
        A = self.isInteger(s, 0, e_pos-1 if (e_pos != -1) else (len(s)-1))
        return A and C

    def isInteger(self, s, i, j):
        if 0 <= i < len(s) and 0 <= j < len(s):
            if s[i] in ("+", "-"):
                i += 1
            return self.isUnsignedInteger(s, i, j)
        return False

    def isUnsignedInteger(self, s, i, j):
        if i > j: return False # 不能为空
        if 0 <= i < len(s) and 0 <= j < len(s):
            for index in range(i, j+1):
                if not s[index].isdigit():
                    return False
            return True
        return False
方法三：正则表达式
按照法一的思路，可得正则表达式：
^[+-]?(\.\d+|\d+\.?\d*)([eE][+-]?\d+)?$

代码
import re
class Solution:
    p = re.compile(r'^[+-]?(\.\d+|\d+\.?\d*)([eE][+-]?\d+)?$')
    def isNumber(self, s: str) -> bool:
        return bool(self.p.match(s.strip()))
方法四：DFA(deterministic finite automaton, 确定性有限自动机)
见代码内注释

代码
class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #define DFA state transition tables
        states = [{},
                 # State (1) - initial state (scan ahead thru blanks)
                 {'blank': 1, 'sign': 2, 'digit':3, '.':4},
                 # State (2) - found sign (expect digit/dot)
                 {'digit':3, '.':4},
                 # State (3) - digit consumer (loop until non-digit)
                 {'digit':3, '.':5, 'e':6, 'blank':9},
                 # State (4) - found dot (only a digit is valid)
                 {'digit':5},
                 # State (5) - after dot (expect digits, e, or end of valid input)
                 {'digit':5, 'e':6, 'blank':9},
                 # State (6) - found 'e' (only a sign or digit valid)
                 {'sign':7, 'digit':8},
                 # State (7) - sign after 'e' (only digit)
                 {'digit':8},
                 # State (8) - digit after 'e' (expect digits or end of valid input)
                 {'digit':8, 'blank':9},
                 # State (9) - Terminal state (fail if non-blank found)
                 {'blank':9}]
        currentState = 1
        for c in s:
            # If char c is of a known class set it to the class name
            if c in '0123456789':
                c = 'digit'
            elif c in ' \t\n':
                c = 'blank'
            elif c in '+-':
                c = 'sign'
            # If char/class is not in our state transition table it is invalid input
            if c not in states[currentState]:
                return False
            # State transition
            currentState = states[currentState][c]
        # The only valid terminal states are end on digit, after dot, digit after e, or white space after valid input
        if currentState not in [3,5,8,9]:
            return False
        return True
方法五： try/except法
class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        try:
            float(s)
            return True
        except :
            return False

作者：victoria-zhou
链接：https://leetcode-cn.com/problems/biao-shi-shu-zhi-de-zi-fu-chuan-lcof/solution/onpythonjie-ti-wu-fa-luo-ji-pan-duan-regexdfadeng-/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''