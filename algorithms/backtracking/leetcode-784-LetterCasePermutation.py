# encoding=utf8

'''
784. 字母大小写全排列
给定一个字符串S，通过将字符串S中的每个字母转变大小写，我们可以获得一个新的字符串。返回所有可能得到的字符串集合。

示例:
输入: S = "a1b2"
输出: ["a1b2", "a1B2", "A1b2", "A1B2"]

输入: S = "3z4"
输出: ["3z4", "3Z4"]

输入: S = "12345"
输出: ["12345"]
注意：

S 的长度不超过12。
S 仅由数字和字母组成。

784. Letter Case Permutation
Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.  Return a list of all possible strings we could create.

Examples:
Input: S = "a1b2"
Output: ["a1b2", "a1B2", "A1b2", "A1B2"]

Input: S = "3z4"
Output: ["3z4", "3Z4"]

Input: S = "12345"
Output: ["12345"]
Note:

S will be a string with length between 1 and 12.
S will consist only of letters or digits.
'''


class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        if not S:
            return [""]
        upper_str = S.upper()
        S = S.lower()
        if upper_str == S:
            return [S]
        self.vals = []

        def backtrack(res, n):
            if n == len(S):
                self.vals.append(res)
            else:
                if res[n] != upper_str[n]:
                    backtrack(res[:n] + res[n].upper() + res[n + 1:], n + 1)
                backtrack(res, n + 1)

        backtrack(S, 0)
        return self.vals[::-1]
    
class Solution1:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = []
        m = sum(1 if c.isalpha() else 0 for c in s)
        for mask in range(2**m):
            tmp = []
            k = 0
            for c in s:
                if c.isalpha():
                    if (mask >> k) & 1 == 1:
                        tmp.append(c.upper())
                    else:
                        tmp.append(c.lower())
                    k += 1
                else:
                    tmp.append(c)
            res.append("".join(tmp))
        return res


'''
方法一：递归【通过】
思路

从左往右依次遍历字符，过程中保持 ans 为已遍历过字符的字母大小全排列。

例如，当 S = "abc" 时，考虑字母 "a", "b", "c"，初始令 ans = [""]，依次更新 ans = ["a", "A"]， ans = ["ab", "Ab", "aB", "AB"]， ans = ["abc", "Abc", "aBc", "ABc", "abC", "AbC", "aBC", "ABC"]。

算法

如果下一个字符 c 是字母，将当前已遍历过的字符串全排列复制两份，在第一份的每个字符串末尾添加 lowercase(c)，在第二份的每个字符串末尾添加 uppercase(c)。

如果下一个字符 c 是数字，将 c 直接添加到每个字符串的末尾。

JavaPython
class Solution(object):
    def letterCasePermutation(self, S):
        ans = [[]]

        for char in S:
            n = len(ans)
            if char.isalpha():
                for i in xrange(n):
                    ans.append(ans[i][:])
                    ans[i].append(char.lower())
                    ans[n+i].append(char.upper())
            else:
                for i in xrange(n):
                    ans[i].append(char)

        return map("".join, ans)
复杂度分析

时间复杂度：O(2^{N} * N)O(2 
N
 ∗N)，其中 NN 是 S 的长度。

空间复杂度：O(2^N * N)O(2 
N
 ∗N)。

方法二：二分掩码【通过】
思路

假设字符串 S 有 BB 个字母，那么全排列就有 2^B2 
B
  个字符串，且可以用位掩码 bits 唯一地表示。

例如，可以用 00 表示 a7b， 01 表示 a7B， 10 表示 A7b， 11 表示 A7B。注意数字不是掩码的一部分。

算法

根据位掩码，构造正确的全排列结果。如果下一个字符是字母，则根据位掩码添加小写或大写字母。 否则添加对应的数字。

JavaPython
class Solution(object):
    def letterCasePermutation(self, S):
        B = sum(letter.isalpha() for letter in S)
        ans = []

        for bits in xrange(1 << B):
            b = 0
            word = []
            for letter in S:
                if letter.isalpha():
                    if (bits >> b) & 1:
                        word.append(letter.lower())
                    else:
                        word.append(letter.upper())

                    b += 1
                else:
                    word.append(letter)

            ans.append("".join(word))
        return ans
复杂度分析

时间和空间复杂度：O(2^{N} * N)O(2 
N
 ∗N)，与方法一分析相同。
方法三： 内置函数库【通过】
思路和算法

集合的笛卡尔乘积是从所有集合中选择每种可能的组合。例如 {1, 2 } x {a, b, c} = {1a, 1b, 1c, 2a, 2b, 2c}。

对于具有内置函数来计算笛卡尔积的语言，可以直接调用内置函数减少工作量。

Python
class Solution(object):
    def letterCasePermutation(self, S):
        f = lambda x: (x.lower(), x.upper()) if x.isalpha() else x
        return map("".join, itertools.product(*map(f, S)))
复杂度分析

时间和空间复杂度：O(2^{N} * N)O(2 
N
 ∗N)，与方法一分析相同。

作者：LeetCode
链接：https://leetcode-cn.com/problems/letter-case-permutation/solution/zi-mu-da-xiao-xie-quan-pai-lie-by-leetcode/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
