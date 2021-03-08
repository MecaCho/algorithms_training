# encoding=utf8

'''
132. Palindrome Partitioning II
Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.



Example 1:

Input: s = "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.
Example 2:

Input: s = "a"
Output: 0
Example 3:

Input: s = "ab"
Output: 1


Constraints:

1 <= s.length <= 2000
s consists of lower-case English letters only.


132. 分割回文串 II
给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是回文。

返回符合要求的 最少分割次数 。



示例 1：

输入：s = "aab"
输出：1
解释：只需一次分割就可将 s 分割成 ["aa","b"] 这样两个回文子串。
示例 2：

输入：s = "a"
输出：0
示例 3：

输入：s = "ab"
输出：1


提示：

1 <= s.length <= 2000
s 仅由小写英文字母组成
'''


class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        # self.vals = []

        # def bk(nums, temp):
        #     if not nums and temp[-1][::-1] == temp[-1]:
        #         self.vals.append(temp)
        #         return
        #     for i in range(len(nums)):
        #         if temp and temp[-1][::-1] != temp[-1]:
        #             continue
        #         bk(nums[ i +1:], temp +["".join(nums[: i +1])])

        # bk(list(s), [])
        # return len(min(self.vals, key=lambda x: len(x))) - 1

        n = len(s)
        g = [[True] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                g[i][j] = (s[i] == s[j]) and g[i + 1][j - 1]

        f = [float("inf")] * n
        for i in range(n):
            if g[0][i]:
                f[i] = 0
            else:
                for j in range(i):
                    if g[j + 1][i]:
                        f[i] = min(f[i], f[j] + 1)

        return f[n - 1]

# solutions


'''
方法一：动态规划
思路与算法

设 f[i]f[i] 表示字符串的前缀 s[0..i]s[0..i] 的最少分割次数。要想得出 f[i]f[i] 的值，我们可以考虑枚举 s[0..i]s[0..i] 分割出的最后一个回文串，这样我们就可以写出状态转移方程：

f[i] = \min_{0 \leq j < i} \{ f[j] \} + 1, \quad 其中 ~ s[j+1..i] ~是一个回文串
f[i]= 
0≤j<i
min
​	
 {f[j]}+1,其中 s[j+1..i] 是一个回文串

即我们枚举最后一个回文串的起始位置 j+1j+1，保证 s[j+1..i]s[j+1..i] 是一个回文串，那么 f[i]f[i] 就可以从 f[j]f[j] 转移而来，附加 11 次额外的分割次数。

注意到上面的状态转移方程中，我们还少考虑了一种情况，即 s[0..i]s[0..i] 本身就是一个回文串。此时其不需要进行任何分割，即：

f[i] = 0
f[i]=0

那么我们如何知道 s[j+1..i]s[j+1..i] 或者 s[0..i]s[0..i] 是否为回文串呢？我们可以使用与「131. 分割回文串的官方题解」中相同的预处理方法，将字符串 ss 的每个子串是否为回文串预先计算出来，即：

设 g(i, j)g(i,j) 表示 s[i..j]s[i..j] 是否为回文串，那么有状态转移方程：

g(i, j) = \begin{cases} \texttt{True}, & \quad i \geq j \\ g(i+1,j-1) \wedge (s[i]=s[j]), & \quad \text{otherwise} \end{cases}
g(i,j)={ 
True,
g(i+1,j−1)∧(s[i]=s[j]),
​	
  
i≥j
otherwise
​	
 

其中 \wedge∧ 表示逻辑与运算，即 s[i..j]s[i..j] 为回文串，当且仅当其为空串（i>ji>j），其长度为 11（i=ji=j），或者首尾字符相同且 s[i+1..j-1]s[i+1..j−1] 为回文串。

这样一来，我们只需要 O(1)O(1) 的时间就可以判断任意 s[i..j]s[i..j] 是否为回文串了。通过动态规划计算出所有的 ff 值之后，最终的答案即为 f[n-1]f[n−1]，其中 nn 是字符串 ss 的长度。

代码

C++JavaPython3JavaScriptGolangC

class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        g = [[True] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                g[i][j] = (s[i] == s[j]) and g[i + 1][j - 1]

        f = [float("inf")] * n
        for i in range(n):
            if g[0][i]:
                f[i] = 0
            else:
                for j in range(i):
                    if g[j + 1][i]:
                        f[i] = min(f[i], f[j] + 1)
        
        return f[n - 1]
复杂度分析

时间复杂度：O(n^2)O(n 
2
 )，其中 nn 是字符串 ss 的长度。预处理计算 gg 和动态规划计算 ff 的时间复杂度均为 O(n^2)O(n 
2
 )。

空间复杂度：O(n^2)O(n 
2
 )，数组 gg 需要使用 O(n^2)O(n 
2
 ) 的空间，数组 ff 需要使用 O(n^2)O(n 
2
 ) 的空间。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/palindrome-partitioning-ii/solution/fen-ge-hui-wen-chuan-ii-by-leetcode-solu-norx/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
