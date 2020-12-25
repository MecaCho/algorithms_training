# encoding=utf8

'''
455. Assign Cookies
Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie.

Each child i has a greed factor g[i], which is the minimum size of a cookie that the child will be content with; and each cookie j has a size s[j]. If s[j] >= g[i], we can assign the cookie j to the child i, and the child i will be content. Your goal is to maximize the number of your content children and output the maximum number.





Example 1:

Input: g = [1,2,3], s = [1,1]
Output: 1
Explanation: You have 3 children and 2 cookies. The greed factors of 3 children are 1, 2, 3.
And even though you have 2 cookies, since their size is both 1, you could only make the child whose greed factor is 1 content.
You need to output 1.
Example 2:

Input: g = [1,2], s = [1,2,3]
Output: 2
Explanation: You have 2 children and 3 cookies. The greed factors of 2 children are 1, 2.
You have 3 cookies and their sizes are big enough to gratify all of the children,
You need to output 2.


Constraints:

1 <= g.length <= 3 * 104
0 <= s.length <= 3 * 104
1 <= g[i], s[j] <= 231 - 1


455. 分发饼干
假设你是一位很棒的家长，想要给你的孩子们一些小饼干。但是，每个孩子最多只能给一块饼干。

对每个孩子 i，都有一个胃口值 g[i]，这是能让孩子们满足胃口的饼干的最小尺寸；并且每块饼干 j，都有一个尺寸 s[j] 。如果 s[j] >= g[i]，我们可以将这个饼干 j 分配给孩子 i ，这个孩子会得到满足。你的目标是尽可能满足越多数量的孩子，并输出这个最大数值。


示例 1:

输入: g = [1,2,3], s = [1,1]
输出: 1
解释:
你有三个孩子和两块小饼干，3个孩子的胃口值分别是：1,2,3。
虽然你有两块小饼干，由于他们的尺寸都是1，你只能让胃口值是1的孩子满足。
所以你应该输出1。
示例 2:

输入: g = [1,2], s = [1,2,3]
输出: 2
解释:
你有两个孩子和三块小饼干，2个孩子的胃口值分别是1,2。
你拥有的饼干数量和尺寸都足以让所有孩子满足。
所以你应该输出2.


提示：

1 <= g.length <= 3 * 104
0 <= s.length <= 3 * 104
1 <= g[i], s[j] <= 231 - 1
'''


class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        cake_index = 0
        child_index = 0
        g.sort()
        s.sort()
        while child_index < len(g) and cake_index < len(s):
            if g[child_index] <= s[cake_index]:
                child_index += 1

            cake_index += 1

        return child_index


# solution

'''
方法一：排序 + 贪心算法
为了尽可能满足最多数量的孩子，从贪心的角度考虑，应该按照孩子的胃口从小到大的顺序依次满足每个孩子，且对于每个孩子，应该选择可以满足这个孩子的胃口且尺寸最小的饼干。证明如下。

假设有 mm 个孩子，胃口值分别是 g_1g 
1
​	
  到 g_mg 
m
​	
 ，有 nn 块饼干，尺寸分别是 s_1s 
1
​	
  到 s_ns 
n
​	
 ，满足 g_i \le g_{i+1}g 
i
​	
 ≤g 
i+1
​	
  和 s_j \le s_{j+1}s 
j
​	
 ≤s 
j+1
​	
 ，其中 1 \le i < m1≤i<m，1 \le j < n1≤j<n。

假设在对前 i-1i−1 个孩子分配饼干之后，可以满足第 ii 个孩子的胃口的最小的饼干是第 jj 块饼干，即 s_js 
j
​	
  是剩下的饼干中满足 g_i \le s_jg 
i
​	
 ≤s 
j
​	
  的最小值，最优解是将第 jj 块饼干分配给第 ii 个孩子。如果不这样分配，考虑如下两种情形：

如果 i<mi<m 且 g_{i+1} \le s_jg 
i+1
​	
 ≤s 
j
​	
  也成立，则如果将第 jj 块饼干分配给第 i+1i+1 个孩子，且还有剩余的饼干，则可以将第 j+1j+1 块饼干分配给第 ii 个孩子，分配的结果不会让更多的孩子被满足；

如果 j<nj<n，则如果将第 j+1j+1 块饼干分配给第 ii 个孩子，当 g_{i+1} \le s_jg 
i+1
​	
 ≤s 
j
​	
  时，可以将第 jj 块饼干分配给第 i+1i+1 个孩子，分配的结果不会让更多的孩子被满足；当 g_{i+1}>s_jg 
i+1
​	
 >s 
j
​	
  时，第 jj 块饼干无法分配给任何孩子，因此剩下的可用的饼干少了一块，因此分配的结果不会让更多的孩子被满足，甚至可能因为少了一块可用的饼干而导致更少的孩子被满足。

基于上述分析，可以使用贪心算法尽可能满足最多数量的孩子。

首先对数组 gg 和 ss 排序，然后从小到大遍历 gg 中的每个元素，对于每个元素找到能满足该元素的 ss 中的最小的元素。具体而言，令 ii 是 gg 的下标，jj 是 ss 的下标，初始时 ii 和 jj 都为 00，进行如下操作。

对于每个元素 g[i]g[i]，找到未被使用的最小的 jj 使得 g[i] \le s[j]g[i]≤s[j]，则 s[j]s[j] 可以满足 g[i]g[i]。由于 gg 和 ss 已经排好序，因此整个过程只需要对数组 gg 和 ss 各遍历一次。当两个数组之一遍历结束时，说明所有的孩子都被分配到了饼干，或者所有的饼干都已经被分配或被尝试分配（可能有些饼干无法分配给任何孩子），此时被分配到饼干的孩子数量即为可以满足的最多数量。

JavaJavaScriptC++GolangPython3C

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        n, m = len(g), len(s)
        i = j = count = 0

        while i < n and j < m:
            while j < m and g[i] > s[j]:
                j += 1
            if j < m:
                count += 1
            i += 1
            j += 1
        
        return count
复杂度分析

时间复杂度：O(m \log m + n \log n)O(mlogm+nlogn)，其中 mm 和 nn 分别是数组 gg 和 ss 的长度。对两个数组排序的时间复杂度是 O(m \log m + n \log n)O(mlogm+nlogn)，遍历数组的时间复杂度是 O(m+n)O(m+n)，因此总时间复杂度是 O(m \log m + n \log n)O(mlogm+nlogn)。

空间复杂度：O(\log m + \log n)O(logm+logn)，其中 mm 和 nn 分别是数组 gg 和 ss 的长度。空间复杂度主要是排序的额外空间开销。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/assign-cookies/solution/fen-fa-bing-gan-by-leetcode-solution-50se/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
