'''
976. Largest Perimeter Triangle
Given an array A of positive lengths, return the largest perimeter of a triangle with non-zero area, formed from 3 of these lengths.

If it is impossible to form any triangle of non-zero area, return 0.



Example 1:

Input: [2,1,2]
Output: 5
Example 2:

Input: [1,2,1]
Output: 0
Example 3:

Input: [3,2,3,4]
Output: 10
Example 4:

Input: [3,6,2,3]
Output: 8


Note:

3 <= A.length <= 10000
1 <= A[i] <= 10^6

976. 三角形的最大周长
给定由一些正数（代表长度）组成的数组 A，返回由其中三个长度组成的、面积不为零的三角形的最大周长。

如果不能形成任何面积不为零的三角形，返回 0。



示例 1：

输入：[2,1,2]
输出：5
示例 2：

输入：[1,2,1]
输出：0
示例 3：

输入：[3,2,3,4]
输出：10
示例 4：

输入：[3,6,2,3]
输出：8


提示：

3 <= A.length <= 10000
1 <= A[i] <= 10^6
'''


class Solution(object):
    def largestPerimeter(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A.sort()
        for i in range(len(A) - 1, 1, -1):
            if A[i] < (A[i - 1] + A[i - 2]):
                return A[i] + A[i - 1] + A[i - 2]

        return 0


# solution


'''
方法一：贪心 + 排序
不失一般性，我们假设三角形的边长满足 a \leq b \leq ca≤b≤c，那么这三条边组成面积不为零的三角形的充分必要条件为 a+b>ca+b>c。

基于此，我们可以选择枚举三角形的最长边 cc，而从贪心的角度考虑，我们一定是选「小于 cc 的最大的两个数」作为边长 aa 和 bb，此时最有可能满足 a+b>ca+b>c，使得三条边能够组成一个三角形，且此时的三角形的周长是最大的。

因此，我们先对整个数组排序，倒序枚举第 ii 个数作为最长边，那么我们只要看其前两个数 A[i-2]A[i−2] 和 A[i-1]A[i−1]，判断 A[i-2]+A[i-1]A[i−2]+A[i−1] 是否大于 A[i]A[i] 即可，如果能组成三角形我们就找到了最大周长的三角形，返回答案 A[i-2]+A[i-1]+A[i]A[i−2]+A[i−1]+A[i] 即可。如果对于任何数作为最长边都不存在面积不为零的三角形，则返回答案 00。

JavaC++JavaScriptGolangC

func largestPerimeter(a []int) int {
    sort.Ints(a)
    for i := len(a) - 1; i >= 2; i-- {
        if a[i-2]+a[i-1] > a[i] {
            return a[i-2] + a[i-1] + a[i]
        }
    }
    return 0
}
复杂度分析

时间复杂度：O(N \log N)O(NlogN)，其中 NN 是数组 AA 的长度。

空间复杂度：\Omega(\log N)Ω(logN)。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/largest-perimeter-triangle/solution/san-jiao-xing-de-zui-da-zhou-chang-by-leetcode-sol/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
