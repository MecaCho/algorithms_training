# encoding=utf8

'''
581. Shortest Unsorted Continuous Subarray
Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.

You need to find the shortest such subarray and output its length.

Example 1:
Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
Note:
Then length of the input array is in range [1, 10,000].
The input array may contain duplicates, so ascending order here means <=.

581. 最短无序连续子数组
给定一个整数数组，你需要寻找一个连续的子数组，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。

你找到的子数组应是最短的，请输出它的长度。

示例 1:

输入: [2, 6, 4, 8, 10, 9, 15]
输出: 5
解释: 你只需要对 [6, 4, 8, 10, 9] 进行升序排序，那么整个表都会变为升序排序。
说明 :

输入的数组长度范围在 [1, 10,000]。
输入的数组可能包含重复元素 ，所以升序的意思是<=。
'''



class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # res = [i for i, (a, b) in enumerate(zip(sorted(nums), nums)) if a != b]
        # return res[-1] - res[0] + 1 if res else 0

        l, r = 0, -1
        max_num, min_num = -float("inf"), float("inf")
        length = len(nums)
        for i in range(length):
            if nums[i] < max_num:
                r = i
            else:
                max_num = nums[i]

            if nums[length-i-1] > min_num:
                l = length-i-1
            else:
                min_num = nums[length-i-1]
            # print(min_num, max_num)
        return r - l + 1

    
    
    
    
# solutions

'''
方法一：排序
思路与算法

我们将给定的数组 \textit{nums}nums 表示为三段子数组拼接的形式，分别记作 \textit{nums}_Anums 
A
​
 ，\textit{nums}_Bnums 
B
​
 ，\textit{nums}_Cnums 
C
​
 。当我们对 \textit{nums}_Bnums 
B
​
  进行排序，整个数组将变为有序。换而言之，当我们对整个序列进行排序，\textit{nums}_Anums 
A
​
  和 \textit{nums}_Cnums 
C
​
  都不会改变。

本题要求我们找到最短的 \textit{nums}_Bnums 
B
​
 ，即找到最大的 \textit{nums}_Anums 
A
​
  和 \textit{nums}_Cnums 
C
​
  的长度之和。因此我们将原数组 \textit{nums}nums 排序与原数组进行比较，取最长的相同的前缀为 \textit{nums}_Anums 
A
​
 ，取最长的相同的后缀为 \textit{nums}_Cnums 
C
​
 ，这样我们就可以取到最短的 \textit{nums}_Bnums 
B
​
 。

具体地，我们创建数组 \textit{nums}nums 的拷贝，记作数组 \textit{numsSorted}numsSorted，并对该数组进行排序，然后我们从左向右找到第一个两数组不同的位置，即为 \textit{nums}_Bnums 
B
​
  的左边界。同理也可以找到 \textit{nums}_Bnums 
B
​
  右边界。最后我们输出 \textit{nums}_Bnums 
B
​
  的长度即可。

特别地，当原数组有序时，\textit{nums}_Bnums 
B
​
  的长度为 00，我们可以直接返回结果。

代码

C++JavaC#Python3JavaScriptGolangC

func findUnsortedSubarray(nums []int) int {
    if sort.IntsAreSorted(nums) {
        return 0
    }
    numsSorted := append([]int(nil), nums...)
    sort.Ints(numsSorted)
    left, right := 0, len(nums)-1
    for nums[left] == numsSorted[left] {
        left++
    }
    for nums[right] == numsSorted[right] {
        right--
    }
    return right - left + 1
}
复杂度分析

时间复杂度：O(n \log n)O(nlogn)，其中 nn 为给定数组的长度。我们需要 O(n \log n)O(nlogn) 的时间进行排序，以及 O(n)O(n) 的时间遍历数组，因此总时间复杂度为 O(n)O(n)。

空间复杂度：O(n)O(n)，其中 nn 为给定数组的长度。我们需要额外的一个数组保存排序后的数组 \textit{numsSorted}numsSorted。

方法二：一次遍历
思路与算法

假设 \textit{nums}_Bnums 
B
​
  在 \textit{nums}nums 中对应区间为 [\textit{left},\textit{right}][left,right]。

注意到 \textit{nums}_Bnums 
B
​
  和 \textit{nums}_Cnums 
C
​
  中任意一个数都大于等于 \textit{nums}_Anums 
A
​
  中任意一个数。因此有 \textit{nums}_Anums 
A
​
  中每一个数 \textit{nums}_inums 
i
​
  都满足：

\textit{nums}_i \leq \min_{j=i+1}^{n-1} \textit{nums}_j
nums 
i
​
 ≤ 
j=i+1
min
n−1
​
 nums 
j
​
 

我们可以从大到小枚举 ii，用一个变量 \textit{minn}minn 记录 \min_{j=i+1}^{n-1} \textit{nums}_jmin 
j=i+1
n−1
​
 nums 
j
​
 。每次移动 ii，都可以 O(1)O(1) 地更新 \textit{minn}minn。这样最后一个使得不等式不成立的 ii 即为 \textit{left}left。\textit{left}left 左侧即为 \textit{nums}_Anums 
A
​
  能取得的最大范围。

同理，我们可以用类似的方法确定 \textit{right}right。在实际代码中，我们可以在一次循环中同时完成左右边界的计算。

特别地，我们需要特判 \textit{nums}nums 有序的情况，此时 \textit{nums}_Bnums 
B
​
  的长度为 00。当我们计算完成左右边界，即可返回 \textit{nums}_Bnums 
B
​
  的长度。

代码

C++JavaC#Python3JavaScriptGolangC

func findUnsortedSubarray(nums []int) int {
    n := len(nums)
    minn, maxn := math.MaxInt64, math.MinInt64
    left, right := -1, -1
    for i, num := range nums {
        if maxn > num {
            right = i
        } else {
            maxn = num
        }
        if minn < nums[n-i-1] {
            left = n - i - 1
        } else {
            minn = nums[n-i-1]
        }
    }
    if right == -1 {
        return 0
    }
    return right - left + 1
}
复杂度分析

时间复杂度：O(n)O(n)，其中 nn 是给定数组的长度，我们仅需要遍历该数组一次。

时间复杂度：O(1)O(1)。我们只需要常数的空间保存若干变量。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/shortest-unsorted-continuous-subarray/solution/zui-duan-wu-xu-lian-xu-zi-shu-zu-by-leet-yhlf/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
