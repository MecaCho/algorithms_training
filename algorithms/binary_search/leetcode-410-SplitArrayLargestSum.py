# encoding=utf8

'''
410. Split Array Largest Sum
Given an array which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays. Write an algorithm to minimize the largest sum among these m subarrays.

Note:
If n is the length of array, assume the following constraints are satisfied:

1 ≤ n ≤ 1000
1 ≤ m ≤ min(50, n)
Examples:

Input:
nums = [7,2,5,10,8]
m = 2

Output:
18

Explanation:
There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8],
where the largest sum among the two subarrays is only 18.

410. 分割数组的最大值
给定一个非负整数数组和一个整数 m，你需要将这个数组分成 m 个非空的连续子数组。设计一个算法使得这 m 个子数组各自和的最大值最小。

注意:
数组长度 n 满足以下条件:

1 ≤ n ≤ 1000
1 ≤ m ≤ min(50, n)
示例:

输入:
nums = [7,2,5,10,8]
m = 2

输出:
18

解释:
一共有四种方法将nums分割为2个子数组。
其中最好的方式是将其分为[7,2,5] 和 [10,8]，
因为此时这两个子数组各自的和的最大值为18，在所有情况中最小。

'''

class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        def check(x):
            cur = 0
            count = 1
            for num in nums:
                if cur + num > x:
                    cur = num
                    count += 1
                else:
                    cur += num
            return count <= m

        i, j = max(nums), sum(nums)
        while i < j:
            mid = (i + j) / 2
            if check(mid):
                j = mid
            else:
                i = mid + 1
        return i


# solutions

'''
方法一：动态规划
思路与算法

「将数组分割为 mm 段，求……」是动态规划题目常见的问法。

本题中，我们可以令 f[i][j]f[i][j] 表示将数组的前 ii 个数分割为 jj 段所能得到的最大连续子数组和的最小值。在进行状态转移时，我们可以考虑第 jj 段的具体范围，即我们可以枚举 kk，其中前 kk 个数被分割为 j-1j−1 段，而第 k+1k+1 到第 ii 个数为第 jj 段。此时，这 jj 段子数组中和的最大值，就等于 f[k][j-1]f[k][j−1] 与 \textit{sub}(k+1, i)sub(k+1,i) 中的较大值，其中 \textit{sub}(i,j)sub(i,j) 表示数组 \textit{nums}nums 中下标落在区间 [i,j][i,j] 内的数的和。

由于我们要使得子数组中和的最大值最小，因此可以列出如下的状态转移方程：

f[i][j] = \min_{k=0}^{i-1} \Big\{ \max(f[k][j-1], \textit{sub}(k+1,i)) \Big\}
f[i][j]= 
k=0
min
i−1
​	
 {max(f[k][j−1],sub(k+1,i))}

对于状态 f[i][j]f[i][j]，由于我们不能分出空的子数组，因此合法的状态必须有 i \geq ji≥j。对于不合法（i < ji<j）的状态，由于我们的目标是求出最小值，因此可以将这些状态全部初始化为一个很大的数。在上述的状态转移方程中，一旦我们尝试从不合法的状态 f[k][j-1]f[k][j−1] 进行转移，那么 \max(\cdots)max(⋯) 将会是一个很大的数，就不会对最外层的 \min\{\cdots\}min{⋯} 产生任何影响。

此外，我们还需要将 f[0][0]f[0][0] 的值初始化为 00。在上述的状态转移方程中，当 j=1j=1 时，唯一的可能性就是前 ii 个数被分成了一段。如果枚举的 k=0k=0，那么就代表着这种情况；如果 k \neq 0k 

​	
 =0，对应的状态 f[k][0]f[k][0] 是一个不合法的状态，无法进行转移。因此我们需要令 f[0][0] = 0f[0][0]=0。

最终的答案即为 f[n][m]f[n][m]。

C++JavaPython3CGolang

class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        n = len(nums)
        f = [[10**18] * (m + 1) for _ in range(n + 1)]
        sub = [0]
        for elem in nums:
            sub.append(sub[-1] + elem)
        
        f[0][0] = 0
        for i in range(1, n + 1):
            for j in range(1, min(i, m) + 1):
                for k in range(i):
                    f[i][j] = min(f[i][j], max(f[k][j - 1], sub[i] - sub[k]))
        
        return f[n][m]
复杂度分析

时间复杂度：O(n^2 \times m)O(n 
2
 ×m)，其中 nn 是数组的长度，mm 是分成的非空的连续子数组的个数。总状态数为 O(n \times m)O(n×m)，状态转移时间复杂度 O(n)O(n)，所以总时间复杂度为 O(n^2 \times m)O(n 
2
 ×m)。

空间复杂度：O(n \times m)O(n×m)，为动态规划数组的开销。

方法二：二分查找 + 贪心
思路及算法

「使……最大值尽可能小」是二分搜索题目常见的问法。

本题中，我们注意到：当我们选定一个值 xx，我们可以线性地验证是否存在一种分割方案，满足其最大分割子数组和不超过 xx。策略如下：

贪心地模拟分割的过程，从前到后遍历数组，用 \textit{sum}sum 表示当前分割子数组的和，\textit{cnt}cnt 表示已经分割出的子数组的数量（包括当前子数组），那么每当 \textit{sum}sum 加上当前值超过了 xx，我们就把当前取的值作为新的一段分割子数组的开头，并将 \textit{cnt}cnt 加 11。遍历结束后验证是否 \textit{cnt}cnt 不超过 mm。

这样我们可以用二分查找来解决。二分的上界为数组 \textit{nums}nums 中所有元素的和，下界为数组 \textit{nums}nums 中所有元素的最大值。通过二分查找，我们可以得到最小的最大分割子数组和，这样就可以得到最终的答案了。

代码

C++JavaPython3CGolang

func splitArray(nums []int, m int) int {
    left, right := 0, 0
    for i := 0; i < len(nums); i++ {
        right += nums[i]
        if left < nums[i] {
            left = nums[i]
        }
    }
    for left < right {
        mid := (right - left) / 2 + left
        if check(nums, mid, m) {
            right = mid
        } else {
            left = mid + 1
        }
    }
    return left
}

func check(nums []int, x, m int) bool {
    sum, cnt := 0, 1
    for i := 0; i < len(nums); i++ {
        if sum + nums[i] > x {
            cnt++
            sum = nums[i]
        } else {
            sum += nums[i]
        }
    }
    return cnt <= m
}
复杂度分析

时间复杂度：O(n \times \log(\textit{sum}-\textit{maxn}))O(n×log(sum−maxn))，其中 \textit{sum}sum 表示数组 \textit{nums}nums 中所有元素的和，\textit{maxn}maxn 表示数组所有元素的最大值。每次二分查找时，需要对数组进行一次遍历，时间复杂度为 O(n)O(n)，因此总时间复杂度是 O(n \times \log(\textit{sum}-\textit{maxn}))O(n×log(sum−maxn))。

空间复杂度：O(1)O(1)。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/split-array-largest-sum/solution/fen-ge-shu-zu-de-zui-da-zhi-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
