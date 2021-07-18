# encoding=utf8

'''
面试题 10.02. Group Anagrams LCCI
Write a method to sort an array of strings so that all the anagrams are in the same group.

Note: This problem is slightly different from the original one the book.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Notes:

All inputs will be in lowercase.
The order of your output does not matter.

面试题 10.02. 变位词组
编写一种方法，对字符串数组进行排序，将所有变位词组合在一起。变位词是指字母相同，但排列不同的字符串。

注意：本题相对原题稍作修改

示例:

输入: ["eat", "tea", "tan", "ate", "nat", "bat"],
输出:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
说明：

所有输入均为小写字母。
不考虑答案输出的顺序。
'''

# solution

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        mp = collections.defaultdict(list)
        for st in strs:
            key = [0]*26
            for char in st:
                key[ord(char)-ord("a")] += 1
            d = tuple(key)
            mp[d].append(st)

        return mp.values()

      
