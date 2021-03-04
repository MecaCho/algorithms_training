# encoding=utf8


'''
354. Russian Doll Envelopes
You have a number of envelopes with widths and heights given as a pair of integers (w, h). One envelope can fit into another if and only if both the width and height of one envelope is greater than the width and height of the other envelope.

What is the maximum number of envelopes can you Russian doll? (put one inside other)

Note:
Rotation is not allowed.

Example:

Input: [[5,4],[6,4],[6,7],[2,3]]
Output: 3
Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).


354. 俄罗斯套娃信封问题
给定一些标记了宽度和高度的信封，宽度和高度以整数对形式 (w, h) 出现。当另一个信封的宽度和高度都比这个信封大的时候，这个信封就可以放进另一个信封里，如同俄罗斯套娃一样。

请计算最多能有多少个信封能组成一组“俄罗斯套娃”信封（即可以把一个信封放到另一个信封里面）。

说明:
不允许旋转信封。

示例:

输入: envelopes = [[5,4],[6,4],[6,7],[2,3]]
输出: 3
解释: 最多信封的个数为 3, 组合为: [2,3] => [5,4] => [6,7]。


'''




class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        envelopes.sort(key=lambda x: x[0])
        length = len(envelopes)
        dp = [1] * length

        for i in range(length):
            for j in range(i, length):
                if envelopes[j][0] > envelopes[i][0] and envelopes[j][1] > envelopes[i][1]:
                    dp[j] = max(dp[i]+1, dp[j])

        return max(dp) if dp else 0


if __name__ == '__main__':
    l = [[1,2], [0,1]]
    l.sort(key=lambda x:x[0])
    print(l)



# sulutions

