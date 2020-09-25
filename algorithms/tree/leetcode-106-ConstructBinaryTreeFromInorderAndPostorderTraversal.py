'''
106. 从中序与后序遍历序列构造二叉树
根据一棵树的中序遍历与后序遍历构造二叉树。

注意:
你可以假设树中没有重复的元素。

例如，给出

中序遍历 inorder = [9,3,15,20,7]
后序遍历 postorder = [9,15,7,20,3]
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7


106. Construct Binary Tree from Inorder and Postorder Traversal
Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        # inorder [左，根，右]
        # postorder [左，右，根]
        if not inorder or not postorder:
            return None
        root = TreeNode(postorder[-1])

        root_index = inorder.index(root.val)

        left = self.buildTree(inorder[:root_index], postorder[:root_index])
        right = self.buildTree(inorder[root_index+1:], postorder[root_index:-1])

        root.left = left
        root.right = right
        return root


'''
如何遍历树
遍历树有两种通用策略：

深度优先遍历（DFS）

这种方法以深度 depth 优先为策略，从根节点开始遍历直到某个叶子节点为止，然后回到根节点，再遍历另外一个分支。
根据根节点，左孩子节点和右孩子节点的访问顺序又可以将 DFS 细分为先序遍历 preorder，中序遍历 inorder 和后序遍历 postorder。

广度优先遍历（BFS）

按照高度顺序，从上往下逐层遍历节点。
先遍历上层节点再遍历下层节点。

下图中按照不同的方法遍历对应子树，得到的序列都是 1-2-3-4-5。根据不同子树结构比较不同遍历方法的特点。



本问题中使用中序和后序遍历。

方法一：递归
如何根据两种遍历序列构造树：中序，和先序/后序/等等。

这类问题在 Facebook 的面试中常常出现，它可以在 \mathcal{O}(N)O(N) 的时间内解决：

通常从先序序列或者后序序列开始，根据不同遍历方法的规律，选择合适的节点构造树。
例如：先序序列的 第一个 节点是根节点，然后是它的左孩子，右孩子等等。
后序序列的 最后一个 节点是根节点，然后是它的右孩子，左孩子等等。

从先序/后序序列中找到根节点，根据根节点将中序序列分为左子树和右子树。从中序序列中获得的信息是：如果当前子树为空（返回 None），否则继续构造子树。



算法

创建 hashmap 存储中序序列：value -> its index 。

方法 helper 的参数是中序序列中当前子树的左右边界，该方法仅用于检查子树是否为空。下面分析 helper(in_left = 0, in_right = n - 1) 的逻辑：

如果 in_left > in_right，说明子树为空，返回 None。

选择后序遍历的最后一个节点作为根节点。

假设根节点在中序遍历中索引为 index。从 in_left 到 index - 1 属于左子树，从 index + 1 到 in_right 属于右子树。

根据后序遍历逻辑，递归创建右子树 helper(index + 1, in_right) 和左子树 helper(in_left, index - 1)。

返回根节点 root。


1 / 7

JavaPython
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def helper(in_left, in_right):
            # if there is no elements to construct subtrees
            if in_left > in_right:
                return None
            
            # pick up the last element as a root
            val = postorder.pop()
            root = TreeNode(val)

            # root splits inorder list
            # into left and right subtrees
            index = idx_map[val]
 
            # build right subtree
            root.right = helper(index + 1, in_right)
            # build left subtree
            root.left = helper(in_left, index - 1)
            return root
        
        # build a hashmap value -> its index
        idx_map = {val:idx for idx, val in enumerate(inorder)} 
        return helper(0, len(inorder) - 1)
复杂度分析

时间复杂度：\mathcal{O}(N)O(N)。
使用主定理计算时间复杂度。
T(N) = aT\left(\frac{N}{b}\right) + \Theta(N^d)T(N)=aT( 
b
N
​	
 )+Θ(N 
d
 )。
该公式表示花费 \Theta(N^d)Θ(N 
d
 ) 时间分解一个问题，得到 aa 个规模为 \frac{N}{b} 
b
N
​	
  的子问题。
这里把一个问题分解为两个子问题 a = 2，计算左右子树的规模为初始问题的一半 b = 2，每次分解花费恒定时间 d = 0，即 \log_b{a} = dlog 
b
​	
 a=d。
根据主定理，时间复杂度为 \mathcal{O}(N^{\log_b(a)}) = \mathcal{O}(N)O(N 
log 
b
​	
 (a)
 )=O(N)。

空间复杂度：\mathcal{O}(N)O(N)，存储整棵树。

'''