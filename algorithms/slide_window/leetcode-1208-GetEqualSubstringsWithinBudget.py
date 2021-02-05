# encoding=utf8

'''
1208. Get Equal Substrings Within Budget
You are given two strings s and t of the same length. You want to change s to t. Changing the i-th character of s to i-th character of t costs |s[i] - t[i]| that is, the absolute difference between the ASCII values of the characters.

You are also given an integer maxCost.

Return the maximum length of a substring of s that can be changed to be the same as the corresponding substring of twith a cost less than or equal to maxCost.

If there is no substring from s that can be changed to its corresponding substring from t, return 0.



Example 1:

Input: s = "abcd", t = "bcdf", maxCost = 3
Output: 3
Explanation: "abc" of s can change to "bcd". That costs 3, so the maximum length is 3.
Example 2:

Input: s = "abcd", t = "cdef", maxCost = 3
Output: 1
Explanation: Each character in s costs 2 to change to charactor in t, so the maximum length is 1.
Example 3:

Input: s = "abcd", t = "acde", maxCost = 0
Output: 1
Explanation: You can't make any change, so the maximum length is 1.


Constraints:

1 <= s.length, t.length <= 10^5
0 <= maxCost <= 10^6
s and t only contain lower case English letters.


1208. 尽可能使字符串相等
给你两个长度相同的字符串，s 和 t。

将 s 中的第 i 个字符变到 t 中的第 i 个字符需要 |s[i] - t[i]| 的开销（开销可能为 0），也就是两个字符的 ASCII 码值的差的绝对值。

用于变更字符串的最大预算是 maxCost。在转化字符串时，总开销应当小于等于该预算，这也意味着字符串的转化可能是不完全的。

如果你可以将 s 的子字符串转化为它在 t 中对应的子字符串，则返回可以转化的最大长度。

如果 s 中没有子字符串可以转化成 t 中对应的子字符串，则返回 0。



示例 1：

输入：s = "abcd", t = "bcdf", cost = 3
输出：3
解释：s 中的 "abc" 可以变为 "bcd"。开销为 3，所以最大长度为 3。
示例 2：

输入：s = "abcd", t = "cdef", cost = 3
输出：1
解释：s 中的任一字符要想变成 t 中对应的字符，其开销都是 2。因此，最大长度为 1。
示例 3：

输入：s = "abcd", t = "acde", cost = 0
输出：1
解释：你无法作出任何改动，所以最大长度为 1。


提示：

1 <= s.length, t.length <= 10^5
0 <= maxCost <= 10^6
s 和 t 都只含小写英文字母。
'''


class Solution(object):
    def equalSubstring(self, s, t, maxCost):
        """
        :type s: str
        :type t: str
        :type maxCost: int
        :rtype: int
        """
        l, res = 0, 0
        cost = 0
        for i in range(len(s)):
            cost += abs(ord(s[i]) - ord(t[i]))
            while cost > maxCost:
                cost -= abs(ord(s[l]) - ord(t[l]))
                l += 1
            res = max(res, i-l+1)

        return res


# solutions

