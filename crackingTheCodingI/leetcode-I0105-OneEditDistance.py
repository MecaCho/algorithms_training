'''
面试题 01.05. 一次编辑
字符串有三种编辑操作:插入一个字符、删除一个字符或者替换一个字符。 给定两个字符串，编写一个函数判定它们是否只需要一次(或者零次)编辑。



示例 1:

输入:
first = "pale"
second = "ple"
输出: True


示例 2:

输入:
first = "pales"
second = "pal"
输出: False

面试题 01.05. One Away LCCI
There are three types of edits that can be performed on strings: insert a character, remove a character, or replace a character. Given two strings, write a function to check if they are one edit (or zero edits) away.



Example 1:

Input:
first = "pale"
second = "ple"
Output: True
Example 2:

Input:
first = "pales"
second = "pal"
Output: False
'''


class Solution(object):
    def oneEditAway(self, first, second):
        """
        :type first: str
        :type second: str
        :rtype: bool
        """
        len1 = len(first)
        len2 = len(second)

        if abs(len1 -len2) > 1:
            return False
        if len(first) > len(second):
            first, second = second, first
        if first == second:
            return True
        for i in range(len(first)):
            if first[i] != second[i]:
                return first[i:] == second[ i +1:] or first[ i +1:] == second[ i +1:]
        # print(i, len(first))
        return True
