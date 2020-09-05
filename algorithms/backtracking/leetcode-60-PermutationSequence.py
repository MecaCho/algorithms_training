


'''
60. 第k个排列
给出集合 [1,2,3,…,n]，其所有元素共有 n! 种排列。

按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：

"123"
"132"
"213"
"231"
"312"
"321"
给定 n 和 k，返回第 k 个排列。

说明：

给定 n 的范围是 [1, 9]。
给定 k 的范围是[1,  n!]。
示例 1:

输入: n = 3, k = 3
输出: "213"
示例 2:

输入: n = 4, k = 9
输出: "2314"

60. Permutation Sequence
The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note:

Given n will be between 1 and 9 inclusive.
Given k will be between 1 and n! inclusive.
Example 1:

Input: n = 3, k = 3
Output: "213"
Example 2:

Input: n = 4, k = 9
Output: "2314"

'''


class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        steps = [1]
        for i in range(1, n+1):
            step = steps[-1]*i
            steps.append(step)
        res = []

        nums = [str(j+1) for j in range(n)]
        while k > 0 and i > 0:
            s = (k-1) / steps[i-1]
            k = k - (s * steps[i-1])
            i -= 1
            res.append(nums[s])
            nums.pop(s)

        # res.extend(nums)
        return "".join(res)



# solution of lc

