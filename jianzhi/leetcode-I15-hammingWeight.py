'''
面试题15. 二进制中1的个数
请实现一个函数，输入一个整数，输出该数二进制表示中 1 的个数。例如，把 9 表示成二进制是 1001，有 2 位是 1。因此，如果输入 9，则该函数输出 2。

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
 

注意：本题与主站 191 题相同：https://leetcode-cn.com/problems/number-of-1-bits/
'''



class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        # res = 0
        # while n:
        #     res += 1
        #     n = n & (n-1)
        # return res
        res = 0
        while n:
            if n % 2 == 1:
                res += 1
            n /= 2
        return res

       
       
       
# solutions
       
‘’‘
方法一：循环检查二进制位
思路及解法

我们可以直接循环检查给定整数 nn 的二进制位的每一位是否为 11。

具体代码中，当检查第 ii 位时，我们可以让 nn 与 2^i2 
i
  进行与运算，当且仅当 nn 的第 ii 位为 11 时，运算结果不为 00。

代码

C++JavaC#Python3GolangJavaScriptC

func hammingWeight(num uint32) (ones int) {
    for i := 0; i < 32; i++ {
        if 1<<i&num > 0 {
            ones++
        }
    }
    return
}
复杂度分析

时间复杂度：O(k)O(k)，其中 kk 是 \texttt{int}int 型的二进制位数，k=32k=32。我们需要检查 nn 的二进制位的每一位，一共需要检查 3232 位。

空间复杂度：O(1)O(1)，我们只需要常数的空间保存若干变量。

方法二：位运算优化
思路及解法

观察这个运算：n~\&~(n - 1)n & (n−1)，其预算结果恰为把 nn 的二进制位中的最低位的 11 变为 00 之后的结果。

如：6~\&~(6-1) = 4, 6 = (110)_2, 4 = (100)_26 & (6−1)=4,6=(110) 
2
​
 ,4=(100) 
2
​
 ，运算结果 44 即为把 66 的二进制位中的最低位的 11 变为 00 之后的结果。

这样我们可以利用这个位运算的性质加速我们的检查过程，在实际代码中，我们不断让当前的 nn 与 n - 1n−1 做与运算，直到 nn 变为 00 即可。因为每次运算会使得 nn 的最低位的 11 被翻转，因此运算次数就等于 nn 的二进制位中 11 的个数。

代码

C++JavaC#Python3GolangJavaScriptC

func hammingWeight(num uint32) (ones int) {
    for ; num > 0; num &= num - 1 {
        ones++
    }
    return
}
复杂度分析

时间复杂度：O(\log n)O(logn)。循环次数等于 nn 的二进制位中 11 的个数，最坏情况下 nn 的二进制位全部为 11。我们需要循环 \log nlogn 次。

空间复杂度：O(1)O(1)，我们只需要常数的空间保存若干变量。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/er-jin-zhi-zhong-1de-ge-shu-lcof/solution/er-jin-zhi-zhong-1de-ge-shu-by-leetcode-50bb1/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
’‘’
