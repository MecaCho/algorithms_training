# encoding=utf8

'''
1232. Check If It Is a Straight Line
You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.





Example 1:



Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
Output: true
Example 2:



Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
Output: false


Constraints:

2 <= coordinates.length <= 1000
coordinates[i].length == 2
-10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
coordinates contains no duplicate point.


1232. 缀点成线
在一个 XY 坐标系中有一些点，我们用数组 coordinates 来分别记录它们的坐标，其中 coordinates[i] = [x, y] 表示横坐标为 x、纵坐标为 y 的点。

请你来判断，这些点是否在该坐标系中属于同一条直线上，是则返回 true，否则请返回 false。



示例 1：



输入：coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
输出：true
示例 2：



输入：coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
输出：false


提示：

2 <= coordinates.length <= 1000
coordinates[i].length == 2
-10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
coordinates 中不含重复的点
'''


class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        if len(coordinates) <= 2:
            return True
        x1 = coordinates[0][0]
        y1 = coordinates[0][1]

        x2 = coordinates[1][0]
        y2 = coordinates[1][1]

        for i in range(2, len(coordinates)):
            x, y = coordinates[i][0], coordinates[i][1]
            if (y - y1) * (x2 - x1) != (x - x1) * (y2 - y1):
                return False

        return True



# solution

'''
方法一：数学
思路

记数组 \textit{coordinates}coordinates 中的点为 P_0, P_1, \dots, P_{n-1}P 
0
​	
 ,P 
1
​	
 ,…,P 
n−1
​	
 。为方便后续计算，将所有点向 (-P_{0x}, -P_{0y})(−P 
0x
​	
 ,−P 
0y
​	
 ) 方向平移。记平移后的点为 P_0', P_1', \dots, P_{n-1}'P 
0
′
​	
 ,P 
1
′
​	
 ,…,P 
n−1
′
​	
 ，其中 P_i'=(P_{ix}-P_{0x}, P_{iy}-P_{0y})P 
i
′
​	
 =(P 
ix
​	
 −P 
0x
​	
 ,P 
iy
​	
 −P 
0y
​	
 )，P_0'P 
0
′
​	
  位于坐标系原点 OO 上。

由于经过两点的直线有且仅有一条，我们以 P_0'P 
0
′
​	
  和 P_1'P 
1
′
​	
  来确定这条直线。

因为 P_0'P 
0
′
​	
  位于坐标系原点 OO 上，直线过原点，故设其方程为 Ax+By=0Ax+By=0，将 P_1'P 
1
′
​	
  坐标代入可得 A=P_{1y}',B=-P_{1x}'A=P 
1y
′
​	
 ,B=−P 
1x
′
​	
 .

然后依次判断 P_2', \dots, P_{n-1}'P 
2
′
​	
 ,…,P 
n−1
′
​	
  是否在这条直线上，将其坐标代入直线方程即可。

代码

C++GolangJavaJavaScriptC

func checkStraightLine(coordinates [][]int) bool {
    deltaX, deltaY := coordinates[0][0], coordinates[0][1]
    for _, p := range coordinates {
        p[0] -= deltaX
        p[1] -= deltaY
    }
    A, B := coordinates[1][1], -coordinates[1][0]
    for _, p := range coordinates[2:] {
        x, y := p[0], p[1]
        if A*x+B*y != 0 {
            return false
        }
    }
    return true
}
复杂度分析

时间复杂度：O(n)O(n)，其中 nn 是数组中的元素数量。

时间复杂度：O(1)O(1)

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/check-if-it-is-a-straight-line/solution/zhui-dian-cheng-xian-by-leetcode-solutio-lpt6/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
