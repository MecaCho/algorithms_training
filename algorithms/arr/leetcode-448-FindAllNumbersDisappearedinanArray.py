'''
448. 找到所有数组中消失的数字
给定一个范围在  1 ≤ a[i] ≤ n ( n = 数组大小 ) 的 整型数组，数组中的元素一些出现了两次，另一些只出现一次。

找到所有在 [1, n] 范围之间没有出现在数组中的数字。

您能在不使用额外空间且时间复杂度为O(n)的情况下完成这个任务吗? 你可以假定返回的数组不算在额外空间内。

示例:

输入:
[4,3,2,7,8,2,3,1]

输出:
[5,6]

448. Find All Numbers Disappeared in an Array
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
'''



class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)):
            # print(i, nums)
            while 1 <= nums[i] <= len(nums) and nums[nums[i] - 1] != nums[i]:
                # print(nums[i], nums[nums[i]-1], nums)
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

                # nums[i], nums[nums[i] - 1]  = nums[nums[i] - 1], nums[i]
                # print(nums[i], nums[nums[i]-1], nums)

        res = []
        for i in range(len(nums)):
            if nums[i] != i + 1:
                res.append(i + 1)
        return res


# tips

'''
This is a really easy problem if you decide to use additional memory. For those trying to write an initial solution using additional memory, think counters!

However, the trick really is to not use any additional space than what is already available to use. Sometimes, multiple passes over the input array help find the solution. However, there's an interesting piece of information in this problem that makes it easy to re-use the input array itself for the solution.

The problem specifies that the numbers in the array will be in the range [1, n] where n is the number of elements in the array. Can we use this information and modify the array in-place somehow to find what we need?
'''