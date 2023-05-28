# encoding=utf8

'''
1439. 有序矩阵中的第 k 个最小数组和
给你一个 m * n 的矩阵 mat，以及一个整数 k ，矩阵中的每一行都以非递减的顺序排列。

你可以从每一行中选出 1 个元素形成一个数组。返回所有可能数组中的第 k 个 最小 数组和。



示例 1：

输入：mat = [[1,3,11],[2,4,6]], k = 5
输出：7
解释：从每一行中选出一个元素，前 k 个和最小的数组分别是：
[1,2], [1,4], [3,2], [3,4], [1,6]。其中第 5 个的和是 7 。
示例 2：

输入：mat = [[1,3,11],[2,4,6]], k = 9
输出：17
示例 3：

输入：mat = [[1,10,10],[1,4,5],[2,3,6]], k = 7
输出：9
解释：从每一行中选出一个元素，前 k 个和最小的数组分别是：
[1,1,2], [1,1,3], [1,4,2], [1,4,3], [1,1,6], [1,5,2], [1,5,3]。其中第 7 个的和是 9 。
示例 4：

输入：mat = [[1,1,10],[2,2,9]], k = 7
输出：12


提示：

m == mat.length
n == mat.length[i]
1 <= m, n <= 40
1 <= k <= min(200, n ^ m)
1 <= mat[i][j] <= 5000
mat[i] 是一个非递减数组


1439. Find the Kth Smallest Sum of a Matrix With Sorted Rows
You are given an m * n matrix, mat, and an integer k, which has its rows sorted in non-decreasing order.

You are allowed to choose exactly 1 element from each row to form an array. Return the Kth smallest array sum among all possible arrays.



Example 1:

Input: mat = [[1,3,11],[2,4,6]], k = 5
Output: 7
Explanation: Choosing one element from each row, the first k smallest sum are:
[1,2], [1,4], [3,2], [3,4], [1,6]. Where the 5th sum is 7.
Example 2:

Input: mat = [[1,3,11],[2,4,6]], k = 9
Output: 17
Example 3:

Input: mat = [[1,10,10],[1,4,5],[2,3,6]], k = 7
Output: 9
Explanation: Choosing one element from each row, the first k smallest sum are:
[1,1,2], [1,1,3], [1,4,2], [1,4,3], [1,1,6], [1,5,2], [1,5,3]. Where the 7th sum is 9.
Example 4:

Input: mat = [[1,1,10],[2,2,9]], k = 7
Output: 12


Constraints:

m == mat.length
n == mat.length[i]
1 <= m, n <= 40
1 <= k <= min(200, n ^ m)
1 <= mat[i][j] <= 5000
mat[i] is a non decreasing array.
'''


