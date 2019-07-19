class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        ret = [False] * (len(s))
        if not wordDict:
            return False
        if not s:
            return True
        wordDict.sort(key=lambda x: len(x))
        max_len = len(wordDict[-1])

        for i in xrange(len(s)):
            start = 0

            while start <= max_len and i - start >= 0:
                if (ret[i - start - 1] and s[i - start:i + 1] in wordDict) or s[:i + 1] in wordDict:
                    ret[i] = True
                    break
                start += 1

        return ret[-1]
