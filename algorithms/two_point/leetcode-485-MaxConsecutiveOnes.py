# encoding=utf8


'''
485. 最大连续1的个数
给定一个二进制数组， 计算其中最大连续1的个数。

示例 1:

输入: [1,1,0,1,1,1]
输出: 3
解释: 开头的两位和最后的三位都是连续1，所以最大连续1的个数是 3.
注意：

输入的数组只包含 0 和1。
输入数组的长度是正整数，且不超过 10,000。

485. Max Consecutive Ones
Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000
'''

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i, j = -1, 0
        max_length = 0
        while j < len(nums):
            if nums[j] == 1:
                max_length = max(max_length, j-i)
            else:
                i = j
            j += 1
        return max_length



class Solution20210215(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        return max(len(substr) for substr in ''.join([str(x) for x in nums]).split("0"))


# tips

'''
You need to think about two things as far as any window is concerned. One is the starting point for the window. How do you detect that a new window of 1s has started? The next part is detecting the ending point for this window. How do you detect the ending point for an existing window? If you figure these two things out, you will be able to detect the windows of consecutive ones. All that remains afterward is to find the longest such window and return the size.
'''

# solutions

'''
方法一：一次遍历
题目的约束让这个问题变得简单，使得我们可以在一次遍历解决它。

算法：

用一个计数器 count 记录 1 的数量，另一个计数器 maxCount 记录当前最大的 1 的数量。
当我们遇到 1 时，count 加一。
当我们遇到 0 时：
将 count 与 maxCount 比较，maxCoiunt 记录较大值。
将 count 设为 0。
返回 maxCount。
JavaPython

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = max_count = 0
        for num in nums:
            if num == 1:
                # Increment the count of 1's by one.
                count += 1
            else:
                # Find the maximum till now.
                max_count = max(max_count, count)
                # Reset count of 1.
                count = 0
        return max(max_count, count)
复杂度分析

时间复杂度：O(N)O(N)。NN 值得是数组的长度。
空间复杂度：O(1)O(1)，仅仅使用了 count 和 maxCount。
方法二：
在 Python 中可以使用 map 和 join 来解决此问题。
使用 splits 函数在 0 处分割将数组转换成字符串。
在获取子串的最大长度就是最大连续 1 的长度。
Python

def findMaxConsecutiveOnes(self, nums):
  return max(map(len, ''.join(map(str, nums)).split('0')))

作者：LeetCode
链接：https://leetcode-cn.com/problems/max-consecutive-ones/solution/zui-da-lian-xu-1de-ge-shu-by-leetcode/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''

