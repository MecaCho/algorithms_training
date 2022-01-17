# encoding=utf8

'''
1220. Count Vowels Permutation
Given an integer n, your task is to count how many strings of length n can be formed under the following rules:

Each character is a lower case vowel ('a', 'e', 'i', 'o', 'u')
Each vowel 'a' may only be followed by an 'e'.
Each vowel 'e' may only be followed by an 'a' or an 'i'.
Each vowel 'i' may not be followed by another 'i'.
Each vowel 'o' may only be followed by an 'i' or a 'u'.
Each vowel 'u' may only be followed by an 'a'.
Since the answer may be too large, return it modulo 10^9 + 7.

 

Example 1:

Input: n = 1
Output: 5
Explanation: All possible strings are: "a", "e", "i" , "o" and "u".
Example 2:

Input: n = 2
Output: 10
Explanation: All possible strings are: "ae", "ea", "ei", "ia", "ie", "io", "iu", "oi", "ou" and "ua".
Example 3: 

Input: n = 5
Output: 68
 

Constraints:

1 <= n <= 2 * 10^4
'''

class Solution(object):
    def countVowelPermutation(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 元音字母 a 前面只能跟着 ‘e’,‘i’,‘u’；
        # 元音字母 ‘e’ 前面只能跟着 ‘a’,‘i’；
        # 每个元音 ‘i’ 前面只能跟着 ‘e’,‘o’；
        # 每个元音 ‘o’ 前面只能跟着 ‘i’；
        # 每个元音 ‘u’ 后面只能跟着 ‘o’,‘i’；
        a, e, i, o, u = 1,1,1,1,1
        M = int(1e9 + 7)
        for _ in range(n-1):
            aa = (e + i +u) % M
            ee = (a + i) % M
            ii = (e + o) % M
            oo = i % M 
            uu = (o + i) % M
            a = aa
            e = ee
            i = ii
            o = oo
            u = uu

        return (a + e + i + o + u) % M

# solutions

'''
我们设 dp[i][j] 代表当前长度为 i且以字符 j 为结尾的字符串的数目
   
dp[i][0]=dp[i−1][1]+dp[i−1][2]+dp[i−1][4]
dp[i][1]=dp[i−1][0]+dp[i−1][2]
dp[i][2]=dp[i−1][1]+dp[i−1][3]
dp[i][3]=dp[i−1][2]
dp[i][4]=dp[i−1][2]+dp[i−1][3] 

'''

