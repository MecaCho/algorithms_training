'''
250. 统计同值子树
给定一个二叉树，统计该二叉树数值相同的子树个数。

同值子树是指该子树的所有节点都拥有相同的数值。

示例：

输入: root = [5,1,5,5,5,null,5]

              5
             / \
            1   5
           / \   \
          5   5   5

输出: 4

250. Count Univalue Subtrees
Given a binary tree, count the number of uni-value subtrees.

A Uni-value subtree means all nodes of the subtree have the same value.

Example :

Input:  root = [5,1,5,5,5,null,5]

              5
             / \
            1   5
           / \   \
          5   5   5

Output: 4
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        self.vals = []
        def dfs(root, res):
            if not root:
                return res
            else:
                root_val = root.val
                left = dfs(root.left, [])
                right = dfs(root.right, [])
                tmp = left + [root_val] + right
                self.vals.append(tmp)
                return tmp
        dfs(root, [])
        print(self.vals)
        return len([i for i in self.vals if len(set(i)) == 1])


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution1(object):
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        # self.vals = []
        # def dfs(root, res):
        #     if not root:
        #         return res
        #     else:
        #         root_val = root.val
        #         left = dfs(root.left, [])
        #         right = dfs(root.right, [])
        #         tmp = left + [root_val] + right
        #         self.vals.append(tmp)
        #         return tmp
        # dfs(root, [])
        # print(self.vals)
        # return len([i for i in self.vals if len(set(i)) == 1])
        self.count = 0
        def dfs(root):
            if not root:
                return True
            else:
                root_val = root.val
                left = dfs(root.left)
                right = dfs(root.right)
                res = left and right
                if root.left and root_val != root.left.val:
                    return False
                if root.right and root_val != root.right.val:
                    return False
                if res:
                    self.count += 1
                return res
        dfs(root)
        # print(self.count)
        return self.count


'''
方法一：深度优先搜索
直觉

给定树中的一个结点，若其满足下面条件中的一个，则子树同值:

该节点没有子结点 （基本情况）
该节点的所有子结点都为同值子树，且结点与其子结点值相同。
这样我们可以在树中使用深度优先搜索，自底向上的判断每个子树是否为同值子树。


1 / 7

算法

PythonJava
class Solution:
    def countUnivalSubtrees(self, root):
        if root is None: return 0
        self.count = 0
        self.is_uni(root)
        return self.count

    def is_uni(self, node):

        # base case - if the node has no children this is a univalue subtree
        if node.left is None and node.right is None:

            # found a univalue subtree - increment
            self.count += 1
            return True

        is_uni = True

        # check if all of the node's children are univalue subtrees and if they have the same value
        # also recursively call is_uni for children
        if node.left is not None:
            is_uni = self.is_uni(node.left) and is_uni and node.left.val == node.val

        if node.right is not None:
            is_uni = self.is_uni(node.right) and is_uni and node.right.val == node.val

        # increment self.res and return whether a univalue tree exists here
        self.count += is_uni
        return is_uni
复杂度分析

时间复杂度 : O(N)O(N)。由于算法的深度优先特性，每个结点的 is_uni 状态是自底向上计算的。给定子结点的is_uni ，计算结点自身的 is_uni 只需要 O(1)O(1) 的时间。故每个结点需要 O(1)O(1) 时间，总复杂度为 O(N)O(N)。

空间复杂度 : O(H)O(H)， 其中 H 为树的高度。每次 is_uni 递归调用都需要栈空间。由于我们在调用 is_uni(node.right) 前会先处理完 is_uni(node.left)，递归栈的大小由从根到叶的最长路径决定 - 换而言之，是树的高度。




方法二：传父值的深度优先搜索
算法

我们可以利用方法一的思路进一步简化算法。我们不检查结点是否有子结点，而是将 null 值看做同值子树，只是不计数。

这样，如果一个结点有 null 子结点，该子结点被自动判定为有效的子树，这样算法就只检查其他子结点是否有效。

最后，辅助函数检查当前节点是否是有效的子树，它返回一个布尔值，指示该节点是否为其父节点的有效组成。这可以通过传入父节点的值来完成。

PythonJava
class Solution:
    def countUnivalSubtrees(self, root):
        self.count = 0
        self.is_valid_part(root, 0)
        return self.count


    def is_valid_part(self, node, val):

        # considered a valid subtree
        if node is None: return True

        # check if node.left and node.right are univalue subtrees of value node.val
        if not all([self.is_valid_part(node.left, node.val),
                    self.is_valid_part(node.right, node.val)]):
            return False

        # if it passed the last step then this a valid subtree - increment
        self.count += 1

        # at this point we know that this node is a univalue subtree of value node.val
        # pass a boolean indicating if this is a valid subtree for the parent node
        return node.val == val
复杂度分析

时间复杂度 : O(N)O(N)。 与上个方法相同。

空间复杂度 : O(H)O(H)。 与上个方法相同。

作者：LeetCode
链接：https://leetcode-cn.com/problems/count-univalue-subtrees/solution/tong-ji-tong-zhi-zi-shu-by-leetcode/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''