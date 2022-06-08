# encoding=utf8

'''
1037. Valid Boomerang
Given an array points where points[i] = [xi, yi] represents a point on the X-Y plane, return true if these points are a boomerang.

A boomerang is a set of three points that are all distinct and not in a straight line.

 

Example 1:

Input: points = [[1,1],[2,3],[3,2]]
Output: true
Example 2:

Input: points = [[1,1],[2,2],[3,3]]
Output: false
 

Constraints:

points.length == 3
points[i].length == 2
0 <= xi, yi <= 100
'''

# golang

'''
func isBoomerang(points [][]int) bool {
    a_x,a_y := points[0][0], points[0][1]
    b_x,b_y := points[1][0], points[1][1]
    c_x,c_y := points[2][0], points[2][1]
    return (a_y - c_y) * (b_x - c_x) != (b_y - c_y) * (a_x - c_x) 
}
'''

