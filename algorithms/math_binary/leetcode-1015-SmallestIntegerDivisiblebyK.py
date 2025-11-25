# encoding=utf8

'''
1015. Smallest Integer Divisible by K

Given a positive integer k, you need to find the length of the smallest positive integer n such that n is divisible by k, and n only contains the digit 1.

Return the length of n. If there is no such n, return -1.

Note: n may not fit in a 64-bit signed integer.

 

Example 1:

Input: k = 1
Output: 1
Explanation: The smallest answer is n = 1, which has length 1.
Example 2:

Input: k = 2
Output: -1
Explanation: There is no such positive integer n divisible by 2.
Example 3:

Input: k = 3
Output: 3
Explanation: The smallest answer is n = 111, which has length 3.
 

Constraints:

1 <= k <= 105

1015. 可被 K 整除的最小整数

给定正整数 k ，你需要找出可以被 k 整除的、仅包含数字 1 的最 小 正整数 n 的长度。

返回 n 的长度。如果不存在这样的 n ，就返回-1。

注意： n 可能不符合 64 位带符号整数。

 

示例 1：

输入：k = 1
输出：1
解释：最小的答案是 n = 1，其长度为 1。

示例 2：

输入：k = 2
输出：-1
解释：不存在可被 2 整除的正整数 n 。

示例 3：

输入：k = 3
输出：3
解释：最小的答案是 n = 111，其长度为 3。

 

提示：

    1 <= k <= 105
'''

class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 2 == 0 or k % 5 == 0:  
            return -1
        
        res, resid = 1, 1  
        while resid % k != 0:  
            resid = (resid % k) * (10 % k) + 1  
            res += 1  
            
        return res  
