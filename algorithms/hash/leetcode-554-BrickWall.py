# encoding=utf8


'''
554. Brick Wall

There is a rectangular brick wall in front of you with n rows of bricks. The ith row has some number of bricks each of the same height (i.e., one unit) but they can be of different widths. The total width of each row is the same.

Draw a vertical line from the top to the bottom and cross the least bricks. If your line goes through the edge of a brick, then the brick is not considered as crossed. You cannot draw a line just along one of the two vertical edges of the wall, in which case the line will obviously cross no bricks.

Given the 2D array wall that contains the information about the wall, return the minimum number of crossed bricks after drawing such a vertical line.

 

Example 1:


Input: wall = [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]
Output: 2
Example 2:

Input: wall = [[1],[1],[1]]
Output: 3
 

Constraints:

n == wall.length
1 <= n <= 104
1 <= wall[i].length <= 104
1 <= sum(wall[i].length) <= 2 * 104
sum(wall[i]) is the same for each row i.
1 <= wall[i][j] <= 231 - 1

554. 砖墙

你的面前有一堵矩形的、由 n 行砖块组成的砖墙。这些砖块高度相同（也就是一个单位高）但是宽度不同。每一行砖块的宽度之和应该相等。

你现在要画一条 自顶向下 的、穿过 最少 砖块的垂线。如果你画的线只是从砖块的边缘经过，就不算穿过这块砖。你不能沿着墙的两个垂直边缘之一画线，这样显然是没有穿过一块砖的。

给你一个二维数组 wall ，该数组包含这堵墙的相关信息。其中，wall[i] 是一个代表从左至右每块砖的宽度的数组。你需要找出怎样画才能使这条线 穿过的砖块数量最少 ，并且返回 穿过的砖块数量 。

 

示例 1：


输入：wall = [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]
输出：2
示例 2：

输入：wall = [[1],[1],[1]]
输出：3
 
提示：

n == wall.length
1 <= n <= 104
1 <= wall[i].length <= 104
1 <= sum(wall[i].length) <= 2 * 104
对于每一行 i ，sum(wall[i]) 应当是相同的
1 <= wall[i][j] <= 231 - 1

'''


class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """

        wall_dict = dict()
        for i in range(len(wall)):
            tmp = 0
            for j in range(len(wall[i]) - 1):
                tmp += wall[i][j]
                if tmp - 1 in wall_dict:
                    wall_dict[tmp-1] += 1
                else:
                    wall_dict[tmp-1] = 1
        return len(wall) - max(wall_dict.values()) if wall_dict else len(wall)
# solutions


'''
方法一：哈希表
思路及算法

由于砖墙是一面矩形，所以对于任意一条垂线，其穿过的砖块数量加上从边缘经过的砖块数量之和是一个定值，即砖墙的高度。

因此，问题可以转换成求「垂线穿过的砖块边缘数量的最大值」，用砖墙的高度减去该最大值即为答案。

虽然垂线在每行至多只能通过一个砖块边缘，但是每行的砖块边缘也各不相同，因此我们需要用哈希表统计所有符合要求的砖块边缘的数量。

注意到题目要求垂线不能通过砖墙的两个垂直边缘，所以砖墙两侧的边缘不应当被统计。因此，我们只需要统计每行砖块中除了最右侧的砖块以外的其他砖块的右边缘即可。

具体地，我们遍历砖墙的每一行，对于当前行，我们从左到右地扫描每一块砖，使用一个累加器记录当前砖的右侧边缘到砖墙的左边缘的距离，将除了最右侧的砖块以外的其他砖块的右边缘到砖墙的左边缘的距离加入到哈希表中。最后我们遍历该哈希表，找到出现次数最多的砖块边缘，这就是垂线经过的砖块边缘，而该垂线经过的砖块数量即为砖墙的高度减去该垂线经过的砖块边缘的数量。

代码

C++JavaC#JavaScriptGolangC

func leastBricks(wall [][]int) int {
    cnt := map[int]int{}
    for _, widths := range wall {
        sum := 0
        for _, width := range widths[:len(widths)-1] {
            sum += width
            cnt[sum]++
        }
    }
    maxCnt := 0
    for _, c := range cnt {
        if c > maxCnt {
            maxCnt = c
        }
    }
    return len(wall) - maxCnt
}
复杂度分析

时间复杂度：O(nm)O(nm)，其中 nn 是砖墙的高度，mm 是每行砖墙的砖的平均数量。我们需要遍历每行砖块中除了最右侧的砖块以外的每一块砖，将其右侧边缘到砖墙的左边缘的距离加入到哈希表中。

空间复杂度：O(nm)O(nm)，其中 nn 是砖墙的高度，mm 是每行砖墙的砖的平均数量。我们需要将每行砖块中除了最右侧的砖块以外的每一块砖的右侧边缘到砖墙的左边缘的距离加入到哈希表中。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/brick-wall/solution/zhuan-qiang-by-leetcode-solution-2kls/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
