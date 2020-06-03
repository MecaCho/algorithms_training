
'''
面试题57. 和为s的两个数字
输入一个递增排序的数组和一个数字s，在数组中查找两个数，使得它们的和正好是s。如果有多对数字的和等于s，则输出任意一对即可。



示例 1：

输入：nums = [2,7,11,15], target = 9
输出：[2,7] 或者 [7,2]
示例 2：

输入：nums = [10,26,30,31,47,60], target = 40
输出：[10,30] 或者 [30,10]


限制：

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^6
'''


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_map = {}
        for num in nums:
            if num in hash_map:
                return [hash_map[num], num]
            else:
                hash_map[target-num] = num
        return []


# 双指针法
class Solution1(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # hash_map = {}
        # for num in nums:
        #     if num in hash_map:
        #         return [hash_map[num], num]
        #     else:
        #         hash_map[target-num] = num
        # return []

        i, j = 0, len(nums) - 1
        while i < j:
            sum_ = nums[i] + nums[j]
            if sum_ > target:
                j -= 1
            elif sum_ < target:
                i += 1
            else:
                return [nums[i], nums[j]]


def TwoSum(s1, s2, add=True):
    print(s1, s2)
    len1 = len(s1)
    len2 = len(s2)

    i = len1 - 1
    j = len2 - 1
    pre = 0
    res = ""
    while i >= 0 or j >= 0:
        num1 = int(s1[i]) if i >= 0 else 0
        num2 = int(s2[j]) if j >= 0 else 0
        flag = False
        if not add:
            if num2 > num1:
                num1 += 10
                flag = True
            num2 = 0 - num2
        # print(num1, num2, pre)

        new_sum = num1 + num2 + pre

        num = new_sum % 10
        if flag:
            pre -= 1
        else:
            pre = int(new_sum / 10)

        res = str(num) + res
        i -= 1
        j -= 1
    # print(res)
    return res


def NewTwoSum(s1, s2):
    if s1[0] == "-" and s2[0] == "-":
        return "-"+TwoSum(s1[1:], s2[1:])
    elif s1[0] == "-":
        return TwoSum(s2, s1[1:], False)
    elif s2[0] == "-":
        return TwoSum(s1, s2[1:], False)
    return TwoSum(s1, s2)

if __name__ == '__main__':
    res = NewTwoSum("-3", "1456676756565000")
    print(res)
