

'''
面试题 01.04. Palindrome Permutation LCCI
Given a string, write a function to check if it is a permutation of a palin­ drome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.



Example1:

Input: "tactcoa"
Output: true（permutations: "tacocat"、"atcocta", etc.）

面试题 01.04. 回文排列
给定一个字符串，编写一个函数判定其是否为某个回文串的排列之一。

回文串是指正反两个方向都一样的单词或短语。排列是指字母的重新排列。

回文串不一定是字典当中的单词。



示例1：

输入："tactcoa"
输出：true（排列有"tacocat"、"atcocta"，等等）
'''




class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        hash_map = {}
        for i in range(len(s)):
            if s[i] in hash_map:
                hash_map[s[i]] += 1
            else:
                hash_map[s[i]] = 1
        count = 0
        for k, v in hash_map.items():
            if v % 2 == 1:
                count += 1
                if count > 1:
                    return False
        return True


if __name__ == '__main__':
    for i in range(10):
        for j in range(10):
            if j == 5:
                break
            print(i, j)