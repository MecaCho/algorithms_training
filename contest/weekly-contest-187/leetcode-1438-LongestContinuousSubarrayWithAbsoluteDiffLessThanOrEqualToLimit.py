


'''
1438. 绝对差不超过限制的最长连续子数组
给你一个整数数组 nums ，和一个表示限制的整数 limit，请你返回最长连续子数组的长度，该子数组中的任意两个元素之间的绝对差必须小于或者等于 limit 。

如果不存在满足条件的子数组，则返回 0 。



示例 1：

输入：nums = [8,2,4,7], limit = 4
输出：2
解释：所有子数组如下：
[8] 最大绝对差 |8-8| = 0 <= 4.
[8,2] 最大绝对差 |8-2| = 6 > 4.
[8,2,4] 最大绝对差 |8-2| = 6 > 4.
[8,2,4,7] 最大绝对差 |8-2| = 6 > 4.
[2] 最大绝对差 |2-2| = 0 <= 4.
[2,4] 最大绝对差 |2-4| = 2 <= 4.
[2,4,7] 最大绝对差 |2-7| = 5 > 4.
[4] 最大绝对差 |4-4| = 0 <= 4.
[4,7] 最大绝对差 |4-7| = 3 <= 4.
[7] 最大绝对差 |7-7| = 0 <= 4.
因此，满足题意的最长子数组的长度为 2 。
示例 2：

输入：nums = [10,1,2,4,7,2], limit = 5
输出：4
解释：满足题意的最长子数组是 [2,4,7,2]，其最大绝对差 |2-7| = 5 <= 5 。
示例 3：

输入：nums = [4,2,2,2,4,4,2,2], limit = 0
输出：3


提示：

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^9
0 <= limit <= 10^9


1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
Given an array of integers nums and an integer limit, return the size of the longest continuous subarray such that the absolute difference between any two elements is less than or equal to limit.

In case there is no subarray satisfying the given condition return 0.



Example 1:

Input: nums = [8,2,4,7], limit = 4
Output: 2
Explanation: All subarrays are:
[8] with maximum absolute diff |8-8| = 0 <= 4.
[8,2] with maximum absolute diff |8-2| = 6 > 4.
[8,2,4] with maximum absolute diff |8-2| = 6 > 4.
[8,2,4,7] with maximum absolute diff |8-2| = 6 > 4.
[2] with maximum absolute diff |2-2| = 0 <= 4.
[2,4] with maximum absolute diff |2-4| = 2 <= 4.
[2,4,7] with maximum absolute diff |2-7| = 5 > 4.
[4] with maximum absolute diff |4-4| = 0 <= 4.
[4,7] with maximum absolute diff |4-7| = 3 <= 4.
[7] with maximum absolute diff |7-7| = 0 <= 4.
Therefore, the size of the longest subarray is 2.
Example 2:

Input: nums = [10,1,2,4,7,2], limit = 5
Output: 4
Explanation: The subarray [2,4,7,2] is the longest since the maximum absolute diff is |2-7| = 5 <= 5.
Example 3:

Input: nums = [4,2,2,2,4,4,2,2], limit = 0
Output: 3


Constraints:

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^9
0 <= limit <= 10^9
'''


class Solution(object):
    def longestSubarray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        mins = []
        maxs = []
        cur = []
        max_length = 0
        # min_val = nums[0]
        # max_val = nums[0]
        for i in range(len(nums)):
            num = nums[i]
            cur.append(num)

            # if num < min_val:
            #     min_val = num
            # if num >= max_val:
            #     max_val = num

            if not mins or num <= mins[-1]:
                mins.append(num)
            if not maxs or num >= maxs[-1]:
                maxs.append(num)

            min_val = mins[-1]
            max_val = maxs[-1]

            # print(min_val, mins, max_val, maxs, cur, len(cur))
            if max_val - min_val > limit:
                pop_val = cur.pop(0)
                if pop_val == mins[0]:
                    mins.pop(0)
                    if not mins:
                        mins.append(cur[0])
                        i = 1
                        while i < len(cur):
                            if cur[i] <= mins[-1]:
                                mins.append(cur[i])
                            i += 1
                if pop_val == maxs[0]:
                    maxs.pop(0)
                    if not maxs:
                        maxs.append(cur[0])
                        i = 1
                        while i < len(cur):
                            if cur[i] >= maxs[-1]:
                                maxs.append(cur[i])
                            i += 1
            else:
                max_length = max(max_length, len(cur))
                # print(max_length, len(cur), max(cur), min(cur), cur)
        # print(len(nums), max(nums), min(nums))
        return max_length

# tips

'''
Use a sliding window approach keeping the maximum and minimum value using a data structure like a multiset from STL in C++.
'''

'''
More specifically, use the two pointer technique, moving the right pointer as far as possible to the right until the subarray is not valid (maxValue - minValue > limit), then moving the left pointer until the subarray is valid again (maxValue - minValue <= limit). Keep repeating this process.
'''

# solutions

'''
思路
使用滑动窗口保持符合条件的子数组，记录最长长度
怎样确定子数组是否符合条件，需要知道两个关键数据
21. 子数组中的最大值
22. 子数组中的最小值
需要对滑入窗口的数据记录，滑出的数据删除，并且使这些记录方便的算出最大值和最小值
31. 使用 map / multiset 可以在滑入滑出的时候方便的增减对应数据
32. 同时 map / multiset 本身是有序的，可以方便的找出最大值最小值
答题
C++C++
    int longestSubarray(vector<int>& nums, int limit) {
        map<int, int> m;
        int ans = 0;
        int i = 0;
        for (int j = 0; j < nums.size(); j++) {
            m[nums[j]]++;
            while (m.rbegin()->first - m.begin()->first > limit) {
                m[nums[i]]--;
                if (m[nums[i]] == 0) {
                    m.erase(nums[i]);
                }
                i++;
            }
            ans = max(ans, j - i + 1);
        }
        return ans;
    }

'''