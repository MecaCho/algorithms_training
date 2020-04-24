
'''
426. 将二叉搜索树转化为排序的双向链表
将一个 二叉搜索树 就地转化为一个 已排序的双向循环链表 。

对于双向循环列表，你可以将左右孩子指针作为双向循环链表的前驱和后继指针，第一个节点的前驱是最后一个节点，最后一个节点的后继是第一个节点。

特别地，我们希望可以 就地 完成转换操作。当转化完成以后，树中节点的左指针需要指向前驱，树中节点的右指针需要指向后继。还需要返回链表中最小元素的指针。



示例 1：

输入：root = [4,2,5,1,3]

输出：[1,2,3,4,5]

解释：下图显示了转化后的二叉搜索树，实线表示后继关系，虚线表示前驱关系。

示例 2：

输入：root = [2,1,3]
输出：[1,2,3]
示例 3：

输入：root = []
输出：[]
解释：输入是空树，所以输出也是空链表。
示例 4：

输入：root = [1]
输出：[1]


提示：

-1000 <= Node.val <= 1000
Node.left.val < Node.val < Node.right.val
Node.val 的所有值都是独一无二的
0 <= Number of Nodes <= 2000

426. Convert Binary Search Tree to Sorted Doubly Linked List
Convert a Binary Search Tree to a sorted Circular Doubly-Linked List in place.

You can think of the left and right pointers as synonymous to the predecessor and successor pointers in a doubly-linked list. For a circular doubly linked list, the predecessor of the first element is the last element, and the successor of the last element is the first element.

We want to do the transformation in place. After the transformation, the left pointer of the tree node should point to its predecessor, and the right pointer should point to its successor. You should return the pointer to the smallest element of the linked list.



Example 1:



Input: root = [4,2,5,1,3]


Output: [1,2,3,4,5]

Explanation: The figure below shows the transformed BST. The solid line indicates the successor relationship, while the dashed line means the predecessor relationship.

Example 2:

Input: root = [2,1,3]
Output: [1,2,3]
Example 3:

Input: root = []
Output: []
Explanation: Input is an empty tree. Output is also an empty Linked List.
Example 4:

Input: root = [1]
Output: [1]


Constraints:

-1000 <= Node.val <= 1000
Node.left.val < Node.val < Node.right.val
All values of Node.val are unique.
0 <= Number of Nodes <= 2000
'''



"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None
        self.vals = []
        def m_trave(root):
            if not root:
                return
            m_trave(root.left)
            self.vals.append(root.val)
            if self.cur:
                self.cur.right, root.left = root, self.cur
            else:
                self.head = root
            self.cur = root
            m_trave(root.right)

        self.head = None
        self.cur = None
        m_trave(root)
        self.head.left, self.cur.right = self.cur, self.head

        return self.head
