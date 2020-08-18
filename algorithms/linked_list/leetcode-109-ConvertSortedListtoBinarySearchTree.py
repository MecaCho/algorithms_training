'''
109. Convert Sorted List to Binary Search Tree
Given the head of a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.



Example 1:


Input: head = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: One possible answer is [0,-3,9,-10,null,5], which represents the shown height balanced BST.
Example 2:

Input: head = []
Output: []
Example 3:

Input: head = [0]
Output: [0]
Example 4:

Input: head = [1,3]
Output: [3,1]


Constraints:

The numner of nodes in head is in the range [0, 2 * 10^4].
-10^5 <= Node.val <= 10^5

109. 有序链表转换二叉搜索树
给定一个单链表，其中的元素按升序排序，将其转换为高度平衡的二叉搜索树。

本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。

示例:

给定的有序链表： [-10, -3, 0, 5, 9],

一个可能的答案是：[0, -3, 9, -10, null, 5], 它可以表示下面这个高度平衡二叉搜索树：

      0
     / \
   -3   9
   /   /
 -10  5
'''



# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return None

        if not head.next:
            return TreeNode(head.val)

        fast, slow = head, head
        pre = head
        while fast and fast.next:
            fast = fast.next.next
            pre = slow
            slow = slow.next

        pre.next = None
        mid = TreeNode(slow.val)
        mid.left = self.sortedListToBST(head)
        mid.right = self.sortedListToBST(slow.next)

        return mid



# solution

