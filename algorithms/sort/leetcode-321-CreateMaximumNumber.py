'''
321. Create Maximum Number
Given two arrays of length m and n with digits 0-9 representing two numbers. Create the maximum number of length k <= m + n from digits of the two. The relative order of the digits from the same array must be preserved. Return an array of the k digits.

Note: You should try to optimize your time and space complexity.

Example 1:

Input:
nums1 = [3, 4, 6, 5]
nums2 = [9, 1, 2, 5, 8, 3]
k = 5
Output:
[9, 8, 6, 5, 3]
Example 2:

Input:
nums1 = [6, 7]
nums2 = [6, 0, 4]
k = 5
Output:
[6, 7, 6, 0, 4]
Example 3:

Input:
nums1 = [3, 9]
nums2 = [8, 9]
k = 3
Output:
[9, 8, 9]


321. 拼接最大数
给定长度分别为 m 和 n 的两个数组，其元素由 0-9 构成，表示两个自然数各位上的数字。现在从这两个数组中选出 k (k <= m + n) 个数字拼接成一个新的数，要求从同一个数组中取出的数字保持其在原数组中的相对顺序。

求满足该条件的最大数。结果返回一个表示该最大数的长度为 k 的数组。

说明: 请尽可能地优化你算法的时间和空间复杂度。

示例 1:

输入:
nums1 = [3, 4, 6, 5]
nums2 = [9, 1, 2, 5, 8, 3]
k = 5
输出:
[9, 8, 6, 5, 3]
示例 2:

输入:
nums1 = [6, 7]
nums2 = [6, 0, 4]
k = 5
输出:
[6, 7, 6, 0, 4]
示例 3:

输入:
nums1 = [3, 9]
nums2 = [8, 9]
k = 3
输出:
[9, 8, 9]
'''


import collections
class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """

        def pick(k, nums):
            drop = len(nums) - k  # 扔掉drop个数字
            st = []
            for i in nums:
                while drop and st and st[-1] < i:
                    st.pop()
                    drop -= 1
                st.append(i)
            return collections.deque(st[:k])  # 有可能没扔够，确保一下只返回k个数字，这里用了可以popleft的deque

        def merge(nums1, nums2):
            res = []
            while nums1 and nums2:  # 一直popleft直到某个数组取空为止
                res.append(max(nums1, nums2).popleft())
            res.extend(nums1 or nums2)  # 把还有剩的数组并进res里
            return res

        l1, l2 = len(nums1), len(nums2)
        # 穷举所有可能的情况，取出最大值
        return max(merge(pick(i, nums1), pick(k - i, nums2)) for i in range(k + 1) if i <= l1 and k - i <= l2)

