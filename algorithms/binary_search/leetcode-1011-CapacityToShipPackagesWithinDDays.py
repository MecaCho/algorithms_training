# encoding=utf8

'''
1011. Capacity To Ship Packages Within D Days

A conveyor belt has packages that must be shipped from one port to another within D days.

The ith package on the conveyor belt has a weight of weights[i]. Each day, we load the ship with packages on the conveyor belt (in the order given by weights). We may not load more weight than the maximum weight capacity of the ship.

Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within D days.

 

Example 1:

Input: weights = [1,2,3,4,5,6,7,8,9,10], D = 5
Output: 15
Explanation: A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:
1st day: 1, 2, 3, 4, 5
2nd day: 6, 7
3rd day: 8
4th day: 9
5th day: 10

Note that the cargo must be shipped in the order given, so using a ship of capacity 14 and splitting the packages into parts like (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) is not allowed.
Example 2:

Input: weights = [3,2,2,4,1,4], D = 3
Output: 6
Explanation: A ship capacity of 6 is the minimum to ship all the packages in 3 days like this:
1st day: 3, 2
2nd day: 2, 4
3rd day: 1, 4
Example 3:

Input: weights = [1,2,3,1,1], D = 4
Output: 3
Explanation:
1st day: 1
2nd day: 2
3rd day: 3
4th day: 1, 1
 

Constraints:

1 <= D <= weights.length <= 5 * 104
1 <= weights[i] <= 500

1011. 在 D 天内送达包裹的能力

传送带上的包裹必须在 D 天内从一个港口运送到另一个港口。

传送带上的第 i 个包裹的重量为 weights[i]。每一天，我们都会按给出重量的顺序往传送带上装载包裹。我们装载的重量不会超过船的最大运载重量。

返回能在 D 天内将传送带上的所有包裹送达的船的最低运载能力。

 

示例 1：

输入：weights = [1,2,3,4,5,6,7,8,9,10], D = 5
输出：15
解释：
船舶最低载重 15 就能够在 5 天内送达所有包裹，如下所示：
第 1 天：1, 2, 3, 4, 5
第 2 天：6, 7
第 3 天：8
第 4 天：9
第 5 天：10

请注意，货物必须按照给定的顺序装运，因此使用载重能力为 14 的船舶并将包装分成 (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) 是不允许的。 
示例 2：

输入：weights = [3,2,2,4,1,4], D = 3
输出：6
解释：
船舶最低载重 6 就能够在 3 天内送达所有包裹，如下所示：
第 1 天：3, 2
第 2 天：2, 4
第 3 天：1, 4
示例 3：

输入：weights = [1,2,3,1,1], D = 4
输出：3
解释：
第 1 天：1
第 2 天：2
第 3 天：3
第 4 天：1, 1
 

提示：

1 <= D <= weights.length <= 50000
1 <= weights[i] <= 500
'''


class Solution(object):
    def shipWithinDays(self, weights, D):
        """
        :type weights: List[int]
        :type D: int
        :rtype: int
        """
        min_ = max(weights)
        max_ = sum(weights)

        def check(num):
            count = 1
            tmp = 0
            for i in range(len(weights)):
                if tmp + weights[i] > num:
                    tmp = weights[i]
                    count += 1
                else:
                    tmp += weights[i]
                if count > D:
                    return False
            return True


        while min_ < max_:
            mid = (min_ + max_) // 2
            if check(mid):
                max_ = mid
            else:
                min_ = mid + 1
        return min_


      
 class Solution1(object):
    def shipWithinDays(self, weights, D):
        """
        :type weights: List[int]
        :type D: int
        :rtype: int
        """
        min_ = max(weights)
        max_ = sum(weights)

        while min_ < max_:
            mid = (min_ + max_) // 2
            count = 1
            tmp = 0
            for w in weights:
                if tmp + w > mid:
                    count += 1
                    tmp = 0

                tmp += w

            if count <= D:
                max_ = mid
            else:
                min_ = mid + 1
        return min_

       
       
# solutions
       
'''
方法一：二分查找转化为判定问题
思路与算法

假设当船的运载能力为 xx 时，我们可以在 DD 天内运送完所有包裹，那么只要运载能力大于 xx，我们同样可以在 DD 天内运送完所有包裹：我们只需要使用运载能力为 xx 时的运送方法即可。

这样一来，我们就得到了一个非常重要的结论：

存在一个运载能力的「下限」x_\textit{ans}x 
ans
​	
 ，使得当 x \geq x_\textit{ans}x≥x 
ans
​	
  时，我们可以在 DD 天内运送完所有包裹；当 x < x_\textit{ans}x<x 
ans
​	
  时，我们无法在 DD 天内运送完所有包裹。

同时，x_\textit{ans}x 
ans
​	
  即为我们需要求出的答案。因此，我们就可以使用二分查找的方法找出 x_\textit{ans}x 
ans
​	
  的值。

在二分查找的每一步中，我们实际上需要解决一个判定问题：给定船的运载能力 xx，我们是否可以在 DD 天内运送完所有包裹呢？这个判定问题可以通过贪心的方法来解决：

由于我们必须按照数组 \textit{weights}weights 中包裹的顺序进行运送，因此我们从数组 \textit{weights}weights 的首元素开始遍历，将连续的包裹都安排在同一天进行运送。当这批包裹的重量大于运载能力 xx 时，我们就需要将最后一个包裹拿出来，安排在新的一天，并继续往下遍历。当我们遍历完整个数组后，就得到了最少需要运送的天数。

我们将「最少需要运送的天数」与 DD 进行比较，就可以解决这个判定问题。当其小于等于 DD 时，我们就忽略二分的右半部分区间；当其大于 DD 时，我们就忽略二分的左半部分区间。

细节

二分查找的初始左右边界应当如何计算呢？

对于左边界而言，由于我们不能「拆分」一个包裹，因此船的运载能力不能小于所有包裹中最重的那个的重量，即左边界为数组 \textit{weights}weights 中元素的最大值。

对于右边界而言，船的运载能力也不会大于所有包裹的重量之和，即右边界为数组 \textit{weights}weights 中元素的和。

我们从上述左右边界开始进行二分查找，就可以保证找到最终的答案。

代码

C++JavaPython3JavaScriptGolangC

class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        # 确定二分查找左右边界
        left, right = max(weights), sum(weights)
        while left < right:
            mid = (left + right) // 2
            # need 为需要运送的天数
            # cur 为当前这一天已经运送的包裹重量之和
            need, cur = 1, 0
            for weight in weights:
                if cur + weight > mid:
                    need += 1
                    cur = 0
                cur += weight
            
            if need <= D:
                right = mid
            else:
                left = mid + 1
        
        return left
复杂度分析

时间复杂度：O\big(n\log(\Sigma w)\big)O(nlog(Σw))，其中 nn 是数组 \textit{weights}weights 的长度，\Sigma wΣw 是数组 \textit{weights}weights 中元素的和。二分查找需要执行的次数为 O(\log(\Sigma w))O(log(Σw))，每一步中需要对数组 \textit{weights}weights 进行依次遍历，时间为 O(n)O(n)，相乘即可得到总时间复杂度。

空间复杂度：O(1)O(1)。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/capacity-to-ship-packages-within-d-days/solution/zai-d-tian-nei-song-da-bao-guo-de-neng-l-ntml/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