class Solution(object):
    def kthSmallest(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: int
        """
        n = len(mat)
        pre = [0]

        for i in range(n):
            cur = [a + b for a, b in itertools.product(pre, mat[i])]
            pre = heapq.nsmallest(min(k, len(cur)), cur)

        return pre[-1]

        # end = 0
        # for i in range(1, len(mat[0])+1):
        #     if i ** len(mat) >= k:
        #         end = i
        #         break
        # print(end)

        # self.vals = []
        # length = len(mat)
        # def backtrack(res, n):
        #     if n == length:
        #         self.vals.append(sum(res))
        #         # heapq.heappush(self.vals, sum(res))
        #     else:
        #         for j in range(0, end):
        #             # print(end, j)
        #             backtrack(res+[mat[n][j]], n+1)

        # backtrack([], 0)
        # print(sorted(self.vals))
        # # return sorted(self.vals, key=lambda x: sum(x))[k-1]
        # if k > len(self.vals):
        #     return 0
        # # print(heapq.nsmallest(k, self.vals))
        # return sorted(self.vals)[k-1]


        # steps = []
        # i = j =0
        # while i <= len(mat) and j <= len(mat[0]):
        #     i += 1
        #     j += 1
        #     steps.append(i*j)
        # for k in range(len(steps)):
        #     if k <= steps[k]:
        #         new_arr = [for i in mat[k]]




        # # for i in range(len(mat)):
        # #     for j in range(len(mat[0])):
        # #         steps.append((i+1)*(j+1))
        # print(steps)
        # return

# tips

'''
Save all visited sums and corresponding indexes in a priority queue. Then, once you pop the smallest sum so far, you can quickly identify the next m candidates for smallest sum by incrementing each row index by 1.
'''


'''
暴力解法
解题思路
将“求前m行的第k个最小数组和”按动态规划的思路划分成子问题：已知前m-1行的最小数组和的列表，求前m行的第k个最小数组和。
例如，mat = [[1,10,10],[1,4,5],[2,3,6]]，k = 7。已知前两行的最小数组和last_row = [2,5,6,11,11,14,14,15,15]。我们截取last_row的前k个元素（因为后面的元素不再有竞争力），last_row = [2,5,6,11,11,14,14]。然后遍历第三行的每个元素，与last_row的每个元素求和，排序+截取后得到new_row = [4, 5, 7, 8, 8, 8, 9]。返回第k个元素即可。
复杂度分析
时间复杂度：O(m*max(nk, klog(k))O(m∗max(nk,klog(k))。遍历每行，时间复杂度为O(m)O(m)。对于每一行，遍历每一列的元素并求和为O(nk)O(nk)，对该行求出的数组和排序的复杂度为O(klog(k))O(klog(k))。
空间复杂度：O(k)O(k)。每行都要存储一个长度不超过k的"数组和"列表。
代码
class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        last_row = [0]
        for i in range(len(mat)):
            new_row = [] 
            for j in range(len(mat[0])):
                for p in last_row:
                    new_row.append(p + mat[i][j])
            new_row.sort()
            if len(new_row) > k:
                last_row = new_row[ :k]
            else:
                last_row = new_row
        return last_row[k - 1]
最小堆
解题思路
可以先看下264. 丑数 II这道题。T264的最小堆解法：每次从堆中弹出最小的丑数，然后把该丑数能生成的新的丑数push入堆。
本题也很相似，每次从堆中弹出最小的数组和curr_sum和对应的指针pointers，然后轮流将指针pointers的每个索引向后移动一位，生成新的new_sum，加入堆中。
算法流程
最小堆存储的是[curr_sum, pointers]二元组，pointers是指针数组，curr_sum是该pointers指向的元素的和。初始化pointers全为0，求出相应的curr_sum，并将其入堆。
重复下列步骤k次：
从堆中pop出curr_sum和pointers。
遍历pointers的每个索引，将该索引加一，求出新的和，如果没有出现过，push入堆。
栗子
以mat = [[1,10,10],[1,4,5],[2,3,6]]，k = 7为例，初始化pointers = (0, 0, 0)，curr_sum = 4，哈希表seen加入(0, 0, 0)
从堆中pop出最小和，pointers = (0, 0, 0)，curr_sum = 4。新生成[13, (1, 0, 0)],[7, (0, 1, 0)]，[5, (0, 0, 1)]，在seen中做好标记，然后将三者入堆。重复该步骤k次。
复杂度分析
时间复杂度：O(kmlog(k))O(kmlog(k))。执行k次循环：每次循环时，出堆操作，是O(log(k)))O(log(k)))；每次出堆后，要生成m个新的数组和，是O(n)O(n)；将新生成的的数组和入队，是O(logk)O(logk)。所以总的是O(k * (log(k) + m * log(k))) = O(kmlog(k)))O(k∗(log(k)+m∗log(k)))=O(kmlog(k)))
空间复杂度：O(km^2)O(km 
2
 )。堆中的元素个数不会超过km个，每个的空间是O(m)O(m)
代码
import heapq

class Solution:
    def kthSmallest(self, mat, k: int) -> int:
        m, n = len(mat), len(mat[0])
        # 初始化指针
        pointers = [0] * m 
        # 初始化heap
        heap = []
        curr_sum = 0
        for i in range(m):
            curr_sum += mat[i][0]
        heapq.heappush(heap, [curr_sum, tuple(pointers)])
        # 初始化seen
        seen = set()
        seen.add(tuple(pointers))
        # 执行k次
        for _ in range(k):
            # 从堆中pop出curr_sum(最小数组和)和pointers(指针数组)
            curr_sum, pointers = heapq.heappop(heap)
            # 每个指针轮流后移一位，将new_sum(新的数组和)和new_pointers(新的指针数组)push入堆
            for i, j in enumerate(pointers):
                if j < n - 1:
                    new_pointers = list(pointers)
                    new_pointers[i] = j + 1
                    new_pointers = tuple(new_pointers)
                    if new_pointers not in seen:
                        new_sum = curr_sum + mat[i][j + 1]- mat[i][j]
                        heapq.heappush(heap, [new_sum, new_pointers])
                        seen.add(new_pointers)
        return curr_sum

作者：coldme-2
链接：https://leetcode-cn.com/problems/find-the-kth-smallest-sum-of-a-matrix-with-sorted-rows/solution/bao-li-jie-fa-zui-xiao-dui-by-coldme-2/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''

