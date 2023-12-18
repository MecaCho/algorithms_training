# encoding=utf8


'''

162. 寻找峰值
峰值元素是指其值大于左右相邻值的元素。

给定一个输入数组 nums，其中 nums[i] ≠ nums[i+1]，找到峰值元素并返回其索引。

数组可能包含多个峰值，在这种情况下，返回任何一个峰值所在位置即可。

你可以假设 nums[-1] = nums[n] = -∞。

示例 1:

输入: nums = [1,2,3,1]
输出: 2
解释: 3 是峰值元素，你的函数应该返回其索引 2。
示例 2:

输入: nums = [1,2,1,3,5,6,4]
输出: 1 或 5 
解释: 你的函数可以返回索引 1，其峰值元素为 2；
     或者返回索引 5， 其峰值元素为 6。
说明:

你的解法应该是 O(logN) 时间复杂度的。


162. Find Peak Element
A peak element is an element that is greater than its neighbors.

Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that nums[-1] = nums[n] = -∞.

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 1 or 5 
Explanation: Your function can return either index number 1 where the peak element is 2, 
             or index number 5 where the peak element is 6.
Note:

Your solution should be in logarithmic complexity.
'''

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        def get_value(i):
            if i == -1 or i == n:
                return -float("inf")
            return nums[i]

        l, r = 0, n-1
        while True:
            mid = (l+r) // 2
            if get_value(mid-1) < get_value(mid) and get_value(mid) > get_value(mid+1):
                return mid
            if get_value(mid) < get_value(mid+1):
                l = mid + 1
            else:
                r = mid - 1





class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                return i
        return len(nums) - 1

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for i in range(len(nums)):
            if nums[i] > nums[res]:
                res = i

        return res

# solutions

