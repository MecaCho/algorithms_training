'''
316. 去除重复字母
给你一个字符串 s ，请你去除字符串中重复的字母，使得每个字母只出现一次。需保证 返回结果的字典序最小（要求不能打乱其他字符的相对位置）。

注意：该题与 1081 https://leetcode-cn.com/problems/smallest-subsequence-of-distinct-characters 相同

 

示例 1：

输入：s = "bcabc"
输出："abc"
示例 2：

输入：s = "cbacdcbc"
输出："acdb"
 

提示：

1 <= s.length <= 104
s 由小写英文字母组成


316. Remove Duplicate Letters
Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

Note: This question is the same as 1081: https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/

 

Example 1:

Input: s = "bcabc"
Output: "abc"
Example 2:

Input: s = "cbacdcbc"
Output: "acdb"
 

Constraints:

1 <= s.length <= 104
s consists of lowercase English letters.
'''


class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        while s:
            # 从右往左找，找到最小位置的索引号
            loc = min(map(s.rindex, s))
            # 找该索引前面最小的字母
            a = min(s[:loc + 1])
            res += a
            s = s[s.index(a):].replace(a, "")
        return res

# solution

'''
方法一：贪心 + 栈
思路与算法

首先考虑一个简单的问题：给定一个字符串 ss，如何去掉其中的一个字符 \textit{ch}ch，使得得到的字符串字典序最小呢？答案是：找出最小的满足 s[i]>s[i+1]s[i]>s[i+1] 的下标 ii，并去除字符 s[i]s[i]。为了叙述方便，下文中称这样的字符为「关键字符」。

在理解这一点之后，就可以着手本题了。一个直观的思路是：我们在字符串 ss 中找到「关键字符」，去除它，然后不断进行这样的循环。但是这种朴素的解法会创建大量的中间字符串，我们有必要寻找一种更优的方法。

我们从前向后扫描原字符串。每扫描到一个位置，我们就尽可能地处理所有的「关键字符」。假定在扫描位置 s[i-1]s[i−1] 之前的所有「关键字符」都已经被去除完毕，在扫描字符 s[i]s[i] 时，新出现的「关键字符」只可能出现在 s[i]s[i] 或者其后面的位置。

于是，我们使用栈来维护去除「关键字符」后得到的字符串。如果栈顶字符大于当前字符 s[i]s[i]，说明栈顶字符为「关键字符」，故应当被去除。去除后，新的栈顶字符就与 s[i]s[i] 相邻了，我们继续比较新的栈顶字符与 s[i]s[i] 的大小。重复上述操作，直到栈为空或者栈顶字符不大于 s[i]s[i]。

我们还遗漏了一个要求：原字符串 ss 中的每个字符都需要出现在新字符串中，且只能出现一次。为了让新字符串满足该要求，之前讨论的算法需要进行以下两点的更改。

在考虑字符 s[i]s[i] 时，如果它已经存在于栈中，则不能加入字符 s[i]s[i]。为此，需要记录每个字符是否出现在栈中。

在弹出栈顶字符时，如果字符串在后面的位置上再也没有这一字符，则不能弹出栈顶字符。为此，需要记录每个字符的剩余数量，当这个值为 00 时，就不能弹出栈顶字符了。

代码

C++JavaJavaScriptGolangC

func removeDuplicateLetters(s string) string {
    left := [26]int{}
    for _, ch := range s {
        left[ch-'a']++
    }
    stack := []byte{}
    inStack := [26]bool{}
    for i := range s {
        ch := s[i]
        if !inStack[ch-'a'] {
            for len(stack) > 0 && ch < stack[len(stack)-1] {
                last := stack[len(stack)-1] - 'a'
                if left[last] == 0 {
                    break
                }
                stack = stack[:len(stack)-1]
                inStack[last] = false
            }
            stack = append(stack, ch)
            inStack[ch-'a'] = true
        }
        left[ch-'a']--
    }
    return string(stack)
}
复杂度分析

时间复杂度：O(N)O(N)，其中 NN 为字符串长度。代码中虽然有双重循环，但是每个字符至多只会入栈、出栈各一次。

空间复杂度：O(|\Sigma|)O(∣Σ∣)，其中 \SigmaΣ 为字符集合，本题中字符均为小写字母，所以 |\Sigma|=26∣Σ∣=26。由于栈中的字符不能重复，因此栈中最多只能有 |\Sigma|∣Σ∣ 个字符，另外需要维护两个数组，分别记录每个字符是否出现在栈中以及每个字符的剩余数量。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/remove-duplicate-letters/solution/qu-chu-zhong-fu-zi-mu-by-leetcode-soluti-vuso/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
