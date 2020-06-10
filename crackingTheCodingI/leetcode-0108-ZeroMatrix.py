'''
面试题 01.08. 零矩阵
编写一种算法，若M × N矩阵中某个元素为0，则将其所在的行与列清零。



示例 1：

输入：
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
输出：
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
示例 2：

输入：
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
输出：
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]

Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0.

 

Example 1:

Input:
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output:
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
Example 2:

Input:
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
Output:
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zero-matrix-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        cols = []
        rows = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    cols.append(i)
                    rows.append(j)
        # print(cols, rows)
        for i in cols:
            matrix[i][:] = [0] * len(matrix[0])
        for j in rows:
            for k in range(len(matrix)):
                matrix[k][j] = 0
        return matrix

# golang solutions

'''
func setZeroes(matrix [][]int)  {

    cols := []int{}
    rows := []int{}

    for i := 0; i < len(matrix); i ++ {
        for j := 0; j < len(matrix[0]);j++{
            if matrix[i][j] == 0{
                cols = append(cols, i)
                rows = append(rows, j)
            }
        }
    }

    for _, val := range cols{
        for j := 0; j < len(matrix[0]); j++{
            matrix[val][j] = 0
        }
    }

    for _, val := range rows{
        for j := 0; j < len(matrix); j++{
            matrix[j][val] = 0
        }
    }

}
'''

# tips

'''
如果你在找到0时清除了行和列，则可能会清理整个矩阵。在对矩阵进行任何更改之前，首先尝试找到所有的0。

你能只用额外的O(N)空间而不是O(N2)吗？在为0的单元格列表中你真正需要的是什么信息？

你可能需要一些数据存储来维护一个需要清零的行与列的列表。通过使用矩阵本身来存储数据，你是否可以把额外的空间占用减小到O(1)？
'''