'''
394. 字符串解码
给定一个经过编码的字符串，返回它解码后的字符串。

编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。

你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。

此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。

示例:

s = "3[a]2[bc]", 返回 "aaabcbc".
s = "3[a2[c]]", 返回 "accaccacc".
s = "2[abc]3[cd]ef", 返回 "abcabccdcdcdef".

394. Decode String
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

Examples:

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
'''


class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ''
        i = 0

        if not s:
            return ""
        while i < len(s):
            if "0" <= s[i] <= "9":
                num = int(s[i])
                while "0" <= s[i+1] <= "9":
                    num = 10*num + int(s[i+1])
                    i += 1
                # num = int(num)
                print(num, i)
                j = i+1
                if s[i+1] == "[":
                    j = i + 2
                    left = 0
                    while s[j] != "]" or left != 0:
                        if s[j] == "[":
                            left += 1
                        if s[j] == "]":
                            left -= 1
                        j += 1
                res += num * self.decodeString(s[i+2:j])
                i = j+1
            else:
                res += s[i]
                i += 1
        return res


if __name__ == '__main__':
    demo = Solution()
    l = ["3[a2[c]]", "3[a]2[bc]", "2[abc]3[cd]ef"]
    for s in l:
        res = demo.decodeString(s)
        print(res)



