# encoding=utf8

'''
303. Range Sum Query - Immutable
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Implement the NumArray class:

NumArray(int[] nums) Initializes the object with the integer array nums.
int sumRange(int i, int j) Return the sum of the elements of the nums array in the range [i, j] inclusive (i.e., sum(nums[i], nums[i + 1], ... , nums[j]))


Example 1:

Input
["NumArray", "sumRange", "sumRange", "sumRange"]
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
Output
[null, 1, -1, -3]

Explanation
NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
numArray.sumRange(0, 2); // return 1 ((-2) + 0 + 3)
numArray.sumRange(2, 5); // return -1 (3 + (-5) + 2 + (-1))
numArray.sumRange(0, 5); // return -3 ((-2) + 0 + 3 + (-5) + 2 + (-1))


Constraints:

0 <= nums.length <= 104
-105 <= nums[i] <= 105
0 <= i <= j < nums.length
At most 104 calls will be made to sumRange.



303. 区域和检索 - 数组不可变
给定一个整数数组  nums，求出数组从索引 i 到 j（i ≤ j）范围内元素的总和，包含 i、j 两点。

实现 NumArray 类：

NumArray(int[] nums) 使用数组 nums 初始化对象
int sumRange(int i, int j) 返回数组 nums 从索引 i 到 j（i ≤ j）范围内元素的总和，包含 i、j 两点（也就是 sum(nums[i], nums[i + 1], ... , nums[j])）


示例：

输入：
["NumArray", "sumRange", "sumRange", "sumRange"]
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
输出：
[null, 1, -1, -3]

解释：
NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
numArray.sumRange(0, 2); // return 1 ((-2) + 0 + 3)
numArray.sumRange(2, 5); // return -1 (3 + (-5) + 2 + (-1))
numArray.sumRange(0, 5); // return -3 ((-2) + 0 + 3 + (-5) + 2 + (-1))


提示：

0 <= nums.length <= 104
-105 <= nums[i] <= 105
0 <= i <= j < nums.length
最多调用 104 次 sumRange 方法
'''



class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums


    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return sum(self.nums[i:j+1])



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)


class NumArray2(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        # self.nums = nums
        self.sums = [0]
        for i in range(len(nums)):
            self.sums.append(self.sums[-1] + nums[i])


    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.sums[j+1] - self.sums[i]



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)


# solutions

'''
方法一：前缀和
最朴素的想法是存储数组 \textit{nums}nums 的值，每次调用 \text{sumRange}sumRange 时，通过循环的方法计算数组 \textit{nums}nums 从下标 ii 到下标 jj 范围内的元素和，需要计算 j-i+1j−i+1 个元素的和。由于每次检索的时间和检索的下标范围有关，因此检索的时间复杂度较高，如果检索次数较多，则会超出时间限制。

由于会进行多次检索，即多次调用 \text{sumRange}sumRange，因此为了降低检索的总时间，应该降低 \text{sumRange}sumRange 的时间复杂度，最理想的情况是时间复杂度 O(1)O(1)。为了将检索的时间复杂度降到 O(1)O(1)，需要在初始化的时候进行预处理。

注意到当 i \le ji≤j 时，\text{sumRange}(i,j)sumRange(i,j) 可以写成如下形式：

\begin{aligned} &\quad \ \text{sumRange}(i,j) \\ &=\sum\limits_{k=i}^j \textit{nums}[k] \\ &= \sum\limits_{k=0}^j \textit{nums}[k] - \sum\limits_{k=0}^{i-1} \textit{nums}[k] \end{aligned}
​	
  
 sumRange(i,j)
= 
k=i
∑
j
​	
 nums[k]
= 
k=0
∑
j
​	
 nums[k]− 
k=0
∑
i−1
​	
 nums[k]
​	
 

由此可知，要计算 \text{sumRange}(i,j)sumRange(i,j)，则需要计算数组 \textit{nums}nums 在下标 jj 和下标 i-1i−1 的前缀和，然后计算两个前缀和的差。

如果可以在初始化的时候计算出数组 \textit{nums}nums 在每个下标处的前缀和，即可满足每次调用 \text{sumRange}sumRange 的时间复杂度都是 O(1)O(1)。

具体实现方面，假设数组 \textit{nums}nums 的长度为 nn，创建长度为 n+1n+1 的前缀和数组 \textit{sums}sums，对于 0 \le i<n0≤i<n 都有 \textit{sums}[i+1]=\textit{sums}[i]+\textit{nums}[i]sums[i+1]=sums[i]+nums[i]，则当 0<i \le n0<i≤n 时，\textit{sums}[i]sums[i] 表示数组 \textit{nums}nums 从下标 00 到下标 i-1i−1 的前缀和。

将前缀和数组 \textit{sums}sums 的长度设为 n+1n+1 的目的是为了方便计算 \text{sumRange}(i,j)sumRange(i,j)，不需要对 i=0i=0 的情况特殊处理。此时有：

\text{sumRange}(i,j)=\textit{sums}[j+1]-\textit{sums}[i]
sumRange(i,j)=sums[j+1]−sums[i]

JavaJavaScriptGolangPython3C++C

type NumArray struct {
    sums []int
}

func Constructor(nums []int) NumArray {
    sums := make([]int, len(nums)+1)
    for i, v := range nums {
        sums[i+1] = sums[i] + v
    }
    return NumArray{sums}
}

func (na *NumArray) SumRange(i, j int) int {
    return na.sums[j+1] - na.sums[i]
}
复杂度分析

时间复杂度：初始化 O(n)O(n)，每次检索 O(1)O(1)，其中 nn 是数组 \textit{nums}nums 的长度。
初始化需要遍历数组 \textit{nums}nums 计算前缀和，时间复杂度是 O(n)O(n)。
每次检索只需要得到两个下标处的前缀和，然后计算差值，时间复杂度是 O(1)O(1)。

空间复杂度：O(n)O(n)，其中 nn 是数组 \textit{nums}nums 的长度。需要创建一个长度为 n+1n+1 的前缀和数组。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/range-sum-query-immutable/solution/qu-yu-he-jian-suo-shu-zu-bu-ke-bian-by-l-px41/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
