'''

面试题 02.06. 回文链表
编写一个函数，检查输入的链表是否是回文的。

 

示例 1：

输入： 1->2
输出： false 
示例 2：

输入： 1->2->2->1
输出： true 
 

进阶：
你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？


面试题 02.06. Palindrome Linked List LCCI
Implement a function to check if a linked list is a palindrome.

 
Example 1:

Input:  1->2
Output:  false 
Example 2:

Input:  1->2->2->1
Output:  true 
 

Follow up:
Could you do it in O(n) time and O(1) space?
'''



# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    # def reverseList(self, head):
    #     """
    #     :type head: ListNode
    #     :rtype: ListNode
    #     """
    #     tmp, pre, cur = None, None, head
    #     while cur:
    #         tmp = cur.next
    #         pre, cur.next = cur, pre
    #         cur = tmp

    #     return pre
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # new_head = head
        # reverse_head = self.reverseList(new_head)
        # print(reverse_head, head)
        # if reverse_head == head:
        #     return True
        # return False
        val_list = []
        while head:
            val_list.append(head.val)
            head = head.next
        return val_list[::-1] == val_list
