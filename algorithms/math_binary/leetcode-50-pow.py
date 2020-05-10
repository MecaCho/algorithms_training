'''
50. Pow(x, n)
Implement pow(x, n), which calculates x raised to the power n (xn).

Example 1:

Input: 2.00000, 10
Output: 1024.00000
Example 2:

Input: 2.10000, 3
Output: 9.26100
Example 3:

Input: 2.00000, -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
Note:

-100.0 < x < 100.0
n is a 32-bit signed integer, within the range [−231, 231 − 1]

50. Pow(x, n)
实现 pow(x, n) ，即计算 x 的 n 次幂函数。

示例 1:

输入: 2.00000, 10
输出: 1024.00000
示例 2:

输入: 2.10000, 3
输出: 9.26100
示例 3:

输入: 2.00000, -2
输出: 0.25000
解释: 2-2 = 1/22 = 1/4 = 0.25
说明:

-100.0 < x < 100.0
n 是 32 位有符号整数，其数值范围是 [−231, 231 − 1] 。
'''

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        elif n == 1:
            return x

        exp = abs(n)
        ret = self.myPow(x, exp >> 1)
        ret *= ret
        if exp & 0x1 == 1:
            ret = x * ret

        if n > 0:
            return ret
        return 1.0000000000 / ret


