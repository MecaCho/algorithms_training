# encoding=utf8

'''
260. Single Number III
Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.

Example:

Input:  [1,2,1,3,2,5]
Output: [3,5]
Note:

The order of the result is not important. So in the above example, [5, 3] is also correct.
Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?

260. 只出现一次的数字 III
给定一个整数数组 nums，其中恰好有两个元素只出现一次，其余所有元素均出现两次。 找出只出现一次的那两个元素。

示例 :

输入: [1,2,1,3,2,5]
输出: [3,5]
注意：

结果输出的顺序并不重要，对于上面的例子， [5, 3] 也是正确答案。
你的算法应该具有线性时间复杂度。你能否仅使用常数空间复杂度来实现？
'''

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        xors = 0
        for i in range(len(nums)):
            xors ^= nums[i]
        div = 1
        while div & xors == 0:
            div <<=1
        a, b = 0, 0
        for i in range(len(nums)):
            if nums[i] & div:
                a ^= nums[i]
            else:
                b ^= nums[i]
        return [a, b]
    
# golang solution

'''
func singleNumber(nums []int) []int {
	xors := 0
	for i := 0; i < len(nums); i++ {
		xors ^= nums[i]
	}
	div := 1
	for div&xors == 0 {
		div <<= 1

	}
	a, b := 0, 0
	for i := 0; i < len(nums); i++ {
		if nums[i]&div != 0 {
			a ^= nums[i]
		} else {
			b ^= nums[i]
		}
	}
	return []int{a, b}
}
'''

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        return [num for num, v in freq.items() if v == 1]
        

'''
概述
使用哈希表可以在 \mathcal{O}(N)O(N) 的时间复杂度和 \mathcal{O}(N)O(N) 的空间复杂度中解决该问题。

这个问题在常数的空间复杂度中解决有点困难，但可以借助两个位掩码来实现。



方法一：哈希表
建立一个值到频率的映射关系的哈希表，返回频率为 1 的数字。

算法：

PythonJava
from collections import Counter
class Solution:
    def singleNumber(self, nums: int) -> List[int]:
        hashmap = Counter(nums)
        return [x for x in hashmap if hashmap[x] == 1]
复杂度分析

时间复杂度：\mathcal{O}(N)O(N)。
空间复杂度：\mathcal{O}(N)O(N)，哈希表所使用的空间。
方法二：两个掩码
本文将使用两个按位技巧：

使用异或运算可以帮助我们消除出现两次的数字；我们计算 bitmask ^= x，则 bitmask 留下的就是出现奇数次的位。


x & (-x) 是保留位中最右边 1 ，且将其余的 1 设位 0 的方法。


算法：

首先计算 bitmask ^= x，则 bitmask 不会保留出现两次数字的值，因为相同数字的异或值为 0。

但是 bitmask 会保留只出现一次的两个数字（x 和 y）之间的差异。



我们可以直接从 bitmask 中提取 x 和 y 吗？不能，但是我们可以用 bitmask 作为标记来分离 x 和 y。

我们通过 bitmask & (-bitmask) 保留 bitmask 最右边的 1，这个 1 要么来自 x，要么来自 y。


当我们找到了 x，那么 y = bitmask^x。

PythonJava
class Solution:
    def singleNumber(self, nums: int) -> List[int]:
        # difference between two numbers (x and y) which were seen only once
        bitmask = 0
        for num in nums:
            bitmask ^= num
        
        # rightmost 1-bit diff between x and y
        diff = bitmask & (-bitmask)
        
        x = 0
        for num in nums:
            # bitmask which will contain only x
            if num & diff:
                x ^= num
        
        return [x, bitmask^x]
复杂度分析

时间复杂度：\mathcal{O}(N)O(N) 的时间遍历输入数组。
空间复杂度：\mathcal{O}(1)O(1)。

'''
