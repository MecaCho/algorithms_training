# encoding=utf8

'''
面试题 05.02. Binary Number to String LCCI
Given a real number between 0 and 1 (e.g., 0.72) that is passed in as a double, print the binary representation. If the number cannot be represented accurately in binary with at most 32 characters, print "ERROR".

Example1:

 Input: 0.625
 Output: "0.101"
Example2:

 Input: 0.1
 Output: "ERROR"
 Note: 0.1 cannot be represented accurately in binary.
Note:

This two charaters "0." should be counted into 32 characters.
The number of decimal places for num is at most 6 digits
'''

class Solution:
    def printBin(self, num: float) -> str:
        num *= 64
        if not num.is_integer():
            return 'ERROR'
        return '0.' + bin(int(num))[2:].zfill(6).rstrip('0')

