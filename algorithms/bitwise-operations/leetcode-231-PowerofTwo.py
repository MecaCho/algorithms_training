# encoding=utf8

'''
231. Power of Two

Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x.

 

Example 1:

Input: n = 1
Output: true
Explanation: 20 = 1
Example 2:

Input: n = 16
Output: true
Explanation: 24 = 16
Example 3:

Input: n = 3
Output: false
Example 4:

Input: n = 4
Output: true
Example 5:

Input: n = 5
Output: false
 

Constraints:

-231 <= n <= 231 - 1
 

Follow up: Could you solve it without loops/recursion?

231. 2 的幂

给你一个整数 n，请你判断该整数是否是 2 的幂次方。如果是，返回 true ；否则，返回 false 。

如果存在一个整数 x 使得 n == 2x ，则认为 n 是 2 的幂次方。

 

示例 1：

输入：n = 1
输出：true
解释：20 = 1
示例 2：

输入：n = 16
输出：true
解释：24 = 16
示例 3：

输入：n = 3
输出：false
示例 4：

输入：n = 4
输出：true
示例 5：

输入：n = 5
输出：false
 

提示：

-231 <= n <= 231 - 1
 

进阶：你能够不使用循环/递归解决此问题吗？
'''


class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n & (n-1) == 0 if n > 0 else False
        
# solutions


'''
方法一：二进制表示
思路与算法

一个数 nn 是 22 的幂，当且仅当 nn 是正整数，并且 nn 的二进制表示中仅包含 11 个 11。

因此我们可以考虑使用位运算，将 nn 的二进制表示中最低位的那个 11 提取出来，再判断剩余的数值是否为 00 即可。下面介绍两种常见的与「二进制表示中最低位」相关的位运算技巧。

第一个技巧是

\texttt{n \& (n - 1)}
n & (n - 1)

其中 \texttt{\&}& 表示按位与运算。该位运算技巧可以直接将 nn 二进制表示的最低位 11 移除，它的原理如下：

假设 nn 的二进制表示为 (a 10\cdots 0)_2(a10⋯0) 
2
​	
 ，其中 aa 表示若干个高位，11 表示最低位的那个 11，0\cdots 00⋯0 表示后面的若干个 00，那么 n-1n−1 的二进制表示为：

(a 01\cdots1)_2
(a01⋯1) 
2
​	
 

我们将 (a 10\cdots 0)_2(a10⋯0) 
2
​	
  与 (a 01\cdots1)_2(a01⋯1) 
2
​	
  进行按位与运算，高位 aa 不变，在这之后的所有位都会变为 00，这样我们就将最低位的那个 11 移除了。

因此，如果 nn 是正整数并且 \texttt{n \& (n - 1) = 0}n & (n - 1) = 0，那么 nn 就是 22 的幂。

第二个技巧是

\texttt{n \& (-n)}
n & (-n)

其中 -n−n 是 nn 的相反数，是一个负数。该位运算技巧可以直接获取 nn 二进制表示的最低位的 11。

由于负数是按照补码规则在计算机中存储的，-n−n 的二进制表示为 nn 的二进制表示的每一位取反再加上 11，因此它的原理如下：

假设 nn 的二进制表示为 (a 10\cdots 0)_2(a10⋯0) 
2
​	
 ，其中 aa 表示若干个高位，11 表示最低位的那个 11，0\cdots 00⋯0 表示后面的若干个 00，那么 -n−n 的二进制表示为：

(\bar{a} 01\cdots1)_2 + (1)_2 = (\bar{a} 10\cdots0)_2
( 
a
ˉ
 01⋯1) 
2
​	
 +(1) 
2
​	
 =( 
a
ˉ
 10⋯0) 
2
​	
 

其中 \bar{a} 
a
ˉ
  表示将 aa 每一位取反。我们将 (a 10\cdots 0)_2(a10⋯0) 
2
​	
  与 (\bar{a} 10\cdots0)_2( 
a
ˉ
 10⋯0) 
2
​	
  进行按位与运算，高位全部变为 00，最低位的 11 以及之后的所有 00 不变，这样我们就获取了 nn 二进制表示的最低位的 11。

因此，如果 nn 是正整数并且 \texttt{n \& (-n) = n}n & (-n) = n，那么 nn 就是 22 的幂。

代码

下面分别给出两种位运算技巧对应的代码。
在一些语言中，位运算的优先级较低，需要注意运算顺序。

C++JavaC#Python3JavaScriptGolangC

func isPowerOfTwo(n int) bool {
    return n > 0 && n&(n-1) == 0
}
C++JavaC#Python3JavaScriptGolangC

func isPowerOfTwo(n int) bool {
    return n > 0 && n&-n == n
}
复杂度分析

时间复杂度：O(1)O(1)。

空间复杂度：O(1)O(1)。

方法二：判断是否为最大 22 的幂的约数
思路与算法

除了使用二进制表示判断之外，还有一种较为取巧的做法。

在题目给定的 3232 位有符号整数的范围内，最大的 22 的幂为 2^{30} = 10737418242 
30
 =1073741824。我们只需要判断 nn 是否是 2^{30}2 
30
  的约数即可。

代码

C++JavaC#Python3JavaScriptGolangC

func isPowerOfTwo(n int) bool {
    const big = 1 << 30
    return n > 0 && big%n == 0
}
复杂度分析

时间复杂度：O(1)O(1)。

空间复杂度：O(1)O(1)。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/power-of-two/solution/2de-mi-by-leetcode-solution-rny3/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
