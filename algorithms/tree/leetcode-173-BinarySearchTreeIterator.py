# encoding=utf8

'''
173. Binary Search Tree Iterator
Implement the BSTIterator class that represents an iterator over the in-order traversal of a binary search tree (BST):

BSTIterator(TreeNode root) Initializes an object of the BSTIterator class. The root of the BST is given as part of the constructor. The pointer should be initialized to a non-existent number smaller than any element in the BST.
boolean hasNext() Returns true if there exists a number in the traversal to the right of the pointer, otherwise returns false.
int next() Moves the pointer to the right, then returns the number at the pointer.
Notice that by initializing the pointer to a non-existent smallest number, the first call to next() will return the smallest element in the BST.

You may assume that next() calls will always be valid. That is, there will be at least a next number in the in-order traversal when next() is called.



Example 1:


Input
["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
[[[7, 3, 15, null, null, 9, 20]], [], [], [], [], [], [], [], [], []]
Output
[null, 3, 7, true, 9, true, 15, true, 20, false]

Explanation
BSTIterator bSTIterator = new BSTIterator([7, 3, 15, null, null, 9, 20]);
bSTIterator.next();    // return 3
bSTIterator.next();    // return 7
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 9
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 15
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 20
bSTIterator.hasNext(); // return False


Constraints:

The number of nodes in the tree is in the range [1, 105].
0 <= Node.val <= 106
At most 105 calls will be made to hasNext, and next.


Follow up:

Could you implement next() and hasNext() to run in average O(1) time and use O(h) memory, where h is the height of the tree?


173. 二叉搜索树迭代器
实现一个二叉搜索树迭代器类BSTIterator ，表示一个按中序遍历二叉搜索树（BST）的迭代器：
BSTIterator(TreeNode root) 初始化 BSTIterator 类的一个对象。BST 的根节点 root 会作为构造函数的一部分给出。指针应初始化为一个不存在于 BST 中的数字，且该数字小于 BST 中的任何元素。
boolean hasNext() 如果向指针右侧遍历存在数字，则返回 true ；否则返回 false 。
int next()将指针向右移动，然后返回指针处的数字。
注意，指针初始化为一个不存在于 BST 中的数字，所以对 next() 的首次调用将返回 BST 中的最小元素。

你可以假设 next() 调用总是有效的，也就是说，当调用 next() 时，BST 的中序遍历中至少存在一个下一个数字。



示例：


输入
["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
[[[7, 3, 15, null, null, 9, 20]], [], [], [], [], [], [], [], [], []]
输出
[null, 3, 7, true, 9, true, 15, true, 20, false]

解释
BSTIterator bSTIterator = new BSTIterator([7, 3, 15, null, null, 9, 20]);
bSTIterator.next();    // 返回 3
bSTIterator.next();    // 返回 7
bSTIterator.hasNext(); // 返回 True
bSTIterator.next();    // 返回 9
bSTIterator.hasNext(); // 返回 True
bSTIterator.next();    // 返回 15
bSTIterator.hasNext(); // 返回 True
bSTIterator.next();    // 返回 20
bSTIterator.hasNext(); // 返回 False


提示：

树中节点的数目在范围 [1, 105] 内
0 <= Node.val <= 106
最多调用 105 次 hasNext 和 next 操作


进阶：

你可以设计一个满足下述条件的解决方案吗？next() 和 hasNext() 操作均摊时间复杂度为 O(1) ，并使用 O(h) 内存。其中 h 是树的高度。

'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator(object):

    def traversal(self, root):
        vals = []
        if not root:
            return vals
        stack = [(0, root)]
        while stack:
            flag, node = stack.pop()
            if node:
                if flag:
                    vals.append(node.val)
                else:
                    stack.append((0, node.right))
                    stack.append((1, node))
                    stack.append((0, node.left))
        return vals


    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.vals = self.traversal(root)
        self.length = len(self.vals)
        self.index = 0


    def next(self):
        """
        :rtype: int
        """
        val = None
        if self.hasNext:
            val = self.vals[self.index]
            self.index += 1
        return val


    def hasNext(self):
        """
        :rtype: bool
        """
        return self.index < self.length



# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()


# solutions


'''
前言
根据二叉搜索树的性质，不难发现，原问题等价于对二叉搜索树进行中序遍历。因此，我们可以采取与「94. 二叉树的中序遍历」类似的方法来解决这一问题。

下面基于「94. 二叉树的中序遍历的官方题解」，给出本题的两种解法。读者将不难发现两篇题解的代码存在诸多相似之处。

方法一：扁平化
我们可以直接对二叉搜索树做一次完全的递归遍历，获取中序遍历的全部结果并保存在数组中。随后，我们利用得到的数组本身来实现迭代器。

C++JavaGolangJavaScriptC

type BSTIterator struct {
    arr []int
}

func Constructor(root *TreeNode) (it BSTIterator) {
    it.inorder(root)
    return
}

func (it *BSTIterator) inorder(node *TreeNode) {
    if node == nil {
        return
    }
    it.inorder(node.Left)
    it.arr = append(it.arr, node.Val)
    it.inorder(node.Right)
}

func (it *BSTIterator) Next() int {
    val := it.arr[0]
    it.arr = it.arr[1:]
    return val
}

func (it *BSTIterator) HasNext() bool {
    return len(it.arr) > 0
}
复杂度分析

时间复杂度：初始化需要 O(n)O(n) 的时间，其中 nn 为树中节点的数量。随后每次调用只需要 O(1)O(1) 的时间。

空间复杂度：O(n)O(n)，因为需要保存中序遍历的全部结果。

方法二：迭代
除了递归的方法外，我们还可以利用栈这一数据结构，通过迭代的方式对二叉树做中序遍历。此时，我们无需预先计算出中序遍历的全部结果，只需要实时维护当前栈的情况即可。

C++JavaGolangJavaScriptC

type BSTIterator struct {
    stack []*TreeNode
    cur   *TreeNode
}

func Constructor(root *TreeNode) BSTIterator {
    return BSTIterator{cur: root}
}

func (it *BSTIterator) Next() int {
    for node := it.cur; node != nil; node = node.Left {
        it.stack = append(it.stack, node)
    }
    it.cur, it.stack = it.stack[len(it.stack)-1], it.stack[:len(it.stack)-1]
    val := it.cur.Val
    it.cur = it.cur.Right
    return val
}

func (it *BSTIterator) HasNext() bool {
    return it.cur != nil || len(it.stack) > 0
}
复杂度分析

时间复杂度：显然，初始化和调用 \text{hasNext()}hasNext() 都只需要 O(1)O(1) 的时间。每次调用 \text{next()}next() 函数最坏情况下需要 O(n)O(n) 的时间；但考虑到 nn 次调用 \text{next()}next() 函数总共会遍历全部的 nn 个节点，因此总的时间复杂度为 O(n)O(n)，因此单次调用平均下来的均摊复杂度为 O(1)O(1)。

空间复杂度：O(n)O(n)，其中 nn 是二叉树的节点数量。空间复杂度取决于栈深度，而栈深度在二叉树为一条链的情况下会达到 O(n)O(n) 的级别。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/binary-search-tree-iterator/solution/er-cha-sou-suo-shu-die-dai-qi-by-leetcod-4y0y/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
