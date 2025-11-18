# encoding=utf8

'''
717. 1-bit and 2-bit Characters
We have two special characters:

The first character can be represented by one bit 0.
The second character can be represented by two bits (10 or 11).
Given a binary array bits that ends with 0, return true if the last character must be a one-bit character.

 

Example 1:

Input: bits = [1,0,0]
Output: true
Explanation: The only way to decode it is two-bit character and one-bit character.
So the last character is one-bit character.
Example 2:

Input: bits = [1,1,1,0]
Output: false
Explanation: The only way to decode it is two-bit character and two-bit character.
So the last character is not one-bit character.
 

Constraints:

1 <= bits.length <= 1000
bits[i] is either 0 or 1.

717. 1 比特与 2 比特字符

有两种特殊字符：

    第一种字符可以用一比特 0 表示
    第二种字符可以用两比特（10 或 11）表示

给你一个以 0 结尾的二进制数组 bits ，如果最后一个字符必须是一个一比特字符，则返回 true 。

 

示例 1:

输入: bits = [1, 0, 0]
输出: true
解释: 唯一的解码方式是将其解析为一个两比特字符和一个一比特字符。
所以最后一个字符是一比特字符。

示例 2:

输入：bits = [1,1,1,0]
输出：false
解释：唯一的解码方式是将其解析为两比特字符和两比特字符。
所以最后一个字符不是一比特字符。

 

提示:

    1 <= bits.length <= 1000
    bits[i] 为 0 或 1


'''

class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i, n = 0, len(bits)
        while i < n-1:
            i += bits[i] +1
        return i == n-1


class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        i, n = 0, len(bits)
        while i < n-1:
            if bits[i] == 0:
                i += 1
            else:
                i += 2
            
        return True if i == n-1 else False
      
