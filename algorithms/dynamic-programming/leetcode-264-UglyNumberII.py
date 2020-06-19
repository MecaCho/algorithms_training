

'''
264. 丑数 II
编写一个程序，找出第 n 个丑数。

丑数就是只包含质因数 2, 3, 5 的正整数。

示例:

输入: n = 10
输出: 12
解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。
说明:

1 是丑数。
n 不超过1690。

264. Ugly Number II
Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.

Example:

Input: n = 10
Output: 12
Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
Note:

1 is typically treated as an ugly number.
n does not exceed 1690.


'''

# tips

'''
k[1] = min( k[0]x2, k[0]x3, k[0]x5). The answer is k[0]x2. So we move 2's pointer to 1. Then we test:

k[2] = min( k[1]x2, k[0]x3, k[0]x5). And so on. Be careful about the cases such as 6, in which we need to forward both pointers of 2 and 3.
'''


class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = [1]
        i2 ,i3 ,i5 = 0 ,0 ,0
        for i in range(1691):

            num = min(res[i2 ] *2, res[i3 ] *3, res[i5 ] *5)

            if len(res) == n:
                break

            if num == res[i2 ] *2:
                i2 += 1
            if num == res[i3 ] *3:
                i3 += 1
            if num == res[i5 ] *5:
                i5 += 1
            # print(num, i2, i3, i5,res)
            res.append(num)
        # print(res)
        return res[-1]


class Solution_(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        # res = [1]
        # i2,i3,i5 = 0,0,0
        # for i in range(1691):

        #     num = min(res[i2]*2, res[i3]*3, res[i5]*5)

        #     if len(res) == n:
        #         break

        #     if num == res[i2]*2:
        #         i2 += 1
        #     if num == res[i3]*3:
        #         i3 += 1
        #     if num == res[i5]*5:
        #         i5 += 1
        #     # print(num, i2, i3, i5,res)
        #     res.append(num)
        # # print(res)
        # return res[-1]

        i2, i3, i5 = 0, 0, 0
        ugly_nums = [1]
        for i in range(n - 1):
            print(i2, i3, i5)

            min_num = min(ugly_nums[i2] * 2, ugly_nums[i3] * 3, ugly_nums[i5] * 5)

            if min_num == ugly_nums[i2] * 2:
                i2 += 1
            if min_num == ugly_nums[i3] * 3:
                i3 += 1
            if min_num == ugly_nums[i5] * 5:
                i5 += 1

            ugly_nums.append(min_num)
        # print(ugly_nums, len(ugly_nums))

        return ugly_nums[-1]


# tips

'''
The naive approach is to call isUgly for every number until you reach the nth one. Most numbers are not ugly. Try to focus your effort on generating only the ugly ones.

An ugly number must be multiplied by either 2, 3, or 5 from a smaller ugly number.

The key is how to maintain the order of the ugly numbers. Try a similar approach of merging from three sorted lists: L1, L2, and L3.

Assume you have Uk, the kth ugly number. Then Uk+1 must be Min(L1 * 2, L2 * 3, L3 * 5).
'''