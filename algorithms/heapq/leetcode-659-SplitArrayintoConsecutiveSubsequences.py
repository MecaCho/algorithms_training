'''
659. Split Array into Consecutive Subsequences
Given an array nums sorted in ascending order, return true if and only if you can split it into 1 or more subsequences such that each subsequence consists of consecutive integers and has length at least 3.



Example 1:

Input: [1,2,3,3,4,5]
Output: True
Explanation:
You can split them into two consecutive subsequences :
1, 2, 3
3, 4, 5
Example 2:

Input: [1,2,3,3,4,4,5,5]
Output: True
Explanation:
You can split them into two consecutive subsequences :
1, 2, 3, 4, 5
3, 4, 5
Example 3:

Input: [1,2,3,4,4,5]
Output: False


Constraints:

1 <= nums.length <= 10000

659. 分割数组为连续子序列
给你一个按升序排序的整数数组 num（可能包含重复数字），请你将它们分割成一个或多个子序列，其中每个子序列都由连续整数组成且长度至少为 3 。

如果可以完成上述分割，则返回 true ；否则，返回 false 。



示例 1：

输入: [1,2,3,3,4,5]
输出: True
解释:
你可以分割出这样两个连续子序列 :
1, 2, 3
3, 4, 5


示例 2：

输入: [1,2,3,3,4,4,5,5]
输出: True
解释:
你可以分割出这样两个连续子序列 :
1, 2, 3, 4, 5
3, 4, 5


示例 3：

输入: [1,2,3,4,4,5]
输出: False


提示：

输入的数组长度范围为 [1, 10000]
'''


import heapq
import collections
class Solution(object):
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        mp = collections.defaultdict(list)
        for x in nums:
            queue = mp.get(x - 1)
            if queue:
                prevLength = heapq.heappop(queue)
                heapq.heappush(mp[x], prevLength + 1)
            else:
                heapq.heappush(mp[x], 1)
        # print queue, mp
        return not any(queue and queue[0] < 3 for queue in mp.values())


# solution

