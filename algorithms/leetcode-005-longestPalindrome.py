class Solution(object):

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        maxStr = ""
        P = [[True if i==j else False for i in range(len(s))] for j in range(len(s))]

        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                if s[i] == s[j] and (j -i < 3 or P[i+1][j-1]):
                    P[i][j] = True
                if P[i][j] and (j - i + 1 > len(maxStr)):
                    maxStr = s[i:j+1]
        return maxStr