'''
前言
本题的方法被称为「快速幂算法」，有递归和迭代两个版本。这篇题解会从递归版本的开始讲起，再逐步引出迭代的版本。

当指数 nn 为负数时，我们可以计算 x^{-n}x 
−n
  再取倒数得到结果，因此我们只需要考虑 nn 为自然数的情况。

方法一：快速幂 + 递归
「快速幂算法」的本质是分治算法。举个例子，如果我们要计算 x^{64}x 
64
 ，我们可以按照：

x \to x^2 \to x^4 \to x^8 \to x^{16} \to x^{32} \to x^{64}
x→x 
2
 →x 
4
 →x 
8
 →x 
16
 →x 
32
 →x 
64
 

的顺序，从 xx 开始，每次直接把上一次的结果进行平方，计算 66 次就可以得到 x^{64}x 
64
  的值，而不需要对 xx 乘 6363 次 xx。

再举一个例子，如果我们要计算 x^{77}x 
77
 ，我们可以按照：

x \to x^2 \to x^4 \to x^9 \to x^{19} \to x^{38} \to x^{77}
x→x 
2
 →x 
4
 →x 
9
 →x 
19
 →x 
38
 →x 
77
 

的顺序，在 x \to x^2x→x 
2
 ，x^2 \to x^4x 
2
 →x 
4
 ，x^{19} \to x^{38}x 
19
 →x 
38
  这些步骤中，我们直接把上一次的结果进行平方，而在 x^4 \to x^9x 
4
 →x 
9
 ，x^9 \to x^{19}x 
9
 →x 
19
 ，x^{38} \to x^{77}x 
38
 →x 
77
  这些步骤中，我们把上一次的结果进行平方后，还要额外乘一个 xx。

直接从左到右进行推导看上去很困难，因为在每一步中，我们不知道在将上一次的结果平方之后，还需不需要额外乘 xx。但如果我们从右往左看，分治的思想就十分明显了：

当我们要计算 x^nx 
n
  时，我们可以先递归地计算出 y = x^{\lfloor n/2 \rfloor}y=x 
⌊n/2⌋
 ，其中 \lfloor a \rfloor⌊a⌋ 表示对 aa 进行下取整；

根据递归计算的结果，如果 nn 为偶数，那么 x^n = y^2x 
n
 =y 
2
 ；如果 nn 为奇数，那么 x^n = y^2 * xx 
n
 =y 
2
 ∗x；

递归的边界为 n = 0n=0，任意数的 00 次方均为 11。

由于每次递归都会使得指数减少一半，因此递归的层数为 O(\log n)O(logn)，算法可以在很快的时间内得到结果。

C++JavaPython3Golang
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def quickMul(N):
            if N == 0:
                return 1.0
            y = quickMul(N // 2)
            return y * y if N % 2 == 0 else y * y * x
        
        return quickMul(n) if n >= 0 else 1.0 / quickMul(-n)
复杂度分析

时间复杂度：O(\log n)O(logn)，即为递归的层数。

空间复杂度：O(\log n)O(logn)，即为递归的层数。这是由于递归的函数调用会使用栈空间。

方法二：快速幂 + 迭代
由于递归需要使用额外的栈空间，我们试着将递归转写为迭代。在方法一中，我们也提到过，从左到右进行推导是不容易的，因为我们不知道是否需要额外乘 xx。但我们不妨找一找规律，看看哪些地方额外乘了 xx，并且它们对答案产生了什么影响。

我们还是以 x^{77}x 
77
  作为例子：

x \to x^2 \to x^4 \to^+ x^9 \to^+ x^{19} \to x^{38} \to^+ x^{77}
x→x 
2
 →x 
4
 → 
+
 x 
9
 → 
+
 x 
19
 →x 
38
 → 
+
 x 
77
 

并且把需要额外乘 xx 的步骤打上了 ++ 标记。可以发现：

x^{38} \to^+ x^{77}x 
38
 → 
+
 x 
77
  中额外乘的 xx 在 x^{77}x 
77
  中贡献了 xx；

x^9 \to^+ x^{19}x 
9
 → 
+
 x 
19
  中额外乘的 xx 在之后被平方了 22 次，因此在 x^{77}x 
77
  中贡献了 x^{2^2} = x^4x 
2 
2
 
 =x 
4
 ；

x^4 \to^+ x^9x 
4
 → 
+
 x 
9
  中额外乘的 xx 在之后被平方了 33 次，因此在 x^{77}x 
77
  中贡献了 x^{2^3} = x^8x 
2 
3
 
 =x 
8
 ；

最初的 xx 在之后被平方了 66 次，因此在 x^{77}x 
77
  中贡献了 x^{2^6} = x^{64}x 
2 
6
 
 =x 
64
 。

我们把这些贡献相乘，x * x^4 * x^8 * x^{64}x∗x 
4
 ∗x 
8
 ∗x 
64
  恰好等于 x^{77}x 
77
 。而这些贡献的指数部分又是什么呢？它们都是 22 的幂次，这是因为每个额外乘的 xx 在之后都会被平方若干次。而这些指数 11，44，88 和 6464，恰好就对应了 7777 的二进制表示 (1001101)_2(1001101) 
2
​	
  中的每个 11！

因此我们借助整数的二进制拆分，就可以得到迭代计算的方法，一般地，如果整数 nn 的二进制拆分为

n = 2^{i_0} + 2^{i_1} + \cdots + 2^{i_k}
n=2 
i 
0
​	
 
 +2 
i 
1
​	
 
 +⋯+2 
i 
k
​	
 
 

那么

x^n = x^{2^{i_0}} * x^{2^{i_1}} * \cdots * x^{2^{i_k}}
x 
n
 =x 
2 
i 
0
​	
 
 
 ∗x 
2 
i 
1
​	
 
 
 ∗⋯∗x 
2 
i 
k
​	
 
 
 

这样以来，我们从 xx 开始不断地进行平方，得到 x^2, x^4, x^8, x^{16}, \cdotsx 
2
 ,x 
4
 ,x 
8
 ,x 
16
 ,⋯，如果 nn 的第 kk 个（从右往左，从 00 开始计数）二进制位为 11，那么我们就将对应的贡献 x^{2^k}x 
2 
k
 
 计入答案。

下面的代码给出了详细的注释。

C++JavaPython3Golang
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def quickMul(N):
            ans = 1.0
            # 贡献的初始值为 x
            x_contribute = x
            # 在对 N 进行二进制拆分的同时计算答案
            while N > 0:
                if N % 2 == 1:
                    # 如果 N 二进制表示的最低位为 1，那么需要计入贡献
                    ans *= x_contribute
                # 将贡献不断地平方
                x_contribute *= x_contribute
                # 舍弃 N 二进制表示的最低位，这样我们每次只要判断最低位即可
                N //= 2
            return ans
        
        return quickMul(n) if n >= 0 else 1.0 / quickMul(-n)
复杂度分析

时间复杂度：O(\log n)O(logn)，即为对 nn 进行二进制拆分的时间复杂度。

空间复杂度：O(1)O(1)。

'''
