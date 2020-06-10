
'''
4. 寻找两个正序数组的中位数
给定两个大小为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。

请你找出这两个正序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

你可以假设 nums1 和 nums2 不会同时为空。



示例 1:

nums1 = [1, 3]
nums2 = [2]

则中位数是 2.0
示例 2:

nums1 = [1, 2]
nums2 = [3, 4]

则中位数是 (2 + 3)/2 = 2.5

4. Median of Two Sorted Arrays
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5

'''



import heapq


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        new_nums = nums1+nums2
        length = len(new_nums)
        if length == 0:
            return 0
        heapq.heapify(new_nums)
        mid1 = None
        for i in range(length/2):
            mid1 = heapq.heappop(new_nums)
        if length % 2 == 0:
            return float(mid1 + heapq.heappop(new_nums)) / 2
        else:
            return heapq.heappop(new_nums)



        # length = len(nums1) + len(nums2)
        # new_nums = sorted(nums2+nums1)
        # if length % 2 == 0:
        #     return float(new_nums[length/2] + new_nums[length/2-1]) / 2
        # else:
        #     return new_nums[length/2]


# solutions

'''
方法一：二分查找
给定两个有序数组，要求找到两个有序数组的中位数，最直观的思路有以下两种：

使用归并的方式，合并两个有序数组，得到一个大的有序数组。大的有序数组的中间位置的元素，即为中位数。

不需要合并两个有序数组，只要找到中位数的位置即可。由于两个数组的长度已知，因此中位数对应的两个数组的下标之和也是已知的。维护两个指针，初始时分别指向两个数组的下标 00 的位置，每次将指向较小值的指针后移一位（如果一个指针已经到达数组末尾，则只需要移动另一个数组的指针），直到到达中位数的位置。

假设两个有序数组的长度分别为 mm 和 nn，上述两种思路的复杂度如何？

第一种思路的时间复杂度是 O(m+n)O(m+n)，空间复杂度是 O(m+n)O(m+n)。第二种思路虽然可以将空间复杂度降到 O(1)O(1)，但是时间复杂度仍是 O(m+n)O(m+n)。题目要求时间复杂度是 O(\log(m+n))O(log(m+n))，因此上述两种思路都不满足题目要求的时间复杂度。

如何把时间复杂度降低到 O(\log(m+n))O(log(m+n)) 呢？如果对时间复杂度的要求有 \loglog，通常都需要用到二分查找，这道题也可以通过二分查找实现。

根据中位数的定义，当 m+nm+n 是奇数时，中位数是两个有序数组中的第 (m+n)/2(m+n)/2 个元素，当 m+nm+n 是偶数时，中位数是两个有序数组中的第 (m+n)/2(m+n)/2 个元素和第 (m+n)/2+1(m+n)/2+1 个元素的平均值。因此，这道题可以转化成寻找两个有序数组中的第 kk 小的数，其中 kk 为 (m+n)/2(m+n)/2 或 (m+n)/2+1(m+n)/2+1。

假设两个有序数组分别是 \text{A}A 和 \text{B}B。要找到第 kk 个元素，我们可以比较 \text{A}[k/2-1]A[k/2−1] 和 \text{B}[k/2-1]B[k/2−1]，其中 // 表示整数除法。由于 \text{A}[k/2-1]A[k/2−1] 和 \text{B}[k/2-1]B[k/2−1] 的前面分别有 \text{A}[0\,..\,k/2-2]A[0..k/2−2] 和 \text{B}[0\,..\,k/2-2]B[0..k/2−2]，即 k/2-1k/2−1 个元素，对于 \text{A}[k/2-1]A[k/2−1] 和 \text{B}[k/2-1]B[k/2−1] 中的较小值，最多只会有 (k/2-1)+(k/2-1) \leq k/2-2(k/2−1)+(k/2−1)≤k/2−2 个元素比它小，那么它就不能是第 kk 小的数了。

因此我们可以归纳出三种情况：

如果 \text{A}[k/2-1] < \text{B}[k/2-1]A[k/2−1]<B[k/2−1]，则比 \text{A}[k/2-1]A[k/2−1] 小的数最多只有 \text{A}A 的前 k/2-1k/2−1 个数和 \text{B}B 的前 k/2-1k/2−1 个数，即比 \text{A}[k/2-1]A[k/2−1] 小的数最多只有 k-2k−2 个，因此 \text{A}[k/2-1]A[k/2−1] 不可能是第 kk 个数，\text{A}[0]A[0] 到 \text{A}[k/2-1]A[k/2−1] 也都不可能是第 kk 个数，可以全部排除。

如果 \text{A}[k/2-1] > \text{B}[k/2-1]A[k/2−1]>B[k/2−1]，则可以排除 \text{B}[0]B[0] 到 \text{B}[k/2-1]B[k/2−1]。

如果 \text{A}[k/2-1] = \text{B}[k/2-1]A[k/2−1]=B[k/2−1]，则可以归入第一种情况处理。



可以看到，比较 \text{A}[k/2-1]A[k/2−1] 和 \text{B}[k/2-1]B[k/2−1] 之后，可以排除 k/2k/2 个不可能是第 kk 小的数，查找范围缩小了一半。同时，我们将在排除后的新数组上继续进行二分查找，并且根据我们排除数的个数，减少 kk 的值，这是因为我们排除的数都不大于第 kk 小的数。

有以下三种情况需要特殊处理：

如果 \text{A}[k/2-1]A[k/2−1] 或者 \text{B}[k/2-1]B[k/2−1] 越界，那么我们可以选取对应数组中的最后一个元素。在这种情况下，我们必须根据排除数的个数减少 kk 的值，而不能直接将 kk 减去 k/2k/2。

如果一个数组为空，说明该数组中的所有元素都被排除，我们可以直接返回另一个数组中第 kk 小的元素。

如果 k=1k=1，我们只要返回两个数组首元素的最小值即可。

用一个例子说明上述算法。假设两个有序数组如下：

A: 1 3 4 9
B: 1 2 3 4 5 6 7 8 9
两个有序数组的长度分别是 44 和 99，长度之和是 1313，中位数是两个有序数组中的第 77 个元素，因此需要找到第 k=7k=7 个元素。

比较两个有序数组中下标为 k/2-1=2k/2−1=2 的数，即 \text{A}[2]A[2] 和 \text{B}[2]B[2]，如下面所示：

A: 1 3 4 9
       ↑
B: 1 2 3 4 5 6 7 8 9
       ↑
由于 \text{A}[2] > \text{B}[2]A[2]>B[2]，因此排除 \text{B}[0]B[0] 到 \text{B}[2]B[2]，即数组 \text{B}B 的下标偏移（offset）变为 33，同时更新 kk 的值：k=k-k/2=4k=k−k/2=4。

下一步寻找，比较两个有序数组中下标为 k/2-1=1k/2−1=1 的数，即 \text{A}[1]A[1] 和 \text{B}[4]B[4]，如下面所示，其中方括号部分表示已经被排除的数。

A: 1 3 4 9
     ↑
B: [1 2 3] 4 5 6 7 8 9
             ↑
由于 \text{A}[1] < \text{B}[4]A[1]<B[4]，因此排除 \text{A}[0]A[0] 到 \text{A}[1]A[1]，即数组 \text{A}A 的下标偏移变为 22，同时更新 kk 的值：k=k-k/2=2k=k−k/2=2。

下一步寻找，比较两个有序数组中下标为 k/2-1=0k/2−1=0 的数，即比较 \text{A}[2]A[2] 和 \text{B}[3]B[3]，如下面所示，其中方括号部分表示已经被排除的数。

A: [1 3] 4 9
         ↑
B: [1 2 3] 4 5 6 7 8 9
           ↑
由于 \text{A}[2]=B[3]A[2]=B[3]，根据之前的规则，排除 \text{A}A 中的元素，因此排除 \text{A}[2]A[2]，即数组 \text{A}A 的下标偏移变为 33，同时更新 kk 的值： k=k-k/2=1k=k−k/2=1。

由于 kk 的值变成 11，因此比较两个有序数组中的未排除下标范围内的第一个数，其中较小的数即为第 kk 个数，由于 \text{A}[3] > \text{B}[3]A[3]>B[3]，因此第 kk 个数是 \text{B}[3]=4B[3]=4。

A: [1 3 4] 9
           ↑
B: [1 2 3] 4 5 6 7 8 9
           ↑
JavaC++Python3Golang
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def getKthElement(k):
            """
            - 主要思路：要找到第 k (k>1) 小的元素，那么就取 pivot1 = nums1[k/2-1] 和 pivot2 = nums2[k/2-1] 进行比较
            - 这里的 "/" 表示整除
            - nums1 中小于等于 pivot1 的元素有 nums1[0 .. k/2-2] 共计 k/2-1 个
            - nums2 中小于等于 pivot2 的元素有 nums2[0 .. k/2-2] 共计 k/2-1 个
            - 取 pivot = min(pivot1, pivot2)，两个数组中小于等于 pivot 的元素共计不会超过 (k/2-1) + (k/2-1) <= k-2 个
            - 这样 pivot 本身最大也只能是第 k-1 小的元素
            - 如果 pivot = pivot1，那么 nums1[0 .. k/2-1] 都不可能是第 k 小的元素。把这些元素全部 "删除"，剩下的作为新的 nums1 数组
            - 如果 pivot = pivot2，那么 nums2[0 .. k/2-1] 都不可能是第 k 小的元素。把这些元素全部 "删除"，剩下的作为新的 nums2 数组
            - 由于我们 "删除" 了一些元素（这些元素都比第 k 小的元素要小），因此需要修改 k 的值，减去删除的数的个数
            """
            
            index1, index2 = 0, 0
            while True:
                # 特殊情况
                if index1 == m:
                    return nums2[index2 + k - 1]
                if index2 == n:
                    return nums1[index1 + k - 1]
                if k == 1:
                    return min(nums1[index1], nums2[index2])

                # 正常情况
                newIndex1 = min(index1 + k // 2 - 1, m - 1)
                newIndex2 = min(index2 + k // 2 - 1, n - 1)
                pivot1, pivot2 = nums1[newIndex1], nums2[newIndex2]
                if pivot1 <= pivot2:
                    k -= newIndex1 - index1 + 1
                    index1 = newIndex1 + 1
                else:
                    k -= newIndex2 - index2 + 1
                    index2 = newIndex2 + 1
        
        m, n = len(nums1), len(nums2)
        totalLength = m + n
        if totalLength % 2 == 1:
            return getKthElement((totalLength + 1) // 2)
        else:
            return (getKthElement(totalLength // 2) + getKthElement(totalLength // 2 + 1)) / 2

复杂度分析

时间复杂度：O(\log(m+n))O(log(m+n))，其中 mm 和 nn 分别是数组 \text{nums1}nums1 和 \text{nums2}nums2 的长度。初始时有 k=(m+n)/2k=(m+n)/2 或 k=(m+n)/2+1k=(m+n)/2+1，每一轮循环可以将查找范围减少一半，因此时间复杂度是 O(\log(m+n))O(log(m+n))。

空间复杂度：O(1)O(1)。

方法二：划分数组
说明

方法一的时间复杂度已经很优秀了，但本题存在时间复杂度更低的一种方法。这里给出推导过程，勇于挑战自己的读者可以进行尝试。

思路与算法

为了使用划分的方法解决这个问题，需要理解「中位数的作用是什么」。在统计中，中位数被用来：

将一个集合划分为两个长度相等的子集，其中一个子集中的元素总是大于另一个子集中的元素。

如果理解了中位数的划分作用，就很接近答案了。

首先，在任意位置 ii 将 \text{A}A 划分成两个部分：

           left_A            |          right_A
    A[0], A[1], ..., A[i-1]  |  A[i], A[i+1], ..., A[m-1]
由于 \text{A}A 中有 mm 个元素， 所以有 m+1m+1 种划分的方法（i \in [0, m]i∈[0,m]）。

\text{len}(\text{left\_A}) = i, \text{len}(\text{right\_A}) = m - ilen(left_A)=i,len(right_A)=m−i.

注意：当 i = 0i=0 时，\text{left\_A}left_A 为空集， 而当 i = mi=m 时, \text{right\_A}right_A 为空集。

采用同样的方式，在任意位置 jj 将 \text{B}B 划分成两个部分：

           left_B            |          right_B
    B[0], B[1], ..., B[j-1]  |  B[j], B[j+1], ..., B[n-1]
将 \text{left\_A}left_A 和 \text{left\_B}left_B 放入一个集合，并将 \text{right\_A}right_A 和 \text{right\_B}right_B 放入另一个集合。 再把这两个新的集合分别命名为 \text{left\_part}left_part 和 \text{right\_part}right_part：

          left_part          |         right_part
    A[0], A[1], ..., A[i-1]  |  A[i], A[i+1], ..., A[m-1]
    B[0], B[1], ..., B[j-1]  |  B[j], B[j+1], ..., B[n-1]
当 \text{A}A 和 \text{B}B 的总长度是偶数时，如果可以确认：

\text{len}(\text{left\_part}) = \text{len}(\text{right\_part})len(left_part)=len(right_part)
\max(\text{left\_part}) \leq \min(\text{right\_part})max(left_part)≤min(right_part)
那么，\{\text{A}, \text{B}\}{A,B} 中的所有元素已经被划分为相同长度的两个部分，且前一部分中的元素总是小于或等于后一部分中的元素。中位数就是前一部分的最大值和后一部分的最小值的平均值：

\text{median} = \frac{\text{max}(\text{left}\_\text{part}) + \text{min}(\text{right}\_\text{part})}{2}
median= 
2
max(left_part)+min(right_part)
​	
 

当 \text{A}A 和 \text{B}B 的总长度是奇数时，如果可以确认：

\text{len}(\text{left\_part}) = \text{len}(\text{right\_part})+1len(left_part)=len(right_part)+1
\max(\text{left\_part}) \leq \min(\text{right\_part})max(left_part)≤min(right_part)
那么，\{\text{A}, \text{B}\}{A,B} 中的所有元素已经被划分为两个部分，前一部分比后一部分多一个元素，且前一部分中的元素总是小于或等于后一部分中的元素。中位数就是前一部分的最大值：

\text{median} = \text{max}(\text{left}\_\text{part})
median=max(left_part)

第一个条件对于总长度是偶数和奇数的情况有所不同，但是可以将两种情况合并。第二个条件对于总长度是偶数和奇数的情况是一样的。

要确保这两个条件，只需要保证：

i + j = m - i + n - ji+j=m−i+n−j（当 m+nm+n 为偶数）或 i + j = m - i + n - j + 1i+j=m−i+n−j+1（当 m+nm+n 为奇数）。等号左侧为前一部分的元素个数，等号右侧为后一部分的元素个数。将 ii 和 jj 全部移到等号左侧，我们就可以得到 i+j = \frac{m + n + 1}{2}i+j= 
2
m+n+1
​	
 。这里的分数结果只保留整数部分。

0 \leq i \leq m0≤i≤m，0 \leq j \leq n0≤j≤n。如果我们规定 \text{A}A 的长度小于等于 \text{B}B 的长度，即 m \leq nm≤n。这样对于任意的 i \in [0, m]i∈[0,m]，都有 j = \frac{m + n + 1}{2} - i \in [0, n]j= 
2
m+n+1
​	
 −i∈[0,n]，那么我们在 [0, m][0,m] 的范围内枚举 ii 并得到 jj，就不需要额外的性质了。

如果 \text{A}A 的长度较大，那么我们只要交换 \text{A}A 和 \text{B}B 即可。

如果 m > nm>n ，那么得出的 jj 有可能是负数。

\text{B}[j-1] \leq \text{A}[i]B[j−1]≤A[i] 以及 \text{A}[i-1] \leq \text{B}[j]A[i−1]≤B[j]，即前一部分的最大值小于等于后一部分的最小值。

为了简化分析，假设 \text{A}[i-1], \text{B}[j-1], \text{A}[i], \text{B}[j]A[i−1],B[j−1],A[i],B[j] 总是存在。对于 i=0i=0、i=mi=m、j=0j=0、j=nj=n 这样的临界条件，我们只需要规定 A[-1]=B[-1]=-\inftyA[−1]=B[−1]=−∞，A[m]=B[n]=\inftyA[m]=B[n]=∞ 即可。这也是比较直观的：当一个数组不出现在前一部分时，对应的值为负无穷，就不会对前一部分的最大值产生影响；当一个数组不出现在后一部分时，对应的值为正无穷，就不会对后一部分的最小值产生影响。

所以我们需要做的是：

在 [0, m][0,m] 中找到 ii，使得：

\qquad \text{B}[j-1] \leq \text{A}[i]B[j−1]≤A[i] 且 \text{A}[i-1] \leq \text{B}[j]A[i−1]≤B[j]，其中 j = \frac{m + n + 1}{2} - ij= 
2
m+n+1
​	
 −i

我们证明它等价于：

在 [0, m][0,m] 中找到最大的 ii，使得：

\qquad \text{A}[i-1] \leq \text{B}[j]A[i−1]≤B[j]，其中 j = \frac{m + n + 1}{2} - ij= 
2
m+n+1
​	
 −i

这是因为：

当 ii 从 0 \sim m0∼m 递增时，\text{A}[i-1]A[i−1] 递增，\text{B}[j]B[j] 递减，所以一定存在一个最大的 ii 满足 A[i-1] \leq B[j]A[i−1]≤B[j]；

如果 ii 是最大的，那么说明 i+1i+1 不满足。将 i+1i+1 带入可以得到 A[i] > B[j-1]A[i]>B[j−1]，也就是 B[j - 1] < A[i]B[j−1]<A[i]，就和我们进行等价变换前 ii 的性质一致了（甚至还要更强）。

因此我们可以对 ii 在 [0, m][0,m] 的区间上进行二分搜索，找到最大的满足 A[i-1] \leq B[j]A[i−1]≤B[j] 的 ii 值，就得到了划分的方法。此时，划分前一部分元素中的最大值，以及划分后一部分元素中的最小值，才可能作为就是这两个数组的中位数。

JavaC++Python3Golang
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        infinty = 2**40
        m, n = len(nums1), len(nums2)
        left, right, ansi = 0, m, -1
        # median1：前一部分的最大值
        # median2：后一部分的最小值
        median1, median2 = 0, 0

        while left <= right:
            # 前一部分包含 nums1[0 .. i-1] 和 nums2[0 .. j-1]
            # // 后一部分包含 nums1[i .. m-1] 和 nums2[j .. n-1]
            i = (left + right) // 2
            j = (m + n + 1) // 2 - i

            # nums_im1, nums_i, nums_jm1, nums_j 分别表示 nums1[i-1], nums1[i], nums2[j-1], nums2[j]
            nums_im1 = (-infinty if i == 0 else nums1[i - 1])
            nums_i = (infinty if i == m else nums1[i])
            nums_jm1 = (-infinty if j == 0 else nums2[j - 1])
            nums_j = (infinty if j == n else nums2[j])

            if nums_im1 <= nums_j:
                ansi = i
                median1, median2 = max(nums_im1, nums_jm1), min(nums_i, nums_j)
                left = i + 1
            else:
                right = i - 1

        return (median1 + median2) / 2 if (m + n) % 2 == 0 else median1
复杂度分析

时间复杂度：O(\log\min(m,n)))O(logmin(m,n)))，其中 mm 和 nn 分别是数组 \text{nums1}nums1 和 \text{nums2}nums2 的长度。查找的区间是 [0, m][0,m]，而该区间的长度在每次循环之后都会减少为原来的一半。所以，只需要执行 \log mlogm 次循环。由于每次循环中的操作次数是常数，所以时间复杂度为 O(\log m)O(logm)。由于我们可能需要交换 \text{nums1}nums1 和 \text{nums2}nums2 使得 m \leq nm≤n，因此时间复杂度是 O(\log\min(m,n)))O(logmin(m,n)))。

空间复杂度：O(1)O(1)。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/median-of-two-sorted-arrays/solution/xun-zhao-liang-ge-you-xu-shu-zu-de-zhong-wei-s-114/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
