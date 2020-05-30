'''

84. 柱状图中最大的矩形
给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。

求在该柱状图中，能够勾勒出来的矩形的最大面积。





以上是柱状图的示例，其中每个柱子的宽度为 1，给定的高度为 [2,1,5,6,2,3]。





图中阴影部分为所能勾勒出的最大矩形面积，其面积为 10 个单位。



示例:

输入: [2,1,5,6,2,3]
输出: 10

84. Largest Rectangle in Histogram
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.




Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].




The largest rectangle is shown in the shaded area, which has area = 10 unit.



Example:

Input: [2,1,5,6,2,3]
Output: 10
'''






class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        # 超时
        # res = 0
        # for i in range(len(heights)):
        #     min_h = heights[i]
        #     for j in range(i, len(heights)):
        #         min_h = min(min_h, heights[j])
        #         res = max((j-i+1) * min_h, res)

        # return res

        res = 0

        stack = []
        heights.append(0)
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                index = stack.pop()
                loc = 0 if not stack else stack[-1] + 1
                res = max(res, (i-loc)*heights[index])
            stack.append(i)
        return res



# golang

'''
func largestRectangleArea(heights []int) int {

    res := 0
    for i := range heights{
        min_h := heights[i]
        for j := i; j < len(heights);j++{
            if heights[j] < min_h{
                min_h = heights[j]
            }
            // fmt.Println(j, i, heights[j])
            new_res := (j-i+1) * min_h
            if new_res > res{
                res = new_res
            }
        }
    }
    return res
}

func largestRectangleArea(heights []int) int {

    res := 0
    // for i := range heights{
    //     min_h := heights[i]
    //     for j := i; j < len(heights);j++{
    //         if heights[j] < min_h{
    //             min_h = heights[j]
    //         }
    //         // fmt.Println(j, i, heights[j])
    //         new_res := (j-i+1) * min_h
    //         if new_res > res{
    //             res = new_res
    //         }
    //     }
    // }
    // return res

	stack := []int{}
    heights =append(heights, 0)
	for i := range heights {
		
		for len(stack) > 0 && heights[i] < heights[stack[len(stack)-1]]{
            // fmt.Println(stack)
			// index := stack[len(stack)-1]
			loc := 0
			if len(stack) > 1{
				loc = stack[len(stack) - 2] + 1
			}
			
			new_res := (i-loc) * heights[stack[len(stack)-1]]
			if new_res > res{
				res = new_res
			}
			stack = stack[:len(stack)-1]
		}
		stack = append(stack, i)
	}

	return res

}
'''