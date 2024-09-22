# encoding=utf8

'''
1014. Best Sightseeing Pair
Given an array A of positive integers, A[i] represents the value of the i-th sightseeing spot, and two sightseeing spots i and j have distance j - i between them.

The score of a pair (i < j) of sightseeing spots is (A[i] + A[j] + i - j) : the sum of the values of the sightseeing spots, minus the distance between them.

Return the maximum score of a pair of sightseeing spots.



Example 1:

Input: [8,1,5,2,6]
Output: 11
Explanation: i = 0, j = 2, A[i] + A[j] + i - j = 8 + 5 + 0 - 2 = 11


Note:

2 <= A.length <= 50000
1 <= A[i] <= 1000

1014. 最佳观光组合
给定正整数数组 A，A[i] 表示第 i 个观光景点的评分，并且两个景点 i 和 j 之间的距离为 j - i。

一对景点（i < j）组成的观光组合的得分为（A[i] + A[j] + i - j）：景点的评分之和减去它们两者之间的距离。

返回一对观光景点能取得的最高分。



示例：

输入：[8,1,5,2,6]
输出：11
解释：i = 0, j = 2, A[i] + A[j] + i - j = 8 + 5 + 0 - 2 = 11


提示：

2 <= A.length <= 50000
1 <= A[i] <= 1000
'''

class Solution(object):
    def maxScoreSightseeingPair(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        max_val = 0
        # vals = []
        pre_max = A[0]
        for i in range(1, len(A)):
            max_val = max(max_val, pre_max+A[i]-i)
            pre_max = max(pre_max, A[i]+i)
        return max_val

class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        res = 0
        pre_max = values[0] 
        for i in range(1, len(values)):
            res = max(res, pre_max+values[i]-i)
            pre_max = max(pre_max, values[i]+i)
        return res


# tips

'''
Can you tell the best sightseeing spot in one pass (ie. as you iterate over the input?) What should we store or keep track of as we iterate to do this?
'''

#  solutions

'''
方法一：枚举
思路和算法

我们考虑从前往后枚举 jj 来统计答案，对于每个观光景点 jj 而言，我们需要遍历 [0,j-1][0,j−1] 的观光景点 ii 来计算组成观光组合 (i,j)(i,j) 得分的最大值 \textit{cnt}_jcnt 
j
​	
  来作为第 jj 个观光景点的值，那么最后的答案无疑就是所有观光景点值的最大值，即 \max_{j=0..n-1}\{cnt_j\}max 
j=0..n−1
​	
 {cnt 
j
​	
 }。但是枚举 jj 需要 O(n)O(n) 的时间复杂度，遍历 [0,j-1][0,j−1] 的观光景点 ii 也需要 O(n)O(n) 的时间复杂度，因此该方法总复杂度为 O(n^2)O(n 
2
 )，不能通过所有测试用例，我们需要进一步优化时间复杂度。

我们回过头来看得分公式，我们可以将其拆分成 A[i]+iA[i]+i 和 A[j]-jA[j]−j 两部分，这样对于统计景点 jj 答案的时候，由于 A[j]-jA[j]−j 是固定不变的，因此最大化 A[i]+i+A[j]-jA[i]+i+A[j]−j 的值其实就等价于求 [0,j-1][0,j−1] 中 A[i]+iA[i]+i 的最大值 mxmx，景点 jj 的答案即为 mx+A[j]-jmx+A[j]−j 。而 mxmx 的值我们只要从前往后枚举 jj 的时候同时维护即可，这样每次枚举景点 jj 的时候，寻找使得得分最大的 ii 就能从 O(n)O(n) 降至 O(1)O(1) 的时间复杂度，总时间复杂度就能从 O(n^2)O(n 
2
 ) 降至 O(n)O(n)。


1 / 9

C++JavaGolangC#

func maxScoreSightseeingPair(A []int) int {
    ans, mx := 0, A[0] + 0
    for j := 1; j < len(A); j++ {
        ans = max(ans, mx + A[j] - j)
        // 边遍历边维护
        mx = max(mx, A[j] + j)
    }
    return ans
}

func max(x, y int) int {
    if x > y {
        return x
    }
    return y
}
复杂度分析

时间复杂度：O(n)O(n)，其中 nn 为数组 AA 的大小。我们只需要遍历一遍数组即可。
空间复杂度：O(1)O(1)。我们只需要常数空间来存放若干变量。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/best-sightseeing-pair/solution/zui-jia-guan-guang-zu-he-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
