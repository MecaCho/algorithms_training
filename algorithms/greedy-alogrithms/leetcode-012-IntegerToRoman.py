# encoding=utf8


'''

12. Integer to Roman
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.

Example 1:

Input: 3
Output: "III"
Example 2:

Input: 4
Output: "IV"
Example 3:

Input: 9
Output: "IX"
Example 4:

Input: 58
Output: "LVIII"
Explanation: L = 50, V = 5, III = 3.
Example 5:

Input: 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
12. 整数转罗马数字
罗马数字包含以下七种字符： I， V， X， L，C，D 和 M。

字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。

通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：

I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
给定一个整数，将其转为罗马数字。输入确保在 1 到 3999 的范围内。

示例 1:

输入: 3
输出: "III"
示例 2:

输入: 4
输出: "IV"
示例 3:

输入: 9
输出: "IX"
示例 4:

输入: 58
输出: "LVIII"
解释: L = 50, V = 5, III = 3.
示例 5:

输入: 1994
输出: "MCMXCIV"
解释: M = 1000, CM = 900, XC = 90, IV = 4.
'''

# 贪心算法

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        hash_map = (
            ("M", 1000),("CM", 900),  ("D", 500),("CD", 400), ("C", 100), ("XC", 90), ("L", 50), ("XL", 40), 
            ("X", 10), ("IX", 9), ("V", 5),("IV", 4), ("I", 1)
        )

        res = ""
        for k, value in hash_map:
            while (num / value) > 0:
                res += k * (num / value)
                num = num % value
        # print res, "result"
        return res

    
# golang solution

'''
func intToRoman(num int) string {
	vals := []string{"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"}
	keys := []int{1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1}
	res := []byte{}
	for i, key := range keys {
		for num >= key {
			num -= key
			res = append(res, vals[i]...)
		}
		if num == 0 {
			break
		}
	}
	return string(res)
}
'''

# solutions

'''
罗马数字符号

罗马数字由 77 个不同的单字母符号组成，每个符号对应一个具体的数值。此外，减法规则（如问题描述中所述）给出了额外的 66 个复合符号。这给了我们总共 1313 个独特的符号（每个符号由 11 个或 22 个字母组成），如下图所示。



罗马数字的唯一表示法

让我们从一个例子入手。考虑 140140 的罗马数字表示，下面哪一个是正确的？



我们用来确定罗马数字的规则是：对于罗马数字从左到右的每一位，选择尽可能大的符号值。对于 140140，最大可以选择的符号值为 \texttt{C}=100C=100。接下来，对于剩余的数字 4040，最大可以选择的符号值为 \texttt{XL}=40XL=40。因此，140140 的对应的罗马数字为 \texttt{C}+\texttt{XL}=\texttt{CXL}C+XL=CXL。

方法一：模拟
思路

根据罗马数字的唯一表示法，为了表示一个给定的整数 \textit{num}num，我们寻找不超过 \textit{num}num 的最大符号值，将 \textit{num}num 减去该符号值，然后继续寻找不超过 \textit{num}num 的最大符号值，将该符号拼接在上一个找到的符号之后，循环直至 \textit{num}num 为 00。最后得到的字符串即为 \textit{num}num 的罗马数字表示。

编程时，可以建立一个数值-符号对的列表 \textit{valueSymbols}valueSymbols，按数值从大到小排列。遍历 \textit{valueSymbols}valueSymbols 中的每个数值-符号对，若当前数值 \textit{value}value 不超过 \textit{num}num，则从 \textit{num}num 中不断减去 \textit{value}value，直至 \textit{num}num 小于 \textit{value}value，然后遍历下一个数值-符号对。若遍历中 \textit{num}num 为 00 则跳出循环。

代码

C++JavaC#GolangJavaScriptPython3C

var valueSymbols = []struct {
    value  int
    symbol string
}{
    {1000, "M"},
    {900, "CM"},
    {500, "D"},
    {400, "CD"},
    {100, "C"},
    {90, "XC"},
    {50, "L"},
    {40, "XL"},
    {10, "X"},
    {9, "IX"},
    {5, "V"},
    {4, "IV"},
    {1, "I"},
}

func intToRoman(num int) string {
    roman := []byte{}
    for _, vs := range valueSymbols {
        for num >= vs.value {
            num -= vs.value
            roman = append(roman, vs.symbol...)
        }
        if num == 0 {
            break
        }
    }
    return string(roman)
}
复杂度分析

时间复杂度：O(1)O(1)。由于 \textit{valueSymbols}valueSymbols 长度是固定的，且这 1313 字符中的每个字符的出现次数均不会超过 33，因此循环次数有一个确定的上限。对于本题给出的数据范围，循环次数不会超过 1515 次。

空间复杂度：O(1)O(1)。

方法二：硬编码数字
思路



回顾前言中列出的这 1313 个符号，可以发现：

千位数字只能由 \texttt{M}M 表示；
百位数字只能由 \texttt{C}C，\texttt{CD}CD，\texttt{D}D 和 \texttt{CM}CM 表示；
十位数字只能由 \texttt{X}X，\texttt{XL}XL，\texttt{L}L 和 \texttt{XC}XC 表示；
个位数字只能由 \texttt{I}I，\texttt{IV}IV，\texttt{V}V 和 \texttt{IX}IX 表示。
这恰好把这 1313 个符号分为四组，且组与组之间没有公共的符号。因此，整数 \textit{num}num 的十进制表示中的每一个数字都是可以单独处理的。

进一步地，我们可以计算出每个数字在每个位上的表示形式，整理成一张硬编码表。如下图所示，其中 00 对应的是空字符串。



利用模运算和除法运算，我们可以得到 \textit{num}num 每个位上的数字：


thousands_digit = num / 1000
hundreds_digit = (num % 1000) / 100
tens_digit = (num % 100) / 10
ones_digit = num % 10
最后，根据 \textit{num}num 每个位上的数字，在硬编码表中查找对应的罗马字符，并将结果拼接在一起，即为 \textit{num}num 对应的罗马数字。

代码

C++JavaC#GolangJavaScriptPython3C

var (
    thousands = []string{"", "M", "MM", "MMM"}
    hundreds  = []string{"", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"}
    tens      = []string{"", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"}
    ones      = []string{"", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"}
)

func intToRoman(num int) string {
    return thousands[num/1000] + hundreds[num%1000/100] + tens[num%100/10] + ones[num%10]
}
复杂度分析

时间复杂度：O(1)O(1)。计算量与输入数字的大小无关。

空间复杂度：O(1)O(1)。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/integer-to-roman/solution/zheng-shu-zhuan-luo-ma-shu-zi-by-leetcod-75rs/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
