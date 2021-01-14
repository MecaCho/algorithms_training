# encoding=utf8

'''
1018. Binary Prefix Divisible By 5
Given an array A of 0s and 1s, consider N_i: the i-th subarray from A[0] to A[i] interpreted as a binary number (from most-significant-bit to least-significant-bit.)

Return a list of booleans answer, where answer[i] is true if and only if N_i is divisible by 5.

Example 1:

Input: [0,1,1]
Output: [true,false,false]
Explanation:
The input numbers in binary are 0, 01, 011; which are 0, 1, and 3 in base-10.  Only the first number is divisible by 5, so answer[0] is true.
Example 2:

Input: [1,1,1]
Output: [false,false,false]
Example 3:

Input: [0,1,1,1,1,1]
Output: [true,false,false,false,true,false]
Example 4:

Input: [1,1,1,0,1]
Output: [false,false,false,false,false]


Note:

1 <= A.length <= 30000
A[i] is 0 or 1


1018. 可被 5 整除的二进制前缀
给定由若干 0 和 1 组成的数组 A。我们定义 N_i：从 A[0] 到 A[i] 的第 i 个子数组被解释为一个二进制数（从最高有效位到最低有效位）。

返回布尔值列表 answer，只有当 N_i 可以被 5 整除时，答案 answer[i] 为 true，否则为 false。



示例 1：

输入：[0,1,1]
输出：[true,false,false]
解释：
输入数字为 0, 01, 011；也就是十进制中的 0, 1, 3 。只有第一个数可以被 5 整除，因此 answer[0] 为真。
示例 2：

输入：[1,1,1]
输出：[false,false,false]
示例 3：

输入：[0,1,1,1,1,1]
输出：[true,false,false,false,true,false]
示例 4：

输入：[1,1,1,0,1]
输出：[false,false,false,false,false]


提示：

1 <= A.length <= 30000
A[i] 为 0 或 1
'''


class Solution(object):
    def prefixesDivBy5(self, A):
        """
        :type A: List[int]
        :rtype: List[bool]
        """
        res = []
        value = 0
        for a in A:
            value *= 2
            value += a
            if value % 5 == 0:
                res.append(True)
            else:
                res.append(False)
        return res



# solutions

'''
方法一：模拟
令 N_iN 
i
​	
  为数组 AA 从下标 00 到下标 ii 的前缀表示的二进制数，则有 N_0=A[0]N 
0
​	
 =A[0]。当 i>0i>0 时，有 N_i=N_{i-1} \times 2+A[i]N 
i
​	
 =N 
i−1
​	
 ×2+A[i]。令 nn 为数组 AA 的长度，则对于 0 \le i<n0≤i<n，可以依次计算每个 N_iN 
i
​	
  的值。对于每个 N_iN 
i
​	
  的值，判断其是否可以被 55 整除，即可得到答案。

考虑到数组 AA 可能很长，如果每次都保留 N_iN 
i
​	
  的值，则可能导致溢出。由于只需要知道每个 N_iN 
i
​	
  是否可以被 55 整除，因此在计算过程中只需要保留余数即可。

令 M_iM 
i
​	
  表示计算到下标 ii 时的除以 55 的余数，则有 M_0=A[0]M 
0
​	
 =A[0]（显然 A[0]A[0] 一定小于 55），当 i>0i>0 时，有 M_i=(M_{i-1} \times 2+A[i])\bmod 5M 
i
​	
 =(M 
i−1
​	
 ×2+A[i])mod5，判断每个 M_iM 
i
​	
  是否为 00 即可。由于 M_iM 
i
​	
  一定小于 55，因此不会溢出。

如何证明判断 M_iM 
i
​	
  是否为 00 可以得到正确的结果？可以通过数学归纳法证明。

当 i=0i=0 时，由于 N_0=A[0]<5N 
0
​	
 =A[0]<5，因此 M_0=N_0M 
0
​	
 =N 
0
​	
 ，M_0=N_0\bmod 5M 
0
​	
 =N 
0
​	
 mod5 成立。

当 i>0i>0 时，假设 M_{i-1}=N_{i-1}\bmod 5M 
i−1
​	
 =N 
i−1
​	
 mod5 成立，考虑 N_i\bmod 5N 
i
​	
 mod5 和 M_iM 
i
​	
  的值：

\begin{aligned} N_i\bmod 5=&(N_{i-1} \times 2+A[i])\bmod 5 \\ =&(N_{i-1} \times 2)\bmod 5+A[i]\bmod 5 \\ \\ M_i=&(M_{i-1} \times 2+A[i])\bmod 5 \\ =&(N_{i-1}\bmod 5 \times 2+A[i])\bmod 5 \\ =&(N_{i-1}\bmod 5 \times 2)\bmod 5+A[i]\bmod 5 \\ =&(N_{i-1} \times 2)\bmod 5+A[i]\bmod 5 \end{aligned}
N 
i
​	
 mod5=
=
M 
i
​	
 =
=
=
=
​	
  
(N 
i−1
​	
 ×2+A[i])mod5
(N 
i−1
​	
 ×2)mod5+A[i]mod5
(M 
i−1
​	
 ×2+A[i])mod5
(N 
i−1
​	
 mod5×2+A[i])mod5
(N 
i−1
​	
 mod5×2)mod5+A[i]mod5
(N 
i−1
​	
 ×2)mod5+A[i]mod5
​	
 

因此有 M_i=N_i\bmod 5M 
i
​	
 =N 
i
​	
 mod5 成立。

由此可得，对任意 0 \le i<n0≤i<n，都有 M_i=N_i\bmod 5M 
i
​	
 =N 
i
​	
 mod5，因此计算 M_iM 
i
​	
  即可得到正确的结果。

JavaC++JavaScriptPythonGolangC

class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        ans = list()
        prefix = 0
        for num in A:
            prefix = ((prefix << 1) + num) % 5
            ans.append(prefix == 0)
        return ans
复杂度分析

时间复杂度：O(n)O(n)，其中 nn 是数组 AA 的长度。需要遍历数组一次并计算前缀。

空间复杂度：O(1)O(1)。除了返回值以外，额外使用的空间为常数。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/binary-prefix-divisible-by-5/solution/ke-bei-5-zheng-chu-de-er-jin-zhi-qian-zh-asih/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
