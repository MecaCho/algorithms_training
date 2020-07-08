

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
# #
# # 定义三个index 分别指向上面三个数列，下一个丑数一定是三个 index 代表的值中最小的那个。然后相应 index++ 即可。
# #
# # 举个例子
# # 初始值 ugly[0]=1; index1=0; index2=0; index3=0
# #
# #
# # ugly[1]=Min(ugly[index1]*3,ugly[index2]*5,ugly[index3]*7)
# # =Min(1*3,1*5,1*7)
# # =3
# # 于是 index1++;
# #
# # ugly[2]=Min(ugly[index1]*3,ugly[index2]*5,ugly[index3]*7)
# # =Min(3*3,1*5,1*7)
# # =5
# # 于是 index2++;
# # 以此类推


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


# golang

'''
package CrackinfInterview

import (
	"fmt"
	"math"
)


func getKthMagicNumber(k int) int {
	aNum, bNum, cNum := 0, 0, 0
	res := []int{1}

	for i := 0; i < k; i++ {
		min_num := min(res[aNum]*3, res[bNum]*5, res[cNum]*7)

		if min_num == res[aNum]*3 {
			aNum++
		}
		if  min_num == res[bNum] * 5{
			bNum++
		}
		if min_num == res[cNum] * 7{
			cNum++
		}
		res = append(res, min_num)
	}

	return res[k-1]
}

func min(a, b, c int) int {
	return int(math.Min(float64(a), math.Min(float64(b), float64(c))))
}

func Switch() {

	a, b := 1, 2

	switch {
	case 1 == a:
		fmt.Println("1")
		fallthrough
	case 4 == b:
		fmt.Println("2")

	}
}

'''

class Solution1(object):

    ugly = sorted(2**a * 3**b * 5**c
                  for a in range(32) for b in range(20) for c in range(14))

    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """

        # return sorted(2**a * 3**b * 5**c
        #           for a in range(32) for b in range(20) for c in range(14))[n-1]
        return self.ugly[n-1]

# tips

'''
The naive approach is to call isUgly for every number until you reach the nth one. Most numbers are not ugly. Try to focus your effort on generating only the ugly ones.

An ugly number must be multiplied by either 2, 3, or 5 from a smaller ugly number.

The key is how to maintain the order of the ugly numbers. Try a similar approach of merging from three sorted lists: L1, L2, and L3.

Assume you have Uk, the kth ugly number. Then Uk+1 must be Min(L1 * 2, L2 * 3, L3 * 5).
'''

# solutions

# I love this problem. Came up with a linear time solution almost 13 years ago and now I still correctly remembered
# that it was problem 136 at the now defunct acm.uva.es :-)
#
# Python ... Simple Precompute ... 64 ms
#
# It's fastest to precompute and store all possibilities for lookup, and it's simplest to just generate them out of
# order and then sort them.
#
# class Solution:
#     ugly = sorted(2**a * 3**b * 5**c
#                   for a in range(32) for b in range(20) for c in range(14))
#     def nthUglyNumber(self, n):
#         return self.ugly[n-1]
# Python ... O(n), generate first n in order ... 308 ms
#
# My version of epsilon0's solution. It's nicer than my own old one.
#
# This generates the first n ugly numbers, in order from smallest to largest, in O(n) time. For each prime 2,
# 3 and 5, have an index to the next number that can be multiplied with the prime to produce a new ugly number.
# Update the three indexes and then add the smallest of the three candidate ugly numbers.
#
# def nthUglyNumber(self, n):
#     ugly = [1]
#     i2 = i3 = i5 = 0
#     while len(ugly) < n:
#         while ugly[i2] * 2 <= ugly[-1]: i2 += 1
#         while ugly[i3] * 3 <= ugly[-1]: i3 += 1
#         while ugly[i5] * 5 <= ugly[-1]: i5 += 1
#         ugly.append(min(ugly[i2] * 2, ugly[i3] * 3, ugly[i5] * 5))
#     return ugly[-1]
# Python ... O(n), generate first n in order with heapq.merge ... 416 ms
#
# I like using heapq.merge.
#
# def nthUglyNumber(self, n):
#     q2, q3, q5 = [2], [3], [5]
#     ugly = 1
#     for u in heapq.merge(q2, q3, q5):
#         if n == 1:
#             return ugly
#         if u > ugly:
#             ugly = u
#             n -= 1
#             q2 += 2 * u,
#             q3 += 3 * u,
#             q5 += 5 * u,
# Works, but might not be totally safe, both because I extend lists while iterating over them and because at the
# start, q2 becomes empty for a moment, which I think allows heapq.merge to drop it (at least in CPython it just
# doesn't, as it first yields the value before trying to get the next one from that list, and when it continues,
# the list isn't empty anymore).
#
# C++ ... O(n), generate first n in order ... 12 ms
#
# C++ version of the second Python solution, though adding extra variables for the three candidates to prevent
# re-multiplication.
#
# int nthUglyNumber(int n) {
#     vector<int> ugly(n, 1);
#     int c2 = 2, c3 = 3, c5 = 5;
#     int i2 = 0, i3 = 0, i5 = 0;
#     for (int i=1; i<n; ++i) {
#         int last = ugly[i] = min(c2, min(c3, c5));
#         while (c2 <= last) c2 = 2 * ugly[++i2];
#         while (c3 <= last) c3 = 3 * ugly[++i3];
#         while (c5 <= last) c5 = 5 * ugly[++i5];
#     }
#     return ugly[n-1];
# }
# C++ ... O(n), generate on demand and remember ... 4 ms
#
# Same as the previous, but I keep everything in static variables and only compute more when needed. It's faster,
# and I think pretty neat.
#
# int nthUglyNumber(int n) {
#     static vector<int> ugly {1};
#     static int last(1);
#     static int c2(2), c3(3), c5(5);
#     static int i2(0), i3(0), i5(0);
#     while (ugly.size() < n) {
#         while (c2 <= last) c2 = 2 * ugly[++i2];
#         while (c3 <= last) c3 = 3 * ugly[++i3];
#         while (c5 <= last) c5 = 5 * ugly[++i5];
#         ugly.push_back(last = min(c2, min(c3, c5)));
#     }
#     return ugly[n-1];
# }
# C++ ... Simple Precompute ... 4 ms
#
# Precompute all possibilities in easy order and sort them.
#
# int nthUglyNumber(int n) {
#     static vector<int> ugly;
#     long long a, b, c, m = INT_MAX;
#     if (ugly.empty()) {
#         for (a=1; a<=m; a*=2)
#             for (b=a; b<=m; b*=3)
#                 for (c=b; c<=m; c*=5)
#                     ugly.push_back(c);
#         sort(begin(ugly), end(ugly));
#     }
#     return ugly[n-1];
# }
# My own old one
#
# Python version of my own O(n) C++ solution from almost 13 years ago. Good old times...
# Maybe I'll try to improve it, but mainly I wanted to see how a pretty much direct translation would look.
#
# def nthUglyNumber(self, n):
#     factor = 2, 3, 5
#     lists = [collections.deque([1]) for _ in range(3)]
#     for _ in range(n - 1):
#         next = [lists[i][0] * factor[i] for i in range(3)]
#         winner = min(range(3), key=lambda j: next[j])
#         for i in range(winner, 3):
#             lists[i] += next[winner],
#         lists[winner].popleft()
#     return lists[2][-1]
