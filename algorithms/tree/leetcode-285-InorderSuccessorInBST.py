


'''
285. 二叉搜索树中的顺序后继
给你一个二叉搜索树和其中的某一个结点，请你找出该结点在树中顺序后继的节点。

结点 p 的后继是值比 p.val 大的结点中键值最小的结点。



示例 1:



输入: root = [2,1,3], p = 1
输出: 2
解析: 这里 1 的顺序后继是 2。请注意 p 和返回值都应是 TreeNode 类型。
示例 2:



输入: root = [5,3,6,2,4,null,null,1], p = 6
输出: null
解析: 因为给出的结点没有顺序后继，所以答案就返回 null 了。


注意:

假如给出的结点在该树中没有顺序后继的话，请返回 null
我们保证树中每个结点的值是唯一的

285. Inorder Successor in BST
Given a binary search tree and a node in it, find the in-order successor of that node in the BST.

The successor of a node p is the node with the smallest key greater than p.val.



Example 1:


Input: root = [2,1,3], p = 1
Output: 2
Explanation: 1's in-order successor node is 2. Note that both p and the return value is of TreeNode type.
Example 2:


Input: root = [5,3,6,2,4,null,null,1], p = 6
Output: null
Explanation: There is no in-order successor of the current node, so the answer is null.


Note:

If the given node has no in-order successor in the tree, return null.
It's guaranteed that the values of the tree are unique.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        self.res = None
        def inorder_traversal(root):
            if not root:
                return
            inorder_traversal(root.left)
            if not self.res and root.val > p.val:
                self.res = root
                # return
            inorder_traversal(root.right)
        inorder_traversal(root)
        return self.res


'''
方法一：中序遍历
二叉搜索树的中序遍历结果是一个递增的数组，顺序后继是中序遍历中当前节点 之后 最小的节点。

可以分成两种情况来讨论：

如果当前节点有右孩子，顺序后继在当前节点之下，如下图中红色节点所示。

如果当前的话，顺序后继在当前节点之上，如下图中蓝色节点所示。



如果是下图这种情况，找到顺序后继很简单，先找到当前节点的右孩子，然后再持续往左直到左孩子为空。



这种方法的时间复杂度为 O(H_p)O(H 
p
​	
 )，其中 H_pH 
p
​	
  为节点 pp 的高度。

下面再来看一个复杂一点的情况，这时候由于无法访问父亲节点，只能从根节点开始中序遍历。中序遍历通常由有递归和非递归的实现方式，这里用非递归的实现方式会更好一点。

直接在中序遍历过程保存前一个访问的节点，判断前一个节点是否为 p，如果是的话当前节点就是 p 节点的顺序后继。



中序遍历方法的时间复杂度为 O(H)O(H)，其中 HH 为树的高度。在第一种情况下也可以用中序遍历的方法，但之前的方法更快一点。

算法

如果当前节点有右孩子，找到右孩子，再持续往左走直到节点左孩子为空，直接返回该节点。

如果没有的话，就需要用到非递归的中序遍历。维持一个栈，当栈中有节点时：

往左走直到节点的左孩子为空，并将每个访问过的节点压入栈中。

弹出栈中节点，判断当前的前继节点是否为 p，如果是则直接返回当前节点。如果不是，将当前节点赋值给前继节点。

往右走一步。

如果走到这一步，说明不存在顺序后继，返回空。

实现

PythonJava
class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        # the successor is somewhere lower in the right subtree
        # successor: one step right and then left till you can
        if p.right:
            p = p.right
            while p.left:
                p = p.left
            return p
        
        # the successor is somewhere upper in the tree
        stack, inorder = [], float('-inf')
        
        # inorder traversal : left -> node -> right
        while stack or root:
            # 1. go left till you can
            while root:
                stack.append(root)
                root = root.left
                
            # 2. all logic around the node
            root = stack.pop()
            if inorder == p.val:    # if the previous node was equal to p
                return root         # then the current node is its successor
            inorder = root.val
            
            # 3. go one step right
            root = root.right

        # there is no successor
        return None
复杂度分析

时间复杂度：如果节点 p 有右孩子，时间复杂度为 O(H_p)O(H 
p
​	
 )，其中 H_pH 
p
​	
  是节点 p 的高度。如果没有右孩子，时间复杂度为 O(H)O(H)，其中 HH 为树的高度。

空间复杂度：如果节点 p 有右孩子，空间复杂度为 O(1)O(1)。如果没有右孩子，空间复杂度度为 O(H)O(H)。

作者：LeetCode
链接：https://leetcode-cn.com/problems/inorder-successor-in-bst/solution/er-cha-sou-suo-shu-zhong-de-shun-xu-hou-ji-by-leet/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
