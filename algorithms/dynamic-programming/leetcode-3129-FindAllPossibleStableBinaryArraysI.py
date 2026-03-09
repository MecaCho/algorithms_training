# encoding=utf8

'''

3129. Find All Possible Stable Binary Arrays I

You are given 3 positive integers zero, one, and limit.

A 
binary array
 arr is called stable if:

The number of occurrences of 0 in arr is exactly zero.
The number of occurrences of 1 in arr is exactly one.
Each 
subarray
 of arr with a size greater than limit must contain both 0 and 1.
Return the total number of stable binary arrays.

Since the answer may be very large, return it modulo 109 + 7.

 

Example 1:

Input: zero = 1, one = 1, limit = 2

Output: 2

Explanation:

The two possible stable binary arrays are [1,0] and [0,1], as both arrays have a single 0 and a single 1, and no subarray has a length greater than 2.

Example 2:

Input: zero = 1, one = 2, limit = 1

Output: 1

Explanation:

The only possible stable binary array is [1,0,1].

Note that the binary arrays [1,1,0] and [0,1,1] have subarrays of length 2 with identical elements, hence, they are not stable.

Example 3:

Input: zero = 3, one = 3, limit = 2

Output: 14

Explanation:

All the possible stable binary arrays are [0,0,1,0,1,1], [0,0,1,1,0,1], [0,1,0,0,1,1], [0,1,0,1,0,1], [0,1,0,1,1,0], [0,1,1,0,0,1], [0,1,1,0,1,0], [1,0,0,1,0,1], [1,0,0,1,1,0], [1,0,1,0,0,1], [1,0,1,0,1,0], [1,0,1,1,0,0], [1,1,0,0,1,0], and [1,1,0,1,0,0].

 

Constraints:

1 <= zero, one, limit <= 200


3129. 找出所有稳定的二进制数组 I

给你 3 个正整数 zero ，one 和 limit 。

一个 arr 如果满足以下条件，那么我们称它是 稳定的 ：

    0 在 arr 中出现次数 恰好 为 zero 。
    1 在 arr 中出现次数 恰好 为 one 。
    arr 中每个长度超过 limit 的 都 同时 包含 0 和 1 。

请你返回 稳定 二进制数组的 总 数目。

由于答案可能很大，将它对 109 + 7 取余 后返回。

 

示例 1：

输入：zero = 1, one = 1, limit = 2

输出：2

解释：

两个稳定的二进制数组为 [1,0] 和 [0,1] ，两个数组都有一个 0 和一个 1 ，且没有子数组长度大于 2 。

示例 2：

输入：zero = 1, one = 2, limit = 1

输出：1

解释：

唯一稳定的二进制数组是 [1,0,1] 。

二进制数组 [1,1,0] 和 [0,1,1] 都有长度为 2 且元素全都相同的子数组，所以它们不稳定。

示例 3：

输入：zero = 3, one = 3, limit = 2

输出：14

解释：

所有稳定的二进制数组包括 [0,0,1,0,1,1] ，[0,0,1,1,0,1] ，[0,1,0,0,1,1] ，[0,1,0,1,0,1] ，[0,1,0,1,1,0] ，[0,1,1,0,0,1] ，[0,1,1,0,1,0] ，[1,0,0,1,0,1] ，[1,0,0,1,1,0] ，[1,0,1,0,0,1] ，[1,0,1,0,1,0] ，[1,0,1,1,0,0] ，[1,1,0,0,1,0] 和 [1,1,0,1,0,0] 。

 

提示：

    1 <= zero, one, limit <= 200
'''

class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10**9 + 7
        
        # dp0[i][j] = number of stable arrays with i zeros and j ones, ending in 0
        # dp1[i][j] = number of stable arrays with i zeros and j ones, ending in 1
        dp0 = [[0] * (one + 1) for _ in range(zero + 1)]
        dp1 = [[0] * (one + 1) for _ in range(zero + 1)]
        
        # Base cases initialization is handled within the loop logic naturally, 
        # but let's be explicit about the "only zeros" or "only ones" scenarios.
        
        for i in range(zero + 1):
            for j in range(one + 1):
                if i == 0 and j == 0:
                    continue
                
                # Calculate dp0[i][j]: Ends with 0
                if i > 0:
                    if j == 0:
                        # Only zeros available. Valid only if total zeros <= limit
                        if i <= limit:
                            dp0[i][j] = 1
                        else:
                            dp0[i][j] = 0
                    else:
                        # Sum dp1[i-k][j] for k in 1..limit
                        total = 0
                        for k in range(1, min(i, limit) + 1):
                            total = (total + dp1[i-k][j]) % MOD
                        dp0[i][j] = total
                
                # Calculate dp1[i][j]: Ends with 1
                if j > 0:
                    if i == 0:
                        # Only ones available. Valid only if total ones <= limit
                        if j <= limit:
                            dp1[i][j] = 1
                        else:
                            dp1[i][j] = 0
                    else:
                        # Sum dp0[i][j-k] for k in 1..limit
                        total = 0
                        for k in range(1, min(j, limit) + 1):
                            total = (total + dp0[i][j-k]) % MOD
                        dp1[i][j] = total

        return (dp0[zero][one] + dp1[zero][one]) % MOD

