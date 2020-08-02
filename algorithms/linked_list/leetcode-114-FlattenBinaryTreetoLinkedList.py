




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

# solutions

'''
方法一：前序遍历
将二叉树展开为单链表之后，单链表中的节点顺序即为二叉树的前序遍历访问各节点的顺序。因此，可以对二叉树进行前序遍历，获得各节点被访问到的顺序。由于将二叉树展开为链表之后会破坏二叉树的结构，因此在前序遍历结束之后更新每个节点的左右子节点的信息，将二叉树展开为单链表。

对二叉树的前序遍历不熟悉的读者请自行练习「144. 二叉树的前序遍历」。

前序遍历可以通过递归或者迭代的方式实现。以下代码通过递归实现前序遍历。

JavaC++GolangPython3JavaScriptC

class Solution:
    def flatten(self, root: TreeNode) -> None:
        preorderList = list()

        def preorderTraversal(root: TreeNode):
            if root:
                preorderList.append(root)
                preorderTraversal(root.left)
                preorderTraversal(root.right)
        
        preorderTraversal(root)
        size = len(preorderList)
        for i in range(1, size):
            prev, curr = preorderList[i - 1], preorderList[i]
            prev.left = None
            prev.right = curr
以下代码通过迭代实现前序遍历。

JavaC++GolangPython3JavaScriptC

class Solution:
    def flatten(self, root: TreeNode) -> None:
        preorderList = list()
        stack = list()
        node = root

        while node or stack:
            while node:
                preorderList.append(node)
                stack.append(node)
                node = node.left
            node = stack.pop()
            node = node.right
        
        size = len(preorderList)
        for i in range(1, size):
            prev, curr = preorderList[i - 1], preorderList[i]
            prev.left = None
            prev.right = curr
复杂度分析

时间复杂度：O(n)O(n)，其中 nn 是二叉树的节点数。前序遍历的时间复杂度是 O(n)O(n)，前序遍历之后，需要对每个节点更新左右子节点的信息，时间复杂度也是 O(n)O(n)。

空间复杂度：O(n)O(n)，其中 nn 是二叉树的节点数。空间复杂度取决于栈（递归调用栈或者迭代中显性使用的栈）和存储前序遍历结果的列表的大小，栈内的元素个数不会超过 nn，前序遍历列表中的元素个数是 nn。

方法二：前序遍历和展开同步进行
使用方法一的前序遍历，由于将节点展开之后会破坏二叉树的结构而丢失子节点的信息，因此前序遍历和展开为单链表分成了两步。能不能在不丢失子节点的信息的情况下，将前序遍历和展开为单链表同时进行？

之所以会在破坏二叉树的结构之后丢失子节点的信息，是因为在对左子树进行遍历时，没有存储右子节点的信息，在遍历完左子树之后才获得右子节点的信息。只要对前序遍历进行修改，在遍历左子树之前就获得左右子节点的信息，并存入栈内，子节点的信息就不会丢失，就可以将前序遍历和展开为单链表同时进行。

该做法不适用于递归实现的前序遍历，只适用于迭代实现的前序遍历。修改后的前序遍历的具体做法是，每次从栈内弹出一个节点作为当前访问的节点，获得该节点的子节点，如果子节点不为空，则依次将右子节点和左子节点压入栈内（注意入栈顺序）。

展开为单链表的做法是，维护上一个访问的节点 prev，每次访问一个节点时，令当前访问的节点为 curr，将 prev 的左子节点设为 null 以及将 prev 的右子节点设为 curr，然后将 curr 赋值给 prev，进入下一个节点的访问，直到遍历结束。需要注意的是，初始时 prev 为 null，只有在 prev 不为 null 时才能对 prev 的左右子节点进行更新。

JavaC++GolangPython3JavaScriptC

class Solution:
    def flatten(self, root: TreeNode) -> None:
        if not root:
            return
        
        stack = [root]
        prev = None
        
        while stack:
            curr = stack.pop()
            if prev:
                prev.left = None
                prev.right = curr
            left, right = curr.left, curr.right
            if right:
                stack.append(right)
            if left:
                stack.append(left)
            prev = curr
复杂度分析

时间复杂度：O(n)O(n)，其中 nn 是二叉树的节点数。前序遍历的时间复杂度是 O(n)O(n)，前序遍历的同时对每个节点更新左右子节点的信息，更新子节点信息的时间复杂度是 O(1)O(1)，因此总时间复杂度是 O(n)O(n)。

空间复杂度：O(n)O(n)，其中 nn 是二叉树的节点数。空间复杂度取决于栈的大小，栈内的元素个数不会超过 nn。

方法三：寻找前驱节点
前两种方法都借助前序遍历，前序遍历过程中需要使用栈存储节点。有没有空间复杂度是 O(1)O(1) 的做法呢？

注意到前序遍历访问各节点的顺序是根节点、左子树、右子树。如果一个节点的左子节点为空，则该节点不需要进行展开操作。如果一个节点的左子节点不为空，则该节点的左子树中的最后一个节点被访问之后，该节点的右子节点被访问。该节点的左子树中最后一个被访问的节点是左子树中的最右边的节点，也是该节点的前驱节点。因此，问题转化成寻找当前节点的前驱节点。

具体做法是，对于当前节点，如果其左子节点不为空，则在其左子树中找到最右边的节点，作为前驱节点，将当前节点的右子节点赋给前驱节点的右子节点，然后将当前节点的左子节点赋给当前节点的右子节点，并将当前节点的左子节点设为空。对当前节点处理结束后，继续处理链表中的下一个节点，直到所有节点都处理结束。


1 / 18

JavaC++GolangPython3JavaScriptC

class Solution:
    def flatten(self, root: TreeNode) -> None:
        curr = root
        while curr:
            if curr.left:
                predecessor = nxt = curr.left
                while predecessor.right:
                    predecessor = predecessor.right
                predecessor.right = curr.right
                curr.left = None
                curr.right = nxt
            curr = curr.right
复杂度分析

时间复杂度：O(n)O(n)，其中 nn 是二叉树的节点数。展开为单链表的过程中，需要对每个节点访问一次，在寻找前驱节点的过程中，每个节点最多被额外访问一次。

空间复杂度：O(1)O(1)。

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

