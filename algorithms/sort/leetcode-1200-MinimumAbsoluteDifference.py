# encoding=utf8

'''
1200. Minimum Absolute Difference
Given an array of distinct integers arr, find all pairs of elements with the minimum absolute difference of any two elements.

Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows

a, b are from arr
a < b
b - a equals to the minimum absolute difference of any two elements in arr
 

Example 1:

Input: arr = [4,2,1,3]
Output: [[1,2],[2,3],[3,4]]
Explanation: The minimum absolute difference is 1. List all pairs with difference equal to 1 in ascending order.
Example 2:

Input: arr = [1,3,6,10,15]
Output: [[1,3]]
Example 3:

Input: arr = [3,8,-10,23,19,-4,-14,27]
Output: [[-14,-10],[19,23],[23,27]]
 

Constraints:

2 <= arr.length <= 105
-106 <= arr[i] <= 106

1200. 最小绝对差

给你个整数数组 arr，其中每个元素都 不相同。

请你找到所有具有最小绝对差的元素对，并且按升序的顺序返回。

每对元素对 [a,b] 如下：

    a , b 均为数组 arr 中的元素
    a < b
    b - a 等于 arr 中任意两个元素的最小绝对差

 

示例 1：

输入：arr = [4,2,1,3]
输出：[[1,2],[2,3],[3,4]]

示例 2：

输入：arr = [1,3,6,10,15]
输出：[[1,3]]

示例 3：

输入：arr = [3,8,-10,23,19,-4,-14,27]
输出：[[-14,-10],[19,23],[23,27]]

 

提示：

    2 <= arr.length <= 10^5
    -10^6 <= arr[i] <= 10^6
'''

class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        arr.sort()
        min_abs = float("inf")
        abs_dict = []
        for i in range(1, len(arr)):
            abs_ = arr[i] - arr[i-1]
            if abs_ < min_abs:
                min_abs = abs_
                abs_dict = [[arr[i-1], arr[i]]]
            elif abs_ == min_abs:
                abs_dict.append([arr[i-1], arr[i]])

        return abs_dict

