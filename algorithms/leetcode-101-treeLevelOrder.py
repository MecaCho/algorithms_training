'''

102. Binary Tree Level Order Traversal
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]

102. 二叉树的层次遍历
给定一个二叉树，返回其按层次遍历的节点值。 （即逐层地，从左到右访问所有节点）。

例如:
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：

[
  [3],
  [9,20],
  [15,7]
]
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []

        def deep_trave(root, deepth, res=[]):
            if not root:
                return res
            if len(res) < deepth + 1:
                res.append([root.val])
            else:
                res[deepth].append(root.val)
            deep_trave(root.left, deepth + 1, res)
            deep_trave(root.right, deepth + 1, res)
            return res

        res = deep_trave(root, 0, res=res)
        return res


'''
方法一：宽度优先搜索
思路和算法

我们可以用宽度优先搜索解决这个问题。

我们可以想到最朴素的方法是用一个二元组 (node, level) 来表示状态，它表示某个节点和它所在的层数，每个新进队列的节点的 level 值都是父亲节点的 level 值加一。最后根据每个点的 level 对点进行分类，分类的时候我们可以利用哈希表，维护一个以 level 为键，对应节点值组成的数组为值，宽度优先搜索结束以后按键 level 从小到大取出所有值，组成答案返回即可。

考虑如何优化空间开销：如何不用哈希映射，并且只用一个变量 node 表示状态，实现这个功能呢？

我们可以用一种巧妙的方法修改 BFS：

首先根元素入队
当队列不为空的时候
求当前队列的长度 s_is 
i
​	
 
依次从队列中取 s_is 
i
​	
  个元素进行拓展，然后进入下一次迭代
它和 BFS 的区别在于 BFS 每次只取一个元素拓展，而这里每次取 s_is 
i
​	
  个元素。在上述过程中的第 ii 次迭代就得到了二叉树的第 ii 层的 s_is 
i
​	
  个元素。

为什么这么做是对的呢？我们观察这个算法，可以归纳出这样的循环不变式：第 ii 次迭代前，队列中的所有元素就是第 ii 层的所有元素，并且按照从左向右的顺序排列。证明它的三条性质（你也可以把它理解成数学归纳法）：

初始化：i = 1i=1 的时候，队列里面只有 root，是唯一的层数为 11 的元素，因为只有一个元素，所以也显然满足「从左向右排列」；
保持：如果 i = ki=k 时性质成立，即第 kk 轮中出队 s_ks 
k
​	
  的元素是第 kk 层的所有元素，并且顺序从左到右。因为对树进行 BFS 的时候由低 kk 层的点拓展出的点一定也只能是 k + 1k+1 层的点，并且 k + 1k+1 层的点只能由第 kk 层的点拓展到，所以由这 s_ks 
k
​	
  个点能拓展到下一层所有的 s_{k+1}s 
k+1
​	
  个点。又因为队列的先进先出（FIFO）特性，既然第 kk 层的点的出队顺序是从左向右，那么第 k + 1k+1 层也一定是从左向右。至此，我们已经可以通过数学归纳法证明循环不变式的正确性。
终止：因为该循环不变式是正确的，所以按照这个方法迭代之后每次迭代得到的也就是当前层的层次遍历结果。至此，我们证明了算法是正确的。
代码

C++JavaScriptGolang

func levelOrder(root *TreeNode) [][]int {
    ret := [][]int{}
    if root == nil {
        return ret
    }
    q := []*TreeNode{root}
    for i := 0; len(q) > 0; i++ {
        ret = append(ret, []int{})
        p := []*TreeNode{}
        for j := 0; j < len(q); j++ {
            node := q[j]
            ret[i] = append(ret[i], node.Val)
            if node.Left != nil {
                p = append(p, node.Left)
            }
            if node.Right != nil {
                p = append(p, node.Right)
            }
        }
        q = p
    }
    return ret
}
复杂度分析

记树上所有节点的个数为 nn。

时间复杂度：每个点进队出队各一次，故渐进时间复杂度为 O(n)O(n)。
空间复杂度：队列中元素的个数不超过 nn 个，故渐进空间复杂度为 O(n)O(n)。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/binary-tree-level-order-traversal/solution/er-cha-shu-de-ceng-xu-bian-li-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
