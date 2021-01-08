# encoding=utf8

'''
189. Rotate Array
Given an array, rotate the array to the right by k steps, where k is non-negative.

Follow up:

Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
Could you do it in-place with O(1) extra space?


Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]


Constraints:

1 <= nums.length <= 2 * 104
-231 <= nums[i] <= 231 - 1
0 <= k <= 105


189. 旋转数组
给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。

示例 1:

输入: [1,2,3,4,5,6,7] 和 k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右旋转 1 步: [7,1,2,3,4,5,6]
向右旋转 2 步: [6,7,1,2,3,4,5]
向右旋转 3 步: [5,6,7,1,2,3,4]
示例 2:

输入: [-1,-100,3,99] 和 k = 2
输出: [3,99,-1,-100]
解释:
向右旋转 1 步: [99,-1,-100,3]
向右旋转 2 步: [3,99,-1,-100]
说明:

尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
要求使用空间复杂度为 O(1) 的 原地 算法。
'''


class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        return nums[len(nums) - k:] + nums[0:len(nums) - k]


class Solution20210108(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:len(nums) - k] if k != 0 else nums


if __name__ == '__main__':
    demo = Solution()
    print(demo.rotate([1, 2, 3, 4, 5, 6, 7], 3))

# solutions

'''
方法一：使用额外的数组
我们可以使用额外的数组来将每个元素放至正确的位置。用 nn 表示数组的长度，我们遍历原数组，将原数组下标为 ii 的元素放至新数组下标为 (i+k)\bmod n(i+k)modn 的位置，最后将新数组拷贝至原数组即可。

C++JavaJavaScriptGolangC

func rotate(nums []int, k int) {
    newNums := make([]int, len(nums))
    for i, v := range nums {
        newNums[(i+k)%len(nums)] = v
    }
    copy(nums, newNums)
}
复杂度分析

时间复杂度： O(n)O(n)，其中 nn 为数组的长度。

空间复杂度： O(n)O(n)。

方法二：环状替换
方法一中使用额外数组的原因在于如果我们直接将每个数字放至它最后的位置，这样被放置位置的元素会被覆盖从而丢失。因此，从另一个角度，我们可以将被替换的元素保存在变量 \textit{temp}temp 中，从而避免了额外数组的开销。

我们从位置 00 开始，最初令 \textit{temp}=\textit{nums}[0]temp=nums[0]。根据规则，位置 00 的元素会放至 (0+k)\bmod n(0+k)modn 的位置，令 x=(0+k)\bmod 
nx=(0+k)modn，此时交换 \textit{temp}temp 和 \textit{nums}[x]nums[x]，完成位置 xx 的更新。然后，我们考察位置 xx，并交换 \textit{temp}temp 和 
\textit{nums}[(x+k)\bmod n]nums[(x+k)modn]，从而完成下一个位置的更新。不断进行上述过程，直至回到初始位置 00。

容易发现，当回到初始位置 00 时，有些数字可能还没有遍历到，此时我们应该从下一个数字开始重复的过程，可是这个时候怎么才算遍历结束呢？我们不妨先考虑这样一个问题：从 00 开始不断遍历，最终回到起点 00 的过程中，我们遍历了多少个元素？

由于最终回到了起点，故该过程恰好走了整数数量的圈，不妨设为 aa 圈；再设该过程总共遍历了 bb 个元素。因此，我们有 an=bkan=bk，即 anan 一定为 n,kn,k 的公倍数。又因为我们在第一次回到起点时就结束，因此 aa 
要尽可能小，故 anan 就是 n,kn,k 的最小公倍数 \text{lcm}(n,k)lcm(n,k)，因此 bb 就为 \text{lcm}(n,k)/klcm(n,k)/k。

这说明单次遍历会访问到 \text{lcm}(n,k)/klcm(n,k)/k 个元素。为了访问到所有的元素，我们需要进行遍历的次数为

\frac{n}{\text{lcm}(n,k)/k}=\frac{nk}{\text{lcm}(n,k)}=\text{gcd}(n,k)
lcm(n,k)/k
n
​	
 = 
lcm(n,k)
nk
​	
 =gcd(n,k)

其中 \text{gcd}gcd 指的是最大公约数。

我们用下面的例子更具体地说明这个过程：


nums = [1, 2, 3, 4, 5, 6]
k = 2


如果读者对上面的数学推导的理解有一定困难，也可以使用另外一种方式完成代码：使用单独的变量 \textit{count}count 跟踪当前已经访问的元素数量，当 \textit{count}=ncount=n 时，结束遍历过程。

C++JavaJavaScriptGolangC

func rotate(nums []int, k int) {
    n := len(nums)
    k %= n
    for start, count := 0, gcd(k, n); start < count; start++ {
        pre, cur := nums[start], start
        for ok := true; ok; ok = cur != start {
            next := (cur + k) % n
            nums[next], pre, cur = pre, nums[next], next
        }
    }
}

func gcd(a, b int) int {
    for a != 0 {
        a, b = b%a, a
    }
    return b
}
复杂度分析

时间复杂度：O(n)O(n)，其中 nn 为数组的长度。每个元素只会被遍历一次。

空间复杂度：O(1)O(1) 。我们只需常数空间存放若干变量。

方法三：数组翻转
该方法基于如下的事实：当我们将数组的元素向右移动 kk 次后，尾部 k\bmod nkmodn 个元素会移动至数组头部，其余元素向后移动 k\bmod nkmodn 个位置。

该方法为数组的翻转：我们可以先将所有元素翻转，这样尾部的 k\bmod nkmodn 个元素就被移至数组头部，然后我们再翻转 [0, k\bmod n-1][0,kmodn−1] 区间的元素和 [k\bmod n, 
n-1][kmodn,n−1] 区间的元素即能得到最后的答案。

我们以 n=7n=7，k=3k=3 为例进行如下展示：

操作	结果
原始数组	1~2~3~4~5~6~71 2 3 4 5 6 7
翻转所有元素	7~6~5~4~3~2~17 6 5 4 3 2 1
翻转 [0, k\bmod n - 1][0,kmodn−1] 区间的元素	5~6~7~4~3~2~15 6 7 4 3 2 1
翻转 [k\bmod n, n - 1][kmodn,n−1] 区间的元素	5~6~7~1~2~3~45 6 7 1 2 3 4
C++JavaJavaScriptGolangC

func reverse(a []int) {
    for i, n := 0, len(a); i < n/2; i++ {
        a[i], a[n-1-i] = a[n-1-i], a[i]
    }
}

func rotate(nums []int, k int) {
    k %= len(nums)
    reverse(nums)
    reverse(nums[:k])
    reverse(nums[k:])
}
复杂度分析

时间复杂度：O(n)O(n)，其中 nn 为数组的长度。每个元素被翻转两次，一共 nn 个元素，因此总时间复杂度为 O(2n)=O(n)O(2n)=O(n)。

空间复杂度：O(1)O(1)。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/rotate-array/solution/xuan-zhuan-shu-zu-by-leetcode-solution-nipk/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
