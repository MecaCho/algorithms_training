'''
708. 循环有序列表的插入
给定循环升序列表中的一个点，写一个函数向这个列表中插入一个新元素，使这个列表仍然是循环升序的。给定的可以是这个列表中任意一个顶点的指针，并不一定是这个列表中最小元素的指针。

如果有多个满足条件的插入位置，你可以选择任意一个位置插入新的值，插入后整个列表仍然保持有序。

如果列表为空（给定的节点是 null），你需要创建一个循环有序列表并返回这个点。否则。请返回原先给定的节点。

下面的例子可以帮你更好的理解这个问题：





在上图中，有一个包含三个元素的循环有序列表，你获得值为 3 的节点的指针，我们需要向表中插入元素 2。






新插入的节点应该在 1 和 3 之间，插入之后，整个列表如上图所示，最后返回节点 3。


708. Insert into a Sorted Circular Linked List
Given a node from a Circular Linked List which is sorted in ascending order, write a function to insert a value insertVal into the list such that it remains a sorted circular list. The given node can be a reference to any single node in the list, and may not be necessarily the smallest value in the circular list.

If there are multiple suitable places for insertion, you may choose any place to insert the new value. After the insertion, the circular list should remain sorted.

If the list is empty (i.e., given node is null), you should create a new single circular list and return the reference to that single node. Otherwise, you should return the original given node.



Example 1:



Input: head = [3,4,1], insertVal = 2
Output: [3,4,1,2]
Explanation: In the figure above, there is a sorted circular list of three elements. You are given a reference to the node with value 3, and we need to insert 2 into the list. The new node should be inserted between node 1 and node 3. After the insertion, the list should look like this, and we should still return node 3.



Example 2:

Input: head = [], insertVal = 1
Output: [1]
Explanation: The list is empty (given head is null). We create a new single circular list and return the reference to that single node.
Example 3:

Input: head = [1], insertVal = 0
Output: [1,0]


Constraints:

0 <= Number of Nodes <= 5 * 10^4
-10^6 <= Node.val <= 10^6
-10^6 <= insertVal <= 10^6
'''


"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Node(object):
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def insert(self, head, insertVal):
        """
        :type head: Node
        :type insertVal: int
        :rtype: Node
        """
        if not head:
            node = Node(insertVal)
            node.next = node
            return node
        cur = head
        while cur:

            cur_val = cur.val
            next_val = cur.next.val
            if insertVal < next_val < cur_val:
                break
            # print(cur_val <= insertVal <= next_val, cur_val, next_val, insertVal)
            if insertVal <= next_val < cur_val or cur.next == head or cur_val <= insertVal <= next_val or insertVal \
                    >= cur_val > next_val:
                break
            cur = cur.next

        new_node = Node(insertVal)

        new_node.next = cur.next
        cur.next = new_node

        return head


'''
方法一：双指针迭代
尽管问题看起来很简单，但是要编写一个涵盖所有情况的解决方案其实不简单。

通常对于链表的问题，可以采用双指针迭代的方法，用两个指针遍历链表。

用两个指针遍历的原因之一是在单链表中的没有对前继节点的引用，因此我们用一个指针指向当前节点的前继节点。

我们使用 prev 和 curr 两个指针遍历循环链表，当我们找到合适的插入位置时，我们将其插入到 prev 和 curr 之间。



算法：

首先，我们定义双指针迭代的算法框架如下：

我们用 prev 和 curr 两个指针循环遍历链表。循环的终止条件是两个指针返回到起点，即 prev==head。
在每一次迭代过程中，我们都会检查由两个指针限定的位置是否是新值插入的正确位置。
如果不是正确的位置，则两个指针都向前移动一步。现在困难的地方是如何设计出一个简洁的逻辑来处理解决不同的情况。我们分为三个不同的情况。
情况 1： 新节点的值位于当前链表的最小值和最大值之间。因此，应该将其插入到链表中间。



从上面的例子我们可以看到，新值（6）位于链表的最大值和最小值之间（即 1 和 9）之间。无论从哪个节点开始（在本例子中从节点 {3} 开始），新节点最终会被插入到节点 {5} 和 {7} 之间。

我们要找到满足 {prev.val <= insertVal <= curr.val} 条件的位置。

情况 2： 新值超出了链表中的最小值和最大值，即小于最小值或大于最大值。在任一情况下，新值都应插入在尾节点（即链表最大值的节点）之后。





首先我们要在链表中找到相邻节点值下降的位置，即 {prev.val>curr.val} 来找到尾节点。因为节点值是升序排序的，所以尾节点在链表中具有最大的值。

此外，检查新值是大于尾节点的值还是小于头节点的值，分别由 prev 和 curr 指向。

图片 case 2.1 对应于新值大于或等于尾节点值的条件，即 {insertVal>=prev.val}。

图片 case 2.2 对应于新值小于或等于头节点值的条件，即 {insertVal<=curr.val}。

一旦找到头尾节点，就可以通过在头尾节点之间插入新值来扩展链表，即在 prev 和 curr 之间插入新值。

情况 3： 链表的元素的值相同。
尽管在问题描述中没有说明，但是链表可能出现所有节点的值均相同。



在这种情况下，我们最终会遍历链表回到起点。然后我们可以在任一节点后插入新值，那我们不如在入口节点之后插入新值。

注意，我们不能够跳过迭代，因为必须遍历链表来确定链表是否只存在一个唯一的值。

还有一种情况，是当链表为空时，我们可以在进入循环之前解决它。

PythonJava
class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':

        if head == None:
            newNode = Node(insertVal, None)
            newNode.next = newNode
            return newNode
 
        prev, curr = head, head.next
        toInsert = False

        while True:
            
            if prev.val <= insertVal <= curr.val:
                # Case #1.
                toInsert = True
            elif prev.val > curr.val:
                # Case #2. where we locate the tail element
                # 'prev' points to the tail, i.e. the largest element!
                if insertVal >= prev.val or insertVal <= curr.val:
                    toInsert = True

            if toInsert:
                prev.next = Node(insertVal, curr)
                # mission accomplished
                return head

            prev, curr = curr, curr.next
            # loop condition
            if prev == head:
                break
        # Case #3.
        # did not insert the node in the loop
        prev.next = Node(insertVal, curr)
        return head
复杂度分析

时间复杂度：\mathcal{O}(N)O(N)。其中 NN 指的时链表的元素个数。最坏的情况下我们会遍历整个链表。
空间复杂度：\mathcal{O}(1)O(1)，仅仅使用了两个指针。

作者：LeetCode
链接：https://leetcode-cn.com/problems/insert-into-a-sorted-circular-linked-list/solution/xun-huan-you-xu-lie-biao-de-cha-ru-by-leetcode/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''