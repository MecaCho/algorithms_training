'''

101. Symmetric Tree
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
 

But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3
 

Note:
Bonus points if you could solve it both recursively and iteratively.


101. 对称二叉树
给定一个二叉树，检查它是否是镜像对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3
但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3
说明:

如果你可以运用递归和迭代两种方法解决这个问题，会很加分。
'''


'''
递归
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution1(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def is_mirror(root_left, root_right):
            if not root_left and not root_right:
                return True
            if not root_right or not root_left:
                return False
            if root_left.val != root_right.val:
                return False
            return is_mirror(root_left.right, root_right.left) and is_mirror(root_left.left, root_right.right)
        return is_mirror(root, root)


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # val_list = []
        def dfs(root, res=[]):
            if not root:
                return [None]
            l = dfs(root.left)
            r = dfs(root.right)
            if l or r:
                l = [None] if not l else l
                r = [None] if not r else r
            return l + [root.val] + r

        def root_trave_pre(q, res=[]):
            if not q:
                return []
            l = root_trave_pre(q.left)
            r = root_trave_pre(q.right)
            if not l and r:
                l = [None]
            res =  r + l + [q.val]
            return res

        def root_trave_pro(q, res=[]):
            if not q:
                return []
            l = root_trave_pro(q.left)
            r = root_trave_pro(q.right)
            if not r and l:
                r = [None]
            res =  l + r + [q.val]
            return res

        pre_vals = root_trave_pro(root)
        pro_vals = root_trave_pre(root)
        return pre_vals == pro_vals



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

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func isMiorr(p, q *TreeNode) bool {

	if p == nil && q == nil {
		return true
	}

	if p == nil || q == nil {
		return false
	}

	return p.Val == q.Val && isMiorr(q.Right, p.Left) && isMiorr(q.Left, p.Right)

}

func isSymmetric(root *TreeNode) bool {
	//
	// if root.Left == nil && root.Right == nil {
	// 	return true
	// }
	//
	// if root.Left == nil || root.Right == nil {
	// 	return false
	// }
	//
	// if root.Left.Val != root.Right.Val {
	// 	return false
	// }

	return isMiorr(root, root)
}

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func isMiorr(p, q *TreeNode) bool {

	if p == nil && q == nil {
		return true
	}

	if p == nil || q == nil {
		return false
	}

	return p.Val == q.Val && isMiorr(q.Right, p.Left) && isMiorr(q.Left, p.Right)

}

// 迭代

func isSymmetric1(root *TreeNode) bool {

	// return isMiorr(root, root)
	queue := []*TreeNode{}

	queue = append(queue, root)

	for len(queue) > 0 {

		vals := []int{}
		for _, node := range queue {
			if node != nil {
				vals = append(vals, node.Val)
			} else {
				vals = append(vals, math.MinInt16)
			}

		}

		for i := range vals {
			if vals[i] != vals[len(vals)-1-i] {
				return false
			}
		}

		newQueue := []*TreeNode{}

		for i := range queue {
			if queue[i] != nil {
				newQueue = append(newQueue, queue[i].Left)
				newQueue = append(newQueue, queue[i].Right)
			}

		}

		queue = newQueue

	}

	return true

}
'''


# solutions

'''
方法一：递归
思路和算法

如果一个树的左子树与右子树镜像对称，那么这个树是对称的。



因此，该问题可以转化为：两个树在什么情况下互为镜像？

如果同时满足下面的条件，两个树互为镜像：

它们的两个根结点具有相同的值
每个树的右子树都与另一个树的左子树镜像对称


我们可以实现这样一个递归函数，通过「同步移动」两个指针的方法来遍历这棵树，pp 指针和 qq 指针一开始都指向这棵树的根，随后 pp 右移时，qq 左移，pp 左移时，qq 右移。每次检查当前 pp 和 qq 节点的值是否相等，如果相等再判断左右子树是否对称。

代码如下。

C++JavaGolangTypeScript
func isSymmetric(root *TreeNode) bool {
    return check(root, root)
}

func check(p, q *TreeNode) bool {
    if p == nil && q == nil {
        return true
    }
    if p == nil || q == nil {
        return false
    }
    return p.Val == q.Val && check(p.Left, q.Right) && check(p.Right, q.Left) 
}
复杂度分析

假设树上一共 nn 个节点。

时间复杂度：这里遍历了这棵树，渐进时间复杂度为 O(n)O(n)。
空间复杂度：这里的空间复杂度和递归使用的栈空间有关，这里递归层数不超过 nn，故渐进空间复杂度为 O(n)O(n)。
方法二：迭代
思路和算法

「方法一」中我们用递归的方法实现了对称性的判断，那么如何用迭代的方法实现呢？首先我们引入一个队列，这是把递归程序改写成迭代程序的常用方法。初始化时我们把根节点入队两次。每次提取两个结点并比较它们的值（队列中每两个连续的结点应该是相等的，而且它们的子树互为镜像），然后将两个结点的左右子结点按相反的顺序插入队列中。当队列为空时，或者我们检测到树不对称（即从队列中取出两个不相等的连续结点）时，该算法结束。

C++JavaGolangTypeScript
func isSymmetric(root *TreeNode) bool {
    u, v := root, root
    q := []*TreeNode{}
    q = append(q, u)
    q = append(q, v)
    for len(q) > 0 {
        u, v = q[0], q[1]
        q = q[2:]
        if u == nil && v == nil {
            continue
        }
        if u == nil || v == nil {
            return false
        }
        if u.Val != v.Val {
            return false
        }
        q = append(q, u.Left)
        q = append(q, v.Right)

        q = append(q, u.Right)
        q = append(q, v.Left)
    }
    return true
}
复杂度分析

时间复杂度：O(n)O(n)，同「方法一」。
空间复杂度：这里需要用一个队列来维护节点，每个节点最多进队一次，出队一次，队列中最多不会超过 nn 个点，故渐进空间复杂度为 O(n)O(n)。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/symmetric-tree/solution/dui-cheng-er-cha-shu-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''