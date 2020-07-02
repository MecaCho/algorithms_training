'''
378. 有序矩阵中第K小的元素
给定一个 n x n 矩阵，其中每行和每列元素均按升序排序，找到矩阵中第k小的元素。
请注意，它是排序后的第k小元素，而不是第k个元素。

示例:

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

返回 13。
说明:
你可以假设 k 的值永远是有效的, 1 ≤ k ≤ n2 。

378. Kth Smallest Element in a Sorted Matrix
Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.
Note:
You may assume k is always valid, 1 ≤ k ≤ n2.
'''


class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        def get_lower_nums(mid, row, col):
            i = row - 1
            j = 0
            cnt = 0
            while i >= 0 and j < col:
                if (matrix[i][j] <= mid):
                    cnt = cnt + i + 1
                    j+= 1
                else:
                    i -= 1
            return cnt
        if not matrix:
            return 0
        if not matrix[0]:
            return 0
        col_len = len(matrix)
        row_len = len(matrix[0])
        i = matrix[0][0]
        j = matrix[col_len-1][row_len - 1]
        while i <= j:
            mid = (i + j)/2
            nums = get_lower_nums(mid, row_len, col_len)
            if nums > k-1:
                j = mid - 1
            elif nums <= k-1:
                i = mid + 1
            # else:
            #     return mid
        return i


# solutions


'''
方法一：直接排序
思路及算法

最直接的做法是将这个二维数组另存为为一维数组，并对该一维数组进行排序。最后这个一维数组中的第 kk 个数即为答案。

代码

C++JavaPython3GolangC

func kthSmallest(matrix [][]int, k int) int {
    rows, columns := len(matrix), len(matrix[0])
    sorted := make([]int, rows * columns)
    index := 0
    for _, row := range matrix {
        for _, num := range row {
            sorted[index] = num
            index++
        }
    }
    sort.Ints(sorted)
    return sorted[k-1]
}
复杂度分析

时间复杂度：O(n^2\log{n})O(n 
2
 logn)，对 n^2n 
2
  个数排序。

空间复杂度：O(n^2)O(n 
2
 )，一维数组需要存储这 n^2n 
2
  个数。

方法二：归并排序
思路及算法

由题目给出的性质可知，这个矩阵的每一行均为一个有序数组。问题即转化为从这 nn 个有序数组中找第 kk 大的数，可以想到利用归并排序的做法，归并到第 kk 个数即可停止。

一般归并排序是两个数组归并，而本题是 nn 个数组归并，所以需要用小根堆维护，以优化时间复杂度。

具体如何归并，可以参考力扣 23. 合并K个排序链表。

代码

C++JavaPython3GolangC

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        pq = [(matrix[i][0], i, 0) for i in range(n)]
        heapq.heapify(pq)

        ret = 0
        for i in range(k - 1):
            num, x, y = heapq.heappop(pq)
            if y != n - 1:
                heapq.heappush(pq, (matrix[x][y + 1], x, y + 1))
        
        return heapq.heappop(pq)[0]
复杂度分析

时间复杂度：O(k\log{n})O(klogn)，归并 kk 次，每次堆中插入和弹出的操作时间复杂度均为 \log{n}logn。

空间复杂度：O(n)O(n)，堆的大小始终为 nn。

需要注意的是，kk 在最坏情况下是 n^2n 
2
 ，因此该解法最坏时间复杂度为 O(n^2\log{n})O(n 
2
 logn)。

方法三：二分查找
思路及算法

由题目给出的性质可知，这个矩阵内的元素是从左上到右下递增的（假设矩阵左上角为 matrix[0][0]matrix[0][0]）。以下图为例：



我们知道整个二维数组中 matrix[0][0]matrix[0][0] 为最小值，matrix[n - 1][n - 1]matrix[n−1][n−1] 为最大值，现在我们将其分别记作 ll 和 rr。

可以发现一个性质：任取一个数 midmid 满足 l\leq mid \leq rl≤mid≤r，那么矩阵中不大于 midmid 的数，肯定全部分布在矩阵的左上角。

例如下图，取 mid=8mid=8：



我们可以看到，矩阵中大于 midmid 的数就和不大于 midmid 的数分别形成了两个板块，沿着一条锯齿线将这个矩形分开。其中左上角板块的大小即为矩阵中不大于 midmid 的数的数量。

读者也可以自己取一些 midmid 值，通过画图以加深理解。

我们只要沿着这条锯齿线走一遍即可计算出这两个板块的大小，也自然就统计出了这个矩阵中不大于 midmid 的数的个数了。

走法演示如下，依然取 mid=8mid=8：



可以这样描述走法：

初始位置在 matrix[n - 1][0]matrix[n−1][0]（即左下角）；

设当前位置为 matrix[i][j]matrix[i][j]。若 matrix[i][j] \leq midmatrix[i][j]≤mid，则将当前所在列的不大于 midmid 的数的数量（即 i + 1i+1）累加到答案中，并向右移动，否则向上移动；

不断移动直到走出格子为止。

我们发现这样的走法时间复杂度为 O(n)O(n)，即我们可以线性计算对于任意一个 midmid，矩阵中有多少数不小于它。这满足了二分答案的性质。

不妨假设答案为 xx，那么可以知道 l\leq x\leq rl≤x≤r，这样就确定了二分答案的上下界。

每次对于「猜测」的答案 midmid，计算矩阵中有多少数不大于 midmid ：

如果数量不多于 kk，那么说明最终答案 xx 不小于 midmid；
如果数量少于 kk，那么说明最终答案 xx 大于 midmid。
这样我们就可以计算出最终的结果 xx 了。

代码

C++JavaPython3GolangC

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)

        def check(mid):
            i, j = n - 1, 0
            num = 0
            while i >= 0 and j < n:
                if matrix[i][j] <= mid:
                    num += i + 1
                    j += 1
                else:
                    i -= 1
            return num >= k

        left, right = matrix[0][0], matrix[-1][-1]
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1
        
        return left
复杂度分析

时间复杂度：O(n\log(r-l))O(nlog(r−l))，二分查找进行次数为 O(\log(r-l))O(log(r−l))，每次操作时间复杂度为 O(n)O(n)。

空间复杂度：O(1)O(1)。

写在最后
上述三种解法，第一种没有利用矩阵的性质，所以时间复杂度最差；第二种解法只利用了一部分性质（每一列是一个有序数列，而忽视了行之间的关系）；第三种解法则利用了全部性质，所以时间复杂度最佳。

这也启示我们要认真把握题目中的条件与性质，更有利于我们解题。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/kth-smallest-element-in-a-sorted-matrix/solution/you-xu-ju-zhen-zhong-di-kxiao-de-yuan-su-by-leetco/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''