# encoding=utf8


'''
993. Cousins in Binary Tree

In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.

Two nodes of a binary tree are cousins if they have the same depth, but have different parents.

We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.

Return true if and only if the nodes corresponding to the values x and y are cousins.

 

Example 1:


Input: root = [1,2,3,4], x = 4, y = 3
Output: false
Example 2:


Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true
Example 3:



Input: root = [1,2,3,null,4], x = 2, y = 3
Output: false
 

Constraints:

The number of nodes in the tree will be between 2 and 100.
Each node has a unique integer value from 1 to 100.


993. 二叉树的堂兄弟节点

在二叉树中，根节点位于深度 0 处，每个深度为 k 的节点的子节点位于深度 k+1 处。

如果二叉树的两个节点深度相同，但 父节点不同 ，则它们是一对堂兄弟节点。

我们给出了具有唯一值的二叉树的根节点 root ，以及树中两个不同节点的值 x 和 y 。

只有与值 x 和 y 对应的节点是堂兄弟节点时，才返回 true 。否则，返回 false。

 

示例 1：


输入：root = [1,2,3,4], x = 4, y = 3
输出：false
示例 2：


输入：root = [1,2,3,null,4,null,5], x = 5, y = 4
输出：true
示例 3：



输入：root = [1,2,3,null,4], x = 2, y = 3
输出：false
 

提示：

二叉树的节点数介于 2 到 100 之间。
每个节点的值都是唯一的、范围为 1 到 100 的整数。
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        self.x_deepth, self.x_parent = None, None
        self.y_deepth, self.y_parent = None, None
        self.x_found, self.y_found = False, False
        def dfs(root, p, deepth):
            if not root:
                return 
            if x == root.val:
                self.x_found = True
                self.x_parent = p
                self.x_deepth = deepth
            if y == root.val:
                self.y_found = True
                self.y_parent = p
                self.y_deepth = deepth
            if self.x_found and self.y_found:
                return
            dfs(root.left, root, deepth+1)
            dfs(root.right, root, deepth+1)
        dfs(root, None, 0)
        # print(self.x_parent, self.y_parent)
        if self.x_deepth == self.y_deepth and self.x_parent != self.y_parent:
            return True
        return False

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        self.node_x = (None, 0)
        self.node_y = (None, 0)
        def dfs(root, p, depth):
            if not root:
                return
            if root.val == x:
                # print(p, depth)
                self.node_x = (p, depth)
            if root.val == y:
                self.node_y = (p, depth)
            dfs(root.left, root, depth+1)
            dfs(root.right, root, depth+1)
        dfs(root, None, 0)
        # print(self.node_x, self.node_y)
        if self.node_x[0] != self.node_y[0] and self.node_x[1] == self.node_y[1]:
            return True
        return False


# solutions

'''
前言
要想判断两个节点 xx 和 yy 是否为堂兄弟节点，我们就需要求出这两个节点分别的「深度」以及「父节点」。

因此，我们可以从根节点开始，对树进行一次遍历，在遍历的过程中维护「深度」以及「父节点」这两个信息。当我们遍历到 xx 或 yy 节点时，就将信息记录下来；当这两个节点都遍历完成了以后，我们就可以退出遍历的过程，判断它们是否为堂兄弟节点了。

常见的遍历方法有两种：深度优先搜索和广度优先搜索。

方法一：深度优先搜索
思路与算法

我们只需要在深度优先搜索的递归函数中增加表示「深度」以及「父节点」的两个参数即可。

代码

C++JavaC#Python3JavaScriptGolangC

func isCousins(root *TreeNode, x, y int) bool {
    var xParent, yParent *TreeNode
    var xDepth, yDepth int
    var xFound, yFound bool

    var dfs func(node, parent *TreeNode, depth int)
    dfs = func(node, parent *TreeNode, depth int) {
        if node == nil {
            return
        }

        if node.Val == x {
            xParent, xDepth, xFound = parent, depth, true
        } else if node.Val == y {
            yParent, yDepth, yFound = parent, depth, true
        }

        // 如果两个节点都找到了，就可以提前退出遍历
        // 即使不提前退出，对最坏情况下的时间复杂度也不会有影响
        if xFound && yFound {
            return
        }

        dfs(node.Left, node, depth+1)

        if xFound && yFound {
            return
        }

        dfs(node.Right, node, depth+1)
    }
    dfs(root, nil, 0)

    return xDepth == yDepth && xParent != yParent
}
复杂度分析

时间复杂度：O(n)O(n)，其中 nn 是树中的节点个数。在最坏情况下，我们需要遍历整棵树，时间复杂度为 O(n)O(n)。

空间复杂度：O(n)O(n)，即为深度优先搜索的过程中需要使用的栈空间。在最坏情况下，树呈现链状结构，递归的深度为 O(n)O(n)。

方法二：广度优先搜索
思路与算法

在广度优先搜索的过程中，每当我们从队首取出一个节点，它就会作为「父节点」，将最多两个子节点放入队尾。因此，除了节点以外，我们只需要在队列中额外存储「深度」的信息即可。

代码

C++JavaC#Python3JavaScriptGolangC

func isCousins(root *TreeNode, x, y int) bool {
    var xParent, yParent *TreeNode
    var xDepth, yDepth int
    var xFound, yFound bool

    // 用来判断是否遍历到 x 或 y 的辅助函数
    update := func(node, parent *TreeNode, depth int) {
        if node.Val == x {
            xParent, xDepth, xFound = parent, depth, true
        } else if node.Val == y {
            yParent, yDepth, yFound = parent, depth, true
        }
    }

    type pair struct {
        node  *TreeNode
        depth int
    }
    q := []pair{{root, 0}}
    update(root, nil, 0)
    for len(q) > 0 && (!xFound || !yFound) {
        node, depth := q[0].node, q[0].depth
        q = q[1:]
        if node.Left != nil {
            q = append(q, pair{node.Left, depth + 1})
            update(node.Left, node, depth+1)
        }
        if node.Right != nil {
            q = append(q, pair{node.Right, depth + 1})
            update(node.Right, node, depth+1)
        }
    }

    return xDepth == yDepth && xParent != yParent
}
复杂度分析

时间复杂度：O(n)O(n)，其中 nn 是树中的节点个数。在最坏情况下，我们需要遍历整棵树，时间复杂度为 O(n)O(n)。

空间复杂度：O(n)O(n)，即为广度优先搜索的过程中需要使用的队列空间。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/cousins-in-binary-tree/solution/er-cha-shu-de-tang-xiong-di-jie-dian-by-mfh2d/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
