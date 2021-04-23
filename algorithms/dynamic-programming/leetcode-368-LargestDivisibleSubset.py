# encoding=utf8


'''
368. Largest Divisible Subset
Given a set of distinct positive integers nums, return the largest subset answer such that every pair (answer[i], answer[j]) of elements in this subset satisfies:

answer[i] % answer[j] == 0, or
answer[j] % answer[i] == 0
If there are multiple solutions, return any of them.

 

Example 1:

Input: nums = [1,2,3]
Output: [1,2]
Explanation: [1,3] is also accepted.
Example 2:

Input: nums = [1,2,4,8]
Output: [1,2,4,8]
 

Constraints:

1 <= nums.length <= 1000
1 <= nums[i] <= 2 * 109
All the integers in nums are unique.


368. 最大整除子集
给你一个由 无重复 正整数组成的集合 nums ，请你找出并返回其中最大的整除子集 answer ，子集中每一元素对 (answer[i], answer[j]) 都应当满足：
answer[i] % answer[j] == 0 ，或
answer[j] % answer[i] == 0
如果存在多个有效解子集，返回其中任何一个均可。

 

示例 1：

输入：nums = [1,2,3]
输出：[1,2]
解释：[1,3] 也会被视为正确答案。
示例 2：

输入：nums = [1,2,4,8]
输出：[1,2,4,8]
 

提示：

1 <= nums.length <= 1000
1 <= nums[i] <= 2 * 109
nums 中的所有整数 互不相同
'''



class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        f = [[x] for x in nums]
        for j in range(len(nums)):
            for i in range(j):
                if nums[j]%nums[i]==0 and len(f[i])+1 > len(f[j]):
                    f[j] = f[i] + [nums[j]]
        return max(f, key=len)



# solutions


