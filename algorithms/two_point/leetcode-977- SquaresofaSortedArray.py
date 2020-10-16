'''
977. Squares of a Sorted Array
Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.



Example 1:

Input: [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Example 2:

Input: [-7,-3,2,3,11]
Output: [4,9,9,49,121]


Note:

1 <= A.length <= 10000
-10000 <= A[i] <= 10000
A is sorted in non-decreasing order.

977. 有序数组的平方
给定一个按非递减顺序排序的整数数组 A，返回每个数字的平方组成的新数组，要求也按非递减顺序排序。



示例 1：

输入：[-4,-1,0,3,10]
输出：[0,1,9,16,100]
示例 2：

输入：[-7,-3,2,3,11]
输出：[4,9,9,49,121]


提示：

1 <= A.length <= 10000
-10000 <= A[i] <= 10000
A 已按非递减顺序排序。
'''


class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        return sorted([i*i for i in A])



# solution

'''
方法一：直接排序
思路与算法

最简单的方法就是将数组 AA 中的数平方后直接排序。

代码

C++JavaPython3GolangC

class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        return sorted(num * num for num in A)
复杂度分析

时间复杂度：O(n \log n)O(nlogn)，其中 nn 是数组 AA 的长度。

空间复杂度：O(\log n)O(logn)。除了存储答案的数组以外，我们需要 O(\log n)O(logn) 的栈空间进行排序。

方法二：双指针
思路与算法

方法一没有利用「数组 AA 已经按照升序排序」这个条件。显然，如果数组 AA 中的所有数都是非负数，那么将每个数平方后，数组仍然保持升序；如果数组 AA 中的所有数都是负数，那么将每个数平方后，数组会保持降序。

这样一来，如果我们能够找到数组 AA 中负数与非负数的分界线，那么就可以用类似「归并排序」的方法了。具体地，我们设 \textit{neg}neg 为数组 AA 中负数与非负数的分界线，也就是说，A[0]A[0] 到 A[\textit{neg}]A[neg] 均为负数，而 A[\textit{neg}+1]A[neg+1] 到 A[n-1]A[n−1] 均为非负数。当我们将数组 AA 中的数平方后，那么 A[0]A[0] 到 A[\textit{neg}]A[neg] 单调递减，A[\textit{neg}+1]A[neg+1] 到 A[n-1]A[n−1] 单调递增。

由于我们得到了两个已经有序的子数组，因此就可以使用归并的方法进行排序了。具体地，使用两个指针分别指向位置 \textit{neg}neg 和 \textit{neg}+1neg+1，每次比较两个指针对应的数，选择较小的那个放入答案并移动指针。当某一指针移至边界时，将另一指针还未遍历到的数依次放入答案。

代码

C++JavaPython3GolangC

class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        n = len(A)
        negative = -1
        for i, num in enumerate(A):
            if num < 0:
                negative = i
            else:
                break

        ans = list()
        i, j = negative, negative + 1
        while i >= 0 or j < n:
            if i < 0:
                ans.append(A[j] * A[j])
                j += 1
            elif j == n:
                ans.append(A[i] * A[i])
                i -= 1
            elif A[i] * A[i] < A[j] * A[j]:
                ans.append(A[i] * A[i])
                i -= 1
            else:
                ans.append(A[j] * A[j])
                j += 1

        return ans
复杂度分析

时间复杂度：O(n)O(n)，其中 nn 是数组 AA 的长度。

空间复杂度：O(1)O(1)。

方法三：双指针
思路与算法

同样地，我们可以使用两个指针分别指向位置 00 和 n-1n−1，每次比较两个指针对应的数，选择较大的那个逆序放入答案并移动指针。这种方法无需处理某一指针移动至边界的情况，读者可以仔细思考其精髓所在。

代码

C++JavaPython3GolangC

class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        n = len(A)
        ans = [0] * n
        
        i, j, pos = 0, n - 1, n - 1
        while i <= j:
            if A[i] * A[i] > A[j] * A[j]:
                ans[pos] = A[i] * A[i]
                i += 1
            else:
                ans[pos] = A[j] * A[j]
                j -= 1
            pos -= 1
        
        return ans
复杂度分析

时间复杂度：O(n)O(n)，其中 nn 是数组 AA 的长度。

空间复杂度：O(1)O(1)。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/squares-of-a-sorted-array/solution/you-xu-shu-zu-de-ping-fang-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''