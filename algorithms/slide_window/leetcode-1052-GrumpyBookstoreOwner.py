# encoding=utf8

'''
1052. Grumpy Bookstore Owner
Today, the bookstore owner has a store open for customers.length minutes.  Every minute, some number of customers (customers[i]) enter the store, and all those customers leave after the end of that minute.

On some minutes, the bookstore owner is grumpy.  If the bookstore owner is grumpy on the i-th minute, grumpy[i] = 1, otherwise grumpy[i] = 0.  When the bookstore owner is grumpy, the customers of that minute are not satisfied, otherwise they are satisfied.

The bookstore owner knows a secret technique to keep themselves not grumpy for X minutes straight, but can only use it once.

Return the maximum number of customers that can be satisfied throughout the day.



Example 1:

Input: customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], X = 3
Output: 16
Explanation: The bookstore owner keeps themselves not grumpy for the last 3 minutes.
The maximum number of customers that can be satisfied = 1 + 1 + 1 + 1 + 7 + 5 = 16.


Note:

1 <= X <= customers.length == grumpy.length <= 20000
0 <= customers[i] <= 1000
0 <= grumpy[i] <= 1


1052. 爱生气的书店老板
今天，书店老板有一家店打算试营业 customers.length 分钟。每分钟都有一些顾客（customers[i]）会进入书店，所有这些顾客都会在那一分钟结束后离开。

在某些时候，书店老板会生气。 如果书店老板在第 i 分钟生气，那么 grumpy[i] = 1，否则 grumpy[i] = 0。 当书店老板生气时，那一分钟的顾客就会不满意，不生气则他们是满意的。

书店老板知道一个秘密技巧，能抑制自己的情绪，可以让自己连续 X 分钟不生气，但却只能使用一次。

请你返回这一天营业下来，最多有多少客户能够感到满意的数量。


示例：

输入：customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], X = 3
输出：16
解释：
书店老板在最后 3 分钟保持冷静。
感到满意的最大客户数量 = 1 + 1 + 1 + 1 + 7 + 5 = 16.


提示：

1 <= X <= customers.length == grumpy.length <= 20000
0 <= customers[i] <= 1000
0 <= grumpy[i] <= 1
'''


