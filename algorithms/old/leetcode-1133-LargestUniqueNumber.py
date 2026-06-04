'''
1133. Largest Unique Number
Given an array of integers A, return the largest integer that only occurs once.

If no integer occurs once, return -1.

 

Example 1:

Input: [5,7,3,9,4,9,8,3,1]
Output: 8
Explanation: 
The maximum integer in the array is 9 but it is repeated. The number 8 occurs only once, so it's the answer.
Example 2:

Input: [9,9,8,8]
Output: -1
Explanation: 
There is no number that occurs only once.
 

Note:

1 <= A.length <= 2000
0 <= A[i] <= 1000

1133. 最大唯一数
给你一个整数数组 A，请找出并返回在该数组中仅出现一次的最大整数。

如果不存在这个只出现一次的整数，则返回 -1。

 

示例 1：

输入：[5,7,3,9,4,9,8,3,1]
输出：8
解释： 
数组中最大的整数是 9，但它在数组中重复出现了。而第二大的整数是 8，它只出现了一次，所以答案是 8。
示例 2：

输入：[9,9,8,8]
输出：-1
解释： 
数组中不存在仅出现一次的整数。
 

提示：

1 <= A.length <= 2000
0 <= A[i] <= 1000
'''

class Solution(object):
    def largestUniqueNumber(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # if len(A) == 1:
        #     return -1
        sort_A = sorted(A, reverse=True)
        a_dict = {}
        for i in range(len(sort_A)):
            num = sort_A[i]
            if num in a_dict:
                a_dict[num] += 1
            else:
                if i == len(A) - 1:
                    return num
                a_dict[num] = 1
            # print(a_dict, sort_A[i-1], a_dict.keys())
            if len(a_dict.keys()) > 1 and a_dict[sort_A[i - 1]] == 1:
                return sort_A[i - 1]
        return -1
