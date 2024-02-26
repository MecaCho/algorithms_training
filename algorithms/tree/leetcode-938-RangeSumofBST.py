# encoding=utf8


'''
938. Range Sum of BST

Given the root node of a binary search tree, return the sum of values of all nodes with a value in the range [low, high].

 

Example 1:


Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
Output: 32
Example 2:


Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
Output: 23
 

Constraints:

The number of nodes in the tree is in the range [1, 2 * 104].
1 <= Node.val <= 105
1 <= low <= high <= 105
All Node.val are unique.

938. 二叉搜索树的范围和

给定二叉搜索树的根结点 root，返回值位于范围 [low, high] 之间的所有结点的值的和。

 

示例 1：


输入：root = [10,5,15,3,7,null,18], low = 7, high = 15
输出：32
示例 2：


输入：root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
输出：23
 

提示：

树中节点数目在范围 [1, 2 * 104] 内
1 <= Node.val <= 105
1 <= low <= high <= 105
所有 Node.val 互不相同
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        self.val = 0
        def check(root):
            if not root:
                return 0

            if low <= root.val <= high:
                self.val += root.val
                check(root.left)
                check(root.right)
            elif root.val < low:
                check(root.right)
            elif root.val > high:
                check(root.left)

        check(root)
        return self.val

       
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution1(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        if not root:
            return 0
        if low <= root.val <= high:
            return self.rangeSumBST(root.left, low, high) + root.val + self.rangeSumBST(root.right, low, high)
        elif root.val > high:
            return self.rangeSumBST(root.left, low, high) 
        else:
            return self.rangeSumBST(root.right, low, high)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        l_r_sum = self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)
        return root.val + l_r_sum if low <= root.val <= high else l_r_sum

         
# golang solution

'''
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func rangeSumBST(root *TreeNode, low int, high int) int {
    if root == nil{
        return 0
    }
    if root.Val < low{
        return rangeSumBST(root.Right, low, high)
    }

    if root.Val > high{
        return rangeSumBST(root.Left, low, high)
    }

    return rangeSumBST(root.Left, low, high) + root.Val + rangeSumBST(root.Right, low, high)

}
'''



# golang solution 

'''
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func rangeSumBST(root *TreeNode, low int, high int) int {
    queue := []*TreeNode{}

    if root == nil{
        return 0
    }
    queue = append(queue, root)

    res := 0

    for len(queue) > 0{
        node := queue[0]
        queue = queue[1:]
        if node == nil{
            continue
        }
        if node.Val < low{
            queue = append(queue, node.Right)
        } else if node.Val > high{
            queue = append(queue, node.Left)
        } else{
            res += node.Val
            queue = append(queue, node.Left)
            queue = append(queue, node.Right)
        }
    }
    return res
}
'''

# solutions

'''
方法一：深度优先搜索
思路

按深度优先搜索的顺序计算范围和。记当前子树根节点为 \textit{root}root，分以下四种情况讨论：

\textit{root}root 节点为空

返回 00。

\textit{root}root 节点的值大于 \textit{high}high

由于二叉搜索树右子树上所有节点的值均大于根节点的值，即均大于 \textit{high}high，故无需考虑右子树，返回左子树的范围和。

\textit{root}root 节点的值小于 \textit{low}low

由于二叉搜索树左子树上所有节点的值均小于根节点的值，即均小于 \textit{low}low，故无需考虑左子树，返回右子树的范围和。

\textit{root}root 节点的值在 [\textit{low},\textit{high}][low,high] 范围内

此时应返回 \textit{root}root 节点的值、左子树的范围和、右子树的范围和这三者之和。

代码

C++JavaGolangJavaScriptPython3C

func rangeSumBST(root *TreeNode, low, high int) int {
    if root == nil {
        return 0
    }
    if root.Val > high {
        return rangeSumBST(root.Left, low, high)
    }
    if root.Val < low {
        return rangeSumBST(root.Right, low, high)
    }
    return root.Val + rangeSumBST(root.Left, low, high) + rangeSumBST(root.Right, low, high)
}
复杂度分析

时间复杂度：O(n)O(n)，其中 nn 是二叉搜索树的节点数。

空间复杂度：O(n)O(n)。空间复杂度主要取决于栈空间的开销。

方法二：广度优先搜索
思路

使用广度优先搜索的方法，用一个队列 qq 存储需要计算的节点。每次取出队首节点时，若节点为空则跳过该节点，否则按方法一中给出的大小关系来决定加入队列的子节点。

代码

C++JavaGolangJavaScriptPython3C

func rangeSumBST(root *TreeNode, low, high int) (sum int) {
    q := []*TreeNode{root}
    for len(q) > 0 {
        node := q[0]
        q = q[1:]
        if node == nil {
            continue
        }
        if node.Val > high {
            q = append(q, node.Left)
        } else if node.Val < low {
            q = append(q, node.Right)
        } else {
            sum += node.Val
            q = append(q, node.Left, node.Right)
        }
    }
    return
}
复杂度分析

时间复杂度：O(n)O(n)，其中 nn 是二叉搜索树的节点数。

空间复杂度：O(n)O(n)。空间复杂度主要取决于队列的空间。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/range-sum-of-bst/solution/er-cha-sou-suo-shu-de-fan-wei-he-by-leet-rpq7/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''

