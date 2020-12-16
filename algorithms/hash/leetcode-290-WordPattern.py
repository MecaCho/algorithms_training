'''
290. 单词规律
给定一种规律 pattern 和一个字符串 str ，判断 str 是否遵循相同的规律。

这里的 遵循 指完全匹配，例如， pattern 里的每个字母和字符串 str 中的每个非空单词之间存在着双向连接的对应规律。

示例1:

输入: pattern = "abba", str = "dog cat cat dog"
输出: true
示例 2:

输入:pattern = "abba", str = "dog cat cat fish"
输出: false
示例 3:

输入: pattern = "aaaa", str = "dog cat cat dog"
输出: false
示例 4:

输入: pattern = "abba", str = "dog dog dog dog"
输出: false
说明:
你可以假设 pattern 只包含小写字母， str 包含了由单个空格分隔的小写字母。

290. Word Pattern
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Example 1:

Input: pattern = "abba", str = "dog cat cat dog"
Output: true
Example 2:

Input:pattern = "abba", str = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", str = "dog cat cat dog"
Output: false
Example 4:

Input: pattern = "abba", str = "dog dog dog dog"
Output: false
Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters that may be separated by a single space.
'''


class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """

        word_list = str.split(" ")

        if not pattern or len(pattern) != len(word_list):
            return False

        hash_map = {}
        for i in range(len(pattern)):
            if pattern[i] not in hash_map:
                if word_list[i] in hash_map.values():
                    return False
                hash_map[pattern[i]] = word_list[i]

            else:
                if hash_map[pattern[i]] != word_list[i]:
                    return False
        return True



class Solution20201216(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        keys = list(pattern)
        words = s.split(" ")
        if len(keys) != len(words):
            return False
        w_map = {}
        for i in range(len(words)):
            if words[i] in w_map.values():
                if not w_map.get(keys[i]) or words[i] != w_map[keys[i]]:
                    return False
            else:
                if w_map.get(keys[i]) and w_map[keys[i]] != words[i]:
                    return False
                w_map[keys[i]] = words[i]
        return True


# solution

'''
方法一：哈希表
思路及解法

在本题中，我们需要判断字符与字符串之间是否恰好一一对应。即任意一个字符都对应着唯一的字符串，任意一个字符串也只被唯一的一个字符对应。在集合论中，这种关系被称为「双射」。

想要解决本题，我们可以利用哈希表记录每一个字符对应的字符串，以及每一个字符串对应的字符。然后我们枚举每一对字符与字符串的配对过程，不断更新哈希表，如果发生了冲突，则说明给定的输入不满足双射关系。

在实际代码中，我们枚举 \textit{pattern}pattern 中的每一个字符，利用双指针来均摊线性地找到该字符在 \textit{str}str 中对应的字符串。每次确定一个字符与字符串的组合，我们就检查是否出现冲突，最后我们再检查两字符串是否比较完毕即可。

代码

C++JavaGolangJavaScriptPython3

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        word2ch = dict()
        ch2word = dict()
        words = s.split()
        if len(pattern) != len(words):
            return False
        
        for ch, word in zip(pattern, words):
            if (word in word2ch and word2ch[word] != ch) or (ch in ch2word and ch2word[ch] != word):
                return False
            word2ch[word] = ch
            ch2word[ch] = word
    
        return True
思路及解法

时间复杂度：O(n + m)O(n+m)，其中 nn 为 \textit{pattern}pattern 的长度，mm 为 \textit{str}str 的长度。插入和查询哈希表的均摊时间复杂度均为 O(n + m)O(n+m)。每一个字符至多只被遍历一次。

空间复杂度：O(n + m)O(n+m)，其中 nn 为 \textit{pattern}pattern 的长度，mm 为 \textit{str}str 的长度。最坏情况下，我们需要存储 \textit{pattern}pattern 中的每一个字符和 \textit{str}str 中的每一个字符串。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/word-pattern/solution/dan-ci-gui-lu-by-leetcode-solution-6vqv/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
