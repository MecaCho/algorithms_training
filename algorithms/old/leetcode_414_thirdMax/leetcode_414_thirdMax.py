class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sorted(set(nums), reverse=True)[2] if len(set(nums)) >= 3 else sorted(nums, reverse=True)[0]


class Solution1(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_third = [float("-inf")]*3

        for num in nums:
            if num in min_third:
                continue
            if num > min_third[0]:
                min_third = [num, min_third[0], min_third[1]]
            elif num > min_third[1]:
                min_third = [min_third[0], num, min_third[1]]
            elif num > min_third[2]:
                min_third[2] = num
        return min_third[2] if len(set(nums)) >= 3 else min_third[0]


if __name__ == '__main__':
    demo = Solution()
    print demo.thirdMax([3, 9, 100])

    demo = Solution1()
    print demo.thirdMax([3, 100, 10, 99])
