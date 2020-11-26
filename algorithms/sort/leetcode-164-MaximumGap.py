'''
164. Maximum Gap
Given an unsorted array, find the maximum difference between the successive elements in its sorted form.

Return 0 if the array contains less than 2 elements.

Example 1:

Input: [3,6,9,1]
Output: 3
Explanation: The sorted form of the array is [1,3,6,9], either
             (3,6) or (6,9) has the maximum difference 3.
Example 2:

Input: [10]
Output: 0
Explanation: The array contains less than 2 elements, therefore return 0.
Note:

You may assume all elements in the array are non-negative integers and fit in the 32-bit signed integer range.
Try to solve it in linear time/space.

164. 最大间距
给定一个无序的数组，找出数组在排序之后，相邻元素之间最大的差值。

如果数组元素个数小于 2，则返回 0。

示例 1:

输入: [3,6,9,1]
输出: 3
解释: 排序后的数组是 [1,3,6,9], 其中相邻元素 (3,6) 和 (6,9) 之间都存在最大差值 3。
示例 2:

输入: [10]
输出: 0
解释: 数组元素个数小于 2，因此返回 0。
说明:

你可以假设数组中所有元素都是非负整数，且数值在 32 位有符号整数范围内。
请尝试在线性时间复杂度和空间复杂度的条件下解决此问题。
'''


class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0

        nums.sort()
        res = 0
        for i in range(1, len(nums)):
            t = nums[i] - nums[i-1]
            res = max(res, t)

        return res


# solution

'''
方法一：基数排序
思路与算法

一种最简单的思路是将数组排序后再找出最大间距，但传统的基于比较的排序算法（快速排序、归并排序等）均需要 O(N\log N)O(NlogN) 的时间复杂度。我们必须使用其他的排序算法。例如，基数排序可以在 O(N)O(N) 的时间内完成整数之间的排序。

代码

C++JavaJavaScriptGolangC

func maximumGap(nums []int) (ans int) {
    n := len(nums)
    if n < 2 {
        return
    }

    buf := make([]int, n)
    maxVal := max(nums...)
    for exp := 1; exp <= maxVal; exp *= 10 {
        cnt := [10]int{}
        for _, v := range nums {
            digit := v / exp % 10
            cnt[digit]++
        }
        for i := 1; i < 10; i++ {
            cnt[i] += cnt[i-1]
        }
        for i := n - 1; i >= 0; i-- {
            digit := nums[i] / exp % 10
            buf[cnt[digit]-1] = nums[i]
            cnt[digit]--
        }
        copy(nums, buf)
    }

    for i := 1; i < n; i++ {
        ans = max(ans, nums[i]-nums[i-1])
    }
    return
}

func max(a ...int) int {
    res := a[0]
    for _, v := range a[1:] {
        if v > res {
            res = v
        }
    }
    return res
}
复杂度分析

时间复杂度：O(N)O(N)，其中 NN 是数组的长度。

空间复杂度：O(N)O(N)，其中 NN 是数组的长度。

方法二：基于桶的算法
思路与算法

设长度为 NN 的数组中最大值为 \textit{max,min}max,min，则不难发现相邻数字的最大间距不会小于 \lceil (\textit{max}-\textit{min}) / (N-1) \rceil⌈(max−min)/(N−1)⌉。

为了说明这一点，我们使用反证法：假设相邻数字的间距都小于 \lceil (\textit{max}-\textit{min}) / (N-1) \rceil⌈(max−min)/(N−1)⌉，并记数组排序后从小到大的数字依次为 A_1, A_2, ..., A_NA 
1
​	
 ,A 
2
​	
 ,...,A 
N
​	
 ，则有

\begin{aligned} A_N - A_1&=(A_N - A_{N-1})+(A_{N-1}-A_{N-2})+ ... + (A_2 - A_1) \\ &< \lceil (\textit{max}-\textit{min}) / (N-1) \rceil + \lceil (\textit{max}-\textit{min}) / (N-1) \rceil + ... + \lceil (\textit{max}-\textit{min}) / (N-1) \rceil \\ &< (N-1) \cdot \lceil (\textit{max}-\textit{min}) / (N-1) \rceil= \textit{max}-\textit{min} \end{aligned}
A 
N
​	
 −A 
1
​	
 
​	
  
=(A 
N
​	
 −A 
N−1
​	
 )+(A 
N−1
​	
 −A 
N−2
​	
 )+...+(A 
2
​	
 −A 
1
​	
 )
<⌈(max−min)/(N−1)⌉+⌈(max−min)/(N−1)⌉+...+⌈(max−min)/(N−1)⌉
<(N−1)⋅⌈(max−min)/(N−1)⌉=max−min
​	
 

但根据 A_1, A_NA 
1
​	
 ,A 
N
​	
  的定义，一定有 A_1=\textit{min}A 
1
​	
 =min，且 A_N=\textit{max}A 
N
​	
 =max，故上式会导出矛盾。

因此，我们可以选取整数 d = \lfloor (\textit{max}-\textit{min}) / (N-1) \rfloor < \lceil (\textit{max}-\textit{min}) / (N-1) \rceild=⌊(max−min)/(N−1)⌋<⌈(max−min)/(N−1)⌉。随后，我们将整个区间划分为若干个大小为 dd 的桶，并找出每个整数所在的桶。根据前面的结论，能够知道，元素之间的最大间距一定不会出现在某个桶的内部，而一定会出现在不同桶当中。

因此，在找出每个元素所在的桶之后，我们可以维护每个桶内元素的最大值与最小值。随后，只需从前到后不断比较相邻的桶，用后一个桶的最小值与前一个桶的最大值之差作为两个桶的间距，最终就能得到所求的答案。

代码

C++JavaJavaScriptGolangC

type pair struct{ min, max int }

func maximumGap(nums []int) (ans int) {
    n := len(nums)
    if n < 2 {
        return
    }

    minVal := min(nums...)
    maxVal := max(nums...)
    d := max(1, (maxVal-minVal)/(n-1))
    bucketSize := (maxVal-minVal)/d + 1

    // 存储 (桶内最小值，桶内最大值) 对，(-1, -1) 表示该桶是空的
    buckets := make([]pair, bucketSize)
    for i := range buckets {
        buckets[i] = pair{-1, -1}
    }
    for _, v := range nums {
        bid := (v - minVal) / d
        if buckets[bid].min == -1 {
            buckets[bid].min = v
            buckets[bid].max = v
        } else {
            buckets[bid].min = min(buckets[bid].min, v)
            buckets[bid].max = max(buckets[bid].max, v)
        }
    }

    prev := -1
    for i, b := range buckets {
        if b.min == -1 {
            continue
        }
        if prev != -1 {
            ans = max(ans, b.min-buckets[prev].max)
        }
        prev = i
    }
    return
}

func min(a ...int) int {
    res := a[0]
    for _, v := range a[1:] {
        if v < res {
            res = v
        }
    }
    return res
}

func max(a ...int) int {
    res := a[0]
    for _, v := range a[1:] {
        if v > res {
            res = v
        }
    }
    return res
}
复杂度分析

时间复杂度：O(N)O(N)，其中 NN 是数组的长度。注意到桶的数量为 (\textit{max}-\textit{min})/d \approx N - 1 =O(N)(max−min)/d≈N−1=O(N)。

空间复杂度：O(N)O(N)，其中 NN 是数组的长度。我们开辟的空间大小取决于桶的数量。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/maximum-gap/solution/zui-da-jian-ju-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''