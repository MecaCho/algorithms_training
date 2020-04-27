


'''
484. 寻找排列
现在给定一个只由字符 'D' 和 'I' 组成的 秘密签名。'D' 表示两个数字间的递减关系，'I' 表示两个数字间的递增关系。并且 秘密签名 是由一个特定的整数数组生成的，该数组唯一地包含 1 到 n 中所有不同的数字（秘密签名的长度加 1 等于 n）。例如，秘密签名 "DI" 可以由数组 [2,1,3] 或 [3,1,2] 生成，但是不能由数组 [3,2,4] 或 [2,1,3,4] 生成，因为它们都不是合法的能代表 "DI" 秘密签名 的特定串。

现在你的任务是找到具有最小字典序的 [1, 2, ... n] 的排列，使其能代表输入的 秘密签名。

示例 1：

输入： "I"
输出： [1,2]
解释： [1,2] 是唯一合法的可以生成秘密签名 "I" 的特定串，数字 1 和 2 构成递增关系。


示例 2：

输入： "DI"
输出： [2,1,3]
解释： [2,1,3] 和 [3,1,2] 可以生成秘密签名 "DI"，
但是由于我们要找字典序最小的排列，因此你需要输出 [2,1,3]。


注：

输出字符串只会包含字符 'D' 和 'I'。
输入字符串的长度是一个正整数且不会超过 10,000。

484. Find Permutation
By now, you are given a secret signature consisting of character 'D' and 'I'. 'D' represents a decreasing relationship between two numbers, 'I' represents an increasing relationship between two numbers. And our secret signature was constructed by a special integer array, which contains uniquely all the different number from 1 to n (n is the length of the secret signature plus 1). For example, the secret signature "DI" can be constructed by array [2,1,3] or [3,1,2], but won't be constructed by array [3,2,4] or [2,1,3,4], which are both illegal constructing special string that can't represent the "DI" secret signature.

On the other hand, now your job is to find the lexicographically smallest permutation of [1, 2, ... n] could refer to the given secret signature in the input.

Example 1:
Input: "I"
Output: [1,2]
Explanation: [1,2] is the only legal initial spectial string can construct secret signature "I", where the number 1 and 2 construct an increasing relationship.
Example 2:
Input: "DI"
Output: [2,1,3]
Explanation: Both [2,1,3] and [3,1,2] can construct the secret signature "DI",
but since we want to find the one with the smallest lexicographical permutation, you need to output [2,1,3]
Note:

The input string will only contain the character 'D' and 'I'.
The length of input string is a positive integer and will not exceed 10,000
'''


class Solution(object):
    def findPermutation(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        import itertools
        itertools.permutations()
        itertools.combinations([], )
        res = [i+1 for i in range(len(s)+1)]
        i = 0
        while i < len(s):
            if s[i] == "I":
                i += 1
                continue
            start = i
            while start < len(s) and s[start] == "D":
                start += 1
            # print(res)
            new_res = res[i:start+1]
            # print(new_res, i, start)
            res[i:start+1] = new_res[::-1]
            i = start+1
        return res
