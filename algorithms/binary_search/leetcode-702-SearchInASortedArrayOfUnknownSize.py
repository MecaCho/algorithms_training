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


'''
方法一：二分查找
划分为两个子问题：

定义搜索范围，即搜索的左边界和有边界。
在定义的边界内执行二分查找。


定义搜索边界：

这是一个关键的子问题，让我们把前两个索引 0 和 1 作为左右边界。如果目标值不在第 0 个元素和第 1 个元素之间，那么它就在有边界的边界之外。

这意味着左边界可以向右移动，有边界应该扩展，为了保证对数时间的复杂度，我们将有边界扩展到两倍：right = right * 2。



如果目标值小于右边界的元素，则说明搜索边界设置好了。否则重复这两个步骤，直到确定边界：

将左边界移动到右边界：left = right。
扩展右边界：right = right * 2。


二分查找：

二分查找是具有对数时间复杂度的教科书式算法，它的基础思想是将目标值 target 与数组中间的元素 mid 进行比较。

如果 target == mid，则在数组中找到了目标值。
如果 target < mid，则左半部分数组继续查找。
如果 target > mid，则右半部分数组继续查找。


为了加快速度，我们可以使用位移运算：

左移：x << 1，与 x * 2 的作用相同。
右移：x >> 1，与 x / 2 的作用相同。
算法：

定义搜索边界：

初始化 left = 0 和 right = 1。
若目标值在搜索边界的右边，即 reader.get(right) < target：
将左边界移动到右边界：left = right。
扩展右边界：right *= 2，为了加快速度，我们使用有移代替：right <<= 1。
直到目标值在搜索边界内。
二分查找：

当 left <= right：
获取搜索边界的中间元素索引 pivot = (left + right) / 2。为了避免溢出，使用 pivot = left + ((right - left) >> 1) 代替。
获取中间元素：num = reader.get(pivot)。
比较目标值和中间元素：
如果 num == target：返回 pivot。
如果 num > target，则 right = pivot -1。
如果 num < target，则 left = pivot +1。
未找到目标值，返回 -1。
PythonJavaC++
class Solution:
    def search(self, reader, target):
        if reader.get(0) == target:
            return 0
        
        # search boundaries
        left, right = 0, 1
        while reader.get(right) < target:
            left = right
            right <<= 1
        
        # binary search
        while left <= right:
            pivot = left + ((right - left) >> 1)
            num = reader.get(pivot)
            
            if num == target:
                return pivot
            if num > target:
                right = pivot - 1
            else:
                left = pivot + 1
        
        # there is no target element
        return -1
复杂度分析

时间复杂度：\mathcal{O}(\log T)O(logT)。其中 TT 是目标值的索引。
空间复杂度：O(1)O(1)。

作者：LeetCode
链接：https://leetcode-cn.com/problems/search-in-a-sorted-array-of-unknown-size/solution/sou-suo-chang-du-wei-zhi-de-you-xu-shu-zu-by-leetc/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''