# encoding=utf8

'''
274. H-Index
Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return compute the researcher's h-index.

According to the definition of h-index on Wikipedia: A scientist has an index h if h of their n papers have at least h citations each, and the other n − h papers have no more than h citations each.

If there are several possible values for h, the maximum one is taken as the h-index.

 

Example 1:

Input: citations = [3,0,6,1,5]
Output: 3
Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively.
Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.
Example 2:

Input: citations = [1,3,1]
Output: 1
 

Constraints:

n == citations.length
1 <= n <= 5000
0 <= citations[i] <= 1000

274. H 指数
给定一位研究者论文被引用次数的数组（被引用次数是非负整数）。编写一个方法，计算出研究者的 h 指数。

h 指数的定义：h 代表“高引用次数”（high citations），一名科研人员的 h 指数是指他（她）的 （N 篇论文中）总共有 h 篇论文分别被引用了至少 h 次。且其余的 N - h 篇论文每篇被引用次数 不超过 h 次。

例如：某人的 h 指数是 20，这表示他已发表的论文中，每篇被引用了至少 20 次的论文总共有 20 篇。

 

示例：

输入：citations = [3,0,6,1,5]
输出：3 
解释：给定数组表示研究者总共有 5 篇论文，每篇论文相应的被引用了 3, 0, 6, 1, 5 次。
     由于研究者有 3 篇论文每篇 至少 被引用了 3 次，其余两篇论文每篇被引用 不多于 3 次，所以她的 h 指数是 3。
 

提示：如果 h 有多种可能的值，h 指数是其中最大的那个。
'''

# golang solution

'''
func hIndex(citations []int) int {
	sort.Ints(citations)
	i := sort.Search(len(citations), func(i int) bool {
		return citations[i] >= (len(citations)-i)
	})
	return len(citations)-i
}
'''

# solutions

'''
方法一：排序
首先我们可以将初始的 \text{H}H 指数 hh 设为 00，然后将引用次数排序，并且对排序后的数组从大到小遍历。

根据 \text{H}H 指数的定义，如果当前 \text{H}H 指数为 hh 并且在遍历过程中找到当前值 \textit{citations}[i] > hcitations[i]>h，则说明我们找到了一篇被引用了至少 h+1h+1 次的论文，所以将现有的 hh 值加 11。继续遍历直到 hh 无法继续增大。最后返回 hh 作为最终答案。

JavaC#Python3JavaScriptGolangC++C

func hIndex(citations []int) (h int) {
    sort.Ints(citations)
    for i := len(citations) - 1; i >= 0 && citations[i] > h; i-- {
        h++
    }
    return
}
复杂度分析

时间复杂度：O(n \log n)O(nlogn)，其中 nn 为数组 \textit{citations}citations 的长度。即为排序的时间复杂度。

空间复杂度：O(\log n)O(logn)，其中 nn 为数组 \textit{citations}citations 的长度。即为排序的空间复杂度。

方法二：计数排序
根据上述解法我们发现，最终的时间复杂度与排序算法的时间复杂度有关，所以我们可以使用计数排序算法，新建并维护一个数组 \textit{counter}counter 用来记录当前引用次数的论文有几篇。

根据定义，我们可以发现 \text{H}H 指数不可能大于总的论文发表数，所以对于引用次数超过论文发表数的情况，我们可以将其按照总的论文发表数来计算即可。这样我们可以限制参与排序的数的大小为 [0,n][0,n]（其中 nn 为总的论文发表数），使得计数排序的时间复杂度降低到 O(n)O(n)。

最后我们可以从后向前遍历数组 \textit{counter}counter，对于每个 0 \le i \le n0≤i≤n，在数组 \textit{counter}counter 中得到大于或等于当前引用次数 ii 的总论文数。当我们找到一个 \text{H}H 指数时跳出循环，并返回结果。

JavaC#Python3JavaScriptGolangC++C

func hIndex(citations []int) (h int) {
    n := len(citations)
    counter := make([]int, n+1)
    for _, citation := range citations {
        if citation >= n {
            counter[n]++
        } else {
            counter[citation]++
        }
    }
    for i, tot := n, 0; i >= 0; i-- {
        tot += counter[i]
        if tot >= i {
            return i
        }
    }
    return 0
}
复杂度分析

时间复杂度：O(n)O(n)，其中 nn 为数组 \textit{citations}citations 的长度。需要遍历数组 \textit{citations}citations 一次，以及遍历长度为 n+1n+1 的数组 \textit{counter}counter 一次。

空间复杂度：O(n)O(n)，其中 nn 为数组 \textit{citations}citations 的长度。需要创建长度为 n+1n+1 的数组 \textit{counter}counter。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/h-index/solution/h-zhi-shu-by-leetcode-solution-fnhl/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
