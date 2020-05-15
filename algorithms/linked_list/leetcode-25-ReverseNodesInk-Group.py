'''
25. K 个一组翻转链表
给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。

k 是一个正整数，它的值小于或等于链表的长度。

如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。



示例：

给你这个链表：1->2->3->4->5

当 k = 2 时，应当返回: 2->1->4->3->5

当 k = 3 时，应当返回: 3->2->1->4->5



说明：

你的算法只能使用常数的额外空间。
你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。


25. Reverse Nodes in k-Group
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

Example:

Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5

Note:

Only constant extra memory is allowed.
You may not alter the values in the list's nodes, only nodes itself may be changed.
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
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


'''
方法一：模拟
思路与算法

本题的目标非常清晰易懂，不涉及复杂的算法，但是实现过程中需要考虑的细节比较多，容易写出冗长的代码。主要考察面试者设计的能力。

我们需要把链表结点按照 k 个一组分组，所以可以使用一个指针 head 依次指向每组的头结点。这个指针每次向前移动 k 步，直至链表结尾。对于每个分组，我们先判断它的长度是否大于等于 k。若是，我们就翻转这部分链表，否则不需要翻转。

接下来的问题就是如何翻转一个分组内的子链表。翻转一个链表并不难，过程可以参考 206. 反转链表。但是对于一个子链表，除了翻转其本身之外，还需要将子链表的头部与上一个子链表连接，以及子链表的尾部与下一个子链表连接。如下图所示：



因此，在翻转子链表的时候，我们不仅需要子链表头结点 head，还需要有 head 的上一个结点 pre，以便翻转完后把子链表再接回 pre。

但是对于第一个子链表，它的头结点 head 前面是没有结点 pre 的。太麻烦了！难道只能特判了吗？答案是否定的。没有条件，我们就创造条件；没有结点，我们就创建一个结点。我们新建一个结点，把它接到链表的头部，让它作为 pre 的初始值，这样 head 前面就有了一个结点，我们就可以避开链表头部的边界条件。这么做还有一个好处，下面我们会看到。

反复移动指针 head 与 pre，对 head 所指向的子链表进行翻转，直到结尾，我们就得到了答案。下面我们该返回函数值了。

有的同学可能发现这又是一件麻烦事：链表翻转之后，链表的头结点发生了变化，那么应该返回哪个结点呢？照理来说，前 k 个结点翻转之后，链表的头结点应该是第 k 个结点。那么要在遍历过程中记录第 k 个结点吗？但是如果链表里面没有 k 个结点，答案又还是原来的头结点。我们又多了一大堆循环和判断要写，太崩溃了！

等等！还记得我们创建了节点 pre吗？这个结点一开始被连接到了头结点的前面，而无论之后链表有没有翻转，它的 next 指针都会指向正确的头结点。那么我们只要返回它的下一个结点就好了。至此，问题解决。


1 / 19

Python3C++JavaScriptGolang
class Solution:
    # 翻转一个子链表，并且返回新的头与尾
    def reverse(self, head: ListNode, tail: ListNode):
        prev = tail.next
        p = head
        while prev != tail:
            nex = p.next
            p.next = prev
            prev = p
            p = nex
        return tail, head

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        hair = ListNode(0)
        hair.next = head
        pre = hair

        while head:
            tail = pre
            # 查看剩余部分长度是否大于等于 k
            for i in range(k):
                tail = tail.next
                if not tail:
                    return hair.next
            nex = tail.next
            head, tail = self.reverse(head, tail)
            # 把子链表重新接回原链表
            pre.next = head
            tail.next = nex
            pre = tail
            head = tail.next
        
        return hair.next
复杂度分析

时间复杂度：O(n)O(n)，其中 nn 为链表的长度。head 指针会在 O(\lfloor \frac{n}{k} \rfloor)O(⌊ 
k
n
​	
 ⌋) 个结点上停留，每次停留需要进行一次 O(k)O(k) 的翻转操作。

空间复杂度：O(1)O(1)，我们只需要建立常数个变量。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/reverse-nodes-in-k-group/solution/k-ge-yi-zu-fan-zhuan-lian-biao-by-leetcode-solutio/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''