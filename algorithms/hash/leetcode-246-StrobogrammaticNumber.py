
'''
246. 中心对称数
中心对称数是指一个数字在旋转了 180 度之后看起来依旧相同的数字（或者上下颠倒地看）。

请写一个函数来判断该数字是否是中心对称数，其输入将会以一个字符串的形式来表达数字。

示例 1:

输入:  "69"
输出: true
示例 2:

输入:  "88"
输出: true
示例 3:

输入:  "962"
输出: false

246. Strobogrammatic Number
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Write a function to determine if a number is strobogrammatic. The number is represented as a string.

Example 1:

Input:  "69"
Output: true
Example 2:

Input:  "88"
Output: true
Example 3:

Input:  "962"
Output: false
'''




class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        hash_map = {"6": "9", "9": "6", "8": "8", "0": "0", "1": "1"}
        new_num = []
        for i in range(len(num)):
            if num[i] not in hash_map:
                return False
            else:
                new_num.append(hash_map[num[i]])
        # print(new_num, num)
        return "".join(new_num) == num[::-1]
