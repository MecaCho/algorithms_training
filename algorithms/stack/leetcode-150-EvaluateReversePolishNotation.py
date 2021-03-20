# encoding=utf8


'''
150. Evaluate Reverse Polish Notation
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, and /. Each operand may be an integer or another expression.

Note that division between two integers should truncate toward zero.

It is guaranteed that the given RPN expression is always valid. That means the expression would always evaluate to a result, and there will not be any division by zero operation.



Example 1:

Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
Example 2:

Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
Example 3:

Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22


Constraints:

1 <= tokens.length <= 104
tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].



150. 逆波兰表达式求值
根据 逆波兰表示法，求表达式的值。

有效的算符包括 +、-、*、/ 。每个运算对象可以是整数，也可以是另一个逆波兰表达式。



说明：

整数除法只保留整数部分。
给定逆波兰表达式总是有效的。换句话说，表达式总会得出有效数值且不存在除数为 0 的情况。


示例 1：

输入：tokens = ["2","1","+","3","*"]
输出：9
解释：该算式转化为常见的中缀算术表达式为：((2 + 1) * 3) = 9
示例 2：

输入：tokens = ["4","13","5","/","+"]
输出：6
解释：该算式转化为常见的中缀算术表达式为：(4 + (13 / 5)) = 6
示例 3：

输入：tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
输出：22
解释：
该算式转化为常见的中缀算术表达式为：
  ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22


提示：

1 <= tokens.length <= 104
tokens[i] 要么是一个算符（"+"、"-"、"*" 或 "/"），要么是一个在范围 [-200, 200] 内的整数


逆波兰表达式：

逆波兰表达式是一种后缀表达式，所谓后缀就是指算符写在后面。

平常使用的算式则是一种中缀表达式，如 ( 1 + 2 ) * ( 3 + 4 ) 。
该算式的逆波兰表达式写法为 ( ( 1 2 + ) ( 3 4 + ) * ) 。
逆波兰表达式主要有以下两个优点：

去掉括号后表达式无歧义，上式即便写成 1 2 + 3 4 + * 也可以依据次序计算出正确结果。
适合用栈操作运算：遇到数字则入栈；遇到算符则取出栈顶两个数字进行计算，并将结果压入栈中。
'''



class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for i in range(len(tokens)):
            if tokens[i] in "+-*/":
                a = stack.pop()
                b = stack.pop()
                if tokens[i] == "+":
                    tmp = a+b
                elif tokens[i] == "-":
                    tmp = b-a
                elif tokens[i] == "*":
                    tmp = b*a
                else:
                    tmp =  int(b/a) if a*b > 0 else -int(-b/a)
                stack.append(tmp)
            else:
                stack.append(int(tokens[i]))
        # print(stack)
        return stack[-1]


# solutions


