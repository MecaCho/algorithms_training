# encoding=utf8

'''
670. Maximum Swap
You are given an integer num. You can swap two digits at most once to get the maximum valued number.

Return the maximum valued number you can get.

 

Example 1:

Input: num = 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.
Example 2:

Input: num = 9973
Output: 9973
Explanation: No swap.
 

Constraints:

0 <= num <= 108

'''

class Solution:
    def maximumSwap(self, num: int) -> int:
        chars = sorted(list(str(num)), reverse=True)
        num_s = list(str(num))
        for i in range(len(num_s)):
            if num_s[i] != chars[i]:
                k = len(num_s[i:])
                index = k - num_s[i:][::-1].index(chars[i]) + i - 1
                num_s[i], num_s[index] = chars[i], num_s[i]
                break

        return int("".join(num_s))

# tips

'''
将元数字按照数位降序排列的值最大，但我们只有一次交换机惠。最贪心的方案是：找到最左侧可以增大的数位，再找到最右侧最大的数位，将两者交换。
'''
