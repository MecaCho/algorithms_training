# encoding=utf8

'''
3130. Find All Possible Stable Binary Arrays II

You are given 3 positive integers zero, one, and limit.

A binary array arr is called stable if:

The number of occurrences of 0 in arr is exactly zero.
The number of occurrences of 1 in arr is exactly one.
Each subarray of arr with a size greater than limit must contain both 0 and 1.
Return the total number of stable binary arrays.

Since the answer may be very large, return it modulo 109 + 7.

 

Example 1:

Input: zero = 1, one = 1, limit = 2

Output: 2

Explanation:

The two possible stable binary arrays are [1,0] and [0,1].

Example 2:

Input: zero = 1, one = 2, limit = 1

Output: 1

Explanation:

The only possible stable binary array is [1,0,1].

Example 3:

Input: zero = 3, one = 3, limit = 2

Output: 14

Explanation:

All the possible stable binary arrays are [0,0,1,0,1,1], [0,0,1,1,0,1], [0,1,0,0,1,1], [0,1,0,1,0,1], [0,1,0,1,1,0], [0,1,1,0,0,1], [0,1,1,0,1,0], [1,0,0,1,0,1], [1,0,0,1,1,0], [1,0,1,0,0,1], [1,0,1,0,1,0], [1,0,1,1,0,0], [1,1,0,0,1,0], and [1,1,0,1,0,0].

 

Constraints:

1 <= zero, one, limit <= 1000
'''

