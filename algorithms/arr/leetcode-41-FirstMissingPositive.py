'''
41. 缺失的第一个正数
给你一个未排序的整数数组，请你找出其中没有出现的最小的正整数。



示例 1:

输入: [1,2,0]
输出: 3
示例 2:

输入: [3,4,-1,1]
输出: 2
示例 3:

输入: [7,8,9,11,12]
输出: 1


提示：

你的算法的时间复杂度应为O(n)，并且只能使用常数级别的额外空间。

41. First Missing Positive
Given an unsorted integer array, find the smallest missing positive integer.

Example 1:

Input: [1,2,0]
Output: 3
Example 2:

Input: [3,4,-1,1]
Output: 2
Example 3:

Input: [7,8,9,11,12]
Output: 1
Note:

Your algorithm should run in O(n) time and uses constant extra space.
'''

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        i = 0
        while i < len(nums):
            # print(i, nums[i], nums)
            while nums[i] >= 1 and nums[i] < len(nums) and nums[nums[i]-1] != nums[i]:
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]

            i += 1

        res = 0
        while res < len(nums):
            if nums[res] != res+1:
                return res+1
            res += 1
        # print(res)
        return len(nums) + 1


# 变形题


def find_missd_min_num(nums):
    if not nums:
        return None

    i = 0
    while i < len(nums):
        print(i, nums[i], nums)
        while nums[i] >= 0 and nums[i] < len(nums) and nums[i] != i:
            nums[nums[i]], nums[i] = nums[i], nums[nums[i]]

        i += 1

    for i in range(len(nums)):
        if nums[i] != i:
            return i


if __name__ == '__main__':
    res = find_missd_min_num(nums=[10,2,3,4,5,7, 1,0])
    print(res)
# tips

'''
Think about how you would solve the problem in non-constant space. Can you apply that logic to the existing space?

We don't care about duplicates or non-positive integers

Remember that O(2n) = O(n)
'''