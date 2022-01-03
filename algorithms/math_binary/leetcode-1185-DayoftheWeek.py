# encoding-utf8


'''
1185. Day of the Week
Given a date, return the corresponding day of the week for that date.

The input is given as three integers representing the day, month and year respectively.

Return the answer as one of the following values {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}.

 

Example 1:

Input: day = 31, month = 8, year = 2019
Output: "Saturday"
Example 2:

Input: day = 18, month = 7, year = 1999
Output: "Sunday"
Example 3:

Input: day = 15, month = 8, year = 1993
Output: "Sunday"
 

Constraints:

The given dates are valid dates between the years 1971 and 2100.
'''


class Solution(object):
    def dayOfTheWeek(self, day, month, year):
        """
        :type day: int
        :type month: int
        :type year: int
        :rtype: str
        """
        # c 是世纪数减一，也就是年份的前两位。
        # y 是年份的后两位。
        # m 是月份。m 的取值范围是 3 至 14，因为某年的 1、2 月要看作上一年的 13、14月，比如 2019 年的 1 月 1 日要看作 2018 年的 13 月 1 日来计算。
        # d 是日数。
        # W = D%7 是结果代表一周中第几天, 0 为周日
        # 由于最后计算 D 可能为负数，需要处理一下。方法很多：这里由 D 计算式发现减的内容最大为 199 所以可以加上一个大于 199 且是 7 的倍数的数，随便取一个 210 加上保证结果为正
        week= ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday","Saturday"]
        if month < 3:
            m = month + 12
            y = year - 1
        else:
            m = month
            y = year
        index = 0
        c = y/100
        y %= 100
        D = c/4 - 2*c + y + y/4 + 13*(m+1)/5 + day - 1 + 210
        return week[D%7] 


