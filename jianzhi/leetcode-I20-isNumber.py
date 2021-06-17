# encoding=utf8

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

        
class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
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

# solution

'''
方法一：确定有限状态自动机
预备知识

确定有限状态自动机（以下简称「自动机」）是一类计算模型。它包含一系列状态，这些状态中：

有一个特殊的状态，被称作「初始状态」。
还有一系列状态被称为「接受状态」，它们组成了一个特殊的集合。其中，一个状态可能既是「初始状态」，也是「接受状态」。
起初，这个自动机处于「初始状态」。随后，它顺序地读取字符串中的每一个字符，并根据当前状态和读入的字符，按照某个事先约定好的「转移规则」，从当前状态转移到下一个状态；当状态转移完成后，它就读取下一个字符。当字符串全部读取完毕后，如果自动机处于某个「接受状态」，则判定该字符串「被接受」；否则，判定该字符串「被拒绝」。

注意：如果输入的过程中某一步转移失败了，即不存在对应的「转移规则」，此时计算将提前中止。在这种情况下我们也判定该字符串「被拒绝」。

一个自动机，总能够回答某种形式的「对于给定的输入字符串 S，判断其是否满足条件 P」的问题。在本题中，条件 P 即为「构成合法的表示数值的字符串」。

自动机驱动的编程，可以被看做一种暴力枚举方法的延伸：它穷尽了在任何一种情况下，对应任何的输入，需要做的事情。

自动机在计算机科学领域有着广泛的应用。在算法领域，它与大名鼎鼎的字符串查找算法「KMP」算法有着密切的关联；在工程领域，它是实现「正则表达式」的基础。

问题描述

在 C++ 文档 中，描述了一个合法的数值字符串应当具有的格式。具体而言，它包含以下部分：

符号位，即 ++、-− 两种符号
整数部分，即由若干字符 0-90−9 组成的字符串
小数点
小数部分，其构成与整数部分相同
指数部分，其中包含开头的字符 \text{e}e（大写小写均可）、可选的符号位，和整数部分
相比于 C++ 文档而言，本题还有一点额外的不同，即允许字符串首末两端有一些额外的空格。

在上面描述的五个部分中，每个部分都不是必需的，但也受一些额外规则的制约，如：

如果符号位存在，其后面必须跟着数字或小数点。
小数点的前后两侧，至少有一侧是数字。
思路与算法

根据上面的描述，现在可以定义自动机的「状态集合」了。那么怎么挖掘出所有可能的状态呢？一个常用的技巧是，用「当前处理到字符串的哪个部分」当作状态的表述。根据这一技巧，不难挖掘出所有状态：

起始的空格
符号位
整数部分
左侧有整数的小数点
左侧无整数的小数点（根据前面的第二条额外规则，需要对左侧有无整数的两种小数点做区分）
小数部分
字符 \text{e}e
指数部分的符号位
指数部分的整数部分
末尾的空格
下一步是找出「初始状态」和「接受状态」的集合。根据题意，「初始状态」应当为状态 1，而「接受状态」的集合则为状态 3、状态 4、状态 6、状态 9 以及状态 10。换言之，字符串的末尾要么是空格，要么是数字，要么是小数点，但前提是小数点的前面有数字。

最后，需要定义「转移规则」。结合数值字符串应当具备的格式，将自动机转移的过程以图解的方式表示出来：



比较上图与「预备知识」一节中对自动机的描述，可以看出有一点不同：

我们没有单独地考虑每种字符，而是划分为若干类。由于全部 1010 个数字字符彼此之间都等价，因此只需定义一种统一的「数字」类型即可。对于正负号也是同理。
在实际代码中，我们需要处理转移失败的情况。例如当位于状态 1（起始空格）时，没有对应字符 \text{e}e 的状态。为了处理这种情况，我们可以创建一个特殊的拒绝状态。如果当前状态下没有对应读入字符的「转移规则」，我们就转移到这个特殊的拒绝状态。一旦自动机转移到这个特殊状态，我们就可以立即判定该字符串不「被接受」。

代码

可以很简单地将上面的状态转移图翻译成代码：

C++JavaGolangCPython3

from enum import Enum

class Solution:
    def isNumber(self, s: str) -> bool:
        State = Enum("State", [
            "STATE_INITIAL",
            "STATE_INT_SIGN",
            "STATE_INTEGER",
            "STATE_POINT",
            "STATE_POINT_WITHOUT_INT",
            "STATE_FRACTION",
            "STATE_EXP",
            "STATE_EXP_SIGN",
            "STATE_EXP_NUMBER",
            "STATE_END",
        ])
        Chartype = Enum("Chartype", [
            "CHAR_NUMBER",
            "CHAR_EXP",
            "CHAR_POINT",
            "CHAR_SIGN",
            "CHAR_SPACE",
            "CHAR_ILLEGAL",
        ])

        def toChartype(ch: str) -> Chartype:
            if ch.isdigit():
                return Chartype.CHAR_NUMBER
            elif ch.lower() == "e":
                return Chartype.CHAR_EXP
            elif ch == ".":
                return Chartype.CHAR_POINT
            elif ch == "+" or ch == "-":
                return Chartype.CHAR_SIGN
            elif ch == " ":
                return Chartype.CHAR_SPACE
            else:
                return Chartype.CHAR_ILLEGAL
        
        transfer = {
            State.STATE_INITIAL: {
                Chartype.CHAR_SPACE: State.STATE_INITIAL,
                Chartype.CHAR_NUMBER: State.STATE_INTEGER,
                Chartype.CHAR_POINT: State.STATE_POINT_WITHOUT_INT,
                Chartype.CHAR_SIGN: State.STATE_INT_SIGN,
            },
            State.STATE_INT_SIGN: {
                Chartype.CHAR_NUMBER: State.STATE_INTEGER,
                Chartype.CHAR_POINT: State.STATE_POINT_WITHOUT_INT,
            },
            State.STATE_INTEGER: {
                Chartype.CHAR_NUMBER: State.STATE_INTEGER,
                Chartype.CHAR_EXP: State.STATE_EXP,
                Chartype.CHAR_POINT: State.STATE_POINT,
                Chartype.CHAR_SPACE: State.STATE_END,
            },
            State.STATE_POINT: {
                Chartype.CHAR_NUMBER: State.STATE_FRACTION,
                Chartype.CHAR_EXP: State.STATE_EXP,
                Chartype.CHAR_SPACE: State.STATE_END,
            },
            State.STATE_POINT_WITHOUT_INT: {
                Chartype.CHAR_NUMBER: State.STATE_FRACTION,
            },
            State.STATE_FRACTION: {
                Chartype.CHAR_NUMBER: State.STATE_FRACTION,
                Chartype.CHAR_EXP: State.STATE_EXP,
                Chartype.CHAR_SPACE: State.STATE_END,
            },
            State.STATE_EXP: {
                Chartype.CHAR_NUMBER: State.STATE_EXP_NUMBER,
                Chartype.CHAR_SIGN: State.STATE_EXP_SIGN,
            },
            State.STATE_EXP_SIGN: {
                Chartype.CHAR_NUMBER: State.STATE_EXP_NUMBER,
            },
            State.STATE_EXP_NUMBER: {
                Chartype.CHAR_NUMBER: State.STATE_EXP_NUMBER,
                Chartype.CHAR_SPACE: State.STATE_END,
            },
            State.STATE_END: {
                Chartype.CHAR_SPACE: State.STATE_END,
            },
        }

        st = State.STATE_INITIAL
        for ch in s:
            typ = toChartype(ch)
            if typ not in transfer[st]:
                return False
            st = transfer[st][typ]
        
        return st in [State.STATE_INTEGER, State.STATE_POINT, State.STATE_FRACTION, State.STATE_EXP_NUMBER, State.STATE_END]
复杂度分析

时间复杂度：O(N)O(N)，其中 NN 为字符串的长度。我们需要遍历字符串的每个字符，其中状态转移所需的时间复杂度为 O(1)O(1)。
空间复杂度：O(1)O(1)。只需要创建固定大小的状态转移表。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/biao-shi-shu-zhi-de-zi-fu-chuan-lcof/solution/biao-shi-shu-zhi-de-zi-fu-chuan-by-leetcode-soluti/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''


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
