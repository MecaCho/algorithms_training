# encoding=utf8

'''
567. Permutation in String
Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.



Example 1:

Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input:s1= "ab" s2 = "eidboaoo"
Output: False


Constraints:

The input strings only contain lower case letters.
The length of both given strings is in range [1, 10,000].


567. 字符串的排列
给定两个字符串 s1 和 s2，写一个函数来判断 s2 是否包含 s1 的排列。

换句话说，第一个字符串的排列之一是第二个字符串的子串。

示例1:

输入: s1 = "ab" s2 = "eidbaooo"
输出: True
解释: s2 包含 s1 的排列之一 ("ba").


示例2:

输入: s1= "ab" s2 = "eidboaoo"
输出: False


注意：

输入的字符串只包含小写字母
两个字符串的长度都在 [1, 10,000] 之间
'''




class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        counter1, counter2 = [0]*26,[0]*26
        i = 0
        length_s1 = len(s1)
        if length_s1 > len(s2):
            return False
        while i < len(s1):
            counter1[ord(s1[i]) - ord("a")] += 1
            counter2[ord(s2[i]) - ord("a")] += 1
            i += 1
        if counter2 == counter1:
            return True

        # print(counter1, counter2)
        while i < len(s2):
            counter2[ord(s2[i]) - ord("a")] += 1
            counter2[ord(s2[i-length_s1]) - ord("a")] -= 1
            if counter2 == counter1:
                return True
            # print(counter1, counter2)
            i += 1

        return False


