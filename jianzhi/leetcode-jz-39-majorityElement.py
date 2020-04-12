'''
面试题39. 数组中出现次数超过一半的数字
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。



你可以假设数组是非空的，并且给定的数组总是存在多数元素。



示例 1:

输入: [1, 2, 3, 2, 2, 2, 5, 4, 2]
输出: 2


限制：

1 <= 数组长度 <= 50000



注意：本题与主站 169 题相同：https://leetcode-cn.com/problems/majority-element/
'''






class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sorted(nums)[len(nums)//2] if nums else 0


class Solution1(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = nums[0] if nums else 0
        count = 0
        for num in nums:
            if count == 0:
                res = num
            if num == res:
                count += 1
            else:
                count -= 1
        return res


class Solution1_(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        votes, count = 0, 0
        x = None
        for num in nums:
            if votes == 0:
                x = num
            votes += 1 if num == x else -1
        # 验证 x 是否为众数
        for num in nums:
            if num == x: count += 1
        return x if count > len(nums) // 2 else 0 # 当无众数时返回 0
