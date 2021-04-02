# encoding=utf8

'''
面试题 17.21. Volume of Histogram LCCI
Imagine a histogram (bar graph). Design an algorithm to compute the volume of water it could hold if someone poured water across the top. You can assume that each histogram bar has width 1.



The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6


面试题 17.21. 直方图的水量
给定一个直方图(也称柱状图)，假设有人从上面源源不断地倒水，最后直方图能存多少水量?直方图的宽度为 1。



上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的直方图，在这种情况下，可以接 6 个单位的水（蓝色部分表示水）。 感谢 Marcos 贡献此图。

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
        max_right = [0 for _ in range(length - 1)] + [height[-1]]

        for i in range(1, length):
            j = length - i - 1
            max_left.append(max(max_left[i - 1], height[i - 1]))
            max_right[j] = max(height[j + 1], max_right[j + 1])

        # print(max_left, max_right)

        res = 0
        for i in range(length):
            res += max(0, min(max_right[i] - height[i], max_left[i] - height[i]))

        return res
