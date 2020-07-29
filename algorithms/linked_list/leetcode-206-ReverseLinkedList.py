
'''
206. Reverse Linked List
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?

206. 反转链表
反转一个单链表。

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
进阶:
你可以迭代或递归地反转链表。你能否用两种方法解决这道题？

```
1.迭代
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        tmp, pre, cur = None, None, head
        while cur:
            tmp = cur.next
            pre, cur.next = cur, pre
            cur = tmp

        return pre

'''2.递归'''

class Solution1(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        p = self.reverseList(head.next)

        head.next.next = head
        head.next = None

        return p

# golang

'''

// 递归

type ListNode struct {
	Val  int
	Next *ListNode
}

func reverseList(head *ListNode) *ListNode {

	if head == nil || head.Next == nil {
		return head
	}

	p := reverseList(head.Next)

	head.Next.Next = head
	head.Next = nil

	return p

}

// 迭代
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func reverseList(head *ListNode) *ListNode {
	var pre *ListNode
	cur := head
	for cur != nil {
		tmp := cur.Next
		cur.Next = pre
		pre = cur
		cur = tmp
	}
    
	return pre

}
'''


# reverse linked list k

# 1 2 3 4 5 6 7
# 7 4 5 6 1 2 3


def reverse_linked_list(head):
    if not head:
        return head
    pre, cur = None, head
    while cur:
        tmp = cur.next
        pre, cur.next = cur, pre
        cur = tmp
    return pre


def reverse_linked_list_k(head, k):
    i = 0
    pre = head
    k_lists = []
    while head:
        if i % k == 0:
            k_lists.append(pre)
            pre = head
        i += 1
        head = head.next
    res = k_lists[-1]
    length = len(k_lists)

    for i in range(length - 1, 1, -1):
        # //k
        k_lists[i].next.next.next = k_lists[i - 1]  # k
    return res


test_cases = []
