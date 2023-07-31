# encoding=utf8

'''
143. Reorder List
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:

Given 1->2->3->4, reorder it to 1->4->2->3.
Example 2:

Given 1->2->3->4->5, reorder it to 1->5->2->4->3.

143. 重排链表
给定一个单链表 L：L0→L1→…→Ln-1→Ln ，
将其重新排列后变为： L0→Ln→L1→Ln-1→L2→Ln-2→…

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

示例 1:

给定链表 1->2->3->4, 重新排列为 1->4->2->3.
示例 2:

给定链表 1->2->3->4->5, 重新排列为 1->5->2->4->3.

'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return head
        slow = head
        fast = head
        while fast and slow and fast.next:
            fast = fast.next.next
            slow = slow.next

        right = slow.next
        slow.next = None

        pre = None
        cur = right
        while cur:
            tmp = cur.next

            cur.next = pre
            pre = cur
            cur = tmp

        right = pre

        while head and right:
            tmp = head.next
            head.next = right

            tmp1 = right.next
            right.next = tmp

            right = tmp1

            head = head.next.next


class Solution1(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """

        if not head or not head.next:
            return head
        dummy = ListNode(0)
        dummy.next = head
        pre = head
        cur = head
        while cur.next.next:
            cur = cur.next

        last = cur.next
        cur.next = None

        h = self.reorderList(pre.next)

        pre.next = last
        last.next = h

        return dummy.next


# golang版本及题解

'''
package link_list

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func ReorderList(head *ListNode) {
	if head == nil || head.Next == nil {
		return
	}

	var dummy ListNode
	dummy.Next = head
	pre := head
	cur := head
	for cur.Next.Next != nil {
		cur = cur.Next
	}

	last := cur.Next
	cur.Next = nil

	tmp := pre.Next

	ReorderList(tmp)

	pre.Next = last
	last.Next = tmp

}

func reorderList2(head *ListNode) {

	if head == nil || head.Next == nil {
		return
	}

	fast := head
	slow := head

	for fast != nil && fast.Next != nil && slow != nil {
		fast = fast.Next.Next
		slow = slow.Next
	}

	right := slow.Next

	slow.Next = nil

	var pre *ListNode
	cur := right
	for cur != nil {
		tmp := cur.Next
		cur.Next = pre
		pre = cur
		cur = tmp
	}

	right = pre

	for head != nil && right != nil {
		tmp := head.Next
		head.Next = right

		tmp1 := right.Next
		right.Next = tmp
		right = tmp1
		head = head.Next.Next
	}
}

func ReorderList1(head *ListNode) {
	if head == nil || head.Next == nil {
		return
	}

	fast := head
	slow := head

	for fast != nil && fast.Next != nil && slow != nil {
		fast = fast.Next.Next
		slow = slow.Next
	}

	right := slow.Next

	slow.Next = nil

	right = reverseList(right)

	for head != nil && right != nil {
		tmp := head.Next
		head.Next = right

		tmp1 := right.Next
		right.Next = tmp
		right = tmp1
		head = head.Next.Next
	}

}

// 递归解法，找到最后一个节点连接到第一个节点后面，中间部分递归处理，该方法在Python会超时
//
// /**
// * Definition for singly-linked list.
// * type ListNode struct {
// *     Val int
// *     Next *ListNode
// * }
// */
// func ReorderList(head *ListNode) {
// 	if head == nil || head.Next == nil {
// 		return
// 	}
//
// 	var dummy ListNode
// 	dummy.Next = head
// 	pre := head
// 	cur := head
// 	for cur.Next.Next != nil {
// 		cur = cur.Next
// 	}
//
// 	last := cur.Next
// 	cur.Next = nil
//
// 	tmp := pre.Next
//
// 	ReorderList(tmp)
//
// 	pre.Next = last
// 	last.Next = tmp
//
// }
// 1.快慢指针找到中间节点，
// 2.对后半部分反转，
// 3.然后拼接前后两个部分
//
// func reorderList2(head *ListNode)  {
//
// 	if head == nil || head.Next == nil {
// 		return
// 	}
//
//
//    // 1.快慢指针找到中间节点，
// 	fast := head
// 	slow := head
//
// 	for fast != nil && fast.Next != nil && slow != nil {
// 		fast = fast.Next.Next
// 		slow = slow.Next
// 	}
//
// 	right := slow.Next
//
// 	slow.Next = nil
//
//    //2.对后半部分反转
// 	var pre *ListNode
// 	cur := right
// 	for cur != nil {
// 		tmp := cur.Next
// 		cur.Next = pre
// 		pre = cur
// 		cur = tmp
// 	}
//
// 	right = pre
//    // 3.然后拼接前后两个部分
// 	for head != nil && right != nil {
// 		tmp := head.Next
// 		head.Next = right
//
// 		tmp1 := right.Next
// 		right.Next = tmp
// 		right = tmp1
// 		head = head.Next.Next
// 	}
// }
//
// 作者：qiuwenqi
// 链接：https://leetcode-cn.com/problems/reorder-list/solution/golangliang-chong-fang-fa-di-gui-he-die-dai-by-qiu/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

'''
