# encoding=utf8


'''
1447. Simplified Fractions
Given an integer n, return a list of all simplified fractions between 0 and 1 (exclusive) such that the denominator is less-than-or-equal-to n. You can return the answer in any order.

 

Example 1:

Input: n = 2
Output: ["1/2"]
Explanation: "1/2" is the only unique fraction with a denominator less-than-or-equal-to 2.
Example 2:

Input: n = 3
Output: ["1/2","1/3","2/3"]
Example 3:

Input: n = 4
Output: ["1/2","1/3","1/4","2/3","3/4"]
Explanation: "2/4" is not a simplified fraction because it can be simplified to "1/2".
 

Constraints:

1 <= n <= 100

5397. 最简分数
给你一个整数 n ，请你返回所有 0 到 1 之间（不包括 0 和 1）满足分母小于等于  n 的 最简 分数 。分数可以以 任意 顺序返回。



示例 1：

输入：n = 2
输出：["1/2"]
解释："1/2" 是唯一一个分母小于等于 2 的最简分数。
示例 2：

输入：n = 3
输出：["1/2","1/3","2/3"]
示例 3：

输入：n = 4
输出：["1/2","1/3","1/4","2/3","3/4"]
解释："2/4" 不是最简分数，因为它可以化简为 "1/2" 。
示例 4：

输入：n = 1
输出：[]


提示：

1 <= n <= 100

5397. Simplified Fractions
Given an integer n, return a list of all simplified fractions between 0 and 1 (exclusive) such that the denominator is less-than-or-equal-to n. The fractions can be in any order.



Example 1:

Input: n = 2
Output: ["1/2"]
Explanation: "1/2" is the only unique fraction with a denominator less-than-or-equal-to 2.
Example 2:

Input: n = 3
Output: ["1/2","1/3","2/3"]
Example 3:

Input: n = 4
Output: ["1/2","1/3","1/4","2/3","3/4"]
Explanation: "2/4" is not a simplified fraction because it can be simplified to "1/2".
Example 4:

Input: n = 1
Output: []


Constraints:

1 <= n <= 100
'''


class Solution(object):
    def simplifiedFractions(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        def gcd(m, n):
            if n == 0:
                return m
            else:
                return gcd(n, m % n)

        res = []
        for i in range(1, n):
            for j in range(i + 1, n + 1):
                if gcd(i, j) == 1:
                    res.append("{}/{}".format(i, j))

        return res

# tips

'''
A fraction is fully simplified if there is no integer that divides cleanly into the numerator and denominator.
In other words the greatest common divisor of the numerator and the denominator of a simplified fraction is 1.
'''

# solutions

'''
方法一：数学
由于要保证分数在 (0,1)(0,1) 范围内，我们可以枚举分母 \textit{denominator}\in [2,n]denominator∈[2,n] 和分子 \textit{numerator}\in [1,\textit{denominator})numerator∈[1,denominator)，若分子分母的最大公约数为 11，则我们找到了一个最简分数。

Python3C++JavaC#GolangCJavaScript

class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        return [f"{numerator}/{denominator}" for denominator in range(2, n + 1) for numerator in range(1, denominator) if gcd(denominator, numerator) == 1]
复杂度分析

时间复杂度：O(n^2\log n)O(n 
2
 logn)。需要枚举 O(n^2)O(n 
2
 ) 对分子分母的组合，每对分子分母计算最大公因数和生成字符串的复杂度均为 O(\log n)O(logn)。

空间复杂度：O(1)O(1)。除答案数组外，我们只需要常数个变量。
'''


