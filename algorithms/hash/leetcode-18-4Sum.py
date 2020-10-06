'''
18. 四数之和
给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。

注意：

答案中不可以包含重复的四元组。

示例：

给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。

满足要求的四元组集合为：
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]

18. 4Sum
Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]

'''


class Solution(object):

    def twoSum(self, nums, target):
        res = []
        hash_map = {}
        for i in range(len(nums)):
            if nums[i] in hash_map:
                res.append((hash_map[nums[i]], nums[i]))
            else:
                hash_map[target -nums[i]] = nums[i]
        return res

    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        pre = None
        for i in range(len(nums)):
            for j in range( i +1, len(nums)):
                sum_ = nums[i] + nums[j]
                if pre == (nums[i], nums[j]):
                    continue

                t_s = self.twoSum(nums[ j +1:], target - sum_)
                if not t_s:
                    continue
                for t in t_s:
                    new_res = sorted((nums[i], nums[j], t[0], t[1]))
                    if new_res not in res:
                        res.append(new_res)
                pre = (nums[i], nums[j])
        return res


class Solution20201005(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.vals = []
        nums.sort()
        print(nums)
        def bk(path, start, sum_):
            if len(path) > 4:
                return
            if len(path) == 4:
                if sum_ == target:
                    self.vals.append(path)
                    return
                else:
                    return
            # print(path, sum_, start)
            # if start >= len(nums) or nums[start] > target - sum_:
                # return
            print(len(path), start, sum_)
            for i in range(start, len(nums)):
                if i == start or nums[i] != nums[i-1]:
                    bk(path+[nums[i]], i+1, sum_+nums[i])
        bk([], 0, 0)
        return self.vals


# test cases
# [1,-2,-5,-4,-3,3,3,5]
# -11
# [-3,-1,0,2,4,5]
# 2
# [-497,-473,-465,-462,-450,-445,-411,-398,-398,-392,-382,-376,-361,-359,-353,-347,-329,-328,-317,-307,-273,-230,
# -228,-227,-217,-199,-190,-175,-155,-151,-122,-102,-97,-96,-95,-87,-85,-84,-73,-71,-51,-50,-39,-24,-19,-1,-1,7,22,
# 25,27,37,40,43,45,51,72,91,97,108,119,121,122,123,127,156,166,171,175,180,203,211,217,218,224,231,245,293,297,299,
# 300,318,326,336,353,358,376,391,405,423,445,451,459,464,471,486,487,488]
# 2251


import time


if __name__ == '__main__':
    test_cases = [
        ([1, -2, -5, -4, -3, 3, 3, 5], -11),
        ([-3, -1, 0, 2, 4, 5], 2),
        ([
            -497, -473, -465, -462, -450, -445, -411, -398, -398, -392, -382, -376, -361, -359, -353, -347, -329,
            -328, -317, -307, -273, -230, -228, -227, -217, -199, -190, -175, -155, -151, -122, -102, -97, -96, -95,
            -87, -85, -84, -73, -71, -51, -50, -39, -24, -19, -1, -1, 7, 22, 25, 27, 37, 40, 43, 45, 51, 72, 91, 97,
            108, 119, 121, 122, 123, 127, 156, 166, 171, 175, 180, 203, 211, 217, 218, 224, 231, 245, 293, 297, 299, 300, 318, 326, 336, 353, 358, 376, 391, 405, 423, 445, 451, 459, 464, 471, 486, 487, 488]
        ,2251)
        ]
    demo = Solution20201005()
    for nums, t in test_cases:
        t0 = time.time()
        res = demo.fourSum(nums, t)
        print(res)
        print(time.time() - t0)
