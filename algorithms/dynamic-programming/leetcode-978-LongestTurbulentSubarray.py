# encoding=utf8


'''
978. Longest Turbulent Subarray
Given an integer array arr, return the length of a maximum size turbulent subarray of arr.

A subarray is turbulent if the comparison sign flips between each adjacent pair of elements in the subarray.

More formally, a subarray [arr[i], arr[i + 1], ..., arr[j]] of arr is said to be turbulent if and only if:

For i <= k < j:
arr[k] > arr[k + 1] when k is odd, and
arr[k] < arr[k + 1] when k is even.
Or, for i <= k < j:
arr[k] > arr[k + 1] when k is even, and
arr[k] < arr[k + 1] when k is odd.


Example 1:

Input: arr = [9,4,2,10,7,8,8,1,9]
Output: 5
Explanation: arr[1] > arr[2] < arr[3] > arr[4] < arr[5]
Example 2:

Input: arr = [4,8,12,16]
Output: 2
Example 3:

Input: arr = [100]
Output: 1


Constraints:

1 <= arr.length <= 4 * 104
0 <= arr[i] <= 109



978. 最长湍流子数组
当 A 的子数组 A[i], A[i+1], ..., A[j] 满足下列条件时，我们称其为湍流子数组：

若 i <= k < j，当 k 为奇数时， A[k] > A[k+1]，且当 k 为偶数时，A[k] < A[k+1]；
或 若 i <= k < j，当 k 为偶数时，A[k] > A[k+1] ，且当 k 为奇数时， A[k] < A[k+1]。
也就是说，如果比较符号在子数组中的每个相邻元素对之间翻转，则该子数组是湍流子数组。

返回 A 的最大湍流子数组的长度。



示例 1：

输入：[9,4,2,10,7,8,8,1,9]
输出：5
解释：(A[1] > A[2] < A[3] > A[4] < A[5])
示例 2：

输入：[4,8,12,16]
输出：2
示例 3：

输入：[100]
输出：1


提示：

1 <= A.length <= 40000
0 <= A[i] <= 10^9


'''

# solutions

