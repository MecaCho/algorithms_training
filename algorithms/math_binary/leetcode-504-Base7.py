# encoding=utf8

'''
504. Base 7
Given an integer num, return a string of its base 7 representation.

 

Example 1:

Input: num = 100
Output: "202"
Example 2:

Input: num = -7
Output: "-10"
 

Constraints:

-107 <= num <= 107
'''

class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        res = "-" if num < 0 else ""
        num = abs(num)
        base = 1
        while num / base >= 7:
            base *= 7

        while base:
            a, num = num / base, num % base
            base /= 7
            res += str(a)
        return res

      
