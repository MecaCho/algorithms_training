'''
139. 单词拆分
给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。

说明：

拆分时可以重复使用字典中的单词。
你可以假设字典中没有重复的单词。
示例 1：

输入: s = "leetcode", wordDict = ["leet", "code"]
输出: true
解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。
示例 2：

输入: s = "applepenapple", wordDict = ["apple", "pen"]
输出: true
解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
     注意你可以重复使用字典中的单词。
示例 3：

输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
输出: false

139. Word Break
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
'''


# golang

'''
func wordBreak(s string, wordDict []string) bool {
    if len(s) < 1{
        return false
    }

	sort.Slice(wordDict, func(i, j int) bool {

		return len(wordDict[i]) > len(wordDict[j])

	})

	dp := []int{}

	for i := range s{

		dp = append(dp, 0)

		for _, word := range wordDict{
			wordLength := len(word)
			if s[:i+1] == word || (i >= wordLength && s[i-wordLength+1:i+1] == word && dp[i-wordLength] == 1) {
				dp[i] = 1
				break
			}

		}
	}

	return dp[len(s)-1] == 1
}
'''


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = []
        for i in range(len(s)):
            dp.append(any((s[:i+1] == word or (i > len(word) and dp[i-len(word)] and s[i-len(word):i+1]==word)) for word in wordDict))

        return dp[-1]


class Solution1(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """

        # res = []

        def dfs(s):
            res = []
            for word in wordDict:
                if len(s) < len(word):
                    continue
                if s == word:
                    res = [[word]]
                if s.startswith(word):
                    pre = dfs(s[len(word):])
                    for p in pre:
                        res.append([word] + p)
            return res

        res = dfs(s)
        return res

if __name__ == '__main__':
    s = "applepenappleapplepenappleapplep" \
        "enappleapplepenappleapplepenappleappl" \
        "epenappleapplepenappleapplepenappleapplepen" \
        "appleapplepenappleapplepenappleapplepenapplea" \
        "pplepenappleapplepenappleapplepenappleapplepenapp" \
        "leapplepenappleapplepenappleapplepenappleapplepen" \
        "appleapplepenappleapplepenappleapplepenappleapplepenapple"
    words = ["apple", "pen", "abcdef", "abcdef", "abcdefg"]

    # s = "catsandog"
    # words = ["cats", "dog", "sand", "and", "cat"]
    demo = Solution1()
    import time
    start = time.time()
    res = demo.wordBreak(s, words)
    end = time.time()
    print(end - start)
    print(res)
