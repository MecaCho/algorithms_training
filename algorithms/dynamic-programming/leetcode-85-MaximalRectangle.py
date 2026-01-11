# encoding=utf8

'''
85. Maximal Rectangle

Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.



Example 1:


Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 6
Explanation: The maximal rectangle is shown in the above picture.
Example 2:

Input: matrix = []
Output: 0
Example 3:

Input: matrix = [["0"]]
Output: 0
Example 4:

Input: matrix = [["1"]]
Output: 1
Example 5:

Input: matrix = [["0","0"]]
Output: 0


Constraints:

rows == matrix.length
cols == matrix.length
0 <= row, cols <= 200
matrix[i][j] is '0' or '1'.


85. 最大矩形
给定一个仅包含 0 和 1 、大小为 rows x cols 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。



示例 1：


输入：matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
输出：6
解释：最大矩形如上图所示。
示例 2：

输入：matrix = []
输出：0
示例 3：

输入：matrix = [["0"]]
输出：0
示例 4：

输入：matrix = [["1"]]
输出：1
示例 5：

输入：matrix = [["0","0"]]
输出：0


提示：

rows == matrix.length
cols == matrix[0].length
0 <= row, cols <= 200
matrix[i][j] 为 '0' 或 '1'
'''

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
    
        rows = len(matrix)
        cols = len(matrix[0])
        max_area = 0
        # Initialize height array (histogram) for the first row
        heights = [0] * cols
        
        for row in range(rows):
            # Update the histogram for current row
            for col in range(cols):
                if matrix[row][col] == '1':
                    heights[col] += 1
                else:
                    heights[col] = 0
            
            # Calculate max area for current histogram (using monotonic stack)
            stack = []
            current_max = 0
            # Add a sentinel 0 at the end to process remaining bars in stack
            temp_heights = heights + [0]
            
            for i in range(len(temp_heights)):
                # Pop from stack when current height < stack top's height
                while stack and temp_heights[i] < temp_heights[stack[-1]]:
                    height_idx = stack.pop()
                    height = temp_heights[height_idx]
                    # Width = current index - previous index in stack - 1 (or current index if stack is empty)
                    width = i if not stack else i - stack[-1] - 1
                    current_max = max(current_max, height * width)
                stack.append(i)
            
            # Update global maximum area
            max_area = max(max_area, current_max)
        
        return max_area

# golang solution

'''
func maximalRectangle(matrix [][]byte) (ans int) {
    if len(matrix) == 0 {
        return
    }
    m, n := len(matrix), len(matrix[0])
    left := make([][]int, m)
    for i, row := range matrix {
        left[i] = make([]int, n)
        for j, v := range row {
            if v == '0' {
                continue
            }
            if j == 0 {
                left[i][j] = 1
            } else {
                left[i][j] = left[i][j-1] + 1
            }
        }
    }
    for i, row := range matrix {
        for j, v := range row {
            if v == '0' {
                continue
            }
            width := left[i][j]
            area := width
            for k := i - 1; k >= 0; k-- {
                width = min(width, left[k][j])
                area = max(area, (i-k+1)*width)
            }
            ans = max(ans, area)
        }
    }
    return
}

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}

'''
