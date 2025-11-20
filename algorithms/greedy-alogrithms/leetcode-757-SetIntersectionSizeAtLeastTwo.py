# encoding=utf8

'''
757. Set Intersection Size At Least Two

An integer interval [a, b] (for integers a < b) is a set of all consecutive integers from a to b, including a and b.

Find the minimum size of a set S such that for every integer interval A in intervals, the intersection of S with A has a size of at least two.

 

Example 1:

Input: intervals = [[1,3],[1,4],[2,5],[3,5]]
Output: 3
Explanation: Consider the set S = {2, 3, 4}.  For each interval, there are at least 2 elements from S in the interval.
Also, there isn't a smaller size set that fulfills the above condition.
Thus, we output the size of this set, which is 3.
Example 2:

Input: intervals = [[1,2],[2,3],[2,4],[4,5]]
Output: 5
Explanation: An example of a minimum sized set is {1, 2, 3, 4, 5}.
 

Constraints:

1 <= intervals.length <= 3000
intervals[i].length == 2
0 <= ai < bi <= 108

757. 设置交集大小至少为2

给你一个二维整数数组 intervals ，其中 intervals[i] = [starti, endi] 表示从 starti 到 endi 的所有整数，包括 starti 和 endi 。

包含集合 是一个名为 nums 的数组，并满足 intervals 中的每个区间都 至少 有 两个 整数在 nums 中。

    例如，如果 intervals = [[1,3], [3,7], [8,9]] ，那么 [1,2,4,7,8,9] 和 [2,3,4,8,9] 都符合 包含集合 的定义。

返回包含集合可能的最小大小。

 

示例 1：

输入：intervals = [[1,3],[3,7],[8,9]]
输出：5
解释：nums = [2, 3, 4, 8, 9].
可以证明不存在元素数量为 4 的包含集合。

示例 2：

输入：intervals = [[1,3],[1,4],[2,5],[3,5]]
输出：3
解释：nums = [2, 3, 4].
可以证明不存在元素数量为 2 的包含集合。 

示例 3：

输入：intervals = [[1,2],[2,3],[2,4],[4,5]]
输出：5
解释：nums = [1, 2, 3, 4, 5].
可以证明不存在元素数量为 4 的包含集合。 

 

提示：

    1 <= intervals.length <= 3000
    intervals[i].length == 2
    0 <= starti < endi <= 108


'''

class Solution(object):
    def intersectionSizeTwo(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key = lambda x:(x[1],-x[0]))

        li = [-1,-1]
        for x in intervals:
            if x[0] <= li[-2]:
                continue
            if x[0] > li[-1]:
                li.append(x[1]-1)
            li.append(x[1])

        return len(li) - 2
        
