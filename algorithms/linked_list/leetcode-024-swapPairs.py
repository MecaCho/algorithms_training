'''
24. Swap Nodes in Pairs
Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.

 

Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.

24. 两两交换链表中的节点
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

 

示例:

给定 1->2->3->4, 你应该返回 2->1->4->3.
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        first = ListNode(0)
        first.next = head
        res = first
        second = head
        cur = head
        while cur and cur.next:
            cur = cur.next.next

            first.next = second.next
            first.next.next = second
            second.next = cur

            first = first.next.next
            second = second.next

        return res.next

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution1(object):
    def reverseList(self, head, k):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        t = head
        tmp, pre, cur = None, None, head
        while cur and k > 0:
            tmp = cur.next
            pre, cur.next = cur, pre
            cur = tmp
            k -= 1

        return pre, t

    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        cur = head
        dummy = ListNode(0)
        dummy.next = head
        n = 0
        pre, cur = head, head

        tail = dummy
        while 1:
            if n % k == 0 and n / k > 0:
                fast = cur
                kk = k
                while fast and kk > 0:
                    fast = fast.next
                    kk -= 1
                h, t = self.reverseList(pre, k)
                tail.next = h
                t.next = cur
                pre = cur
                tail = t
            if not cur:
                break
            cur = cur.next
            n += 1
        return dummy.next

    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self.reverseKGroup(head, 2)
        # first = ListNode(0)
        # first.next = head
        # res = first
        # second = head
        # cur = head
        # while cur and cur.next:
        #     cur = cur.next.next

        #     first.next = second.next
        #     first.next.next = second
        #     second.next = cur

        #     first = first.next.next
        #     second = second.next

        # return res.next


# 递归
class Solution2(object):

    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # return self.reverseKGroup(head, 2)

        if not head or not head.next:
            return head
        res = head.next
        head.next = self.swapPairs(res.next)
        res.next = head

        return res

'''
方法一：递归
这个题目要求我们从第一个节点开始两两交换链表中的节点，且要真正的交换节点。

算法：

从链表的头节点 head 开始递归。
每次递归都负责交换一对节点。由 firstNode 和 secondNode 表示要交换的两个节点。
下一次递归则是传递的是下一对需要交换的节点。若链表中还有节点，则继续递归。
交换了两个节点以后，返回 secondNode，因为它是交换后的新头。
在所有节点交换完成以后，我们返回交换后的头，实际上是原始链表的第二个节点。
PythonJava
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def swapPairs(self, head: ListNode) -> ListNode:
        """
        :type head: ListNode
        :rtype: ListNode
        """

        # If the list has no node or has only one node left.
        if not head or not head.next:
            return head

        # Nodes to be swapped
        first_node = head
        second_node = head.next

        # Swapping
        first_node.next  = self.swapPairs(second_node.next)
        second_node.next = first_node

        # Now the head is the second node
        return second_node
复杂度分析

时间复杂度：O(N)O(N)，其中 NN 指的是链表的节点数量。
空间复杂度：O(N)O(N)，递归过程使用的堆栈空间。
方法二：迭代
我们把链表分为两部分，即奇数节点为一部分，偶数节点为一部分，A 指的是交换节点中的前面的节点，B 指的是要交换节点中的后面的节点。在完成它们的交换，我们还得用 prevNode 记录 A 的前驱节点。

算法：

firstNode（即 A） 和 secondNode（即 B） 分别遍历偶数节点和奇数节点，即两步看作一步。
交换两个节点：
 firstNode.next = secondNode.next
 secondNode.next = firstNode
还需要更新 prevNode.next 指向交换后的头。
prevNode.next = secondNode
迭代完成后得到最终的交换结果。
PythonJava
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Dummy node acts as the prevNode for the head node
        # of the list and hence stores pointer to the head node.
        dummy = ListNode(-1)
        dummy.next = head

        prev_node = dummy

        while head and head.next:

            # Nodes to be swapped
            first_node = head;
            second_node = head.next;

            # Swapping
            prev_node.next = second_node
            first_node.next = second_node.next
            second_node.next = first_node

            # Reinitializing the head and prev_node for next swap
            prev_node = first_node
            head = first_node.next

        # Return the new head node.
        return dummy.next
复杂度分析

时间复杂度：O(N)O(N)，其中 NN 指的是链表的节点数量。
空间复杂度：O(1)O(1)。

作者：LeetCode
链接：https://leetcode-cn.com/problems/swap-nodes-in-pairs/solution/liang-liang-jiao-huan-lian-biao-zhong-de-jie-di-19/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''