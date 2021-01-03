# encoding=utf8

'''
面试题 02.04. 分割链表
编写程序以 x 为基准分割链表，使得所有小于 x 的节点排在大于或等于 x 的节点之前。如果链表中包含 x，x 只需出现在小于 x 的元素之后(如下所示)。分割元素 x 只需处于“右半部分”即可，其不需要被置于左右两部分之间。

示例:

输入: head = 3->5->8->5->10->2->1, x = 5
输出: 3->1->2->10->5->5->8

面试题 02.04. Partition List LCCI
Write code to partition a linked list around a value x, such that all nodes less than x come before all nodes greater than or equal to x. If x is contained within the list, the values of x only need to be after the elements less than x (see below). The partition element x can appear anywhere in the "right partition"; it does not need to appear between the left and right partitions.

Example:

Input: head = 3->5->8->5->10->2->1, x = 5
Output: 3->1->2->10->5->5->8
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """

        cur = head
        low = ListNode(0)
        high = ListNode(0)

        # low.next = head
        # high.next = head

        low_ = low
        high_ = high

        while cur:
            # print(cur.val)
            if cur.val >= x:
                high.next = cur
                high = high.next
            else:
                low.next = cur
                low = low.next
            cur = cur.next

        low.next = None
        high.next = None

        low.next = high_.next

        return low_.next

# golang solutions

'''
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func partition(head *ListNode, x int) *ListNode {

    cur := head
    low := &ListNode{0, nil}
    // low.Next = head
    high := &ListNode{0, nil}

    low_, high_ := low, high

    for cur != nil{
        if cur.Val >= x{
            high.Next = cur
            high = high.Next
        }else{
            low.Next = cur
            low = low.Next
        }
        cur = cur.Next
    }
    low.Next = nil
    high.Next = nil

    low.Next = high_.Next

    return low_.Next

}
'''

# tips

'''
这个问题有很多解法，其中大部分都有最优的运行时间。有些代码比其他代码更短，更干净。你可以想出不同的解法吗？

考虑元素不必保持相同的相对顺序。我们只需要确保小于基准点的元素必须位于比基准点大的元素之前。这有助于你想出更多的解法吗？
'''