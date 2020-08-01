'''
632. Smallest Range Covering Elements from K Lists
You have k lists of sorted integers in ascending order. Find the smallest range that includes at least one number from each of the k lists.

We define the range [a,b] is smaller than range [c,d] if b-a < d-c or a < c if b-a == d-c.



Example 1:

Input: [[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
Output: [20,24]
Explanation:
List 1: [4, 10, 15, 24,26], 24 is in range [20,24].
List 2: [0, 9, 12, 20], 20 is in range [20,24].
List 3: [5, 18, 22, 30], 22 is in range [20,24].


Note:

The given list may contain duplicates, so ascending order means >= here.
1 <= k <= 3500
-105 <= value of elements <= 105.

632. 最小区间
你有 k 个升序排列的整数数组。找到一个最小区间，使得 k 个列表中的每个列表至少有一个数包含在其中。

我们定义如果 b-a < d-c 或者在 b-a == d-c 时 a < c，则区间 [a,b] 比 [c,d] 小。

示例 1:

输入:[[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
输出: [20,24]
解释:
列表 1：[4, 10, 15, 24, 26]，24 在区间 [20,24] 中。
列表 2：[0, 9, 12, 20]，20 在区间 [20,24] 中。
列表 3：[5, 18, 22, 30]，22 在区间 [20,24] 中。
注意:

给定的列表可能包含重复元素，所以在这里升序表示 >= 。
1 <= k <= 3500
-105 <= 元素的值 <= 105
对于使用Java的用户，请注意传入类型已修改为List<List<Integer>>。重置代码模板后可以看到这项改动。
'''


import heapq

class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        rangeLeft, rangeRight = -10 ** 9, 10 ** 9
        maxValue = max(vec[0] for vec in nums)
        priorityQueue = [(vec[0], i, 0) for i, vec in enumerate(nums)]
        heapq.heapify(priorityQueue)

        while True:
            minValue, row, idx = heapq.heappop(priorityQueue)
            print(minValue, row, idx)
            if maxValue - minValue < rangeRight - rangeLeft:
                rangeLeft, rangeRight = minValue, maxValue
            if idx == len(nums[row]) - 1:
                break
            maxValue = max(maxValue, nums[row][idx + 1])
            heapq.heappush(priorityQueue, (nums[row][idx + 1], row, idx + 1))

        return [rangeLeft, rangeRight]



# solutions

'''
def smallestRange(self, A):
    pq = [(row[0], i, 0) for i, row in enumerate(A)]
    heapq.heapify(pq)
    
    ans = -1e9, 1e9
    right = max(row[0] for row in A)
    while pq:
        left, i, j = heapq.heappop(pq)
        if right - left < ans[1] - ans[0]:
            ans = left, right
        if j + 1 == len(A[i]):
            return ans
        v = A[i][j+1]
        right = max(right, v)
        heapq.heappush(pq, (v, i, j+1))
Keep a heap of the smallest elements. As we pop element A[i][j], we'll replace it with A[i][j+1]. For each such element left, we want right, the maximum of the closest value in each row of the array that is >= left, which is also equal to the current maximum of our heap. We'll keep track of right as we proceed.

Edited with thanks to @StefanPochmann
'''

