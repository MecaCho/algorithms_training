'''
116. Populating Next Right Pointers in Each Node
You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.



Follow up:

You may only use constant extra space.
Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.


Example 1:



Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.


Constraints:

The number of nodes in the given tree is less than 4096.
-1000 <= node.val <= 1000

116. 填充每个节点的下一个右侧节点指针
给定一个完美二叉树，其所有叶子节点都在同一层，每个父节点都有两个子节点。二叉树定义如下：

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。

初始状态下，所有 next 指针都被设置为 NULL。



示例：



输入：{"$id":"1","left":{"$id":"2","left":{"$id":"3","left":null,"next":null,"right":null,"val":4},"next":null,"right":{"$id":"4","left":null,"next":null,"right":null,"val":5},"val":2},"next":null,"right":{"$id":"5","left":{"$id":"6","left":null,"next":null,"right":null,"val":6},"next":null,"right":{"$id":"7","left":null,"next":null,"right":null,"val":7},"val":3},"val":1}

输出：{"$id":"1","left":{"$id":"2","left":{"$id":"3","left":null,"next":{"$id":"4","left":null,"next":{"$id":"5","left":null,"next":{"$id":"6","left":null,"next":null,"right":null,"val":7},"right":null,"val":6},"right":null,"val":5},"right":null,"val":4},"next":{"$id":"7","left":{"$ref":"5"},"next":null,"right":{"$ref":"6"},"val":3},"right":{"$ref":"4"},"val":2},"next":null,"right":{"$ref":"7"},"val":1}

解释：给定二叉树如图 A 所示，你的函数应该填充它的每个 next 指针，以指向其下一个右侧节点，如图 B 所示。


提示：

你只能使用常量级额外空间。
使用递归解题也符合要求，本题中递归程序占用的栈空间不算做额外的空间复杂度。
'''


"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
# var connect = function (root) {
#      if (root == null || root.left == null)
#         return root;
#     root.left.next = root.right;
#     root.right.next = root.next == null ? null : root.next.left;
#     root.left = connect(root.left);
#     root.right = connect(root.right);
#     return root;
# };



class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root or not root.left:
            return root

        root.left.next = root.right
        root.right.next = None if not root.next else root.next.left

        root.left = self.connect(root.left)
        root.right = self.connect(root.right)

        return root


# solutions

'''
方法一：层次遍历
思路与算法

题目本身希望我们将二叉树的每一层节点都连接起来形成一个链表。因此直观的做法我们可以对二叉树进行层次遍历，在层次遍历的过程中将我们将二叉树每一层的节点拿出来遍历并连接。

层次遍历基于广度优先搜索，它与广度优先搜索的不同之处在于，广度优先搜索每次只会取出一个节点来拓展，而层次遍历会每次将队列中的所有元素都拿出来拓展，这样能保证每次从队列中拿出来遍历的元素都是属于同一层的，因此我们可以在遍历的过程中修改每个节点的 next 指针，同时拓展下一层的新队列。


1 / 15

代码

JavaPython3C++JavaScriptGolangC

import collections 

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        if not root:
            return root
        
        # 初始化队列同时将第一层节点加入队列中，即根节点
        Q = collections.deque([root])
        
        # 外层的 while 循环迭代的是层数
        while Q:
            
            # 记录当前队列大小
            size = len(Q)
            
            # 遍历这一层的所有节点
            for i in range(size):
                
                # 从队首取出元素
                node = Q.popleft()
                
                # 连接
                if i < size - 1:
                    node.next = Q[0]
                
                # 拓展下一层节点
                if node.left:
                    Q.append(node.left)
                if node.right:
                    Q.append(node.right)
        
        # 返回根节点
        return root
复杂度分析

时间复杂度：O(N)O(N)。每个节点会被访问一次且只会被访问一次，即从队列中弹出，并建立 next 指针。

空间复杂度：O(N)O(N)。这是一棵完美二叉树，它的最后一个层级包含 N/2N/2 个节点。广度优先遍历的复杂度取决于一个层级上的最大元素数量。这种情况下空间复杂度为 O(N)O(N)。

方法二：使用已建立的 \text{next}next 指针
思路

一棵树中，存在两种类型的 next 指针。

第一种情况是连接同一个父节点的两个子节点。它们可以通过同一个节点直接访问到，因此执行下面操作即可完成连接。

Java

node.left.next = node.right


第二种情况在不同父亲的子节点之间建立连接，这种情况不能直接连接。



如果每个节点有指向父节点的指针，可以通过该指针找到 next 节点。如果不存在该指针，则按照下面思路建立连接：

第 NN 层节点之间建立 next 指针后，再建立第 N+1N+1 层节点的 next 指针。可以通过 next 指针访问同一层的所有节点，因此可以使用第 NN 层的 next 指针，为第 N+1N+1 层节点建立 next 指针。

算法

从根节点开始，由于第 00 层只有一个节点，所以不需要连接，直接为第 11 层节点建立 next 指针即可。该算法中需要注意的一点是，当我们为第 NN 层节点建立 next 指针时，处于第 N-1N−1 层。当第 NN 层节点的 next 指针全部建立完成后，移至第 NN 层，建立第 N+1N+1 层节点的 next 指针。

遍历某一层的节点时，这层节点的 next 指针已经建立。因此我们只需要知道这一层的最左节点，就可以按照链表方式遍历，不需要使用队列。

上面思路的伪代码如下：

Java

leftmost = root
while (leftmost.left != null) {
    head = leftmost
    while (head.next != null) {
        1) Establish Connection 1
        2) Establish Connection 2 using next pointers
        head = head.next
    }
    leftmost = leftmost.left
}


两种类型的 next 指针。

第一种情况两个子节点属于同一个父节点，因此直接通过父节点建立两个子节点的 next 指针即可。

Java

node.left.next = node.right


第二种情况是连接不同父节点之间子节点的情况。更具体地说，连接的是第一个父节点的右孩子和第二父节点的左孩子。由于已经在父节点这一层建立了 next 指针，因此可以直接通过第一个父节点的 next 指针找到第二个父节点，然后在它们的孩子之间建立连接。

Java

node.right.next = node.next.left


完成当前层的连接后，进入下一层重复操作，直到所有的节点全部连接。进入下一层后需要更新最左节点，然后从新的最左节点开始遍历该层所有节点。因为是完美二叉树，因此最左节点一定是当前层最左节点的左孩子。如果当前最左节点的左孩子不存在，说明已经到达该树的最后一层，完成了所有节点的连接。



代码

JavaPython3C++JavaScriptGolangC

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        if not root:
            return root
        
        # 从根节点开始
        leftmost = root
        
        while leftmost.left:
            
            # 遍历这一层节点组织成的链表，为下一层的节点更新 next 指针
            head = leftmost
            while head:
                
                # CONNECTION 1
                head.left.next = head.right
                
                # CONNECTION 2
                if head.next:
                    head.right.next = head.next.left
                
                # 指针向后移动
                head = head.next
            
            # 去下一层的最左的节点
            leftmost = leftmost.left
        
        return root 
复杂度分析

时间复杂度：O(N)O(N)，每个节点只访问一次。

空间复杂度：O(1)O(1)，不需要存储额外的节点。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node/solution/tian-chong-mei-ge-jie-dian-de-xia-yi-ge-you-ce-2-4/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
