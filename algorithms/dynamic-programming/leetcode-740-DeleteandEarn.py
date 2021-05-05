# encoding=utf8

'''
740. Delete and Earn

Given an array nums of integers, you can perform operations on the array.

In each operation, you pick any nums[i] and delete it to earn nums[i] points. After, you must delete every element equal to nums[i] - 1 or nums[i] + 1.

You start with 0 points. Return the maximum number of points you can earn by applying such operations.

 

Example 1:

Input: nums = [3,4,2]
Output: 6
Explanation: Delete 4 to earn 4 points, consequently 3 is also deleted.
Then, delete 2 to earn 2 points.
6 total points are earned.
Example 2:

Input: nums = [2,2,3,3,3,4]
Output: 9
Explanation: Delete 3 to earn 3 points, deleting both 2's and the 4.
Then, delete 3 again to earn 3 points, and 3 again to earn 3 points.
9 total points are earned.
 

Constraints:

1 <= nums.length <= 2 * 104
1 <= nums[i] <= 104


740. 删除并获得点数

给你一个整数数组 nums ，你可以对它进行一些操作。

每次操作中，选择任意一个 nums[i] ，删除它并获得 nums[i] 的点数。之后，你必须删除每个等于 nums[i] - 1 或 nums[i] + 1 的元素。

开始你拥有 0 个点数。返回你能通过这些操作获得的最大点数。

 

示例 1：

输入：nums = [3,4,2]
输出：6
解释：
删除 4 获得 4 个点数，因此 3 也被删除。
之后，删除 2 获得 2 个点数。总共获得 6 个点数。
示例 2：

输入：nums = [2,2,3,3,3,4]
输出：9
解释：
删除 3 获得 3 个点数，接着要删除两个 2 和 4 。
之后，再次删除 3 获得 3 个点数，再次删除 3 获得 3 个点数。
总共获得 9 个点数。
 

提示：

1 <= nums.length <= 2 * 104
1 <= nums[i] <= 104
'''


class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = max(nums) + 1
        values = {i:0 for i in range(length)}
        for num in nums:
            values[num] += num
        
        dp = []
        for i in range(length):
            dp.append([0, 0])
            dp[i][0] = dp[i-1][1]
            dp[i][1] = max(dp[i-1][0] + values[i], dp[i-1][1])
        return dp[-1][1]

# solutions

'''
方法一：动态规划
思路

根据题意，在选择了元素 xx 后，该元素以及所有等于 x-1x−1 或 x+1x+1 的元素会从数组中删去。若还有多个值为 xx 的元素，由于所有等于 x-1x−1 或 x+1x+1 的元素已经被删除，我们可以直接删除 xx 并获得其点数。因此若选择了 xx，所有等于 xx 的元素也应一同被选择，以尽可能多地获得点数。

记元素 xx 在数组中出现的次数为 c_xc 
x
​	
 ，我们可以用一个数组 sumsum 记录数组 \textit{nums}nums 中所有相同元素之和，即 \textit{sum}[x]=x\cdot c_xsum[x]=x⋅c 
x
​	
 。若选择了 xx，则可以获取 \textit{sum}[x]sum[x] 的点数，且无法再选择 x-1x−1 和 x+1x+1。这与「198. 打家劫舍」是一样的，在统计出 \textit{sum}sum 数组后，读者可参考「198. 打家劫舍的官方题解」中的动态规划过程计算出答案。

代码

C++JavaC#GolangPython3CJavaScript

func deleteAndEarn(nums []int) int {
    maxVal := 0
    for _, val := range nums {
        maxVal = max(maxVal, val)
    }
    sum := make([]int, maxVal+1)
    for _, val := range nums {
        sum[val] += val
    }
    return rob(sum)
}

func rob(nums []int) int {
    first, second := nums[0], max(nums[0], nums[1])
    for i := 2; i < len(nums); i++ {
        first, second = second, max(first+nums[i], second)
    }
    return second
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}
复杂度分析

时间复杂度：O(N+M)O(N+M)，其中 NN 是数组 \textit{nums}nums 的长度，MM 是 \textit{nums}nums 中元素的最大值。

空间复杂度：O(M)O(M)。

方法二：排序 + 动态规划
注意到若 \textit{nums}nums 中不存在某个元素 xx，则选择任一小于 xx 的元素不会影响到大于 xx 的元素的选择。因此我们可以将 \textit{nums}nums 排序后，将其划分成若干连续子数组，子数组内任意相邻元素之差不超过 11。对每个子数组按照方法一的动态规划过程计算出结果，累加所有结果即为答案。

代码

C++JavaC#GolangPython3CJavaScript

func deleteAndEarn(nums []int) (ans int) {
    sort.Ints(nums)
    sum := []int{nums[0]}
    for i := 1; i < len(nums); i++ {
        if val := nums[i]; val == nums[i-1] {
            sum[len(sum)-1] += val
        } else if val == nums[i-1]+1 {
            sum = append(sum, val)
        } else {
            ans += rob(sum)
            sum = []int{val}
        }
    }
    ans += rob(sum)
    return
}

func rob(nums []int) int {
    if len(nums) == 1 {
        return nums[0]
    }
    first, second := nums[0], max(nums[0], nums[1])
    for i := 2; i < len(nums); i++ {
        first, second = second, max(first+nums[i], second)
    }
    return second
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}
复杂度分析

时间复杂度：O(N\log N)O(NlogN)，其中 NN 是数组 \textit{nums}nums 的长度。对 \textit{nums}nums 排序需要花费 O(N\log N)O(NlogN) 的时间，遍历计算需要花费 O(N)O(N) 的时间，故总的时间复杂度为 O(N\log N)O(NlogN)。

空间复杂度：O(N)O(N)。统计 \textit{sum}sum 至多需要花费 O(N)O(N) 的空间。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/delete-and-earn/solution/shan-chu-bing-huo-de-dian-shu-by-leetcod-x1pu/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
