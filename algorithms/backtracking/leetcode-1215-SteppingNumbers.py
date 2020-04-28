'''
1215. 步进数
如果一个整数上的每一位数字与其相邻位上的数字的绝对差都是 1，那么这个数就是一个「步进数」。

例如，321 是一个步进数，而 421 不是。

给你两个整数，low 和 high，请你找出在 [low, high] 范围内的所有步进数，并返回 排序后 的结果。



示例：

输入：low = 0, high = 21
输出：[0,1,2,3,4,5,6,7,8,9,10,12,21]


提示：

0 <= low <= high <= 2 * 10^9

1215. Stepping Numbers
A Stepping Number is an integer such that all of its adjacent digits have an absolute difference of exactly 1. For example, 321 is a Stepping Number while 421 is not.

Given two integers low and high, find and return a sorted list of all the Stepping Numbers in the range [low, high] inclusive.



Example 1:

Input: low = 0, high = 21
Output: [0,1,2,3,4,5,6,7,8,9,10,12,21]


Constraints:

0 <= low <= high <= 2 * 10^9
'''


class Solution(object):
    def countSteppingNumbers(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """

        self.vals = []
        def dfs(val):
            if val > high:
                return
            else:
                if val >= low:
                    self.vals.append(val)
            right = val % 10
            # print(val, right)
            if right > 0:
                dfs(val * 10 + right -1)
            if right < 9:
                dfs(val * 10 + right + 1)
        for i in range(10):
            dfs(i)

        return sorted(set(self.vals))
