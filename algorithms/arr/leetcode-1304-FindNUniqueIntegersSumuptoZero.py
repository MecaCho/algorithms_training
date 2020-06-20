'''
1304. 和为零的N个唯一整数
给你一个整数 n，请你返回 任意 一个由 n 个 各不相同 的整数组成的数组，并且这 n 个数相加和为 0 。



示例 1：

输入：n = 5
输出：[-7,-1,1,3,4]
解释：这些数组也是正确的 [-5,-1,1,2,3]，[-3,-1,2,-2,4]。
示例 2：

输入：n = 3
输出：[-1,0,1]
示例 3：

输入：n = 1
输出：[0]


提示：

1 <= n <= 1000

1304. Find N Unique Integers Sum up to Zero
Given an integer n, return any array containing n unique integers such that they add up to 0.



Example 1:

Input: n = 5
Output: [-7,-1,1,3,4]
Explanation: These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].
Example 2:

Input: n = 3
Output: [-1,0,1]
Example 3:

Input: n = 1
Output: [0]


Constraints:

1 <= n <= 1000
'''

class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = range(-n/2, n/2+1)
        # print(res)
        if n % 2 == 1:
            res.pop(0)
        else:
            res.remove(0)
        return res

# solutions

'''
方法一：构造
我们首先将最小的 n - 1 个自然数 0, 1, 2, ..., n - 2 放入数组中，它们的和为 sum。对于剩下的 1 个数，我们可以令其为 -sum，此时这 n 个数的和为 0，并且：

当 n = 1 时，我们构造的答案中只有唯一的 1 个数 0；

当 n > 1 时，我们构造的答案中包含 n - 1 个互不相同的自然数和 1 个负数；

因此这 n 个数互不相同，即我们得到了一个满足要求的数组。

C++Python3

class Solution:
    def sumZero(self, n: int) -> List[int]:
        ans = [x for x in range(n - 1)]
        ans.append(-sum(ans))
        return ans
复杂度分析

时间复杂度：O(N)O(N)。

空间复杂度：O(1)O(1)，除了存储答案的数组 ans 之外，额外的空间复杂度是 O(1)O(1)。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/find-n-unique-integers-sum-up-to-zero/solution/he-wei-ling-de-nge-wei-yi-zheng-shu-by-leetcode-so/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''