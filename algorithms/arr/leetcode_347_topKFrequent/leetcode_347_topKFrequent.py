'''

347. Top K Frequent Elements
Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
Note:

You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
It's guaranteed that the answer is unique, in other words the set of the top k frequent elements is unique.
You can return the answer in any order.


347. 前 K 个高频元素
给定一个非空的整数数组，返回其中出现频率前 k 高的元素。



示例 1:

输入: nums = [1,1,1,2,2,3], k = 2
输出: [1,2]
示例 2:

输入: nums = [1], k = 1
输出: [1]


提示：

你可以假设给定的 k 总是合理的，且 1 ≤ k ≤ 数组中不相同的元素的个数。
你的算法的时间复杂度必须优于 O(n log n) , n 是数组的大小。
题目数据保证答案唯一，换句话说，数组中前 k 个高频元素的集合是唯一的。
你可以按任意顺序返回答案。
'''


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        sum_dict = dict()
        for num in nums:
            if num in sum_dict:
                sum_dict[num] += 1
            else:
                sum_dict[num] = 1
        ret = []
        for key in sorted(sum_dict, key=sum_dict.__getitem__, reverse=True):
            if k > 0:
                ret.append(key)
                k -= 1
            else:
                break
        return ret


import collections


class Solution2(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counter = collections.Counter(nums)
        return [key for key, _ in counter.most_common(k)]


if __name__ == '__main__':
    test_list = [1, 1, 1, 2, 2, 3, 4, 5, 6, 9, 10]
    demo = Solution()

    print(demo.topKFrequent(test_list, 10))

    demo1 = Solution2()

    print(demo1.topKFrequent(test_list, 10))
