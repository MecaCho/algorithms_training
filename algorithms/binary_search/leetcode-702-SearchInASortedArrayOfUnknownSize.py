'''
702. 搜索长度未知的有序数组
给定一个升序整数数组，写一个函数搜索 nums 中数字 target。如果 target 存在，返回它的下标，否则返回 -1。注意，这个数组的大小是未知的。你只可以通过 ArrayReader 接口访问这个数组，ArrayReader.get(k) 返回数组中第 k 个元素（下标从 0 开始）。

你可以认为数组中所有的整数都小于 10000。如果你访问数组越界，ArrayReader.get 会返回 2147483647。



样例 1：

输入: array = [-1,0,3,5,9,12], target = 9
输出: 4
解释: 9 存在在 nums 中，下标为 4
样例 2：

输入: array = [-1,0,3,5,9,12], target = 2
输出: -1
解释: 2 不在数组中所以返回 -1


注释 ：

你可以认为数组中所有元素的值互不相同。
数组元素的值域是 [-9999, 9999]。

702. Search in a Sorted Array of Unknown Size
Given an integer array sorted in ascending order, write a function to search target in nums.  If target exists, then return its index, otherwise return -1. However, the array size is unknown to you. You may only access the array using an ArrayReader interface, where ArrayReader.get(k) returns the element of the array at index k (0-indexed).

You may assume all integers in the array are less than 10000, and if you access the array out of bounds, ArrayReader.get will return 2147483647.



Example 1:

Input: array = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
Example 2:

Input: array = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1


Note:

You may assume that all elements in the array are unique.
The value of each element in the array will be in the range [-9999, 9999].
'''


# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
# class ArrayReader(object):
#    def get(self, index):
#        """
#        :type index: int
#        :rtype int
#        """

class Solution(object):
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        i, j = 0, 20000
        while i <= j:
            mid = ( i +j) / 2
            val = reader.get(mid)
            if target == val:
                return mid
            elif target > val:
                i = mid + 1
            else:
                j = mid - 1
        return -1
