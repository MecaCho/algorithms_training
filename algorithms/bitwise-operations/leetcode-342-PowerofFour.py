# encoding=utf8

'''
342. Power of Four

Given an integer n, return true if it is a power of four. Otherwise, return false.

An integer n is a power of four, if there exists an integer x such that n == 4x.

 

Example 1:

Input: n = 16
Output: true
Example 2:

Input: n = 5
Output: false
Example 3:

Input: n = 1
Output: true
 

Constraints:

-231 <= n <= 231 - 1
 

Follow up: Could you solve it without loops/recursion?

342. 4的幂

给定一个整数，写一个函数来判断它是否是 4 的幂次方。如果是，返回 true ；否则，返回 false 。

整数 n 是 4 的幂次方需满足：存在整数 x 使得 n == 4x

 

示例 1：

输入：n = 16
输出：true
示例 2：

输入：n = 5
输出：false
示例 3：

输入：n = 1
输出：true
 

提示：

-231 <= n <= 231 - 1
 

进阶：

你能不使用循环或者递归来完成本题吗？
'''


class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0 or n & (n-1) != 0:
            return False
        return len(bin(n)) % 2 == 1
      
      
# solutions

'''
前言
如果 nn 是 44 的幂，那么 nn 一定也是 22 的幂。因此我们可以首先判断 nn 是否是 22 的幂，在此基础上再判断 nn 是否是 44 的幂。

判断 nn 是否是 22 的幂可以参考「231. 2的幂的官方题解」。由于这一步的方法有很多种，在下面的题解中，我们使用

\texttt{n \& (n - 1)}
n & (n - 1)

这一方法进行判断。

方法一：二进制表示中 11 的位置
思路与算法

如果 nn 是 44 的幂，那么 nn 的二进制表示中有且仅有一个 11，并且这个 11 出现在从低位开始的第偶数个二进制位上（这是因为这个 11 后面必须有偶数个 00）。这里我们规定最低位为第 00 位，例如 n=16n=16 时，nn 的二进制表示为

(10000)_2
(10000) 
2
​	
 

唯一的 11 出现在第 44 个二进制位上，因此 nn 是 44 的幂。

由于题目保证了 nn 是一个 3232 位的有符号整数，因此我们可以构造一个整数 \textit{mask}mask，它的所有偶数二进制位都是 00，所有奇数二进制位都是 11。这样一来，我们将 nn 和 \textit{mask}mask 进行按位与运算，如果结果为 00，说明 nn 二进制表示中的 11 出现在偶数的位置，否则说明其出现在奇数的位置。

根据上面的思路，\textit{mask}mask 的二进制表示为：

\textit{mask} = (10101010101010101010101010101010)_2
mask=(10101010101010101010101010101010) 
2
​	
 

我们也可以将其表示成 1616 进制的形式，使其更加美观：

\textit{mask} = (\text{AAAAAAAA})_{16}
mask=(AAAAAAAA) 
16
​	
 

代码

C++JavaC#Python3JavaScriptGolangC

func isPowerOfFour(n int) bool {
    return n > 0 && n&(n-1) == 0 && n&0xaaaaaaaa == 0
}
复杂度分析

时间复杂度：O(1)O(1)。

空间复杂度：O(1)O(1)。

思考

事实上，我们令：

\textit{mask} = (\text{2AAAAAAA})_{16}
mask=(2AAAAAAA) 
16
​	
 

也可以使得上面的判断满足要求，读者可以思考其中的原因。

提示：nn 是一个「有符号」的 3232 位整数。

方法二：取模性质
思路与算法

如果 nn 是 44 的幂，那么它可以表示成 4^x4 
x
  的形式，我们可以发现它除以 33 的余数一定为 11，即：

4^x \equiv (3+1)^x \equiv 1^x \equiv 1 \quad (\bmod ~3)
4 
x
 ≡(3+1) 
x
 ≡1 
x
 ≡1(mod 3)

如果 nn 是 22 的幂却不是 44 的幂，那么它可以表示成 4^x \times 24 
x
 ×2 的形式，此时它除以 33 的余数一定为 22。

因此我们可以通过 nn 除以 33 的余数是否为 11 来判断 nn 是否是 44 的幂。

代码

C++JavaC#Python3JavaScriptGolangC

func isPowerOfFour(n int) bool {
    return n > 0 && n&(n-1) == 0 && n%3 == 1
}
复杂度分析

时间复杂度：O(1)O(1)。

空间复杂度：O(1)O(1)。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/power-of-four/solution/4de-mi-by-leetcode-solution-b3ya/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''

