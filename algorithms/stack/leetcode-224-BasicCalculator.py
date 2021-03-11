# encoding=utf8

'''
224. Basic Calculator
Given a string s representing an expression,
implement a basic calculator to evaluate it.



Example 1:

Input: s = "1 + 1"
Output: 2
Example 2:

Input: s = " 2-1 + 2 "
Output: 3
Example 3:

Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23


Constraints:

1 <= s.length <= 3 * 105
s consists of digits, '+', '-', '(', ')', and ' '.
s represents a valid expression.


224. 基本计算器
实现一个基本的计算器来计算一个简单的字符串表达式 s 的值。



示例 1：

输入：s = "1 + 1"
输出：2
示例 2：

输入：s = " 2-1 + 2 "
输出：3
示例 3：

输入：s = "(1+(4+5+2)-3)+(6+8)"
输出：23


提示：

1 <= s.length <= 3 * 105
s 由数字、'+'、'-'、'('、')'、和 ' ' 组成
s 表示一个有效的表达式
'''


class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        op = [1]
        sign = 1
        n = len(s)
        i = 0
        res = 0
        while i < n:
            if s[i] == " ":
                # print(i)
                i += 1
            elif s[i] == "+":
                sign = op[-1]
                i += 1
            elif s[i] == "-":
                sign = -op[-1]
                i += 1
            elif s[i] == "(":
                op.append(sign)
                i += 1
            elif s[i] == ")":
                op.pop()
                i += 1
            else:
                num = 0
                while i < n and '0' <= s[i] <= '9':
                    num = num * 10 + int(s[i])
                    i += 1
                # print(sign * num, op)
                res += sign * num

        return res


# golang solution

'''
func calculate(s string) int {
    ops := []int{1}
    sign := 1
    n := len(s)
    res := 0
    for i := 0; i < n; {
        switch s[i] {
        case ' ':
            i++
        case '+':
            sign = ops[len(ops)-1]
            i++
        case '-':
            sign = -ops[len(ops)-1]
            i++
        case '(':
            ops = append(ops, sign)
            i++
        case ')':
            ops = ops[:len(ops)-1]
            i++
        default:
            num := 0
            for ; i < n && '0' <= s[i] && s[i] <= '9'; i++ {
                num = num*10 + int(s[i]-'0')
            }
            res += sign * num
        }
    }
    return res

}
'''


# solutions

'''
方法一：括号展开 + 栈
由于字符串除了数字与括号外，只有加号和减号两种运算符。因此，如果展开表达式中所有的括号，则得到的新表达式中，数字本身不会发生变化，只是每个数字前面的符号会发生变化。

因此，我们考虑使用一个取值为 \{-1,+1\}{−1,+1} 的整数 \textit{sign}sign 代表「当前」的符号。根据括号表达式的性质，它的取值：

与字符串中当前位置的运算符有关；
如果当前位置处于一系列括号之内，则也与这些括号前面的运算符有关：每当遇到一个以 -− 号开头的括号，则意味着此后的符号都要被「翻转」。
考虑到第二点，我们需要维护一个栈 \textit{ops}ops，其中栈顶元素记录了当前位置所处的每个括号所「共同形成」的符号。例如，对于字符串 \text{1+2+(3-(4+5))}1+2+(3-(4+5))：

扫描到 \text{1+2}1+2 时，由于当前位置没有被任何括号所包含，则栈顶元素为初始值 +1+1；
扫描到 \text{1+2+(3}1+2+(3 时，当前位置被一个括号所包含，该括号前面的符号为 ++ 号，因此栈顶元素依然 +1+1；
扫描到 \text{1+2+(3-(4}1+2+(3-(4 时，当前位置被两个括号所包含，分别对应着 ++ 号和 -− 号，由于 ++ 号和 -− 号合并的结果为 -− 号，因此栈顶元素变为 -1−1。
在得到栈 \textit{ops}ops 之后， \textit{sign}sign 的取值就能够确定了：如果当前遇到了 ++ 号，则更新 \textit{sign} \leftarrow \text{ops.top()}sign←ops.top()；如果遇到了遇到了 -− 号，则更新 \textit{sign} \leftarrow -\text{ops.top()}sign←−ops.top()。

然后，每当遇到 (( 时，都要将当前的 \textit{sign}sign 取值压入栈中；每当遇到 )) 时，都从栈中弹出一个元素。这样，我们能够在扫描字符串的时候，即时地更新 \textit{ops}ops 中的元素。

C++JavaJavaScriptGolangC

func calculate(s string) (ans int) {
    ops := []int{1}
    sign := 1
    n := len(s)
    for i := 0; i < n; {
        switch s[i] {
        case ' ':
            i++
        case '+':
            sign = ops[len(ops)-1]
            i++
        case '-':
            sign = -ops[len(ops)-1]
            i++
        case '(':
            ops = append(ops, sign)
            i++
        case ')':
            ops = ops[:len(ops)-1]
            i++
        default:
            num := 0
            for ; i < n && '0' <= s[i] && s[i] <= '9'; i++ {
                num = num*10 + int(s[i]-'0')
            }
            ans += sign * num
        }
    }
    return
}
复杂度分析

时间复杂度：O(n)O(n)，其中 nn 为字符串 ss 的长度。需要遍历字符串 ss 一次，计算表达式的值。

空间复杂度：O(n)O(n)，其中 nn 为字符串 ss 的长度。空间复杂度主要取决于栈的空间，栈中的元素数量不超过 nn。

备注
本题有多种基于栈这一数据结构的解法，每种解法基于相近的思路，但具有完全不同的实现方式。感兴趣的读者可以尝试阅读其他基于栈的解法，本题解不再一一列举。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/basic-calculator/solution/ji-ben-ji-suan-qi-by-leetcode-solution-jvir/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''

