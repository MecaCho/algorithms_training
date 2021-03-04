#encoding=utf8

'''
338. Counting Bits
Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

Example 1:

Input: 2
Output: [0,1,1]
Example 2:

Input: 5
Output: [0,1,1,2,1,2]
Follow up:

It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?
Space complexity should be O(n).
Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.


338. 比特位计数
给定一个非负整数 num。对于 0 ≤ i ≤ num 范围中的每个数字 i ，计算其二进制数中的 1 的数目并将它们作为数组返回。

示例 1:

输入: 2
输出: [0,1,1]
示例 2:

输入: 5
输出: [0,1,1,2,1,2]
进阶:

给出时间复杂度为O(n*sizeof(integer))的解答非常容易。但你可以在线性时间O(n)内用一趟扫描做到吗？
要求算法的空间复杂度为O(n)。
你能进一步完善解法吗？要求在C++或任何其他语言中不使用任何内置函数（如 C++ 中的 __builtin_popcount）来执行此操作。
'''


class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        dp = [0] * (num + 1)
        for i in range(num//2+1):
            dp[2*i] = dp[i]
            if 2*i + 1 <= num:
                dp[2*i+1] = dp[i] + 1

        return dp


# solutions


'''
前言
这道题需要计算从 00 到 \textit{num}num 的每个数的二进制表示中的 11 的数目。最直观的方法是对每个数直接计算二进制表示中的 11 的数目，时间复杂度较高。也可以使用动态规划的方法，时间复杂度较低。

为了表述简洁，下文用「一比特数」表示二进制表示中的 11 的数目。

方法一：直接计算
最直观的方法是对从 00 到 \textit{num}num 的每个数直接计算「一比特数」。

每个 \texttt{int}int 型的数都可以用 3232 位二进制数表示，只要遍历其二进制表示的每一位即可得到 11 的数目。

利用位运算的技巧，可以在一定程度上提升计算速度。按位与运算（\&&）的一个性质是：对于任意整数 xx，令 x=x \&(x-1)x=x&(x−1)，该运算将 xx 的二进制表示的最后一个 11 变成 00。因此，对 xx 重复该操作，直到 xx 变成 00，则操作次数即为 xx 的「一比特数」。

另外，部分编程语言有相应的内置函数，例如 \texttt{Java}Java 的 \texttt{Integer.bitCount}Integer.bitCount，\texttt{C++}C++ 的 \texttt{\_\_builtin\_popcount}__builtin_popcount，\texttt{Go}Go 的 \texttt{bits.OnesCount}bits.OnesCount 等，读者可以自行尝试。需要注意的是，使用编程语言的内置函数时，不适用本方法的时间复杂度分析。

JavaJavaScriptGolangPython3C++C

class Solution:
    def countBits(self, num: int) -> List[int]:
        def countOnes(x: int) -> int:
            ones = 0
            while x > 0:
                x &= (x - 1)
                ones += 1
            return ones
        
        bits = [countOnes(i) for i in range(num + 1)]
        return bits
复杂度分析

时间复杂度：O(k \times \textit{num})O(k×num)，其中 kk 是 \texttt{int}int 型的二进制位数，k=32k=32。需要对从 00 到 \textit{num}num 的每个数使用 O(k)O(k) 的时间计算「一比特数」，因此时间复杂度是 O(k \times \textit{num})O(k×num)。

空间复杂度：O(1)O(1)。除了返回的数组以外，空间复杂度为常数。

方法二：动态规划——最高有效位
方法一需要对每个数遍历其二进制表示的每一位。可以换一个思路，当计算 ii 的「一比特数」时，如果存在 0 \le j<i0≤j<i，jj 的「一比特数」已知，且 ii 和 jj 相比，ii 的二进制表示只多了一个 11，则可以快速得到 ii 的「一比特数」。

令 \textit{bits}[i]bits[i] 表示 ii 的「一比特数」，则上述关系可以表示成：\textit{bits}[i]= \textit{bits}[j]+1bits[i]=bits[j]+1。

对于正整数 xx，如果可以知道最大的正整数 yy，使得 y \le xy≤x 且 yy 是 22 的整数次幂，则 yy 的二进制表示中只有最高位是 11，其余都是 00，此时称 yy 为 xx 的「最高有效位」。令 z=x-yz=x−y，显然 0 \le z<x0≤z<x，则 \textit{bits}[x]=\textit{bits}[z]+1bits[x]=bits[z]+1。

为了判断一个正整数是不是 22 的整数次幂，可以利用方法一中提到的按位与运算的性质。如果正整数 yy 是 22 的整数次幂，则 yy 的二进制表示中只有最高位是 11，其余都是 00，因此 y \&(y-1)=0y&(y−1)=0。由此可见，正整数 yy 是 22 的整数次幂，当且仅当 y \&(y-1)=0y&(y−1)=0。

显然，00 的「一比特数」为 00。使用 \textit{highBit}highBit 表示当前的最高有效位，遍历从 11 到 \textit{num}num 的每个正整数 ii，进行如下操作。

如果 i \&(i-1)=0i&(i−1)=0，则令 \textit{highBit}=ihighBit=i，更新当前的最高有效位。

ii 比 i-\textit{highBit}i−highBit 的「一比特数」多 11，由于是从小到大遍历每个数，因此遍历到 ii 时，i-\textit{highBit}i−highBit 的「一比特数」已知，令 \textit{bits}[i]=\textit{bits}[i-\textit{highBit}]+1bits[i]=bits[i−highBit]+1。

最终得到的数组 \textit{bits}bits 即为答案。

JavaJavaScriptGolangPython3C++C

class Solution:
    def countBits(self, num: int) -> List[int]:
        bits = [0]
        highBit = 0
        for i in range(1, num + 1):
            if i & (i - 1) == 0:
                highBit = i
            bits.append(bits[i - highBit] + 1)
        return bits
复杂度分析

时间复杂度：O(\textit{num})O(num)。对于每个数，只需要 O(1)O(1) 的时间计算「一比特数」。

空间复杂度：O(1)O(1)。除了返回的数组以外，空间复杂度为常数。

方法三：动态规划——最低有效位
方法二需要实时维护最高有效位，当遍历到的数是 22 的整数次幂时，需要更新最高有效位。如果再换一个思路，可以使用「最低有效位」计算「一比特数」。

对于正整数 xx，将其二进制表示右移一位，等价于将其二进制表示的最低位去掉，得到的数是 \lfloor \frac{x}{2} \rfloor⌊ 
2
x
​	
 ⌋。如果 \textit{bits}\big[\lfloor \frac{x}{2} \rfloor\big]bits[⌊ 
2
x
​	
 ⌋] 的值已知，则可以得到 \textit{bits}[x]bits[x] 的值：

如果 xx 是偶数，则 \textit{bits}[x]=\textit{bits}\big[\lfloor \frac{x}{2} \rfloor\big]bits[x]=bits[⌊ 
2
x
​	
 ⌋]；

如果 xx 是奇数，则 \textit{bits}[x]=\textit{bits}\big[\lfloor \frac{x}{2} \rfloor\big]+1bits[x]=bits[⌊ 
2
x
​	
 ⌋]+1。

上述两种情况可以合并成：\textit{bits}[x]bits[x] 的值等于 \textit{bits}\big[\lfloor \frac{x}{2} \rfloor\big]bits[⌊ 
2
x
​	
 ⌋] 的值加上 xx 除以 22 的余数。

由于 \lfloor \frac{x}{2} \rfloor⌊ 
2
x
​	
 ⌋ 可以通过 x >> 1x>>1 得到，xx 除以 22 的余数可以通过 x \& 1x&1 得到，因此有：\textit{bits}[x]=\textit{bits}[x>>1]+(x \& 1)bits[x]=bits[x>>1]+(x&1)。

遍历从 11 到 \textit{num}num 的每个正整数 ii，计算 \textit{bits}bits 的值。最终得到的数组 \textit{bits}bits 即为答案。

JavaJavaScriptGolangPython3C++C

class Solution:
    def countBits(self, num: int) -> List[int]:
        bits = [0]
        for i in range(1, num + 1):
            bits.append(bits[i >> 1] + (i & 1))
        return bits
复杂度分析

时间复杂度：O(\textit{num})O(num)。对于每个数，只需要 O(1)O(1) 的时间计算「一比特数」。

空间复杂度：O(1)O(1)。除了返回的数组以外，空间复杂度为常数。

方法四：动态规划——最低设置位
定义正整数 xx 的「最低设置位」为 xx 的二进制表示中的最低的 11 所在位。例如，1010 的二进制表示是 1010_{(2)}1010 
(2)
​	
 ，其最低设置位为 22，对应的二进制表示是 10_{(2)}10 
(2)
​	
 。

令 y=x \&(x-1)y=x&(x−1)，则 yy 为将 xx 的最低设置位从 11 变成 00 之后的数，显然 0 \le y<x0≤y<x，\textit{bits}[x]=\textit{bits}[y]+1bits[x]=bits[y]+1。因此对任意正整数 xx，都有 \textit{bits}[x]=\textit{bits}[x \&(x-1)]+1bits[x]=bits[x&(x−1)]+1。

遍历从 11 到 \textit{num}num 的每个正整数 ii，计算 \textit{bits}bits 的值。最终得到的数组 \textit{bits}bits 即为答案。

JavaJavaScriptGolangPython3C++C

class Solution:
    def countBits(self, num: int) -> List[int]:
        bits = [0]
        for i in range(1, num + 1):
            bits.append(bits[i & (i - 1)] + 1)
        return bits
复杂度分析

时间复杂度：O(\textit{num})O(num)。对于每个数，只需要 O(1)O(1) 的时间计算「一比特数」。

空间复杂度：O(1)O(1)。除了返回的数组以外，空间复杂度为常数。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/counting-bits/solution/bi-te-wei-ji-shu-by-leetcode-solution-0t1i/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
