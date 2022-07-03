# encoding=utf8

'''
556. Next Greater Element III
Given a positive integer n, find the smallest integer which has exactly the same digits existing in the integer n and is greater in value than n. If no such positive integer exists, return -1.

Note that the returned integer should fit in 32-bit integer, if there is a valid answer but it does not fit in 32-bit integer, return -1.

 

Example 1:

Input: n = 12
Output: 21
Example 2:

Input: n = 21
Output: -1
 

Constraints:

1 <= n <= 231 - 1
'''

class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 10019876
        if n > 2**31-1:
            return -1
        def next_p(nums):
            if len(nums) < 2:
                return nums
            i = len(nums) - 2
            while i >= 0:
                if nums[i] < nums[i+1]:
                    j = i+1
                    while j < len(nums) and nums[i] < nums[j]:
                        j += 1
                    nums[i], nums[j-1] = nums[j-1], nums[i]

                    break
                i -= 1

            nums[i+1:] = nums[i+1:][::-1]
            
            return nums

        def n_to_list(n):
            res = []
            while n:
                res.append(n%10)
                n /= 10
            return res[::-1]

        def list_to_n(l):
            res = 0
            tmp = 0
            while l:
                x = l.pop(0)
                res = tmp + x
                tmp = res * 10
            return res

        next_n = list_to_n(next_p(n_to_list(n)))
        if next_n <= n or next_n > (2**31-1):
            return -1
        return next_n

      
