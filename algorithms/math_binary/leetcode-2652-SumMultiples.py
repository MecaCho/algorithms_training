# encoding=utf8

'''
2652. Sum Multiples

Given a positive integer n, find the sum of all integers in the range [1, n] inclusive that are divisible by 3, 5, or 7.

Return an integer denoting the sum of all numbers in the given range satisfying the constraint.

 

Example 1:

Input: n = 7
Output: 21
Explanation: Numbers in the range [1, 7] that are divisible by 3, 5, or 7 are 3, 5, 6, 7. The sum of these numbers is 21.
Example 2:

Input: n = 10
Output: 40
Explanation: Numbers in the range [1, 10] that are divisible by 3, 5, or 7 are 3, 5, 6, 7, 9, 10. The sum of these numbers is 40.
Example 3:

Input: n = 9
Output: 30
Explanation: Numbers in the range [1, 9] that are divisible by 3, 5, or 7 are 3, 5, 6, 7, 9. The sum of these numbers is 30.
 

Constraints:

1 <= n <= 103
'''

class Solution:
    def sumOfMultiples(self, n: int) -> int:
        # 3, 5,7,15,21,35,105
        # 3,15,21,105
        # 5,15,35,105
        # 7,21,35,105
        def sum_m_n(n, m):
            return (m+n//m*m)*(n//m)//2
        return sum_m_n(n, 3) + sum_m_n(n, 5) + sum_m_n(n, 7) - sum_m_n(n, 3*5) - sum_m_n(n, 3*7) - sum_m_n(n, 5*7) + sum_m_n(n, 3*5*7)

