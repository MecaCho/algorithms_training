# encoding=utf8


'''
191. Number of 1 Bits
Write a function that takes an unsigned integer and return the number of '1' bits it has (also known as the Hamming weight).

 

Example 1:

Input: 00000000000000000000000000001011
Output: 3
Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.
Example 2:

Input: 00000000000000000000000010000000
Output: 1
Explanation: The input binary string 00000000000000000000000010000000 has a total of one '1' bit.
Example 3:

Input: 11111111111111111111111111111101
Output: 31
Explanation: The input binary string 11111111111111111111111111111101 has a total of thirty one '1' bits.
 

Note:

Note that in some languages such as Java, there is no unsigned integer type. In this case, the input will be given as signed integer type and should not affect your implementation, as the internal binary representation of the integer is the same whether it is signed or unsigned.
In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 3 above the input represents the signed integer -3.
 

Follow up:

If this function is called many times, how would you optimize it?

191. 位1的个数
编写一个函数，输入是一个无符号整数，返回其二进制表达式中数字位数为 ‘1’ 的个数（也被称为汉明重量）。

 

示例 1：

输入：00000000000000000000000000001011
输出：3
解释：输入的二进制串 00000000000000000000000000001011 中，共有三位为 '1'。
示例 2：

输入：00000000000000000000000010000000
输出：1
解释：输入的二进制串 00000000000000000000000010000000 中，共有一位为 '1'。
示例 3：

输入：11111111111111111111111111111101
输出：31
解释：输入的二进制串 11111111111111111111111111111101 中，共有 31 位为 '1'。
 

提示：

请注意，在某些语言（如 Java）中，没有无符号整数类型。在这种情况下，输入和输出都将被指定为有符号整数类型，并且不应影响您的实现，因为无论整数是有符号的还是无符号的，其内部的二进制表示形式都是相同的。
在 Java 中，编译器使用二进制补码记法来表示有符号整数。因此，在上面的 示例 3 中，输入表示有符号整数 -3。
 

进阶:
如果多次调用这个函数，你将如何优化你的算法？
'''



class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        while n:
            res += 1
            n = n & (n-1)
        return res




class Solution20210322(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        while n:
            n &= n -1
            res += 1

        return res



# solutions

'''
方法 1：循环和位移动
算法

这个方法比较直接。我们遍历数字的 32 位。如果某一位是 11 ，将计数器加一。

我们使用 位掩码 来检查数字的第 i^{th}i 
th
  位。一开始，掩码 m=1m=1 因为 11 的二进制表示是

0000\ 0000\ 0000\ 0000\ 0000\ 0000\ 0000\ 0001
0000 0000 0000 0000 0000 0000 0000 0001

显然，任何数字跟掩码 11 进行逻辑与运算，都可以让我们获得这个数字的最低位。检查下一位时，我们将掩码左移一位。

0000\ 0000\ 0000\ 0000\ 0000\ 0000\ 0000\ 0010
0000 0000 0000 0000 0000 0000 0000 0010

并重复此过程。

class Solution:
    def hammingWeight(self, n: int) -> int:
        ret = sum(1 for i in range(32) if n & (1 << i)) 
        return ret

复杂度分析

时间复杂度：O(1)O(1) 。运行时间依赖于数字 nn 的位数。由于这题中 nn 是一个 32 位数，所以运行时间是 O(1)O(1) 的。

空间复杂度：O(1)O(1)。没有使用额外空间。

方法 2：位操作的小技巧
算法

我们可以把前面的算法进行优化。我们不再检查数字的每一个位，而是不断把数字最后一个 11 反转，并把答案加一。当数字变成 00 的时候偶，我们就知道它没有 11 的位了，此时返回答案。

这里关键的想法是对于任意数字 nn ，将 nn 和 n - 1n−1 做与运算，会把最后一个 11 的位变成 00 。为什么？考虑 nn 和 n - 1n−1 的二进制表示。



图片 1. 将 nn 和 n-1n−1 做与运算会将最低位的 11 变成 00

在二进制表示中，数字 nn 中最低位的 11 总是对应 n - 1n−1 中的 00 。因此，将 nn 和 n - 1n−1 与运算总是能把 nn 中最低位的 11 变成 00 ，并保持其他位不变。

使用这个小技巧，代码变得非常简单。

class Solution:
    def hammingWeight(self, n: int) -> int:
        ret = 0
        while n:
            n &= n - 1
            ret += 1
        return ret

复杂度分析

时间复杂度：O(1)O(1) 。运行时间与 nn 中位为 11 的有关。在最坏情况下， nn 中所有位都是 11 。对于 32 位整数，运行时间是 O(1)O(1) 的。

空间复杂度：O(1)O(1) 。没有使用额外空间。

作者：LeetCode
链接：https://leetcode-cn.com/problems/number-of-1-bits/solution/wei-1de-ge-shu-by-leetcode/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
