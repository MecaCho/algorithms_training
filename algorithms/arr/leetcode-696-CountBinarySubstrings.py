'''
696. Count Binary Substrings
Give a string s, count the number of non-empty (contiguous) substrings that have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.

Substrings that occur multiple times are counted the number of times they occur.

Example 1:
Input: "00110011"
Output: 6
Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: "0011", "01", "1100", "10", "0011", and "01".

Notice that some of these substrings repeat and are counted the number of times they occur.

Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.
Example 2:
Input: "10101"
Output: 4
Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal number of consecutive 1's and 0's.
Note:

s.length will be between 1 and 50,000.
s will only consist of "0" or "1" characters.

696. 计数二进制子串
给定一个字符串 s，计算具有相同数量0和1的非空(连续)子字符串的数量，并且这些子字符串中的所有0和所有1都是组合在一起的。

重复出现的子串要计算它们出现的次数。

示例 1 :

输入: "00110011"
输出: 6
解释: 有6个子串具有相同数量的连续1和0：“0011”，“01”，“1100”，“10”，“0011” 和 “01”。

请注意，一些重复出现的子串要计算它们出现的次数。

另外，“00110011”不是有效的子串，因为所有的0（和1）没有组合在一起。
示例 2 :

输入: "10101"
输出: 4
解释: 有4个子串：“10”，“01”，“10”，“01”，它们具有相同数量的连续1和0。
注意：

s.length 在1到50,000之间。
s 只包含“0”或“1”字符。
'''


class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        pre, cur = 0, 0
        for i in range(len(s)):
            # if i == 0:
            #     cur += 1
            if i == 0 or s[i] == s[i-1]:
                cur += 1
            else:
                pre = cur
                cur = 1
            if pre >= cur:
                res += 1
        return res


# tips

'''
How many valid binary substrings exist in "000111", and how many in "11100"? What about "00011100"?
'''

# solutions

'''
方法一：按字符分组
思路与算法

我们可以将字符串 ss 按照 00 和 11 的连续段分组，存在 \rm countscounts 数组中，例如 s = 00111011s=00111011，可以得到这样的 \rm countscounts 数组：{\rm counts} = \{2, 3, 1, 2\}counts={2,3,1,2}。

这里 \rm countscounts 数组中两个相邻的数一定代表的是两种不同的字符。假设 \rm countscounts 数组中两个相邻的数字为 uu 或者 vv，它们对应着 uu 个 00 和 vv 个 11，或者 uu 个 11 和 vv 个 00。它们能组成的满足条件的子串数目为 \min \{ u, v \}min{u,v}，即一对相邻的数字对答案的贡献。

我们只要遍历所有相邻的数对，求它们的贡献总和，即可得到答案。

不难得到这样的实现：

C++JavaJavaScriptGolangC

func countBinarySubstrings(s string) int {
    counts := []int{}
    ptr, n := 0, len(s)
    for ptr < n {
        c := s[ptr]
        count := 0
        for ptr < n && s[ptr] == c {
            ptr++
            count++
        }
        counts = append(counts, count)
    }
    ans := 0
    for i := 1; i < len(counts); i++ {
        ans += min(counts[i], counts[i-1])
    }
    return ans
}

func min(x, y int) int {
    if x < y {
        return x
    }
    return y
}
这个实现的时间复杂度和空间复杂度都是 O(n)O(n)。

对于某一个位置 ii，其实我们只关心 i - 1i−1 位置的 \rm countscounts 值是多少，所以可以用一个 \rm lastlast 变量来维护当前位置的前一个位置，这样可以省去一个 \rm countscounts 数组的空间。

代码如下。

代码

C++JavaJavaScriptGolangC

func countBinarySubstrings(s string) int {
    var ptr, last, ans int
    n := len(s)
    for ptr < n {
        c := s[ptr]
        count := 0
        for ptr < n && s[ptr] == c {
            ptr++
            count++
        }
        ans += min(count, last)
        last = count
    }

    return ans
}

func min(x, y int) int {
    if x < y {
        return x
    }
    return y
}
复杂度分析

时间复杂度：O(n)O(n)。
空间复杂度：O(1)O(1)。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/count-binary-substrings/solution/ji-shu-er-jin-zhi-zi-chuan-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''