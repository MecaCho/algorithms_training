
'''
面试题50. 第一个只出现一次的字符
在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。

示例:

s = "abaccdeff"
返回 "b"

s = ""
返回 " "


限制：

0 <= s 的长度 <= 50000
'''




class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: str
        """
        # hash_map = {}
        # import collections
        # counter = collections.Counter(list(s))
        # for k, v in counter.items():
        #     if v == 1:
        #         return k
        # return " "
        key_dict = {}

        for key in s:
            if key in key_dict:
                key_dict[key] += 1
            else:
                key_dict[key] = 1

        for i in range(len(s)):
            if key_dict[s[i]] == 1:
                return s[i]
        return " "
