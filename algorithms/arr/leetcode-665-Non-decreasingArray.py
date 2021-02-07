# encoding=utf8

'''
665. Non-decreasing Array
Given an array nums with n integers, your task is to check if it could become non-decreasing by modifying at most one element.

We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) such that (0 <= i <= n - 2).



Example 1:

Input: nums = [4,2,3]
Output: true
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.
Example 2:

Input: nums = [4,2,1]
Output: false
Explanation: You can't get a non-decreasing array by modify at most one element.


Constraints:

n == nums.length
1 <= n <= 104
-105 <= nums[i] <= 105


665. 非递减数列
给你一个长度为 n 的整数数组，请你判断在 最多 改变 1 个元素的情况下，该数组能否变成一个非递减数列。

我们是这样定义一个非递减数列的： 对于数组中所有的 i (0 <= i <= n-2)，总满足 nums[i] <= nums[i + 1]。



示例 1:

输入: nums = [4,2,3]
输出: true
解释: 你可以通过把第一个4变成1来使得它成为一个非递减数列。
示例 2:

输入: nums = [4,2,1]
输出: false
解释: 你不能在只改变一个元素的情况下将其变为非递减数列。


说明：

1 <= n <= 10 ^ 4
- 10 ^ 5 <= nums[i] <= 10 ^ 5
'''



class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count = 0
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                count += 1
                if i > 0 and nums[i+1] < nums[i-1]:
                    nums[i+1] = nums[i]

        return count < 2


# solutions


'''
方法一：数组
首先思考如下问题：

要使数组 \textit{nums}nums 变成一个非递减数列，数组中至多有多少个 ii 满足 \textit{nums}[i]>\textit{nums}[i+1]nums[i]>nums[i+1]？

假设有两个不同的下标 ii, jj 满足上述不等式，不妨设 i<ji<j.

若 i+1<ji+1<j，则无论怎么修改 \textit{nums}[i]nums[i] 或 \textit{nums}[i+1]nums[i+1]，都不会影响 \textit{nums}[j]nums[j] 与 \textit{nums}[j+1]nums[j+1] 之间的大小关系；修改 \textit{nums}[j]nums[j] 或 \textit{nums}[j+1]nums[j+1] 也同理。因此，这种情况下，我们无法将 \textit{nums}nums 变成非递减数列。

若 i+1=ji+1=j，则有 \textit{nums}[i]>\textit{nums}[i+1]>\textit{nums}[i+2]nums[i]>nums[i+1]>nums[i+2]。同样地，无论怎么修改其中一个数，都无法使这三个数变为 \textit{nums}[i]\le\textit{nums}[i+1]\le\textit{nums}[i+2]nums[i]≤nums[i+1]≤nums[i+2] 的大小关系。

因此，上述问题的结论是:

至多一个。

满足这个条件就足够了吗？并不，对于满足该条件的数组 [3,4,1,2][3,4,1,2] 而言，无论怎么修改也无法将其变成非递减数列。

因此，若找到了一个满足 \textit{nums}[i]>\textit{nums}[i+1]nums[i]>nums[i+1] 的 ii，在修改 \textit{nums}[i]nums[i] 或 \textit{nums}[i+1]nums[i+1] 之后，还需要检查 \textit{nums}nums 是否变成了非递减数列。

我们可以将 \textit{nums}[i]nums[i] 修改成小于或等于 \textit{nums}[i+1]nums[i+1] 的数，但由于还需要保证 \textit{nums}[i]nums[i] 不小于它之前的数，\textit{nums}[i]nums[i] 越大越好，所以将 \textit{nums}[i]nums[i] 修改成 \textit{nums}[i+1]nums[i+1] 是最佳的；同理，对于 \textit{nums}[i+1]nums[i+1]，修改成 \textit{nums}[i]nums[i] 是最佳的。

C++JavaGolangJavaScriptC

func checkPossibility(nums []int) bool {
    for i := 0; i < len(nums)-1; i++ {
        x, y := nums[i], nums[i+1]
        if x > y {
            nums[i] = y
            if sort.IntsAreSorted(nums) {
                return true
            }
            nums[i] = x // 复原
            nums[i+1] = x
            return sort.IntsAreSorted(nums)
        }
    }
    return true
}
优化

上面的代码多次遍历了 \textit{nums}nums 数组，能否只遍历一次呢？

修改 \textit{nums}[i]nums[i] 为 \textit{nums}[i+1]nums[i+1] 后，还需要保证 \textit{nums}[i-1]\le\textit{nums}[i]nums[i−1]≤nums[i] 仍然成立，即 \textit{nums}[i-1]\le\textit{nums}[i+1]nums[i−1]≤nums[i+1]，若该不等式不成立则整个数组必然不是非递减的，则需要修改 \textit{nums}[i+1]nums[i+1] 为 \textit{nums}[i]nums[i]。修改完后，接着判断后续数字的大小关系。在遍历中统计 \textit{nums}[i]>\textit{nums}[i+1]nums[i]>nums[i+1] 的次数，若超过一次可以直接返回 \text{false}false。

C++JavaGolangJavaScriptC

func checkPossibility(nums []int) bool {
    cnt := 0
    for i := 0; i < len(nums)-1; i++ {
        x, y := nums[i], nums[i+1]
        if x > y {
            cnt++
            if cnt > 1 {
                return false
            }
            if i > 0 && y < nums[i-1] {
                nums[i+1] = x
            }
        }
    }
    return true
}
复杂度分析

时间复杂度：O(n)O(n)，其中 nn 是数组 \textit{nums}nums 的长度。

空间复杂度：O(1)O(1)。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/non-decreasing-array/solution/fei-di-jian-shu-lie-by-leetcode-solution-zdsm/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
