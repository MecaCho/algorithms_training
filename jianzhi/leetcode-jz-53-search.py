
'''
面试题53 - I. 在排序数组中查找数字 I
统计一个数字在排序数组中出现的次数。



示例 1:

输入: nums = [5,7,7,8,8,10], target = 8
输出: 2
示例 2:

输入: nums = [5,7,7,8,8,10], target = 6
输出: 0


限制：

0 <= 数组长度 <= 50000



注意：本题与主站 34 题相同（仅返回值不同）：https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/
'''


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def get_count(loc):
            l, r = loc -1, loc + 1
            count = 1
            while (l >= 0 and nums[l] == target) or (r < len(nums) and nums[r] == target):
                if l >= 0 and nums[l] == target:
                    count += 1
                    l -= 1
                if r < len(nums) and nums[r] == target:
                    count += 1
                    r += 1
            return count

        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) / 2
            if target > nums[mid]:
                l = mid + 1
            elif target < nums[mid]:
                r = mid - 1
            else:
                return get_count(mid)
        return 0