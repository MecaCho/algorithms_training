

'''
面试题 17.04. 消失的数字
数组nums包含从0到n的所有整数，但其中缺了一个。请编写代码找出那个缺失的整数。你有办法在O(n)时间内完成吗？

注意：本题相对书上原题稍作改动

示例 1：

输入：[3,0,1]
输出：2
 

示例 2：

输入：[9,6,4,2,3,5,7,0,1]
输出：8

面试题 17.04. Missing Number LCCI
An array contains all the integers from 0 to n, except for one number which is missing.  Write code to find the missing integer. Can you do it in O(n) time?

Note: This problem is slightly different from the original one the book.

Example 1:

Input: [3,0,1]
Output: 2
 

Example 2:

Input: [9,6,4,2,3,5,7,0,1]
Output: 8
'''






class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums) + 1
        return (length + 0) * (length - 1) / 2 - sum(nums)



# 利用异或的特性，res = res ^ x ^ x。对同一个值异或两次，那么结果等于它本身，所以我们对res从0-nums.length进行异或，同时对nums数组中的值进行异或，出现重复的会消失，所以最后res的值是只出现一次的数字，也就是nums数组中缺失的那个数字。
class Solution1(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # length = len(nums) + 1
        # return (length + 0) * (length - 1) / 2 - sum(nums)
        res = len(nums)
        for i in range(len(nums)):
            res ^= i
            res ^= nums[i]
        return res