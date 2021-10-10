# encoding=utf8

'''
441. Arranging Coins
You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.

Given the integer n, return the number of complete rows of the staircase you will build.

 

Example 1:


Input: n = 5
Output: 2
Explanation: Because the 3rd row is incomplete, we return 2.
Example 2:


Input: n = 8
Output: 3
Explanation: Because the 4th row is incomplete, we return 3.
 

Constraints:

1 <= n <= 231 - 1

441. 排列硬币
你总共有 n 枚硬币，并计划将它们按阶梯状排列。对于一个由 k 行组成的阶梯，其第 i 行必须正好有 i 枚硬币。阶梯的最后一行 可能 是不完整的。

给你一个数字 n ，计算并返回可形成 完整阶梯行 的总行数。

 

示例 1：


输入：n = 5
输出：2
解释：因为第三行不完整，所以返回 2 。
示例 2：


输入：n = 8
输出：3
解释：因为第四行不完整，所以返回 3 。
 

提示：

1 <= n <= 231 - 1
'''

class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = int(math.sqrt(n*2))
        while i > 0:
            if (1+i)*i/2 <=n:
                return i
            i -= 1

            
# solutions

'''
方法一：二分查找
思路和算法

根据等差数列求和公式可知，前 kk 个完整阶梯行所需的硬币数量为

\textit{total} = \frac{k \times (k+1)}{2}
total= 
2
k×(k+1)
​
 

因此，可以通过二分查找计算 nn 枚硬币可形成的完整阶梯行的总行数。

因为 1 \le n \le 2^{31} -11≤n≤2 
31
 −1，所以 nn 枚硬币至少可以组成 11 个完整阶梯行，至多可以组成 nn 个完整阶梯行（在 n = 1n=1 时得到）。

代码

Python3JavaC#JavaScriptC++Golang

class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 1, n
        while left < right:
            mid = (left + right + 1) // 2
            if mid * (mid + 1) <= 2 * n:
                left = mid
            else:
                right = mid - 1
        return left
复杂度分析

时间复杂度：O(\log n)O(logn)。

空间复杂度：O(1)O(1)。

方法二：数学
思路和算法

考虑直接通过求解方程来计算 nn 枚硬币可形成的完整阶梯行的总行数。不妨设可以形成的行数为 xx，则有

\frac{(x+1) \times x}{2} = n
2
(x+1)×x
​
 =n

整理得一元二次方程

x^2 + x - 2n = 0
x 
2
 +x−2n=0

因为 n \ge 1n≥1 ，所以判别式

\Delta = b^2 - 4ac = 8n + 1 > 0
Δ=b 
2
 −4ac=8n+1>0

解得

x_1 = \frac{-1 - \sqrt{8n+1}}{2}, \hspace{1em} x_2 = \frac{-1 + \sqrt{8n+1}}{2}
 

因为 x_1 < 0x 
1
​
 <0，故舍去。此时 x_2x 
2
​
  即为硬币可以排列成的行数，可以完整排列的行数即 \lfloor x_2 \rfloor⌊x 
2
​
 ⌋，其中符号 \lfloor x \rfloor⌊x⌋ 表示 xx 的向下取整。

代码

Python3JavaC#JavaScriptC++Golang

class Solution:
    def arrangeCoins(self, n: int) -> int:
        return int((pow(8 * n + 1, 0.5) - 1) / 2)
复杂度分析

代码中使用的 \texttt{pow}pow 函数的时空复杂度与 CPU 支持的指令集相关，这里不深入分析。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/arranging-coins/solution/pai-lie-ying-bi-by-leetcode-solution-w52c/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
