
'''
718. 最长重复子数组
给两个整数数组 A 和 B ，返回两个数组中公共的、长度最长的子数组的长度。

示例 1:

输入:
A: [1,2,3,2,1]
B: [3,2,1,4,7]
输出: 3
解释:
长度最长的公共子数组是 [3, 2, 1]。
说明:

1 <= len(A), len(B) <= 1000
0 <= A[i], B[i] < 100

718. Maximum Length of Repeated Subarray
Given two integer arrays A and B, return the maximum length of an subarray that appears in both arrays.

Example 1:

Input:
A: [1,2,3,2,1]
B: [3,2,1,4,7]
Output: 3
Explanation:
The repeated subarray with maximum length is [3, 2, 1].


Note:

1 <= len(A), len(B) <= 1000
0 <= A[i], B[i] < 100

'''


class Solution(object):
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        dp = [[0 for _ in range(len(A)+1)] for _ in range(len(B)+1)]
        res = 0
        for i in range(1,len(A)+1):
            for j in range(1,len(B)+1):
                if A[i-1] == B[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                    res = max(res, dp[i][j])
        return res


# tips

'''
Use dynamic programming. dp[i][j] will be the answer for inputs A[i:], B[j:].
'''

# solutions

'''
方法一：穷举 + 哈希表 [超出时间限制]
在最简单的穷举法中，我们穷举数组 A 中的起始位置 i 和数组 B 中的起始位置 j，随后超出最大的满足 A[i: i + k] == B[j: j + k] 的 k。这个过程的伪代码如下：

ans = 0
for i in [0 .. A.length - 1]:
    for j in [0 .. B.length - 1]:
        k = 0
        while (A[i+k] == B[j+k]): k += 1 #and i+k < A.length etc.
        ans = max(ans, k)
在多数情况下，A[i] 和 B[j] 不相等，因此我们可以将 B 中所有的字符存入哈希表 Bstarts，哈希表的键为字符，值为字符在 B 中出现的位置。那么在穷举 i 时，我们只需要穷举 Bstarts[A[i]] 中的所有位置作为 j 即可。但这样做并不能减少时间复杂度。

PythonJava
class Solution(object):
    def findLength(self, A, B):
        ans = 0
        Bstarts = collections.defaultdict(list)
        for j, y in enumerate(B):
            Bstarts[y].append(j)

        for i, x in enumerate(A):
            for j in Bstarts[x]:
                k = 0
                while i+k < len(A) and j+k < len(B) and A[i+k] == B[j+k]:
                    k += 1
                ans = max(ans, k)
        return ans
复杂度分析

时间复杂度：O(M*N\min(M，N))O(M∗Nmin(M，N))，其中 MM 和 NN 分别是数组 A 和 B 的长度。
空间复杂度：O(N)O(N)。
方法二：二分查找 + 简单判断 [超出时间限制]
如果数组 A 和 B 有一个长度为 k 的公共子数组，那么它们一定有长度为 j <= k 的公共子数组。这样我们可以通过二分查找的方法找到最大的 k。

二分查找的下界为 0，上界为 min(len(A), len(B))。在二分查找的每一步中，我们仍然使用最简单的判断方法，即找出数组 A 和 B 中所有长度为 mid 的子数组，判断是否存在一个子数组在 A 和 B 中都出现过。

PythonJava
class Solution(object):
    def findLength(self, A, B):
        def check(length):
            seen = set(tuple(A[i:i+length])
                       for i in xrange(len(A) - length + 1))
            return any(tuple(B[j:j+length]) in seen
                       for j in xrange(len(B) - length + 1))

        lo, hi = 0, min(len(A), len(B)) + 1
        while lo < hi:
            mi = (lo + hi) / 2
            if check(mi):
                lo = mi + 1
            else:
                hi = mi
        return lo - 1
复杂度分析

时间复杂度：O\big((M + N) \min(M, N) \log{(\min(M, N))}\big)O((M+N)min(M,N)log(min(M,N)))。其中 MM 和 NN 是数组 A 和 B 的长度。对于 LL，简单判断是否有长度为 LL 的子数组的时间复杂度为 O((M+N)*L)O((M+N)∗L)，二分查找为对数时间复杂度。
空间复杂度：O(M^2)O(M 
2
 )。
方法三：动态规划 [通过]
设 dp[i][j] 为 A[i:] 和 B[j:] 的最长公共前缀，那么答案就为所有 dp[i][j] 中的最大值 max(dp[i][j])。如果 A[i] == B[j]，那么状态转移方程为 dp[i][j] = dp[i + 1][j + 1] + 1，否则状态转移方程为 dp[i][j] = 0。

PythonJava
class Solution(object):
    def findLength(self, A, B):
        memo = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]
        for i in range(len(A) - 1, -1, -1):
            for j in range(len(B) - 1, -1, -1):
                if A[i] == B[j]:
                    memo[i][j] = memo[i+1][j+1]+1
        return max(max(row) for row in memo)
复杂度分析

时间复杂度：O(M* N)O(M∗N)，其中 MM 和 NN 是数组 A 和 B 的长度。
空间复杂度：O(M* N)O(M∗N)，即为数组 dp 使用的空间。
方法四：二分查找 + 哈希 [通过]
分析

方法二中的简单判断显得过于简单，在二分查找的每一步中，我们可以考虑使用哈希的方法来判断数组 A 和 B 中是否存在相同的长度为 mid 的子数组。

算法

我们使用 Rabin-Karp 算法求出一个序列的哈希值。具体地，我们制定一个素数 pp，那么序列 SS 的哈希值为：

\mathrm{hash}(S) = \sum_{i=0}^{|S|-1} p^i * S[i]
hash(S)= 
i=0
∑
∣S∣−1
​	
 p 
i
 ∗S[i]

形象地来说，就是把 SS 看成一个类似 pp 进制的数（但左侧为低位，右侧为高位），它的十进制值就是这个它的哈希值。由于这个值一般会非常大，因此会将它对另一个素数 MM 取模。

当我们要在一个序列 SS 中算出所有长度为 ll 的子序列的哈希值时，我们可以用类似滑动窗口的方法，在线性时间内得到这些子序列的哈希值。例如，如果我们当前得到了 S[0:l]S[0:l] 的哈希值，希望算出 S[1:l+1]S[1:l+1] 的哈希值，可以通过

S[1:l+1] = \frac{S[0:l] - S[0]}{p} + p^{n-1}*S[l]
S[1:l+1]= 
p
S[0:l]−S[0]
​	
 +p 
n−1
 ∗S[l]

得到。由于分子上的 S[0:l] - S[0]S[0:l]−S[0] 已经对 MM 取模，我们无法知道它除以 pp 的值，因此我们需要使用 Fermat 小定理的推论：

p^{-1} \equiv p^{M-2}\pmod{M}
p 
−1
 ≡p 
M−2
 (modM)

将除法变为乘法，这样原式变为

S[1:l+1] = (S[0:l] - S[0]) * p^{M-2} + p^{n-1}*S[l]
S[1:l+1]=(S[0:l]−S[0])∗p 
M−2
 +p 
n−1
 ∗S[l]

为了保证百分百的正确性，当两个字符串的哈希值相等时，我们会判断它们对应的字符串是否相等，防止哈希碰撞。

PythonJava
class Solution(object):
    def findLength(self, A, B):
        P, MOD = 113, 10**9 + 7
        Pinv = pow(P, MOD-2, MOD)
        def check(guess):
            def rolling(A, length):
                if length == 0:
                    yield 0, 0
                    return

                h, power = 0, 1
                for i, x in enumerate(A):
                    h = (h + x * power) % MOD
                    if i < length - 1:
                        power = (power * P) % MOD
                    else:
                        yield h, i - (length - 1)
                        h = (h - A[i - (length - 1)]) * Pinv % MOD

            hashes = collections.defaultdict(list)
            for ha, start in rolling(A, guess):
                hashes[ha].append(start)
            for ha, start in rolling(B, guess):
                iarr = hashes.get(ha, [])
                if any(A[i:i+guess] == B[start:start+guess] for i in iarr):
                    return True
            return False

        lo, hi = 0, min(len(A), len(B)) + 1
        while lo < hi:
            mi = (lo + hi) / 2
            if check(mi):
                lo = mi + 1
            else:
                hi = mi
        return lo - 1
复杂度分析

时间复杂度：O\big((M+N) \log{(\min(M, N))}\big)O((M+N)log(min(M,N)))，其中 MM 和 NN 是数组 A 和 B 的长度。二分查找为对数时间复杂度，计算哈希值的时间复杂度为 O(M+N)O(M+N)，哈希检测的时间复杂度为 O(1)O(1)。如果我们在哈希值相等时仍然判断它们对应的字符串是否相等，则时间复杂度需要加上 O(\min(M,N))O(min(M,N)) 一项，由于它小于 O(M+N)O(M+N)，因此总的时间复杂度不变。
空间复杂度：O(M)O(M)。

'''