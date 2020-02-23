class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = maxLength = 0
        strmap = {}
        for i in range(len(s)):
            if s[i] in strmap and strmap[s[i]] >= start:
                start = strmap[s[i]] + 1
            else:
                maxLength = max(maxLength, i - start + 1)
            strmap[s[i]] = i
        return maxLength
