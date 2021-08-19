# encoding=utf8

'''
345. Reverse Vowels of a String
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both cases.

 

Example 1:

Input: s = "hello"
Output: "holle"
Example 2:

Input: s = "leetcode"
Output: "leotcede"
 

Constraints:

1 <= s.length <= 3 * 105
s consist of printable ASCII characters.
'''

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        aeiou = "aeiouAEIOU"
        s = list(s)
        n = len(s)
        i, j = 0, n - 1
        while i < j:
            while i < n and s[i] not in aeiou:
                i += 1
            while j > 0 and s[j] not in aeiou:
                j -= 1

            if i < j:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1

        return "".join(s)
