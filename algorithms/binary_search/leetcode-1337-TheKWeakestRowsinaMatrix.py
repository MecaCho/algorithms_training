# encoding=utf8

'''
1337. The K Weakest Rows in a Matrix
You are given an m x n binary matrix mat of 1's (representing soldiers) and 0's (representing civilians). The soldiers are positioned in front of the civilians. That is, all the 1's will appear to the left of all the 0's in each row.

A row i is weaker than a row j if one of the following is true:

The number of soldiers in row i is less than the number of soldiers in row j.
Both rows have the same number of soldiers and i < j.
Return the indices of the k weakest rows in the matrix ordered from weakest to strongest.

 

Example 1:

Input: mat = 
[[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]], 
k = 3
Output: [2,0,3]
Explanation: 
The number of soldiers in each row is: 
- Row 0: 2 
- Row 1: 4 
- Row 2: 1 
- Row 3: 2 
- Row 4: 5 
The rows ordered from weakest to strongest are [2,0,3,1,4].
Example 2:

Input: mat = 
[[1,0,0,0],
 [1,1,1,1],
 [1,0,0,0],
 [1,0,0,0]], 
k = 2
Output: [0,2]
Explanation: 
The number of soldiers in each row is: 
- Row 0: 1 
- Row 1: 4 
- Row 2: 1 
- Row 3: 1 
The rows ordered from weakest to strongest are [0,2,3,1].
 

Constraints:

m == mat.length
n == mat[i].length
2 <= n, m <= 100
1 <= k <= m
matrix[i][j] is either 0 or 1.

1337. 矩阵中战斗力最弱的 K 行
给你一个大小为 m * n 的矩阵 mat，矩阵由若干军人和平民组成，分别用 1 和 0 表示。

请你返回矩阵中战斗力最弱的 k 行的索引，按从最弱到最强排序。

如果第 i 行的军人数量少于第 j 行，或者两行军人数量相同但 i 小于 j，那么我们认为第 i 行的战斗力比第 j 行弱。

军人 总是 排在一行中的靠前位置，也就是说 1 总是出现在 0 之前。

 

示例 1：

输入：mat = 
[[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]], 
k = 3
输出：[2,0,3]
解释：
每行中的军人数目：
行 0 -> 2 
行 1 -> 4 
行 2 -> 1 
行 3 -> 2 
行 4 -> 5 
从最弱到最强对这些行排序后得到 [2,0,3,1,4]
示例 2：

输入：mat = 
[[1,0,0,0],
 [1,1,1,1],
 [1,0,0,0],
 [1,0,0,0]], 
k = 2
输出：[0,2]
解释： 
每行中的军人数目：
行 0 -> 1 
行 1 -> 4 
行 2 -> 1 
行 3 -> 1 
从最弱到最强对这些行排序后得到 [0,2,3,1]
 

提示：

m == mat.length
n == mat[i].length
2 <= n, m <= 100
1 <= k <= m
matrix[i][j] 不是 0 就是 1
'''

class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        values = []
        for i in range(len(mat)):
            values.append((i, sum(mat[i])))
            
        values.sort(key=lambda x: x[1])
        # print(values)
        res = [x[0] for x in values]
        return res[:k] if len(res) > k else res

# solutions