'''
前言
首先需要理解什么叫「整除子集」。根据题目的描述，如果一个所有元素互不相同的集合中的任意元素存在整除关系，就称为整除子集。为了得到「最大整除子集」，我们需要考虑如何从一个小的整除子集扩充成为更大的整除子集。

根据整除关系具有传递性，即如果 a\big|ba 
∣
∣
∣
​	
 b，并且 b\big|cb 
∣
∣
∣
​	
 c，那么 a\big|ca 
∣
∣
∣
​	
 c，可知：

如果整数 aa 是整除子集 S_1S 
1
​	
  的最小整数 bb 的约数（即 a\big|ba 
∣
∣
∣
​	
 b），那么可以将 aa 添加到 S_1S 
1
​	
  中得到一个更大的整除子集；

如果整数 cc 是整除子集 S_2S 
2
​	
  的最大整数 dd 的倍数（即 d\big|cd 
∣
∣
∣
​	
 c），那么可以将 cc 添加到 S_2S 
2
​	
  中得到一个更大的整除子集。

这两点揭示了当前问题状态转移的特点，因此可以使用动态规划的方法求解。题目只要求我们得到多个目标子集的其中一个，根据求解动态规划问题的经验，我们需要将子集的大小定义为状态，然后根据结果倒推得到一个目标子集。事实上，当前问题和使用动态规划解决的经典问题「300. 最长递增子序列」有相似之处。

方法一：动态规划
根据前言的分析，我们需要将输入数组 \textit{nums}nums 按照升序排序，以便获得一个子集的最小整数或者最大整数。又根据动态规划的「无后效性」状态设计准则，我们需要将状态定义成「某个元素必须选择」。

状态定义：\textit{dp}[i]dp[i] 表示在输入数组 \textit{nums}nums 升序排列的前提下，以 \textit{nums}[i]nums[i] 为最大整数的「整除子集」的大小（在这种定义下 \textit{nums}[i]nums[i] 必须被选择）。

状态转移方程：枚举 j = 0 \ldots i-1j=0…i−1 的所有整数 \textit{nums}[j]nums[j]，如果 \textit{nums}[j]nums[j] 能整除 \textit{nums}[i]nums[i]，说明 \textit{nums}[i]nums[i] 可以扩充在以 \textit{nums}[j]nums[j] 为最大整数的整除子集里成为一个更大的整除子集。

初始化：由于 \textit{nums}[i]nums[i] 必须被选择，因此对于任意 i = 0 \ldots n-1i=0…n−1，初始的时候 \textit{dp}[i] = 1dp[i]=1，这里 nn 是输入数组的长度。

输出：由于最大整除子集不一定包含 \textit{nums}nums 中最大的整数，所以我们需要枚举所有的 \textit{dp}[i]dp[i]，选出最大整除子集的大小 \textit{maxSize}maxSize，以及该最大子集中的最大整数 \textit{maxVal}maxVal。按照如下方式倒推获得一个目标子集：

倒序遍历数组 \textit{dp}dp，直到找到 \textit{dp}[i] = \textit{maxSize}dp[i]=maxSize 为止，把此时对应的 \textit{nums}[i]nums[i] 加入结果集，此时 \textit{maxVal} = \textit{nums}[i]maxVal=nums[i]；

然后将 \textit{maxSize}maxSize 的值减 11，继续倒序遍历找到 \textit{dp}[i] = \textit{maxSize}dp[i]=maxSize，且 \textit{nums}[i]nums[i] 能整除 \textit{maxVal}maxVal 的 ii 为止，将此时的 \textit{nums}[i]nums[i] 加入结果集，\textit{maxVal}maxVal 更新为此时的 num[i]num[i]；

重复上述操作，直到 \textit{maxSize}maxSize 的值变成 00，此时的结果集即为一个目标子集。

下面用一个例子说明如何得到最大整除子集。假设输入数组为 [2,4,7,8,9,12,16,18][2,4,7,8,9,12,16,18]（已经有序），得到的动态规划表格如下：

\textit{nums}nums	22	44	77	88	99	1212	1616	2020
\textit{dp}dp	11	22	11	33	11	33	44	33
得到最大整除子集的做法如下：

根据 \textit{dp}dp 的计算结果，\textit{maxSize}=4maxSize=4，\textit{maxVal}=16maxVal=16，因此大小为 44 的最大整除子集包含的最大整数为 1616；

然后查找大小为 33 的最大整除子集，我们看到 88 和 1212 对应的状态值都是 33，最大整除子集一定包含 88，这是因为 8 \big| 168 
∣
∣
∣
​	
 16；

然后查找大小为 22 的最大整除子集，我们看到 44 对应的状态值是 22，最大整除子集一定包含 44；

然后查找大小为 11 的最大整除子集，我们看到 22 对应的状态值是 11，最大整除子集一定包含 22。

通过这样的方式，我们就找到了满足条件的某个最大整除子集 [16,8,4,2][16,8,4,2]。

代码

JavaJavaScriptGolangC++C

func largestDivisibleSubset(nums []int) (res []int) {
    sort.Ints(nums)

    // 第 1 步：动态规划找出最大子集的个数、最大子集中的最大整数
    n := len(nums)
    dp := make([]int, n)
    for i := range dp {
        dp[i] = 1
    }
    maxSize, maxVal := 1, 1
    for i := 1; i < n; i++ {
        for j, v := range nums[:i] {
            if nums[i]%v == 0 && dp[j]+1 > dp[i] {
                dp[i] = dp[j] + 1
            }
        }
        if dp[i] > maxSize {
            maxSize, maxVal = dp[i], nums[i]
        }
    }

    if maxSize == 1 {
        return []int{nums[0]}
    }

    // 第 2 步：倒推获得最大子集
    for i := n - 1; i >= 0 && maxSize > 0; i-- {
        if dp[i] == maxSize && maxVal%nums[i] == 0 {
            res = append(res, nums[i])
            maxVal = nums[i]
            maxSize--
        }
    }
    return
}
复杂度分析

时间复杂度：O(n^2)O(n 
2
 )，其中 nn 为输入数组的长度。对数组 \textit{nums}nums 排序的时间复杂度为 O(n \log n)O(nlogn)，计算数组 \textit{dp}dp 元素的时间复杂度为 O(n^2)O(n 
2
 )，倒序遍历得到一个目标子集，时间复杂度为 O(n)O(n)。

空间复杂度：O(n)O(n)，其中 nn 为输入数组的长度。需要创建长度为 nn 的数组 \textit{dp}dp。

'''

