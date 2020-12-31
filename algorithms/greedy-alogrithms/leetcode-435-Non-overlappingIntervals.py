# encoding=utf8

'''
435. Non-overlapping Intervals
Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.



Example 1:

Input: [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of intervals are non-overlapping.
Example 2:

Input: [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of intervals non-overlapping.
Example 3:

Input: [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.


Note:

You may assume the interval's end point is always bigger than its start point.
Intervals like [1,2] and [2,3] have borders "touching" but they don't overlap each other.


435. 无重叠区间
给定一个区间的集合，找到需要移除区间的最小数量，使剩余区间互不重叠。

注意:

可以认为区间的终点总是大于它的起点。
区间 [1,2] 和 [2,3] 的边界相互“接触”，但没有相互重叠。
示例 1:

输入: [ [1,2], [2,3], [3,4], [1,3] ]

输出: 1

解释: 移除 [1,3] 后，剩下的区间没有重叠。
示例 2:

输入: [ [1,2], [1,2], [1,2] ]

输出: 2

解释: 你需要移除两个 [1,2] 来使剩下的区间没有重叠。
示例 3:

输入: [ [1,2], [2,3] ]

输出: 0

解释: 你不需要移除任何区间，因为它们已经是无重叠的了。
'''


class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key=lambda x: x[1])

        if not intervals:
            return 0

        pre = intervals[0][1]

        count = 1
        for i in range(1, len(intervals)):
            if intervals[i][0] >= pre:
                count += 1
                pre = intervals[i][1]

        return len(intervals) - count


# solution

'''
方法一：动态规划
思路与算法

题目的要求等价于「选出最多数量的区间，使得它们互不重叠」。由于选出的区间互不重叠，因此我们可以将它们按照端点从小到大的顺序进行排序，并且无论我们按照左端点还是右端点进行排序，得到的结果都是唯一的。

这样一来，我们可以先将所有的 nn 个区间按照左端点（或者右端点）从小到大进行排序，随后使用动态规划的方法求出区间数量的最大值。设排完序后这 nn 个区间的左右端点分别为 l_0, \cdots, l_{n-1}l 
0
​	
 ,⋯,l 
n−1
​	
  以及 r_0, \cdots, r_{n-1}r 
0
​	
 ,⋯,r 
n−1
​	
 ，那么我们令 f_if 
i
​	
  表示「以区间 ii 为最后一个区间，可以选出的区间数量的最大值」，状态转移方程即为：

f_i = \min_{j < i ~\wedge~ r_j \leq l_i} \{ f_j \} + 1
f 
i
​	
 = 
j<i ∧ r 
j
​	
 ≤l 
i
​	
 
min
​	
 {f 
j
​	
 }+1

即我们枚举倒数第二个区间的编号 jj，满足 j < ij<i，并且第 jj 个区间必须要与第 ii 个区间不重叠。由于我们已经按照左端点进行升序排序了，因此只要第 jj 个区间的右端点 r_jr 
j
​	
  没有越过第 ii 个区间的左端点 l_il 
i
​	
 ，即 r_j \leq l_ir 
j
​	
 ≤l 
i
​	
 ，那么第 jj 个区间就与第 ii 个区间不重叠。我们在所有满足要求的 jj 中，选择 f_jf 
j
​	
  最大的那一个进行状态转移，如果找不到满足要求的区间，那么状态转移方程中 \minmin 这一项就为 00，f_if 
i
​	
  就为 11。

最终的答案即为所有 f_if 
i
​	
  中的最大值。

代码

由于方法一的时间复杂度较高，因此在下面的 \texttt{Python}Python 代码中，我们尽量使用列表推导优化常数，使得其可以在时间限制内通过所有测试数据。

C++JavaPython3GolangCJavaScript

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        intervals.sort()
        n = len(intervals)
        f = [1]

        for i in range(1, n):
            f.append(max((f[j] for j in range(i) if intervals[j][1] <= intervals[i][0]), default=0) + 1)

        return n - max(f)
复杂度分析

时间复杂度：O(n^2)O(n 
2
 )，其中 nn 是区间的数量。我们需要 O(n \log n)O(nlogn) 的时间对所有的区间按照左端点进行升序排序，并且需要 O(n^2)O(n 
2
 ) 的时间进行动态规划。由于前者在渐进意义下小于后者，因此总时间复杂度为 O(n^2)O(n 
2
 )。

注意到方法一本质上是一个「最长上升子序列」问题，因此我们可以将时间复杂度优化至 O(n \log n)O(nlogn)，具体可以参考「300. 最长递增子序列的官方题解」

空间复杂度：O(n)O(n)，即为存储所有状态 f_if 
i
​	
  需要的空间。

方法二：贪心算法
思路与算法

我们不妨想一想应该选择哪一个区间作为首个区间。

假设在某一种最优的选择方法中，[l_k, r_k][l 
k
​	
 ,r 
k
​	
 ] 是首个（即最左侧的）区间，那么它的左侧没有其它区间，右侧有若干个不重叠的区间。设想一下，如果此时存在一个区间 [l_j, r_j][l 
j
​	
 ,r 
j
​	
 ]，使得 r_j < r_kr 
j
​	
 <r 
k
​	
 ，即区间 jj 的右端点在区间 kk 的左侧，那么我们将区间 kk 替换为区间 jj，其与剩余右侧被选择的区间仍然是不重叠的。而当我们将区间 kk 替换为区间 jj 后，就得到了另一种最优的选择方法。

我们可以不断地寻找右端点在首个区间右端点左侧的新区间，将首个区间替换成该区间。那么当我们无法替换时，首个区间就是所有可以选择的区间中右端点最小的那个区间。因此我们将所有区间按照右端点从小到大进行排序，那么排完序之后的首个区间，就是我们选择的首个区间。

如果有多个区间的右端点都同样最小怎么办？由于我们选择的是首个区间，因此在左侧不会有其它的区间，那么左端点在何处是不重要的，我们只要任意选择一个右端点最小的区间即可。

当确定了首个区间之后，所有与首个区间不重合的区间就组成了一个规模更小的子问题。由于我们已经在初始时将所有区间按照右端点排好序了，因此对于这个子问题，我们无需再次进行排序，只要找出其中与首个区间不重合并且右端点最小的区间即可。用相同的方法，我们可以依次确定后续的所有区间。

在实际的代码编写中，我们对按照右端点排好序的区间进行遍历，并且实时维护上一个选择区间的右端点 \textit{right}right。如果当前遍历到的区间 [l_i, r_i][l 
i
​	
 ,r 
i
​	
 ] 与上一个区间不重合，即 l_i \geq \textit{right}l 
i
​	
 ≥right，那么我们就可以贪心地选择这个区间，并将 \textit{right}right 更新为 r_ir 
i
​	
 。

代码

C++JavaPython3GolangCJavaScript

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        intervals.sort(key=lambda x: x[1])
        n = len(intervals)
        right = intervals[0][1]
        ans = 1

        for i in range(1, n):
            if intervals[i][0] >= right:
                ans += 1
                right = intervals[i][1]
        
        return n - ans
复杂度分析

时间复杂度：O(n \log n)O(nlogn)，其中 nn 是区间的数量。我们需要 O(n \log n)O(nlogn) 的时间对所有的区间按照左端点进行升序排序，并且需要 O(n)O(n) 的时间进行遍历。由于前者在渐进意义下大于后者，因此总时间复杂度为 O(n \log n)O(nlogn)。

空间复杂度：O(\log n)O(logn)，即为排序需要使用的栈空间。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/non-overlapping-intervals/solution/wu-zhong-die-qu-jian-by-leetcode-solutio-cpsb/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
