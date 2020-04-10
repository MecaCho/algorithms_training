'''

面试题 01.03. URL化
URL化。编写一种方法，将字符串中的空格全部替换为%20。假定该字符串尾部有足够的空间存放新增字符，并且知道字符串的“真实”长度。（注：用Java实现的话，请使用字符数组实现，以便直接在数组上操作。）

示例1:

 输入："Mr John Smith    ", 13
 输出："Mr%20John%20Smith"
示例2:

 输入："               ", 5
 输出："%20%20%20%20%20"
提示：

字符串长度在[0, 500000]范围内。

面试题 01.03. String to URL LCCI
Write a method to replace all spaces in a string with '%20'. You may assume that the string has sufficient space at the end to hold the additional characters,and that you are given the "true" length of the string. (Note: If implementing in Java,please use a character array so that you can perform this operation in place.)

Example 1:

Input: "Mr John Smith ", 13
Output: "Mr%20John%20Smith"
Explanation: 
The missing numbers are [5,6,8,...], hence the third missing number is 8.
Example 2:

Input: "               ", 5
Output: "%20%20%20%20%20"
 

Note:

0 <= S.length <= 500000
'''






class Solution(object):
    def replaceSpaces(self, S, length):
        """
        :type S: str
        :type length: int
        :rtype: str
        """
        S = list(S)
        i = length - 1
        j = len(S) - 1
        # print(i, j, S[i])
        while i>=0:
            if S[i] != " ":
                S[j] = S[i]
                j -= 1
            else:
                # print(j, j-2)
                # S[j-2:j+1] = ["%","2","0"]
                # S[j], S[j-1], S[j-2] = "%","2","0"
                S[j-2:j+1] = "%20"
                j -= 3
            i -= 1
        # print(S)

        return "".join(S[j+1:])
        # print(len(S))
        # return S.strip().replace(" ", "%20")
