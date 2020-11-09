'''

973. 最接近原点的 K 个点
我们有一个由平面上的点组成的列表 points。需要从中找出 K 个距离原点 (0, 0) 最近的点。

（这里，平面上两点之间的距离是欧几里德距离。）

你可以按任何顺序返回答案。除了点坐标的顺序之外，答案确保是唯一的。



示例 1：

输入：points = [[1,3],[-2,2]], K = 1
输出：[[-2,2]]
解释：
(1, 3) 和原点之间的距离为 sqrt(10)，
(-2, 2) 和原点之间的距离为 sqrt(8)，
由于 sqrt(8) < sqrt(10)，(-2, 2) 离原点更近。
我们只需要距离原点最近的 K = 1 个点，所以答案就是 [[-2,2]]。
示例 2：

输入：points = [[3,3],[5,-1],[-2,4]], K = 2
输出：[[3,3],[-2,4]]
（答案 [[-2,4],[3,3]] 也会被接受。）


提示：

1 <= K <= points.length <= 10000
-10000 < points[i][0] < 10000
-10000 < points[i][1] < 10000
通过次数14,283提交次数24,478

973. K Closest Points to Origin
We have a list of points on the plane.  Find the K closest points to the origin (0, 0).

(Here, the distance between two points on a plane is the Euclidean distance.)

You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)



Example 1:

Input: points = [[1,3],[-2,2]], K = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].
Example 2:

Input: points = [[3,3],[5,-1],[-2,4]], K = 2
Output: [[3,3],[-2,4]]
(The answer [[-2,4],[3,3]] would also be accepted.)


Note:

1 <= K <= points.length <= 10000
-10000 < points[i][0] < 10000
-10000 < points[i][1] < 10000
'''


class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        l = []
        import heapq
        for i in range(len(points)):
            heapq.heappush(l, points[i])
        largest = heapq.nsmallest(K, l, key=lambda x :x[0 ] *x[0] + x[1 ] *x[1])

        return largest



