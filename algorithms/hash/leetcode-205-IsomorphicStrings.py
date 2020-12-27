# encoding=utf8

'''
205. 同构字符串
给定两个字符串 s 和 t，判断它们是否是同构的。

如果 s 中的字符可以被替换得到 t ，那么这两个字符串是同构的。

所有出现的字符都必须用另一个字符替换，同时保留字符的顺序。两个字符不能映射到同一个字符上，但字符可以映射自己本身。

示例 1:

输入: s = "egg", t = "add"
输出: true
示例 2:

输入: s = "foo", t = "bar"
输出: false
示例 3:

输入: s = "paper", t = "title"
输出: true
说明:
你可以假设 s 和 t 具有相同的长度。

205. Isomorphic Strings
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
Note:
You may assume both s and t have the same length.
'''


class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        # hash_map = {}
        # for i in range(len(s)):
        #     if s[i] not in hash_map.keys() and t[i] not in hash_map.values():
        #         hash_map[s[i]] = t[i]
        #     elif s[i] in hash_map:
        #         if hash_map[s[i]] != t[i]:
        #             return False
        #     elif t[i] in hash_map.values():
        #         return False
        # return True
        s_indexs = []
        t_indexs = []
        s_map = {}
        t_map = {}
        for i in range(len(s)):
            if s[i] in s_map:
                s_indexs.append(s_map[s[i]])
            else:
                s_map[s[i]] = i
                s_indexs.append(i)
            if t[i] in t_map:
                t_indexs.append(t_map[t[i]])
            else:
                t_map[t[i]] = i
                t_indexs.append(i)
            if s_indexs != t_indexs:
                return False
        return True



class Solution20201227(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        for i in range(len(s)):
            if s.index(s[i]) != t.index(t[i]):
                return False

        return True


# solution

'''
方法一：哈希表
此题是「290. 单词规律」的简化版，需要我们判断 ss 和 tt 每个位置上的字符是否都一一对应，即 ss 的任意一个字符被 tt 中唯一的字符对应，同时 tt 的任意一个字符被 ss 中唯一的字符对应。这也被称为「双射」的关系。

以示例 22 为例，tt 中的字符 aa 和 rr 虽然有唯一的映射 oo，但对于 ss 中的字符 oo 来说其存在两个映射 \{a,r\}{a,r}，故不满足条件。

因此，我们维护两张哈希表，第一张哈希表 \textit{s2t}s2t 以 ss 中字符为键，映射至 tt 的字符为值，第二张哈希表 \textit{t2s}t2s 以 tt 中字符为键，映射至 ss 的字符为值。从左至右遍历两个字符串的字符，不断更新两张哈希表，如果出现冲突（即当前下标 \textit{index}index 对应的字符 s[\textit{index}]s[index] 已经存在映射且不为 t[\textit{index}]t[index] 或当前下标 \textit{index}index 对应的字符 t[\textit{index}]t[index] 已经存在映射且不为 s[\textit{index}]s[index]）时说明两个字符串无法构成同构，返回 \rm falsefalse。

如果遍历结束没有出现冲突，则表明两个字符串是同构的，返回 \rm truetrue 即可。

C++JavaJavaScriptGolangC

func isIsomorphic(s, t string) bool {
    s2t := map[byte]byte{}
    t2s := map[byte]byte{}
    for i := range s {
        x, y := s[i], t[i]
        if s2t[x] > 0 && s2t[x] != y || t2s[y] > 0 && t2s[y] != x {
            return false
        }
        s2t[x] = y
        t2s[y] = x
    }
    return true
}
复杂度分析

时间复杂度：O(n)O(n)，其中 nn 为字符串的长度。我们只需同时遍历一遍字符串 ss 和 tt 即可。
空间复杂度：O(|\Sigma|)O(∣Σ∣)，其中 \SigmaΣ 是字符串的字符集。哈希表存储字符的空间取决于字符串的字符集大小，最坏情况下每个字符均不相同，需要 O(|\Sigma|)O(∣Σ∣) 的空间。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/isomorphic-strings/solution/tong-gou-zi-fu-chuan-by-leetcode-solutio-s6fd/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
