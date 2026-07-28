# encoding=utf8

'''
3517. Smallest Palindromic Rearrangement I

You are given a string s.
Return the palindromic of s.

Example 1:
Input: s = "z"
Output: "z"
Explanation:
A string of only one character is already the lexicographically smallest palindrome.
Example 2:
Input: s = "babab"
Output: "abbba"
Explanation:
Rearranging "babab" → "abbba" gives the smallest lexicographic palindrome.
Example 3:
Input: s = "daccad"
Output: "acddca"
Explanation:
Rearranging "daccad" → "acddca" gives the smallest lexicographic palindrome.

Constraints:
1 <= s.length <= 105
s consists of lowercase English letters.
s is guaranteed to be palindromic.

'''

class Solution:
    def smallestPalindrome(self, s: str) -> str:
        from collections import Counter

        counts = Counter(s)

        left_half = []
        mid = ""

        # Iterate in alphabetical order
        for char in sorted(counts.keys()):
            cnt = counts[char]
            if cnt % 2 == 1:
                mid = char
            left_half.append(char * (cnt // 2))

        left_str = "".join(left_half)
        return left_str + mid + left_str[::-1]

