# encoding=utf8

'''
709. To Lower Case
Given a string s, return the string after replacing every uppercase letter with the same lowercase letter.

 

Example 1:

Input: s = "Hello"
Output: "hello"
Example 2:

Input: s = "here"
Output: "here"
Example 3:

Input: s = "LOVELY"
Output: "lovely"
 

Constraints:

1 <= s.length <= 100
s consists of printable ASCII characters.
'''

class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        return "".join([chr(ord(i) + 32) if "A" <= i <= "Z" else i for i in str])


if __name__ == '__main__':
    demo = Solution()
    print demo.toLowerCase("Hello")

# tips

'''
大写字母A - Z 的ASCII 码范围为 [65, 90]：

小写字母a - z 的ASCII 码范围为 [97, 122]。

因此，如果我们发现ch 的ASCII 码在 [65, 96]的范围内，那么我们将它的ASCII 码增加 32，即可得到对应的小写字母。

可以对ch 的ASCII 码与 32做按位或运算，替代与 32的加法运算
'''
