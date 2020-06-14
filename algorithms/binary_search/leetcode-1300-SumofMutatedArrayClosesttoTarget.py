'''
1300. 转变数组后最接近目标值的数组和
给你一个整数数组 arr 和一个目标值 target ，请你返回一个整数 value ，使得将数组中所有大于 value 的值变成 value 后，数组的和最接近  target （最接近表示两者之差的绝对值最小）。

如果有多种使得和最接近 target 的方案，请你返回这些整数中的最小值。

请注意，答案不一定是 arr 中的数字。



示例 1：

输入：arr = [4,9,3], target = 10
输出：3
解释：当选择 value 为 3 时，数组会变成 [3, 3, 3]，和为 9 ，这是最接近 target 的方案。
示例 2：

输入：arr = [2,3,5], target = 10
输出：5
示例 3：

输入：arr = [60864,25176,27249,21296,20204], target = 56803
输出：11361


提示：

1 <= arr.length <= 10^4
1 <= arr[i], target <= 10^5

1300. Sum of Mutated Array Closest to Target
Given an integer array arr and a target value target, return the integer value such that when we change all the integers larger than value in the given array to be equal to value, the sum of the array gets as close as possible (in absolute difference) to target.

In case of a tie, return the minimum such integer.

Notice that the answer is not neccesarilly a number from arr.



Example 1:

Input: arr = [4,9,3], target = 10
Output: 3
Explanation: When using 3 arr converts to [3, 3, 3] which sums 9 and that's the optimal answer.
Example 2:

Input: arr = [2,3,5], target = 10
Output: 5
Example 3:

Input: arr = [60864,25176,27249,21296,20204], target = 56803
Output: 11361


Constraints:

1 <= arr.length <= 10^4
1 <= arr[i], target <= 10^5
'''


