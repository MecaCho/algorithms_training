# encoding=utf8

'''
330. Patching Array
Given a sorted positive integer array nums and an integer n, add/patch elements to the array such that any number in range [1, n] inclusive can be formed by the sum of some elements in the array. Return the minimum number of patches required.

Example 1:

Input: nums = [1,3], n = 6
Output: 1
Explanation:
Combinations of nums are [1], [3], [1,3], which form possible sums of: 1, 3, 4.
Now if we add/patch 2 to nums, the combinations are: [1], [2], [3], [1,3], [2,3], [1,2,3].
Possible sums are 1, 2, 3, 4, 5, 6, which now covers the range [1, 6].
So we only need 1 patch.
Example 2:

Input: nums = [1,5,10], n = 20
Output: 2
Explanation: The two patches can be [2, 4].
Example 3:

Input: nums = [1,2,2], n = 5
Output: 0


330. 按要求补齐数组
给定一个已排序的正整数数组 nums，和一个正整数 n 。从 [1, n] 区间内选取任意个数字补充到 nums 中，使得 [1, n] 区间内的任何数字都可以用 nums 中某几个数字的和来表示。请输出满足上述要求的最少需要补充的数字个数。

示例 1:

输入: nums = [1,3], n = 6
输出: 1
解释:
根据 nums 里现有的组合 [1], [3], [1,3]，可以得出 1, 3, 4。
现在如果我们将 2 添加到 nums 中， 组合变为: [1], [2], [3], [1,3], [2,3], [1,2,3]。
其和可以表示数字 1, 2, 3, 4, 5, 6，能够覆盖 [1, 6] 区间里所有的数。
所以我们最少需要添加一个数字。
示例 2:

输入: nums = [1,5,10], n = 20
输出: 2
解释: 我们需要添加 [2, 4]。
示例 3:

输入: nums = [1,2,2], n = 5
输出: 0
'''


class Solution(object):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        miss, res, i = 1, 0, 0
        while miss <= n:
            if i < len(nums) and nums[i] <= miss:
                miss += nums[i]
                i += 1
            else:
                miss += miss
                res += 1

        return res


# solution

'''
这道题给我们一个有序的正数数组nums，又给了我们一个正整数n，问我们最少需要给nums加几个数字，使其能组成[1,n]之间的所有数字，注意数组中的元素不能重复使用，否则的话只有要有1，就能组成所有的数字了。这道题我又不会了，上网看到了史蒂芬大神的解法，膜拜啊，这里就全部按他的解法来讲吧。我们定义一个变量miss，用来表示[0,n]之间最小的不能表示的值，那么初始化为1，为啥不为0呢，因为n=0没啥意义，直接返回0了。那么此时我们能表示的范围是[0, miss)，表示此时我们能表示0到miss-1的数，如果此时的num <= miss，那么我们可以把我们能表示数的范围扩大到[0, miss+num)，如果num>miss，那么此时我们需要添加一个数，为了能最大限度的增加表示数范围，我们加上miss它本身，以此类推直至遍历完整个数组，我们可以得到结果。下面我们来举个例子说明：

给定nums = [1, 2, 4, 11, 30], n = 50，我们需要让[0, 50]之间所有的数字都能被nums中的数字之和表示出来。

首先使用1, 2, 4可能表示出0到7之间的所有数，表示范围为[0, 8)，但我们不能表示8，因为下一个数字11太大了，所以我们要在数组里加上一个8，此时能表示的范围是[0, 16)，那么我们需要插入16吗，答案是不需要，因为我们数组有1和4，可以组成5，而下一个数字11，加一起能组成16，所以有了数组中的11，我们此时能表示的范围扩大到[0, 27)，但我们没法表示27，因为30太大了，所以此时我们给数组中加入一个27，那么现在能表示的范围是[0, 54)，已经满足要求了，我们总共添加了两个数8和27，所以返回2即可。
'''