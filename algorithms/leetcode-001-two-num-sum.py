class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_dict = dict()
        for i, num in enumerate(nums):
            if num_dict.get(target - num) is not None:
                return num_dict[target - num], i
            num_dict[num] = i
        return None
