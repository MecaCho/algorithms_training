# encoding=utf8

'''
17.19. Missing Two LCCI
You are given an array with all the numbers from 1 to N appearing exactly once, except for two number that is missing. How can you find the missing number in O(N) time and 0(1) space?

You can return the missing numbers in any order.

Example 1:

Input: [1]
Output: [2,3]
Example 2:

Input: [2,3]
Output: [1,4]
Note:

nums.length <= 30000
'''

class Solution:
    def missingTwo(self, nums: List[int]) -> List[int]:
        xorsum = 0
        n = len(nums) + 2
        for num in nums:
            xorsum ^= num
        for i in range(1, n + 1):
            xorsum ^= i
        
        lsb = xorsum & (-xorsum)
        type1 = type2 = 0
        for num in nums:
            if num & lsb:
                type1 ^= num
            else:
                type2 ^= num
        for i in range(1, n + 1):
            if i & lsb:
                type1 ^= i
            else:
                type2 ^= i
        
        return [type1, type2]