class Solution(object):
    def maxSatisfied(self, customers, grumpy, X):
        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type X: int
        :rtype: int
        """
        total = sum([c*(1-g) for c, g in zip(customers, grumpy)])

        add = sum([c for c, g in zip(customers[:X], grumpy[:X]) if g])

        res = total + add
        for i in range(X, len(customers)):
            if grumpy[i] == 1:
                add += grumpy[i] * customers[i]
            if grumpy[i-X] == 1:
                add -= grumpy[i-X] * customers[i-X]
            res = max(res, total + add)

        return res



# solutions

'''
方法一：滑动窗口
假设数组 \textit{customers}customers 和 \textit{grumpy}grumpy 的长度是 nn，不使用秘密技巧时，满意的顾客数量是 \textit{total}total，则 \textit{total}total 的值为：

\textit{total}=\sum\limits_{i=0}^{n-1} \textit{customers}[i] \times \mathbb{I}(\textit{grumpy}[i]=0)
total= 
i=0
∑
n−1
​	
 customers[i]×I(grumpy[i]=0)

其中 \mathbb{I}(\textit{grumpy}[i]=0)I(grumpy[i]=0) 为示性函数，当 \textit{grumpy}[i]=0grumpy[i]=0 时 \mathbb{I}(\textit{grumpy}[i]=0)=1I(grumpy[i]=0)=1，当 \textit{grumpy}[i]=1grumpy[i]=1 时 \mathbb{I}(\textit{grumpy}[i]=0)=0I(grumpy[i]=0)=0。

秘密技巧的效果是，找到数组 \textit{grumpy}grumpy 的一个长度为 XX 的子数组，使得该子数组中的元素都变成 00，数组 \textit{customers}customers 的对应下标范围的子数组中的所有顾客都变成满意的。如果对下标范围 [i-X+1,i][i−X+1,i] 的子数组使用秘密技巧时（其中 i \ge X-1i≥X−1），增加的满意顾客的数量是 \textit{increase}_iincrease 
i
​	
 ，则 \textit{increase}_iincrease 
i
​	
  的值为：

\textit{increase}_i=\sum\limits_{j=i-X+1}^i \textit{customers}[j] \times \mathbb{I}(\textit{grumpy}[j]=1)
increase 
i
​	
 = 
j=i−X+1
∑
i
​	
 customers[j]×I(grumpy[j]=1)

其中 \mathbb{I}(\textit{grumpy}[j]=1)I(grumpy[j]=1) 为示性函数，当 \textit{grumpy}[j]=1grumpy[j]=1 时 \mathbb{I}(\textit{grumpy}[j]=1)=1I(grumpy[j]=1)=1，当 \textit{grumpy}[j]=0grumpy[j]=0 时 \mathbb{I}(\textit{grumpy}[j]=1)=0I(grumpy[j]=1)=0。由于 \textit{grumpy}[j]grumpy[j] 的值只能是 11 或 00，因此 \mathbb{I}(\textit{grumpy}[j]=1)=\textit{grumpy}[j]I(grumpy[j]=1)=grumpy[j]，\textit{increase}_iincrease 
i
​	
  的值可以表示成如下形式：

\textit{increase}_i=\sum\limits_{j=i-X+1}^i \textit{customers}[j] \times \textit{grumpy}[j]
increase 
i
​	
 = 
j=i−X+1
∑
i
​	
 customers[j]×grumpy[j]

为了让满意的顾客数量最大化，应该找到满足 X-1 \le i<nX−1≤i<n 的下标 ii，使得 \textit{increase}_iincrease 
i
​	
  的值最大。

注意到当 i>X-1i>X−1 时，将 ii 替换成 i-1i−1，可以得到 \textit{increase}_{i-1}increase 
i−1
​	
  的值为：

\textit{increase}_{i-1}=\sum\limits_{j=i-X}^{i-1} \textit{customers}[j] \times \textit{grumpy}[j]
increase 
i−1
​	
 = 
j=i−X
∑
i−1
​	
 customers[j]×grumpy[j]

将 \textit{increase}_iincrease 
i
​	
  和 \textit{increase}_{i-1}increase 
i−1
​	
  相减，可以得到如下关系：

\begin{aligned} &\quad \ \textit{increase}_i-\textit{increase}_{i-1} \\ &= \textit{customers}[i] \times \textit{grumpy}[i]-\textit{customers}[i-X] \times \textit{grumpy}[i-X] \end{aligned}
​	
  
 increase 
i
​	
 −increase 
i−1
​	
 
=customers[i]×grumpy[i]−customers[i−X]×grumpy[i−X]
​	
 

整理得到：

\textit{increase}_i=\textit{increase}_{i-1}-\textit{customers}[i-X] \times \textit{grumpy}[i-X]+\textit{customers}[i] \times \textit{grumpy}[i]
increase 
i
​	
 =increase 
i−1
​	
 −customers[i−X]×grumpy[i−X]+customers[i]×grumpy[i]

上述过程可以看成维护一个长度为 XX 的滑动窗口。当滑动窗口从下标范围 [i-X,i-1][i−X,i−1] 移动到下标范围 [i-X+1,i][i−X+1,i] 时，下标 i-Xi−X 从窗口中移出，下标 ii 进入到窗口内。

利用上述关系，可以在 O(1)O(1) 的时间内通过 \textit{increase}_{i-1}increase 
i−1
​	
  得到 \textit{increase}_iincrease 
i
​	
 。

由于长度为 XX 的子数组的最小结束下标是 X-1X−1，因此第一个长度为 XX 的子数组对应的 \textit{increase}increase 的值为 \textit{increase}_{X-1}increase 
X−1
​	
 ，需要通过遍历数组 \textit{customers}customers 和 \textit{grumpy}grumpy 的前 XX 个元素计算得到。从 \textit{increase}_Xincrease 
X
​	
  到 \textit{increase}_{n-1}increase 
n−1
​	
  的值则可利用上述关系快速计算得到。只需要遍历数组 \textit{customers}customers 和 \textit{grumpy}grumpy 各一次即可得到 X \le i<nX≤i<n 的每个 \textit{increase}_iincrease 
i
​	
  的值，时间复杂度是 O(n)O(n)。

又由于计算初始的 \textit{total}total 的值需要遍历数组 \textit{customers}customers 和 \textit{grumpy}grumpy 各一次，因此整个过程只需要遍历数组 \textit{customers}customers 和 \textit{grumpy}grumpy 各两次，时间复杂度是 O(n)O(n)。

在上述过程中维护增加的满意顾客的最大数量，记为 \textit{maxIncrease}maxIncrease，则满意顾客的最大总数是 \textit{total}+\textit{maxIncrease}total+maxIncrease。


1 / 9

JavaJavaScriptGolangPython3C++C

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        n = len(customers)
        total = sum(c for c, g in zip(customers, grumpy) if g == 0)
        maxIncrease = increase = sum(c * g for c, g in zip(customers[:X], grumpy[:X]))
        for i in range(X, n):
            increase += customers[i] * grumpy[i] - customers[i - X] * grumpy[i - X]
            maxIncrease = max(maxIncrease, increase)
        return total + maxIncrease
复杂度分析

时间复杂度：O(n)O(n)，其中 nn 是数组 \textit{customers}customers 和 \textit{grumpy}grumpy 的长度。需要对两个数组各遍历两次。

空间复杂度：O(1)O(1)。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/grumpy-bookstore-owner/solution/ai-sheng-qi-de-shu-dian-lao-ban-by-leetc-dloq/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''


