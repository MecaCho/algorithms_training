# encoding=utf8

'''
3524. Find X Value of Array I
You are given an array of positive integers nums, and a positive integer k.

You are allowed to perform an operation once on nums, where in each operation you can remove any non-overlapping prefix and suffix from nums such that nums remains non-empty.

You need to find the x-value of nums, which is the number of ways to perform this operation so that the product of the remaining elements leaves a remainder of x when divided by k.

Return an array result of size k where result[x] is the x-value of nums for 0 <= x <= k - 1.

A prefix of an array is a subarray that starts from the beginning of the array and extends to any point within it.

A suffix of an array is a subarray that starts at any point within the array and extends to the end of the array.

Note that the prefix and suffix to be chosen for the operation can be empty.

 

Example 1:

Input: nums = [1,2,3,4,5], k = 3
Output: [9,2,4]
Explanation:
For x = 0, the possible operations include all possible ways to remove non-overlapping prefix/suffix that do not remove nums[2] == 3.
For x = 1, the possible operations are:
- Remove the empty prefix and the suffix [2, 3, 4, 5]. nums becomes [1].
- Remove the prefix [1, 2, 3] and the suffix [5]. nums becomes [4].
For x = 2, the possible operations are:
- Remove the empty prefix and the suffix [3, 4, 5]. nums becomes [1, 2].
- Remove the prefix [1] and the suffix [3, 4, 5]. nums becomes [2].
- Remove the prefix [1, 2, 3] and the empty suffix. nums becomes [4, 5].
- Remove the prefix [1, 2, 3, 4] and the empty suffix. nums becomes [5].

Example 2:

Input: nums = [1,2,4,8,16,32], k = 4
Output: [18,1,2,0]
Explanation:
For x = 0, the only operations that do not result in x = 0 are:
- Remove the empty prefix and the suffix [4, 8, 16, 32]. nums becomes [1, 2].
- Remove the empty prefix and the suffix [2, 4, 8, 16, 32]. nums becomes [1].
- Remove the prefix [1] and the suffix [4, 8, 16, 32]. nums becomes [2].
For x = 1, the only possible operation is:
- Remove the empty prefix and the suffix [2, 4, 8, 16, 32]. nums becomes [1].
For x = 2, the possible operations are:
- Remove the empty prefix and the suffix [4, 8, 16, 32]. nums becomes [1, 2].
- Remove the prefix [1] and the suffix [4, 8, 16, 32]. nums becomes [2].
For x = 3, there is no possible way to perform the operation.

Example 3:

Input: nums = [1,1,2,1,1], k = 2
Output: [9,6]

 

Constraints:

1 <= nums[i] <= 10^9
1 <= nums.length <= 10^5
1 <= k <= 5


3524. 求出数组的 X 值 I
给你一个由 正 整数组成的数组 nums ，以及一个 正 整数 k 。

你可以对 nums 执行 一次 操作，该操作中可以移除任意 不重叠 的前缀和后缀，使得 nums 仍然 非空 。

你需要找出 nums 的 x 值 ，即在执行操作后，剩余元素的 乘积 除以 k 后的 余数 为 x 的操作数量。

返回一个大小为 k 的数组 result ，其中 result[x] 表示对于 0 <= x <= k - 1 ， nums 的 x 值 。

数组的 前缀 指从数组起始位置开始到数组中任意位置的一段连续子数组。

数组的 后缀 是指从数组中任意位置开始到数组末尾的一段连续子数组。

子数组 是数组中一段连续的元素序列。

注意 ，在操作中选择的前缀和后缀可以是 空的 。

 

示例 1：

输入：nums = [1,2,3,4,5], k = 3
输出：[9,2,4]
解释：
对于 x = 0 ，可行的操作包括所有不会移除 nums[2] == 3 的前后缀移除方式。
对于 x = 1 ，可行操作包括：
- 移除空前缀和后缀 [2, 3, 4, 5] ， nums 变为 [1] 。
- 移除前缀 [1, 2, 3] 和后缀 [5] ， nums 变为 [4] 。
对于 x = 2 ，可行操作包括：
- 移除空前缀和后缀 [3, 4, 5] ， nums 变为 [1, 2] 。
- 移除前缀 [1] 和后缀 [3, 4, 5] ， nums 变为 [2] 。
- 移除前缀 [1, 2, 3] 和空后缀， nums 变为 [4, 5] 。
- 移除前缀 [1, 2, 3, 4] 和空后缀， nums 变为 [5] 。

示例 2：

输入：nums = [1,2,4,8,16,32], k = 4
输出：[18,1,2,0]
解释：
对于 x = 0 ，唯一 不 得到 x = 0 的操作有：
- 移除空前缀和后缀 [4, 8, 16, 32] ， nums 变为 [1, 2] 。
- 移除空前缀和后缀 [2, 4, 8, 16, 32] ， nums 变为 [1] 。
- 移除前缀 [1] 和后缀 [4, 8, 16, 32] ， nums 变为 [2] 。
对于 x = 1 ，唯一的操作是：
- 移除空前缀和后缀 [2, 4, 8, 16, 32] ， nums 变为 [1] 。
对于 x = 2 ，可行操作包括：
- 移除空前缀和后缀 [4, 8, 16, 32] ， nums 变为 [1, 2] 。
- 移除前缀 [1] 和后缀 [4, 8, 16, 32] ， nums 变为 [2] 。
对于 x = 3 ，没有可行的操作。

示例 3：

输入：nums = [1,1,2,1,1], k = 2
输出：[9,6]

 

提示：

1 <= nums[i] <= 10^9
1 <= nums.length <= 10^5
1 <= k <= 5
'''


class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        ans = [0] * k
        # f[r] 表示以当前位置的前一个位置结尾、乘积模 k 为 r 的子数组数量
        f = [0] * k

        for x in nums:
            g = [0] * k
            # 延长此前以各余数 r 结尾的子数组
            for r, cnt in enumerate(f):
                g[(r * x) % k] += cnt
            # 以当前元素 x 单独作为一个新子数组的起点
            g[x % k] += 1
            # 累加当前位置结尾的所有子数组乘积余数结果
            for r, cnt in enumerate(g):
                ans[r] += cnt
            f = g

        return ans


# golang solution

'''
func resultArray(nums []int, k int) []int64 {
	ans := make([]int64, k)
	// f[r] 表示以当前前驱位置结尾、乘积模 k 为 r 的子数组数量
	f := make([]int64, k)

	for _, x := range nums {
		g := make([]int64, k)
		// 延长此前以各余数 r 结尾的子数组
		for r, cnt := range f {
			g[(r*x)%k] += cnt
		}
		// 当前元素 x 作为新子数组的单元素
		g[x%k]++
		// 将以当前位置结尾的各类余数子数组计入总和
		for r, cnt := range g {
			ans[r] += cnt
		}
		f = g
	}

	return ans
}
'''

