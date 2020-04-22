
'''
面试题44. 数字序列中某一位的数字
数字以0123456789101112131415…的格式序列化到一个字符序列中。在这个序列中，第5位（从下标0开始计数）是5，第13位是1，第19位是4，等等。

请写一个函数，求任意第n位对应的数字。



示例 1：

输入：n = 3
输出：3
示例 2：

输入：n = 11
输出：0


限制：

0 <= n < 2^31
注意：本题与主站 400 题相同：https://leetcode-cn.com/problems/nth-digit/
'''



class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        step = [10]
        j = 2
        st = 10
        while st <= 2**31 and n >= st:
            st +=  j*9*(pow(10, (j-1)))
            step.append(st)
            j += 1
        print(step)
        if n < 10:
            return n
        for k in range(1, len(step)+1):
            if n < step[k]:
                return int(str(10**k + (n - step[k-1]) / (k+1))[(n-step[k-1])%(k+1)])
