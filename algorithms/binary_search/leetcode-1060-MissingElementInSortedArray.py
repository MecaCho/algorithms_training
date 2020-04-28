'''
1060. 有序数组中的缺失元素
给出一个有序数组 A，数组中的每个数字都是 独一无二的，找出从数组最左边开始的第 K 个缺失数字。



示例 1：

输入：A = [4,7,9,10], K = 1
输出：5
解释：
第一个缺失数字为 5 。
示例 2：

输入：A = [4,7,9,10], K = 3
输出：8
解释：
缺失数字有 [5,6,8,...]，因此第三个缺失数字为 8 。
示例 3：

输入：A = [1,2,4], K = 3
输出：6
解释：
缺失数字有 [3,5,6,7,...]，因此第三个缺失数字为 6 。


提示：

1 <= A.length <= 50000
1 <= A[i] <= 1e7
1 <= K <= 1e8

1060. Missing Element in Sorted Array
Given a sorted array A of unique numbers, find the K-th missing number starting from the leftmost number of the array.



Example 1:

Input: A = [4,7,9,10], K = 1
Output: 5
Explanation:
The first missing number is 5.
Example 2:

Input: A = [4,7,9,10], K = 3
Output: 8
Explanation:
The missing numbers are [5,6,8,...], hence the third missing number is 8.
Example 3:

Input: A = [1,2,4], K = 3
Output: 6
Explanation:
The missing numbers are [3,5,6,7,...], hence the third missing number is 6.


Note:

1 <= A.length <= 50000
1 <= A[i] <= 1e7
1 <= K <= 1e8
'''


class Solution(object):
    def missingElement(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def get_num(k):
            if k < 0:
                return 0
            return nums[k] - nums[0] - k

        last = get_num(len(nums) - 1)
        if last < k:
            return nums[-1] + k- last

        i, j = 0, len(nums) - 1
        while i <= j:
            mid = (i + j) / 2
            mid_num = get_num(mid)
            if mid_num == k:
                return nums[mid] - 1
            if mid_num < k:
                i = mid + 1
            else:
                j = mid - 1

        return nums[i - 1] + k - get_num(i - 1)
