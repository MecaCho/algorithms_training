
'''
面试题 05.03. 翻转数位
给定一个32位整数 num，你可以将一个数位从0变为1。请编写一个程序，找出你能够获得的最长的一串1的长度。

示例 1：

输入: num = 1775(110111011112)
输出: 8
示例 2：

输入: num = 7(01112)
输出: 4

面试题 05.03. Reverse Bits LCCI
You have an integer and you can flip exactly one bit from a 0 to a 1. Write code to find the length of the longest sequence of 1s you could create.

Example 1:

Input: num = 1775(110111011112)
Output: 8
Example 2:

Input: num = 7(01112)
Output: 4
'''




class Solution(object):
    def reverseBits(self, num):
        """
        :type num: int
        :rtype: int
        """
        bin_num = bin(num)
        # print(bin_num)
        vals = []
        while num:
            if num % 2== 0:
                vals.append(0)
            else:
                if not vals or vals[-1] == 0:
                    vals.append(1)
                else:
                    vals[-1] += 1
            num /= 2
        max_val = 1
        # print(vals)
        for i in range(len(vals)):
            max_val = max(max_val, sum(vals[i:i+3])+1)
        return max_val
