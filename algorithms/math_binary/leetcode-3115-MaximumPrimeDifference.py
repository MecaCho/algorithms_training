# encoding=utf8

'''

3115. Maximum Prime Difference

You are given an integer array nums.

Return an integer that is the maximum distance between the indices of two (not necessarily different) prime numbers in nums.

 

Example 1:

Input: nums = [4,2,9,5,3]

Output: 3

Explanation: nums[1], nums[3], and nums[4] are prime. So the answer is |4 - 1| = 3.

Example 2:

Input: nums = [4,8,2,8]

Output: 0

Explanation: nums[2] is prime. Because there is just one prime number, the answer is |2 - 2| = 0.

 

Constraints:

1 <= nums.length <= 3 * 105
1 <= nums[i] <= 100
The input is generated such that the number of prime numbers in the nums is at least one.
'''

class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:

        def is_prime(num):
            # if num == 1:
            #     return 0
            # for i in range(2, num//2+1):
            #     if num % i == 0:
            #         return 0
            # return 1
            primes = {
            2, 3, 5, 7, 11,
            13, 17, 19, 23, 29,
            31, 37, 41, 43, 47,
            53, 59, 61, 67, 71,
            73, 79, 83, 89, 97
            }
            return num in primes

        # print(is_prime(4))
        min_prime_index, max_prime_index = -1, -1
        for i, num in enumerate(nums):
            if is_prime(num):
                if min_prime_index == -1:
                    min_prime_index = i
                max_prime_index = i
        print(min_prime_index, max_prime_index)
        return max_prime_index - min_prime_index


