# encoding=utf8

'''
414. Third Maximum Number
Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.

 

Example 1:

Input: nums = [3,2,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2.
The third distinct maximum is 1.
Example 2:

Input: nums = [1,2]
Output: 2
Explanation:
The first distinct maximum is 2.
The second distinct maximum is 1.
The third distinct maximum does not exist, so the maximum (2) is returned instead.
Example 3:

Input: nums = [2,2,3,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2 (both 2's are counted together since they have the same value).
The third distinct maximum is 1.
 

Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
 

Follow up: Can you find an O(n) solution?

414. 第三大的数
给你一个非空数组，返回此数组中 第三大的数 。如果不存在，则返回数组中最大的数。

 

示例 1：

输入：[3, 2, 1]
输出：1
解释：第三大的数是 1 。
示例 2：

输入：[1, 2]
输出：2
解释：第三大的数不存在, 所以返回最大的数 2 。
示例 3：

输入：[2, 2, 3, 1]
输出：1
解释：注意，要求返回第三大的数，是指在所有不同数字中排第三大的数。
此例中存在两个值为 2 的数，它们都排第二。在所有不同数字中排第三大的数为 1 。
 

提示：

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
 

进阶：你能设计一个时间复杂度 O(n) 的解决方案吗？
'''

class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sorted(set(nums), reverse=True)[2] if len(set(nums)) >= 3 else sorted(nums, reverse=True)[0]


class Solution1(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_third = [float("-inf")]*3

        for num in nums:
            if num in min_third:
                continue
            if num > min_third[0]:
                min_third = [num, min_third[0], min_third[1]]
            elif num > min_third[1]:
                min_third = [min_third[0], num, min_third[1]]
            elif num > min_third[2]:
                min_third[2] = num
        return min_third[2] if len(set(nums)) >= 3 else min_third[0]


if __name__ == '__main__':
    demo = Solution()
    print demo.thirdMax([3, 9, 100])

    demo = Solution1()
    print demo.thirdMax([3, 100, 10, 99])
    
    
# solutions

'''
方法一：排序
将数组从大到小排序后，从头开始遍历数组，通过判断相邻元素是否不同，来统计不同元素的个数。如果能找到三个不同的元素，就返回第三大的元素，否则返回最大的元素。

Python3C++JavaC#GolangJavaScript

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        diff = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                diff += 1
                if diff == 3:  # 此时 nums[i] 就是第三大的数
                    return nums[i]
        return nums[0]
复杂度分析

时间复杂度：O(n\log n)O(nlogn)，其中 nn 是数组 \textit{nums}nums 的长度。排序需要 O(n\log n)O(nlogn) 的时间。

空间复杂度：O(\log n)O(logn)。排序需要的栈空间为 O(\log n)O(logn)。

方法二：有序集合
我们可以遍历数组，同时用一个有序集合来维护数组中前三大的数。具体做法是每遍历一个数，就将其插入有序集合，若有序集合的大小超过 33，就删除集合中的最小元素。这样可以保证有序集合的大小至多为 33，且遍历结束后，若有序集合的大小为 33，其最小值就是数组中第三大的数；若有序集合的大小不足 33，那么就返回有序集合中的最大值。

Python3C++JavaC#Golang

from sortedcontainers import SortedList

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        s = SortedList()
        for num in nums:
            if num not in s:
                s.add(num)
                if len(s) > 3:
                    s.pop(0)
        return s[0] if len(s) == 3 else s[-1]
复杂度分析

时间复杂度：O(n)O(n)，其中 nn 是数组 \textit{nums}nums 的长度。由于有序集合的大小至多为 33，插入和删除的时间复杂度可以视作是 O(1)O(1) 的，因此时间复杂度为 O(n)O(n)。

空间复杂度：O(1)O(1)。

方法三：一次遍历
我们可以遍历数组，并用三个变量 aa、bb 和 cc 来维护数组中的最大值、次大值和第三大值，以模拟方法二中的插入和删除操作。为方便编程实现，我们将其均初始化为小于数组最小值的元素，视作「无穷小」，比如 -2^{63}−2 
63
  等。

遍历数组，对于数组中的元素 \textit{num}num：

若 \textit{num}>anum>a，我们将 cc 替换为 bb，bb 替换为 aa，aa 替换为 \textit{num}num，这模拟了将 \textit{num}num 插入有序集合，并删除有序集合中的最小值的过程；
若 a>\textit{num}>ba>num>b，类似地，我们将 cc 替换为 bb，bb 替换为 \textit{num}num，aa 保持不变；
若 b>\textit{num}>cb>num>c，类似地，我们将 cc 替换为 \textit{num}num，aa 和 bb 保持不变；
其余情况不做处理。
遍历结束后，若 cc 仍然为 -2^{63}−2 
63
 ，则说明数组中不存在三个或三个以上的不同元素，即第三大的数不存在，返回 aa，否则返回 cc。

Python3C++JavaC#GolangJavaScript

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        a, b, c = float('-inf'), float('-inf'), float('-inf')
        for num in nums:
            if num > a:
                a, b, c = num, a, b
            elif a > num > b:
                b, c = num, b
            elif b > num > c:
                c = num
        return a if c == float('-inf') else c
另一种不依赖元素范围的做法是，将 aa、bb 和 cc 初始化为空指针或空对象，视作「无穷小」，并在比较大小前先判断是否为空指针或空对象。遍历结束后，若 cc 为空，则说明第三大的数不存在，返回 aa，否则返回 cc。

Python3C++JavaC#GolangJavaScript

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        a, b, c = None, None, None
        for num in nums:
            if a is None or num > a:
                a, b, c = num, a, b
            elif a > num and (b is None or num > b):
                b, c = num, b
            elif b is not None and b > num and (c is None or num > c):
                c = num
        return a if c is None else c
复杂度分析

时间复杂度：O(n)O(n)，其中 nn 是数组 \textit{nums}nums 的长度。

空间复杂度：O(1)O(1)。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/third-maximum-number/solution/di-san-da-de-shu-by-leetcode-solution-h3sp/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