'''
方法一：双指针
设数组 \textit{arr}arr 的长度为 nn，区间 [\textit{left},\textit{right}](0 \le \textit{left} \le \textit{right} \le n-1)[left,right](0≤left≤right≤n−1) 为当前的区间，区间内构成了一个「湍流子数组」。随后，我们要考虑下一个区间的位置。

根据「湍流子数组」的定义，当 0<\textit{right}<n-10<right<n−1 时：

如果 \textit{arr}[\textit{right}-1] < \textit{arr}[\textit{right}]arr[right−1]<arr[right] 且 \textit{arr}[\textit{right}] > \textit{arr}[\textit{right}+1]arr[right]>arr[right+1]，则 [\textit{left},\textit{right}+1][left,right+1] 也构成「湍流子数组」，因此需要将 \textit{right}right 右移一个单位；

如果 \textit{arr}[\textit{right}-1] > \textit{arr}[\textit{right}]arr[right−1]>arr[right] 且 \textit{arr}[\textit{right}] < \textit{arr}[\textit{right}+1]arr[right]<arr[right+1]，同理，也需要将 \textit{right}right 右移一个单位；

否则，[\textit{right}-1,\textit{right}+1][right−1,right+1] 无法构成「湍流子数组」，当 \textit{left}<\textit{right}left<right 时，[\textit{left},\textit{right}+1][left,right+1] 也无法构成「湍流子数组」，因此需要将 \textit{left}left 移到 \textit{right}right，即令 \textit{left}=\textit{right}left=right。

此外，我们还需要特殊考虑区间长度为 11 (即 \textit{left}left 和 \textit{right}right 相等的情况)：只要 \textit{arr}[\textit{right}] \ne \textit{arr}[\textit{right}+1]arr[right]

​
 =arr[right+1]，就可以将 \textit{right}right 右移一个单位；否则，\textit{left}left 和 \textit{right}right 都要同时右移。

C++JavaJavaScriptGolangC

func maxTurbulenceSize(arr []int) int {
    n := len(arr)
    ans := 1
    left, right := 0, 0
    for right < n-1 {
        if left == right {
            if arr[left] == arr[left+1] {
                left++
            }
            right++
        } else {
            if arr[right-1] < arr[right] && arr[right] > arr[right+1] {
                right++
            } else if arr[right-1] > arr[right] && arr[right] < arr[right+1] {
                right++
            } else {
                left = right
            }
        }
        ans = max(ans, right-left+1)
    }
    return ans
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}
复杂度分析

时间复杂度：O(n)O(n)，其中 nn 为数组的长度。区间的左右端点最多各移动 nn 次。

空间复杂度：O(1)O(1)。只需要维护常数额外空间。

方法二：动态规划
也可以使用动态规划的方法计算最长湍流子数组的长度。

记 \textit{dp}[i][0]dp[i][0] 为以 \textit{arr}[i]arr[i] 结尾，且 \textit{arr}[i-1] < \textit{arr}[i]arr[i−1]<arr[i] 的「湍流子数组」的最大长度；\textit{dp}[i][1]dp[i][1] 为以 \textit{arr}[i]arr[i] 结尾，且 \textit{arr}[i-1] > \textit{arr}[i]arr[i−1]>arr[i] 的「湍流子数组」的最大长度。

显然，以下标 00 结尾的「湍流子数组」的最大长度为 11，因此边界情况为 \textit{dp}[0][0]=\textit{dp}[0][1]=1dp[0][0]=dp[0][1]=1。

当 i>0i>0 时，考虑 \textit{arr}[i-1]arr[i−1] 和 \textit{arr}[i]arr[i] 之间的大小关系：

如果 \textit{arr}[i-1]>\textit{arr}[i]arr[i−1]>arr[i]，则如果以下标 i-1i−1 结尾的子数组是「湍流子数组」，应满足 i-1=0i−1=0，或者当 i-1>0i−1>0 时 \textit{arr}[i-2] < \textit{arr}[i-1]arr[i−2]<arr[i−1]，因此 \textit{dp}[i][0]=\textit{dp}[i-1][1]+1dp[i][0]=dp[i−1][1]+1，\textit{dp}[i][1]=1dp[i][1]=1；

如果 \textit{arr}[i-1]<\textit{arr}[i]arr[i−1]<arr[i]，则如果以下标 i-1i−1 结尾的子数组是「湍流子数组」，应满足 i-1=0i−1=0，或者当 i-1>0i−1>0 时 \textit{arr}[i-2] > \textit{arr}[i-1]arr[i−2]>arr[i−1]，因此 \textit{dp}[i][0]=1dp[i][0]=1，\textit{dp}[i][1]=\textit{dp}[i-1][0]+1dp[i][1]=dp[i−1][0]+1；

如果 \textit{arr}[i-1]=\textit{arr}[i]arr[i−1]=arr[i]，则 \textit{arr}[i-1]arr[i−1] 和 \textit{arr}[i]arr[i] 不能同时出现在同一个湍流子数组中，因此 \textit{dp}[i][0]=\textit{dp}[i][1]=1dp[i][0]=dp[i][1]=1。

最终，\textit{dp}dp 数组的最大值即为所求的答案。

C++JavaJavaScriptGolangC

func maxTurbulenceSize(arr []int) int {
    n := len(arr)
    dp := make([][2]int, n)
    dp[0] = [2]int{1, 1}
    for i := 1; i < n; i++ {
        dp[i] = [2]int{1, 1}
        if arr[i-1] > arr[i] {
            dp[i][0] = dp[i-1][1] + 1
        } else if arr[i-1] < arr[i] {
            dp[i][1] = dp[i-1][0] + 1
        }
    }

    ans := 1
    for i := 0; i < n; i++ {
        ans = max(ans, dp[i][0])
        ans = max(ans, dp[i][1])
    }
    return ans
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}
上述实现的空间复杂度是 O(n)O(n)。注意到当 i>0i>0 时，下标 ii 处的 \textit{dp}dp 值只和下标 i-1i−1 处的 \textit{dp}dp 值有关，因此可以用两个变量 \textit{dp}_0dp
0
​
  和 \textit{dp}_1dp
1
​
  代替 \textit{dp}[i][0]dp[i][0] 和 \textit{dp}[i][1]dp[i][1]，将空间复杂度降到 O(1)O(1)。

C++JavaJavaScriptGolangC

func maxTurbulenceSize(arr []int) int {
    ans := 1
    n := len(arr)
    dp0, dp1 := 1, 1
    for i := 1; i < n; i++ {
        if arr[i-1] > arr[i] {
            dp0, dp1 = dp1+1, 1
        } else if arr[i-1] < arr[i] {
            dp0, dp1 = 1, dp0+1
        } else {
            dp0, dp1 = 1, 1
        }
        ans = max(ans, max(dp0, dp1))
    }
    return ans
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}
复杂度分析

时间复杂度：O(n)O(n)，其中 nn 为数组的长度。需要遍历数组 \textit{arr}arr 一次，计算 \textit{dp}dp 的值。

空间复杂度：O(1)O(1)。使用空间优化的做法，只需要维护常数额外空间。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/longest-turbulent-subarray/solution/zui-chang-tuan-liu-zi-shu-zu-by-leetcode-t4d8/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
