

'''
751. IP 到 CIDR
给定一个起始 IP 地址 ip 和一个我们需要包含的 IP 的数量 n，返回用列表（最小可能的长度）表示的 CIDR块的范围。

CIDR 块是包含 IP 的字符串，后接斜杠和固定长度。例如：“123.45.67.89/20”。固定长度 “20” 表示在特定的范围中公共前缀位的长度。

示例 1：

输入：ip = "255.0.0.7", n = 10
输出：["255.0.0.7/32","255.0.0.8/29","255.0.0.16/32"]
解释：
转换为二进制时，初始IP地址如下所示（为清晰起见添加了空格）：
255.0.0.7 -> 11111111 00000000 00000000 00000111
地址 "255.0.0.7/32" 表示与给定地址有相同的 32 位前缀的所有地址，
在这里只有这一个地址。

地址 "255.0.0.8/29" 表示与给定地址有相同的 29 位前缀的所有地址：
255.0.0.8 -> 11111111 00000000 00000000 00001000
有相同的 29 位前缀的地址如下：
11111111 00000000 00000000 00001000
11111111 00000000 00000000 00001001
11111111 00000000 00000000 00001010
11111111 00000000 00000000 00001011
11111111 00000000 00000000 00001100
11111111 00000000 00000000 00001101
11111111 00000000 00000000 00001110
11111111 00000000 00000000 00001111

地址 "255.0.0.16/32" 表示与给定地址有相同的 32 位前缀的所有地址，
这里只有 11111111 00000000 00000000 00010000。

总之，答案指定了从 255.0.0.7 开始的 10 个 IP 的范围。

有一些其他的表示方法，例如：
["255.0.0.7/32","255.0.0.8/30", "255.0.0.12/30", "255.0.0.16/32"],
但是我们的答案是最短可能的答案。

另外请注意以 "255.0.0.7/30" 开始的表示不正确，
因为其包括了 255.0.0.4 = 11111111 00000000 00000000 00000100 这样的地址，
超出了需要表示的范围。


注：

ip 是有效的 IPv4 地址。
每一个隐含地址 ip + x (其中 x < n) 都是有效的 IPv4 地址。
n 为整数，范围为 [1, 1000]。


751. IP to CIDR
Given a start IP address ip and a number of ips we need to cover n, return a representation of the range as a list (of smallest possible length) of CIDR blocks.

A CIDR block is a string consisting of an IP, followed by a slash, and then the prefix length. For example: "123.45.67.89/20". That prefix length "20" represents the number of common prefix bits in the specified range.

Example 1:
Input: ip = "255.0.0.7", n = 10
Output: ["255.0.0.7/32","255.0.0.8/29","255.0.0.16/32"]
Explanation:
The initial ip address, when converted to binary, looks like this (spaces added for clarity):
255.0.0.7 -> 11111111 00000000 00000000 00000111
The address "255.0.0.7/32" specifies all addresses with a common prefix of 32 bits to the given address,
ie. just this one address.

The address "255.0.0.8/29" specifies all addresses with a common prefix of 29 bits to the given address:
255.0.0.8 -> 11111111 00000000 00000000 00001000
Addresses with common prefix of 29 bits are:
11111111 00000000 00000000 00001000
11111111 00000000 00000000 00001001
11111111 00000000 00000000 00001010
11111111 00000000 00000000 00001011
11111111 00000000 00000000 00001100
11111111 00000000 00000000 00001101
11111111 00000000 00000000 00001110
11111111 00000000 00000000 00001111

The address "255.0.0.16/32" specifies all addresses with a common prefix of 32 bits to the given address,
ie. just 11111111 00000000 00000000 00010000.

In total, the answer specifies the range of 10 ips starting with the address 255.0.0.7 .

There were other representations, such as:
["255.0.0.7/32","255.0.0.8/30", "255.0.0.12/30", "255.0.0.16/32"],
but our answer was the shortest possible.

Also note that a representation beginning with say, "255.0.0.7/30" would be incorrect,
because it includes addresses like 255.0.0.4 = 11111111 00000000 00000000 00000100
that are outside the specified range.
Note:
ip will be a valid IPv4 address.
Every implied address ip + x (for x < n) will be a valid IPv4 address.
n will be an integer in the range [1, 1000].
'''







