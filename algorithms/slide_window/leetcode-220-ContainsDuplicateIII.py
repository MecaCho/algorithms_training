# encoding=utf8


'''
220. Contains Duplicate III
Given an integer array nums and two integers k and t, return true if there are two distinct indices i and j in the array such that abs(nums[i] - nums[j]) <= t and abs(i - j) <= k.



Example 1:

Input: nums = [1,2,3,1], k = 3, t = 0
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1, t = 2
Output: true
Example 3:

Input: nums = [1,5,9,1,5,9], k = 2, t = 3
Output: false


Constraints:

0 <= nums.length <= 2 * 104
-231 <= nums[i] <= 231 - 1
0 <= k <= 104
0 <= t <= 231 - 1



220. 存在重复元素 III
给你一个整数数组 nums 和两个整数 k 和 t 。请你判断是否存在 两个不同下标 i 和 j，使得 abs(nums[i] - nums[j]) <= t ，同时又满足 abs(i - j) <= k 。

如果存在则返回 true，不存在返回 false。



示例 1：

输入：nums = [1,2,3,1], k = 3, t = 0
输出：true
示例 2：

输入：nums = [1,0,1,1], k = 1, t = 2
输出：true
示例 3：

输入：nums = [1,5,9,1,5,9], k = 2, t = 3
输出：false


提示：

0 <= nums.length <= 2 * 104
-231 <= nums[i] <= 231 - 1
0 <= k <= 104
0 <= t <= 231 - 1

'''


class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        from sortedcontainers import SortedSet
        st = SortedSet()
        left, right = 0, 0
        res = 0
        while right < len(nums):
            if right - left > k:
                st.remove(nums[left])
                left += 1
            index = bisect.bisect_left(st, nums[right] - t)
            if st and index >= 0 and index < len(st) and abs(st[index] - nums[right]) <= t:
                return True
            st.add(nums[right])
            right += 1
        return False



# solutions



'''
解题思路
题意：数组中是否存在一个大小不超过 k 的子数组，该子数组内的最大值和最小值的差不超过 t。
今天这个题目和「1438. 绝对差不超过限制的最长连续子数组」非常像，本题是固定长度求差值，1438 题是固定差值求长度。

同样地，我们仍然用滑动窗口方法，让滑动窗口的大小固定为 k。

滑动窗口问题，可以使用我多次分享的滑动窗口模板解决，模板请见分享滑动窗口模板，秒杀滑动窗口问题。

本题最大的难点在于快速地找滑动窗口内的最大值和最小值，以及删除指定元素，类似题目如 480. 滑动窗口中位数。

如果遍历求滑动窗口内的最大值和最小值，时间复杂度是 O(K)O(K)，肯定会超时。降低时间复杂度的一个绝招就是增加空间复杂度：利用更好的数据结构。是的，我们的目的是快速让一组数据有序，那就寻找一个内部是有序的数据结构呗！下面我分语言讲解一下常见的内部有序的数据结构。

在 C++ 中 set/multiset/map 内部元素是有序的，它们都基于红黑树实现。其中 set 会对元素去重，而 multiset 可以有重复元素，map 是 key 有序的哈希表。
在 Java 中 TreeSet 是有序的去重集合，TreeMap 是 key 有序的哈希表，它们也是基于红黑树实现的。
在 Python 中 sortedcontainers  实现了有序的容器。
下面这个图是 C++ 的 multiset 内部结构示意图（Java 的 TreeSet 也类似，但没有重复元素），它是个平衡二叉搜索树(BST)，插入元素时会自动调整二叉树，使得每个子树根节点的键值大于左子树所有节点的键值，同时保证根节点左右子树的高度相等。这样二叉树高度最小，检索速度最快。它的中序遍历是有序的，另外它也允许出现重复的值。



本题要点：

本题需要保存滑动窗口内的所有元素，可以使用的 C++ 的 multiset/map/set 与 Java 中的 TreeMap。
当频繁的插入和删除元素时，multiset/map 和 TreeMap 等有序的数据结构能够在在 O(log(K))O(log(K))  的时间复杂度内调整 BST，从而维护结构的有序性。
multiset 和 TreeMap 都提供了获取第一个元素和最后一个元素的函数，也就能在 O(1)O(1) 的时间内获取滑动窗口内最小值和最大值。
代码
有了非常高效的数据结构，做这个题已经不难了。我下面的代码演示了用 C++ 的 set/map 和 Python 的 SortedSet 解决本题。

right 指针每次后移，如果发现 set 的大小大于 k ，则需要把 nums[left] 从 set 中删除；
查找 set 中是否有大于等于 nums[right] - t 的元素，如果有的话，说明在大小不超过为 k 的窗口内有绝对值差小于等于 t 的两个元素，返回 true。
如果把 nums 遍历了一遍仍然没有结果，则返回 false。
C++ 代码使用 set，Python 使用 SortedList 的代码如下。

C++Python

class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        from sortedcontainers import SortedSet
        st = SortedSet()
        left, right = 0, 0
        res = 0
        while right < len(nums):
            if right - left > k:
                st.remove(nums[left])
                left += 1
            index = bisect.bisect_left(st, nums[right] - t)
            if st and index >= 0 and index < len(st) and abs(st[index] - nums[right]) <= t:
                return True
            st.add(nums[right])
            right += 1
        return False
C++ 的 map 写法如下：

C++

class Solution {
public:
    bool containsNearbyAlmostDuplicate(vector<int>& nums, int k, int t) {
        map<long long, int> m;
        int left = 0, right = 0;
        while (right < nums.size()) {
            if (right - left > k) {
                m.erase(nums[left]);
                left ++;
            }
            auto a = m.lower_bound((long long) nums[right] - t);
            if (a != m.end() && abs(a->first - nums[right]) <= t) {
                return true;
            }
            m[nums[right]] = right;
            right ++;
        }
        return false;
    }
};
时间复杂度：O(N*log(min(n, k)))O(N∗log(min(n,k)))，每个元素遍历一次，新元素插入红黑树的调整时间为 O(log(x))O(log(x))，set 中最多有 min(n, k)min(n,k) 个元素；
空间复杂度：O(min(n, k))O(min(n,k))。
刷题心得
本题的重点在于快速求滑动窗口内的最大值和最小值。常见的方法有：

使用 multiset、TreeMap等数据结构；
单调递增队列或者单调递减队列；
参考资料：

力扣官方题解
Grandyang
SortedSet

作者：fuxuemingzhu
链接：https://leetcode-cn.com/problems/contains-duplicate-iii/solution/fu-xue-ming-zhu-hua-dong-chuang-kou-mo-b-jnze/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
