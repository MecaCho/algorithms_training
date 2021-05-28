# encoding=utf8

'''
477. Total Hamming Distance

The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given an integer array nums, return the sum of Hamming distances between all the pairs of the integers in nums.

 

Example 1:

Input: nums = [4,14,2]
Output: 6
Explanation: In binary representation, the 4 is 0100, 14 is 1110, and 2 is 0010 (just
showing the four bits relevant in this case).
The answer will be:
HammingDistance(4, 14) + HammingDistance(4, 2) + HammingDistance(14, 2) = 2 + 2 + 2 = 6.
Example 2:

Input: nums = [4,14,4]
Output: 4
 

Constraints:

1 <= nums.length <= 105
0 <= nums[i] <= 109

477. 汉明距离总和

两个整数的 汉明距离 指的是这两个数字的二进制数对应位不同的数量。

计算一个数组中，任意两个数之间汉明距离的总和。

示例:

输入: 4, 14, 2

输出: 6

解释: 在二进制表示中，4表示为0100，14表示为1110，2表示为0010。（这样表示是为了体现后四位之间关系）
所以答案为：
HammingDistance(4, 14) + HammingDistance(4, 2) + HammingDistance(14, 2) = 2 + 2 + 2 = 6.
注意:

数组中元素的范围为从 0到 10^9。
数组的长度不超过 10^4。
'''


class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        ans = 0
        for i in range(30):
            c = sum(((val >> i) & 1) for val in nums)
            ans += c * (n - c)
        return ans
       
# solutions

'''
方法一：逐位统计
在计算汉明距离时，我们考虑的是同一比特位上的值是否不同，而不同比特位之间是互不影响的。

对于数组 \textit{nums}nums 中的某个元素 \textit{val}val，若其二进制的第 ii 位为 11，我们只需统计 \textit{nums}nums 中有多少元素的第 ii 位为 00，即计算出了 \textit{val}val 与其他元素在第 ii 位上的汉明距离之和。

具体地，若长度为 nn 的数组 \textit{nums}nums 的所有元素二进制的第 ii 位共有 cc 个 11，n-cn−c 个 00，则些元素在二进制的第 ii 位上的汉明距离之和为

c\cdot(n-c)
c⋅(n−c)

我们可以从二进制的最低位到最高位，逐位统计汉明距离。将每一位上得到的汉明距离累加即为答案。

具体实现时，对于整数 \textit{val}val 二进制的第 ii 位，我们可以用代码 (val >> i) & 1 来取出其第 ii 位的值。此外，由于 10^9<2^{30}10 
9
 <2 
30
 ，我们可以直接从二进制的第 00 位枚举到第 2929 位。

C++JavaC#GolangPython3CJavaScript

func totalHammingDistance(nums []int) (ans int) {
    n := len(nums)
    for i := 0; i < 30; i++ {
        c := 0
        for _, val := range nums {
            c += val >> i & 1
        }
        ans += c * (n - c)
    }
    return
}
复杂度分析

时间复杂度：O(n\cdot L)O(n⋅L)。其中 nn 是数组 \textit{nums}nums 的长度，L=30L=30。

空间复杂度：O(1)O(1)。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/total-hamming-distance/solution/yi-ming-ju-chi-zong-he-by-leetcode-solut-t0ev/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
