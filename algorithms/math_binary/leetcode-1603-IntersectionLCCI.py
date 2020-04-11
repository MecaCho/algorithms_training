'''
面试题 16.03. 交点
给定两条线段（表示为起点start = {X1, Y1}和终点end = {X2, Y2}），如果它们有交点，请计算其交点，没有交点则返回空值。

要求浮点型误差不超过10^-6。若有多个交点（线段重叠）则返回 X 值最小的点，X 坐标相同则返回 Y 值最小的点。

 

示例 1：

输入：
line1 = {0, 0}, {1, 0}
line2 = {1, 1}, {0, -1}
输出： {0.5, 0}
示例 2：

输入：
line1 = {0, 0}, {3, 3}
line2 = {1, 1}, {2, 2}
输出： {1, 1}
示例 3：

输入：
line1 = {0, 0}, {1, 1}
line2 = {1, 0}, {2, 1}
输出： {}，两条线段没有交点
 

提示：

坐标绝对值不会超过 2^7
输入的坐标均是有效的二维坐标

相关企业：华为、字节跳动

面试题 16.03. Intersection LCCI
Given two straight line segments (represented as a start point and an end point), compute the point of intersection, if any. If there's no intersection, return an empty array.

The absolute error should not exceed 10^-6. If there are more than one intersections, return the one with smallest X axis value. If there are more than one intersections that have same X axis value, return the one with smallest Y axis value.
Example 1:

Input: 
line1 = {0, 0}, {1, 0}
line2 = {1, 1}, {0, -1}
Output:  {0.5, 0}
Example 2:

Input: 
line1 = {0, 0}, {3, 3}
line2 = {1, 1}, {2, 2}
Output:  {1, 1}
Example 3:

Input: 
line1 = {0, 0}, {1, 1}
line2 = {1, 0}, {2, 1}
Output:  {}  (no intersection)
Note:

The absolute value of coordinate value will not exceed 2^7.
All coordinates are valid 2D coordinates.
'''






class Solution(object):
    def intersection(self, start1, end1, start2, end2):
        """
        :type start1: List[int]
        :type end1: List[int]
        :type start2: List[int]
        :type end2: List[int]
        :rtype: List[float]
        """
        def get_line(start, end):
            x1, y1 = start
            x2, y2 = end
            return (y2 - y1, x1 - x2, x2 * y1 - x1 * y2)

        def in_line(x, y):
            for s, e in ((start1, end1), (start2, end2)):
                mnx = min(s[0], e[0])
                mxx = max(s[0], e[0])
                mny = min(s[1], e[1])
                mxy = max(s[1], e[1])
                if not (mnx <= x <= mxx and mny <= y <= mxy):
                    return False
            return True

        a1, b1, c1 = get_line(start1, end1)
        a2, b2, c2 = get_line(start2, end2)
        if a1 * b2 == a2 * b1:
            # 平行
            if c1 != c2:
                return []
            # 共线, 需要额外判断交点是否在两条线段上
            res = []
            for x,y in (start1, end1, start2, end2):
                # print(x,y)
                if in_line(x, y):
                    if not res or x < res[0] or x == res[0] and y < res[1]:
                        res = [x,y]
            return res

        x = float(c2 * b1 - c1 * b2) / float(a1 * b2 - a2 * b1)
        y = float(c1 * a2 - c2 * a1) / float(a1 * b2 - a2 * b1)
        # print(x, y)
        if in_line(x, y):
            return [x, y]
        else:
            return []

