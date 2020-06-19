'''
387. 字符串中的第一个唯一字符
给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。

案例:

s = "leetcode"
返回 0.

s = "loveleetcode",
返回 2.
 

注意事项：您可以假定该字符串只包含小写字母。

387. First Unique Character in a String
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.


'''

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: str
        """
        letters='abcdefghijklmnopqrstuvwxyz'
        indexs = [s.index(l) for l in letters if s.count(l) == 1]
        return s[min(indexs)] if indexs else " "

class Solution1(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: str
        """
        hash_map = {}
        import collections
        counter = collections.Counter(s)
        for c in s:
            if counter[c] == 1:
                return c
        return " "


class Solution2(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        key_dict = {}

        for key in s:
            if key in key_dict:
                key_dict[key] += 1
            else:
                key_dict[key] = 1

        for i in range(len(s)):
            if key_dict[s[i]] == 1:
                return i
        return -1
