'''
267. 回文排列 II
给定一个字符串 s ，返回其通过重新排列组合后所有可能的回文字符串，并去除重复的组合。

如不能形成任何回文排列时，则返回一个空列表。

示例 1：

输入: "aabb"
输出: ["abba", "baab"]
示例 2：

输入: "abc"
输出: []

267. Palindrome Permutation II
Given a string s, return all the palindromic permutations (without duplicates) of it. Return an empty list if no palindromic permutation could be form.

Example 1:

Input: "aabb"
Output: ["abba", "baab"]
Example 2:

Input: "abc"
Output: []
'''



class Solution(object):
    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(set(list(s))) == 1:
            return [s]
        import collections
        hash_map = collections.Counter(s)
        new_s = ""
        count = 0
        mid = ""

        for k, v in hash_map.items():
            if v % 2 == 0:
                new_s += k * (v / 2)
            else:
                mid = k
                count += 1
                new_s += k * (v / 2)
                if count > 1:
                    return []

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
                for i in range(len(new_per) + 1):
                    # if val not in self.hash_map:
                    if pre is None or val != pre:
                        pre = new_per[i] if i < len(new_per) else None
                        backtrack(new_nums, new_per[:i] + [val] + new_per[i:])
                        # self.hash_map[val] = True

        backtrack(new_s, [])
        # import itertools

        # for i in itertools.permutations(list(new_s)):
        # print(i)
        # print(self.vals)
        # return sorted(list(set(["".join(i[::-1]) + mid + "".join(i) for i in list(itertools.permutations(list(
        # new_s)))])))
        return ["".join(i[::-1]) + mid + "".join(i) for i in self.vals]
