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

'''
Approach 1: Longest Common Substring
Approach 2: Brute Force
Approach 3: Dynamic Programming

To improve over the brute force solution, we first observe how we can avoid unnecessary re-computation while validating palindromes. Consider the case "ababa". If we already knew that "bab" is a palindrome, it is obvious that "ababa" must be a palindrome since the two left and right end letters are the same.

Approach 4: Expand Around Center
    
Approach 5: Manacher's Algorithm
'''
