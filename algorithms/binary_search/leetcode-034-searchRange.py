'''

34. 在排序数组中查找元素的第一个和最后一个位置
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

你的算法时间复杂度必须是 O(log n) 级别。

如果数组中不存在目标值，返回 [-1, -1]。

示例 1:

输入: nums = [5,7,7,8,8,10], target = 8
输出: [3,4]
示例 2:

输入: nums = [5,7,7,8,8,10], target = 6
输出: [-1,-1]

34. Find First and Last Position of Element in Sorted Array
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]


34. 在排序数组中查找元素的第一个和最后一个位置
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

你的算法时间复杂度必须是 O(log n) 级别。

如果数组中不存在目标值，返回 [-1, -1]。

示例 1:

输入: nums = [5,7,7,8,8,10], target = 8
输出: [3,4]
示例 2:

输入: nums = [5,7,7,8,8,10], target = 6
输出: [-1,-1]
'''


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        j = len(nums) - 1
        res = [-1, -1]
        while i <= j:
            print(i, j, nums[i], nums[j])
            mid = (i + j) / 2
            if nums[mid] == target:
                l = r = mid
                while l-1 >=0 and nums[l-1] == target:
                    l -= 1
                while r+1 <= len(nums) -1 and nums[r+1] == target:
                    r += 1
                res = [l, r]
                break
            elif nums[mid] < target:
                i = mid + 1
            elif nums[mid] > target:
                j = mid - 1
        return res


class Solution1(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        left, right = -1, -1
        i, j = 0, len(nums) - 1
        while i < j:
            mid = (i + j) / 2
            if nums[mid] < target:
                i = mid + 1
            else:
                j = mid
        if i >= len(nums) or nums[i] != target:
            return [-1, -1]
        left = i

        i, j = 0, len(nums) - 1
        while i <= j:
            mid = (i + j) / 2
            if nums[mid] > target:
                j = mid - 1
            else:
                i = mid + 1
        right = i - 1

        return [left, right]


class Solution20201201(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        def where_left(nums, target):
            i, j = 0, len(nums) - 1
            while i < j:
                mid = (i + j) // 2
                # if nums[mid] == target:
                #     return mid
                if nums[mid] < target:
                    i = mid + 1
                else:
                    j = mid
            return i

        def where_right(nums, target):
            i, j = 0, len(nums) - 1
            while i < j:
                mid = (i + j+1) // 2
                # if nums[mid] == target:
                #     return mid
                if nums[mid] > target:
                    j = mid - 1
                else:
                    i = mid
            return j

        left = where_left(nums, target)
        if left >= len(nums) or nums[left] != target:
            return [-1, -1]
        right = where_right(nums, target)

        return [left, right]



if __name__ == '__main__':
    demo = Solution20201201()
    res = demo.searchRange([8,8,8,8,8,8,9], 8)
    print(res)
