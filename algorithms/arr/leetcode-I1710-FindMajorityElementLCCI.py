
'''
面试题 17.10. 主要元素
如果数组中多一半的数都是同一个，则称之为主要元素。给定一个整数数组，找到它的主要元素。若没有，返回-1。

示例 1：

输入：[1,2,5,9,5,9,5,5,5]
输出：5
 

示例 2：

输入：[3,2]
输出：-1
 

示例 3：

输入：[2,2,1,1,1,2,2]
输出：2

面试题 17.10. Find Majority Element LCCI
A majority element is an element that makes up more than half of the items in an array. Given a positive integers array, find the majority element. If there is no majority element, return -1. Do this in O(N) time and O(1) space.

Example 1:

Input: [1,2,5,9,5,9,5,5,5]
Output: 5
 

Example 2:

Input: [3,2]
Output: -1
 

Example 3:

Input: [2,2,1,1,1,2,2]
Output: 2
'''







class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sorted(nums)[len(nums)/2]


'''

解法一
摩尔投票法（Boyer–Moore majority vote algorithm），也被称作「多数投票法」，算法解决的问题是：如何在任意多的候选人中（选票无序），选出获得票数最多的那个。

算法可以分为两个阶段：

对抗阶段：分属两个候选人的票数进行两两对抗抵消
计数阶段：计算对抗结果中最后留下的候选人票数是否有效

解法二 位运算
构造ans使得它是主要元素。
由于主要元素是数组中多一半的数，那么这个主要元素的每位二进制也是数组每个元素二进制数中多一半的数
统计每位数字的第i位二进制，假如第i位为1比较多，那么将ans的第i位置为1，否则为0

'''
