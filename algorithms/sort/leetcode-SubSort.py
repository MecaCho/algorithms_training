'''
面试题 16.16. Sub Sort LCCI
Given an array of integers, write a method to find indices m and n such that if you sorted elements m through n, the entire array would be sorted. Minimize n - m (that is, find the smallest such sequence).

Return [m,n]. If there are no such m and n (e.g. the array is already sorted), return [-1, -1].

Example:

Input:  [1,2,4,7,10,11,7,12,6,7,16,18,19]
Output:  [3,9]
Note:

0 <= len(array) <= 1000000


面试题 16.16. 部分排序
给定一个整数数组，编写一个函数，找出索引m和n，只要将索引区间[m,n]的元素排好序，整个数组就是有序的。注意：n-m尽量最小，也就是说，找出符合条件的最短序列。函数返回值为[m,n]，若不存在这样的m和n（例如整个数组是有序的），请返回[-1,-1]。

示例：

输入： [1,2,4,7,10,11,7,12,6,7,16,18,19]
输出： [3,9]
提示：

0 <= len(array) <= 1000000
'''



class Solution(object):
    def subSort(self, array):
        """
        :type array: List[int]
        :rtype: List[int]
        """
        array_ = sorted(array)
        l, r = -1, -1
        i, j = 0, len(array) - 1
        while i < len(array):
            if array[i] != array_[i]:
                l = i
                break
            i += 1
        while j > 0:
            if array[j] != array_[j]:
                r = j
                break
            j -= 1
        return [l, r]


# tips

'''
在开始和结束时知道最长的排序序列会有帮助吗？

我们可以把这个数组分成3个子数组：LEFT、MIDDLE和RIGHT。LEFT和RIGHT都是有序的。MIDDLE的元素顺序是任意的。我们需要展开MIDDLE，直到可以对这些元素排序并使整个数组有序。

考虑3个子数组：LEFT、MIDDLE和RIGHT。只关注这个问题：是否可以排序MIDDLE以使整个数组有序？如何进行验证？

为了能够对MIDDLE进行排序并对整个数组进行排序，需要MAX(LEFT) <= MIN(MIDDLE, RIGHT)和MAX(LEFT, MIDDLE) <= MIN(RIGHT)。

你能把中间部分展开直到满足前面的条件吗？

你应该能在O(N)时间内解出来。
'''
