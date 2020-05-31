



'''
1087. 字母切换
我们用一个特殊的字符串 S 来表示一份单词列表，之所以能展开成为一个列表，是因为这个字符串 S 中存在一个叫做「选项」的概念：

单词中的每个字母可能只有一个选项或存在多个备选项。如果只有一个选项，那么该字母按原样表示。

如果存在多个选项，就会以花括号包裹来表示这些选项（使它们与其他字母分隔开），例如 "{a,b,c}" 表示 ["a", "b", "c"]。

例子："{a,b,c}d{e,f}" 可以表示单词列表 ["ade", "adf", "bde", "bdf", "cde", "cdf"]。

请你按字典顺序，返回所有以这种方式形成的单词。



示例 1：

输入："{a,b}c{d,e}f"
输出：["acdf","acef","bcdf","bcef"]
示例 2：

输入："abcd"
输出：["abcd"]


提示：

1 <= S.length <= 50
你可以假设题目中不存在嵌套的花括号
在一对连续的花括号（开花括号与闭花括号）之间的所有字母都不会相同

1087. Brace Expansion
A string S represents a list of words.

Each letter in the word has 1 or more options.  If there is one option, the letter is represented as is.  If there is more than one option, then curly braces delimit the options.  For example, "{a,b,c}" represents options ["a", "b", "c"].

For example, "{a,b,c}d{e,f}" represents the list ["ade", "adf", "bde", "bdf", "cde", "cdf"].

Return all words that can be formed in this manner, in lexicographical order.



Example 1:

Input: "{a,b}c{d,e}f"
Output: ["acdf","acef","bcdf","bcef"]
Example 2:

Input: "abcd"
Output: ["abcd"]


Note:

1 <= S.length <= 50
There are no nested curly brackets.
All characters inside a pair of consecutive opening and ending curly brackets are different.
'''


import re

class Solution(object):
    def expand(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        left = right = 0
        for i in range(len(S)):
            c = S[i]
            if c == "{":
                left = i
            if c == "}":
                right = i
            if right - left == 1:
                return []
        self.vals = []
        def backtrack(str_list):
            if len(str_list) == 1:
                self.vals.append(str_list[0])
            else:
                # for i in range(1, len(str_list)):
                if "," in str_list[1]:
                    str_list[1] = sorted(str_list[1].split(","))
                    for j in range(len(str_list[1])):
                        backtrack([str_list[0]+str_list[1][j]]+str_list[2:])
                else:
                    backtrack([str_list[0]+str_list[1]]+str_list[2:])
        str_list = [i for i in re.split("[{}]", S)]

        backtrack(str_list)
        return self.vals

# tips

'''

All generated strings are of the same size. How can we generate all of these strings?
Do a backtracking on which each level of it has to choose one single (e.g. 'a') character or any character of the given parenthesized group (e.g. "{a,b,c}")

'''