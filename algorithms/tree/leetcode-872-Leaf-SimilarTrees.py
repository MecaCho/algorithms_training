# encoding=utf8

'''
872. Leaf-Similar Trees

Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.



For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

 

Example 1:


Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
Output: true
Example 2:

Input: root1 = [1], root2 = [1]
Output: true
Example 3:

Input: root1 = [1], root2 = [2]
Output: false
Example 4:

Input: root1 = [1,2], root2 = [2,2]
Output: true
Example 5:


Input: root1 = [1,2,3], root2 = [1,3,2]
Output: false
 

Constraints:

The number of nodes in each tree will be in the range [1, 200].
Both of the given trees will have values in the range [0, 200].


872. 叶子相似的树

请考虑一棵二叉树上所有的叶子，这些叶子的值按从左到右的顺序排列形成一个 叶值序列 。



举个例子，如上图所示，给定一棵叶值序列为 (6, 7, 4, 9, 8) 的树。

如果有两棵二叉树的叶值序列是相同，那么我们就认为它们是 叶相似 的。

如果给定的两个根结点分别为 root1 和 root2 的树是叶相似的，则返回 true；否则返回 false 。

 

示例 1：



输入：root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
输出：true
示例 2：

输入：root1 = [1], root2 = [1]
输出：true
示例 3：

输入：root1 = [1], root2 = [2]
输出：false
示例 4：

输入：root1 = [1,2], root2 = [2,2]
输出：true
示例 5：



输入：root1 = [1,2,3], root2 = [1,3,2]
输出：false
 

提示：

给定的两棵树可能会有 1 到 200 个结点。
给定的两棵树上的值介于 0 到 200 之间。
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        def dfs(root, tmp):
            if not root:
                return
            if not root.left and not root.right:
                tmp.append(root.val)
            if root.left:
                dfs(root.left, tmp)
            if root.right:
                dfs(root.right, tmp)
        vals1 = []
        vals2 = []
        dfs(root1, vals1)
        dfs(root2, vals2)

        return vals1 == vals2
       
       
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
func leafSimilar(root1 *TreeNode, root2 *TreeNode) bool {
	var dfs func(node *TreeNode, vals *[]int)
	dfs = func(root *TreeNode, vals *[]int) {
		if root == nil {
			return
		}
		if root.Left == nil && root.Right == nil {
			*vals = append(*vals, root.Val)
		}
		dfs(root.Left, vals)
		dfs(root.Right, vals)
	}

	vals1 := []int{}
	vals2 := []int{}
	dfs(root1, &vals1)
	dfs(root2, &vals2)

	if len(vals1) != len(vals2) {
		return false
	}

	for k, v := range vals1 {
		if v != vals2[k] {
			return false
		}
	}
	return true
}
'''

# solutions

'''
方法一：深度优先搜索
思路与算法

我们可以使用深度优先搜索的方法得到一棵树的「叶值序列」。

具体地，在深度优先搜索的过程中，我们总是先搜索当前节点的左子节点，再搜索当前节点的右子节点。如果我们搜索到一个叶节点，就将它的值放入序列中。

在得到了两棵树分别的「叶值序列」后，我们比较它们是否相等即可。

代码

C++JavaC#Python3JavaScriptGolangC

func leafSimilar(root1, root2 *TreeNode) bool {
    vals := []int{}
    var dfs func(*TreeNode)
    dfs = func(node *TreeNode) {
        if node == nil {
            return
        }
        if node.Left == nil && node.Right == nil {
            vals = append(vals, node.Val)
            return
        }
        dfs(node.Left)
        dfs(node.Right)
    }
    dfs(root1)
    vals1 := append([]int(nil), vals...)
    vals = []int{}
    dfs(root2)
    if len(vals) != len(vals1) {
        return false
    }
    for i, v := range vals1 {
        if v != vals[i] {
            return false
        }
    }
    return true
}
复杂度分析

时间复杂度：O(n_1 + n_2)O(n 
1
​	
 +n 
2
​	
 )，其中 n_1n 
1
​	
  和 n_2n 
2
​	
  分别是两棵树的节点个数。

空间复杂度：O(n_1 + n_2)O(n 
1
​	
 +n 
2
​	
 )。空间复杂度主要取决于存储「叶值序列」的空间以及深度优先搜索的过程中需要使用的栈空间。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/leaf-similar-trees/solution/xie-zi-xiang-si-de-shu-by-leetcode-solut-z0w6/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
