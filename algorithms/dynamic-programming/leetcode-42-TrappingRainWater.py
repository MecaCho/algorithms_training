# encoding=utf8



'''
42. Trapping Rain Water
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6

42. 接雨水
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。



上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 感谢 Marcos 贡献此图。

示例:

输入: [0,1,0,2,1,0,1,3,2,1,2,1]
输出: 6
'''

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        length = len(height)
        max_left = [height[0]]
        max_right = [0 for i in range(length-1)] + [height[-1]]
        for i in range(1, length):
            max_left.append(max(max_left[i-1], height[i-1]))
            j = length - 1 - i

            max_right[j] = max(max_right[j+1], height[j+1])

        print(max_left, max_right)
        res = 0
        for i in range(1, length - 1):

            res += max(min(max_left[i], max_right[i]) - height[i], 0)
        return res


class Solution20210402(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        length = len(height)

        max_left = [height[0]]
        max_right = [0 for _ in range(length - 1)] + [height[-1]]

        for i in range(1, length):
            j = length - i - 1
            max_left.append(max(max_left[i - 1], height[i - 1]))
            max_right[j] = max(height[j + 1], max_right[j + 1])

        print(max_left, max_right)

        res = 0
        for i in range(length):
            res += max(0, min(max_right[i] - height[i], max_left[i] - height[i]))

        return res