class Solution20201109(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        points.sort(key=lambda x: x[0]**2 + x[1]**2)
        return points[:K] if K < len(points) else points


# solution

'''
前言
当我们计算出每个点到原点的欧几里得距离的平方后，本题和「剑指 Offer 40. 最小的k个数」是完全一样的题。

为什么是欧几里得距离的「平方」？这是因为欧几里得距离并不一定是个整数，在进行计算和比较时可能会引进误差；但它的平方一定是个整数，这样我们就无需考虑误差了。

方法一：排序
思路和算法

将每个点到原点的欧几里得距离的平方从小到大排序后，取出前 KK 个即可。

代码

C++JavaPython3GolangC

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        points.sort(key=lambda x: (x[0] ** 2 + x[1] ** 2))
        return points[:K]
复杂度分析

时间复杂度：O(n\log n)O(nlogn)，其中 nn 是数组 \textit{points}points 的长度。算法的时间复杂度即排序的时间复杂度。

空间复杂度：O(\log n)O(logn)，排序所需额外的空间复杂度为 O(\log n)O(logn)。

方法二：优先队列
思路和算法

我们可以使用一个优先队列（大根堆）实时维护前 KK 个最小的距离平方。

首先我们将前 KK 个点的编号（为了方便最后直接得到答案）以及对应的距离平方放入优先队列中，随后从第 K+1K+1 个点开始遍历：如果当前点的距离平方比堆顶的点的距离平方要小，就把堆顶的点弹出，再插入当前的点。当遍历完成后，所有在优先队列中的点就是前 KK 个距离最小的点。

不同的语言提供的优先队列的默认情况不一定相同。在 C++ 语言中，优先队列即为大根堆，但在 Python 语言中，优先队列为小根堆，因此我们需要在优先队列中存储（以及比较）距离平方的相反数。

代码

C++JavaPython3Golang

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        q = [(-x ** 2 - y ** 2, i) for i, (x, y) in enumerate(points[:K])]
        heapq.heapify(q)
        
        n = len(points)
        for i in range(K, n):
            x, y = points[i]
            dist = -x ** 2 - y ** 2
            heapq.heappushpop(q, (dist, i))
        
        ans = [points[identity] for (_, identity) in q]
        return ans
复杂度分析

时间复杂度：O(n\log K)O(nlogK)，其中 nn 是数组 \textit{points}points 的长度。由于优先队列维护的是前 KK 个距离最小的点，因此弹出和插入操作的单次时间复杂度均为 O(\log K)O(logK)。在最坏情况下，数组里 nn 个点都会插入，因此时间复杂度为 O(n\log K)O(nlogK)。

空间复杂度：O(K)O(K)，因为优先队列中最多有 KK 个点。
方法三：快速选择（快速排序的思想）
思路和算法

我们也可以借鉴快速排序的思想。

快速排序中的划分操作每次执行完后，都能将数组分成两个部分，其中小于等于分界值 \textit{pivot}pivot 的元素都会被放到左侧部分，而大于 \textit{pivot}pivot 的元素都都会被放到右侧部分。与快速排序不同的是，在本题中我们可以根据 KK 与 \textit{pivot}pivot 下标的位置关系，只处理划分结果的某一部分（而不是像快速排序一样需要处理两个部分）。

我们定义函数 random_select(left, right, K) 表示划分数组 \textit{points}points 的 [\textit{left},\textit{right}][left,right] 区间，并且需要找到其中第 KK 个距离最小的点。在一次划分操作完成后，设 \textit{pivot}pivot 的下标为 ii，即区间 [\textit{left}, i-1][left,i−1] 中的点的距离都小于等于 \textit{pivot}pivot，而区间 [i+1,\textit{right}][i+1,right] 的点的距离都大于 \textit{pivot}pivot。此时会有三种情况：

如果 K = i-\textit{left}+1K=i−left+1，那么说明 \textit{pivot}pivot 就是第 KK 个距离最小的点，我们可以结束整个过程；

如果 K < i-\textit{left}+1K<i−left+1，那么说明第 KK 个距离最小的点在 \textit{pivot}pivot 左侧，因此递归调用 random_select(left, i - 1, K)；

如果 K > i-\textit{left}+1K>i−left+1，那么说明第 KK 个距离最小的点在 \textit{pivot}pivot 右侧，因此递归调用 random_select(i + 1, right, K - (i - left + 1))。

在整个过程结束之后，第 KK 个距离最小的点恰好就在数组 \textit{points}points 中的第 KK 个位置，并且其左侧的所有点的距离都小于它。此时，我们就找到了前 KK 个距离最小的点。

代码

C++C++apiJavaPythonGolangC

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        def random_select(left: int, right: int, K: int):
            pivot_id = random.randint(left, right)
            pivot = points[pivot_id][0] ** 2 + points[pivot_id][1] ** 2
            points[right], points[pivot_id] = points[pivot_id], points[right]
            i = left - 1
            for j in range(left, right):
                if points[j][0] ** 2 + points[j][1] ** 2 <= pivot:
                    i += 1
                    points[i], points[j] = points[j], points[i]
            i += 1
            points[i], points[right] = points[right], points[i]
            # [left, i-1] 都小于等于 pivot, [i+1, right] 都大于 pivot
            if K < i - left + 1:
                random_select(left, i - 1, K)
            elif K > i - left + 1:
                random_select(i + 1, right, K - (i - left + 1))

        n = len(points)
        random_select(0, n - 1, K)
        return points[:K]
复杂度分析

时间复杂度：期望为 O(n)O(n)，其中 nn 是数组 \textit{points}points 的长度。由于证明过程很繁琐，所以不再这里展开讲。具体证明可以参考《算法导论》第 9 章第 2 小节。

最坏情况下，时间复杂度为 O(n^2)O(n 
2
 )。具体地，每次的划分点都是最大值或最小值，一共需要划分 n-1n−1 次，而一次划分需要线性的时间复杂度，所以最坏情况下时间复杂度为 O(n^2)O(n 
2
 )。

空间复杂度：期望为 O(\log n)O(logn)，即为递归调用的期望深度。

最坏情况下，空间复杂度为 O(n)O(n)，此时需要划分 n-1n−1 次，对应递归的深度为 n-1n−1 层，所以最坏情况下时间复杂度为 O(n)O(n)。

然而注意到代码中的递归都是「尾递归」，因此如果编译器支持尾递归优化，那么空间复杂度总为 O(1)O(1)。即使不支持尾递归优化，我们也可以很方便地将上面的代码改成循环迭代的写法。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/k-closest-points-to-origin/solution/zui-jie-jin-yuan-dian-de-k-ge-dian-by-leetcode-sol/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''