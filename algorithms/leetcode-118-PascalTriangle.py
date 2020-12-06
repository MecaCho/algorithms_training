'''

118. 杨辉三角
给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。



在杨辉三角中，每个数是它左上方和右上方的数的和。

示例:

输入: 5
输出:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]


118. Pascal's Triangle
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
'''



class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows < 1:
            return []
        elif numRows == 1:
            return [[1]]
        else:
            val_list = self.generate(numRows - 1)
            val_list.append([1] + [val_list[-1][i] + val_list[-1][i+1] for i in range(len(val_list[-1]) - 1)] + [1])
            return val_list



class Solution20201206(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []
        for i in range(numRows):
            tmp = [1]
            if res:
                pre_row = res[-1]
                pre_length = len(res[-1])
                for j in range(1, pre_length):
                    tmp.append(pre_row[j]+pre_row[j-1])
                tmp.append(1)
            res.append(tmp)

        return res