class Solution(object):
    def ipToCIDR(self, ip, n):
        """
        :type ip: str
        :type n: int
        :rtype: List[str]
        """
        # def get_num(n):
        #     for
        # def get_prefix(ip, n):
        #     l = ip.split(".")
        #     res = ""
        #     while n > 8:
        #         res += l.pop(0) + "."
        #         n -= 8
        #     res += bin(int(l[0]))[2:].rjust(8, "0")[:n]
        #     return res

        # base = int(math.log(n, 2))

        # res = get_prefix(ip, 32 - base)
        # print(res)
        start = self.ipToInt(ip)
        res = []
        while n:
            # base = int(math.log(n, 2))
            # res.append()
            # n -= 2**base
            mask = max(33 - (start & -start).bit_length(), 33 - n.bit_length())
            print(mask)
            res.append(self.intToIP(start) + '/' + str(mask))
            start += 1 << (32 - mask)
            n -= 1 << (32 - mask)
        return res

    def ipToInt(self, ip):
        res = 0
        for x in ip.split('.'):
            res = 256 * res + int(x)
        return res

    def intToIP(self, x):
        return ".".join(str((x >> i) % 256) for i in (24, 16, 8, 0))




# tips

'''
Convert the ip addresses to and from (long) integers. You want to know what is the most addresses you can put in this block starting from the "start" ip, up to n. It is the smallest between the lowest bit of start and the highest bit of n. Then, repeat this process with a new start and n.

'''

# solutions

'''
方法一：
若是手写计算答案则相对简单，写代码棘手的部分是所涉及的位操作。
我们思考一个问题：对于所需的 n 个 ip 地址，以及从起始 ip 地址开始且在范围内的 ip 地址，哪些 CIDR 块能够表示在范围内的大部分 ip 地址？用贪心的思想是可行的，我们可以一直重复这个过程，直到我们包括 n 个 ip 地址，所以我们应该尽可能的使用一个大的 CIDR 块。
算法：

我们需要将 ip 地址转换为长整数，通过一些基本的操作来实现这个功能--具体看代码实现方式。
然后，将 255.0.0.24 这样的 ip 地址转换为 start，它以二进制 00011000 结尾。如果 n>=8，那么我们应该使用整个块 255.0.0.24/29。否则，我们只取满足 2^x>=n2 
x
 >=n x 的最小值 。
在一般情况下啊，我们使用 n 和 start&-start（start 的最低位）的位长度来计算能表示 2^{32 - \text{mask}}2 
32−mask
  个 ip 地址的掩码。然后，我们动态调整 start 和 n。
在 Java 和 C++ 中，我们应该小心使用长整数来表示转换后的 IP 地址，因为该数字可能超过 2^{31}2 
31
 。
PythonJava
class Solution(object):
    def ipToInt(self, ip):
        ans = 0
        for x in ip.split('.'):
            ans = 256 * ans + int(x)
        return ans

    def intToIP(self, x):
        return ".".join(str((x >> i) % 256)
                        for i in (24, 16, 8, 0))

    def ipToCIDR(self, ip, n):
        start = self.ipToInt(ip)
        ans = []
        while n:
            mask = max(33 - (start & -start).bit_length(),
                       33 - n.bit_length())
            ans.append(self.intToIP(start) + '/' + str(mask))
            start += 1 << (32 - mask)
            n -= 1 << (32 - mask)
        return ans
复杂度分析

时间复杂度：O(N)O(N)。其中 NN 表示的是 nums 的长度
空间复杂度：O(1)O(1)。

作者：LeetCode
链接：https://leetcode-cn.com/problems/ip-to-cidr/solution/ip-dao-cidr-by-leetcode/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
