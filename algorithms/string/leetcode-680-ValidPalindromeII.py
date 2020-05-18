'''
680. Valid Palindrome II
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True
Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
Note:
The string will only contain lowercase characters a-z. The maximum length of the string is 50000.

680. 验证回文字符串 Ⅱ
给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文字符串。

示例 1:

输入: "aba"
输出: True
示例 2:

输入: "abca"
输出: True
解释: 你可以删除c字符。
注意:

字符串只包含从 a-z 的小写字母。字符串的最大长度是50000。
'''
class Solution(object):

    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i, j = 0, len(s ) -1
        count = 1
        def is_palindrome(s):
            # s = "".join(filter(lambda x: x.isalnum(), s)).lower()
            return s == s[::-1]
        while i <= j:
            if s[i] != s[j]:
                return is_palindrome(s[i:j]) or is_palindrome(s[ i +1: j +1])
            else:
                i += 1
                j -= 1
        return True


'''
方法一：贪心算法
考虑最朴素的方法：首先判断原串是否是回文串，如果是，就返回 true；如果不是，则枚举每一个位置作为被删除的位置，再判断剩下的字符串是否是回文串。这种做法的渐进时间复杂度是 O(n^2)O(n 
2
 ) 的，会超出时间限制。

我们换一种想法。首先考虑如果不允许删除字符，如何判断一个字符串是否是回文串。常见的做法是使用双指针。定义左右指针，初始时分别指向字符串的第一个字符和最后一个字符，每次判断左右指针指向的字符是否相同，如果不相同，则不是回文串；如果相同，则将左右指针都往中间移动一位，直到左右指针相遇，则字符串是回文串。

在允许最多删除一个字符的情况下，同样可以使用双指针，通过贪心算法实现。初始化两个指针 low 和 high 分别指向字符串的第一个字符和最后一个字符。每次判断两个指针指向的字符是否相同，如果相同，则更新指针，令 low = low + 1 和 high = high - 1，然后判断更新后的指针范围内的子串是否是回文字符串。如果两个指针指向的字符不同，则两个字符中必须有一个被删除，此时我们就分成两种情况：即删除左指针对应的字符，留下子串 s[low + 1], s[low + 1], ..., s[high]，或者删除右指针对应的字符，留下子串 s[low], s[low + 1], ..., s[high - 1]。当这两个子串中至少有一个是回文串时，就说明原始字符串删除一个字符之后就以成为回文串。



JavaPython3C++Golang
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def checkPalindrome(low, high):
            i, j = low, high
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        low, high = 0, len(s) - 1
        while low < high:
            if s[low] == s[high]: 
                low += 1
                high -= 1
            else:
                return checkPalindrome(low + 1, high) or checkPalindrome(low, high - 1)
        return True
复杂度分析

时间复杂度：O(n)O(n)，其中 nn 是字符串的长度。判断整个字符串是否是回文字符串的时间复杂度是 O(n)O(n)，遇到不同字符时，判断两个子串是否是回文字符串的时间复杂度也都是 O(n)O(n)。

空间复杂度：O(1)O(1)。只需要维护有限的常量空间。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/valid-palindrome-ii/solution/yan-zheng-hui-wen-zi-fu-chuan-ii-by-leetcode-solut/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''