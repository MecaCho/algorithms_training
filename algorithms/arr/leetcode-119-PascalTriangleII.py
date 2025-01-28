# encoding=utf8

'''
119. Pascal's Triangle II
Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 3
Output: [1,3,3,1]
Follow up:

Could you optimize your algorithm to use only O(k) extra space?

119. 杨辉三角 II
给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。



在杨辉三角中，每个数是它左上方和右上方的数的和。

示例:

输入: 3
输出: [1,3,3,1]
进阶：

你可以优化你的算法到 O(k) 空间复杂度吗？
'''


class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        else:
            val_list = [0] + self.getRow(rowIndex - 1) + [0]
            return [val_list[i] + val_list[i+1] for i in range(len(val_list) - 1)]



class Solution1(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex < 2:
            return [1]*(rowIndex+1)

        pre = self.getRow(rowIndex - 1)
        return [1] + [pre[i] + pre[i-1] for i in range(1, rowIndex)] + [1]


# solutions

'''
方法一：递推
杨辉三角，是二项式系数在三角形中的一种几何排列。它是中国古代数学的杰出研究成果之一，它把二项式系数图形化，把组合数内在的一些代数性质直观地从图形中体现出来，是一种离散型的数与形的结合。

杨辉三角具有以下性质：

每行数字左右对称，由 11 开始逐渐变大再变小，并最终回到 11。

第 nn 行（从 00 开始编号）的数字有 n+1n+1 项，前 nn 行共有 \frac{n(n+1)}{2} 
2
n(n+1)
​	
  个数。

第 nn 行的第 mm 个数（从 00 开始编号）可表示为可以被表示为组合数 \mathcal{C}(n,m)C(n,m)，记作 \mathcal{C}_n^mC 
n
m
​	
  或 \binom{n}{m}( 
m
n
​	
 )，即为从 nn 个不同元素中取 mm 个元素的组合数。我们可以用公式来表示它：\mathcal{C}_n^m=\dfrac{n!}{m!(n-m)!}C 
n
m
​	
 = 
m!(n−m)!
n!
​	
 

每个数字等于上一行的左右两个数字之和，可用此性质写出整个杨辉三角。即第 nn 行的第 ii 个数等于第 n-1n−1 行的第 i-1i−1 个数和第 ii 个数之和。这也是组合数的性质之一，即 \mathcal{C}_n^i=\mathcal{C}_{n-1}^i+\mathcal{C}_{n-1}^{i-1}C 
n
i
​	
 =C 
n−1
i
​	
 +C 
n−1
i−1
​	
 。

(a+b)^n(a+b) 
n
  的展开式（二项式展开）中的各项系数依次对应杨辉三角的第 nn 行中的每一项。

依据性质 44，我们可以一行一行地计算杨辉三角。每当我们计算出第 ii 行的值，我们就可以在线性时间复杂度内计算出第 i+1i+1 行的值。

代码

C++JavaGolangJavaScriptC

func getRow(rowIndex int) []int {
    C := make([][]int, rowIndex+1)
    for i := range C {
        C[i] = make([]int, i+1)
        C[i][0], C[i][i] = 1, 1
        for j := 1; j < i; j++ {
            C[i][j] = C[i-1][j-1] + C[i-1][j]
        }
    }
    return C[rowIndex]
}
优化

注意到对第 i+1i+1 行的计算仅用到了第 ii 行的数据，因此可以使用滚动数组的思想优化空间复杂度。

C++JavaGolangJavaScriptC

func getRow(rowIndex int) []int {
    var pre, cur []int
    for i := 0; i <= rowIndex; i++ {
        cur = make([]int, i+1)
        cur[0], cur[i] = 1, 1
        for j := 1; j < i; j++ {
            cur[j] = pre[j-1] + pre[j]
        }
        pre = cur
    }
    return pre
}
进一步优化

能否只用一个数组呢？

递推式 \mathcal{C}_n^i=\mathcal{C}_{n-1}^i+\mathcal{C}_{n-1}^{i-1}C 
n
i
​	
 =C 
n−1
i
​	
 +C 
n−1
i−1
​	
  表明，当前行第 ii 项的计算只与上一行第 i-1i−1 项及第 ii 项有关。因此我们可以倒着计算当前行，这样计算到第 ii 项时，第 i-1i−1 项仍然是上一行的值。

C++JavaGolangJavaScriptC

func getRow(rowIndex int) []int {
    row := make([]int, rowIndex+1)
    row[0] = 1
    for i := 1; i <= rowIndex; i++ {
        for j := i; j > 0; j-- {
            row[j] += row[j-1]
        }
    }
    return row
}
复杂度分析

时间复杂度：O(\textit{rowIndex}^2)O(rowIndex 
2
 )。

空间复杂度：O(1)O(1)。不考虑返回值的空间占用。

方法二：线性递推
由组合数公式 \mathcal{C}_n^m=\dfrac{n!}{m!(n-m)!}C 
n
m
​	
 = 
m!(n−m)!
n!
​	
 ，可以得到同一行的相邻组合数的关系

\mathcal{C}_n^m= \mathcal{C}_n^{m-1} \times \dfrac{n-m+1}{m}
C 
n
m
​	
 =C 
n
m−1
​	
 × 
m
n−m+1
​	
 

由于 \mathcal{C}_n^0=1C 
n
0
​	
 =1，利用上述公式我们可以在线性时间计算出第 nn 行的所有组合数。

代码

C++JavaGolangJavaScriptC

func getRow(rowIndex int) []int {
    row := make([]int, rowIndex+1)
    row[0] = 1
    for i := 1; i <= rowIndex; i++ {
        row[i] = row[i-1] * (rowIndex - i + 1) / i
    }
    return row
}
复杂度分析

时间复杂度：O(\textit{rowIndex})O(rowIndex)。

空间复杂度：O(1)O(1)。不考虑返回值的空间占用。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/pascals-triangle-ii/solution/yang-hui-san-jiao-ii-by-leetcode-solutio-shuk/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
