'''
1371. 每个元音包含偶数次的最长子字符串
给你一个字符串 s ，请你返回满足以下条件的最长子字符串的长度：每个元音字母，即 'a'，'e'，'i'，'o'，'u' ，在子字符串中都恰好出现了偶数次。



示例 1：

输入：s = "eleetminicoworoep"
输出：13
解释：最长子字符串是 "leetminicowor" ，它包含 e，i，o 各 2 个，以及 0 个 a，u 。
示例 2：

输入：s = "leetcodeisgreat"
输出：5
解释：最长子字符串是 "leetc" ，其中包含 2 个 e 。
示例 3：

输入：s = "bcbcbc"
输出：6
解释：这个示例中，字符串 "bcbcbc" 本身就是最长的，因为所有的元音 a，e，i，o，u 都出现了 0 次。


提示：

1 <= s.length <= 5 x 10^5
s 只包含小写英文字母。

1371. Find the Longest Substring Containing Vowels in Even Counts
Given the string s, return the size of the longest substring containing each vowel an even number of times. That is, 'a', 'e', 'i', 'o', and 'u' must appear an even number of times.



Example 1:

Input: s = "eleetminicoworoep"
Output: 13
Explanation: The longest substring is "leetminicowor" which contains two each of the vowels: e, i and o and zero of the vowels: a and u.
Example 2:

Input: s = "leetcodeisgreat"
Output: 5
Explanation: The longest substring is "leetc" which contains two e's.
Example 3:

Input: s = "bcbcbc"
Output: 6
Explanation: In this case, the given string "bcbcbc" is the longest because all vowels: a, e, i, o and u appear zero times.


Constraints:

1 <= s.length <= 5 x 10^5
s contains only lowercase English letters.
'''


class Solution(object):
    def findTheLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        status = [None for _ in range( 1<<5)]
        status[0] = 0
        a = "aeiou"
        hash_map = {a[i]: i for i in range(len(a))}
        init_statu = 0
        max_length = 0
        for i in range(len(s)):
            if s[i] in a:
                init_statu ^= 1 << hash_map[s[i]]

            if status[init_statu] is None:
                status[init_statu] = i + 1
            else:
                max_length = max(max_length, i+ 1 - status[init_statu])

        return max_length


# tips

'''
Represent the counts (odd or even) of vowels with a bitmask.

Precompute the prefix xor for the bitmask of vowels and then get the longest valid substring.
'''
