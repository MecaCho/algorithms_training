# encoding=utf8

'''
58. Length of Last Word
Given a string s consisting of some words separated by some number of spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.

 

Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
Example 3:

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
 

Constraints:

1 <= s.length <= 104
s consists of only English letters and spaces ' '.
There will be at least one word in s.

58. 最后一个单词的长度
给你一个字符串 s，由若干单词组成，单词前后用一些空格字符隔开。返回字符串中最后一个单词的长度。

单词 是指仅由字母组成、不包含任何空格字符的最大子字符串。

 

示例 1：

输入：s = "Hello World"
输出：5
示例 2：

输入：s = "   fly me   to   the moon  "
输出：4
示例 3：

输入：s = "luffy is still joyboy"
输出：6
 

提示：

1 <= s.length <= 104
s 仅有英文字母和空格 ' ' 组成
s 中至少存在一个单词
'''


class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.strip().split(" ")[-1])

    
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = s.split(" ")
        for word in l[::-1]:
            if word:
                return len(word)


if __name__ == '__main__':
    demo = Solution()
    print(demo.lengthOfLastWord("abc Hello jjfkd "))
   
   
# Golang solution

'''
func lengthOfLastWord(s string) (ans int) {
    index := len(s) - 1
    for s[index] == ' ' {
        index--
    }
    for index >= 0 && s[index] != ' ' {
        ans++
        index--
    }
    return
}
'''

