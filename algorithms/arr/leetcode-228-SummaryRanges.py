# encoding=utf8

'''
228. Summary Ranges
You are given a sorted unique integer array nums.

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b


Example 1:

Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"
Example 2:

Input: nums = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: The ranges are:
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"
Example 3:

Input: nums = []
Output: []
Example 4:

Input: nums = [-1]
Output: ["-1"]
Example 5:

Input: nums = [0]
Output: ["0"]


Constraints:

0 <= nums.length <= 20
-231 <= nums[i] <= 231 - 1
All the values of nums are unique.
nums is sorted in ascending order.


228. 汇总区间
给定一个无重复元素的有序整数数组 nums 。

返回 恰好覆盖数组中所有数字 的 最小有序 区间范围列表。也就是说，nums 的每个元素都恰好被某个区间范围所覆盖，并且不存在属于某个范围但不属于 nums 的数字 x 。

列表中的每个区间范围 [a,b] 应该按如下格式输出：

"a->b" ，如果 a != b
"a" ，如果 a == b


示例 1：

输入：nums = [0,1,2,4,5,7]
输出：["0->2","4->5","7"]
解释：区间范围是：
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"
示例 2：

输入：nums = [0,2,3,4,6,8,9]
输出：["0","2->4","6","8->9"]
解释：区间范围是：
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"
示例 3：

输入：nums = []
输出：[]
示例 4：

输入：nums = [-1]
输出：["-1"]
示例 5：

输入：nums = [0]
输出：["0"]


提示：

0 <= nums.length <= 20
-231 <= nums[i] <= 231 - 1
nums 中的所有值都 互不相同
nums 按升序排列
'''


class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        res = []
        if not nums:
            return res
        start = nums[0]
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1] + 1:
                if nums[i - 1] > start:
                    res.append(str(start) + "->" + str(nums[i - 1]))
                else:
                    res.append(str(start))
                start = nums[i]
        if nums[-1] == start:
            res.append(str(start))
        else:
            res.append(str(start) + "->" + str(nums[-1]))
        return res


# solutions

'''
方法一：一次遍历
我们从数组的位置 00 出发，向右遍历。每次遇到相邻元素之间的差值大于 11 时，我们就找到了一个区间。遍历完数组之后，就能得到一系列的区间的列表。

在遍历过程中，维护下标 \textit{low}low 和 \textit{high}high 分别记录区间的起点和终点，对于任何区间都有 \textit{low} \le \textit{high}low≤high。当得到一个区间时，根据 \textit{low}low 和 \textit{high}high 的值生成区间的字符串表示。

当 \textit{low}<\textit{high}low<high 时，区间的字符串表示为 ``\textit{low} \rightarrow \textit{high}"‘‘low→high"；

当 \textit{low}=\textit{high}low=high 时，区间的字符串表示为 ``\textit{low}"‘‘low"。

C++JavaGolangCJavaScript

func summaryRanges(nums []int) (ans []string) {
    for i, n := 0, len(nums); i < n; {
        left := i
        for i++; i < n && nums[i-1]+1 == nums[i]; i++ {
        }
        s := strconv.Itoa(nums[left])
        if left < i-1 {
            s += "->" + strconv.Itoa(nums[i-1])
        }
        ans = append(ans, s)
    }
    return
}
复杂度分析

时间复杂度：O(n)O(n)，其中 nn 为数组的长度。

空间复杂度：O(1)O(1)。除了用于输出的空间外，额外使用的空间为常数。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/summary-ranges/solution/hui-zong-qu-jian-by-leetcode-solution-6zrs/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