'''
方法一：哈希表 + 最小堆
由于需要将数组分割成一个或多个由连续整数组成的子序列，因此只要知道子序列的最后一个数字和子序列的长度，就能确定子序列。

当 xx 在数组中时，如果存在一个子序列以 x-1x−1 结尾，长度为 kk，则可以将 xx 加入该子序列中，得到长度为 k+1k+1 的子序列。如果不存在以 x-1x−1 结尾的子序列，则必须新建一个只包含 xx 的子序列，长度为 11。

当 xx 在数组中时，如果存在多个子序列以 x-1x−1 结尾，应该将 xx 加入其中的哪一个子序列？由于题目要求每个子序列的长度至少为 33，显然应该让最短的子序列尽可能长，因此应该将 xx 加入其中最短的子序列。

基于上述分析，可以使用哈希表和最小堆进行实现。

哈希表的键为子序列的最后一个数字，值为最小堆，用于存储所有的子序列长度，最小堆满足堆顶的元素是最小的，因此堆顶的元素即为最小的子序列长度。

遍历数组，当遍历到元素 xx 时，可以得到一个以 xx 结尾的子序列。

如果哈希表中存在以 x-1x−1 结尾的子序列，则取出以 x-1x−1 结尾的最小的子序列长度，将子序列长度加 11 之后作为以 xx 结尾的子序列长度。此时，以 x-1x−1 结尾的子序列减少了一个，以 xx 结尾的子序列增加了一个。

如果哈希表中不存在以 x-1x−1 结尾的子序列，则新建一个长度为 11 的以 xx 结尾的子序列。

由于数组是有序的，因此当遍历到元素 xx 时，数组中所有小于 xx 的元素都已经被遍历过，不会出现当前元素比之前的元素小的情况。

遍历结束之后，检查哈希表中存储的每个子序列的长度是否都不小于 33，即可判断是否可以完成分割。由于哈希表中的每条记录的值都是最小堆，堆顶元素为最小的子序列长度（以当前的键为最后一个数字的子序列），因此只要遍历每个最小堆的堆顶元素，即可判断每个子序列的长度是否都不小于 33。


1 / 23

JavaC++JavaScriptPython3Golang

class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        mp = collections.defaultdict(list)
        for x in nums:
            if queue := mp.get(x - 1):
                prevLength = heapq.heappop(queue)
                heapq.heappush(mp[x], prevLength + 1)
            else:
                heapq.heappush(mp[x], 1)
        
        return not any(queue and queue[0] < 3 for queue in mp.values())
复杂度分析

时间复杂度：O(n \log n)O(nlogn)，其中 nn 是数组的长度。
需要遍历数组，对于数组中的每个数，都要对哈希表和最小堆进行更新。每个数对应的最小堆的长度不超过 nn，因此每次对最小堆的操作的时间复杂度是 O(\log n)O(logn)，数组长度为 nn，因此时间复杂度是 O(n \log n)O(nlogn)。
然后需要遍历哈希表中的每一条记录，判断是否满足每个子序列的长度都不小于 33，子序列的数量不会超过 nn，因此时间复杂度是 O(n)O(n)。
因此总时间复杂度是 O(n \log n)O(nlogn)。

空间复杂度：O(n)O(n)，其中 nn 是数组的长度。需要使用哈希表和最小堆存储以每个数结尾的各个子序列的长度，哈希表和最小堆中的元素数量不会超过数组的长度。

方法二：贪心
从方法一可以看到，对于数组中的元素 xx，如果存在一个子序列以 x-1x−1 结尾，则可以将 xx 加入该子序列中。将 xx 加入已有的子序列总是比新建一个只包含 xx 的子序列更优，因为前者可以将一个已有的子序列的长度增加 11，而后者新建一个长度为 11 的子序列，而题目要求分割成的子序列的长度都不小于 33，因此应该尽量避免新建短的子序列。

基于此，可以通过贪心的方法判断是否可以完成分割。

使用两个哈希表，第一个哈希表存储数组中的每个数字的剩余次数，第二个哈希表存储数组中的每个数字作为结尾的子序列的数量。

初始时，每个数字的剩余次数即为每个数字在数组中出现的次数，因此遍历数组，初始化第一个哈希表。

在初始化第一个哈希表之后，遍历数组，更新两个哈希表。只有当一个数字的剩余次数大于 00 时，才需要考虑这个数字是否属于某个子序列。假设当前元素是 xx，进行如下操作。

首先判断是否存在以 x-1x−1 结尾的子序列，即根据第二个哈希表判断 x-1x−1 作为结尾的子序列的数量是否大于 00，如果大于 00，则将元素 xx 加入该子序列中。由于 xx 被使用了一次，因此需要在第一个哈希表中将 xx 的剩余次数减 11。又由于该子序列的最后一个数字从 x-1x−1 变成了 xx，因此需要在第二个哈希表中将 x-1x−1 作为结尾的子序列的数量减 11，以及将 xx 作为结尾的子序列的数量加 11。

否则，xx 为一个子序列的第一个数，为了得到长度至少为 33 的子序列，x+1x+1 和 x+2x+2 必须在子序列中，因此需要判断在第一个哈希表中 x+1x+1 和 x+2x+2 的剩余次数是否都大于 00。

当 x+1x+1 和 x+2x+2 的剩余次数都大于 00 时，可以新建一个长度为 33 的子序列 [x,x+1,x+2][x,x+1,x+2]。由于这三个数都被使用了一次，因此需要在第一个哈希表中将这三个数的剩余次数分别减 11。又由于该子序列的最后一个数字是 x+2x+2，因此需要在第二个哈希表中将 x+2x+2 作为结尾的子序列的数量加 11。

否则，无法得到长度为 33 的子序列 [x,x+1,x+2][x,x+1,x+2]，因此无法完成分割，返回 \text{false}false。

如果整个数组遍历结束时，没有遇到无法完成分割的情况，则可以完成分割，返回 \text{true}true。


1 / 22

JavaC++JavaScriptPython3GolangC

class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        countMap = collections.Counter(nums)
        endMap = collections.Counter()

        for x in nums:
            if (count := countMap[x]) > 0:
                if (prevEndCount := endMap.get(x - 1, 0)) > 0:
                    countMap[x] -= 1
                    endMap[x - 1] = prevEndCount - 1
                    endMap[x] += 1
                else:
                    if (count1 := countMap.get(x + 1, 0)) > 0 and (count2 := countMap.get(x + 2, 0)) > 0:
                        countMap[x] -= 1
                        countMap[x + 1] -= 1
                        countMap[x + 2] -= 1
                        endMap[x + 2] += 1
                    else:
                        return False
        
        return True
复杂度分析

时间复杂度：O(n)O(n)，其中 nn 是数组的长度。需要遍历数组两次，对于数组中的每个元素，更新哈希表的时间复杂度是常数。

空间复杂度：O(n)O(n)，其中 nn 是数组的长度。需要使用两个哈希表，每个哈希表的大小都不会超过 nn。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/split-array-into-consecutive-subsequences/solution/fen-ge-shu-zu-wei-lian-xu-zi-xu-lie-by-l-lbs5/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''