# encoding=utf8

'''
896. Monotonic Array
An array is monotonic if it is either monotone increasing or monotone decreasing.

An array A is monotone increasing if for all i <= j, A[i] <= A[j].  An array A is monotone decreasing if for all i <= j, A[i] >= A[j].

Return true if and only if the given array A is monotonic.



Example 1:

Input: [1,2,2,3]
Output: true
Example 2:

Input: [6,5,4,4]
Output: true
Example 3:

Input: [1,3,2]
Output: false
Example 4:

Input: [1,2,4,5]
Output: true
Example 5:

Input: [1,1,1]
Output: true


Note:

1 <= A.length <= 50000
-100000 <= A[i] <= 100000


896. 单调数列
如果数组是单调递增或单调递减的，那么它是单调的。

如果对于所有 i <= j，A[i] <= A[j]，那么数组 A 是单调递增的。 如果对于所有 i <= j，A[i]> = A[j]，那么数组 A 是单调递减的。

当给定的数组 A 是单调数组时返回 true，否则返回 false。



示例 1：

输入：[1,2,2,3]
输出：true
示例 2：

输入：[6,5,4,4]
输出：true
示例 3：

输入：[1,3,2]
输出：false
示例 4：

输入：[1,2,4,5]
输出：true
示例 5：

输入：[1,1,1]
输出：true


提示：

1 <= A.length <= 50000
-100000 <= A[i] <= 100000
'''



class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        inc, dec = False, False
        for i in range(1, len(A)):
            if A[i] > A[i-1]:
                inc |= True
            elif A[i] < A[i-1]:
                dec |= True
            if inc and dec:
                return False

        return not inc or not dec


class Solution1(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        inc, dec = True, True
        for i in range(1, len(A)):
            if A[i] > A[i-1]:
                inc = False
            elif A[i] < A[i-1]:
                dec = False
            if not inc and not dec:
                return False

        return inc or dec

class Solution20210228(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        return A == sorted(A) or A == sorted(A, reverse=True)


# solutions



'''
方法一：两次遍历
遍历两次数组，分别判断其是否为单调递增或单调递减。

代码

C++JavaGolangJavaScriptC

func isMonotonic(A []int) bool {
    return sort.IntsAreSorted(A) || sort.IsSorted(sort.Reverse(sort.IntSlice(A)))
}
复杂度分析

时间复杂度：O(n)O(n)，其中 nn 是数组 AA 的长度。

空间复杂度：O(1)O(1)。

方法二：一次遍历
遍历数组 AA，若既遇到了 A[i]>A[i+1]A[i]>A[i+1] 又遇到了 A[i']<A[i'+1]A[i 
′
 ]<A[i 
′
 +1]，则说明 AA 既不是单调递增的，也不是单调递减的。

代码

C++JavaGolangJavaScriptC

func isMonotonic(A []int) bool {
    inc, dec := true, true
    for i := 0; i < len(A)-1; i++ {
        if A[i] > A[i+1] {
            inc = false
        }
        if A[i] < A[i+1] {
            dec = false
        }
    }
    return inc || dec
}
复杂度分析

时间复杂度：O(n)O(n)，其中 nn 是数组 AA 的长度。

空间复杂度：O(1)O(1)。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/monotonic-array/solution/dan-diao-shu-lie-by-leetcode-solution-ysex/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