class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10**9 + 7
        
        # dp0[i][j] = ways to form array with i zeros and j ones, ending in 0
        # dp1[i][j] = ways to form array with i zeros and j ones, ending in 1
        dp0 = [[0] * (one + 1) for _ in range(zero + 1)]
        dp1 = [[0] * (one + 1) for _ in range(zero + 1)]
        
        # Base cases:
        # If we only have zeros (j=0), valid only if count <= limit
        for i in range(1, min(zero, limit) + 1):
            dp0[i][0] = 1
            
        # If we only have ones (i=0), valid only if count <= limit
        for j in range(1, min(one, limit) + 1):
            dp1[0][j] = 1
            
        # Fill DP table
        for i in range(1, zero + 1):
            # Maintain a sliding window sum for dp1[...][j] to compute dp0[i][j]
            # We need sum(dp1[i-k][j]) for 1 <= k <= limit
            # Which is sum(dp1[x][j]) for i-limit <= x <= i-1
            
            current_sum_0 = 0
            
            for j in range(1, one + 1):
                # --- Calculate dp0[i][j] ---
                # Add the new element entering the window: dp1[i-1][j]
                current_sum_0 = (current_sum_0 + dp1[i-1][j]) % MOD
                
                # Remove the element leaving the window: dp1[i-limit-1][j]
                if i - limit - 1 >= 0:
                    current_sum_0 = (current_sum_0 - dp1[i-limit-1][j] + MOD) % MOD
                
                dp0[i][j] = current_sum_0
                
                # --- Calculate dp1[i][j] ---
                # We need a separate sliding window for dp1 calculation? 
                # Actually, we can compute dp1[i][j] using a similar logic but iterating differently?
                # No, the dependency for dp1[i][j] is on dp0[i][j-k]. 
                # Since we are iterating i then j, when we are at (i, j), 
                # we have already computed dp0[i][0...j-1]. 
                # So we can maintain a sliding window sum for the row i of dp0.
                
                # However, note that dp0[i][j] was just computed. 
                # The transition for dp1[i][j] depends on dp0[i][j-k].
                # This requires a sliding window over 'j' for a fixed 'i'.
                # We can maintain this sum inside the j loop.
                
                # Let's restructure slightly to handle both sums cleanly.
                # But wait, the logic above for dp0 used a vertical window (varying i, fixed j).
                # The logic for dp1 needs a horizontal window (fixed i, varying j).
                
                # Let's restart the inner logic to be clearer.
                pass

        # Re-implementing the loops with clear sliding windows for both directions
        # Resetting DP for clarity in the final block
        dp0 = [[0] * (one + 1) for _ in range(zero + 1)]
        dp1 = [[0] * (one + 1) for _ in range(zero + 1)]

        # Base cases again
        for i in range(1, min(zero, limit) + 1):
            dp0[i][0] = 1
        for j in range(1, min(one, limit) + 1):
            dp1[0][j] = 1

        for i in range(1, zero + 1):
            sum_for_dp0 = 0 # Maintains sum of dp1[i-k][j] for current j
            sum_for_dp1 = 0 # Maintains sum of dp0[i][j-k] for current i
            
            # We need to iterate j. But sum_for_dp0 depends on column j, varying i.
            # sum_for_dp1 depends on row i, varying j.
            
            # Strategy:
            # 1. Pre-calculate or maintain sum_for_dp0 as we iterate i? 
            #    Actually, for a fixed j, as i increases, the window slides.
            #    But we are iterating i then j. 
            #    So for a fixed i, we iterate j. 
            #    For dp0[i][j], we need sum of dp1[x][j] where x in [i-limit, i-1].
            #    Since j changes every step, we can't easily maintain a single variable for sum_for_dp0 
            #    unless we store the column sums or recompute. 
            #    Recomputing is O(limit). Total O(Z*O*limit). With 1000^3 = 1e9, it's risky.
            #    
            # Alternative: Swap loops? Iterate j then i?
            # If we iterate j then i:
            #   For fixed j, as i increments, we can maintain sum_for_dp0 easily.
            #   But calculating dp1[i][j] needs sum of dp0[i][y] for y in [j-limit, j-1].
            #   Since i is changing, and we need a window over j for the *current* i,
            #   this suggests we need to maintain the row-sum dynamically.
            
            # Best Approach: Two passes or careful state maintenance.
            # Actually, O(Z*O*limit) in Python might TLE. Let's try to optimize both.
            # We can maintain the sliding window sum for dp0 vertically (over i) 
            # by storing an auxiliary array `col_sum[j]` that updates as i increases.
            # And maintain sliding window for dp1 horizontally (over j) inside the j loop.
            
            pass

        # Final Optimized Implementation
        dp0 = [[0] * (one + 1) for _ in range(zero + 1)]
        dp1 = [[0] * (one + 1) for _ in range(zero + 1)]
        
        # Base cases
        for i in range(1, min(zero, limit) + 1):
            dp0[i][0] = 1
        for j in range(1, min(one, limit) + 1):
            dp1[0][j] = 1
            
        # Auxiliary array to maintain the vertical sliding window sum for dp1
        # col_sum[j] will store sum(dp1[i-k][j]) for k in 1..limit
        col_sum = [0] * (one + 1)
        
        for i in range(1, zero + 1):
            # Reset horizontal sum for dp1 calculation for this row
            row_sum = 0
            
            for j in range(1, one + 1):
                # Update vertical window for dp0[i][j]
                # Add dp1[i-1][j] to the window
                col_sum[j] = (col_sum[j] + dp1[i-1][j]) % MOD
                # Remove dp1[i-limit-1][j] from the window if applicable
                if i > limit:
                    col_sum[j] = (col_sum[j] - dp1[i-limit-1][j] + MOD) % MOD
                
                dp0[i][j] = col_sum[j]
                
                # Update horizontal window for dp1[i][j]
                # Add dp0[i][j-1] to the window
                row_sum = (row_sum + dp0[i][j-1]) % MOD
                # Remove dp0[i][j-limit-1] from the window if applicable
                if j > limit:
                    row_sum = (row_sum - dp0[i][j-limit-1] + MOD) % MOD
                
                dp1[i][j] = row_sum

        return (dp0[zero][one] + dp1[zero][one]) % MOD

