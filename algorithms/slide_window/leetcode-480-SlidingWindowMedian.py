# encoding=utf8

'''
480. Sliding Window Median
Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

Examples:
[2,3,4] , the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Your job is to output the median array for each window in the original array.

For example,
Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.

Window position                Median
---------------               -----
[1  3  -1] -3  5  3  6  7       1
 1 [3  -1  -3] 5  3  6  7       -1
 1  3 [-1  -3  5] 3  6  7       -1
 1  3  -1 [-3  5  3] 6  7       3
 1  3  -1  -3 [5  3  6] 7       5
 1  3  -1  -3  5 [3  6  7]      6
Therefore, return the median sliding window as [1,-1,-1,3,5,6].

Note:
You may assume k is always valid, ie: k is always smaller than input array's size for non-empty array.
Answers within 10^-5 of the actual value will be accepted as correct.


480. 滑动窗口中位数
中位数是有序序列最中间的那个数。如果序列的大小是偶数，则没有最中间的数；此时中位数是最中间的两个数的平均数。

例如：

[2,3,4]，中位数是 3
[2,3]，中位数是 (2 + 3) / 2 = 2.5
给你一个数组 nums，有一个大小为 k 的窗口从最左端滑动到最右端。窗口中有 k 个数，每次窗口向右移动 1 位。你的任务是找出每次窗口移动后得到的新窗口中元素的中位数，并输出由它们组成的数组。



示例：

给出 nums = [1,3,-1,-3,5,3,6,7]，以及 k = 3。

窗口位置                      中位数
---------------               -----
[1  3  -1] -3  5  3  6  7       1
 1 [3  -1  -3] 5  3  6  7      -1
 1  3 [-1  -3  5] 3  6  7      -1
 1  3  -1 [-3  5  3] 6  7       3
 1  3  -1  -3 [5  3  6] 7       5
 1  3  -1  -3  5 [3  6  7]      6
 因此，返回该滑动窗口的中位数数组 [1,-1,-1,3,5,6]。



提示：

你可以假设 k 始终有效，即：k 始终小于输入的非空数组的元素个数。
与真实值误差在 10 ^ -5 以内的答案将被视作正确答案。
'''


class Solution(object):
    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        return [sorted(nums[i:i+k])[k//2] for i in range(len(nums)-k+1)] if k%2 else [(sorted(nums[i:i+k])[k//2]+sorted(nums[i:i+k])[(k-1)//2])/2.0 for i in range(len(nums)-k+1)]


# tips

'''
The simplest of solutions comes from the basic idea of finding the median given a set of numbers. We know that by definition, a median is the center element (or an average of the two center elements). Given an unsorted list of numbers, how do we find the median element? If you know the answer to this question, can we extend this idea to every sliding window that we come across in the array?

Is there a better way to do what we are doing in the above hint? Don't you think there is duplication of calculation being done there? Is there some sort of optimization that we can do to achieve the same result? This approach is merely a modification of the basic approach except that it simply reduces duplication of calculations once done.

The third line of thought is also based on this same idea but achieving the result in a different way. We obviously need the window to be sorted for us to be able to find the median. Is there a data-structure out there that we can use (in one or more quantities) to obtain the median element extremely fast, say O(1) time while having the ability to perform the other operations fairly efficiently as well?
'''


'''
前言
本题和 295. 数据流的中位数 非常相似。
求a的中位数的思路与代码如下：

python3思路

a[len(a)//2] if len(a)%2 else (a[len(a)//2-1] + a[len(a)//2]) / 2
解法一：数组+暴力法
思路
这个办法不难想到，就是将每一组的中位数加入返回结果res，再返回。

执行结果
第一种
执行用时：4992 ms, 在所有 Python3 提交中击败了25.46%的用户
内存消耗：16.1 MB, 在所有 Python3 提交中击败了42.07%的用户

第二种
执行用时：7248 ms, 在所有 Python3 提交中击败了5.09%的用户
内存消耗：16.4 MB, 在所有 Python3 提交中击败了14.02%的用户

代码
python3python3

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        median = lambda a: a[len(a)//2] if len(a)%2 else (a[len(a)//2-1] + a[len(a)//2]) / 2
        res = []
        for i in range(len(nums)-k+1):
            res.append(median(sorted(nums[i:i+k])))
        return res
时间复杂度
时间复杂度：O(n k log k)O(nklogk)，排序的时间复杂度为O(k log k)O(klogk)，总共执行了nn次。

解法二：数组+二分查找
思路
维护一个数组a，它保存当前数组，最开始等于排好序的nums的前k个元素。注意：a是排好序的。
用res保存返回结果，首先将a加入。
用i, j循环nums，它们分别表示删除值和加入值，每一对i, j都要执行下面步骤：
将a中值为i的元素删除；
将j增加在合适的位置，使用二分查找库（bisect）；
得到中位数并增加到res的最后。
返回。
举例
输入：nums = [1, 3, -1, -3, 5], k = 2
步骤：

a = [1, 3]，res = [a的中位数] = [2]
a = [1, 3]，删除1，增加-1，a = [-1, 3]，res增加a的中位数 = 1，res = [2, 1]
a = [-1, 3]，删除3，增加-3，a = [-3, -1]，res增加a的中位数 = -2，res = [2, 1, -2]
a = [-3, -1]，删除-1，增加5，a = [-3, 5]，res增加a的中位数 = 1，res = [2, 1, -2, 1]
返回res
执行结果
执行用时：308 ms, 在所有 Python3 提交中击败了38.91%的用户
内存消耗：16.1 MB, 在所有 Python3 提交中击败了43.91%的用户

python3

import bisect

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        median = lambda a: a[len(a)//2] if len(a)%2 else (a[len(a)//2-1] + a[len(a)//2]) / 2
        a = sorted(nums[:k])
        res = [median(a)]
        for i, j in zip(nums[:-k], nums[k:]):
            a.remove(i)
            a.insert(bisect.bisect_left(a, j), j)
            res.append(median(a))
        return res
时间复杂度
时间复杂度：O(n^2)O(n 
2
 )

解法三：数组+二分查找（优化）
思路
和解法二思路一致，思路改变部分加粗了，思路如下：

维护一个数组a，它保存当前数组，最开始等于排好序的nums的前k个元素。注意：a是排好序的。
用res保存返回结果，首先将a加入。
用i, j循环nums，它们分别表示删除值和加入值，每一对i, j都要执行下面步骤：
将值为i的索引从a中删除，使用二分查找库（bisect）；
将j增加在合适的位置，使用二分查找库（bisect）；
得到中位数并增加到res的最后。
返回。
执行结果
执行用时：72 ms, 在所有 Python3 提交中击败了100.00%的用户
内存消耗：16.1 MB, 在所有 Python3 提交中击败了44.28%的用户

python3

import bisect

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        median = lambda a: a[len(a)//2] if len(a)%2 else (a[len(a)//2-1] + a[len(a)//2]) / 2
        a = sorted(nums[:k])
        res = [median(a)]
        for i, j in zip(nums[:-k], nums[k:]):
            a.pop(bisect.bisect_left(a, i))
            a.insert(bisect.bisect_left(a, j), j)
            res.append(median(a))
        return res
时间复杂度
时间复杂度：O(n^2)O(n 
2
 )



作者：ting-ting-28
链接：https://leetcode-cn.com/problems/sliding-window-median/solution/python3-chao-xiang-xi-duo-jie-fa-bao-li-ga02a/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''

