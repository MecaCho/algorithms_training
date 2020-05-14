'''
560. 和为K的子数组
给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。

示例 1 :

输入:nums = [1,1,1], k = 2
输出: 2 , [1,1] 与 [1,1] 为两种不同的情况。
说明 :

数组的长度为 [1, 20,000]。
数组中元素的范围是 [-1000, 1000] ，且整数 k 的范围是 [-1e7, 1e7]。

560. Subarray Sum Equals K
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:

Input:nums = [1,1,1], k = 2
Output: 2


Constraints:

The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
'''

import collections

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # count = 0
        # for i in range(len(nums)):
        #     tmp_sum = 0
        #     for j in range(i, len(nums)):
        #         tmp_sum += nums[j]
        #         if tmp_sum == k:
        #             count += 1
        # return count

        res = 0
        hash_map = collections.defaultdict(int)
        pre = 0
        hash_map[0] = 1

        for i in range(len(nums)):
            pre += nums[i]
            if hash_map.get(pre-k):
                res += hash_map[pre-k]
            hash_map[pre] += 1

        return res


'''
方法一：枚举
思路和算法

考虑以 ii 结尾和为 kk 的连续子数组个数，我们需要统计符合条件的下标 jj 的个数，其中 0\leq j\leq i0≤j≤i 且 [j..i][j..i] 这个子数组的和恰好为 kk 。

我们可以枚举 [0..i][0..i] 里所有的下标 jj 来判断是否符合条件，可能有读者会认为假定我们确定了子数组的开头和结尾，还需要 O(n)O(n) 的时间复杂度遍历子数组来求和，那样复杂度就将达到 O(n^3)O(n 
3
 ) 从而无法通过所有测试用例。但是如果我们知道 [j,i][j,i] 子数组的和，就能 O(1)O(1) 推出 [j-1,i][j−1,i] 的和，因此这部分的遍历求和是不需要的，我们在枚举下标 jj 的时候已经能 O(1)O(1) 求出 [j,i][j,i] 的子数组之和。

JavaC++JavaScriptGolang
func subarraySum(nums []int, k int) int {
    count := 0
    for start := 0; start < len(nums); start++ {
        sum := 0
        for end := start; end >= 0; end-- {
            sum += nums[end]
            if sum == k {
                count++
            }
        }
    }
    return count
}
复杂度分析

时间复杂度：O(n^2)O(n 
2
 )，其中 nn 为数组的长度。枚举子数组开头和结尾需要 O(n^2)O(n 
2
 ) 的时间，其中求和需要 O(1)O(1) 的时间复杂度，因此总时间复杂度为 O(n^2)O(n 
2
 )。

空间复杂度：O(1)O(1)。只需要常数空间存放若干变量。

方法二：前缀和 + 哈希表优化
思路和算法

我们可以基于方法一利用数据结构进行进一步的优化，我们知道方法一的瓶颈在于对每个 ii，我们需要枚举所有的 jj 来判断是否符合条件，这一步是否可以优化呢？答案是可以的。

我们定义 \textit{pre}[i]pre[i] 为 [0..i][0..i] 里所有数的和，则 \textit{pre}[i]pre[i] 可以由 \textit{pre}[i-1]pre[i−1] 递推而来，即：

\textit{pre}[i]=\textit{pre}[i-1]+\textit{nums}[i]
pre[i]=pre[i−1]+nums[i]

那么「[j..i][j..i] 这个子数组和为 kk 」这个条件我们可以转化为

\textit{pre}[i]-\textit{pre}[j-1]==k
pre[i]−pre[j−1]==k

简单移项可得符合条件的下标 jj 需要满足

\textit{pre}[j-1] == \textit{pre}[i] - k
pre[j−1]==pre[i]−k

所以我们考虑以 ii 结尾的和为 kk 的连续子数组个数时只要统计有多少个前缀和为 \textit{pre}[i]-kpre[i]−k 的 \textit{pre}[j]pre[j] 即可。我们建立哈希表 \textit{mp}mp，以和为键，出现次数为对应的值，记录 \textit{pre}[i]pre[i] 出现的次数，从左往右边更新 \textit{mp}mp 边计算答案，那么以 ii 结尾的答案 \textit{mp}[\textit{pre}[i]-k]mp[pre[i]−k] 即可在 O(1)O(1) 时间内得到。最后的答案即为所有下标结尾的和为 kk 的子数组个数之和。

需要注意的是，从左往右边更新边计算的时候已经保证了\textit{mp}[\textit{pre}[i]-k]mp[pre[i]−k] 里记录的 \textit{pre}[j]pre[j] 的下标范围是 0\leq j\leq i0≤j≤i 。同时，由于\textit{pre}[i]pre[i] 的计算只与前一项的答案有关，因此我们可以不用建立 \textit{pre}pre 数组，直接用 \textit{pre}pre 变量来记录 pre[i-1]pre[i−1] 的答案即可。

下面的动画描述了这一过程：


1 / 9

JavaC++JavaScriptGolang
func subarraySum(nums []int, k int) int {
    count, pre := 0, 0
    m := map[int]int{}
    m[0] = 1
    for i := 0; i < len(nums); i++ {
        pre += nums[i]
        if _, ok := m[pre - k]; ok {
            count += m[pre - k]
        }
        m[pre] += 1
    }
    return count
}
复杂度分析

时间复杂度：O(n)O(n)，其中 nn 为数组的长度。我们遍历数组的时间复杂度为 O(n)O(n)，中间利用哈希表查询删除的复杂度均为 O(1)O(1)，因此总时间复杂度为 O(n)O(n)。

空间复杂度：O(n)O(n)，其中 nn 为数组的长度。哈希表在最坏情况下可能有 nn 个不同的键值，因此需要 O(n)O(n) 的空间复杂度。

'''


'''
Will Brute force work here? Try to optimize it.
Can we optimize it by using some extra space?
What about storing sum frequencies in a hash table? Will it be useful?
sum(i,j)=sum(0,j)-sum(0,i), where sum(i,j) represents the sum of all the elements from index i to j-1. Can we use this property to optimize it.
'''