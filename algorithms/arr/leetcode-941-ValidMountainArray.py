'''
941. Valid Mountain Array
Given an array A of integers, return true if and only if it is a valid mountain array.

Recall that A is a mountain array if and only if:

A.length >= 3
There exists some i with 0 < i < A.length - 1 such that:
A[0] < A[1] < ... A[i-1] < A[i]
A[i] > A[i+1] > ... > A[A.length - 1]




Example 1:

Input: [2,1]
Output: false
Example 2:

Input: [3,5,5]
Output: false
Example 3:

Input: [0,3,2,1]
Output: true


Note:

0 <= A.length <= 10000
0 <= A[i] <= 10000


941. 有效的山脉数组
给定一个整数数组 A，如果它是有效的山脉数组就返回 true，否则返回 false。

让我们回顾一下，如果 A 满足下述条件，那么它是一个山脉数组：

A.length >= 3
在 0 < i < A.length - 1 条件下，存在 i 使得：
A[0] < A[1] < ... A[i-1] < A[i]
A[i] > A[i+1] > ... > A[A.length - 1]






示例 1：

输入：[2,1]
输出：false
示例 2：

输入：[3,5,5]
输出：false
示例 3：

输入：[0,3,2,1]
输出：true


提示：

0 <= A.length <= 10000
0 <= A[i] <= 10000
'''


class Solution(object):
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A) < 3:
            return False

        mount = 0

        for i in range(1, len(A)-1):
            if A[i] > A[i-1] and A[i] > A[i+1]:
                mount += 1

            if mount > 1 or A[i] == A[i-1]:
                return False
        print(mount)

        return mount == 1 and A[-1] < A[-2] and A[0] < A[1]

# solution

'''
方法一：线性扫描
按题意模拟即可。我们从数组的最左侧开始向右扫描，直到找到第一个不满足 A[i] < A[i + 1]A[i]<A[i+1] 的下标 ii，那么 ii 就是这个数组的最高点的下标。如果 i = 0i=0 或者不存在这样的 ii（即整个数组都是单调递增的），那么就返回 \text{false}false。否则从 ii 开始继续向右扫描，判断接下来的的下标 jj 是否都满足 A[j] > A[j + 1]A[j]>A[j+1]，若都满足就返回 \text{true}true，否则返回 \text{false}false。

JavaPythonC++JavaScriptGolangC

class Solution(object):
    def validMountainArray(self, A):
        N = len(A)
        i = 0

        # 递增扫描
        while i + 1 < N and A[i] < A[i + 1]:
            i += 1

        # 最高点不能是数组的第一个位置或最后一个位置
        if i == 0 or i == N - 1:
            return False

        # 递减扫描
        while i + 1 < N and A[i] > A[i + 1]:
            i += 1

        return i == N - 1
复杂度分析

时间复杂度：O(N)O(N)，其中 NN 是数组 AA 的长度。

空间复杂度：O(1)O(1)。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/valid-mountain-array/solution/you-xiao-de-shan-mai-shu-zu-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''