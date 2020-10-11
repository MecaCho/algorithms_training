'''
416. Partition Equal Subset Sum
Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.



Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.


Constraints:

1 <= nums.length <= 200
1 <= nums[i] <= 100

416. 分割等和子集
给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

注意:

每个数组中的元素不会超过 100
数组的大小不会超过 200
示例 1:

输入: [1, 5, 11, 5]

输出: true

解释: 数组可以分割成 [1, 5, 5] 和 [11].


示例 2:

输入: [1, 2, 3, 5]

输出: false

解释: 数组不能分割成两个元素和相等的子集.
'''


class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 2:
            return False
        sum_ = sum(nums)
        if sum_ % 2 == 1:
            return False

        target = sum_ / 2

        dp = [True] + [False] * target
        for i in range(len(nums)):
            for j in range(target, nums[i] - 1, -1):
                dp[j] = dp[j] or dp[j - nums[i]]

        return dp[target]


# solutions

'''
前言
作者在这里希望读者认真阅读前言部分。

本题是经典的NP 完全问题，也就是说，如果你发现了该问题的一个多项式算法，那么恭喜你证明出了 P=NP，可以期待一下图灵奖了。

正因如此，我们不应期望该问题有多项式时间复杂度的解法。我们能想到，例如基于贪心算法的「将数组降序排序后，依次将每个元素添加至当前元素和较小的子集中」之类的方法都是错误的，可以轻松地举出反例。因此，我们必须尝试非多项式时间复杂度的算法，例如时间复杂度与元素大小相关的动态规划。

方法一：动态规划
思路与算法

这道题可以换一种表述：给定一个只包含正整数的非空数组 \textit{nums}[0]nums[0]，判断是否可以从数组中选出一些数字，使得这些数字的和等于整个数组的元素和的一半。因此这个问题可以转换成「0-10−1 背包问题」。这道题与传统的「0-10−1 背包问题」的区别在于，传统的「0-10−1 背包问题」要求选取的物品的重量之和不能超过背包的总容量，这道题则要求选取的数字的和恰好等于整个数组的元素和的一半。类似于传统的「0-10−1 背包问题」，可以使用动态规划求解。

在使用动态规划求解之前，首先需要进行以下判断。

根据数组的长度 nn 判断数组是否可以被划分。如果 n<2n<2，则不可能将数组分割成元素和相等的两个子集，因此直接返回 \text{false}false。

计算整个数组的元素和 \textit{sum}sum 以及最大元素 \textit{maxNum}maxNum。如果 \textit{sum}sum 是奇数，则不可能将数组分割成元素和相等的两个子集，因此直接返回 \text{false}false。如果 \textit{sum}sum 是偶数，则令 \textit{target}=\frac{\textit{sum}}{2}target= 
2
sum
​	
 ，需要判断是否可以从数组中选出一些数字，使得这些数字的和等于 \textit{target}target。如果 \textit{maxNum}>\textit{target}maxNum>target，则除了 \textit{maxNum}maxNum 以外的所有元素之和一定小于 \textit{target}target，因此不可能将数组分割成元素和相等的两个子集，直接返回 \text{false}false。

创建二维数组 \textit{dp}dp，包含 nn 行 \textit{target}+1target+1 列，其中 \textit{dp}[i][j]dp[i][j] 表示从数组的 [0,i][0,i] 下标范围内选取若干个正整数（可以是 00 个），是否存在一种选取方案使得被选取的正整数的和等于 jj。初始时，\textit{dp}dp 中的全部元素都是 \text{false}false。

在定义状态之后，需要考虑边界情况。以下两种情况都属于边界情况。

如果不选取任何正整数，则被选取的正整数等于 00。因此对于所有 0 \le i < n0≤i<n，都有 \textit{dp}[i][0]=\text{true}dp[i][0]=true。

当 i==0i==0 时，只有一个正整数 \textit{nums}[0]nums[0] 可以被选取，因此 \textit{dp}[0][\textit{nums}[0]]=\text{true}dp[0][nums[0]]=true。

对于 i>0i>0 且 j>0j>0 的情况，如何确定 \textit{dp}[i][j]dp[i][j] 的值？需要分别考虑以下两种情况。

如果 j \ge \textit{nums}[i]j≥nums[i]，则对于当前的数字 \textit{nums}[i]nums[i]，可以选取也可以不选取，两种情况只要有一个为 \text{true}true，就有 \textit{dp}[i][j]=\text{true}dp[i][j]=true。

如果不选取 \textit{nums}[i]nums[i]，则 \textit{dp}[i][j]=\textit{dp}[i-1][j]dp[i][j]=dp[i−1][j]；
如果选取 \textit{nums}[i]nums[i]，则 \textit{dp}[i][j]=\textit{dp}[i-1][j-\textit{nums}[i]]dp[i][j]=dp[i−1][j−nums[i]]。
如果 j < \textit{nums}[i]j<nums[i]，则在选取的数字的和等于 jj 的情况下无法选取当前的数字 \textit{nums}[i]nums[i]，因此有 \textit{dp}[i][j]=\textit{dp}[i-1][j]dp[i][j]=dp[i−1][j]。

状态转移方程如下：

\textit{dp}[i][j]=\begin{cases} \textit{dp}[i-1][j]~|~\textit{dp}[i-1][j-\textit{nums}[i]], & j \ge \textit{nums}[i] \\ \textit{dp}[i-1][j], & j < \textit{nums}[i] \end{cases}
dp[i][j]={ 
dp[i−1][j] ∣ dp[i−1][j−nums[i]],
dp[i−1][j],
​	
  
j≥nums[i]
j<nums[i]
​	
 

最终得到 \textit{dp}[n-1][\textit{target}]dp[n−1][target] 即为答案。


1 / 12

JavaC++JavaScriptGolangCPython3

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 2:
            return False
        
        total = sum(nums)
        maxNum = max(nums)
        if total & 1:
            return False
        
        target = total // 2
        if maxNum > target:
            return False
        
        dp = [[0] * (target + 1) for _ in range(n)]
        for i in range(n):
            dp[i][0] = True
        
        dp[0][nums[0]] = True
        for i in range(1, n):
            num = nums[i]
            for j in range(1, target + 1):
                if j >= num:
                    dp[i][j] = dp[i - 1][j] | dp[i - 1][j - num]
                else:
                    dp[i][j] = dp[i - 1][j]
        
        return dp[n - 1][target]
上述代码的空间复杂度是 O(n \times \textit{target})O(n×target)。但是可以发现在计算 \textit{dp}dp 的过程中，每一行的 dpdp 值都只与上一行的 dpdp 值有关，因此只需要一个一维数组即可将空间复杂度降到 O(\textit{target})O(target)。此时的转移方程为：

\textit{dp}[j]=\textit{dp}[j]\ |\ dp[j-\textit{nums}[i]]
dp[j]=dp[j] ∣ dp[j−nums[i]]

且需要注意的是第二层的循环我们需要从大到小计算，因为如果我们从小到大更新 \textit{dp}dp 值，那么在计算 \textit{dp}[j]dp[j] 值的时候，\textit{dp}[j-\textit{nums}[i]]dp[j−nums[i]] 已经是被更新过的状态，不再是上一行的 \textit{dp}dp 值。

代码

JavaC++JavaScriptGolangCPython3

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 2:
            return False
        
        total = sum(nums)
        if total % 2 != 0:
            return False
        
        target = total // 2
        dp = [True] + [False] * target
        for i, num in enumerate(nums):
            for j in range(target, num - 1, -1):
                dp[j] |= dp[j - num]
        
        return dp[target]
复杂度分析

时间复杂度：O(n \times \textit{target})O(n×target)，其中 nn 是数组的长度，\textit{target}target 是整个数组的元素和的一半。需要计算出所有的状态，每个状态在进行转移时的时间复杂度为 O(1)O(1)。

空间复杂度：O(\textit{target})O(target)，其中 \textit{target}target 是整个数组的元素和的一半。空间复杂度取决于 \textit{dp}dp 数组，在不进行空间优化的情况下，空间复杂度是 O(n \times \textit{target})O(n×target)，在进行空间优化的情况下，空间复杂度可以降到 O(\textit{target})O(target)。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/partition-equal-subset-sum/solution/fen-ge-deng-he-zi-ji-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''