'''
1030. Matrix Cells in Distance Order
We are given a matrix with R rows and C columns has cells with integer coordinates (r, c), where 0 <= r < R and 0 <= c < C.

Additionally, we are given a cell in that matrix with coordinates (r0, c0).

Return the coordinates of all cells in the matrix, sorted by their distance from (r0, c0) from smallest distance to largest distance.  Here, the distance between two cells (r1, c1) and (r2, c2) is the Manhattan distance, |r1 - r2| + |c1 - c2|.  (You may return the answer in any order that satisfies this condition.)



Example 1:

Input: R = 1, C = 2, r0 = 0, c0 = 0
Output: [[0,0],[0,1]]
Explanation: The distances from (r0, c0) to other cells are: [0,1]
Example 2:

Input: R = 2, C = 2, r0 = 0, c0 = 1
Output: [[0,1],[0,0],[1,1],[1,0]]
Explanation: The distances from (r0, c0) to other cells are: [0,1,1,2]
The answer [[0,1],[1,1],[0,0],[1,0]] would also be accepted as correct.
Example 3:

Input: R = 2, C = 3, r0 = 1, c0 = 2
Output: [[1,2],[0,2],[1,1],[0,1],[1,0],[0,0]]
Explanation: The distances from (r0, c0) to other cells are: [0,1,1,2,2,3]
There are other answers that would also be accepted as correct, such as [[1,2],[1,1],[0,2],[1,0],[0,1],[0,0]].


Note:

1 <= R <= 100
1 <= C <= 100
0 <= r0 < R
0 <= c0 < C

1030. 距离顺序排列矩阵单元格
给出 R 行 C 列的矩阵，其中的单元格的整数坐标为 (r, c)，满足 0 <= r < R 且 0 <= c < C。

另外，我们在该矩阵中给出了一个坐标为 (r0, c0) 的单元格。

返回矩阵中的所有单元格的坐标，并按到 (r0, c0) 的距离从最小到最大的顺序排，其中，两单元格(r1, c1) 和 (r2, c2) 之间的距离是曼哈顿距离，|r1 - r2| + |c1 - c2|。（你可以按任何满足此条件的顺序返回答案。）



示例 1：

输入：R = 1, C = 2, r0 = 0, c0 = 0
输出：[[0,0],[0,1]]
解释：从 (r0, c0) 到其他单元格的距离为：[0,1]
示例 2：

输入：R = 2, C = 2, r0 = 0, c0 = 1
输出：[[0,1],[0,0],[1,1],[1,0]]
解释：从 (r0, c0) 到其他单元格的距离为：[0,1,1,2]
[[0,1],[1,1],[0,0],[1,0]] 也会被视作正确答案。
示例 3：

输入：R = 2, C = 3, r0 = 1, c0 = 2
输出：[[1,2],[0,2],[1,1],[0,1],[1,0],[0,0]]
解释：从 (r0, c0) 到其他单元格的距离为：[0,1,1,2,2,3]
其他满足题目要求的答案也会被视为正确，例如 [[1,2],[1,1],[0,2],[1,0],[0,1],[0,0]]。


提示：

1 <= R <= 100
1 <= C <= 100
0 <= r0 < R
0 <= c0 < C
'''


class Solution(object):
    def allCellsDistOrder(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
        ret = [(i, j) for i in range(R) for j in range(C)]
        ret.sort(key=lambda x: abs(x[0] - r0) + abs(x[1] - c0))
        return ret

# solution

'''
方法一：直接排序
思路及解法

最容易想到的方法是首先存储矩阵内所有的点，然后将其按照哈曼顿距离直接排序。

代码

C++JavaGolangPython3C

class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        ret = [(i, j) for i in range(R) for j in range(C)]
        ret.sort(key=lambda x: abs(x[0] - r0) + abs(x[1] - c0))
        return ret
复杂度分析

时间复杂度：O(RC \log(RC))O(RClog(RC))，存储所有点时间复杂度 O(RC)O(RC)，排序时间复杂度 O(RC \log(RC))O(RClog(RC))。

空间复杂度：O(\log(RC))O(log(RC))，即为排序需要使用的栈空间，不考虑返回值的空间占用。

方法二：桶排序
思路及解法

注意到方法一中排序的时间复杂度太高。实际在枚举所有点时，我们可以直接按照哈曼顿距离分桶。这样我们就可以实现线性的桶排序。

代码

C++JavaGolangPython3C

class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        maxDist = max(r0, R - 1 - r0) + max(c0, C - 1 - c0)
        bucket = collections.defaultdict(list)
        dist = lambda r1, c1, r2, c2: abs(r1 - r2) + abs(c1 - c2)

        for i in range(R):
            for j in range(C):
                bucket[dist(i, j, r0, c0)].append([i, j])

        ret = list()
        for i in range(maxDist + 1):
            ret.extend(bucket[i])
        
        return ret
复杂度分析

时间复杂度：O(RC)O(RC)，存储所有点时间复杂度 O(RC)O(RC)，桶排序时间复杂度 O(RC)O(RC)。

空间复杂度：O(RC)O(RC)，需要存储矩阵内所有点。

方法三：几何法
思路及解法

我们也可以直接变换枚举矩阵的顺序，直接按照曼哈顿距离遍历该矩形即可。

注意到曼哈顿距离相同的位置恰好构成一个斜着的正方形边框，因此我们可以从小到大枚举曼哈顿距离，并使用循环来直接枚举该距离对应的边框。我们每次从该正方形边框的上顶点出发，依次经过右顶点、下顶点和左顶点，最后回到上顶点。这样即可完成当前层的遍历。



注意正方形边框中的部分点不一定落在矩阵中，所以我们需要做好边界判断。

代码

C++JavaGolangPython3C

class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        dirs = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
        maxDist = max(r0, R - 1 - r0) + max(c0, C - 1 - c0)
        row, col = r0, c0
        ret = [[row, col]]
        for dist in range(1, maxDist + 1):
            row -= 1
            for i, (dr, dc) in enumerate(dirs):
                while (i % 2 == 0 and row != r0) or (i % 2 != 0 and col != c0):
                    if 0 <= row < R and 0 <= col < C:
                        ret.append([row, col])
                    row += dr
                    col += dc
        return ret
复杂度分析

时间复杂度：O\big((R+C)^2\big)O((R+C) 
2
 )，我们需要遍历矩阵内所有点，同时也会遍历部分超过矩阵部分的点。在最坏情况下，给定的单元格位于矩阵的一个角，例如 (0,0)(0,0)，此时最大的曼哈顿距离为 R+C-2R+C−2，需要遍历的点数为 2(R+C-2)(R+C-1)+12(R+C−2)(R+C−1)+1，因此时间复杂度为 O\big((R+C)^2\big)O((R+C) 
2
 )。

空间复杂度：O(1)O(1)，不考虑返回值的空间占用。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/matrix-cells-in-distance-order/solution/ju-chi-shun-xu-pai-lie-ju-zhen-dan-yuan-ge-by-leet/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''