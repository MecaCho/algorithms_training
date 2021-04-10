# encoding=utf8


'''
263. 丑数
编写一个程序判断给定的数是否为丑数。

丑数就是只包含质因数 2, 3, 5 的正整数。

示例 1:

输入: 6
输出: true
解释: 6 = 2 × 3
示例 2:

输入: 8
输出: true
解释: 8 = 2 × 2 × 2
示例 3:

输入: 14
输出: false
解释: 14 不是丑数，因为它包含了另外一个质因数 7。
说明：

1 是丑数。
输入不会超过 32 位有符号整数的范围: [−231,  231 − 1]。

263. Ugly Number
Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.

Example 1:

Input: 6
Output: true
Explanation: 6 = 2 × 3
Example 2:

Input: 8
Output: true
Explanation: 8 = 2 × 2 × 2
Example 3:

Input: 14
Output: false
Explanation: 14 is not ugly since it includes another prime factor 7.
Note:

1 is typically treated as an ugly number.
Input is within the 32-bit signed integer range: [−231,  231 − 1].
'''




class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        while num > 1:
            count = 0
            for k in [2, 3, 5]:
                if num % k == 0:
                    num /= k
                    count += 1
            if not count:
                return False
        return True



class Solution20210410(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """
        flag = True
        while flag and n:
            if n % 2 == 0:
                flag = True
                n /= 2
            elif n % 3 == 0:
                flag = True
                n /= 3
            elif n % 5 == 0:
                flag = True
                n /= 5
            else:
                flag = False
        return n == 1


# solutions

'''
方法一：数学
根据丑数的定义，00 和负整数一定不是丑数。

当 n>0n>0 时，若 nn 是丑数，则 nn 可以写成 n = 2^a \times 3^b \times 5^cn=2 
a
 ×3 
b
 ×5 
c
  的形式，其中 a,b,ca,b,c 都是非负整数。特别地，当 a,b,ca,b,c 都是 00 时，n=1n=1。

为判断 nn 是否满足上述形式，可以对 nn 反复除以 2,3,52,3,5，直到 nn 不再包含质因数 2,3,52,3,5。若剩下的数等于 11，则说明 nn 不包含其他质因数，是丑数；否则，说明 nn 包含其他质因数，不是丑数。

JavaJavaScriptGolangPython3C++C

class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False

        factors = [2, 3, 5]
        for factor in factors:
            while n % factor == 0:
                n //= factor
        
        return n == 1
复杂度分析

时间复杂度：O(\log n)O(logn)。时间复杂度取决于对 nn 除以 2,3,52,3,5 的次数，由于每次至少将 nn 除以 22，因此除法运算的次数不会超过 O(\log n)O(logn)。

空间复杂度：O(1)O(1)。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/ugly-number/solution/chou-shu-by-leetcode-solution-fazd/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
