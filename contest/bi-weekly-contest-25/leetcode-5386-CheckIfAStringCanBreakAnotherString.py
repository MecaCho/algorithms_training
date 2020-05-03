
'''
Given two strings: s1 and s2 with the same size, check if some permutation of string s1 can break some permutation of string s2 or vice-versa (in other words s2 can break s1).

A string x can break string y (both of size n) if x[i] >= y[i] (in alphabetical order) for all i between 0 and n-1.



Example 1:

Input: s1 = "abc", s2 = "xya"
Output: true
Explanation: "ayx" is a permutation of s2="xya" which can break to string "abc" which is a permutation of s1="abc".
Example 2:

Input: s1 = "abe", s2 = "acd"
Output: false
Explanation: All permutations for s1="abe" are: "abe", "aeb", "bae", "bea", "eab" and "eba" and all permutation for s2="acd" are: "acd", "adc", "cad", "cda", "dac" and "dca". However, there is not any permutation from s1 which can break some permutation from s2 and vice-versa.
Example 3:

Input: s1 = "leetcodee", s2 = "interview"
Output: true


Constraints:

s1.length == n
s2.length == n
1 <= n <= 10^5
All strings consist of lowercase English letters.
'''

class Solution(object):
    def checkIfCanBreak(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        s1_list = sorted(list(s1))
        s2_list = sorted(list(s2))
        count = 0
        # print(s1_list, s2_list)
        for i in range(len(s1)):
            c = 0
            if s1_list[i] > s2_list[i]:
                c = 1
            elif s1_list[i] < s2_list[i]:
                c = -1
            # print(count, c)
            if count > 0 and c == -1 or (count < 0 and c == 1):
                return False
            count += c
        return True



if __name__ == '__main__':
    demo = Solution()
    cases = [("abe", "acd"), ("leetcodee", "interview"), ("abc", "xya")]
    for s1, s2 in cases:
        res = demo.checkIfCanBreak(s1, s2)
        print(res)