'''
前言
由于本题中的矩阵行数 mm 和列数 nn 均不超过 100100，数据规模较小，因此我们可以设计出一些时间复杂度较高的方法，例如直接对整个矩阵进行一次遍历，计算出每一行的战斗力，再进行排序并返回最弱的 kk 行的索引。

下面我们根据矩阵的性质，给出一种时间复杂度较为优秀的方法。

方法一：二分查找 + 堆
思路与算法

题目描述中有一条重要的保证：

军人总是排在一行中的靠前位置，也就是说 11 总是出现在 00 之前。

因此，我们可以通过二分查找的方法，找出一行中最后的那个 11 的位置。如果其位置为 \textit{pos}pos，那么这一行 11 的个数就为 \textit{pos} + 1pos+1。特别地，如果这一行没有 11，那么令 \textit{pos}=-1pos=−1。

当我们得到每一行的战斗力后，我们可以将它们全部放入一个小根堆中，并不断地取出堆顶的元素 kk 次，这样我们就得到了最弱的 kk 行的索引。

需要注意的是，如果我们依次将每一行的战斗力以及索引（因为如果战斗力相同，索引较小的行更弱，所以我们需要在小根堆中存放战斗力和索引的二元组）放入小根堆中，那么这样做的时间复杂度是 O(m \log m)O(mlogm) 的。一种更好的方法是使用这 mm 个战斗力值直接初始化一个小根堆，时间复杂度为 O(m)O(m)。读者可以参考《算法导论》的 \text{6.3}6.3 节或者「堆排序中建堆过程时间复杂度 O(n)O(n) 怎么来的？」了解该过程时间复杂度的证明方法。

代码

C++JavaPython3Golang

func kWeakestRows(mat [][]int, k int) []int {
    h := hp{}
    for i, row := range mat {
        pow := sort.Search(len(row), func(j int) bool { return row[j] == 0 })
        h = append(h, pair{pow, i})
    }
    heap.Init(&h)
    ans := make([]int, k)
    for i := range ans {
        ans[i] = heap.Pop(&h).(pair).idx
    }
    return ans
}

type pair struct{ pow, idx int }
type hp []pair

func (h hp) Len() int            { return len(h) }
func (h hp) Less(i, j int) bool  { a, b := h[i], h[j]; return a.pow < b.pow || a.pow == b.pow && a.idx < b.idx }
func (h hp) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *hp) Push(v interface{}) { *h = append(*h, v.(pair)) }
func (h *hp) Pop() interface{}   { a := *h; v := a[len(a)-1]; *h = a[:len(a)-1]; return v }
复杂度分析

时间复杂度：O(m \log n + k \log m)O(mlogn+klogm)：

我们需要 O(m \log n)O(mlogn) 的时间对每一行进行二分查找。

我们需要 O(m)O(m) 的时间建立小根堆。

我们需要 O(k \log m)O(klogm) 的时间从堆中取出 kk 个最小的元素。

空间复杂度：O(m)O(m)，即为堆需要使用的空间。

方法二：二分查找 + 快速选择
思路与算法

我们也可以通过快速选择算法，在平均 O(m)O(m) 的时间内不计顺序地内找出 kk 个最小的元素，再使用排序算法在 O(k \log k)O(klogk) 的时间对这 kk 个最小的元素进行升序排序，就可以得到最终的答案。读者可以参考「剑指 Offer 40. 最小的k个数」官方题解的方法三或者「215. 数组中的第K个最大元素」的官方题解中的方法一了解快速选择算法，下面的代码将上述题解中的快速选择算法封装成一个 \text{Helper}Helper 类进行使用。

C++JavaC#Python3Golang

type pair struct{ pow, idx int }

func kWeakestRows(mat [][]int, k int) []int {
    m := len(mat)
    pairs := make([]pair, m)
    for i, row := range mat {
        pow := sort.Search(len(row), func(j int) bool { return row[j] == 0 })
        pairs[i] = pair{pow, i}
    }
    rand.Seed(time.Now().UnixNano())
    randomizedSelected(pairs, 0, m-1, k)
    pairs = pairs[:k]
    sort.Slice(pairs, func(i, j int) bool {
        a, b := pairs[i], pairs[j]
        return a.pow < b.pow || a.pow == b.pow && a.idx < b.idx
    })
    ans := make([]int, k)
    for i, p := range pairs {
        ans[i] = p.idx
    }
    return ans
}

func randomizedSelected(a []pair, l, r, k int) {
    if l >= r {
        return
    }
    pos := randomPartition(a, l, r)
    num := pos - l + 1
    if k == num {
        return
    }
    if k < num {
        randomizedSelected(a, l, pos-1, k)
    } else {
        randomizedSelected(a, pos+1, r, k-num)
    }
}

func randomPartition(a []pair, l, r int) int {
    i := rand.Intn(r-l+1) + l
    a[i], a[r] = a[r], a[i]
    return partition(a, l, r)
}

func partition(a []pair, l, r int) int {
    pivot := a[r]
    i := l - 1
    for j := l; j < r; j++ {
        if a[j].pow < pivot.pow || a[j].pow == pivot.pow && a[j].idx <= pivot.idx {
            i++
            a[i], a[j] = a[j], a[i]
        }
    }
    a[i+1], a[r] = a[r], a[i+1]
    return i + 1
}
复杂度分析

时间复杂度：O(m \log n + k \log k)O(mlogn+klogk)：

我们需要 O(m \log n)O(mlogn) 的时间对每一行进行二分查找。

我们需要 O(m)O(m) 的时间完成快速选择算法。

我们需要 O(k \log k)O(klogk) 的时间对这 kk 个最小的元素进行升序排序。

空间复杂度：O(m)O(m)，即为快速选择算法中的数组需要使用的空间。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/the-k-weakest-rows-in-a-matrix/solution/fang-zhen-zhong-zhan-dou-li-zui-ruo-de-k-xing-by-l/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
