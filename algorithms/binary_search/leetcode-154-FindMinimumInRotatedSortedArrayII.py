# encoding=utf8

'''
154. 寻找旋转排序数组中的最小值 II
假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

请找出其中最小的元素。

注意数组中可能存在重复的元素。

示例 1：

输入: [1,3,5]
输出: 1
示例 2：

输入: [2,2,2,0,1]
输出: 0
说明：

这道题是 寻找旋转排序数组中的最小值 的延伸题目。
允许重复会影响算法的时间复杂度吗？会如何影响，为什么？

154. Find Minimum in Rotated Sorted Array II
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

The array may contain duplicates.

Example 1:

Input: [1,3,5]
Output: 1
Example 2:

Input: [2,2,2,0,1]
Output: 0
Note:

This is a follow up problem to Find Minimum in Rotated Sorted Array.
Would allow duplicates affect the run-time complexity? How and why?
'''

# 执行用时 :
# 24 ms
# , 在所有 Python 提交中击败了
# 71.10%
# 的用户
# 内存消耗 :
# 12.8 MB
# , 在所有 Python 提交中击败了
# 33.33%
# 的用户
# 双指针

class Solution(object):
    def minArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i,j = 0, len(nums)-1
        while i < j:
            if nums[i+1] >= nums[i]:
                i += 1
            else:
                return nums[i+1]

            if nums[j-1] <= nums[j]:
                j -= 1
            else:
                return nums[j]

        return nums[0] if nums else None



# 二分法


class Solution1_(object):
    def minArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i, j = 0, len(nums) - 1
        while i < j:
            m = (i + j) // 2
            if nums[m] > nums[j]: i = m + 1
            elif nums[m] < nums[j]: j = m
            else: j -= 1
        return nums[i]

# 执行用时 :
# 28 ms
# , 在所有 Python 提交中击败了
# 55.78%
# 的用户
# 内存消耗 :
# 12.8 MB
# , 在所有 Python 提交中击败了
# 33.33%
# 的用户
class Solution1(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #             # 由于原始数组是递增，那么旋转之后，旋转点左右的两部分仍然是递增的
            # # 这里记原始数组中旋转点左侧的数组为 A，原始数组中旋转点右侧的数组为 B
            # # 旋转之后有原来的 AB 变成了 BA，
            # if nums[mid] > nums[r]:
            #     # 说明mid在原来的 B 部分
        i,j = 0, len(nums)-1
        while i < j:
            # 旋转之后有原来的 AB 变成了 BA，
            mid = (i+j) // 2
            if nums[mid] > nums[j]:
                # 说明mid在原来的 B 部分
                i = mid + 1
            elif nums[mid] < nums[j]:
                # # 说明mid在原来的 A 部分
                j = mid
            else:
                j -= 1
        return nums[i] if nums else None



class Solution20210409(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r)/2
            num = nums[mid]
            if num > nums[r]:
                l = mid + 1
            elif num == nums[r]:
                r -= 1
            else:
                r = mid
        return nums[l]


if __name__ == '__main__':
    demo = Solution20210409()
    res = demo.findMin([2,2,2,2,3,0,1,2,2,2])
    print res
