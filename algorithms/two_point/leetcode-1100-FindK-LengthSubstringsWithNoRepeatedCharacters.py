
'''

1100. 长度为 K 的无重复字符子串
给你一个字符串 S，找出所有长度为 K 且不含重复字符的子串，请你返回全部满足要求的子串的 数目。



示例 1：

输入：S = "havefunonleetcode", K = 5
输出：6
解释：
这里有 6 个满足题意的子串，分别是：'havef','avefu','vefun','efuno','etcod','tcode'。
示例 2：

输入：S = "home", K = 5
输出：0
解释：
注意：K 可能会大于 S 的长度。在这种情况下，就无法找到任何长度为 K 的子串。


提示：

1 <= S.length <= 10^4
S 中的所有字符均为小写英文字母
1 <= K <= 10^4

1100. Find K-Length Substrings With No Repeated Characters
Given a string S, return the number of substrings of length K with no repeated characters.



Example 1:

Input: S = "havefunonleetcode", K = 5
Output: 6
Explanation:
There are 6 substrings they are : 'havef','avefu','vefun','efuno','etcod','tcode'.
Example 2:

Input: S = "home", K = 5
Output: 0
Explanation:
Notice K can be larger than the length of S. In this case is not possible to find any substring.


Note:

1 <= S.length <= 10^4
All characters of S are lowercase English letters.
1 <= K <= 10^4
'''






class Solution(object):
    def numKLenSubstrNoRepeats(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: int
        """
        hash_map = {}
        res = []
        for i in range(len(S)):
            hash_map[S[i]] = i
            min_index = min(hash_map.values())
            if len(hash_map) == K and i - min_index + 1 == K:
                res.append(S[min_index:min_index+K])
            if len(hash_map) == K:
                hash_map.pop(S[min_index])

        return len(res)