'''

前言
根据题目的要求，如果我们选择了 kk 个信封，它们的的宽度依次为 w_0, w_1, \cdots, w_{k-1}w 
0
​	
 ,w 
1
​	
 ,⋯,w 
k−1
​	
 ，高度依次为 h_0, h_1, \cdots, h_{k-1}h 
0
​	
 ,h 
1
​	
 ,⋯,h 
k−1
​	
 ，那么需要满足：

\begin{cases} w_0 < w_1 < \cdots < w_{k-1} \\ h_0 < h_1 < \cdots < h_{k-1} \end{cases}
{ 
w 
0
​	
 <w 
1
​	
 <⋯<w 
k−1
​	
 
h 
0
​	
 <h 
1
​	
 <⋯<h 
k−1
​	
 
​	
 

同时控制 ww 和 hh 两个维度并不是那么容易，因此我们考虑固定一个维度，再在另一个维度上进行选择。例如，我们固定 ww 维度，那么我们将数组 \textit{envelopes}envelopes 中的所有信封按照 ww 升序排序。这样一来，我们只要按照信封在数组中的出现顺序依次进行选取，就一定保证满足：

w_0 \leq w_1 \leq \cdots \leq w_{k-1}
w 
0
​	
 ≤w 
1
​	
 ≤⋯≤w 
k−1
​	
 

了。然而小于等于 \leq≤ 和小于 << 还是有区别的，但我们不妨首先考虑一个简化版本的问题：

如果我们保证所有信封的 ww 值互不相同，那么我们可以设计出一种得到答案的方法吗？

在 ww 值互不相同的前提下，小于等于 \leq≤ 和小于 << 是等价的，那么我们在排序后，就可以完全忽略 ww 维度，只需要考虑 hh 维度了。此时，我们需要解决的问题即为：

给定一个序列，我们需要找到一个最长的子序列，使得这个子序列中的元素严格单调递增，即上面要求的：

h_0 < h_1 < \cdots < h_{k-1}
h 
0
​	
 <h 
1
​	
 <⋯<h 
k−1
​	
 

那么这个问题就是经典的「最长严格递增子序列」问题了，读者可以参考力扣平台的 300. 最长递增子序列 及其 官方题解。最长严格递增子序列的详细解决方法属于解决本题的前置知识点，不是本文分析的重点，因此这里不再赘述，会在方法一和方法二中简单提及。

当我们解决了简化版本的问题之后，我们来想一想使用上面的方法解决原问题，会产生什么错误。当 ww 值相同时，如果我们不规定 hh 值的排序顺序，那么可能会有如下的情况：

排完序的结果为 [(w, h)] = [(1, 1), (1, 2), (1, 3), (1, 4)][(w,h)]=[(1,1),(1,2),(1,3),(1,4)]，由于这些信封的 ww 值都相同，不存在一个信封可以装下另一个信封，那么我们只能在其中选择 11 个信封。然而如果我们完全忽略 ww 维度，剩下的 hh 维度为 [1, 2, 3, 4][1,2,3,4]，这是一个严格递增的序列，那么我们就可以选择所有的 44 个信封了，这就产生了错误。

因此，我们必须要保证对于每一种 ww 值，我们最多只能选择 11 个信封。

我们可以将 hh 值作为排序的第二关键字进行降序排序，这样一来，对于每一种 ww 值，其对应的信封在排序后的数组中是按照 hh 值递减的顺序出现的，那么这些 hh 值不可能组成长度超过 11 的严格递增的序列，这就从根本上杜绝了错误的出现。

因此我们就可以得到解决本题需要的方法：

首先我们将所有的信封按照 ww 值第一关键字升序、hh 值第二关键字降序进行排序；

随后我们就可以忽略 ww 维度，求出 hh 维度的最长严格递增子序列，其长度即为答案。

下面简单提及两种计算最长严格递增子序列的方法，更详细的请参考上文提到的题目以及对应的官方题解。

方法一：动态规划
思路与算法

设 f[i]f[i] 表示 hh 的前 ii 个元素可以组成的最长严格递增子序列的长度，并且我们必须选择第 ii 个元素 h_ih 
i
​	
 。在进行状态转移时，我们可以考虑倒数第二个选择的元素 h_jh 
j
​	
 ，必须满足 h_j < h_ih 
j
​	
 <h 
i
​	
  且 j < ij<i，因此可以写出状态转移方程：

f[i] = \max_{j<i ~\wedge~ h_j<h_i } \{ f[j] \} + 1
f[i]= 
j<i ∧ h 
j
​	
 <h 
i
​	
 
max
​	
 {f[j]}+1

如果不存在比 h_ih 
i
​	
  小的元素 h_jh 
j
​	
 ，那么 f[i]f[i] 的值为 11，即只选择了唯一的第 ii 个元素。

在计算完所有的 ff 值之后，其中的最大值即为最长严格递增子序列的长度。

代码

由于方法一的时间复杂度较高，一些语言对应的代码可能会超出时间限制。

C++JavaPython3JavaScriptGolangC

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if not envelopes:
            return 0
        
        n = len(envelopes)
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        f = [1] * n
        for i in range(n):
            for j in range(i):
                if envelopes[j][1] < envelopes[i][1]:
                    f[i] = max(f[i], f[j] + 1)
        
        return max(f)
复杂度分析

时间复杂度：O(n^2)O(n 
2
 )，其中 nn 是数组 \textit{envelopes}envelopes 的长度，排序需要的时间复杂度为 O(n \log n)O(nlogn)，动态规划需要的时间复杂度为 O(n^2)O(n 
2
 )，前者在渐近意义下小于后者，可以忽略。

空间复杂度：O(n)O(n)，即为数组 ff 需要的空间。

方法二：基于二分查找的动态规划
思路与算法

设 f[j]f[j] 表示 hh 的前 ii 个元素可以组成的长度为 jj 的最长严格递增子序列的末尾元素的最小值，如果不存在长度为 jj 的最长严格递增子序列，对应的 ff 值无定义。在定义范围内，可以看出 ff 值是严格单调递增的，因为越长的子序列的末尾元素显然越大。

在进行状态转移时，我们考虑当前的元素 h_ih 
i
​	
 ：

如果 h_ih 
i
​	
  大于 ff 中的最大值，那么 h_ih 
i
​	
  就可以接在 ff 中的最大值之后，形成一个长度更长的严格递增子序列；

否则我们找出 ff 中比 h_ih 
i
​	
  严格小的最大的元素 f[j_0]f[j 
0
​	
 ]，即 f[j_0] < h_i \leq f[j_0+1]f[j 
0
​	
 ]<h 
i
​	
 ≤f[j 
0
​	
 +1]，那么 h_ih 
i
​	
  可以接在 f[j_0]f[j 
0
​	
 ] 之后，形成一个长度为 j_0+1j 
0
​	
 +1 的严格递增子序列，因此需要对 f[j_0+1]f[j 
0
​	
 +1] 进行更新：

f[j_0+1] = h_i
f[j 
0
​	
 +1]=h 
i
​	
 

我们可以在 ff 上进行二分查找，找出满足要求的 j_0j 
0
​	
 。

在遍历所有的 h_ih 
i
​	
  之后，ff 中最后一个有定义的元素的下标增加 11（下标从 00 开始）即为最长严格递增子序列的长度。

代码

C++JavaPython3JavaScriptGolangC

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if not envelopes:
            return 0
        
        n = len(envelopes)
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        f = [envelopes[0][1]]
        for i in range(1, n):
            if (num := envelopes[i][1]) > f[-1]:
                f.append(num)
            else:
                index = bisect.bisect_left(f, num)
                f[index] = num
        
        return len(f)
复杂度分析

时间复杂度：O(n \log n)O(nlogn)，其中 nn 是数组 \textit{envelopes}envelopes 的长度，排序需要的时间复杂度为 O(n \log n)O(nlogn)，动态规划需要的时间复杂度同样为 O(n \log n)O(nlogn)。

空间复杂度：O(n)O(n)，即为数组 ff 需要的空间。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/russian-doll-envelopes/solution/e-luo-si-tao-wa-xin-feng-wen-ti-by-leetc-wj68/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''

