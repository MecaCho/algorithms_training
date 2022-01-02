# encoding=utf8

'''
390. Elimination Game
You have a list arr of all integers in the range [1, n] sorted in a strictly increasing order. Apply the following algorithm on arr:

Starting from left to right, remove the first number and every other number afterward until you reach the end of the list.
Repeat the previous step again, but this time from right to left, remove the rightmost number and every other number from the remaining numbers.
Keep repeating the steps again, alternating left to right and right to left, until a single number remains.
Given the integer n, return the last number that remains in arr.

 

Example 1:

Input: n = 9
Output: 6
Explanation:
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
arr = [2, 4, 6, 8]
arr = [2, 6]
arr = [6]
Example 2:

Input: n = 1
Output: 1
 

Constraints:

1 <= n <= 109
'''

class Solution(object):
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        return 1 if n== 1 else 2 * (n / 2 + 1 - self.lastRemaining(n / 2))

      
      
# solutions

'''
假如输入为 n，我们使用 f(n) 表示 从左到右(forward) 的最终结果，使用 b(n)表示 从右到左(backward) 的最终结果。则：

当 n = 1 时，存在 f(n) = 1, b(n) = 1
对于任意 n，存在 f(n) + b(n) = n + 1
对于 n > 2 的情况下，f(n) = 2 * b(n / 2)
所以：f(n) = 2 * (n / 2 + 1 - f(n / 2))

https://blog.csdn.net/afei__/article/details/83689502
'''

