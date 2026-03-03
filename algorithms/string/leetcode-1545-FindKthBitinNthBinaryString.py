# encoding=utf8

'''
1545. Find Kth Bit in Nth Binary String

Given two positive integers n and k, the binary string Sn is formed as follows:

    S1 = "0"
    Si = Si - 1 + "1" + reverse(invert(Si - 1)) for i > 1

Where + denotes the concatenation operation, reverse(x) returns the reversed string x, and invert(x) inverts all the bits in x (0 changes to 1 and 1 changes to 0).

For example, the first four strings in the above sequence are:

    S1 = "0"
    S2 = "011"
    S3 = "0111001"
    S4 = "011100110110001"

Return the kth bit in Sn. It is guaranteed that k is valid for the given n.

 

Example 1:

Input: n = 3, k = 1
Output: "0"
Explanation: S3 is "0111001".
The 1st bit is "0".

Example 2:

Input: n = 4, k = 11
Output: "1"
Explanation: S4 is "011100110110001".
The 11th bit is "1".

 

Constraints:

    1 <= n <= 20
    1 <= k <= 2n - 1
'''

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        # Base case: S1 is "0"
        if n == 1:
            return "0"
        
        # The length of S_{n-1} is 2^(n-1) - 1
        # The middle '1' is at position 2^(n-1)
        mid = 1 << (n - 1)
        
        if k < mid:
            # Case 1: In the left part (S_{n-1})
            return self.findKthBit(n - 1, k)
        elif k == mid:
            # Case 2: The middle element
            return "1"
        else:
            # Case 3: In the right part (reverse(invert(S_{n-1})))
            # Find the corresponding position in S_{n-1}
            # The mapping is symmetric around the middle '1'
            k_mirror = 2 * mid - k
            
            # Get the bit from the recursive call and invert it
            bit = self.findKthBit(n - 1, k_mirror)
            return "1" if bit == "0" else "0"

