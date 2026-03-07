# encoding=utf8

'''
1888. Minimum Number of Flips to Make the Binary String Alternating

You are given a binary string s. You are allowed to perform two types of operations on the string in any sequence:

    Type-1: Remove the character at the start of the string s and append it to the end of the string.
    Type-2: Pick any character in s and flip its value, i.e., if its value is '0' it becomes '1' and vice-versa.

Return the minimum number of type-2 operations you need to perform such that s becomes alternating.

The string is called alternating if no two adjacent characters are equal.

    For example, the strings "010" and "1010" are alternating, while the string "0100" is not.

 

Example 1:

Input: s = "111000"
Output: 2
Explanation: Use the first operation two times to make s = "100011".
Then, use the second operation on the third and sixth elements to make s = "101010".

Example 2:

Input: s = "010"
Output: 0
Explanation: The string is already alternating.

Example 3:

Input: s = "1110"
Output: 1
Explanation: Use the second operation on the second element to make s = "1010".

 

Constraints:

    1 <= s.length <= 105
    s[i] is either '0' or '1'.


'''

class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        ss = s + s
        
        # Calculate initial cost for the first window against pattern "0101..."
        # Pattern: index k expects '0' if k%2==0 else '1'
        curr = 0
        for k in range(n):
            expected = '0' if k % 2 == 0 else '1'
            if ss[k] != expected:
                curr += 1
                
        min_ops = min(curr, n - curr)
        
        # Slide the window
        for i in range(n - 1):
            # Character leaving the window (at index i in ss, which was position 0 in the prev window)
            out_char = ss[i]
            # Character entering the window (at index i+n in ss, which will be position n-1 in the new window)
            in_char = ss[i + n]
            
            # Mismatch status of the outgoing character in the previous context (position 0, expected '0')
            out_mismatch = 1 if out_char != '0' else 0
            
            # Mismatch status of the incoming character in the new context (position n-1)
            expected_in = '0' if (n - 1) % 2 == 0 else '1'
            in_mismatch = 1 if in_char != expected_in else 0
            
            # Update current cost using the derived formula:
            # new_curr = (n - 1) - (curr - out_mismatch) + in_mismatch
            curr = n - 1 - curr + out_mismatch + in_mismatch
            
            # Update global minimum considering both patterns (curr and n-curr)
            min_ops = min(min_ops, curr, n - curr)
            
        return min_ops


