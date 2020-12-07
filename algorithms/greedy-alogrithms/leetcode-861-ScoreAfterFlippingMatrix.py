'''
861. Score After Flipping Matrix
We have a two dimensional matrix A where each value is 0 or 1.

A move consists of choosing any row or column, and toggling each value in that row or column: changing all 0s to 1s, and all 1s to 0s.

After making any number of moves, every row of this matrix is interpreted as a binary number, and the score of the matrix is the sum of these numbers.

Return the highest possible score.



Example 1:

Input: [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
Output: 39
Explanation:
Toggled to [[1,1,1,1],[1,0,0,1],[1,1,1,1]].
0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39


Note:

1 <= A.length <= 20
1 <= A[0].length <= 20
A[i][j] is 0 or 1.

861. 翻转矩阵后的得分
有一个二维矩阵 A 其中每个元素的值为 0 或 1 。

移动是指选择任一行或列，并转换该行或列中的每一个值：将所有 0 都更改为 1，将所有 1 都更改为 0。

在做出任意次数的移动后，将该矩阵的每一行都按照二进制数来解释，矩阵的得分就是这些数字的总和。

返回尽可能高的分数。



示例：

输入：[[0,0,1,1],[1,0,1,0],[1,1,0,0]]
输出：39
解释：
转换为 [[1,1,1,1],[1,0,0,1],[1,1,1,1]]
0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39


提示：

1 <= A.length <= 20
1 <= A[0].length <= 20
A[i][j] 是 0 或 1
'''


class Solution(object):
    def matrixScore(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        m = len(A)
        n = len(A[0])
        res = 0
        for i in range(m):
            if A[i][0] == 0:
                for j in range(n):
                    A[i][j] ^= 1

        for j in range(n):
            cnt = 0
            for i in range(m):
                cnt += A[i][j]
            res += max(cnt, m - cnt) * (1 << (n - j - 1))

        return res


# solution

'''
方法一：贪心
根据题意，能够知道一个重要的事实：给定一个翻转方案，则它们之间任意交换顺序后，得到的结果保持不变。因此，我们总可以先考虑所有的行翻转，再考虑所有的列翻转。

不难发现一点：为了得到最高的分数，矩阵的每一行的最左边的数都必须为 11。为了做到这一点，我们可以翻转那些最左边的数不为 11 的那些行，而其他的行则保持不动。

当将每一行的最左边的数都变为 11 之后，就只能进行列翻转了。为了使得总得分最大，我们要让每个列中 11 的数目尽可能多。因此，我们扫描除了最左边的列以外的每一列，如果该列 00 的数目多于 11 的数目，就翻转该列，其他的列则保持不变。

实际编写代码时，我们无需修改原矩阵，而是可以计算每一列对总分数的「贡献」，从而直接计算出最高的分数。假设矩阵共有 mm 行 nn 列，计算方法如下：

对于最左边的列而言，由于最优情况下，它们的取值都为 11，因此每个元素对分数的贡献都为 2^{n-1}2 
n−1
 ，总贡献为 m \times 2^{n-1}m×2 
n−1
 。

对于第 jj 列（j>0j>0，此处规定最左边的列是第 00 列）而言，我们统计这一列 0,10,1 的数量，令其中的最大值为 kk，则 kk 是列翻转后的 11 的数量，该列的总贡献为 k \times 2^{n-j-1}k×2 
n−j−1
 。需要注意的是，在统计 0,10,1 的数量的时候，要考虑最初进行的行反转。

C++JavaGolangJavaScriptC

func matrixScore(a [][]int) int {
    m, n := len(a), len(a[0])
    ans := 1 << (n - 1) * m
    for j := 1; j < n; j++ {
        ones := 0
        for _, row := range a {
            if row[j] == row[0] {
                ones++
            }
        }
        if ones < m-ones {
            ones = m - ones
        }
        ans += 1 << (n - 1 - j) * ones
    }
    return ans
}
复杂度分析

时间复杂度：O(mn)O(mn)，其中 mm 为矩阵行数，nn 为矩阵列数。

空间复杂度：O(1)O(1)。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/score-after-flipping-matrix/solution/fan-zhuan-ju-zhen-hou-de-de-fen-by-leetc-cxma/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''