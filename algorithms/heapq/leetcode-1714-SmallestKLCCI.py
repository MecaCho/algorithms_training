'''
面试题 17.14. 最小K个数
设计一个算法，找出数组中最小的k个数。以任意顺序返回这k个数均可。

示例：

输入： arr = [1,3,5,7,2,4,6,8], k = 4
输出： [1,2,3,4]
提示：

0 <= len(arr) <= 100000
0 <= k <= min(100000, len(arr))

面试题 17.14. Smallest K LCCI
Design an algorithm to find the smallest K numbers in an array.

Example:

Input:  arr = [1,3,5,7,2,4,6,8], k = 4
Output:  [1,2,3,4]
Note:

0 <= len(arr) <= 100000
0 <= k <= min(100000, len(arr))
'''



import heapq

class Solution(object):
    def smallestK(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        heapq.heapify(arr)
        return heapq.nsmallest(k, arr)
