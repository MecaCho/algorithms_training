# encoding=utf8

'''
47. Permutations II

Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

 

Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
Example 2:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
 

Constraints:

1 <= nums.length <= 8
-10 <= nums[i] <= 10

47. 全排列 II
给定一个可包含重复数字的序列，返回所有不重复的全排列。

示例:

输入: [1,1,2]
输出:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]

'''


class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        self.vals = []
        def bk(nums, res):
            if not nums:
                self.vals.append(res)
            pre = None
            for i in range(len(nums)):
                if pre is None or pre != nums[i]:
                    bk(nums[:i]+nums[i+1:], res+[nums[i]])
                pre = nums[i]
        bk(nums, [])
        return self.vals




class Solution1(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.vals = []
        # self.hash_map = {}
        def backtrack(nums, new_per):
            if not nums:
                # if new_per not in self.vals:
                self.vals.append(new_per)
            else:
                val = nums[0]
                new_nums = nums[1:]
                i = 0
                pre = None
                for i in range(len(new_per)+1):
                    # if val not in self.hash_map:
                    if pre is None or val != pre:
                        pre = new_per[i] if i < len(new_per) else None
                        backtrack(new_nums, new_per[:i] + [val] + new_per[i:])
                        # self.hash_map[val] = True

        backtrack(nums, [])
        # print(len(self.vals))
        return self.vals


class Solution20200918(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.vals = []
        length = len(nums)
        nums.sort()
        # def bk(arr):
        #     if len(arr) == length:
        #         self.vals.append(arr)
        #         return
        #     for i in range(length):
        #         if nums[i] != nums[i-1]:
        #             bk(arr+[nums[i]])
        # bk([])
        # return self.vals
        def bk(nums, temp_pers):
        # conditions
            if not nums:
                self.vals.append(temp_pers)
            for i in range(len(nums)):
                # if nums contain duplicates
                if i == 0 or nums[i] != nums[i-1]:
                    bk(nums[:i]+nums[i+1:], temp_pers+[nums[i]])
        bk(nums, [])
        return self.vals

'''
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.vals = []
        # self.hash_map = {}
        def backtrack(nums, new_per):
            if not nums:
                # if new_per not in self.vals:
                self.vals.append(new_per)
            else:
                val = nums[0]
                new_nums = nums[1:]
                i = 0
                pre = None
                for i in range(len(new_per)+1):
                    # if val not in self.hash_map:
                    if pre is None or val != pre:
                        pre = new_per[i] if i < len(new_per) else None
                        backtrack(new_nums, new_per[:i] + [val] + new_per[i:])
                        # self.hash_map[val] = True

        backtrack(nums, [])
        print(len(self.vals))
        return self.vals

def stringToIntegerList(input):
    return json.loads(input)

def int2dArrayToString(input):
    return json.dumps(input)

def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')
    lines = readlines()
    while True:
        try:
            line = lines.next()
            nums = stringToIntegerList(line)
            
            ret = Solution().permuteUnique(nums)

            out = int2dArrayToString(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()
'''
