'''

179. 最大数
给定一组非负整数，重新排列它们的顺序使之组成一个最大的整数。

示例 1:

输入: [10,2]
输出: 210
示例 2:

输入: [3,30,34,5,9]
输出: 9534330
说明: 输出结果可能非常大，所以你需要返回一个字符串而不是整数。

179. Largest Number
Given a list of non negative integers, arrange them such that they form the largest number.

Example 1:

Input: [10,2]
Output: "210"
Example 2:

Input: [3,30,34,5,9]
Output: "9534330"
Note: The result may be very large, so you need to return a string instead of an integer.
'''

class LargerNumKey(str):
    def __lt__(x, y):
        return x+y > y+x

class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        # new_nums = sorted(map(str, nums), cmp=lambda x,y:True if x+y > y+x else False)
        new_nums = sorted(map(str, nums), key=LargerNumKey)
        # new_nums_ = sorted(nums, cmp=lambda x,y:str(y)+str(x) > str(x) + str(y))
        # print(new_nums_, nums)

        return "".join(new_nums) if new_nums[0] != "0" else "0"
