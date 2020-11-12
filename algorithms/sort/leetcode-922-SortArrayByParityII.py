'''
922. Sort Array By Parity II
Given an array A of non-negative integers, half of the integers in A are odd, and half of the integers are even.

Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] is even, i is even.

You may return any answer array that satisfies this condition.



Example 1:

Input: [4,2,5,7]
Output: [4,5,2,7]
Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.


Note:

2 <= A.length <= 20000
A.length % 2 == 0
0 <= A[i] <= 1000

922. 按奇偶排序数组 II
给定一个非负整数数组 A， A 中一半整数是奇数，一半整数是偶数。

对数组进行排序，以便当 A[i] 为奇数时，i 也是奇数；当 A[i] 为偶数时， i 也是偶数。

你可以返回任何满足上述条件的数组作为答案。



示例：

输入：[4,2,5,7]
输出：[4,5,2,7]
解释：[4,7,2,5]，[2,5,4,7]，[2,7,4,5] 也会被接受。


提示：

2 <= A.length <= 20000
A.length % 2 == 0
0 <= A[i] <= 1000
'''


class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        i, j = 0, 1

        while i < len(A) and j < len(A):
            while i < len(A) and A[i] % 2 == 0:
                i += 2
            while j < len(A) and A[j] % 2 == 1:
                j += 2
            if i < len(A) and j < len(A):
                A[i], A[j] = A[j], A[i]
        return A


# solution

'''
方法一： 两次遍历
思路和算法

遍历一遍数组把所有的偶数放进 ans[0]，ans[2]，ans[4]，依次类推。

再遍历一遍数组把所有的奇数依次放进 ans[1]，ans[3]，ans[5]，依次类推。

C++JavaCJavaScriptGolang

func sortArrayByParityII(a []int) []int {
    ans := make([]int, len(a))
    i := 0
    for _, v := range a {
        if v%2 == 0 {
            ans[i] = v
            i += 2
        }
    }
    i = 1
    for _, v := range a {
        if v%2 == 1 {
            ans[i] = v
            i += 2
        }
    }
    return ans
}
复杂度分析

时间复杂度：O(N)O(N)，其中 NN 是数组 A 的长度。

空间复杂度：O(1)O(1)。注意在这里我们不考虑输出数组的空间占用。

方法二： 双指针
思路与算法

如果原数组可以修改，则可以使用就地算法求解。

为数组的偶数下标部分和奇数下标部分分别维护指针 i, ji,j。随后，在每一步中，如果 A[i]A[i] 为奇数，则不断地向前移动 jj（每次移动两个单位），直到遇见下一个偶数。此时，可以直接将 A[i]A[i] 与 A[j]A[j] 交换。我们不断进行这样的过程，最终能够将所有的整数放在正确的位置上。

C++JavaCJavaScriptGolang

func sortArrayByParityII(a []int) []int {
    for i, j := 0, 1; i < len(a); i += 2 {
        if a[i]%2 == 1 {
            for a[j]%2 == 1 {
                j += 2
            }
            a[i], a[j] = a[j], a[i]
        }
    }
    return a
}
复杂度分析

时间复杂度：O(N)O(N)，其中 NN 是数组 A 的长度。

空间复杂度：O(1)O(1)。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/sort-array-by-parity-ii/solution/an-qi-ou-pai-xu-shu-zu-ii-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''