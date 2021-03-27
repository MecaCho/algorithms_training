# encoding=utf8


'''

118. 杨辉三角
给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。



在杨辉三角中，每个数是它左上方和右上方的数的和。

示例:

输入: 5
输出:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]


118. Pascal's Triangle
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
'''



class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows < 1:
            return []
        elif numRows == 1:
            return [[1]]
        else:
            val_list = self.generate(numRows - 1)
            val_list.append([1] + [val_list[-1][i] + val_list[-1][i+1] for i in range(len(val_list[-1]) - 1)] + [1])
            return val_list



class Solution20201206(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []
        for i in range(numRows):
            tmp = [1]
            if res:
                pre_row = res[-1]
                pre_length = len(res[-1])
                for j in range(1, pre_length):
                    tmp.append(pre_row[j]+pre_row[j-1])
                tmp.append(1)
            res.append(tmp)

        return res


# solution

'''
方法一：数学
思路及解法

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
 )，即为从 nn 个不同元素中取 mm 个元素的组合数。我们可以用公式来表示它：\mathcal{C}_n^m=\dfrac{n!}{m!\times (n-m)!}C 
n
m
​	
 = 
m!×(n−m)!
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

C++JavaGolangCJavaScriptPython3

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ret = list()
        for i in range(numRows):
            row = list()
            for j in range(0, i + 1):
                if j == 0 or j == i:
                    row.append(1)
                else:
                    row.append(ret[i - 1][j] + ret[i - 1][j - 1])
            ret.append(row)
        return ret
复杂度分析

时间复杂度：O(\textit{numRows}^2)O(numRows 
2
 )。

空间复杂度：O(1)O(1)。不考虑返回值的空间占用。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/pascals-triangle/solution/yang-hui-san-jiao-by-leetcode-solution-lew9/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
