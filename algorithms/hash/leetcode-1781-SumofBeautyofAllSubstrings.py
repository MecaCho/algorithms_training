# encoding=utf8


'''
1781. Sum of Beauty of All Substrings
The beauty of a string is the difference in frequencies between the most frequent and least frequent characters.

For example, the beauty of "abaacc" is 3 - 1 = 2.
Given a string s, return the sum of beauty of all of its substrings.

 

Example 1:

Input: s = "aabcb"
Output: 5
Explanation: The substrings with non-zero beauty are ["aab","aabc","aabcb","abcb","bcb"], each with beauty equal to 1.
Example 2:

Input: s = "aabcbaa"
Output: 17
 

Constraints:

1 <= s.length <= 500
s consists of only lowercase English letters.
'''

class Solution:
    def beautySum(self, s: str) -> int:
        res = 0
        n = len(s)
        for i in range(n):
            cnt = Counter()
            max_f = 0
            for j in range(i, n):
                cnt[s[j]] += 1
                if cnt[s[j]] > max_f:
                    max_f = cnt[s[j]]
                res += max_f - min(cnt.values())

        return res


