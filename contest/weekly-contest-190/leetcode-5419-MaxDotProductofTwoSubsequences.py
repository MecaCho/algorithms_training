'''
5419. 两个子序列的最大点积
给你两个数组 nums1 和 nums2 。

请你返回 nums1 和 nums2 中两个长度相同的 非空 子序列的最大点积。

数组的非空子序列是通过删除原数组中某些元素（可能一个也不删除）后剩余数字组成的序列，但不能改变数字间相对顺序。比方说，[2,3,5] 是 [1,2,3,4,5] 的一个子序列而 [1,5,3] 不是。



示例 1：

输入：nums1 = [2,1,-2,5], nums2 = [3,0,-6]
输出：18
解释：从 nums1 中得到子序列 [2,-2] ，从 nums2 中得到子序列 [3,-6] 。
它们的点积为 (2*3 + (-2)*(-6)) = 18 。
示例 2：

输入：nums1 = [3,-2], nums2 = [2,-6,7]
输出：21
解释：从 nums1 中得到子序列 [3] ，从 nums2 中得到子序列 [7] 。
它们的点积为 (3*7) = 21 。
示例 3：

输入：nums1 = [-1,-1], nums2 = [1,1]
输出：-1
解释：从 nums1 中得到子序列 [-1] ，从 nums2 中得到子序列 [1] 。
它们的点积为 -1 。


提示：

1 <= nums1.length, nums2.length <= 500
-1000 <= nums1[i], nums2[i] <= 100


点积：

定义 a = [a1, a2,…, an] 和 b = [b1, b2,…, bn] 的点积为：

\mathbf{a}\cdot \mathbf{b} = \sum_{i=1}^n a_ib_i = a_1b_1 + a_2b_2 + \cdots + a_nb_n

这里的 Σ 指示总和符号。

5419. Max Dot Product of Two Subsequences
Given two arrays nums1 and nums2.

Return the maximum dot product between non-empty subsequences of nums1 and nums2 with the same length.

A subsequence of a array is a new array which is formed from the original array by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, [2,3,5] is a subsequence of [1,2,3,4,5] while [1,5,3] is not).



Example 1:

Input: nums1 = [2,1,-2,5], nums2 = [3,0,-6]
Output: 18
Explanation: Take subsequence [2,-2] from nums1 and subsequence [3,-6] from nums2.
Their dot product is (2*3 + (-2)*(-6)) = 18.
Example 2:

Input: nums1 = [3,-2], nums2 = [2,-6,7]
Output: 21
Explanation: Take subsequence [3] from nums1 and subsequence [7] from nums2.
Their dot product is (3*7) = 21.
Example 3:

Input: nums1 = [-1,-1], nums2 = [1,1]
Output: -1
Explanation: Take subsequence [-1] from nums1 and subsequence [1] from nums2.
Their dot product is -1.


Constraints:

1 <= nums1.length, nums2.length <= 500
-1000 <= nums1[i], nums2[i] <= 1000
'''


class Solution(object):
    def maxDotProduct(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        dp = [[[-float("inf"), nums1[i] * nums2[j]] for j in range(len(nums2))] for i in range(len(nums1))]
        res = -float("inf")

        for i in range(len(nums1)):
            for j in range(len(nums2)):
                max1 = max(dp[i - 1][j]) if i > 0 else -float("inf")
                max2 = max(dp[i][j - 1]) if j > 0 else -float("inf")
                dp[i][j][0] = max(max1, max2)
                if i > 0 and j > 0:
                    dp[i][j][1] = max(max(dp[i - 1][j - 1]) + nums1[i] * nums2[j], dp[i][j][1])

        res = max(res, max(dp[-1][-1]))
        return res

# tips

'''
Use dynamic programming, define DP[i][j] as the maximum dot product of two subsequences starting in the position i of nums1 and position j of nums2.
'''

# 题解

'''
注意边界条件的处理

不取nums1[i]，nums2[j]： dp[i][j][0] = max(max(dp[i - 1][j])), max(dp[i][j-1])))

取nums1[i]，nums2[j]: dp[i][j][1] = max(max(dp[i - 1][j - 1]) + nums1[i] * nums2[j], dp[i][j][1])

class Solution(object):
    def maxDotProduct(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        dp = [[[-float("inf"), nums1[i]*nums2[j]] for j in range(len(nums2))] for i in range(len(nums1))]
        res = -float("inf")
        
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                max1 = max(dp[i - 1][j]) if i > 0 else -float("inf")
                max2 = max(dp[i][j-1]) if j > 0 else -float("inf")
                dp[i][j][0] = max(max1, max2)
                if i > 0 and j > 0:
                    dp[i][j][1] = max(max(dp[i - 1][j - 1]) + nums1[i] * nums2[j], dp[i][j][1])
                    
        res = max(res, max(dp[-1][-1]))
        return res
'''

# 排名	用户名	得分	完成时间 	题目1 (3)	题目2 (4)	题目3 (5)	题目4 (6)
# 607 / 3350	qiuwenqi 	12	0:29:43	 0:08:06	 0:14:59	 0:29:43