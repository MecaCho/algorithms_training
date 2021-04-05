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