'''
前言
假定字符串 ss 和 tt 的长度均为 nn，对于任意 0 \le i<n0≤i<n，将 s[i]s[i] 变成 t[i]t[i] 的开销是 \Big| s[i]-t[i] \Big| 
∣
∣
∣
∣
​	
 s[i]−t[i] 
∣
∣
∣
∣
​	
 ，因此可以创建一个长度为 nn 的数组 \textit{diff}diff，其中 \textit{diff}[i]=\Big|s[i]-t[i] \Big|diff[i]= 
∣
∣
∣
∣
​	
 s[i]−t[i] 
∣
∣
∣
∣
​	
 。

创建数组 \textit{diff}diff 之后，问题转化成计算数组 \textit{diff}diff 的元素和不超过 \textit{maxCost}maxCost 的最长子数组的长度。有两种方法可以解决，第一种方法是前缀和 + 二分查找，第二种方法是双指针。

方法一：前缀和 + 二分查找
首先计算数组 \textit{diff}diff 的前缀和，创建长度为 n+1n+1 的数组 \textit{accDiff}accDiff，其中 \textit{accDiff}[0]=0accDiff[0]=0，对于 0 \le i< n0≤i<n，有 \textit{accDiff}[i+1]=\textit{accDiff}[i]+\textit{diff}[i]accDiff[i+1]=accDiff[i]+diff[i]。

即当 1 \le i \le n1≤i≤n 时，\textit{accDiff}[i]accDiff[i] 为 \textit{diff}diff 从下标 00 到下标 i-1i−1 的元素和：

\textit{accDiff}[i]=\sum\limits_{j=0}^{i-1} \textit{diff}[j]
accDiff[i]= 
j=0
∑
i−1
​	
 diff[j]

当 \textit{diff}diff 的子数组以下标 jj 结尾时，需要找到最小的下标 kk（k \le jk≤j），使得 \textit{diff}diff 从下标 kk 到 jj 的元素和不超过 \textit{maxCost}maxCost，此时子数组的长度是 j-k+1j−k+1。由于已经计算出前缀和数组 \textit{accDiff}accDiff，因此可以通过 \textit{accDiff}accDiff 得到 \textit{diff}diff 从下标 kk 到 jj 的元素和：

\begin{aligned} &\quad \ \sum\limits_{i=k}^j \textit{diff}[k] \\ &= \sum\limits_{i=0}^j \textit{diff}[i] - \sum\limits_{i=0}^{k-1} \textit{diff}[i] \\ &= \textit{accDiff}[j+1] - \textit{accDiff}[k] \end{aligned}
​	
  
  
i=k
∑
j
​	
 diff[k]
= 
i=0
∑
j
​	
 diff[i]− 
i=0
∑
k−1
​	
 diff[i]
=accDiff[j+1]−accDiff[k]
​	
 

因此，找到最小的下标 kk（k \le jk≤j），使得 \textit{diff}diff 从下标 kk 到 jj 的元素和不超过 \textit{maxCost}maxCost，等价于找到最小的下标 kk（k \le jk≤j），使得 \textit{accDiff}[j+1] - \textit{accDiff}[k] \le \textit{maxCost}accDiff[j+1]−accDiff[k]≤maxCost。

由于 \textit{diff}diff 的的每个元素都是非负的，因此 \textit{accDiff}accDiff 是递增的，对于每个下标 jj，可以通过在 \textit{accDiff}accDiff 内进行二分查找的方法找到符合要求的最小的下标 kk。

以下是具体实现方面的细节。

不需要计算数组 \textit{diff}diff 的元素值，而是可以根据字符串 ss 和 tt 的对应位置字符直接计算 \textit{accDiff}accDiff 的元素值。

对于下标范围 [1,n][1,n] 内的每个 ii，通过二分查找的方式，在下标范围 [0,i][0,i] 内找到最小的下标 \textit{start}start，使得 \textit{accDiff}[\textit{start}] \ge \textit{accDiff}[i]-\textit{maxCost}accDiff[start]≥accDiff[i]−maxCost，此时对应的 \textit{diff}diff 的子数组的下标范围是从 \textit{start}start 到 i-1i−1，子数组的长度是 i-\textit{start}i−start。

遍历下标范围 [1,n][1,n] 内的每个 ii 之后，即可得到符合要求的最长子数组的长度，即字符串可以转化的最大长度。

JavaJavaScriptC++GolangPython3C

class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)
        accDiff = [0] + list(accumulate(abs(ord(sc) - ord(tc)) for sc, tc in zip(s, t)))
        maxLength = 0

        for i in range(1, n + 1):
            start = bisect.bisect_left(accDiff, accDiff[i] - maxCost)
            maxLength = max(maxLength, i - start)
        
        return maxLength
复杂度分析

时间复杂度：O(n \log n)O(nlogn)，其中 nn 是字符串的长度。
计算前缀和数组 \textit{accDiff}accDiff 的时间复杂度是 O(n)O(n)。
需要进行 nn 次二分查找，每次二分查找的时间复杂度是 O(\log n)O(logn)，二分查找共需要 O(n \log n)O(nlogn) 的时间。
因此总时间复杂度是 O(n \log n)O(nlogn)。

空间复杂度：O(n)O(n)，其中 nn 是字符串的长度。需要创建长度为 n+1n+1 的前缀和数组 \textit{accDiff}accDiff。

方法二：双指针
由于 \textit{diff}diff 的的每个元素都是非负的，因此可以用双指针的方法得到符合要求的最长子数组的长度。

双指针法的思想是，维护两个指针 \textit{start}start 和 \textit{end}end 表示数组 \textit{diff}diff 的子数组的开始下标和结束下标，满足子数组的元素和不超过 \textit{maxCost}maxCost，子数组的长度是 \textit{end}-\textit{start}+1end−start+1。初始时，\textit{start}start 和 \textit{end}end 的值都是 00。

另外还要维护子数组的元素和 \textit{sum}sum，初始值为 00。在移动两个指针的过程中，更新 \textit{sum}sum 的值，判断子数组的元素和是否大于 \textit{maxCost}maxCost，并决定应该如何移动指针。

为了得到符合要求的最长子数组的长度，应遵循以下两点原则：

当 \textit{start}start 的值固定时，\textit{end}end 的值应尽可能大；

当 \textit{end}end 的值固定时，\textit{start}start 的值应尽可能小。

基于上述原则，双指针的做法如下：

将 \textit{diff}[\textit{end}]diff[end] 的值加到 \textit{sum}sum；

如果 \textit{sum} \le \textit{maxCost}sum≤maxCost，则子数组的元素和不超过 \textit{maxCost}maxCost，使用当前子数组的长度 \textit{end}-\textit{start}+1end−start+1 更新最大子数组的长度；

如果 \textit{sum}>\textit{maxCost}sum>maxCost，则子数组的元素和大于 \textit{maxCost}maxCost，需要向右移动指针 \textit{start}start 并同时更新 \textit{sum}sum 的值，直到 \textit{sum} \le \textit{maxCost}sum≤maxCost，此时子数组的元素和不超过 \textit{maxCost}maxCost，使用子数组的长度 \textit{end}-\textit{start}+1end−start+1 更新最大子数组的长度；

将指针 \textit{end}end 右移一位，重复上述步骤，直到 \textit{end}end 超出数组下标范围。

遍历结束之后，即可得到符合要求的最长子数组的长度，即字符串可以转化的最大长度。

JavaJavaScriptC++GolangPython3C

class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)
        diff = [abs(ord(sc) - ord(tc)) for sc, tc in zip(s, t)]
        maxLength = start = end = 0
        total = 0

        while end < n:
            total += diff[end]
            while total > maxCost:
                total -= diff[start]
                start += 1
            maxLength = max(maxLength, end - start + 1)
            end += 1
        
        return maxLength
复杂度分析

时间复杂度：O(n)O(n)，其中 nn 是字符串的长度。
计算数组 \textit{diff}diff 的时间复杂度是 O(n)O(n)。
遍历数组的过程中，两个指针的移动次数都不会超过 nn 次。
因此总时间复杂度是 O(n)O(n)。

空间复杂度：O(n)O(n)，其中 nn 是字符串的长度。需要创建长度为 nn 的数组 \textit{diff}diff。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/get-equal-substrings-within-budget/solution/jin-ke-neng-shi-zi-fu-chuan-xiang-deng-b-higz/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
