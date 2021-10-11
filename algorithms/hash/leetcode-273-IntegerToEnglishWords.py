# encoding=utf8


'''
273. Integer to English Words
Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.

Example 1:

Input: 123
Output: "One Hundred Twenty Three"
Example 2:

Input: 12345
Output: "Twelve Thousand Three Hundred Forty Five"
Example 3:

Input: 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
Example 4:

Input: 1234567891
Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"

273. 整数转换英文表示
将非负整数转换为其对应的英文表示。可以保证给定输入小于 231 - 1 。

示例 1:

输入: 123
输出: "One Hundred Twenty Three"
示例 2:

输入: 12345
输出: "Twelve Thousand Three Hundred Forty Five"
示例 3:

输入: 1234567
输出: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
示例 4:

输入: 1234567891
输出: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"


'''


class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        base = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        teen = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen",
                "Nineteen"]
        ty = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        hash_map = ["", "Thousand", "Million", "Billion"]

        def convert(num):
            mod = num % 100
            hundred = base[num / 100] + " Hundred " if num / 100 > 0 else " "
            res = ""
            if 10 <= mod < 20:
                res =   hundred + teen[(num % 100) % 10]
            elif 20 <= mod <= 99:
                res = hundred + ty[(num % 100) / 10] + " " + base[num % 10]
            elif mod < 10:
                res = hundred + base[num % 100]
            return res.strip()
        
        if num == 0:
            return "Zero"

        res = ""
        n = 0
        while num > 0:
            mod = num % 1000
            num = num / 1000
            if mod > 0:
                res = convert(mod) + " " + hash_map[n] + " " + res
            n += 1
        return res.strip()

# solutions

'''
方法一：递归
由于非负整数 \textit{num}num 的最大值为 2^{31}-12 
31
 −1，因此最多有 1010 位数。将整数转换成英文表示中，将数字按照 33 位一组划分，将每一组的英文表示拼接之后即可得到整数 \textit{num}num 的英文表示。

每一组最多有 33 位数，可以使用递归的方式得到每一组的英文表示。根据数字所在的范围，具体做法如下：

小于 2020 的数可以直接得到其英文表示；

大于等于 2020 且小于 100100 的数首先将十位转换成英文表示，然后对个位递归地转换成英文表示；

大于等于 100100 的数首先将百位转换成英文表示，然后对其余部分（十位和个位）递归地转换成英文表示。

从高到低的每一组的单位依次是 10^910 
9
 、10^610 
6
 、10^310 
3
 、11，除了最低组以外，每一组都有对应的表示单位的词，分别是 \text{``Billion"}“Billion"、\text{``Million"}“Million"、\text{``Thousand"}“Thousand"。

得到每一组的英文表示后，需要对每一组加上对应的表示单位的词，然后拼接得到整数 \textit{num}num 的英文表示。

具体实现中需要注意以下两点：

只有非零的组的英文表示才会拼接到整数 \textit{num}num 的英文表示中；

如果 \textit{num} = 0num=0，则不适用上述做法，而是直接返回 \text{``Zero"}“Zero"。

JavaC#C++JavaScriptGolangPython3

singles = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
thousands = ["", "Thousand", "Million", "Billion"]

class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        def recursion(num: int) -> str:
            s = ""
            if num == 0:
                return s
            elif num < 10:
                s += singles[num] + " "
            elif num < 20:
                s += teens[num - 10] + " "
            elif num < 100:
                s += tens[num // 10] + " " + recursion(num % 10)
            else:
                s += singles[num // 100] + " Hundred " + recursion(num % 100)
            return s

        s = ""
        unit = int(1e9)
        for i in range(3, -1, -1):
            curNum = num // unit
            if curNum:
                num -= curNum * unit
                s += recursion(curNum) + thousands[i] + " "
            unit //= 1000
        return s.strip()
复杂度分析

时间复杂度：O(1)O(1)。非负整数 \textit{nums}nums 按照 33 位一组划分最多有 44 组，分别得到每一组的英文表示，然后拼接得到整数 \textit{num}num 的英文表示，时间复杂度是常数。

空间复杂度：O(1)O(1)。空间复杂度主要取决于存储英文表示的字符串和递归调用栈，英文表示的长度可以看成常数，递归调用栈不会超过 33 层。

方法二：迭代
也可以使用迭代的方式得到每一组的英文表示。由于每一组最多有 33 位数，因此依次得到百位、十位、个位上的数字，生成该组的英文表示，注意只有非零位才会被添加到英文表示中。

JavaC#C++JavaScriptGolangPython3

singles = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
thousands = ["", "Thousand", "Million", "Billion"]

class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        def toEnglish(num: int) -> str:
            s = ""
            if num >= 100:
                s += singles[num // 100] + " Hundred "
                num %= 100
            if num >= 20:
                s += tens[num // 10] + " "
                num %= 10
            if 0 < num < 10:
                s += singles[num] + " "
            elif num >= 10:
                s += teens[num - 10] + " "
            return s

        s = ""
        unit = int(1e9)
        for i in range(3, -1, -1):
            curNum = num // unit
            if curNum:
                num -= curNum * unit
                s += toEnglish(curNum) + thousands[i] + " "
            unit //= 1000
        return s.strip()
复杂度分析

时间复杂度：O(1)O(1)。

空间复杂度：O(1)O(1)。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/integer-to-english-words/solution/zheng-shu-zhuan-huan-ying-wen-biao-shi-b-ivik/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''

