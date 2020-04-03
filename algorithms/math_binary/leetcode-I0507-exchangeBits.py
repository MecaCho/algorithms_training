
'''
面试题 05.07. 配对交换
配对交换。编写程序，交换某个整数的奇数位和偶数位，尽量使用较少的指令（也就是说，位0与位1交换，位2与位3交换，以此类推）。

示例1:

 输入：num = 2（或者0b10）
 输出 1 (或者 0b01)
示例2:

 输入：num = 3
 输出：3
提示:

num的范围在[0, 2^30 - 1]之间，不会发生整数溢出。

面试题 05.07. Exchange LCCI
Write a program to swap odd and even bits in an integer with as few instructions as possible (e.g., bit 0 and bit 1 are swapped, bit 2 and bit 3 are swapped, and so on).

Example1:

 Input: num = 2（0b10）
 Output 1 (0b01)
Example2:

 Input: num = 3
 Output: 3
Note:

0 <= num <= 2^30 - 1
The result integer fits into 32-bit integer.


'''



class Solution(object):
    def exchangeBits(self, num):
        """
        :type num: int
        :rtype: int
        """
        res = 0
        i = 0
        while num:
            last = (num % 2)
            second = (num % 4)
            print(last, second, res)
            res = res + (last * 2 + (second - last) / 2) * (4**i)
            i += 1
            num = num / 4
        # res +=
        return res

#class Solution {
#     public int exchangeBits(int num) {
#         //奇数
#         int odd = num & 0x55555555;
#         //偶数
#         int even = num & 0xaaaaaaaa;
#         odd = odd << 1;
#         even = even >>> 1;
#         return odd | even;
#     }
# }
# 思路的话就是分别取出奇数位和偶数位，移动后做或运算。
# 题目规定 num 是int范围的数
# 0x55555555 = 0b0101_0101_0101_0101_0101_0101_0101_0101
# 0xaaaaaaaa = 0b1010_1010_1010_1010_1010_1010_1010_1010
#
# 用这两个数做与运算，就可以把奇数位和偶数位取出来，
# 然后位左移奇数位，右移偶数位，
# 再把 奇数位和偶数位做或运算。
#