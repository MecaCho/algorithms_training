'''
1028. 从先序遍历还原二叉树
我们从二叉树的根节点 root 开始进行深度优先搜索。

在遍历中的每个节点处，我们输出 D 条短划线（其中 D 是该节点的深度），然后输出该节点的值。（如果节点的深度为 D，则其直接子节点的深度为 D + 1。根节点的深度为 0）。

如果节点只有一个子节点，那么保证该子节点为左子节点。

给出遍历输出 S，还原树并返回其根节点 root。



示例 1：



输入："1-2--3--4-5--6--7"
输出：[1,2,5,3,4,6,7]
示例 2：



输入："1-2--3---4-5--6---7"
输出：[1,2,5,3,null,6,null,4,null,7]
示例 3：



输入："1-401--349---90--88"
输出：[1,401,null,349,88,90]


提示：

原始树中的节点数介于 1 和 1000 之间。
每个节点的值介于 1 和 10 ^ 9 之间。

1028. Recover a Tree From Preorder Traversal
We run a preorder depth first search on the root of a binary tree.

At each node in this traversal, we output D dashes (where D is the depth of this node), then we output the value of this node.  (If the depth of a node is D, the depth of its immediate child is D+1.  The depth of the root node is 0.)

If a node has only one child, that child is guaranteed to be the left child.

Given the output S of this traversal, recover the tree and return its root.



Example 1:



Input: "1-2--3--4-5--6--7"
Output: [1,2,5,3,4,6,7]
Example 2:



Input: "1-2--3---4-5--6---7"
Output: [1,2,5,3,null,6,null,4,null,7]


Example 3:



Input: "1-401--349---90--88"
Output: [1,401,null,349,88,90]


Note:

The number of nodes in the original tree is between 1 and 1000.
Each node will have a value between 1 and 10^9.
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def recoverFromPreorder(self, S):
        """
        :type S: str
        :rtype: TreeNode
        """
        self.vals = []
        chs = [""] + re.split(r'(\-*)', S)

        for i in range(len(chs)):
            if i % 2 == 0:
                self.vals.append((chs[i].count("-"), int(chs[i + 1])))

        def dfs(l, level):
            if not l:
                return None

            deepth, node = l.pop(0)

            loc = None
            for i in range(len(l)):
                if i > 0 and l[i][0] == level + 1:
                    loc = i
                    break
            left = l[:loc] if loc else l
            r = l[loc:] if loc else []
            root = TreeNode(node)

            root.left = dfs(left, level + 1)
            root.right = dfs(r, level + 1)

            return root

        return dfs(self.vals, 0)

# Runtime: 72 ms, faster than 88.70% of Python online submissions for Recover a Tree From Preorder Traversal.
# Memory Usage: 13.9 MB, less than 26.80% of Python online submissions for Recover a Tree From Preorder Traversal.

# tips
'''
Do an iterative depth first search, parsing dashes from the string to inform you how to link the nodes together.
'''


# solutions

'''
前言
相较于传统的递归 + 回溯的实现方法而言，本题使用迭代方法（模拟递归）更加简洁方便。

方法一：迭代
我们每次从字符串 ss 中取出一个节点的值以及它的深度信息。具体地：

我们首先读取若干个字符 -，直到遇到非 - 字符位置。通过 - 的个数，我们就可以知道当前节点的深度信息；

我们再读取若干个数字，直到遇到非数字或者字符串的结尾。通过这些数字，我们就可以知道当前节点的值。

得到这些信息之后，我们就需要考虑将当前的节点放在何处。记当前节点为 TT，上一个节点为 SS，那么实际上只有两种情况：

TT 是 SS 的左子节点；

TT 是根节点到 SS 这一条路径上（不包括 SS）某一个节点的右子节点。

为什么不包括 SS？因为题目中规定了如果节点只有一个子节点，那么保证该子节点为左子节点。在 TT 出现之前，SS 仍然还是一个叶节点，没有左子节点，因此 TT 如果是 SS 的子节点，一定是优先变成 SS 的左子节点。
这是因为先序遍历本身的性质。在先序遍历中，我们是通过「根 — 左 — 右」的顺序访问每一个节点的。想一想先序遍历的递归 + 回溯方法，对于在先序遍历中任意的两个相邻的节点 SS 和 TT，要么 TT 就是 SS 的左子节点（对应上面的第一种情况），要么在遍历到 SS 之后发现 SS 是个叶节点，于是回溯到之前的某个节点，并开始递归地遍历其右子节点（对应上面的第二种情况）。这样以来，我们按照顺序维护从根节点到当前节点的路径上的所有节点，就可以方便地处理这两种情况。仔细想一想，这实际上就是使用递归 + 回溯的方法遍历一棵树时，栈中的所有节点，也就是可以回溯到的节点。因此我们只需要使用一个栈来模拟递归 + 回溯即可。

回到上面的分析，当我们得到当前节点的值以及深度信息之后，我们可以发现：如果 TT 是 SS 的左子节点，那么 TT 的深度恰好比 SS 的深度大 11；在其它的情况下，TT 是栈中某个节点（不包括 SS）的右子节点，那么我们将栈顶的节点不断地出栈，直到 TT 的深度恰好比栈顶节点的深度大 11，此时我们就找到了 TT 的双亲节点。

扩展与思考

通过上面的分析，我们只需要借助一个栈，通过迭代的方法就可以还原出这棵二叉树。由于题目给出的 SS 一定是某棵二叉树的先序遍历结果，因此我们在代码中不需要处理任何异常异常情况。

读者可以进行如下的思考：如果给定的 SS 只保证由数字和 - 组成，那么我们如何修改代码，使其判断是否能够还原出一棵二叉树呢？

C++Python3JavaGolang

func recoverFromPreorder(S string) *TreeNode {
    path, pos := []*TreeNode{}, 0
    for pos < len(S) {
        level := 0
        for S[pos] == '-' {
            level++
            pos++
        }
        value := 0
        for ; pos < len(S) && S[pos] >= '0' && S[pos] <= '9'; pos++ {
            value = value * 10 + int(S[pos] - '0')
        }
        node := &TreeNode{Val: value}
        if level == len(path) {
            if len(path) > 0 { path[len(path)-1].Left = node }
        } else {
            path = path[:level]
            path[len(path)-1].Right = node
        }
        path = append(path, node)
    }
    return path[0]
}
复杂度分析

时间复杂度：O(|s|)O(∣s∣)，其中 |s|∣s∣ 是字符串 ss 的长度。我们的算法不断地从 SS 中取出一个节点的信息，直到取完为止。在这个过程中，我们实际上是对 SS 进行了一次遍历。

时间复杂度：O(h)O(h)，其中 hh 是还原出的二叉树的高度。除了作为答案返回的二叉树使用的空间以外，我们使用了一个栈帮助我们进行迭代。由于栈中存放了从根节点到当前节点这一路径上的所有节点，因此最多只会同时由 hh 个节点。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/recover-a-tree-from-preorder-traversal/solution/cong-xian-xu-bian-li-huan-yuan-er-cha-shu-by-leetc/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''