'''
140. 单词拆分 II
给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，在字符串中增加空格来构建一个句子，使得句子中所有的单词都在词典中。返回所有这些可能的句子。

说明：

分隔时可以重复使用字典中的单词。
你可以假设字典中没有重复的单词。
示例 1：

输入:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
输出:
[
  "cats and dog",
  "cat sand dog"
]
示例 2：

输入:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
输出:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
解释: 注意你可以重复使用字典中的单词。
示例 3：

输入:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
输出:
[]

140. Word Break II
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
Output:
[
  "cats and dog",
  "cat sand dog"
]
Example 2:

Input:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
Output:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
Explanation: Note that you are allowed to reuse a dictionary word.
Example 3:

Input:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
Output:
[]
'''


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        cache = {"":[]}
        def dfs(s):
            if s in cache:
                return cache[s]
            res = []
            for word in wordDict:
                if len(s) < len(word):
                    continue
                if s == word:
                    res = [word]
                if s.startswith(word):
                    pre = dfs(s[len(word):])
                    for p in pre:
                        res.append(word +" "+ p)
            cache[s] = res
            return res

        res = dfs(s)
        return res


class Solution20201101(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """

        memo = {len(s): ['']}

        def sentences(i):
            if i not in memo:
                memo[i] = [s[i:j] + (tail and ' ' + tail)
                           for j in range(i + 1, len(s) + 1)
                           if s[i:j] in wordDict
                           for tail in sentences(j)]
            return memo[i]

        return sentences(0)


# solution

'''
前言
这道题是「139. 单词拆分」的进阶，第 139 题要求判断是否可以拆分，这道题要求返回所有可能的拆分结果。

第 139 题可以使用动态规划的方法判断是否可以拆分，因此这道题也可以使用动态规划的思想。但是这道题如果使用自底向上的动态规划的方法进行拆分，则无法事先判断拆分的可行性，在不能拆分的情况下会超时。

例如以下例子，由于字符串 ss 中包含字母 \texttt{b}b，而单词列表 \textit{wordDict}wordDict 中的所有单词都由字母 \texttt{a}a 组成，不包含字母 \texttt{b}b，因此不能拆分，但是自底向上的动态规划仍然会在每个下标都进行大量的匹配，导致超时。


s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
为了避免动态规划的方法超时，需要首先使用第 139 题的代码进行判断，在可以拆分的情况下再使用动态规划的方法进行拆分。相比之下，自顶向下的记忆化搜索可以在搜索过程中将不可以拆分的情况进行剪枝，因此记忆化搜索是更优的做法。

方法一：记忆化搜索
对于字符串 ss，如果某个前缀是单词列表中的单词，则拆分出该单词，然后对 ss 的剩余部分继续拆分。如果可以将整个字符串 ss 拆分成单词列表中的单词，则得到一个句子。在对 ss 的剩余部分拆分得到一个句子之后，将拆分出的第一个单词（即 ss 的前缀）添加到句子的头部，即可得到一个完整的句子。上述过程可以通过回溯实现。

假设字符串 ss 的长度为 nn，回溯的时间复杂度在最坏情况下高达 O(n^n)O(n 
n
 )。时间复杂度高的原因是存在大量重复计算，可以通过记忆化的方式降低时间复杂度。

具体做法是，使用哈希表存储字符串 ss 的每个下标和从该下标开始的部分可以组成的句子列表，在回溯过程中如果遇到已经访问过的下标，则可以直接从哈希表得到结果，而不需要重复计算。如果到某个下标发现无法匹配，则哈希表中该下标对应的是空列表，因此可以对不能拆分的情况进行剪枝优化。

还有一个可优化之处为使用哈希集合存储单词列表中的单词，这样在判断一个字符串是否是单词列表中的单词时只需要判断该字符串是否在哈希集合中即可，而不再需要遍历单词列表。

JavaJavaScriptGolangC++Python3C

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        @lru_cache(None)
        def backtrack(index: int) -> List[List[str]]:
            if index == len(s):
                return [[]]
            ans = list()
            for i in range(index + 1, len(s) + 1):
                word = s[index:i]
                if word in wordSet:
                    nextWordBreaks = backtrack(i)
                    for nextWordBreak in nextWordBreaks:
                        ans.append(nextWordBreak.copy() + [word])
            return ans
        
        wordSet = set(wordDict)
        breakList = backtrack(0)
        return [" ".join(words[::-1]) for words in breakList]
复杂度分析

本题的时间与空间复杂度均为指数级别，较难进行具体的分析。在最坏的情况下，考虑下面这样一组测试数据：


s = "aaa...aaa"
wordDict = ["a","aa","aaa", ..., "aaa...aaa"]
显然，ss 的任意一种分隔方法均符合题目要求。即使我们忽略存储最终答案需要的空间，但在记忆化搜索的过程中缓存下来，防止重复计算而使用的空间不可以忽略。这一部分的占用的空间至少为 O(n \cdot 2^n)O(n⋅2 
n
 )，其中 nn 是 ss 的长度，即 ss 的分隔方法有 2^n2 
n
  种，每一种方法需要一个长度为 O(n)O(n) 的字符串进行存储。

对于时间复杂度部分，由于写入 O(n \cdot 2^n)O(n⋅2 
n
 ) 空间至少也需要 O(n \cdot 2^n)O(n⋅2 
n
 ) 的时间，因此时间复杂度同样为指数级别。

虽然记忆化搜索和普通的回溯方法的时间复杂度均为指数级别，但前者的底数为 22，后者的底数为 nn，因此记忆化搜索仍然具有一定的优越性。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/word-break-ii/solution/dan-ci-chai-fen-ii-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''