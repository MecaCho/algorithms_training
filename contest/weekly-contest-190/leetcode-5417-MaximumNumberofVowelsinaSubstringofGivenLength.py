'''
5417. 定长子串中元音的最大数目
给你字符串 s 和整数 k 。

请返回字符串 s 中长度为 k 的单个子字符串中可能包含的最大元音字母数。

英文中的 元音字母 为（a, e, i, o, u）。



示例 1：

输入：s = "abciiidef", k = 3
输出：3
解释：子字符串 "iii" 包含 3 个元音字母。
示例 2：

输入：s = "aeiou", k = 2
输出：2
解释：任意长度为 2 的子字符串都包含 2 个元音字母。
示例 3：

输入：s = "leetcode", k = 3
输出：2
解释："lee"、"eet" 和 "ode" 都包含 2 个元音字母。
示例 4：

输入：s = "rhythms", k = 4
输出：0
解释：字符串 s 中不含任何元音字母。
示例 5：

输入：s = "tryhard", k = 4
输出：1


提示：

1 <= s.length <= 10^5
s 由小写英文字母组成
1 <= k <= s.length

5417. Maximum Number of Vowels in a Substring of Given Length
Given a string s and an integer k.

Return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are (a, e, i, o, u).



Example 1:

Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.
Example 2:

Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.
Example 3:

Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.
Example 4:

Input: s = "rhythms", k = 4
Output: 0
Explanation: We can see that s doesn't have any vowel letters.
Example 5:

Input: s = "tryhard", k = 4
Output: 1


Constraints:

1 <= s.length <= 10^5
s consists of lowercase English letters.
1 <= k <= s.length
'''


class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        cur_num = len([c for c in s[:k] if c in "aeiou"])
        max_num = cur_num
        for i in range(k, len(s)):

            if s[i] in "aeiou":
                cur_num += 1
            if s[ i -k] in "aeiou":
                cur_num -= 1
            max_num = max(cur_num, max_num)
        return max_num


class Solution1:
    def maxVowels(self, s: str, k: int) -> int:
        value = [0]
        for c in s:
            value.append(value[-1] + int(c in "aeiou"))
        ans = 0
        for i in range(k, len(s) + 1):
            ans = max(ans, value[i] - value[i - k])
        return ans


# tips

'''
Keep a window of size k and maintain the number of vowels in it.

Keep moving the window and update the number of vowels while moving. Answer is max number of vowels of any window.
'''