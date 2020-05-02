

'''
1099. 小于 K 的两数之和
给你一个整数数组 A 和一个整数 K，请在该数组中找出两个元素，使它们的和小于 K 但尽可能地接近 K，返回这两个元素的和。

如不存在这样的两个元素，请返回 -1。



示例 1：

输入：A = [34,23,1,24,75,33,54,8], K = 60
输出：58
解释：
34 和 24 相加得到 58，58 小于 60，满足题意。
示例 2：

输入：A = [10,20,30], K = 15
输出：-1
解释：
我们无法找到和小于 15 的两个元素。


提示：

1 <= A.length <= 100
1 <= A[i] <= 1000
1 <= K <= 2000


1099. Two Sum Less Than K
Given an array A of integers and integer K, return the maximum S such that there exists i < j with A[i] + A[j] = S and S < K. If no i, j exist satisfying this equation, return -1.



Example 1:

Input: A = [34,23,1,24,75,33,54,8], K = 60
Output: 58
Explanation:
We can use 34 and 24 to sum 58 which is less than 60.
Example 2:

Input: A = [10,20,30], K = 15
Output: -1
Explanation:
In this case it's not possible to get a pair sum less that 15.


Note:

1 <= A.length <= 100
1 <= A[i] <= 1000
1 <= K <= 2000
'''




class Solution(object):
    def twoSumLessThanK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        A = sorted(A)
        i = 0
        j = len(A) - 1
        res = -1
        while i < j:
            # mid = (i + j)/2
            sum_ = A[i] + A[j]
            # if sum_ == K:
            #     return K
            if sum_ >= K:
                j -= 1
            else:
                res = max(res, sum_)
                i += 1
        return res
