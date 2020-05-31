

'''
5425. 切割后面积最大的蛋糕
矩形蛋糕的高度为 h 且宽度为 w，给你两个整数数组 horizontalCuts 和 verticalCuts，其中 horizontalCuts[i] 是从矩形蛋糕顶部到第  i 个水平切口的距离，类似地， verticalCuts[j] 是从矩形蛋糕的左侧到第 j 个竖直切口的距离。

请你按数组 horizontalCuts 和 verticalCuts 中提供的水平和竖直位置切割后，请你找出 面积最大 的那份蛋糕，并返回其 面积 。由于答案可能是一个很大的数字，因此需要将结果对 10^9 + 7 取余后返回。



示例 1：



输入：h = 5, w = 4, horizontalCuts = [1,2,4], verticalCuts = [1,3]
输出：4
解释：上图所示的矩阵蛋糕中，红色线表示水平和竖直方向上的切口。切割蛋糕后，绿色的那份蛋糕面积最大。
示例 2：



输入：h = 5, w = 4, horizontalCuts = [3,1], verticalCuts = [1]
输出：6
解释：上图所示的矩阵蛋糕中，红色线表示水平和竖直方向上的切口。切割蛋糕后，绿色和黄色的两份蛋糕面积最大。
示例 3：

输入：h = 5, w = 4, horizontalCuts = [3], verticalCuts = [3]
输出：9


提示：

2 <= h, w <= 10^9
1 <= horizontalCuts.length < min(h, 10^5)
1 <= verticalCuts.length < min(w, 10^5)
1 <= horizontalCuts[i] < h
1 <= verticalCuts[i] < w
题目数据保证 horizontalCuts 中的所有元素各不相同
题目数据保证 verticalCuts 中的所有元素各不相同


5425. Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts
Given a rectangular cake with height h and width w, and two arrays of integers horizontalCuts and verticalCuts where horizontalCuts[i] is the distance from the top of the rectangular cake to the ith horizontal cut and similarly, verticalCuts[j] is the distance from the left of the rectangular cake to the jth vertical cut.

Return the maximum area of a piece of cake after you cut at each horizontal and vertical position provided in the arrays horizontalCuts and verticalCuts. Since the answer can be a huge number, return this modulo 10^9 + 7.



Example 1:



Input: h = 5, w = 4, horizontalCuts = [1,2,4], verticalCuts = [1,3]
Output: 4
Explanation: The figure above represents the given rectangular cake. Red lines are the horizontal and vertical cuts. After you cut the cake, the green piece of cake has the maximum area.
Example 2:



Input: h = 5, w = 4, horizontalCuts = [3,1], verticalCuts = [1]
Output: 6
Explanation: The figure above represents the given rectangular cake. Red lines are the horizontal and vertical cuts. After you cut the cake, the green and yellow pieces of cake have the maximum area.
Example 3:

Input: h = 5, w = 4, horizontalCuts = [3], verticalCuts = [3]
Output: 9


Constraints:

2 <= h, w <= 10^9
1 <= horizontalCuts.length < min(h, 10^5)
1 <= verticalCuts.length < min(w, 10^5)
1 <= horizontalCuts[i] < h
1 <= verticalCuts[i] < w
It is guaranteed that all elements in horizontalCuts are distinct.
It is guaranteed that all elements in verticalCuts are distinct.
'''


class Solution(object):
    def maxArea(self, h, w, horizontalCuts, verticalCuts):
        """
        :type h: int
        :type w: int
        :type horizontalCuts: List[int]
        :type verticalCuts: List[int]
        :rtype: int
        """
        horizontalCuts += [0, h]
        horizontalCuts = sorted(horizontalCuts)
        h_s = [horizontalCuts[i] - horizontalCuts[i - 1] for i in range(1, len(horizontalCuts))]
        max_h = max(h_s)

        verticalCuts += [0, w]
        verticalCuts = sorted(verticalCuts)
        v_s = [verticalCuts[i] - verticalCuts[i - 1] for i in range(1, len(verticalCuts))]

        # print(h_s, v_s)

        max_v = max(v_s)

        return (max_h * max_v) % (10 ** 9 + 7)


# golang solutions

'''
func maxArea(h int, w int, horizontalCuts []int, verticalCuts []int) int {
	horizontalCuts = append(horizontalCuts, 0, h)

	verticalCuts = append(verticalCuts, 0, w)

    sort.Ints(horizontalCuts)

	max_h := 0
	hs := []int{}
	for i, v := range horizontalCuts {
		if i > 0 {
			h := v - horizontalCuts[i-1]
			if h > max_h {
				max_h = h
			}
			hs = append(hs, h)
		}
	}

    sort.Ints(verticalCuts)
	max_v := 0
	vs := []int{}
	for i, val := range verticalCuts {
		if i > 0 {
			v := val - verticalCuts[i-1]
			if v > max_v {
				max_v = v
			}
			vs = append(vs, v)
		}
	}

    // fmt.Println(horizontalCuts, verticalCuts)

	return (max_h * max_v) % (int(math.Pow10(9)) + 7)

}
'''


# tips

'''
Sort the arrays, then compute the maximum difference between two consecutive elements for horizontal cuts and vertical cuts.

The answer is the product of these maximum values in horizontal cuts and vertical cuts.
'''