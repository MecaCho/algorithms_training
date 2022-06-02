# encoding=utf8

'''
450. Delete Node in a BST
Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node.
 

Example 1:


Input: root = [5,3,6,2,4,null,7], key = 3
Output: [5,4,6,2,null,null,7]
Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.
One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.

Example 2:

Input: root = [5,3,6,2,4,null,7], key = 0
Output: [5,3,6,2,4,null,7]
Explanation: The tree does not contain a node with value = 0.
Example 3:

Input: root = [], key = 0
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 104].
-105 <= Node.val <= 105
Each node has a unique value.
root is a valid binary search tree.
-105 <= key <= 105
 

Follow up: Could you solve it with time complexity O(height of tree)?
'''

# golang

'''
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func deleteNode(root *TreeNode, key int) *TreeNode {
    switch {
    case root == nil:
        return nil
    case root.Val > key:
        root.Left = deleteNode(root.Left, key)
    case root.Val < key:
        root.Right = deleteNode(root.Right, key)
    case root.Left == nil || root.Right == nil:
        if root.Left != nil {
            return root.Left
        }
        return root.Right
    default:
        successor := root.Right
        for successor.Left != nil {
            successor = successor.Left
        }
        successor.Right = deleteNode(root.Right, successor.Val)
        successor.Left = root.Left
        return successor
    }
    return root
}
'''

'''
root 为空，代表未搜索到值为 key 的节点，返回空。
root.val>key，表示值为 key 的节点可能存在于root 的左子树中，需要递归地在root.left 调用deleteNode，并返回root。
root.val<key，表示值为 key 的节点可能存在于root 的右子树中，需要递归地在root.right 调用deleteNode，并返回root。
root.val=key，root 即为要删除的节点。此时要做的是删除root，并将它的子树合并成一棵子树，保持有序性，并返回根节点。根据root 的子树情况分成以下情况讨论：
  root 为叶子节点，没有子树。此时可以直接将它删除，即返回空。
  root 只有左子树，没有右子树。此时可以将它的左子树作为新的子树，返回它的左子节点。
  root 只有右子树，没有左子树。此时可以将它的右子树作为新的子树，返回它的右子节点。
  root 有左右子树，这时可以将 root 的后继节点（比 root 大的最小节点，即它的右子树中的最小节点，记为successor作为新的根节点替代root，并将successor 从root 的右子树中删除，
  使得在保持有序性的情况下合并左右子树。

'''

