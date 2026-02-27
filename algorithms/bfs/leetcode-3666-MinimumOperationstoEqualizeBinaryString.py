# encoding=utf8

'''
3666. Minimum Operations to Equalize Binary String

You are given a binary string s, and an integer k.

In one operation, you must choose exactly k different indices and flip each '0' to '1' and each '1' to '0'.

Return the minimum number of operations required to make all characters in the string equal to '1'. If it is not possible, return -1.

 

Example 1:

Input: s = "110", k = 1

Output: 1

Explanation:

    There is one '0' in s.
    Since k = 1, we can flip it directly in one operation.

Example 2:

Input: s = "0101", k = 3

Output: 2

Explanation:

One optimal set of operations choosing k = 3 indices in each operation is:

    Operation 1: Flip indices [0, 1, 3]. s changes from "0101" to "1000".
    Operation 2: Flip indices [1, 2, 3]. s changes from "1000" to "1111".

Thus, the minimum number of operations is 2.

Example 3:

Input: s = "101", k = 2

Output: -1

Explanation:

Since k = 2 and s has only one '0', it is impossible to flip exactly k indices to make all '1'. Hence, the answer is -1.

 

Constraints:

    1 <= s.length <= 10​​​​​​​5
    s[i] is either '0' or '1'.
    1 <= k <= s.length
'''

class Solution:
    def minOperations(self, s: str, k: int) -> int:
        n = len(s)
        c = s.count('0')
        
        if c == 0:
            return 0
        
        if k == n:
            return 1 if c == n else -1
        
        if k % 2 == 0 and c % 2 != 0:
            return -1
        
        m = (c + k - 1) // k
        
        while True:
            total = m * k
            if total < c:
                m += 1
                continue
            
            if (total - c) % 2 != 0:
                m += 1
                continue
            
            # Calculate max capacity
            # Zero columns (need odd): max val is m if m is odd, else m-1
            cap_z = m if m % 2 == 1 else m - 1
            # One columns (need even): max val is m if m is even, else m-1
            cap_o = m if m % 2 == 0 else m - 1
            
            max_possible = c * cap_z + (n - c) * cap_o
            
            if total <= max_possible:
                return m
            
            m += 1
            
