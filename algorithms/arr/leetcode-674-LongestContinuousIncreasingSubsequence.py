# encoding=utf8

'''
674. 最长连续递增序列
给定一个未经排序的整数数组，找到最长且连续的的递增序列。

示例 1:

输入: [1,3,5,4,7]
输出: 3
解释: 最长连续递增序列是 [1,3,5], 长度为3。
尽管 [1,3,5,7] 也是升序的子序列, 但它不是连续的，因为5和7在原数组里被4隔开。 
示例 2:

输入: [2,2,2,2,2]
输出: 1
解释: 最长连续递增序列是 [2], 长度为1。
注意：数组长度不会超过10000。

674. Longest Continuous Increasing Subsequence
Given an unsorted array of integers, find the length of longest continuous increasing subsequence (subarray).

Example 1:
Input: [1,3,5,4,7]
Output: 3
Explanation: The longest continuous increasing subsequence is [1,3,5], its length is 3. 
Even though [1,3,5,7] is also an increasing subsequence, it's not a continuous one where 5 and 7 are separated by 4. 
Example 2:
Input: [2,2,2,2,2]
Output: 1
Explanation: The longest continuous increasing subsequence is [2], its length is 1. 
Note: Length of the array will not exceed 10,000.

'''


class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        dp = [1] * length
        for i in range(1, length):
            if nums[i] > nums[i-1]:
                dp[i] = max(dp[i-1] + 1, dp[i])
        return max(dp) if dp else 0



class Solution20210124(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        max_ = 1
        cur = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                cur += 1
            else:
                cur = 1
            if cur > max_:
                max_ = cur

        return max_



# solutions

'''
方法一：贪心
对于下标范围 [l,r][l,r] 的连续子序列，如果对任意 l \le i<rl≤i<r 都满足 \textit{nums}[i]<\textit{nums}[i+1]nums[i]<nums[i+1]，则该连续子序列是递增序列。

假设数组 \textit{nums}nums 的长度是 nn，对于 0<l \le r<n-10<l≤r<n−1，如果下标范围 [l,r][l,r] 的连续子序列是递增序列，则考虑 \textit{nums}[l-1]nums[l−1] 和 \textit{nums}[r+1]nums[r+1]。

如果 \textit{nums}[l-1]<\textit{nums}[l]nums[l−1]<nums[l]，则将 \textit{nums}[l-1]nums[l−1] 加到 \textit{nums}[l]nums[l] 的前面，可以得到更长的连续递增序列.

如果 \textit{nums}[r+1]>\textit{nums}[r]nums[r+1]>nums[r]，则将 \textit{nums}[r+1]nums[r+1] 加到 \textit{nums}[r]nums[r] 的后面，可以得到更长的连续递增序列。

基于上述分析可知，为了得到最长连续递增序列，可以使用贪心的策略得到尽可能长的连续递增序列。做法是使用记录当前连续递增序列的开始下标和结束下标，遍历数组的过程中每次比较相邻元素，根据相邻元素的大小关系决定是否需要更新连续递增序列的开始下标。

具体而言，令 \textit{start}start 表示连续递增序列的开始下标，初始时 \textit{start}=0start=0，然后遍历数组 \textit{nums}nums，进行如下操作。

如果下标 i>0i>0 且 \textit{nums}[i] \le \textit{nums}[i-1]nums[i]≤nums[i−1]，则说明当前元素小于或等于上一个元素，因此 \textit{nums}[i-1]nums[i−1] 和 \textit{nums}[i]nums[i] 不可能属于同一个连续递增序列，必须从下标 ii 处开始一个新的连续递增序列，因此令 \textit{start}=istart=i。如果下标 i=0i=0 或 \textit{nums}[i]>\textit{nums}[i-1]nums[i]>nums[i−1]，则不更新 \textit{start}start 的值。

此时下标范围 [\textit{start},i][start,i] 的连续子序列是递增序列，其长度为 i-\textit{start}+1i−start+1，使用当前连续递增序列的长度更新最长连续递增序列的长度。

遍历结束之后，即可得到整个数组的最长连续递增序列的长度。

JavaJavaScriptGolangC++CPython3

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        start = 0

        for i in range(n):
            if i > 0 and nums[i] <= nums[i - 1]:
                start = i
            ans = max(ans, i - start + 1)
        
        return ans
复杂度分析

时间复杂度：O(n)O(n)，其中 nn 是数组 \textit{nums}nums 的长度。需要遍历数组一次。

空间复杂度：O(1)O(1)。额外使用的空间为常数。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/longest-continuous-increasing-subsequence/solution/zui-chang-lian-xu-di-zeng-xu-lie-by-leet-dmb8/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''