'''
方法一：寻找最大值
思路与算法

由于题目保证了 \textit{nums}[i] \neq \textit{nums}[i+1]nums[i] 

​
 =nums[i+1]，那么数组 \textit{nums}nums 中最大值两侧的元素一定严格小于最大值本身。因此，最大值所在的位置就是一个可行的峰值位置。

我们对数组 \textit{nums}nums 进行一次遍历，找到最大值对应的位置即可。

代码

C++JavaC#Python3GolangJavaScript

func findPeakElement(nums []int) (idx int) {
    for i, v := range nums {
        if v > nums[idx] {
            idx = i
        }
    }
    return
}
复杂度分析

时间复杂度：O(n)O(n)，其中 nn 是数组 \textit{nums}nums 的长度。

空间复杂度：O(1)O(1)。

方法二：迭代爬坡
思路与算法

俗话说「人往高处走，水往低处流」。如果我们从一个位置开始，不断地向高处走，那么最终一定可以到达一个峰值位置。

因此，我们首先在 [0, n)[0,n) 的范围内随机一个初始位置 ii，随后根据 \textit{nums}[i-1], \textit{nums}[i], \textit{nums}[i+1]nums[i−1],nums[i],nums[i+1] 三者的关系决定向哪个方向走：

如果 \textit{nums}[i-1] < \textit{nums}[i] > \textit{nums}[i+1]nums[i−1]<nums[i]>nums[i+1]，那么位置 ii 就是峰值位置，我们可以直接返回 ii 作为答案；

如果 \textit{nums}[i-1] < \textit{nums}[i] < \textit{nums}[i+1]nums[i−1]<nums[i]<nums[i+1]，那么位置 ii 处于上坡，我们需要往右走，即 i \leftarrow i+1i←i+1；

如果 \textit{nums}[i-1] > \textit{nums}[i] > \textit{nums}[i+1]nums[i−1]>nums[i]>nums[i+1]，那么位置 ii 处于下坡，我们需要往左走，即 i \leftarrow i-1i←i−1；

如果 \textit{nums}[i-1] > \textit{nums}[i] < \textit{nums}[i+1]nums[i−1]>nums[i]<nums[i+1]，那么位置 ii 位于山谷，两侧都是上坡，我们可以朝任意方向走。

如果我们规定对于最后一种情况往右走，那么当位置 ii 不是峰值位置时：

如果 \textit{nums}[i] < \textit{nums}[i+1]nums[i]<nums[i+1]，那么我们往右走；

如果 \textit{nums}[i] > \textit{nums}[i+1]nums[i]>nums[i+1]，那么我们往左走。

代码

C++JavaC#Python3GolangJavaScript

func findPeakElement(nums []int) int {
    n := len(nums)
    idx := rand.Intn(n)

    // 辅助函数，输入下标 i，返回 nums[i] 的值
    // 方便处理 nums[-1] 以及 nums[n] 的边界情况
    get := func(i int) int {
        if i == -1 || i == n {
            return math.MinInt64
        }
        return nums[i]
    }

    for !(get(idx-1) < get(idx) && get(idx) > get(idx+1)) {
        if get(idx) < get(idx+1) {
            idx++
        } else {
            idx--
        }
    }

    return idx
}
复杂度分析

时间复杂度：O(n)O(n)，其中 nn 是数组 \textit{nums}nums 的长度。在最坏情况下，数组 \textit{nums}nums 单调递增，并且我们随机到位置 00，这样就需要向右走到数组 \textit{nums}nums 的最后一个位置。

空间复杂度：O(1)O(1)。

方法三：方法二的二分查找优化
思路与算法

我们可以发现，如果 \textit{nums}[i] < \textit{nums}[i+1]nums[i]<nums[i+1]，并且我们从位置 ii 向右走到了位置 i+1i+1，那么位置 ii 左侧的所有位置是不可能在后续的迭代中走到的。

这是因为我们每次向左或向右移动一个位置，要想「折返」到位置 ii 以及其左侧的位置，我们首先需要在位置 i+1i+1 向左走到位置 ii，但这是不可能的。

并且根据方法二，我们知道位置 i+1i+1 以及其右侧的位置中一定有一个峰值，因此我们可以设计出如下的一个算法：

对于当前可行的下标范围 [l, r][l,r]，我们随机一个下标 ii；

如果下标 ii 是峰值，我们返回 ii 作为答案；

如果 \textit{nums}[i] < \textit{nums}[i+1]nums[i]<nums[i+1]，那么我们抛弃 [l, i][l,i] 的范围，在剩余 [i+1, r][i+1,r] 的范围内继续随机选取下标；

如果 \textit{nums}[i] > \textit{nums}[i+1]nums[i]>nums[i+1]，那么我们抛弃 [i, r][i,r] 的范围，在剩余 [l, i-1][l,i−1] 的范围内继续随机选取下标。

在上述算法中，如果我们固定选取 ii 为 [l, r][l,r] 的中点，那么每次可行的下标范围会减少一半，成为一个类似二分查找的方法，时间复杂度为 O(\log n)O(logn)。

代码

C++JavaC#Python3GolangJavaScript

func findPeakElement(nums []int) int {
    n := len(nums)

    // 辅助函数，输入下标 i，返回 nums[i] 的值
    // 方便处理 nums[-1] 以及 nums[n] 的边界情况
    get := func(i int) int {
        if i == -1 || i == n {
            return math.MinInt64
        }
        return nums[i]
    }

    left, right := 0, n-1
    for {
        mid := (left + right) / 2
        if get(mid-1) < get(mid) && get(mid) > get(mid+1) {
            return mid
        }
        if get(mid) < get(mid+1) {
            left = mid + 1
        } else {
            right = mid - 1
        }
    }
}
复杂度分析

时间复杂度：O(\log n)O(logn)，其中 nn 是数组 \textit{nums}nums 的长度。

空间复杂度：O(1)O(1)。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/find-peak-element/solution/xun-zhao-feng-zhi-by-leetcode-solution-96sj/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
