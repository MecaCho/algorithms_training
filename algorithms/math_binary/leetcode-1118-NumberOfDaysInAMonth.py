
'''
1118. 一月有多少天
指定年份 Y 和月份 M，请你帮忙计算出该月一共有多少天。

 

示例 1：

输入：Y = 1992, M = 7
输出：31
示例 2：

输入：Y = 2000, M = 2
输出：29
示例 3：

输入：Y = 1900, M = 2
输出：28
 

提示：

1583 <= Y <= 2100
1 <= M <= 12

1118. Number of Days in a Month
Given a year Y and a month M, return how many days there are in that month.

 

Example 1:

Input: Y = 1992, M = 7
Output: 31
Example 2:

Input: Y = 2000, M = 2
Output: 29
Example 3:

Input: Y = 1900, M = 2
Output: 28
 

Note:

1583 <= Y <= 2100
1 <= M <= 12
'''







class Solution(object):
    def numberOfDays(self, Y, M):
        """
        :type Y: int
        :type M: int
        :rtype: int
        """
        def is_leap(y):
            return (y % 4 == 0 and y % 100 != 0) or (y % 400 ==0)
        months = [31,28,31,30,31,30,31,31,30,31,30,31]
        if M == 2 and is_leap(Y):
            return 29
        return months[M-1]
