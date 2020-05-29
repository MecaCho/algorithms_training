




# golang solutions

'''
package link_list

// 114. 二叉树展开为链表
// 给定一个二叉树，原地将它展开为一个单链表。
//
//
//
// 例如，给定二叉树
//
//    1
//   / \
//  2   5
// / \   \
// 3   4   6
// 将其展开为：
//
// 1
// \
//  2
//   \
//    3
//     \
//      4
//       \
//        5
//         \
//          6

// 114. Flatten Binary Tree to Linked List
// Given a binary tree, flatten it to a linked list in-place.
//
// For example, given the following tree:
//
//    1
//   / \
//  2   5
// / \   \
// 3   4   6
// The flattened tree should look like:
//
// 1
// \
//  2
//   \
//    3
//     \
//      4
//       \
//        5
//         \
//          6

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func flatten(root *TreeNode) {

	if root == nil {
		return
	}

	left := root.Left
	right := root.Right

	flatten(left)
	flatten(right)

	if left == nil {
		root.Right = right
		root.Left = nil
		return
	}

	loc_left := left

	for left != nil {
		if left.Right == nil {
			left.Right = right
			break
		}
		left = left.Right
	}

	root.Right = loc_left
	root.Left = nil
}

'''
