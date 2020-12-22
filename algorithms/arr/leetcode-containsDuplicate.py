# encoding=utf-8
'''
217. Contains Duplicate
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

Example 1:

Input: [1,2,3,1]
Output: true
Example 2:

Input: [1,2,3,4]
Output: false
Example 3:

Input: [1,1,1,3,3,4,3,2,4,2]
Output: true

存在重复元素
给定一个整数数组，判断是否存在重复元素。

如果任何值在数组中出现至少两次，函数返回 true。如果数组中每个元素都不相同，则返回 false。

示例 1:

输入: [1,2,3,1]
输出: true
示例 2:

输入: [1,2,3,4]
输出: false
示例 3:

输入: [1,1,1,3,3,4,3,2,4,2]
输出: true
'''


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(set(nums)) != len(nums)


class Solution20201213(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(set(nums)) != len(nums)


# solution

'''
方法一：排序
在对数字从小到大排序之后，数组的重复元素一定出现在相邻位置中。因此，我们可以扫描已排序的数组，每次判断相邻的两个元素是否相等，如果相等则说明存在重复的元素。

C++JavaGolangCJavaScript

func containsDuplicate(nums []int) bool {
    sort.Ints(nums)
    for i := 1; i < len(nums); i++ {
        if nums[i] == nums[i-1] {
            return true
        }
    }
    return false
}
复杂度分析

时间复杂度：O(N\log N)O(NlogN)，其中 NN 为数组的长度。需要对数组进行排序。

空间复杂度：O(\log N)O(logN)，其中 NN 为数组的长度。注意我们在这里应当考虑递归调用栈的深度。

方法二：哈希表
对于数组中每个元素，我们将它插入到哈希表中。如果插入一个元素时发现该元素已经存在于哈希表中，则说明存在重复的元素。

C++JavaGolangCJavaScript

func containsDuplicate(nums []int) bool {
    set := map[int]struct{}{}
    for _, v := range nums {
        if _, has := set[v]; has {
            return true
        }
        set[v] = struct{}{}
    }
    return false
}
复杂度分析

时间复杂度：O(N)O(N)，其中 NN 为数组的长度。

空间复杂度：O(N)O(N)，其中 NN 为数组的长度。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/contains-duplicate/solution/cun-zai-zhong-fu-yuan-su-by-leetcode-sol-iedd/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
