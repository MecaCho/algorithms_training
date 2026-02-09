# encoding=utf8

'''
1382. Balance a Binary Search Tree

Given the root of a binary search tree, return a balanced binary search tree with the same node values. If there is more than one answer, return any of them.

A binary search tree is balanced if the depth of the two subtrees of every node never differs by more than 1.

 

Example 1:

Input: root = [1,null,2,null,3,null,4,null,null]
Output: [2,1,3,null,null,null,4]
Explanation: This is not the only correct answer, [3,1,4,null,2] is also correct.

Example 2:

Input: root = [2,1,3]
Output: [2,1,3]

 

Constraints:

    The number of nodes in the tree is in the range [1, 104].
    1 <= Node.val <= 105
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # 步骤1：中序遍历BST，得到升序数组
        def inorder_traversal(node):
            res = []
            if node:
                res += inorder_traversal(node.left)
                res.append(node.val)
                res += inorder_traversal(node.right)
            return res
        
        sorted_vals = inorder_traversal(root)
        
        # 步骤2：根据升序数组构建平衡BST
        def build_balanced_bst(nums, left, right):
            # 递归终止条件：左指针超过右指针
            if left > right:
                return None
            # 取中间元素作为根节点，保证左右子树平衡
            mid = (left + right) // 2
            root = TreeNode(nums[mid])
            # 递归构建左子树（左半数组）
            root.left = build_balanced_bst(nums, left, mid - 1)
            # 递归构建右子树（右半数组）
            root.right = build_balanced_bst(nums, mid + 1, right)
            return root
        
        return build_balanced_bst(sorted_vals, 0, len(sorted_vals) - 1)
        
