'''
1213. Intersection of Three Sorted Arrays
Given three integer arrays arr1, arr2 and arr3 sorted in strictly increasing order, return a sorted array of only the integers that appeared in all three arrays.

 

Example 1:

Input: arr1 = [1,2,3,4,5], arr2 = [1,2,5,7,9], arr3 = [1,3,4,5,8]
Output: [1,5]
Explanation: Only 1 and 5 appeared in the three arrays.
 

Constraints:

1 <= arr1.length, arr2.length, arr3.length <= 1000
1 <= arr1[i], arr2[i], arr3[i] <= 2000


1213. 三个有序数组的交集
给出三个均为 严格递增排列 的整数数组 arr1，arr2 和 arr3。

返回一个由 仅 在这三个数组中 同时出现 的整数所构成的有序数组。

 

示例：

输入: arr1 = [1,2,3,4,5], arr2 = [1,2,5,7,9], arr3 = [1,3,4,5,8]
输出: [1,5]
解释: 只有 1 和 5 同时在这三个数组中出现.
 

提示：

1 <= arr1.length, arr2.length, arr3.length <= 1000
1 <= arr1[i], arr2[i], arr3[i] <= 2000
'''




class Solution(object):
    def arraysIntersection(self, arr1, arr2, arr3):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type arr3: List[int]
        :rtype: List[int]
        """
        hash_map = {}
        for arr in arr1:
            hash_map[arr] = 1
        for arr in arr2:
            if arr in hash_map:
                hash_map[arr] += 1
        for arr in arr3:
            if arr in hash_map:
                hash_map[arr] += 1
        res = []
        for k, value in hash_map.items():
            if value ==3:
                res.append(k)
        return sorted(res)
