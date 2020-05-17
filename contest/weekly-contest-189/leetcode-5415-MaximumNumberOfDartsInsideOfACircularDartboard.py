


'''
5415. 圆形靶内的最大飞镖数量
墙壁上挂着一个圆形的飞镖靶。现在请你蒙着眼睛向靶上投掷飞镖。

投掷到墙上的飞镖用二维平面上的点坐标数组表示。飞镖靶的半径为 r 。

请返回能够落在 任意 半径为 r 的圆形靶内或靶上的最大飞镖数。



示例 1：



输入：points = [[-2,0],[2,0],[0,2],[0,-2]], r = 2
输出：4
解释：如果圆形的飞镖靶的圆心为 (0,0) ，半径为 2 ，所有的飞镖都落在靶上，此时落在靶上的飞镖数最大，值为 4 。
示例 2：



输入：points = [[-3,0],[3,0],[2,6],[5,4],[0,9],[7,8]], r = 5
输出：5
解释：如果圆形的飞镖靶的圆心为 (0,4) ，半径为 5 ，则除了 (7,8) 之外的飞镖都落在靶上，此时落在靶上的飞镖数最大，值为 5 。
示例 3：

输入：points = [[-2,0],[2,0],[0,2],[0,-2]], r = 1
输出：1
示例 4：

输入：points = [[1,2],[3,5],[1,-1],[2,3],[4,1],[1,3]], r = 2
输出：4


提示：

1 <= points.length <= 100
points[i].length == 2
-10^4 <= points[i][0], points[i][1] <= 10^4
1 <= r <= 5000

5415. Maximum Number of Darts Inside of a Circular Dartboard
You have a very large square wall and a circular dartboard placed on the wall. You have been challenged to throw darts into the board blindfolded. Darts thrown at the wall are represented as an array of points on a 2D plane.

Return the maximum number of points that are within or lie on any circular dartboard of radius r.



Example 1:



Input: points = [[-2,0],[2,0],[0,2],[0,-2]], r = 2
Output: 4
Explanation: Circle dartboard with center in (0,0) and radius = 2 contain all points.
Example 2:



Input: points = [[-3,0],[3,0],[2,6],[5,4],[0,9],[7,8]], r = 5
Output: 5
Explanation: Circle dartboard with center in (0,4) and radius = 5 contain all points except the point (7,8).
Example 3:

Input: points = [[-2,0],[2,0],[0,2],[0,-2]], r = 1
Output: 1
Example 4:

Input: points = [[1,2],[3,5],[1,-1],[2,3],[4,1],[1,3]], r = 2
Output: 4


Constraints:

1 <= points.length <= 100
points[i].length == 2
-10^4 <= points[i][0], points[i][1] <= 10^4
1 <= r <= 5000
'''

import math

class Solution(object):
    def numPoints(self, points, r):
        """
        :type points: List[List[int]]
        :type r: int
        :rtype: int
        """

        # def cald(a, b):
        #     x1, y1 = a
        #     x2, y2 = b
        #     return  math.sqrt((x1-x2)**2+(y1-y2)**2)

        # def GetCenter(a,b):
        #     mid_x = (a[0]+b[0])/2
        #     mid_y = (a[1]+b[1])/2
        #     angle  = math.atan2(b[1]-a[1],b[0]-a[0])
        #     d = math.sqrt(r**2-(cald(a,b)/2)**2)

        #     x = mid_x-d*math.sin(angle)
        #     y = mid_y+d*math.cos(angle)
        #     return [x,y]

        # ans = 1
        # for i in range(len(points)):
        #     for j in range(len(points)):
        #         if i==j or cald(points[i],points[j])>2*r:
        #             continue
        #         cetr = GetCenter(points[i], points[j])
        #         tmp = 0
        #         for k in range(len(points)):
        #             if cald(cetr,points[k]) < r+1e-8:tmp += 1
        #         ans = max(ans,tmp)
        # return ans

        def get_dis(a, b, point):
            x, y = point[0], point[1]
            ds = abs(a - x) ** 2 + abs(b - y) ** 2
            return math.sqrt(ds)

        def get_circle(x1, y1, x2, y2, r):
            midx = (x1 + x2) / 2.0
            midy = (y1 + y2) / 2.0
            angle = math.atan2(float(y2 - y1), float(x2 - x1))
            d = math.sqrt(r ** 2 - get_dis(x1, y1, [midx, midy]) ** 2)
            cx = midx + d * math.sin(angle)
            cy = midy - d * math.cos(angle)
            return cx, cy

        max_count = 1
        for i in range(len(points)):
            for j in range(len(points)):
                if j == i:
                    continue

                if get_dis(points[j][0], points[j][1], points[i]) > 2 * r:
                    continue
                px, py = get_circle(points[j][0], points[j][1], points[i][0], points[i][1], r)
                count = 0
                # print(px, py)
                for point in points:
                    is_in = get_dis(point[0], point[1], [px, py]) <= (r + 1e-8)
                    # print(get_dis(point[0], point[1], [px,py]))
                    if is_in:
                        count += 1
                # print(count)
                max_count = max(max_count, count)
        return max_count

# tips

'''
If there is an optimal solution, you can always move the circle so that two points lie on the boundary of the circle.
When the radius is fixed, you can find either 0 or 1 or 2 circles that pass two given points at the same time.
Loop for each pair of points and find the center of the circle, after that count the number of points inside the circle.
'''
