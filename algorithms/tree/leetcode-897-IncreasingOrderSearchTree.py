# encoding=utf8

'''
897. Increasing Order Search Tree
Given the root of a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only one right child.

 

Example 1:


Input: root = [5,3,6,2,4,null,8,1,null,null,null,7,9]
Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]
Example 2:


Input: root = [5,1,7]
Output: [1,null,5,null,7]
 

Constraints:

The number of nodes in the given tree will be in the range [1, 100].
0 <= Node.val <= 1000


897. 递增顺序搜索树

给你一棵二叉搜索树，请你 按中序遍历 将其重新排列为一棵递增顺序搜索树，使树中最左边的节点成为树的根节点，并且每个节点没有左子节点，只有一个右子节点。

 

示例 1：


输入：root = [5,3,6,2,4,null,8,1,null,null,null,7,9]
输出：[1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]
示例 2：


输入：root = [5,1,7]
输出：[1,null,5,null,7]
 

提示：

树中节点数的取值范围是 [1, 100]
0 <= Node.val <= 1000
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def inorder(root):

            stack = [(0, root)]
            self.vals = []

            while stack:
                flag, node = stack.pop()
                if node:
                    if flag == 1:
                        self.vals.append(node.val)
                    else:
                        stack.append((0, node.right))
                        stack.append((1, node))
                        stack.append((0, node.left))
            return self.vals

        inorder(root)
        # print(self.vals)
        node = TreeNode(0)
        pre = node
        for i in range(len(self.vals)):
            node.right = TreeNode(self.vals[i])
            node.left = None
            node = node.right
        return pre.right

# solutions

'''
方法一：中序遍历之后生成新的树
算法

题目要求我们返回按照中序遍历的结果改造而成的、只有右节点的等价二叉搜索树。我们可以进行如下操作：

先对输入的二叉搜索树执行中序遍历，将结果保存到一个列表中；

然后根据列表中的节点值，创建等价的只含有右节点的二叉搜索树，其过程等价于根据节点值创建一个链表。

代码

JavaJavaScriptGolangC++C

func increasingBST(root *TreeNode) *TreeNode {
    vals := []int{}
    var inorder func(*TreeNode)
    inorder = func(node *TreeNode) {
        if node != nil {
            inorder(node.Left)
            vals = append(vals, node.Val)
            inorder(node.Right)
        }
    }
    inorder(root)

    dummyNode := &TreeNode{}
    curNode := dummyNode
    for _, val := range vals {
        curNode.Right = &TreeNode{Val: val}
        curNode = curNode.Right
    }
    return dummyNode.Right
}
复杂度分析

时间复杂度：O(n)O(n)，其中 nn 是二叉搜索树的节点总数。

空间复杂度：O(n)O(n)，其中 nn 是二叉搜索树的节点总数。需要长度为 nn 的列表保存二叉搜索树的所有节点的值。

方法二：在中序遍历的过程中改变节点指向
算法

方法一需要遍历一次二叉搜索树以后，然后再创建新的等价的二叉搜索树。事实上，还可以遍历一次输入二叉搜索树，在遍历的过程中改变节点指向以满足题目的要求。

在中序遍历的时候，修改节点指向就可以实现。具体地，当我们遍历到一个节点时，把它的左孩子设为空，并将其本身作为上一个遍历到的节点的右孩子。这里需要有一些想象能力。递归遍历的过程中，由于递归函数的调用栈保存了节点的引用，因此上述操作可以实现。下面的幻灯片展示了这样的过程。


1 / 27

代码

JavaJavaScriptGolangC++C

func increasingBST(root *TreeNode) *TreeNode {
    dummyNode := &TreeNode{}
    resNode := dummyNode

    var inorder func(*TreeNode)
    inorder = func(node *TreeNode) {
        if node == nil {
            return
        }
        inorder(node.Left)

        // 在中序遍历的过程中修改节点指向
        resNode.Right = node
        node.Left = nil
        resNode = node

        inorder(node.Right)
    }
    inorder(root)

    return dummyNode.Right
}
复杂度分析

时间复杂度：O(n)O(n)，其中 nn 是二叉搜索树的节点总数。

空间复杂度：O(n)O(n)。递归过程中的栈空间开销为 O(n)O(n)。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/increasing-order-search-tree/solution/di-zeng-shun-xu-cha-zhao-shu-by-leetcode-dfrr/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''

