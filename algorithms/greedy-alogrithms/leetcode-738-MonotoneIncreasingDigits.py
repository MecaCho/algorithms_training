# -*-coding=UTF-8-*-
'''
738. Monotone Increasing Digits
Given a non-negative integer N, find the largest number that is less than or equal to N with monotone increasing digits.

(Recall that an integer has monotone increasing digits if and only if each pair of adjacent digits x and y satisfy x <= y.)

Example 1:
Input: N = 10
Output: 9
Example 2:
Input: N = 1234
Output: 1234
Example 3:
Input: N = 332
Output: 299
Note: N is an integer in the range [0, 10^9].


738. 单调递增的数字
给定一个非负整数 N，找出小于或等于 N 的最大的整数，同时这个整数需要满足其各个位数上的数字是单调递增。

（当且仅当每个相邻位数上的数字 x 和 y 满足 x <= y 时，我们称这个整数是单调递增的。）

示例 1:

输入: N = 10
输出: 9
示例 2:

输入: N = 1234
输出: 1234
示例 3:

输入: N = 332
输出: 299
说明: N 是在 [0, 10^9] 范围内的一个整数。
'''


class Solution(object):
    def monotoneIncreasingDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        i, res = 1, N
        while i <= res/10:
            n = res / i % 100
            i *= 10
            if n/10 > n%10:
                res = res/i * i - 1

        return res


class Solution20201215(object):
    def monotoneIncreasingDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        nums = list(str(N))
        i = 1
        while i < len(nums):
            if nums[i] >= nums[i - 1]:
                i += 1
            else:
                break

        if i < len(nums):
            # nums[i] = chr(ord(nums[i]) - 1)
            # j = i
            while i > 0 and nums[i] < nums[i - 1]:
                nums[i - 1] = chr(ord(nums[i - 1]) - 1)
                i -= 1
            i += 1
            while i < len(nums):
                nums[i] = "9"
                i += 1

        return int("".join(nums))



class Solution_(object):
    def monotoneIncreasingDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        nums = list(str(N))
        i = 1
        while i < len(nums):
            if nums[i] >= nums[i - 1]:
                i += 1
            else:
                break

        if i < len(nums):
            # nums[i] = chr(ord(nums[i]) - 1)
            # j = i
            while i > 0 and nums[i] < nums[i - 1]:
                nums[i - 1] = chr(ord(nums[i - 1]) - 1)
                i -= 1
            i += 1
            while i < len(nums):
                nums[i] = "9"
                i += 1

        return int("".join(nums))



if __name__ == '__main__':
    demo = Solution20201215()
    res = demo.monotoneIncreasingDigits(10)
    print(res)




# solution

'''
方法一：贪心
我们可以从高到低按位构造这个小于等于 NN 的最大单调递增的数字。假设不考虑 NN 的限制，那么对于一个长度为 nn 的数字，最大单调递增的数字一定是每一位都为 99 的数字。

记 \textit{strN}[i]strN[i] 表示数字 NN 从高到低的第 ii 位的数字（ii 从 00 开始）。

如果整个数字 NN 本身已经是按位单调递增的，那么最大的数字即为 NN。

如果找到第一个位置 ii 使得 [0,i-1][0,i−1] 的数位单调递增且 \textit{strN}[i-1]>\textit{strN}[i]strN[i−1]>strN[i]，此时 [0,i][0,i] 的数位都与 NN 的对应数位相等，仍然被 NN 限制着，即我们不能随意填写 [i+1,n-1][i+1,n−1] 位置上的数字。为了得到最大的数字，我们需要解除 NN 的限制，来让剩余的低位全部变成 99 ，即能得到小于 NN 的最大整数。而从贪心的角度考虑，我们需要尽量让高位与 NN 的对应数位相等，故尝试让 \textit{strN}[i-1]strN[i−1] 自身数位减 11。此时已经不再受 NN 的限制，直接将 [i, n-1][i,n−1] 的位置上的数全部变为 99 即可。

但这里存在一个问题：当 \textit{strN}[i-1]strN[i−1] 自身数位减 11 后可能会使得 \textit{strN}[i-1]strN[i−1] 和 \textit{strN}[i-2]strN[i−2] 不再满足递增的关系，因此我们需要从 i-1i−1 开始递减比较相邻数位的关系，直到找到第一个位置 jj 使得 \textit{strN}[j]strN[j] 自身数位减 11 后 \textit{strN}[j-1]strN[j−1] 和 \textit{strN}[j]strN[j] 仍然保持递增关系，或者位置 jj 已经到最左边（即 jj 的值为 00），此时我们将 [j+1,n-1][j+1,n−1] 的数全部变为 99 才能得到最终正确的答案。

代码如下。

C++JavaJavaScriptGolangC

func monotoneIncreasingDigits(n int) int {
    s := []byte(strconv.Itoa(n))
    i := 1
    for i < len(s) && s[i] >= s[i-1] {
        i++
    }
    if i < len(s) {
        for i > 0 && s[i] < s[i-1] {
            s[i-1]--
            i--
        }
        for i++; i < len(s); i++ {
            s[i] = '9'
        }
    }
    ans, _ := strconv.Atoi(string(s))
    return ans
}
复杂度分析

时间复杂度：O(\log N)O(logN)，其中 O(\log N)O(logN) 表示数字 NN 的位数。我们遍历 O(\log N)O(logN) 的时间即能构造出满足条件的数字。

空间复杂度：O(\log N)O(logN)。我们需要 O(\log N)O(logN) 的空间存放数字 NN 每一位的数字大小。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/monotone-increasing-digits/solution/dan-diao-di-zeng-de-shu-zi-by-leetcode-s-5908/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''

