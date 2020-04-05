'''
面试题 08.03. 魔术索引
魔术索引。 在数组A[0...n-1]中，有所谓的魔术索引，满足条件A[i] = i。给定一个有序整数数组，编写一种方法找出魔术索引，若有的话，在数组A中找出一个魔术索引，如果没有，则返回-1。若有多个魔术索引，返回索引值最小的一个。

示例1:

 输入：nums = [0, 2, 3, 4, 5]
 输出：0
 说明: 0下标的元素为0
示例2:

 输入：nums = [1, 1, 1]
 输出：1
提示:

nums长度在[1, 1000000]之间


面试题 08.03. Magic Index LCCI
A magic index in an array A[0...n-1] is defined to be an index such that A[i] = i. Given a sorted array of distinct integers, write a method to find a magic index, if one exists, in array A. If not, return -1. If there are more than one magic index, return the smallest one.

Example1:

 Input: nums = [0, 2, 3, 4, 5]
 Output: 0
Example2:

 Input: nums = [1, 1, 1]
 Output: 1
Note:

1 <= nums.length <= 1000000
'''



class Solution(object):
    def findMagicIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            if i == nums[i]:
                return i
        return -1

class Solution1(object):
    def find(self, nums):
        if not nums:
            return -1

        n = len(nums)
        i = 0
        while i < n:
            if nums[i] == i:
                return i
            if nums[i] > i:  # 此时我们可以排除索引i到nums[i-1]这一整段
                i = nums[i]  # 由于数组可以保持平稳，所以nums[i]这一元素不可排除
            else:
                i += 1

        return -1
