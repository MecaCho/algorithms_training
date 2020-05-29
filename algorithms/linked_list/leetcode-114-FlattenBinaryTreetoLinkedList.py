




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


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class NewListNode(object):
    def __init__(self, y):
        super(ListNode).__init__()
        self.y = y

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pass


class Car(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


class NewCar(Car):
    def __init__(self,x, y,z, m, n):
        super().__init__(x,y,z)
        self.m = m
        self.n = n


class NewProxy():
    def __init__(self, obj):
        self._obj = obj

    # Delegate attribute lookup to internal obj
    def __getattr__(self, name):
        return getattr(self._obj, name)

    # Delegate attribute assignment
    def __setattr__(self, name, value):
        if name.startswith('_'):
            super().__setattr__(name, value) # Call original __setattr__
        else:
            setattr(self._obj, name, value)

if __name__ == '__main__':
    demo = NewCar(10, 12, 16, 99, 100)
    res = demo.x
    res_x = demo.y
    print(res, res_x, demo.m, demo.n)

