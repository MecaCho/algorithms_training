# encoding=utf8

'''
611. Valid Triangle Number
Given an integer array nums, return the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.

 

Example 1:

Input: nums = [2,2,3,4]
Output: 3
Explanation: Valid combinations are: 
2,3,4 (using the first 2)
2,3,4 (using the second 2)
2,2,3
Example 2:

Input: nums = [4,2,3,4]
Output: 4
 

Constraints:

1 <= nums.length <= 1000
0 <= nums[i] <= 1000

611. 有效三角形的个数
给定一个包含非负整数的数组，你的任务是统计其中可以组成三角形三条边的三元组个数。

示例 1:

输入: [2,2,3,4]
输出: 3
解释:
有效的组合是: 
2,3,4 (使用第一个 2)
2,3,4 (使用第二个 2)
2,2,3
注意:

数组长度不超过1000。
数组里整数的范围为 [0, 1000]。
'''


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        res = 0
        for i in range(n):
            k = i
            for j in range(i+1, n):
                # k = j
                while k + 1 < n and nums[k+1] < nums[i] + nums[j]:
                    k += 1

                res += max(k-j, 0)

        return res
      
 # solutions
 
 '''
 方法一：排序 + 二分查找
思路与算法

对于正整数 a, b, ca,b,c，它们可以作为三角形的三条边，当且仅当：

\begin{cases} a + b > c \\ a + c > b \\ b + c > a \end{cases}
  
a+b>c
a+c>b
b+c>a
​
 

均成立。如果我们将三条边进行升序排序，使它们满足 a \leq b \leq ca≤b≤c，那么 a + c > ba+c>b 和 b + c > ab+c>a 使一定成立的，我们只需要保证 a + b > ca+b>c。

因此，我们可以将数组 \textit{nums}nums 进行升序排序，随后使用二重循环枚举 aa 和 bb。设 a = \textit{nums}[i], b = \textit{nums}[j]a=nums[i],b=nums[j]，为了防止重复统计答案，我们需要保证 i < ji<j。剩余的边 cc 需要满足 c < \textit{nums}[i] + \textit{nums}[j]c<nums[i]+nums[j]，我们可以在 [j + 1, n - 1][j+1,n−1] 的下标范围内使用二分查找（其中 nn 是数组 \textit{nums}nums 的长度），找出最大的满足 \textit{nums}[k] < \textit{nums}[i] + \textit{nums}[j]nums[k]<nums[i]+nums[j] 的下标 kk，这样一来，在 [j + 1, k][j+1,k] 范围内的下标都可以作为边 cc 的下标，我们将该范围的长度 k - jk−j 累加入答案。

当枚举完成后，我们返回累加的答案即可。

细节

注意到题目描述中 \textit{nums}nums 包含的元素为非负整数，即除了正整数以外，\textit{nums}nums 还会包含 00。但如果我们将 \textit{nums}nums 进行升序排序，那么在枚举 aa 和 bb 时出现了 00，那么 \textit{nums}[i]nums[i] 一定为 00。此时，边 cc 需要满足 c < \textit{nums}[i] + \textit{nums}[j] = \textit{nums}[j]c<nums[i]+nums[j]=nums[j]，而下标在 [j + 1, n - 1][j+1,n−1] 范围内的元素一定都是大于等于 \textit{nums}[j]nums[j] 的，因此二分查找会失败。若二分查找失败，我们可以令 k = jk=j，此时对应的范围长度 k - j = 0k−j=0，我们也就保证了答案的正确性。

代码

C++JavaC#Python3JavaScriptGolangC

func triangleNumber(nums []int) (ans int) {
    sort.Ints(nums)
    for i, v := range nums {
        for j := i + 1; j < len(nums); j++ {
            ans += sort.SearchInts(nums[j+1:], v+nums[j])
        }
    }
    return
}
复杂度分析

时间复杂度：O(n^2 \log n)O(n 
2
 logn)，其中 nn 是数组 \textit{nums}nums 的长度。我们需要 O(n \log n)O(nlogn) 的时间对数组 \textit{nums}nums 进行排序，随后需要 O(n^2 \log n)O(n 
2
 logn) 的时间使用二重循环枚举 a, ba,b 的下标以及使用二分查找得到 cc 的下标范围。

空间复杂度：O(\log n)O(logn)，即为排序需要的栈空间。

方法二：排序 + 双指针
思路与算法

我们可以对方法一进行优化。

我们将当 a = \textit{nums}[i], b = \textit{nums}[j]a=nums[i],b=nums[j] 时，最大的满足 \textit{nums}[k] < \textit{nums}[i] + \textit{nums}[j]nums[k]<nums[i]+nums[j] 的下标 kk 记为 k_{i, j}k 
i,j
​
 。可以发现，如果我们固定 ii，那么随着 jj 的递增，不等式右侧 \textit{nums}[i] + \textit{nums}[j]nums[i]+nums[j] 也是递增的，因此 k_{i, j}k 
i,j
​
  也是递增的。

这样一来，我们就可以将 jj 和 kk 看成两个同向（递增）移动的指针，将方法一进行如下的优化：

我们使用一重循环枚举 ii。当 ii 固定时，我们使用双指针同时维护 jj 和 kk，它们的初始值均为 ii；

我们每一次将 jj 向右移动一个位置，即 j \leftarrow j+1j←j+1，并尝试不断向右移动 kk，使得 kk 是最大的满足 \textit{nums}[k] < \textit{nums}[i] + \textit{nums}[j]nums[k]<nums[i]+nums[j] 的下标。我们将 \max(k - j, 0)max(k−j,0) 累加入答案。

当枚举完成后，我们返回累加的答案即可。

细节

与方法一中「二分查找的失败」类似，方法二的双指针中，也会出现不存在满足 \textit{nums}[k] < \textit{nums}[i] + \textit{nums}[j]nums[k]<nums[i]+nums[j] 的下标的情况。此时，指针 kk 不会出现在指针 jj 的右侧，即 k - j \leq 0k−j≤0，因此我们需要将 k - jk−j 与 00 中的较大值累加入答案，防止错误的负数出现。

代码

C++JavaC#Python3JavaScriptGolangC

func triangleNumber(nums []int) (ans int) {
    n := len(nums)
    sort.Ints(nums)
    for i, v := range nums {
        k := i
        for j := i + 1; j < n; j++ {
            for k+1 < n && nums[k+1] < v+nums[j] {
                k++
            }
            ans += max(k-j, 0)
        }
    }
    return
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}
复杂度分析

时间复杂度：O(n^2)O(n 
2
 )，其中 nn 是数组 \textit{nums}nums 的长度。我们需要 O(n \log n)O(nlogn) 的时间对数组 \textit{nums}nums 进行排序，随后需要 O(n^2)O(n 
2
 ) 的时间使用一重循环枚举 aa 的下标以及使用双指针维护 b, cb,c 的下标。

空间复杂度：O(\log n)O(logn)，即为排序需要的栈空间。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/valid-triangle-number/solution/you-xiao-san-jiao-xing-de-ge-shu-by-leet-t2td/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
 '''
