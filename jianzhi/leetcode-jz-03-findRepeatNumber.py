'''
面试题03. 数组中重复的数字
找出数组中重复的数字。


在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。

示例 1：

输入：
[2, 3, 1, 0, 2, 5, 3]
输出：2 或 3


限制：

2 <= n <= 100000
'''


class Solution(object):
    def findRepeatNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 排序；O(nlgn);O(1)
        nums = sorted(nums)
        pre = None
        for i in range(len(nums)):
            if pre == nums[i]:
                return pre
            pre = nums[i]


        # 哈希表；O(n);O(n)
        # hash_map = {}
        # for num in nums:
        #     if num in hash_map:
        #         return num
        #     else:
        #         hash_map[num] = 1

        # ；O(n);O(1)
        # for i in range(len(nums)):
        #     while i != nums[i]:
        #         if nums[nums[i]] == nums[i]:
        #             return nums[i]
        #         nums[nums[i]], nums[i] = nums[i], nums[nums[i]]


class Solution1(object):
    def findRepeatNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hash_map = {}
        for num in nums:
            if num in hash_map:
                return num
            else:
                hash_map[num] = 1

'''
方法一：遍历数组
由于只需要找出数组中任意一个重复的数字，因此遍历数组，遇到重复的数字即返回。为了判断一个数字是否重复遇到，使用集合存储已经遇到的数字，如果遇到的一个数字已经在集合中，则当前的数字是重复数字。

初始化集合为空集合，重复的数字 repeat = -1
遍历数组中的每个元素：
将该元素加入集合中，判断是否添加成功
如果添加失败，说明该元素已经在集合中，因此该元素是重复元素，将该元素的值赋给 repeat，并结束遍历
返回 repeat
Java

class Solution {
    public int findRepeatNumber(int[] nums) {
        Set<Integer> set = new HashSet<Integer>();
        int repeat = -1;
        for (int num : nums) {
            if (!set.add(num)) {
                repeat = num;
                break;
            }
        }
        return repeat;
    }
}
复杂性分析

时间复杂度：O(n)O(n)。
遍历数组一遍。使用哈希集合（HashSet），添加元素的时间复杂度为 O(1)O(1)，故总的时间复杂度是 O(n)O(n)。
空间复杂度：O(n)O(n)。不重复的每个元素都可能存入集合，因此占用 O(n)O(n) 额外空间。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof/solution/mian-shi-ti-03-shu-zu-zhong-zhong-fu-de-shu-zi-b-4/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''