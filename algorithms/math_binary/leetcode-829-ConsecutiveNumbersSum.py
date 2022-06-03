# encoding=utf8

'''
829. Consecutive Numbers Sum
Given a positive integer N, how many ways can we write it as a sum of consecutive positive integers?

Example 1:

Input: 5
Output: 2
Explanation: 5 = 5 = 2 + 3
Example 2:

Input: 9
Output: 3
Explanation: 9 = 9 = 4 + 5 = 2 + 3 + 4
Example 3:

Input: 15
Output: 4
Explanation: 15 = 15 = 8 + 7 = 4 + 5 + 6 = 1 + 2 + 3 + 4 + 5
Note: 1 <= N <= 10 ^ 9.

829. 连续整数求和
给定一个正整数 N，试求有多少组连续正整数满足所有数字之和为 N?

示例 1:

输入: 5
输出: 2
解释: 5 = 5 = 2 + 3，共有两组连续整数([5],[2,3])求和后为 5。
示例 2:

输入: 9
输出: 3
解释: 9 = 9 = 4 + 5 = 2 + 3 + 4
示例 3:

输入: 15
输出: 4
解释: 15 = 15 = 8 + 7 = 4 + 5 + 6 = 1 + 2 + 3 + 4 + 5
说明: 1 <= N <= 10 ^ 9
'''


class Solution(object):
    def consecutiveNumbersSum(self, N):
        """
        :type N: int
        :rtype: int
        """
        # 2N=k(x+x+k-1)
        res = 0
        k = 1
        while (k * k) < 2*N:
            if (2 * N) % k ==0:
                x = ((2 * N) / k + 1 -k)
                if x > 0 and (x % 2 == 0):
                    res += 1
            k += 1
        return res

    
# golang

'''
func consecutiveNumbersSum(n int) int {
        res := 0
        k := 1
        N := n
        for (k * k) < 2*N { 
            if (2 * N) % k ==0{
                x := ((2 * N) / k + 1 -k)
                if x > 0 && (x % 2 == 0){
                    res += 1
                } 
            }
            k += 1
        }
        return res
}
'''
