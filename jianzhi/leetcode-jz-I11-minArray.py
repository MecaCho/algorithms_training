
'''
面试题11. 旋转数组的最小数字
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。例如，数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1。

示例 1：

输入：[3,4,5,1,2]
输出：1
示例 2：

输入：[2,2,2,0,1]
输出：0
注意：本题与主站 154 题相同：https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array-ii/
'''


class Solution(object):
    def minArray(self, numbers):
        """
        :type numbers: List[int]
        :rtype: int
        """
        i,j = 0, len(numbers)-1
        while i < j:
            if numbers[i+1] >= numbers[i]:
                i += 1
            else:
                return numbers[i+1]
            if numbers[j-1] <= numbers[j]:
                j -= 1
            else:
                return numbers[j]
        # print(i, j)
        return numbers[0] if numbers else None

# 二分法
class Solution1(object):
    def minArray(self, numbers):
        """
        :type numbers: List[int]
        :rtype: int
        """
        i, j = 0, len(numbers) - 1
        while i < j:
            m = (i + j) // 2
            if numbers[m] > numbers[j]: i = m + 1
            elif numbers[m] < numbers[j]: j = m
            else: j -= 1
        return numbers[i]

class Solution1_(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #             # 由于原始数组是递增，那么旋转之后，旋转点左右的两部分仍然是递增的
            # # 这里记原始数组中旋转点左侧的数组为 A，原始数组中旋转点右侧的数组为 B
            # # 旋转之后有原来的 AB 变成了 BA，
            # if numbers[mid] > numbers[r]:
            #     # 说明mid在原来的 B 部分
        i,j = 0, len(nums)-1
        while i < j:
            mid = (i+j) // 2
            if nums[mid] > nums[j]:
                i = mid + 1
            elif nums[mid] < nums[j]:
                j = mid
            else:
                j -= 1
            # print(i, j)
        # print(i, j)
        return nums[i] if nums else None
