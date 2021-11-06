# encoding=utf8

'''
268. Missing Number
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1:

Input: [3,0,1]
Output: 2
Example 2:

Input: [9,6,4,2,3,5,7,0,1]
Output: 8
Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?

268. 缺失数字
给定一个包含 0, 1, 2, ..., n 中 n 个数的序列，找出 0 .. n 中没有出现在序列中的那个数。

示例 1:

输入: [3,0,1]
输出: 2
示例 2:

输入: [9,6,4,2,3,5,7,0,1]
输出: 8
说明:
你的算法应具有线性时间复杂度。你能否仅使用额外常数空间来实现?
'''


# 求和
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        return n * (n + 1) / 2 - sum(nums)

# 位运算，异或
class Solution2:
    def missingNumber(self, nums):
        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing

class Solution3(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import functools
        import operator
        return functools.reduce(operator.xor, nums+[i for i in range(len(nums)+1)])


class Solution4(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # return len(nums) *(len(nums)  + 1) / 2 - sum(nums)

        i = 0
        while i < len(nums):
            while i != nums[i] and nums[i] < len(nums):
                nums[nums[i]], nums[i] = nums[i], nums[nums[i]]

            i += 1


        # print(nums)

        for i in range(len(nums)):
            if i != nums[i]:
                return i
        return len(nums)

import operator
import functools

def missingNumber(self, nums):
    n = len(nums)
    return functools.reduce(operator.xor, nums) ^ [n, 1, n+1, 0][n % 4]

def missingNumber1(self, nums):
    return (set(range(len(nums)+1)) - set(nums)).pop()

if __name__ == '__main__':
    demo = Solution3()
    res = demo.missingNumber([1,2,3,4,5,6,8,0])
    print(res)

'''
方法一：排序
分析

如果数组是有序的，那么就很容易知道缺失的数字是哪个了。

算法

首先我们对数组进行排序，随后我们可以在常数时间内判断两种特殊情况：0 没有出现在数组的首位，以及 nn 没有出现在数组的末位。如果这两种特殊情况都不满足，那么缺失的数字一定在 0 和 nn 之间（不包括两者）。此时我们可以在线性时间内扫描这个数组，如果某一个数比它前面的那个数大了超过 1，那么这两个数之间的那个数即为缺失的数字。

JavaPython
class Solution:
    def missingNumber(self, nums):
        nums.sort()

        # Ensure that n is at the last index
        if nums[-1] != len(nums):
            return len(nums)
        # Ensure that 0 is at the first index
        elif nums[0] != 0:
            return 0

        # If we get here, then the missing number is on the range (0, n)
        for i in range(1, len(nums)):
            expected_num = nums[i-1] + 1
            if nums[i] != expected_num:
                return expected_num
复杂度分析

时间复杂度：O(n\log n)O(nlogn)。由于排序的时间复杂度为 O(n\log n)O(nlogn)，扫描数组的时间复杂度为 O(n)O(n)，因此总的时间复杂度为 O(n\log n)O(nlogn)。
空间复杂度：O(1)O(1) 或 O(n)O(n)。空间复杂度取决于使用的排序算法，根据排序算法是否进行原地排序（即不使用额外的数组进行临时存储），空间复杂度为 O(1)O(1) 或 O(n)O(n)。
方法二：哈希表
分析

我们可以直接查询每个数是否在数组中出现过来找出缺失的数字。如果使用哈希表，那么每一次查询操作都是常数时间的。

算法

我们将数组中的所有数插入到一个集合中，这样每次查询操作的时间复杂度都是 O(1)O(1) 的。

JavaPython
class Solution:
    def missingNumber(self, nums):
        num_set = set(nums)
        n = len(nums) + 1
        for number in range(n):
            if number not in num_set:
                return number
复杂度分析

时间复杂度：O(n)O(n)。集合的插入操作的时间复杂度都是 O(1)O(1)，一共插入了 nn 个数，时间复杂度为 O(n)O(n)。集合的查询操作的时间复杂度同样是 O(1)O(1)，最多查询 n+1n+1 次，时间复杂度为 O(n)O(n)。因此总的时间复杂度为 O(n)O(n)。
空间复杂度：O(n)O(n)。集合中会存储 nn 个数，因此空间复杂度为 O(n)O(n)。
方法三：位运算
分析

由于异或运算（XOR）满足结合律，并且对一个数进行两次完全相同的异或运算会得到原来的数，因此我们可以通过异或运算找到缺失的数字。

算法

我们知道数组中有 nn 个数，并且缺失的数在 [0..n][0..n] 中。因此我们可以先得到 [0..n][0..n] 的异或值，再将结果对数组中的每一个数进行一次异或运算。未缺失的数在 [0..n][0..n] 和数组中各出现一次，因此异或后得到 0。而缺失的数字只在 [0..n][0..n] 中出现了一次，在数组中没有出现，因此最终的异或结果即为这个缺失的数字。

在编写代码时，由于 [0..n][0..n] 恰好是这个数组的下标加上 nn，因此可以用一次循环完成所有的异或运算，例如下面这个例子：

下标	0	1	2	3
数字	0	1	3	4
可以将结果的初始值设为 nn，再对数组中的每一个数以及它的下标进行一个异或运算，即：

\begin{aligned} \mathrm{missing} &= 4 \wedge (0 \wedge 0) \wedge (1 \wedge 1) \wedge (2 \wedge 3) \wedge (3 \wedge 4) \\ &= (4 \wedge 4) \wedge (0 \wedge 0) \wedge (1 \wedge 1) \wedge (3 \wedge 3) \wedge 2 \\ &= 0 \wedge 0 \wedge 0 \wedge 0 \wedge 2 \\ &= 2 \end{aligned}
missing
​	
  
=4∧(0∧0)∧(1∧1)∧(2∧3)∧(3∧4)
=(4∧4)∧(0∧0)∧(1∧1)∧(3∧3)∧2
=0∧0∧0∧0∧2
=2
​	
 

就得到了缺失的数字为 2。

JavaPython
class Solution:
    def missingNumber(self, nums):
        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing
复杂度分析

时间复杂度：O(n)O(n)。这里假设异或运算的时间复杂度是常数的，总共会进行 O(n)O(n) 次异或运算，因此总的时间复杂度为 O(n)O(n)。
空间复杂度：O(1)O(1)。算法中只用到了 O(1)O(1) 的额外空间，用来存储答案。
方法四：数学
分析

我们可以用 高斯求和公式 求出 [0..n][0..n] 的和，减去数组中所有数的和，就得到了缺失的数字。高斯求和公式即

\sum_{i=0}^{n}i = \frac{n(n+1)}{2}
i=0
∑
n
​	
 i= 
2
n(n+1)
​	
 

算法

我们在线性时间内可以求出数组中所有数的和，并在常数时间内求出前 n+1n+1 个自然数（包括 0）的和，将后者减去前者，就得到了缺失的数字。

JavaPython
class Solution:
    def missingNumber(self, nums):
        expected_sum = len(nums)*(len(nums)+1)//2
        actual_sum = sum(nums)
        return expected_sum - actual_sum
复杂度分析

时间复杂度：O(n)O(n)。求出数组中所有数的和的时间复杂度为 O(n)O(n)，高斯求和公式的时间复杂度为 O(1)O(1)，因此总的时间复杂度为 O(n)O(n)。
空间复杂度：O(1)O(1)。算法中只用到了 O(1)O(1) 的额外空间，用来存储答案。

'''