# leetcode-solution
'''
方法一：堆
给定 kk 个列表，需要找到最小区间，使得每个列表都至少有一个数在该区间中。该问题可以转化为，从 kk 个列表中各取一个数，使得这 kk 个数中的最大值与最小值的差最小。

假设这 kk 个数中的最小值是第 ii 个列表中的 xx，对于任意 j \ne ij 

​	
 =i，设第 jj 个列表中被选为 kk 个数之一的数是 yy，则为了找到最小区间，yy 应该取第 jj 个列表中大于等于 xx 的最小的数。简单证明如下：假设 zz 也是第 jj 个列表中的数，且 z>yz>y，则有 z-x>y-xz−x>y−x，同时包含 xx 和 zz 的区间一定不会小于同时包含 xx 和 yy 的区间。因此，其余 k-1k−1 个列表中应该取大于等于 xx 的最小的数。

由于 kk 个列表都是升序排列的，因此对每个列表维护一个指针，通过指针得到列表中的元素，指针右移之后指向的元素一定大于或等于之前的元素。

使用最小堆维护 kk 个指针指向的元素中的最小值，同时维护堆中元素的最大值。初始时，kk 个指针都指向下标 00，最大元素即为所有列表的下标 00 位置的元素中的最大值。每次从堆中取出最小值，根据最大值和最小值计算当前区间，如果当前区间小于最小区间则用当前区间更新最小区间，然后将对应列表的指针右移，将新元素加入堆中，并更新堆中元素的最大值。

如果一个列表的指针超出该列表的下标范围，则说明该列表中的所有元素都被遍历过，堆中不会再有该列表中的元素，因此退出循环。

JavaC++GolangPython3C

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        rangeLeft, rangeRight = -10**9, 10**9
        maxValue = max(vec[0] for vec in nums)
        priorityQueue = [(vec[0], i, 0) for i, vec in enumerate(nums)]
        heapq.heapify(priorityQueue)

        while True:
            minValue, row, idx = heapq.heappop(priorityQueue)
            if maxValue - minValue < rangeRight - rangeLeft:
                rangeLeft, rangeRight = minValue, maxValue
            if idx == len(nums[row]) - 1:
                break
            maxValue = max(maxValue, nums[row][idx + 1])
            heapq.heappush(priorityQueue, (nums[row][idx + 1], row, idx + 1))
        
        return [rangeLeft, rangeRight]
复杂度分析

时间复杂度：O(nk \log k)O(nklogk)，其中 nn 是所有列表的平均长度，kk 是列表数量。所有的指针移动的总次数最多是 nknk 次，每次从堆中取出元素和添加元素都需要更新堆，时间复杂度是 O(\log k)O(logk)，因此总时间复杂度是 O(nk \log k)O(nklogk)。

空间复杂度：O(k)O(k)，其中 kk 是列表数量。空间复杂度取决于堆的大小，堆中维护 kk 个元素。

方法二：哈希表 + 滑动窗口
思路

在讲这个方法之前我们先思考这样一个问题：有一个序列 A = \{ a_1, a_2, \cdots, a_n \}A={a 
1
​	
 ,a 
2
​	
 ,⋯,a 
n
​	
 } 和一个序列 B = \{b_1, b_2, \cdots, b_m\}B={b 
1
​	
 ,b 
2
​	
 ,⋯,b 
m
​	
 }，请找出一个 BB 中的一个最小的区间，使得在这个区间中 AA 序列的每个数字至少出现一次，请注意 AA 中的元素可能重复，也就是说如果 AA 中有 pp 个 uu，那么你选择的这个区间中 uu 的个数一定不少于 pp。没错，这就是我们五月份的一道打卡题：「76. 最小覆盖子串」。官方题解使用了一种双指针的方法，遍历整个 BB 序列并用一个哈希表表示当前窗口中的元素：

右边界在每次遍历到新元素的时候右移，同时将拓展到的新元素加入哈希表
左边界右移当且仅当当前区间为一个合法的答案区间，即当前窗口内的元素包含 AA 中所有的元素，同时将原来左边界指向的元素从哈希表中移除
答案更新当且仅当当前窗口内的元素包含 AA 中所有的元素
如果这个地方不太理解，可以参考「76. 最小覆盖子串 - LeetCode 官方题解」。

回到这道题，我们发现这两道题的相似之处在于都要求我们找到某个符合条件的最小区间，我们可以借鉴「76. 最小覆盖子串」的做法：这里序列 \{ 0, 1, \cdots , k - 1 \}{0,1,⋯,k−1} 就是上面描述的 AA 序列，即 kk 个列表，我们需要在一个 BB 序列当中找到一个区间，可以覆盖 AA 序列。这里的 BB 序列是什么？我们可以用一个哈希映射来表示 BB 序列—— B[i]B[i] 表示 ii 在哪些列表当中出现过，这里哈希映射的键是一个整数，表示列表中的某个数值，哈希映射的值是一个数组，这个数组里的元素代表当前的键出现在哪些列表里。也许文字表述比较抽象，大家可以结合下面这个例子来理解。

如果列表集合为：

0: [-1, 2, 3]
1: [1]
2: [1, 2]
3: [1, 1, 3]
那么可以得到这样一个哈希映射

-1: [0]
 1: [1, 2, 3, 3]
 2: [0, 2]
 3: [0, 3]
我们得到的这个哈希映射就是这里的 BB 序列。我们要做的就是在 BB 序列上使用双指针维护一个滑动窗口，并用一个哈希表维护当前窗口中已经包含了哪些列表中的元素，记录它们的索引。遍历 BB 序列的每一个元素：

指向窗口右边界的指针右移当且仅当每次遍历到新的元素，并将这个新的元素对应的值数组中的每一个数加入到哈希表中
指向窗口左边界的指针右移当且仅当当前窗口内的元素包含 AA 中所有的元素，同时将原来左边界对应的值数组的元素们从哈希表中移除
答案更新当且仅当当前窗口内的元素包含 AA 中所有的元素
大家可以参考代码理解这个过程。

代码

JavaC++GolangPython

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        n = len(nums)
        indices = collections.defaultdict(list)
        xMin, xMax = 10**9, -10**9
        for i, vec in enumerate(nums):
            for x in vec:
                indices[x].append(i)
            xMin = min(xMin, *vec)
            xMax = max(xMax, *vec)
        
        freq = [0] * n
        inside = 0
        left, right = xMin, xMin - 1
        bestLeft, bestRight = xMin, xMax

        while right < xMax:
            right += 1
            if right in indices:
                for x in indices[right]:
                    freq[x] += 1
                    if freq[x] == 1:
                        inside += 1
                while inside == n:
                    if right - left < bestRight - bestLeft:
                        bestLeft, bestRight = left, right
                    if left in indices:
                        for x in indices[left]:
                            freq[x] -= 1
                            if freq[x] == 0:
                                inside -= 1
                    left += 1

        return [bestLeft, bestRight]
复杂度分析

时间复杂度：O(nk + |V|)O(nk+∣V∣)，其中 nn 是所有列表的平均长度，kk 是列表数量，|V|∣V∣ 是列表中元素的值域，在本题中 |V| \leq 2*10^5∣V∣≤2∗10 
5
 。构造哈希映射的时间复杂度为 O(nk)O(nk)，双指针的移动范围为 |V|∣V∣，在此过程中会对哈希映射再进行一次遍历，时间复杂度为 O(nk)O(nk)，因此总时间复杂度为 O(nk + |V|)O(nk+∣V∣)。

空间复杂度：O(nk)O(nk)，即为哈希映射使用的空间。哈希映射的「键」的数量由列表中的元素个数 nknk 以及值域 |V|∣V∣ 中的较小值决定，「值」为长度不固定的数组，但是它们的长度之和为 nknk，因此哈希映射使用的空间为 O(nk)O(nk)。在使用双指针时，还需要一个长度为 nn 的数组，其对应的空间在渐进意义下小于 O(nk)O(nk)，因此可以忽略。

'''