'''
方法一：栈操作
思路和算法

本题中可能出现括号嵌套的情况，比如 2[a2[bc]]，这种情况下我们可以先转化成 2[abcbc]，在转化成 abcbcabcbc。我们可以把字母、数字和括号看成是独立的 TOKEN，并用栈来维护这些 TOKEN。具体的做法是，遍历这个栈：

如果当前的字符为数位，解析出一个数字（连续的多个数位）并进栈
如果当前的字符为字母或者左括号，直接进栈
如果当前的字符为右括号，开始出栈，一直到左括号出栈，出栈序列反转后拼接成一个字符串，此时取出栈顶的数字（此时栈顶一定是数字，想想为什么？），就是这个字符串应该出现的次数，我们根据这个次数和字符串构造出新的字符串并进栈
重复如上操作，最终将栈中的元素按照从栈底到栈顶的顺序拼接起来，就得到了答案。注意：这里可以用不定长数组来模拟栈操作，方便从栈底向栈顶遍历。

C++JavaGolang
func decodeString(s string) string {
    stk := []string{}
    ptr := 0
    for ptr < len(s) {
        cur := s[ptr]
        if cur >= '0' && cur <= '9' {
            digits := getDigits(s, &ptr)
            stk = append(stk, digits)
        } else if (cur >= 'a' && cur <= 'z' || cur >= 'A' && cur <= 'Z') || cur == '[' {
            stk = append(stk, string(cur))
            ptr++
        } else {
            ptr++
            sub := []string{}
            for stk[len(stk)-1] != "[" {
                sub = append(sub, stk[len(stk)-1])
                stk = stk[:len(stk)-1]
            }
            for i := 0; i < len(sub)/2; i++ {
                sub[i], sub[len(sub)-i-1] = sub[len(sub)-i-1], sub[i]
            }
            stk = stk[:len(stk)-1]
            repTime, _ := strconv.Atoi(stk[len(stk)-1])
            stk = stk[:len(stk)-1]
            t := strings.Repeat(getString(sub), repTime)
            stk = append(stk, t)
        }
    }
    return getString(stk)
}

func getDigits(s string, ptr *int) string {
    ret := ""
    for ; s[*ptr] >= '0' && s[*ptr] <= '9'; *ptr++ {
        ret += string(s[*ptr])
    }
    return ret
}

func getString(v []string) string {
    ret := ""
    for _, s := range v {
        ret += s
    }
    return ret
}
复杂度分析

时间复杂度：记解码后得出的字符串长度为 SS，除了遍历一次原字符串 ss，我们还需要将解码后的字符串中的每个字符都入栈，并最终拼接进答案中，故渐进时间复杂度为 O(S+|s|)O(S+∣s∣)，即 O(S)O(S)。
空间复杂度：记解码后得出的字符串长度为 SS，这里用栈维护 TOKEN，栈的总大小最终与 SS 相同，故渐进空间复杂度为 O(S)O(S)。
方法二：递归
思路和算法

我们也可以用递归来解决这个问题，从左向右解析字符串：

如果当前位置为数字位，那么后面一定包含一个用方括号表示的字符串，即属于这种情况：k[...]：
我们可以先解析出一个数字，然后解析到了左括号，递归向下解析后面的内容，遇到对应的右括号就返回，此时我们可以根据解析出的数字 xx 解析出的括号里的字符串 s's 
′
  构造出一个新的字符串 x \times s'x×s 
′
 ；
我们把 k[...] 解析结束后，再次调用递归函数，解析右括号右边的内容。
如果当前位置是字母位，那么我们直接解析当前这个字母，然后递归向下解析这个字母后面的内容。
如果觉得这里讲的比较抽象，可以结合代码理解一下这个过程。

下面我们可以来讲讲这样做的依据，涉及到《编译原理》相关内容，感兴趣的同学可以参考阅读。 根据题目的定义，我们可以推导出这样的巴科斯范式（BNF）：

\begin{aligned} {\rm String} &\rightarrow { \rm Digits \, [String] \, String \, | \, Alpha \, String \, | \, \epsilon } \\ {\rm Digits} &\rightarrow { \rm Digit \, Digits \, | \, Digit } \\ {\rm Alpha} &\rightarrow { a | \cdots | z | A | \cdots | Z } \\ {\rm Digit} &\rightarrow { 0 | \cdots | 9 } \\ \end{aligned}
String
Digits
Alpha
Digit
​	
  
→Digits[String]String∣AlphaString∣ϵ
→DigitDigits∣Digit
→a∣⋯∣z∣A∣⋯∣Z
→0∣⋯∣9
​	
 

\rm DigitDigit 表示十进制数位，可能的取值是 00 到 99 之间的整数
\rm AlphaAlpha 表示字母，可能的取值是大小写字母的集合，共 5252 个
\rm DigitDigit 表示一个整数，它的组成是 \rm DigitDigit 出现一次或多次
\rm StringString 代表一个代解析的字符串，它可能有三种构成，如 BNF 所示
\rm \epsilonϵ 表示空串，即没有任何子字符
由于 \rm DigitsDigits 和 \rm AlphaAlpha 构成简单，很容易进行词法分析，我们把它他们看作独立的 TOKEN。那么此时的非终结符有 \rm StringString，终结符有 \rm DigitsDigits、\rm AlphaAlpha 和 \rm \epsilonϵ，我们可以根据非终结符和 FOLLOW 集构造出这样的预测分析表：

\rm AlphaAlpha	\rm DigitsDigits	\rm \epsilonϵ
\rm StringString	\rm String \rightarrow Alpha \, StringString→AlphaString	\rm String \rightarrow Digits \, [String] \, StringString→Digits[String]String	\rm String \rightarrow \epsilonString→ϵ
可见不含多重定义的项，为 LL(1) 文法，即：

从左向右分析（Left-to-right-parse）
最左推导（Leftmost-derivation）
超前查看一个符号（1-symbol lookahead）
它决定了我们从左向右遍历这个字符串，每次只判断当前最左边的一个字符的分析方法是正确的。

代码如下。

C++JavaGolang
var (
    src string
    ptr int
)

func decodeString(s string) string {
    src = s
    ptr = 0
    return getString()
}

func getString() string {
    if ptr == len(src) || src[ptr] == ']' {
        return ""
    }
    cur := src[ptr]
    repTime := 1
    ret := ""
    if cur >= '0' && cur <= '9' {
        repTime = getDigits()
        ptr++
        str := getString()
        ptr++
        ret = strings.Repeat(str, repTime)
    } else if cur >= 'a' && cur <= 'z' || cur >= 'A' && cur <= 'Z' {
        ret = string(cur)
        ptr++
    }
    return ret + getString()
}

func getDigits() int {
    ret := 0
    for ; src[ptr] >= '0' && src[ptr] <= '9'; ptr++ {
        ret = ret * 10 + int(src[ptr] - '0')
    }
    return ret
}
复杂度分析

时间复杂度：记解码后得出的字符串长度为 SS，除了遍历一次原字符串 ss，我们还需要将解码后的字符串中的每个字符都拼接进答案中，故渐进时间复杂度为 O(S+|s|)O(S+∣s∣)，即 O(S)O(S)。
空间复杂度：若不考虑答案所占用的空间，那么就只剩递归使用栈空间的大小，这里栈空间的使用和递归树的深度成正比，最坏情况下为 O(|s|)O(∣s∣)，故渐进空间复杂度为 O(|s|)O(∣s∣)。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/decode-string/solution/zi-fu-chuan-jie-ma-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''