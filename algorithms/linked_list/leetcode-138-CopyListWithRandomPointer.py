# encoding=utf8

'''
138. Copy List with Random Pointer
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.

The Linked List is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) where random pointer points to, or null if it does not point to any node.
 

Example 1:


Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
Example 2:


Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]
Example 3:



Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]
Example 4:

Input: head = []
Output: []
Explanation: Given linked list is empty (null pointer), so return null.
 

Constraints:

-10000 <= Node.val <= 10000
Node.random is null or pointing to a node in the linked list.
Number of Nodes will not exceed 1000.

138. 复制带随机指针的链表
给定一个链表，每个节点包含一个额外增加的随机指针，该指针可以指向链表中的任何节点或空节点。

要求返回这个链表的 深拷贝。 

我们用一个由 n 个节点组成的链表来表示输入/输出中的链表。每个节点用一个 [val, random_index] 表示：

val：一个表示 Node.val 的整数。
random_index：随机指针指向的节点索引（范围从 0 到 n-1）；如果不指向任何节点，则为  null 。
 

示例 1：



输入：head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
输出：[[7,null],[13,0],[11,4],[10,2],[1,0]]
示例 2：



输入：head = [[1,1],[2,1]]
输出：[[1,1],[2,1]]
示例 3：



输入：head = [[3,null],[3,0],[3,null]]
输出：[[3,null],[3,0],[3,null]]
示例 4：

输入：head = []
输出：[]
解释：给定的链表为空（空指针），因此返回 null。
 

提示：

-10000 <= Node.val <= 10000
Node.random 为空（null）或指向链表中的节点。
节点数目不超过 1000 。
'''





"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return head
        hash_map = {}
        new_head = head
        while new_head:
            node_ = Node(new_head.val, None, None)
            hash_map[new_head] = node_
            new_head = new_head.next

        node = head
        while node:
            value = hash_map[node]
            value.next = hash_map.get(node.next)
            value.random = hash_map.get(node.random)
            node = node.next
        return hash_map[head]

       
       
# solutions

'''
方法一：回溯 + 哈希表
思路及算法

本题要求我们对一个特殊的链表进行深拷贝。如果是普通链表，我们可以直接按照遍历的顺序创建链表节点。而本题中因为随机指针的存在，当我们拷贝节点时，「当前节点的随机指针指向的节点」可能还没创建，因此我们需要变换思路。一个可行方案是，我们利用回溯的方式，让每个节点的拷贝操作相互独立。对于当前节点，我们首先要进行拷贝，然后我们进行「当前节点的后继节点」和「当前节点的随机指针指向的节点」拷贝，拷贝完成后将创建的新节点的指针返回，即可完成当前节点的两指针的赋值。

具体地，我们用哈希表记录每一个节点对应新节点的创建情况。遍历该链表的过程中，我们检查「当前节点的后继节点」和「当前节点的随机指针指向的节点」的创建情况。如果这两个节点中的任何一个节点的新节点没有被创建，我们都立刻递归地进行创建。当我们拷贝完成，回溯到当前层时，我们即可完成当前节点的指针赋值。注意一个节点可能被多个其他节点指向，因此我们可能递归地多次尝试拷贝某个节点，为了防止重复拷贝，我们需要首先检查当前节点是否被拷贝过，如果已经拷贝过，我们可以直接从哈希表中取出拷贝后的节点的指针并返回即可。

在实际代码中，我们需要特别判断给定节点为空节点的情况。

代码

C++JavaC#JavaScriptGolangC

var cachedNode map[*Node]*Node

func deepCopy(node *Node) *Node {
    if node == nil {
        return nil
    }
    if n, has := cachedNode[node]; has {
        return n
    }
    newNode := &Node{Val: node.Val}
    cachedNode[node] = newNode
    newNode.Next = deepCopy(node.Next)
    newNode.Random = deepCopy(node.Random)
    return newNode
}

func copyRandomList(head *Node) *Node {
    cachedNode = map[*Node]*Node{}
    return deepCopy(head)
}
复杂度分析

时间复杂度：O(n)O(n)，其中 nn 是链表的长度。对于每个节点，我们至多访问其「后继节点」和「随机指针指向的节点」各一次，均摊每个点至多被访问两次。

空间复杂度：O(n)O(n)，其中 nn 是链表的长度。为哈希表的空间开销。

方法二：迭代 + 节点拆分
思路及算法

注意到方法一需要使用哈希表记录每一个节点对应新节点的创建情况，而我们可以使用一个小技巧来省去哈希表的空间。

我们首先将该链表中每一个节点拆分为两个相连的节点，例如对于链表 A \rightarrow B \rightarrow CA→B→C，我们可以将其拆分为 A \rightarrow A' \rightarrow B \rightarrow B' \rightarrow C \rightarrow C'A→A 
′
 →B→B 
′
 →C→C 
′
 。对于任意一个原节点 SS，其拷贝节点 S'S 
′
  即为其后继节点。

这样，我们可以直接找到每一个拷贝节点 S'S 
′
  的随机指针应当指向的节点，即为其原节点 SS 的随机指针指向的节点 TT 的后继节点 T'T 
′
 。需要注意原节点的随机指针可能为空，我们需要特别判断这种情况。

当我们完成了拷贝节点的随机指针的赋值，我们只需要将这个链表按照原节点与拷贝节点的种类进行拆分即可，只需要遍历一次。同样需要注意最后一个拷贝节点的后继节点为空，我们需要特别判断这种情况。


1 / 4

代码

C++JavaC#JavaScriptGolangC

func copyRandomList(head *Node) *Node {
    if head == nil {
        return nil
    }
    for node := head; node != nil; node = node.Next.Next {
        node.Next = &Node{Val: node.Val, Next: node.Next}
    }
    for node := head; node != nil; node = node.Next.Next {
        if node.Random != nil {
            node.Next.Random = node.Random.Next
        }
    }
    headNew := head.Next
    for node := head; node != nil; node = node.Next {
        nodeNew := node.Next
        node.Next = node.Next.Next
        if nodeNew.Next != nil {
            nodeNew.Next = nodeNew.Next.Next
        }
    }
    return headNew
}
复杂度分析

时间复杂度：O(n)O(n)，其中 nn 是链表的长度。我们只需要遍历该链表三次。

读者们也可以自行尝试在计算拷贝节点的随机指针的同时计算其后继指针，这样只需要遍历两次。
空间复杂度：O(1)O(1)。注意返回值不计入空间复杂度。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/copy-list-with-random-pointer/solution/fu-zhi-dai-sui-ji-zhi-zhen-de-lian-biao-rblsf/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
