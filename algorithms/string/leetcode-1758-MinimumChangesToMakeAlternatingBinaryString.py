# encoding=utf8

'''
1758. Minimum Changes To Make Alternating Binary String
You are given a string s consisting only of the characters '0' and '1'. In one operation, you can change any '0' to '1' or vice versa.

The string is called alternating if no two adjacent characters are equal. For example, the string "010" is alternating, while the string "0100" is not.

Return the minimum number of operations needed to make s alternating.

 

Example 1:

Input: s = "0100"
Output: 1
Explanation: If you change the last character to '1', s will be "0101", which is alternating.
Example 2:

Input: s = "10"
Output: 0
Explanation: s is already alternating.
Example 3:

Input: s = "1111"
Output: 2
Explanation: You need two operations to reach "0101" or "1010".
 

Constraints:

1 <= s.length <= 104
s[i] is either '0' or '1'.
'''

class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        a = sum([int(s[i]) == (i%2) for i in range(n)])
        return min(a, n-a)


class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        diff_start_0 = 0
        
        # Calculate cost to transform s into "010101..."
        for i in range(n):
            # Expected character for pattern starting with '0':
            # Even index -> '0', Odd index -> '1'
            expected = '0' if i % 2 == 0 else '1'
            
            if s[i] != expected:
                diff_start_0 += 1
                
        # The cost for the other pattern ("101010...") is simply n - diff_start_0
        diff_start_1 = n - diff_start_0
        
        return min(diff_start_0, diff_start_1)

