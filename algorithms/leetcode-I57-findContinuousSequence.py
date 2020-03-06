'''

面试题57 - II.和为s的连续正数序列
LCOF
English
description is not available
for the problem.Please switch to Chinese.

面试题57 - II.和为s的连续正数序列
输入一个正整数
target ，输出所有和为
target
的连续正整数序列（至少含有两个数）。

序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。



示例
1：

输入：target = 9
输出：[[2, 3, 4], [4, 5]]
示例
2：

输入：target = 15
输出：[[1, 2, 3, 4, 5], [4, 5, 6], [7, 8]]

限制：

1 <= target <= 10 ^ 5

'''


class Solution(object):
    def findContinuousSequence(self, target):
        """
        :type target: int
        :rtype: List[List[int]]
        """
        max = (target + 1) / 2 + 1
        i = 1
        res = []
        # for j in range():
        while i <= max:
            j = i + 1
            while j <= max:
                sum_ = (i + j) * (j - i + 1) / 2
                if sum_ == target:
                    # j += 1
                    res.append([k for k in range(i, j + 1)])
                    break
                if sum_ > target:
                    break
                if sum_ < target:
                    j += 1
            i += 1
        return res



class Solution(object):
    def findContinuousSequence(self, target):
        """
        :type target: int
        :rtype: List[List[int]]
        """
        max = (target + 1) / 2 + 1
        i, j = 1, 1
        sum_ = 0
        res = []
        # for j in range():
        while i <= max:
            # sum_ = (i + j) * (j - i + 1) / 2
            if sum_ == target:
                res.append([k for k in range(i, j)])
                i += 1
                j += 1
                sum_ += j
                sum_ -= i
            if sum_ > target:
                sum_ -= i
                i += 1
            if sum_ < target:
                sum_ += j
                j += 1
        return res


