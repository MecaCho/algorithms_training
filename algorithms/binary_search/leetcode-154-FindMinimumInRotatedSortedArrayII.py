# encoding=utf8

'''
154. 寻找旋转排序数组中的最小值 II
假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

请找出其中最小的元素。

注意数组中可能存在重复的元素。

示例 1：

输入: [1,3,5]
输出: 1
示例 2：

输入: [2,2,2,0,1]
输出: 0
说明：

这道题是 寻找旋转排序数组中的最小值 的延伸题目。
允许重复会影响算法的时间复杂度吗？会如何影响，为什么？

154. Find Minimum in Rotated Sorted Array II
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

The array may contain duplicates.

Example 1:

Input: [1,3,5]
Output: 1
Example 2:

Input: [2,2,2,0,1]
Output: 0
Note:

This is a follow up problem to Find Minimum in Rotated Sorted Array.
Would allow duplicates affect the run-time complexity? How and why?
'''

# 执行用时 :
# 24 ms
# , 在所有 Python 提交中击败了
# 71.10%
# 的用户
# 内存消耗 :
# 12.8 MB
# , 在所有 Python 提交中击败了
# 33.33%
# 的用户
# 双指针

class Solution(object):
    def minArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i,j = 0, len(nums)-1
        while i < j:
            if nums[i+1] >= nums[i]:
                i += 1
            else:
                return nums[i+1]

            if nums[j-1] <= nums[j]:
                j -= 1
            else:
                return nums[j]

        return nums[0] if nums else None



# 二分法


class Solution1_(object):
    def minArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i, j = 0, len(nums) - 1
        while i < j:
            m = (i + j) // 2
            if nums[m] > nums[j]: i = m + 1
            elif nums[m] < nums[j]: j = m
            else: j -= 1
        return nums[i]

# 执行用时 :
# 28 ms
# , 在所有 Python 提交中击败了
# 55.78%
# 的用户
# 内存消耗 :
# 12.8 MB
# , 在所有 Python 提交中击败了
# 33.33%
# 的用户
class Solution1(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #             # 由于原始数组是递增，那么旋转之后，旋转点左右的两部分仍然是递增的
            # # 这里记原始数组中旋转点左侧的数组为 A，原始数组中旋转点右侧的数组为 B
            # # 旋转之后有原来的 AB 变成了 BA，
            # if nums[mid] > nums[r]:
            #     # 说明mid在原来的 B 部分
        i,j = 0, len(nums)-1
        while i < j:
            # 旋转之后有原来的 AB 变成了 BA，
            mid = (i+j) // 2
            if nums[mid] > nums[j]:
                # 说明mid在原来的 B 部分
                i = mid + 1
            elif nums[mid] < nums[j]:
                # # 说明mid在原来的 A 部分
                j = mid
            else:
                j -= 1
        return nums[i] if nums else None



class Solution20210409(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r)/2
            num = nums[mid]
            if num > nums[r]:
                l = mid + 1
            elif num == nums[r]:
                r -= 1
            else:
                r = mid
        return nums[l]


if __name__ == '__main__':
    demo = Solution20210409()
    res = demo.findMin([2,2,2,2,3,0,1,2,2,2])
    print res


# solutions

'''
本题是「153. 寻找旋转排序数组中的最小值」的延伸。读者可以先尝试第 153 题，体会在旋转数组中进行二分查找的思路，再来尝试解决本题。

方法一：二分查找
思路与算法

一个包含重复元素的升序数组在经过旋转之后，可以得到下面可视化的折线图：



其中横轴表示数组元素的下标，纵轴表示数组元素的值。图中标出了最小值的位置，是我们需要查找的目标。

我们考虑数组中的最后一个元素 xx：在最小值右侧的元素，它们的值一定都小于等于 xx；而在最小值左侧的元素，它们的值一定都大于等于 xx。因此，我们可以根据这一条性质，通过二分查找的方法找出最小值。

在二分查找的每一步中，左边界为 \it lowlow，右边界为 \it highhigh，区间的中点为 \it pivotpivot，最小值就在该区间内。我们将中轴元素 \textit{nums}[\textit{pivot}]nums[pivot] 与右边界元素 \textit{nums}[\textit{high}]nums[high] 进行比较，可能会有以下的三种情况：

第一种情况是 \textit{nums}[\textit{pivot}] < \textit{nums}[\textit{high}]nums[pivot]<nums[high]。如下图所示，这说明 \textit{nums}[\textit{pivot}]nums[pivot] 是最小值右侧的元素，因此我们可以忽略二分查找区间的右半部分。



第二种情况是 \textit{nums}[\textit{pivot}] > \textit{nums}[\textit{high}]nums[pivot]>nums[high]。如下图所示，这说明 \textit{nums}[\textit{pivot}]nums[pivot] 是最小值左侧的元素，因此我们可以忽略二分查找区间的左半部分。



第三种情况是 \textit{nums}[\textit{pivot}] == \textit{nums}[\textit{high}]nums[pivot]==nums[high]。如下图所示，由于重复元素的存在，我们并不能确定 \textit{nums}[\textit{pivot}]nums[pivot] 究竟在最小值的左侧还是右侧，因此我们不能莽撞地忽略某一部分的元素。我们唯一可以知道的是，由于它们的值相同，所以无论 \textit{nums}[\textit{high}]nums[high] 是不是最小值，都有一个它的「替代品」\textit{nums}[\textit{pivot}]nums[pivot]，因此我们可以忽略二分查找区间的右端点。



当二分查找结束时，我们就得到了最小值所在的位置。

C++JavaPython3CGolangJavaScript

class Solution:
    def findMin(self, nums: List[int]) -> int:    
        low, high = 0, len(nums) - 1
        while low < high:
            pivot = low + (high - low) // 2
            if nums[pivot] < nums[high]:
                high = pivot 
            elif nums[pivot] > nums[high]:
                low = pivot + 1
            else:
                high -= 1
        return nums[low]
复杂度分析

时间复杂度：平均时间复杂度为 O(\log n)O(logn)，其中 nn 是数组 \it numsnums 的长度。如果数组是随机生成的，那么数组中包含相同元素的概率很低，在二分查找的过程中，大部分情况都会忽略一半的区间。而在最坏情况下，如果数组中的元素完全相同，那么 \texttt{while}while 循环就需要执行 nn 次，每次忽略区间的右端点，时间复杂度为 O(n)O(n)。

空间复杂度：O(1)O(1)。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array-ii/solution/xun-zhao-xuan-zhuan-pai-xu-shu-zu-zhong-de-zui--16/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
