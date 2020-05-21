'''
打家劫舍 II

你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都围成一圈，这意味着第一个房屋和最后一个房屋是紧挨着的。同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。

示例 1:

输入: [2,3,2]
输出: 3
解释: 你不能先偷窃 1 号房屋（金额 = 2），然后偷窃 3 号房屋（金额 = 2）, 因为他们是相邻的。
示例 2:

输入: [1,2,3,1]
输出: 4
解释: 你可以先偷窃 1 号房屋（金额 = 1），然后偷窃 3 号房屋（金额 = 3）。
     偷窃到的最高金额 = 1 + 3 = 4 。
'''


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def new_rob(nums):
            if not nums:
                return 0
            dp = [[0, nums[0]]]
            for i in range(1, len(nums)):
                dp.append([0, 0])
                dp[i][0] = max(dp[i -1])
                dp[i][1] = max(dp[i -1][0] + nums[i], dp[i -1][1])
            return max(dp[-1])
        length = len(nums)
        if length == 0:
            return 0
        elif length == 1:
            return nums[0]
        return max(new_rob(nums[1:]), new_rob(nums[:length -1]))
        # if not nums:
        #     return 0
        # # dp = [num for num in nums]
        # # for i in range(len(nums)-1):
        # #     if i > 1:
        # #         dp[i] = max(dp[i-1], dp[i-2]+nums[i])
        # # if len(nums) > 3:
        # #     i = len(nums) - 1
        # #     if len(nums) % 2 == 1:
        # #         dp[i] = max(dp[i-1], dp[i-2]+nums[i]-nums[0])
        # #     else:
        # #        dp[i] = max(dp[i-1], dp[i-2]+nums[i])
        # # dp = [for num in nums]
        # dp = [[0, nums[0]]]
        # for i in range(1, len(nums)):
        #     dp.append([0, 0])
        #     dp[i][0] = max(dp[i-1])
        #     dp[i][1] = max(dp[i-1][0] + nums[i], dp[i-1][1])
        # return max(dp[-1])

        # [1,3,1,3,100]
        # [1,2,3,1]


        # return max(dp)


'''
只出现一次的数字 II

给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现了三次。找出那个只出现了一次的元素。

说明：

你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

示例 1:

输入: [2,2,3,2]
输出: 3
示例 2:

输入: [0,1,0,1,0,1,99]
输出: 99
'''


class Solution1(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # res = 0
        # nums = nums * 3
        # print(nums)
        # for num in nums:
        #     res ^= num
        # return (res * 3 - sum(nums)) / 2
        return (sum(list(set(nums))) * 3 - sum(nums)) / 2


'''
环形链表

给定一个链表，判断链表中是否有环。

为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。

 

示例 1：

输入：head = [3,2,0,-4], pos = 1
输出：true
解释：链表中有一个环，其尾部连接到第二个节点。


示例 2：

输入：head = [1,2], pos = 0
输出：true
解释：链表中有一个环，其尾部连接到第一个节点。


示例 3：

输入：head = [1], pos = -1
输出：false
解释：链表中没有环。


 

进阶：

你能用 O(1)（即，常量）内存解决此问题吗？
'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution2(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
