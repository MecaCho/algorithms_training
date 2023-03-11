# encoding=utf8

'''
面试题 17.05. Find Longest Subarray LCCI
Given an array filled with letters and numbers, find the longest subarray with an equal number of letters and numbers.

Return the subarray. If there are more than one answer, return the one which has the smallest index of its left endpoint. If there is no answer, return an empty arrary.

Example 1:

Input: ["A","1","B","C","D","2","3","4","E","5","F","G","6","7","H","I","J","K","L","M"]

Output: ["A","1","B","C","D","2","3","4","E","5","F","G","6","7"]
Example 2:

Input: ["A","A"]

Output: []
Note:

array.length <= 100000
'''

class Solution:
    def findLongestSubarray(self, array: List[str]) -> List[str]:
        indexs = {0: -1}

        sum_ = 0
        max_len = 0
        res = []
        for i in range(len(array)):
            if '0' <= array[i][0] <= '9':
                sum_ += 1
            else:
                sum_ -= 1
            if sum_ in indexs:
                if max_len < (i - indexs[sum_]+1):
                    res = [indexs[sum_], i]
                    max_len = i - indexs[sum_]+1
            else:
                indexs[sum_] = i
        return array[res[0]+1:res[1]+1] if res else []
