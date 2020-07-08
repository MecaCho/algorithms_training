'''
面试题 17.09. 第 k 个数
有些数的素因子只有 3，5，7，请设计一个算法找出第 k 个数。注意，不是必须有这些素因子，而是必须不包含其他的素因子。例如，前几个数按顺序应该是 1，3，5，7，9，15，21。

示例 1:

输入: k = 5

输出: 9

面试题 17.09. Get Kth Magic Number LCCI
Design an algorithm to find the kth number such that the only prime factors are 3, 5, and 7. Note that 3, 5, and 7 do not have to be factors, but it should not have any other prime factors. For example, the first several multiples would be (in order) 1, 3, 5, 7, 9, 15, 21.

Example 1:

Input: k = 5

Output: 9
'''

# https://leetcode-cn.com/problems/ugly-number-ii/
# # 不难发现，一个丑数总是由前面的某一个丑数 x3 / x5 / x7 得到。
# # 反过来说也是一样的，一个丑数 x3 / x5 / x7 就会得到某一个更大的丑数。
# #
# # 如果把丑数数列叫做 ugly[i]，那么考虑一下三个数列：
# # 1. ugly[0]*3,ugly[1]*3,ugly[2]*3,ugly[3]*3,ugly[4]*3,ugly[5]*3……
# # 2. ugly[0]*5,ugly[1]*5,ugly[2]*5,ugly[3]*5,ugly[4]*5,ugly[5]*5……
# # 3. ugly[0]*7,ugly[1]*7,ugly[2]*7,ugly[3]*7,ugly[4]*7,ugly[5]*7……
# #
# # 上面这个三个数列合在一起就形成了新的、更长的丑数数列。
# #
# # 如果合在一起呢？这其实就是一个合并有序线性表的问题。


class Solution(object):
    def getKthMagicNumber(self, k):
        """
        :type k: int
        :rtype: int
        """
        p3, p5, p7 = 0, 0, 0

        res = [1]
        i = 0
        while i < k - 1:
            min_num = min(res[p3] * 3, res[p5] * 5, res[p7] * 7)
            if min_num == res[p3] * 3:
                p3 += 1
            if min_num == res[p5] * 5:
                p5 += 1
            if min_num == res[p7] * 7:
                p7 += 1
            res.append(min_num)
            i += 1

        return res[k - 1]




