# encoding=utf8


'''
424. Longest Repeating Character Replacement
Given a string s that consists of only uppercase English letters, you can perform at most k operations on that string.

In one operation, you can choose any character of the string and change it to any other uppercase English character.

Find the length of the longest sub-string containing all repeating letters you can get after performing the above operations.

Note:
Both the string's length and k will not exceed 104.

Example 1:

Input:
s = "ABAB", k = 2

Output:
4

Explanation:
Replace the two 'A's with two 'B's or vice versa.


Example 2:

Input:
s = "AABABBA", k = 1

Output:
4

Explanation:
Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.


424. 替换后的最长重复字符
给你一个仅由大写英文字母组成的字符串，你可以将任意位置上的字符替换成另外的字符，总共可最多替换 k 次。在执行上述操作后，找到包含重复字母的最长子串的长度。

注意：字符串长度 和 k 不会超过 104。



示例 1：

输入：s = "ABAB", k = 2
输出：4
解释：用两个'A'替换为两个'B',反之亦然。
示例 2：

输入：s = "AABABBA", k = 1
输出：4
解释：
将中间的一个'A'替换为'B',字符串变为 "AABBBBA"。
子串 "BBBB" 有最长重复字母, 答案为 4。
'''


class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        maxn = 0
        l, r = 0, 0
        char_num = [0]*26
        length = len(s)
        while r < length:
            char_num[ord(s[r])-ord("A")] += 1
            maxn = max(maxn, char_num[ord(s[r])-ord("A")])
            if r - l + 1 - maxn > k:
                char_num[ord(s[l])-ord("A")] -= 1
                l += 1
            r += 1
        return r - l


# solutions

'''
方法一：双指针
我们可以枚举字符串中的每一个位置作为右端点，然后找到其最远的左端点的位置，满足该区间内除了出现次数最多的那一类字符之外，剩余的字符（即非最长重复字符）数量不超过 kk 个。

这样我们可以想到使用双指针维护这些区间，每次右指针右移，如果区间仍然满足条件，那么左指针不移动，否则左指针至多右移一格，保证区间长度不减小。

虽然这样的操作会导致部分区间不符合条件，即该区间内非最长重复字符超过了 kk 个。但是这样的区间也同样不可能对答案产生贡献。当我们右指针移动到尽头，左右指针对应的区间的长度必然对应一个长度最大的符合条件的区间。

实际代码中，由于字符串中仅包含大写字母，我们可以使用一个长度为 2626 的数组维护每一个字符的出现次数。每次区间右移，我们更新右移位置的字符出现的次数，然后尝试用它更新重复字符出现次数的历史最大值，最后我们使用该最大值计算出区间内非最长重复字符的数量，以此判断左指针是否需要右移即可。

代码

C++JavaGolangCPython3JavaScript

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        num = [0] * 26
        n = len(s)
        maxn = left = right = 0

        while right < n:
            num[ord(s[right]) - ord("A")] += 1
            maxn = max(maxn, num[ord(s[right]) - ord("A")])
            if right - left + 1 - maxn > k:
                num[ord(s[left]) - ord("A")] -= 1
                left += 1
            right += 1
        
        return right - left
时间复杂度

时间复杂度：O(n)O(n)，其中 nn 是字符串的长度。我们至多只需要遍历该字符串一次。

空间复杂度：O(|\Sigma|)O(∣Σ∣)，其中 |\Sigma|∣Σ∣ 是字符集的大小。我们需要存储每个大写英文字母的出现次数。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/longest-repeating-character-replacement/solution/ti-huan-hou-de-zui-chang-zhong-fu-zi-fu-n6aza/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''

# coding=utf-8
import sys

# nums = raw_input()
# print nums
print 'Hello,World!'


def get_max_seq(nums):
    dp = [1] * len(nums)
    for i in range(len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp) if dp else 0




if __name__ == '__main__':
    test_cases = [
        [],
        [10, 9, 2, 5, 3, 7, 101, 18]
        ]
    for case in test_cases:
        res = get_max_seq(case)
        print(res)


