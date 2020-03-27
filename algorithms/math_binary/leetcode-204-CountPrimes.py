'''
204. Count Primes
Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

204. 计数质数
统计所有小于非负整数 n 的质数的数量。

示例:

输入: 10
输出: 4
解释: 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
'''


class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        is_prime_dict = [1] * n
        is_prime_dict[:2] = [0 ] *2
        def is_prime(num):
            for i in range(2, int(math.sqrt(num) ) +1):
                if num % i == 0:
                    return False
            return True


        for i in range(2, int(math.sqrt(n)) + 1):
            if is_prime(i):
                is_prime_dict[ i *2:n:i] = [0] * (( n -1 - 2* i) / i + 1)

        return sum(is_prime_dict)

if __name__ == '__main__':
    print(bin(100)[::-1][:-2])