class Solution(object):
    def findBestValue(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """

        # arr.sort()
        # i, j = 0, len(arr) -1
        # while i <= j:
        #     mid = (i+j) / 2
        #     sum_ = sum(arr[:mid+1 ]) + arr[mid] * (len(arr) - mid+1)
        #     print(i, j, mid, sum_)
        #     if sum_ < target:
        #         i = mid + 1
        #     elif sum_ > target:
        #         j = mid - 1
        #     else:
        #         return arr[mid]
        # return arr[i]
        def check(val):
            res = 0
            for i in range(len(arr)):
                if arr[i] > val:
                    res += val
                else:
                    res += arr[i]
            return res - target

        l, r = int(target / len(arr)), max(arr)
        # print(l, r)
        min_abs = float("inf")
        res = None
        while l <= r:
            mid = (l + r) / 2

            new_abs = check(mid)
            if abs(new_abs) < min_abs:
                min_abs = abs(new_abs)
                res = mid
            if abs(new_abs) == min_abs and mid < res:
                res = mid

            min_abs = min(min_abs, abs(new_abs))

            if new_abs < 0:
                l = mid + 1
            else:
                r = mid - 1
        return res

# tips

'''
If you draw a graph with the value on one axis and the absolute difference between the target and the array sum, what will you get?

That graph is uni-modal.

Use ternary search on that graph to find the best value.
'''


# solutions

'''
方法一：枚举 + 二分查找
思路和算法

由于数组 arr 中每个元素值的范围是 [1,10^5][1,10 
5
 ]，在可以直接枚举的范围内，因此我们可以对所有可能作为 value 的值进行枚举。

那么 value 值的上下界是多少呢？我们需要进行一些分析：

value 的下界为 0。这是因为当 value = 0 时，数组的和为 0。由于 target 是正整数，因此当 value 继续减小时，数组的和也会随之减小，且变为负数（这个和等于 value * n，其中 n 是数组 arr 的长度），并不会比 value = 0 时更接近 target。

value 的上界为数组 arr 中的最大值。这是因为当 value >= arr 时，数组中所有的元素都不变，因为它们均不大于 value。由于我们需要找到最接近 target 的最小 value 值，因此我们只需将数组 arr 中的最大值作为上界即可。

当我们确定了 value 值的上下界之后，就可以进行枚举了。当枚举到 value = x 时，我们需要将数组 arr 中所有小于等于 x 的值保持不变，所有大于 x 的值变为 x。要实现这个操作，我们可以将数组 arr 先进行排序，随后进行二分查找，找出数组 arr 中最小的比 x 大的元素 arr[i]。此时数组的和变为

arr[0] + ... + arr[i - 1] + x * (n - i)
arr[0]+...+arr[i−1]+x∗(n−i)

由于将数组 arr 中的等于 x 的值变为 x 并没有改变原来的值，因此上述操作可以改为：当枚举到 value = x 时，我们需要将数组 arr 中所有小于 x 的值保持不变，所有大于等于 x 的值变为 x。要实现这个操作，我们可以将数组 arr 先进行排序，随后进行二分查找，找出数组 arr 中最小的大于等于 x 的元素 arr[i]。此时数组的和变为

arr[0] + ... + arr[i - 1] + x * (n - i)
arr[0]+...+arr[i−1]+x∗(n−i)

使用该操作是因为很多编程语言自带的二分查找只能返回目标值第一次出现的位置。在此鼓励读者自己实现返回目标值最后一次出现的位置的二分查找。

为了加速求和操作，我们可以预处理出数组 arr 的前缀和，这样数组求和的时间复杂度即能降为 O(1)O(1)。我们将和与 target 进行比较，同时更新答案即可。

C++Python3JavaGolang

class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        arr.sort()
        n = len(arr)
        prefix = [0]
        for num in arr:
            prefix.append(prefix[-1] + num)
        
        r, ans, diff = max(arr), 0, target
        for i in range(1, r + 1):
            it = bisect.bisect_left(arr, i)
            cur = prefix[it] + (n - it) * i
            if abs(cur - target) < diff:
                ans, diff = i, abs(cur - target)
        return ans
复杂度分析

时间复杂度：O((N + C)\log N)O((N+C)logN)，其中 NN 是数组 arr 的长度，CC 是一个常数，为数组 arr 中的最大值，不会超过 10^510 
5
 。排序需要的时间复杂度为 O(N \log N)O(NlogN)，二分查找的单次时间复杂度为 O(\log N)O(logN)，需要进行 CC 次。

空间复杂度：O(N)O(N)。我们需要 O(N)O(N) 的空间用来存储数组 arr 的前缀和，排序需要 O(\log N)O(logN) 的栈空间，因此最后总空间复杂度为 O(N)O(N)。

方法二：双重二分查找
思路和算法

方法一的枚举策略建立在数组 arr 的元素范围不大的条件之上。如果数组 arr 中的元素范围是 [1,10^9][1,10 
9
 ]，那么我们将无法直接枚举，有没有更好的解决方法呢？

我们首先考虑题目的一个简化版本：我们需要找到 value，使得数组的和最接近 target 且不大于 target。可以发现，在 [0,\max (arr)][0,max(arr)]（即方法一中确定的上下界）的范围之内，随着 value 的增大，数组的和是严格单调递增的。这里「严格」的意思是，不存在两个不同的 value 值，它们对应的数组的和相等。这样一来，一定存在唯一的一个 value 值，使得数组的和最接近且不大于 target。并且由于严格单调递增的性质，我们可以通过二分查找的方法，找到这个 value 值，记为 value_lower。

同样地，我们考虑题目的另一个简化版本：我们需要找到一个 value，使得数组的和最接近 target 且大于 target。我们也可以通过二分查找的方法，找到这个 value 值，记为 value_upper。

显然 value 值就是 value_lower 和 value_upper 中的一个，我们只需要比较这两个值对应的数组的和与 target 的差，就能确定最终的答案。这样一来，我们通过两次二分查找，就可以找出 value 值，在每一次二分查找中，我们使用和方法一中相同的查找方法，快速地求出每个 value 值对应的数组的和。算法从整体上来看，是外层二分查找中嵌套了一个内层二分查找。

那么这个方法还有进一步优化的余地吗？仔细思考一下 value_lower 与 value_upper 的定义，前者最接近且不大于 target，后者最接近且大于 target。由于数组的和随着 value 的增大是严格单调递增的，所以 value_upper 的值一定就是 value_lower + 1。因此我们只需要进行一次外层二分查找得到 value_lower，并直接通过 value_lower + 1 计算出 value_upper 的值就行了。这样我们就减少了一次外层二分查找，虽然时间复杂度没有变化，但降低了常数。

C++Python3JavaGolang

class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        arr.sort()
        n = len(arr)
        prefix = [0]
        for num in arr:
            prefix.append(prefix[-1] + num)
        
        l, r, ans = 0, max(arr), -1
        while l <= r:
            mid = (l + r) // 2
            it = bisect.bisect_left(arr, mid)
            cur = prefix[it] + (n - it) * mid
            if cur <= target:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1

        def check(x):
            return sum(x if num >= x else num for num in arr)
        
        choose_small = check(ans)
        choose_big = check(ans + 1)
        return ans if abs(choose_small - target) <= abs(choose_big - target) else ans + 1
复杂度分析

时间复杂度：O(N\log N)O(NlogN)，其中 NN 是数组 arr 的长度。排序需要的时间复杂度为 O(N \log N)O(NlogN)，外层二分查找的时间复杂度为 O(\log C)O(logC)，内层二分查找的时间复杂度为 O(\log N)O(logN)，它们的乘积在数量级上小于 O(N \log N)O(NlogN)。

空间复杂度：O(N)O(N)。分析同方法一。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/sum-of-mutated-array-closest-to-target/solution/bian-shu-zu-hou-zui-jie-jin-mu-biao-zhi-de-shu-zu-/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''