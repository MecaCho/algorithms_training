# encoding=utf8

'''
995. Minimum Number of K Consecutive Bit Flips
In an array A containing only 0s and 1s, a K-bit flip consists of choosing a (contiguous) subarray of length K and simultaneously changing every 0 in the subarray to 1, and every 1 in the subarray to 0.

Return the minimum number of K-bit flips required so that there is no 0 in the array.  If it is not possible, return -1.



Example 1:

Input: A = [0,1,0], K = 1
Output: 2
Explanation: Flip A[0], then flip A[2].
Example 2:

Input: A = [1,1,0], K = 2
Output: -1
Explanation: No matter how we flip subarrays of size 2, we can't make the array become [1,1,1].
Example 3:

Input: A = [0,0,0,1,0,1,1,0], K = 3
Output: 3
Explanation:
Flip A[0],A[1],A[2]: A becomes [1,1,1,1,0,1,1,0]
Flip A[4],A[5],A[6]: A becomes [1,1,1,1,1,0,0,0]
Flip A[5],A[6],A[7]: A becomes [1,1,1,1,1,1,1,1]


Note:

1 <= A.length <= 30000
1 <= K <= A.length



995. K 连续位的最小翻转次数
在仅包含 0 和 1 的数组 A 中，一次 K 位翻转包括选择一个长度为 K 的（连续）子数组，同时将子数组中的每个 0 更改为 1，而每个 1 更改为 0。

返回所需的 K 位翻转的最小次数，以便数组没有值为 0 的元素。如果不可能，返回 -1。



示例 1：

输入：A = [0,1,0], K = 1
输出：2
解释：先翻转 A[0]，然后翻转 A[2]。
示例 2：

输入：A = [1,1,0], K = 2
输出：-1
解释：无论我们怎样翻转大小为 2 的子数组，我们都不能使数组变为 [1,1,1]。
示例 3：

输入：A = [0,0,0,1,0,1,1,0], K = 3
输出：3
解释：
翻转 A[0],A[1],A[2]: A变成 [1,1,1,1,0,1,1,0]
翻转 A[4],A[5],A[6]: A变成 [1,1,1,1,1,0,0,0]
翻转 A[5],A[6],A[7]: A变成 [1,1,1,1,1,1,1,1]


提示：

1 <= A.length <= 30000
1 <= K <= A.length
'''


class Solution(object):
    def minKBitFlips(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        n = len(A)
        ans = 0
        revCnt = 0
        for i in range(n):
            if i >= K and A[i - K] > 1:
                revCnt ^= 1
                A[i - K] -= 2

            if A[i] == revCnt:
                if i + K > n:
                    return -1

                ans += 1
                revCnt ^= 1
                A[i] += 2

        return ans


import collections


class Solution1(object):
    def minKBitFlips(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        N = len(A)
        que = collections.deque()
        res = 0
        for i in range(N):
            if que and i >= que[0] + K:
                que.popleft()
            if len(que) % 2 == A[i]:
                if i +  K > N:
                    return -1
                que.append(i)
                res += 1
        return res


# solutions

'''
解题思路
题目大意：每次翻转长度为 K 的子数组，求最少的翻转次数使数组中所有的 0 都更改为 1。如果不能实现，则返回 -1.

结论 1：后面区间的翻转，不会影响前面的元素。因此可以使用贪心策略，从左到右遍历，遇到每个 0 都把它和后面的 K 个数进行翻转。
结论 2：A[i]A[i] 翻转偶数次的结果是 A[i]A[i]；翻转奇数次的结果是 A[i] ^ 1。
方法一：模拟翻转（超时）
一个直观的思路是，从左到右遍历一遍，遇到数字为 0，那么翻转以该数字为起始的 K 个数字。

代码如下：


class Solution(object):
    def minKBitFlips(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        N = len(A)
        res = 0
        for i in range(N - K + 1):
            if A[i] == 1:
                continue
            for j in range(K):
                A[i + j] ^= 1
            res += 1
        for i in range(N):
            if A[i] == 0:
                return -1
        return res
时间复杂度：O(N * K + N)O(N∗K+N)，超时。
空间复杂度：O(1)O(1)。
方法二：滑动窗口
上面方法超时的主要原因是我们真实地进行了翻转。根据结论二，位置 ii 现在的状态，和它被前面 K - 1K−1 个元素翻转的次数（奇偶性）有关。

我们使用队列模拟滑动窗口，该滑动窗口的含义是前面 K - 1K−1 个元素中，以哪些位置起始的 子区间进行了翻转。该滑动窗口从左向右滑动，
如果当前位置 i 需要翻转，则把该位置存储到队列中。
遍历到新位置 j (j < i + K)j(j<i+K) 时，队列中元素的个数代表了 ii 被前面 K - 1K−1 个元素翻转的次数。

当 ii 位置被翻转了偶数次，如果 A[i]A[i] 为 0，那么翻转后仍是 0，当前元素需要翻转；
当 ii 位置被翻转了奇数次，如果 A[i]A[i] 为 1，那么翻转后是 0，当前元素需要翻转。
综合上面两点，我们得到一个结论，如果 len(que) % 2 == A[i]len(que) 时，当前元素需要翻转。

当 i + K > Ni+K>N 时，说明需要翻转大小为 K 的子区间，但是后面剩余的元素不到 K 个了，所以返回 -1。



对应的 PPT 在这：


11 / 19

代码如下：


class Solution(object):
    def minKBitFlips(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        N = len(A)
        que = collections.deque()
        res = 0
        for i in range(N):
            if que and i >= que[0] + K:
                que.popleft()
            if len(que) % 2 == A[i]:
                if i +  K > N: 
                    return -1
                que.append(i)
                res += 1
        return res
        
时间复杂度：O(N)O(N)。
空间复杂度：O(K)O(K)。

作者：fuxuemingzhu
链接：https://leetcode-cn.com/problems/minimum-number-of-k-consecutive-bit-flips/solution/hua-dong-chuang-kou-shi-ben-ti-zui-rong-z403l/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''

