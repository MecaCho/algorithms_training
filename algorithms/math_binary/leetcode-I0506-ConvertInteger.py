'''
面试题 05.06. 整数转换
整数转换。编写一个函数，确定需要改变几个位才能将整数A转成整数B。

示例1:

 输入：A = 29 （或者0b11101）, B = 15（或者0b01111）
 输出：2
示例2:

 输入：A = 1，B = 2
 输出：2
提示:

A，B范围在[-2147483648, 2147483647]之间

面试题 05.06. Convert Integer LCCI
Write a function to determine the number of bits you would need to flip to convert integer A to integer B.

Example1:

 Input: A = 29 (0b11101), B = 15 (0b01111)
 Output: 2
Example2:

 Input: A = 1，B = 2
 Output: 2
Note:

-2147483648 <= A, B <= 2147483647
'''


class Solution(object):
    def convertInteger(self, A, B):
        """
        :type A: int
        :type B: int
        :rtype: int
        """
        n = (A&0xffffffff) ^ (B&0xffffffff)
        count = 0
        # print(n)
        while n:
            n &= (n-1)
            count += 1
        return count




'''
解题思路
这个问题看似复杂，实则不难，我们发现只有该位置不同时才需要转换，因此想到使用异或得到结果 c，最后数一下 c 中 1 的个数即可。

知识小贴士

真值	原码	反码	补码	备注
+ 1	0 00000001	0 00000001	0 00000001	正数的原码反码补码相同
- 1	1 00000001	1 11111110	1 11111111	负数的补码是符号位不变其余取反加 1
方法一：一行
pythoncpp
lass Solution:
    def convertInteger(self, A: int, B: int) -> int:
        return bin((A & 0xffffffff) ^ (B & 0xffffffff)).count('1')
方法二
不断对 c 进行移位操作，然后检查最低有效位。

pythoncpp
class Solution:
    def convertInteger(self, A: int, B: int) -> int:
        res = 0
        c = A ^ B
        for i in range(32):
            res += c >> i & 1
        return res
方法三
不断翻转最低有效位，计算需要多少次 c 会变成 0。其中 ⚠️c = c & (c - 1) 是一个位操作的常用问题，可以特别注意一下。

pythoncpp
class Solution:
    def convertInteger(self, A: int, B: int) -> int:
        C = (A & 0xffffffff) ^ (B & 0xffffffff)
        cnt = 0
        while C != 0: # 不断翻转最低位直到为 0
            C = C & (C - 1) # 清除最低位
            cnt += 1
        return cnt
复杂度分析
时间复杂度：O(1)O(1)。
空间复杂度：O(1)O(1)。
为什么要和 oxffffffff 作与运算
一般来讲，整形数在内存中是以 补码 的形式存放的，输出的时候同样也是按照 补码 输出的。

但是在 Python 中，情况是这样的：

整形是以 补码 形式存放的，输出的时候是按照 二进制 表示输出的；
对于 bin(x)bin(x)（xx 为 十进制负数），输出的是它的原码的二进制表示加上一个负号，方便查看（方便个🔨🔨🔨）
对于 bin(x)bin(x)（xx 为 十六进制负数），输出的是对应的二进制表示。
所以为了获得十进制负数的补码，我们需要手动将其和 0xffffffff 进行与操作，得到一个十六进制数，再交给 bin() 转化，这时内存中得到的才是你想要的补码。

a = bin(-3)
print(a)

a = bin(3)
print(a)

b = bin(-3 & 0xffffffff)
print(b)

c = bin(0xfffffffd)
print(c)

# 输出
# -0b11
# 0b11
# 0b11111111111111111111111111111101
# 0b11111111111111111111111111111101

'''