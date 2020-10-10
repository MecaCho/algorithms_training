'''
142. 环形链表 II
给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。

为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。

说明：不允许修改给定的链表。



示例 1：

输入：head = [3,2,0,-4], pos = 1
输出：tail connects to node index 1
解释：链表中有一个环，其尾部连接到第二个节点。


示例 2：

输入：head = [1,2], pos = 0
输出：tail connects to node index 0
解释：链表中有一个环，其尾部连接到第一个节点。


示例 3：

输入：head = [1], pos = -1
输出：no cycle
解释：链表中没有环。




进阶：
你是否可以不用额外空间解决此题？

142. Linked List Cycle II
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

Note: Do not modify the linked list.



Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.


Example 2:

Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.


Example 3:

Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.




Follow-up:
Can you solve it without using extra space?
'''

# 哈希表

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        node_map = {}
        while head:
            if head in node_map:
                return head
            else:
                node_map[head] = head
            head = head.next
        return None


# 双指针

class Solution1(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        slow = head
        fast = head

        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        if not slow or not fast or not fast.next :
            return None
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        # print(fast)
        return slow


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution20201010(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        seen = {}
        while head:
            if seen.get(head):
                return head
            seen[head]= 1
            head = head.next
        return None


# solutions

'''
方法 1：哈希表
想法

如果我们用一个 Set 保存已经访问过的节点，我们可以遍历整个列表并返回第一个出现重复的节点。

算法

首先，我们分配一个 Set 
去保存所有的列表节点。我们逐一遍历列表，检查当前节点是否出现过，如果节点已经出现过，那么一定形成了环且它是环的入口。否则如果有其他点是环的入口，我们应该先访问到其他节点而不是这个节点。其他情况，没有成环则直接返回 null 。

算法会在遍历有限个节点后终止，这是因为输入列表会被分成两类：成环的和不成环的。一个不成欢的列表在遍历完所有节点后会到达 null - 即链表的最后一个元素后停止。一个成环列表可以想象成是一个不成环列表将最后一个 null 元素换成环的入口。

如果 while 循环终止，我们返回 null 因为我们已经将所有的节点遍历了一遍且没有遇到重复的节点，这种情况下，列表是不成环的。对于循环列表， while 循环永远不会停止，但在某个节点上， if 条件会被满足并导致函数的退出。

JavaPython

public class Solution {
    public ListNode detectCycle(ListNode head) {
        Set<ListNode> visited = new HashSet<ListNode>();

        ListNode node = head;
        while (node != null) {
            if (visited.contains(node)) {
                return node;
            }
            visited.add(node);
            node = node.next;
        }

        return null;
    }
}
复杂度分析

时间复杂度：O(n)O(n)

不管是成环还是不成环的输入，算法肯定都只会访问每个节点一次。对于非成环列表这是显而易见的，因为第 nn 个节点指向 null ，这会让循环退出。对于循环列表， if 
条件满足时会导致函数的退出，因为它指向了某个已经访问过的节点。两种情况下，访问的节点数最多都是 nn 个，所以运行时间跟节点数目成线性关系。

空间复杂度：O(n)O(n)

不管成环或者不成欢的输入，我们都需要将每个节点插入 Set 中一次。两者唯一的区别是最后访问的节点后是 null 还是一个已经访问过的节点。因此，由于 Set 包含 nn 个不同的节点，所需空间与节点数目也是线性关系的。



方法 2：Floyd 算法
想法

当然一个跑得快的人和一个跑得慢的人在一个圆形的赛道上赛跑，会发生什么？在某一个时刻，跑得快的人一定会从后面赶上跑得慢的人。

算法

Floyd 的算法被划分成两个不同的 阶段 。在第一阶段，找出列表中是否有环，如果没有环，可以直接返回 null 并退出。否则，用 相遇节点 来找到环的入口。

阶段 1

这里我们初始化两个指针 - 快指针和慢指针。我们每次移动慢指针一步、快指针两步，直到快指针无法继续往前移动。如果在某次移动后，快慢指针指向了同一个节点，我们就返回它。否则，我们继续，直到 while 
循环终止且没有返回任何节点，这种情况说明没有成环，我们返回 null 。

下图说明了这个算法的工作方式：



环中的节点从 0 到 C-1C−1 编号，其中 CC 是环的长度。非环节点从 -F−F 到 -1−1 编号，其中 FF 是环以外节点的数目。 FF 次迭代以后，慢指针指向了 0 且快指针指向某个节点 hh ，其中 F \equiv h 
\pmod CF≡h(modC) 。这是因为快指针在 FF 次迭代中遍历了 2F2F 个节点，且恰好有 FF 个在环中。继续迭代 C-hC−h 次，慢指针显然指向第 C-hC−h 号节点，而快指针也会指向相同的节点。原因在于，快指针从 
hh 号节点出发遍历了 2(C-h)2(C−h) 个节点。

\begin{aligned} h + 2(C-h) &= 2C - h \\ &\equiv C-h \pmod C \end{aligned}
h+2(C−h)
​	

=2C−h
≡C−h(modC)
​	


因此，如果列表是有环的，快指针和慢指针最后会同时指向同一个节点，因此被称为 相遇 。

阶段 2

给定阶段 1 找到的相遇点，阶段 2 将找到环的入口。首先我们初始化额外的两个指针： ptr1 ，指向链表的头， ptr2 指向相遇点。然后，我们每次将它们往前移动一步，直到它们相遇，它们相遇的点就是环的入口，返回这个节点。

下面的图将更好的帮助理解和证明这个方法的正确性。



我们利用已知的条件：慢指针移动 1 步，快指针移动 2 步，来说明它们相遇在环的入口处。（下面证明中的 tortoise 表示慢指针，hare 表示快指针）

\begin{aligned} 2 \cdot distance(tortoise) &= distance(hare) \\ 2(F+a) &= F+a+b+a \\ 2F+2a &= F+2a+b \\ F &= b \\ 
\end{aligned}
2⋅distance(tortoise)
2(F+a)
2F+2a
F
​	

=distance(hare)
=F+a+b+a
=F+2a+b
=b
​	


因为 F=bF=b ，指针从 hh 点出发和从链表的头出发，最后会遍历相同数目的节点后在环的入口处相遇。

下面的动画中动态地演示了整个算法过程：


1 / 13

JavaPython

class Solution(object):
    def getIntersect(self, head):
        tortoise = head
        hare = head

        # A fast pointer will either loop around a cycle and meet the slow
        # pointer or reach the `null` at the end of a non-cyclic list.
        while hare is not None and hare.next is not None:
            tortoise = tortoise.next
            hare = hare.next.next
            if tortoise == hare:
                return tortoise

        return None

    def detectCycle(self, head):
        if head is None:
            return None

        # If there is a cycle, the fast/slow pointers will intersect at some
        # node. Otherwise, there is no cycle, so we cannot find an e***ance to
        # a cycle.
        intersect = self.getIntersect(head)
        if intersect is None:
            return None

        # To find the e***ance to the cycle, we have two pointers traverse at
        # the same speed -- one from the front of the list, and the other from
        # the point of intersection.
        ptr1 = head
        ptr2 = intersect
        while ptr1 != ptr2:
            ptr1 = ptr1.next
            ptr2 = ptr2.next

        return ptr1

复杂度分析

时间复杂度：O(n)O(n)

对有环列表，快指针和慢指针在 F+C-hF+C−h 次迭代以后会指向同一个节点，正如上面正确性证明所示， F+C-h \leq F+C = nF+C−h≤F+C=n ，所以阶段 1 运行时间在 O(n)O(n) 时间以内，阶段 2 
运行 F < nF<n 次迭代，所以它运行时间也在 O(n)O(n) 以内。

对于无环链表，快指针大约需要迭代 \dfrac{n}{2} 
2
n
​	
  次会抵达链表的尾部，这样不会进入阶段 2 就直接退出。

因此，不管是哪一类链表，都会在与节点数成线性关系的时间内运行完。

空间复杂度：O(1)O(1)

Floyd 的快慢指针算法仅需要几个指针，所以只需常数级别的额外空间。

作者：LeetCode
链接：https://leetcode-cn.com/problems/linked-list-cycle-ii/solution/huan-xing-lian-biao-ii-by-leetcode/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''

# solutions

'''
解题思路：
这类链表题目一般都是使用双指针法解决的，例如寻找距离尾部第K个节点、寻找环入口、寻找公共尾部入口等。
算法流程：
双指针第一次相遇： 设两指针 fast，slow 指向链表头部 head，fast 每轮走 22 步，slow 每轮走 11 步；

第一种结果： fast 指针走过链表末端，说明链表无环，直接返回 null；

TIPS: 若有环，两指针一定会相遇。因为每走 11 轮，fast 与 slow 的间距 +1+1，fast 终会追上 slow；
第二种结果： 当fast == slow时， 两指针在环中 第一次相遇 。下面分析此时fast 与 slow走过的 步数关系 ：

设链表共有 a+ba+b 个节点，其中 链表头部到链表入口 有 aa 个节点（不计链表入口节点）， 链表环 有 bb 个节点（这里需要注意，aa 和 bb 是未知数，例如图解上链表 a=4a=4 , b=5b=5）；设两指针分别走了 
ff，ss 步，则有：
fast 走的步数是slow步数的 22 倍，即 f = 2sf=2s；（解析： fast 每轮走 22 步）
fast 比 slow多走了 nn 个环的长度，即 f = s + nbf=s+nb；（ 解析： 双指针都走过 aa 步，然后在环内绕圈直到重合，重合时 fast 比 slow 多走 环的长度整数倍 ）；
以上两式相减得：f = 2nbf=2nb，s = nbs=nb，即fast和slow 指针分别走了 2n2n，nn 个 环的周长 （注意： nn 是未知数，不同链表的情况不同）。
目前情况分析：

如果让指针从链表头部一直向前走并统计步数k，那么所有 走到链表入口节点时的步数 是：k=a+nb（先走 aa 步到入口节点，之后每绕 11 圈环（ bb 步）都会再次到入口节点）。
而目前，slow 指针走过的步数为 nbnb 步。因此，我们只要想办法让 slow 再走 aa 步停下来，就可以到环的入口。
但是我们不知道 aa 的值，该怎么办？依然是使用双指针法。我们构建一个指针，此指针需要有以下性质：此指针和slow 一起向前走 a 步后，两者在入口节点重合。那么从哪里走到入口节点需要 aa 步？答案是链表头部head。
双指针第二次相遇：

slow指针 位置不变 ，将fast指针重新 指向链表头部节点 ；slow和fast同时每轮向前走 11 步；
TIPS：此时 f = 0f=0，s = nbs=nb ；
当 fast 指针走到f = af=a 步时，slow 指针走到步s = a+nbs=a+nb，此时 两指针重合，并同时指向链表环入口 。
返回slow指针指向的节点。

复杂度分析：
时间复杂度 O(N)O(N) ：第二次相遇中，慢指针须走步数 a < a + ba<a+b；第一次相遇中，慢指针须走步数 a + b - x < a + ba+b−x<a+b，其中 xx 为双指针重合点与环入口距离；因此总体为线性复杂度；
空间复杂度 O(1)O(1) ：双指针使用常数大小的额外空间。

1 / 11

代码：
PythonJava

class Solution(object):
    def detectCycle(self, head):
        fast, slow = head, head
        while True:
            if not (fast and fast.next): return
            fast, slow = fast.next.next, slow.next
            if fast == slow: break
        fast = head
        while fast != slow:
            fast, slow = fast.next, slow.next
        return fast

'''