'''
前言
将给定的有序链表转换为二叉搜索树的第一步是确定根节点。由于我们需要构造出平衡的二叉树，因此比较直观的想法是让根节点左子树中的节点个数与右子树中的节点个数尽可能接近。这样一来，左右子树的高度也会非常接近，可以达到高度差绝对值不超过 11 的题目要求。

如何找出这样的一个根节点呢？我们可以找出链表元素的中位数作为根节点的值。

这里对于中位数的定义为：如果链表中的元素个数为奇数，那么唯一的中间值为中位数；如果元素个数为偶数，那么唯二的中间值都可以作为中位数，而不是常规定义中二者的平均值。

根据中位数的性质，链表中小于中位数的元素个数与大于中位数的元素个数要么相等，要么相差 11。此时，小于中位数的元素组成了左子树，大于中位数的元素组成了右子树，它们分别对应着有序链表中连续的一段。在这之后，我们使用分治的思想，继续递归地对左右子树进行构造，找出对应的中位数作为根节点，以此类推。

可以证明，这样的构造方法得到的二叉搜索树是平衡的，详见文末的「正确性证明」部分。

方法一：分治
我们可以直接模拟「前言」部分的构造方案。

具体地，设当前链表的左端点为 \textit{left}left，右端点 \textit{right}right，包含关系为「左闭右开」，即 \textit{left}left 包含在链表中而 \textit{right}right 不包含在链表中。我们希望快速地找出链表的中位数节点 \textit{mid}mid。

为什么要设定「左闭右开」的关系？由于题目中给定的链表为单向链表，访问后继元素十分容易，但无法直接访问前驱元素。因此在找出链表的中位数节点 \textit{mid}mid 之后，如果设定「左闭右开」的关系，我们就可以直接用 (\textit{left}, \textit{mid})(left,mid) 以及 (\textit{mid}.\textit{next}, \textit{right})(mid.next,right) 来表示左右子树对应的列表了。并且，初始的列表也可以用 (\textit{head}, \textit{null})(head,null) 方便地进行表示，其中 \textit{null}null 表示空节点。

找出链表中位数节点的方法多种多样，其中较为简单的一种是「快慢指针法」。初始时，快指针 \textit{fast}fast 和慢指针 \textit{slow}slow 均指向链表的左端点 \textit{left}left。我们将快指针 \textit{fast}fast 向右移动两次的同时，将慢指针 \textit{slow}slow 向右移动一次，直到快指针到达边界（即快指针到达右端点或快指针的下一个节点是右端点）。此时，慢指针对应的元素就是中位数。

在找出了中位数节点之后，我们将其作为当前根节点的元素，并递归地构造其左侧部分的链表对应的左子树，以及右侧部分的链表对应的右子树。

C++JavaPython3GolangC

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def getMedian(left: ListNode, right: ListNode) -> ListNode:
            fast = slow = left
            while fast != right and fast.next != right:
                fast = fast.next.next
                slow = slow.next
            return slow
        
        def buildTree(left: ListNode, right: ListNode) -> TreeNode:
            if left == right:
                return None
            mid = getMedian(left, right)
            root = TreeNode(mid.val)
            root.left = buildTree(left, mid)
            root.right = buildTree(mid.next, right)
            return root
        
        return buildTree(head, None)
复杂度分析

时间复杂度：O(n \log n)O(nlogn)，其中 nn 是链表的长度。

设长度为 nn 的链表构造二叉搜索树的时间为 T(n)T(n)，递推式为 T(n) = 2 \cdot T(n/2) + O(n)T(n)=2⋅T(n/2)+O(n)，根据主定理，T(n) = O(n \log n)T(n)=O(nlogn)。

空间复杂度：O(\log n)O(logn)，这里只计算除了返回答案之外的空间。平衡二叉树的高度为 O(\log n)O(logn)，即为递归过程中栈的最大深度，也就是需要的空间。

方法二：分治 + 中序遍历优化
方法一的时间复杂度的瓶颈在于寻找中位数节点。由于构造出的二叉搜索树的中序遍历结果就是链表本身，因此我们可以将分治和中序遍历结合起来，减少时间复杂度。

具体地，设当前链表的左端点编号为 \textit{left}left，右端点编号为 \textit{right}right，包含关系为「双闭」，即 \textit{left}left 和 \textit{right}right 均包含在链表中。链表节点的编号为 [0, n)[0,n)。中序遍历的顺序是「左子树 - 根节点 - 右子树」，那么在分治的过程中，我们不用急着找出链表的中位数节点，而是使用一个占位节点，等到中序遍历到该节点时，再填充它的值。

我们可以通过计算编号范围来进行中序遍历：

中位数节点对应的编号为 \textit{mid} = (\textit{left} + \textit{right} + 1) / 2mid=(left+right+1)/2；

根据方法一中对于中位数的定义，编号为 (\textit{left} + \textit{right}) / 2(left+right)/2 的节点同样也可以是中位数节点。

左右子树对应的编号范围分别为 [\textit{left}, \textit{mid}-1][left,mid−1] 和 [\textit{mid}+1, \textit{right}][mid+1,right]。

如果 \textit{left} > \textit{right}left>right，那么遍历到的位置对应着一个空节点，否则对应着二叉搜索树中的一个节点。

这样一来，我们其实已经知道了这棵二叉搜索树的结构，并且题目给定了它的中序遍历结果，那么我们只要对其进行中序遍历，就可以还原出整棵二叉搜索树了。

C++JavaPython3GolangC

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def getLength(head: ListNode) -> int:
            ret = 0
            while head:
                ret += 1
                head = head.next
            return ret
        
        def buildTree(left: int, right: int) -> TreeNode:
            if left > right:
                return None
            mid = (left + right + 1) // 2
            root = TreeNode()
            root.left = buildTree(left, mid - 1)
            nonlocal head
            root.val = head.val
            head = head.next
            root.right = buildTree(mid + 1, right)
            return root
        
        length = getLength(head)
        return buildTree(0, length - 1)
复杂度分析

时间复杂度：O(n)O(n)，其中 nn 是链表的长度。

设长度为 nn 的链表构造二叉搜索树的时间为 T(n)T(n)，递推式为 T(n) = 2 \cdot T(n/2) + O(1)T(n)=2⋅T(n/2)+O(1)，根据主定理，T(n) = O(n)T(n)=O(n)。

空间复杂度：O(\log n)O(logn)，这里只计算除了返回答案之外的空间。平衡二叉树的高度为 O(\log n)O(logn)，即为递归过程中栈的最大深度，也就是需要的空间。

正确性证明
我们需要证明的是：对于任意的有序链表，用「前言」部分的构造方法得到的二叉搜索树一定是平衡的。显然，如果二叉搜索树的左右子树都是平衡的，并且它们的高度差不超过 11，那么该二叉搜索树就是平衡的。

我们使用数学归纳法，设链表的长度为 nn，对应的二叉搜索树的高度为 H(n)H(n)：

这里规定只包含根节点的二叉搜索树的高度为 11。

当 n=1, 2n=1,2 时，对应的二叉搜索树都是平衡的，并且 H(1) = 1H(1)=1，H(2) = 2H(2)=2；

当 n=3n=3 时，对应的二叉搜索树包含一个根节点和左右子树各一个节点，它是平衡的，并且 H(3) = 2H(3)=2；

假设当 n < n_0n<n 
0
​	
  时，对应的二叉搜索树是平衡的，并且对于任意的 1 \leq n < n_0 - 11≤n<n 
0
​	
 −1，都有 H(n+1) - H(n) \leq 1H(n+1)−H(n)≤1，那么当 n = n_0n=n 
0
​	
  时：

如果 nn 为奇数，设 n=2k+3n=2k+3，那么二叉搜索树的左右子树的大小均为 k+1k+1，高度相等，因此二叉搜索树是平衡的，并且有 H(n)=H(k+1)+1H(n)=H(k+1)+1。而 n-1 = 2k+2n−1=2k+2，对应的二叉搜索树的左右子树的大小为 kk 和 k+1k+1，即 H(n-1)=H(k+1)+1H(n−1)=H(k+1)+1，因此 H(n)=H(n-1)H(n)=H(n−1)；

如果 nn 为偶数，设 n=2k+2n=2k+2，那么二叉搜索树的左右子树的大小为 kk 和 k+1k+1，根据假设，高度差 H(k+1)-H(k) \leq 1H(k+1)−H(k)≤1，因此二叉搜索树是平衡的，并且有 H(n)=H(k+1)+1H(n)=H(k+1)+1。而 n-1=2k+1n−1=2k+1，对应的二叉搜索树的左右子树的大小均为 kk，即 H(n-1)=H(k)+1H(n−1)=H(k)+1，因此 H(n)-H(n-1)=H(k+1)-H(k) \leq 1H(n)−H(n−1)=H(k+1)−H(k)≤1。

这样我们就证明了任意长度的链表对应的二叉搜索树是平衡的。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/convert-sorted-list-to-binary-search-tree/solution/you-xu-lian-biao-zhuan-huan-er-cha-sou-suo-shu-1-3/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''