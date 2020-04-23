'''
47. Permutations II
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
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
