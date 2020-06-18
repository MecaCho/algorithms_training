'''
面试题21. 调整数组顺序使奇数位于偶数前面
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。



示例：

输入：nums = [1,2,3,4]
输出：[1,3,2,4]
注：[3,1,2,4] 也是正确的答案之一。


提示：

1 <= nums.length <= 50000
1 <= nums[i] <= 10000
'''



class Solution(object):
    def exchange(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        i,j = 0,0
        while j < len(nums) and i < len(nums):
            if nums[i] % 2 == 1:
                i += 1
            else:
                if nums[j] % 2 == 1:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            j += 1

        return nums

class Solution1(object):
    def exchange(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        i, j = 0, 0
        while j < len(nums):
            while i < len(nums) and nums[i] % 2 == 1:
                i += 1
                j += 1

            if i < len(nums) and j < len(nums) and nums[i] % 2 == 0 and nums[j] % 2 == 1:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            j += 1
        return nums

class Solution2(object):
    def exchange(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        i, j = 0, 0
        while j < len(nums):
            while j < len(nums) and nums[j] % 2 == 1:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
                i += 1

            j += 1
        return nums
