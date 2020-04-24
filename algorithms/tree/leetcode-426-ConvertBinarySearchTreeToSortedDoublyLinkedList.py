
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



'''
如何遍历树
总的来说，有两种遍历树的策略：

深度优先搜索 (DFS)

在深度优先搜索中，我们以 深度 优先，从根开始先抵达某个叶子，再回退以前往下一个分支。

深度优先搜索又可以根据根节点、左子结点和右子结点的顺序关系分为前序遍历，中序遍历和后序遍历。

广度优先搜索 (BFS)

逐层扫描整棵树，按照高度顺序自顶向下。上层的结点比下层更先访问。

下图表示了不同策略下的访问顺序，请按照 1-2-3-4-5 的顺序来比较不同的策略。



由于原地的要求，本问题需要使用深度优先搜索的中序遍历，利用备忘录法实现。




方法一：递归
算法

标准的中序遍历采用 左 -> 根 -> 右 的顺序，其中 左 和 右 的部分调用递归。

本题的处理在于将前一个结点与当前结点链接，因此，必须跟踪最后一个结点，该结点在新的双向链表中是当前最大的。



另外一个细节：我们也需要保留第一个，也就是最小的结点，以完成闭环。

下面是具体算法：

将 first 和 last 结点 初始化为 null。

调用标准中序遍历 helper(root) :

若结点不为 null :

调用左子树递归 helper(node.left)。

若 last 结点不为空，将 last 与当前的 node 链接。

否则初始化 first 结点。

将当前结点标记为最后 : last = node.

调用右子树递归 helper(node.right)。

将最前与最后的结点链接完成闭环，返回 first 。

实现


4 / 9

PythonC++Java
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        def helper(node):
            """
            Performs standard inorder traversal:
            left -> node -> right
            and links all nodes into DLL
            """
            nonlocal last, first
            if node:
                # left
                helper(node.left)
                # node 
                if last:
                    # link the previous node (last)
                    # with the current one (node)
                    last.right = node
                    node.left = last
                else:
                    # keep the smallest node
                    # to close DLL later on
                    first = node        
                last = node
                # right
                helper(node.right)
        
        if not root:
            return None
        
        # the smallest (first) and the largest (last) nodes
        first, last = None, None
        helper(root)
        # close DLL
        last.right = first
        first.left = last
        return first
复杂度分析

时间复杂度：{O}(N)O(N)，每个结点被处理一次。
空间复杂度：{O}(N)O(N)。需要树高度大小的递归栈，最好情况（平衡树）为 {O}(\log N)O(logN)，最坏情况下（完全不平衡）为 O(N)O(N)。

作者：LeetCode
链接：https://leetcode-cn.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/solution/jiang-er-cha-sou-suo-shu-zhuan-hua-wei-pai-xu-de-s/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''