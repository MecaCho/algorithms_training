# encoding=utf8

'''
2595. Number of Even and Odd Bits

You are given a positive integer n.

Let even denote the number of even indices in the binary representation of n with value 1.

Let odd denote the number of odd indices in the binary representation of n with value 1.

Note that bits are indexed from right to left in the binary representation of a number.

Return the array [even, odd].

 

Example 1:

Input: n = 50

Output: [1,2]

Explanation:

The binary representation of 50 is 110010.

It contains 1 on indices 1, 4, and 5.

Example 2:

Input: n = 2

Output: [0,1]

Explanation:

The binary representation of 2 is 10.

It contains 1 only on index 1.

 

Constraints:

1 <= n <= 1000
'''

class Solution:
    def evenOddBit(self, n: int) -> List[int]:
            binary_rep = bin(n)[2:]
    
            even_count = 0
            odd_count = 0
            
            for i in range(len(binary_rep)):
                if binary_rep[-(i+1)] == '1':  
                    if i % 2 == 0:
                        even_count += 1  
                    else:
                        odd_count += 1   
                        
            return [even_count, odd_count]

class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        res = [0, 0]
        i = 0
        while n:
            res[i] += n & 1
            n >>= 1
            i = i ^ 1
        return res

