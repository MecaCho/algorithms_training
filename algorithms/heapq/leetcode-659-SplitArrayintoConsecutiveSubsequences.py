'''
659. Split Array into Consecutive Subsequences
Given an array nums sorted in ascending order, return true if and only if you can split it into 1 or more subsequences such that each subsequence consists of consecutive integers and has length at least 3.



Example 1:

Input: [1,2,3,3,4,5]
Output: True
Explanation:
You can split them into two consecutive subsequences :
1, 2, 3
3, 4, 5
Example 2:

Input: [1,2,3,3,4,4,5,5]
Output: True
Explanation:
You can split them into two consecutive subsequences :
1, 2, 3, 4, 5
3, 4, 5
Example 3:

Input: [1,2,3,4,4,5]
Output: False


Constraints:

1 <= nums.length <= 10000

659. 分割数组为连续子序列
给你一个按升序排序的整数数组 num（可能包含重复数字），请你将它们分割成一个或多个子序列，其中每个子序列都由连续整数组成且长度至少为 3 。

如果可以完成上述分割，则返回 true ；否则，返回 false 。



示例 1：

输入: [1,2,3,3,4,5]
输出: True
解释:
你可以分割出这样两个连续子序列 :
1, 2, 3
3, 4, 5


示例 2：

输入: [1,2,3,3,4,4,5,5]
输出: True
解释:
你可以分割出这样两个连续子序列 :
1, 2, 3, 4, 5
3, 4, 5


示例 3：

输入: [1,2,3,4,4,5]
输出: False


提示：

输入的数组长度范围为 [1, 10000]
'''


import heapq
import collections
class Solution(object):
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        mp = collections.defaultdict(list)
        for x in nums:
            queue = mp.get(x - 1)
            if queue:
                prevLength = heapq.heappop(queue)
                heapq.heappush(mp[x], prevLength + 1)
            else:
                heapq.heappush(mp[x], 1)
        # print queue, mp
        return not any(queue and queue[0] < 3 for queue in mp.values())

