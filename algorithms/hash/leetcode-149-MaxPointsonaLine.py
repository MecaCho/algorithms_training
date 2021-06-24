# encoding=utf8


'''
149. Max Points on a Line

Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, return the maximum number of points that lie on the same straight line.

 

Example 1:


Input: points = [[1,1],[2,2],[3,3]]
Output: 3
Example 2:


Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4
 

Constraints:

1 <= points.length <= 300
points[i].length == 2
-104 <= xi, yi <= 104
All the points are unique.

149. 直线上最多的点数

给你一个数组 points ，其中 points[i] = [xi, yi] 表示 X-Y 平面上的一个点。求最多有多少个点在同一条直线上。

 

示例 1：


输入：points = [[1,1],[2,2],[3,3]]
输出：3
示例 2：


输入：points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
输出：4
 

提示：

1 <= points.length <= 300
points[i].length == 2
-104 <= xi, yi <= 104
points 中的所有点 互不相同
'''

# golang solution

'''
func maxPoints(points [][]int) int {
    var ans int
    n := len(points)
    if n <= 2 {
        return n
    }
    for i, p := range points {
        if ans >= n-i || ans > n/2 {
            break
        }
        cnt := map[int]int{}
        for _, q := range points[i+1:] {
            x, y := p[0]-q[0], p[1]-q[1]
            if x == 0 {
                y = 1
            } else if y == 0 {
                x = 1
            } else {
                if y < 0 {
                    x, y = -x, -y
                }
                g := gcd(abs(x), abs(y))
                x /= g
                y /= g
            }
            cnt[y+x*20001]++
        }
        for _, c := range cnt {
            ans = max(ans, c+1)
        }
    }
    return ans
}

func max(a, b int) int{
    if a > b{
        return a
    }
    return b
}

func gcd(a, b int) int {
    for a != 0 {
        a, b = b%a, a
    }
    return b
}

func abs(x int) int {
    if x < 0 {
        return -x
    }
    return x
}
'''
