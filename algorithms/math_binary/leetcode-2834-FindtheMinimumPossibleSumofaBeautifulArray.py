# encoding=utf8

'''
2834. Find the Minimum Possible Sum of a Beautiful Array

You are given positive integers n and target.

An array nums is beautiful if it meets the following conditions:

nums.length == n.
nums consists of pairwise distinct positive integers.
There doesn't exist two distinct indices, i and j, in the range [0, n - 1], such that nums[i] + nums[j] == target.
Return the minimum possible sum that a beautiful array could have modulo 109 + 7.

 

Example 1:

Input: n = 2, target = 3
Output: 4
Explanation: We can see that nums = [1,3] is beautiful.
- The array nums has length n = 2.
- The array nums consists of pairwise distinct positive integers.
- There doesn't exist two distinct indices, i and j, with nums[i] + nums[j] == 3.
It can be proven that 4 is the minimum possible sum that a beautiful array could have.
Example 2:

Input: n = 3, target = 3
Output: 8
Explanation: We can see that nums = [1,3,4] is beautiful.
- The array nums has length n = 3.
- The array nums consists of pairwise distinct positive integers.
- There doesn't exist two distinct indices, i and j, with nums[i] + nums[j] == 3.
It can be proven that 8 is the minimum possible sum that a beautiful array could have.
Example 3:

Input: n = 1, target = 1
Output: 1
Explanation: We can see, that nums = [1] is beautiful.
 

Constraints:

1 <= n <= 109
1 <= target <= 109
'''

class Solution:
    def minimumPossibleSum(self, n: int, target: int) -> int:
        mod = 10**9 + 7
        m = target // 2
        if n <= m:
            return ((1 + n) * n // 2) % mod
        return ((1 + m) * m // 2 + (target * 2 + (n - m) - 1) * (n - m) // 2) % mod

# tips

'''
我们需要构造一个大小为 nnn 的正整数数组，该数组由不同的数字组成，并且没有任意两个数字的和等于 target\textit{target}target，在满足这样的前提下，要保证数组的和最小。

为了让数组之和最小，我们按照 1,2,3,⋯1,2,3,\cdots1,2,3,⋯ 的顺序考虑，但添加了 xxx 之后，就不能添加 target−x\textit{target} - xtarget−x，因此最大可以添加到 ⌊target/2⌋\lfloor\textit{target} / 2\rfloor⌊target/2⌋，如果个数还不够 nnn 个，就继续从 target,target+1,target+2,⋯\textit{target}, \textit{target} + 1, \textit{target} + 2, \cdotstarget,target+1,target+2,⋯ 依次添加。由于添加的数字是连续的，所以可以用等差数列求和公式快速求解。


'''
