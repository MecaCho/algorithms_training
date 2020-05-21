'''
750. 角矩形的数量
给定一个只包含 0 和 1 的网格，找出其中角矩形的数量。

一个「角矩形」是由四个不同的在网格上的 1 形成的轴对称的矩形。注意只有角的位置才需要为 1。并且，4 个 1 需要是不同的。



示例 1：

输入：grid =
[[1, 0, 0, 1, 0],
 [0, 0, 1, 0, 1],
 [0, 0, 0, 1, 0],
 [1, 0, 1, 0, 1]]
输出：1
解释：只有一个角矩形，角的位置为 grid[1][2], grid[1][4], grid[3][2], grid[3][4]。
示例 2：

输入：grid =
[[1, 1, 1],
 [1, 1, 1],
 [1, 1, 1]]
输出：9
解释：这里有 4 个 2x2 的矩形，4 个 2x3 和 3x2 的矩形和 1 个 3x3 的矩形。
示例 3：

输入：grid =
[[1, 1, 1, 1]]
输出：0
解释：矩形必须有 4 个不同的角。


提示：

网格 grid 中行和列的数目范围为 [1, 200]。
每个网格 grid[i][j] 中的值不是 0 就是 1 。
网格中 1 的个数不会超过 6000。


750. Number Of Corner Rectangles
Given a grid where each entry is only 0 or 1, find the number of corner rectangles.

A corner rectangle is 4 distinct 1s on the grid that form an axis-aligned rectangle. Note that only the corners need to have the value 1. Also, all four 1s used must be distinct.



Example 1:

Input: grid =
[[1, 0, 0, 1, 0],
 [0, 0, 1, 0, 1],
 [0, 0, 0, 1, 0],
 [1, 0, 1, 0, 1]]
Output: 1
Explanation: There is only one corner rectangle, with corners grid[1][2], grid[1][4], grid[3][2], grid[3][4].


Example 2:

Input: grid =
[[1, 1, 1],
 [1, 1, 1],
 [1, 1, 1]]
Output: 9
Explanation: There are four 2x2 rectangles, four 2x3 and 3x2 rectangles, and one 3x3 rectangle.


Example 3:

Input: grid =
[[1, 1, 1, 1]]
Output: 0
Explanation: Rectangles must have four distinct corners.


Note:

The number of rows and columns of grid will each be in the range [1, 200].
Each grid[i][j] will be either 0 or 1.
The number of 1s in the grid will be at most 6000.
'''



import collections

class Solution(object):
    def countCornerRectangles(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        count = collections.Counter()
        ans = 0
        for row in grid:
            # print(row)
            for i in range(len(row)):
                if row[i]:
                    for j in range(i+1, len(row)):
                        if row[j]:
                            ans += count[i, j]
                            count[i, j] += 1
            # print(count)
        return ans


# tips

'''
For each pair of 1s in the new row (say at `new_row[i]` and `new_row[j]`), we could create more rectangles where that pair forms the base. The number of new rectangles is the number of times some previous row had `row[i] = row[j] = 1`.
'''

# solutions

'''
方法一：
我们可以转换一下思想：每增加一行，角矩形的数量增加了多少。

算法：
我们用 count[i, j] 来记录 row[i] = row[j] = 1 的次数。当我们处理新的一行时，对于每一对 new_row[i] = new_row[j] = 1，我们添加 count[i, j] 到答案中，然后 count[i, j]++。

PythonJava
class Solution(object):
    def countCornerRectangles(self, grid):
        count = collections.Counter()
        ans = 0
        for row in grid:
            for c1, v1 in enumerate(row):
                if v1:
                    for c2 in xrange(c1+1, len(row)):
                        if row[c2]:
                            ans += count[c1, c2]
                            count[c1, c2] += 1
        return ans
复杂度分析

时间复杂度：O(R*C^2)O(R∗C 
2
 )。其中 R, CR,C 指的是行和列。
空间复杂度：使用了 O(C^2)O(C 
2
 ) 的额外空间。
方法二：
算法：

我们能改进方法 1 中的方法吗？当一行有 XX 个 1 时，我们需要 O(X^2)O(X 
2
 ) 的时间来枚举每对 1。当 XX 很小时，这是可以接受的；但当 XX 很大时，这是较为耗时的操作。
假设第一行的元素都是 1 时，f 指的是下一行和第一行所匹配 1 的数量。所能够构造角矩形的数量就是所匹配 1 的数量的对数，即 f * (f-1) / 2。我们可以使用一个集合和对每行进行简单线性扫描快速找到每个 f。
PythonJava
class Solution(object):
    def countCornerRectangles(self, grid):
        rows = [[c for c, val in enumerate(row) if val]
                for row in grid]
        N = sum(len(row) for row in grid)
        SQRTN = int(N**.5)

        ans = 0
        count = collections.Counter()
        for r, row in enumerate(rows):
            if len(row) >= SQRTN:
                target = set(row)
                for r2, row2 in enumerate(rows):
                    if r2 <= r and len(row2) >= SQRTN:
                        continue
                    found = sum(1 for c2 in row2 if c2 in target)
                    ans += found * (found - 1) / 2
            else:
                for pair in itertools.combinations(row, 2):
                    ans += count[pair]
                    count[pair] += 1

        return ans
复杂度分析

时间复杂度：O(N \sqrt N + R*C)O(N 
N
​	
 +R∗C)。其中 NN 是网格中的个数。
空间复杂度：O(N + R + C^2)O(N+R+C 
2
 )，rows, target 和 count 所使用的空间。

作者：LeetCode
链接：https://leetcode-cn.com/problems/number-of-corner-rectangles/solution/jiao-ju-xing-de-shu-liang-by-leetcode/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
