



'''
159. 至多包含两个不同字符的最长子串
给定一个字符串 s ，找出 至多 包含两个不同字符的最长子串 t 。

示例 1:

输入: "eceba"
输出: 3
解释: t 是 "ece"，长度为3。
示例 2:

输入: "ccaabbb"
输出: 5
解释: t 是 "aabbb"，长度为5。

159. Longest Substring with At Most Two Distinct Characters
Given a string s , find the length of the longest substring t  that contains at most 2 distinct characters.

Example 1:

Input: "eceba"
Output: 3
Explanation: t is "ece" which its length is 3.
Example 2:

Input: "ccaabbb"
Output: 5
Explanation: t is "aabbb" which its length is 5.

'''



class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) <= 2:
            return len(s)
        hash_map = {}
        l, r = -1, 0
        max_len = 0
        for i in range(len(s)):
            r = i
            if len(hash_map) <= 2:
                hash_map[s[i]] = i
                if len(hash_map) == 3:
                    min_index = min(hash_map.values())
                    l = min_index
                    hash_map.pop(s[min_index])
                max_len = max(max_len, r-l)
        return max_len