'''
方法一：数学 + 缩小问题规模
思路

要想解决本题，首先需要了解一个简单的结论：

对于 nn 个不同的元素（例如数 1, 2, \cdots, n1,2,⋯,n），它们可以组成的排列总数目为 n!n!。

对于给定的 nn 和 kk，我们不妨从左往右确定第 kk 个排列中的每一个位置上的元素到底是什么。

我们首先确定排列中的首个元素 a_1a 
1
​	
 。根据上述的结论，我们可以知道：

以 11 为 a_1a 
1
​	
  的排列一共有 (n-1)!(n−1)! 个；
以 22 为 a_1a 
1
​	
  的排列一共有 (n-1)!(n−1)! 个；
\cdots⋯
以 nn 为 a_1a 
1
​	
  的排列一共有 (n-1)!(n−1)! 个。
由于我们需要求出从小到大的第 kk 个排列，因此：

如果 k \leq (n-1)!k≤(n−1)!，我们就可以确定排列的首个元素为 11；
如果 (n-1)! < k \leq 2 \cdot (n-1)!(n−1)!<k≤2⋅(n−1)!，我们就可以确定排列的首个元素为 22；
\cdots⋯
如果 (n-1) \cdot (n-1)! < k \leq n \cdot (n-1)!(n−1)⋅(n−1)!<k≤n⋅(n−1)!，我们就可以确定排列的首个元素为 nn。
因此，第 kk 个排列的首个元素就是：

a_1 = \lfloor \frac{k-1}{(n-1)!} \rfloor + 1
a 
1
​	
 =⌊ 
(n−1)!
k−1
​	
 ⌋+1

其中 \lfloor x \rfloor⌊x⌋ 表示将 xx 向下取整。

当我们确定了 a_1a 
1
​	
  后，如何使用相似的思路，确定下一个元素 a_2a 
2
​	
  呢？实际上，我们考虑以 a_1a 
1
​	
  为首个元素的所有排列：

以 [1,n] \backslash a_1[1,n]\a 
1
​	
  最小的元素为 a_2a 
2
​	
  的排列一共有 (n-2)!(n−2)! 个；
以 [1,n] \backslash a_1[1,n]\a 
1
​	
  次小的元素为 a_2a 
2
​	
  的排列一共有 (n-2)!(n−2)! 个；
\cdots⋯
以 [1,n] \backslash a_1[1,n]\a 
1
​	
  最大的元素为 a_2a 
2
​	
  的排列一共有 (n-2)!(n−2)! 个；
其中 [1,n] \backslash a_1[1,n]\a 
1
​	
  表示包含 1, 2, \cdots n1,2,⋯n 中除去 a_1a 
1
​	
  以外元素的集合。这些排列从编号 (a_1-1) \cdot (n-1)!(a 
1
​	
 −1)⋅(n−1)! 开始，到 a_1 \cdot (n-1)!a 
1
​	
 ⋅(n−1)! 结束，总计 (n-1)!(n−1)! 个，因此第 kk 个排列实际上就对应着这其中的第

k' = (k-1) \bmod (n-1)! + 1
k 
′
 =(k−1)mod(n−1)!+1

个排列。这样一来，我们就把原问题转化成了一个完全相同但规模减少 11 的子问题：

求 [1, n] \backslash a_1[1,n]\a 
1
​	
  这 n-1n−1 个元素组成的排列中，第 k'k 
′
  小的排列。

算法

设第 kk 个排列为 a_1, a_2, \cdots, a_na 
1
​	
 ,a 
2
​	
 ,⋯,a 
n
​	
 ，我们从左往右地确定每一个元素 a_ia 
i
​	
 。我们用数组 \textit{valid}valid 记录每一个元素是否被使用过。

我们从小到大枚举 ii：

我们已经使用过了 i-1i−1 个元素，剩余 n-i+1n−i+1 个元素未使用过，每一个元素作为 a_ia 
i
​	
  都对应着 (n-i)!(n−i)! 个排列，总计 (n-i+1)!(n−i+1)! 个排列；

因此在第 kk 个排列中，a_ia 
i
​	
  即为剩余未使用过的元素中第 \lfloor \frac{k-1}{(n-i)!} \rfloor + 1⌊ 
(n−i)!
k−1
​	
 ⌋+1 小的元素；

在确定了 a_ia 
i
​	
  后，这 n-i+1n−i+1 个元素的第 kk 个排列，就等于 a_ia 
i
​	
  之后跟着剩余 n-in−i 个元素的第 (k-1) \bmod (n-i)! + 1(k−1)mod(n−i)!+1 个排列。

在实际的代码中，我们可以首先将 kk 的值减少 11，这样可以减少运算，降低代码出错的概率。对应上述的后两步，即为：

因此在第 kk 个排列中，a_ia 
i
​	
  即为剩余未使用过的元素中第 \lfloor \frac{k}{(n-i)!} \rfloor + 1⌊ 
(n−i)!
k
​	
 ⌋+1 小的元素；

在确定了 a_ia 
i
​	
  后，这 n-i+1n−i+1 个元素的第 kk 个排列，就等于 a_ia 
i
​	
  之后跟着剩余 n-in−i 个元素的第 k \bmod (n-i)!kmod(n−i)! 个排列。

实际上，这相当于我们将所有的排列从 00 开始进行编号。

代码

C++JavaPython3GolangC

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        factorial = [1]
        for i in range(1, n):
            factorial.append(factorial[-1] * i)
        
        k -= 1
        ans = list()
        valid = [1] * (n + 1)
        for i in range(1, n + 1):
            order = k // factorial[n - i] + 1
            for j in range(1, n + 1):
                order -= valid[j]
                if order == 0:
                    ans.append(str(j))
                    valid[j] = 0
                    break
            k %= factorial[n - i]

        return "".join(ans)
复杂度分析

时间复杂度：O(n^2)O(n 
2
 )。

空间复杂度：O(n)O(n)。

思考题

对于给定的排列 a_1, a_2, \cdots, a_na 
1
​	
 ,a 
2
​	
 ,⋯,a 
n
​	
 ，你能求出 kk 吗？

解答：

k = \left( \sum_{i=1}^n \textit{order}(a_i) \cdot (n-i)! \right) + 1
k=( 
i=1
∑
n
​	
 order(a 
i
​	
 )⋅(n−i)!)+1

其中 \textit{order}(a_i)order(a 
i
​	
 ) 表示 a_{i+1}, \cdots, a_na 
i+1
​	
 ,⋯,a 
n
​	
  中小于 a_ia 
i
​	
  的元素个数。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/permutation-sequence/solution/di-kge-pai-lie-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''