'''
文字题解
前言
逆波兰表达式由波兰的逻辑学家卢卡西维兹提出。逆波兰表达式的特点是：没有括号，运算符总是放在和它相关的操作数之后。因此，逆波兰表达式也称后缀表达式。

方法一：栈
逆波兰表达式严格遵循「从左到右」的运算。计算逆波兰表达式的值时，使用一个栈存储操作数，从左到右遍历逆波兰表达式，进行如下操作：

如果遇到操作数，则将操作数入栈；

如果遇到运算符，则将两个操作数出栈，其中先出栈的是右操作数，后出栈的是左操作数，使用运算符对两个操作数进行运算，将运算得到的新操作数入栈。

整个逆波兰表达式遍历完毕之后，栈内只有一个元素，该元素即为逆波兰表达式的值。


1 / 15

JavaJavaScriptGolangPython3C++C

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op_to_binary_fn = {
            "+": add,
            "-": sub,
            "*": mul,
            "/": lambda x, y: int(x / y),   # 需要注意 python 中负数除法的表现与题目不一致
        }

        stack = list()
        for token in tokens:
            try:
                num = int(token)
            except ValueError:
                num2 = stack.pop()
                num1 = stack.pop()
                num = op_to_binary_fn[token](num1, num2)
            finally:
                stack.append(num)
            
        return stack[0]
复杂度分析

时间复杂度：O(n)O(n)，其中 nn 是数组 \textit{tokens}tokens 的长度。需要遍历数组 \textit{tokens}tokens 一次，计算逆波兰表达式的值。

空间复杂度：O(n)O(n)，其中 nn 是数组 \textit{tokens}tokens 的长度。使用栈存储计算过程中的数，栈内元素个数不会超过逆波兰表达式的长度。

方法二：数组模拟栈
方法一使用栈存储操作数。也可以使用一个数组模拟栈操作。

如果使用数组代替栈，则需要预先定义数组的长度。对于长度为 nn 的逆波兰表达式，显然栈内元素个数不会超过 nn，但是将数组的长度定义为 nn 仍然超过了栈内元素个数的上界。那么，栈内元素最多可能有多少个？

对于一个有效的逆波兰表达式，其长度 nn 一定是奇数，且操作数的个数一定比运算符的个数多 11 个，即包含 \frac{n+1}{2} 
2
n+1
​	
  个操作数和 \frac{n-1}{2} 
2
n−1
​	
  个运算符。考虑遇到操作数和运算符时，栈内元素个数分别会如何变化：

如果遇到操作数，则将操作数入栈，因此栈内元素增加 11 个；

如果遇到运算符，则将两个操作数出栈，然后将一个新操作数入栈，因此栈内元素先减少 22 个再增加 11 个，结果是栈内元素减少 11 个。

由此可以得到操作数和运算符与栈内元素个数变化的关系：遇到操作数时，栈内元素增加 11 个；遇到运算符时，栈内元素减少 11 个。

最坏情况下，\frac{n+1}{2} 
2
n+1
​	
  个操作数都在表达式的前面，\frac{n-1}{2} 
2
n−1
​	
  个运算符都在表达式的后面，此时栈内元素最多为 \frac{n+1}{2} 
2
n+1
​	
  个。在其余情况下，栈内元素总是少于 \frac{n+1}{2} 
2
n+1
​	
  个。因此，在任何情况下，栈内元素最多可能有 \frac{n+1}{2} 
2
n+1
​	
  个，将数组的长度定义为 \frac{n+1}{2} 
2
n+1
​	
  即可。

具体实现方面，创建数组 \textit{stack}stack 模拟栈，数组下标 00 的位置对应栈底，定义 \textit{index}index 表示栈顶元素的下标位置，初始时栈为空，\textit{index}=-1index=−1。当遇到操作数和运算符时，进行如下操作：

如果遇到操作数，则将 \textit{index}index 的值加 11，然后将操作数赋给 \textit{stack}[\textit{index}]stack[index]；

如果遇到运算符，则将 \textit{index}index 的值减 11，此时 \textit{stack}[\textit{index}]stack[index] 和 \textit{stack}[\textit{index}+1]stack[index+1] 的元素分别是左操作数和右操作数，使用运算符对两个操作数进行运算，将运算得到的新操作数赋给 \textit{stack}[\textit{index}]stack[index]。

整个逆波兰表达式遍历完毕之后，栈内只有一个元素，因此 \textit{index}=0index=0，此时 \textit{stack}[\textit{index}]stack[index] 即为逆波兰表达式的值。


1 / 15

JavaJavaScriptGolangPython3C++C

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op_to_binary_fn = {
            "+": add,
            "-": sub,
            "*": mul,
            "/": lambda x, y: int(x / y),   # 需要注意 python 中负数除法的表现与题目不一致
        }

        n = len(tokens)
        stack = [0] * ((n + 1) // 2)
        index = -1
        for token in tokens:
            try:
                num = int(token)
                index += 1
                stack[index] = num
            except ValueError:
                index -= 1
                stack[index] = op_to_binary_fn[token](stack[index], stack[index + 1])
            
        return stack[0]
复杂度分析

时间复杂度：O(n)O(n)，其中 nn 是数组 \textit{tokens}tokens 的长度。需要遍历数组 \textit{tokens}tokens 一次，计算逆波兰表达式的值。

空间复杂度：O(n)O(n)，其中 nn 是数组 \textit{tokens}tokens 的长度。需要创建长度为 \frac{n+1}{2} 
2
n+1
​	
  的数组模拟栈操作。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/evaluate-reverse-polish-notation/solution/ni-bo-lan-biao-da-shi-qiu-zhi-by-leetcod-wue9/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''

