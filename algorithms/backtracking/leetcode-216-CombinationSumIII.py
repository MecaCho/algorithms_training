# encoding=utf8

'''
216. 组合总和 III
找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。

说明：

所有数字都是正整数。
解集不能包含重复的组合。
示例 1:

输入: k = 3, n = 7
输出: [[1,2,4]]
示例 2:

输入: k = 3, n = 9
输出: [[1,2,6], [1,3,5], [2,3,4]]

216. Combination Sum III
Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Note:

All numbers will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Example 2:

Input: k = 3, n = 9
Output: [[1,2,6], [1,3,5], [2,3,4]]
'''


class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        self.vals = []
        def bk(target, start, path):
            if target < 0 or len(path) > k:
                return
            if target == 0 and len(path) == k:
                self.vals.append(path)
                return
            for i in range(start, 10):
                if i in path:
                    continue
                bk(target - i,i+1, path + [i])

        bk(n, 1, [])
        return self.vals



class Solution20200911(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        self.vals = []
        def bk(nums, sum_, start):
            if len(nums) > k or sum_ > n:
                return
            if sum_ == n and len(nums) == k:
                self.vals.append(nums)

            for i in range(start, 10):
                bk(nums+[i], sum_+i, i+1)

        bk([], 0, 1)
        return self.vals



# tips

'''
组合问题公式


dp[i] += dp[i-num]
True、False问题公式


dp[i] = dp[i] or dp[i-num]
最大最小问题公式


dp[i] = min(dp[i], dp[i-num]+1)或者dp[i] = max(dp[i], dp[i-num]+1)
以上三组公式是解决对应问题的核心公式。

当然拿到问题后，需要做到以下几个步骤：
1.分析是否为背包问题。
2.是以上三种背包问题中的哪一种。
3.是0-1背包问题还是完全背包问题。也就是题目给的nums数组中的元素是否可以重复使用。
4.如果是组合问题，是否需要考虑元素之间的顺序。需要考虑顺序有顺序的解法，不需要考虑顺序又有对应的解法。

接下来讲一下背包问题的判定
背包问题具备的特征：给定一个target，target可以是数字也可以是字符串，再给定一个数组nums，nums中装的可能是数字，也可能是字符串，问：能否使用nums中的元素做各种排列组合得到target。

背包问题技巧：

1.如果是0-1背包，即数组中的元素不可重复使用，nums放在外循环，target在内循环，且内循环倒序；
for num in nums:
    for i in range(target, nums-1, -1):
    
    
2.如果是完全背包，即数组中的元素可重复使用，nums放在外循环，target在内循环。且内循环正序。
for num in nums:
    for i in range(nums, target+1):
    
    
3.如果组合问题需考虑元素之间的顺序，需将target放在外循环，将nums放在内循环。
for i in range(1, target+1):
    for num in nums:
'''
