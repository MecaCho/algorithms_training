'''
327. Count of Range Sum
Given an integer array nums, return the number of range sums that lie in [lower, upper] inclusive.
Range sum S(i, j) is defined as the sum of the elements in nums between indices i and j (i ≤ j), inclusive.

Note:
A naive algorithm of O(n2) is trivial. You MUST do better than that.

Example:

Input: nums = [-2,5,-1], lower = -2, upper = 2,
Output: 3
Explanation: The three ranges are : [0,0], [2,2], [0,2] and their respective sums are: -2, -1, 2.


Constraints:

0 <= nums.length <= 10^4

327. 区间和的个数
给定一个整数数组 nums，返回区间和在 [lower, upper] 之间的个数，包含 lower 和 upper。
区间和 S(i, j) 表示在 nums 中，位置从 i 到 j 的元素之和，包含 i 和 j (i ≤ j)。

说明:
最直观的算法复杂度是 O(n2) ，请在此基础上优化你的算法。

示例:

输入: nums = [-2,5,-1], lower = -2, upper = 2,
输出: 3
解释: 3个区间分别是: [0,0], [2,2], [0,2]，它们表示的和分别为: -2, -1, 2。
'''


class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        # count = 0
        # for i in range(len(nums)):
        #     sum_ = 0
        #     for j in range(i, len(nums)):
        #         sum_ += nums[j]
        #         if lower <= sum_ <= upper:
        #             count += 1

        # return count

        first = [0]
        for num in nums:
            first.append(first[-1] + num)
        def sort(lo, hi):
            mid = (lo + hi) / 2
            if mid == lo:
                return 0
            count = sort(lo, mid) + sort(mid, hi)
            i = j = mid
            for left in first[lo:mid]:
                while i < hi and first[i] - left <  lower: i += 1
                while j < hi and first[j] - left <= upper: j += 1
                count += j - i
            first[lo:hi] = sorted(first[lo:hi])
            return count
        return sort(0, len(first))


# solution

'''
First compute the prefix sums: first[m] is the sum of the first m numbers.
Then the sum of any subarray nums[i:k] is simply first[k] - first[i].
So we just need to count those where first[k] - first[i] is in [lower,upper].

To find those pairs, I use mergesort with embedded counting. The pairs in the left half and the pairs in the right half get counted in the recursive calls. We just need to also count the pairs that use both halves.

For each left in first[lo:mid] I find all right in first[mid:hi] so that right - left lies in [lower, upper]. Because the halves are sorted, these fitting right values are a subarray first[i:j]. With increasing left we must also increase right, meaning must we leave out first[i] if it's too small and and we must include first[j] if it's small enough.

Besides the counting, I also need to actually merge the halves for the sorting. I let sorted do that, which uses Timsort and takes linear time to recognize and merge the already sorted halves.
'''