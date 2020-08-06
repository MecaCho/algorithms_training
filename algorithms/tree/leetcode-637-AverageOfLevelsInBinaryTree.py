
'''
637. 二叉树的层平均值
给定一个非空二叉树, 返回一个由每层节点平均值组成的数组.

示例 1:

输入:
    3
   / \
  9  20
    /  \
   15   7
输出: [3, 14.5, 11]
解释:
第0层的平均值是 3,  第1层是 14.5, 第2层是 11. 因此返回 [3, 14.5, 11].
注意：

节点值的范围在32位有符号整数范围内。

637. Average of Levels in Binary Tree
Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.
Example 1:
Input:
    3
   / \
  9  20
    /  \
   15   7
Output: [3, 14.5, 11]
Explanation:
The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].
Note:
The range of node's value is in the range of 32-bit signed integer.
'''






# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        self.vals = []
        def traversal(root, deepth):
            if not root:
                return
            root_val = root.val
            if not self.vals or len(self.vals) <= deepth:
                self.vals.append([root_val])
            else:
                self.vals[deepth].append(root_val)

            traversal(root.left, deepth+1)
            traversal(root.right, deepth+1)

        traversal(root, 0)
        # print(self.vals)

        res = []
        for l in self.vals:
            res.append(float(sum(l))/ len(l))
        return res


'''
方法一：深度优先搜索
我们可以使用深度优先搜索遍历整颗二叉树。我们使用两个数组 sum 存放树中每一层的节点数值之和，以及 count 存放树中每一层的节点数量之和。在遍历时，我们需要额外记录当前节点所在的高度，并根据高度 h 更新数组元素 sum[h] 和 count[h]。在遍历结束之后，res = sum / cnt 即为答案。


1 / 8

Java
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    public List < Double > averageOfLevels(TreeNode root) {
        List < Integer > count = new ArrayList < > ();
        List < Double > res = new ArrayList < > ();
        average(root, 0, res, count);
        for (int i = 0; i < res.size(); i++)
            res.set(i, res.get(i) / count.get(i));
        return res;
    }
    public void average(TreeNode t, int i, List < Double > sum, List < Integer > count) {
        if (t == null)
            return;
        if (i < sum.size()) {
            sum.set(i, sum.get(i) + t.val);
            count.set(i, count.get(i) + 1);
        } else {
            sum.add(1.0 * t.val);
            count.add(1);
        }
        average(t.left, i + 1, sum, count);
        average(t.right, i + 1, sum, count);
    }
}
复杂度分析

时间复杂度：O(N)O(N)，其中 NN 是树中的节点个数。

空间复杂度：O(H)O(H)，其中 HH 是树的高度，即为深度优先搜索中使用递归占用的栈空间。

方法二：广度优先搜索
我们同样也可以使用广度优先搜索遍历整颗二叉树。
首先我们将根节点放入队列 queue 中，随后对于 queue 中的每一个节点，我们将它的子节点放入临时队列 temp 中。
在 queue 中的所有节点都处理完毕后，temp 中即存放了所有在 queue 对应的层数的下一层中的节点。
在将子节点放入 temp 的过程中，我们也可以顺便计算出 queue 中节点的数值之和，以此得到平均值。
最后我们将 temp 赋值给 queue，继续进行下一轮的广度优先搜索，直到某一轮 temp 为空。


1 / 16

Java
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    public List < Double > averageOfLevels(TreeNode root) {
        List < Double > res = new ArrayList < > ();
        Queue < TreeNode > queue = new LinkedList < > ();
        queue.add(root);
        while (!queue.isEmpty()) {
            long sum = 0, count = 0;
            Queue < TreeNode > temp = new LinkedList < > ();
            while (!queue.isEmpty()) {
                TreeNode n = queue.remove();
                sum += n.val;
                count++;
                if (n.left != null)
                    temp.add(n.left);
                if (n.right != null)
                    temp.add(n.right);
            }
            queue = temp;
            res.add(sum * 1.0 / count);
        }
        return res;
    }
}
复杂度分析

时间复杂度：O(N)O(N)，其中 NN 是树中的节点个数。

空间复杂度：O(M)O(M)，其中 MM 是树中每一层节点个数的最大值，即为广度优先搜索中使用队列存储同一层节点需要的空间。

作者：LeetCode
链接：https://leetcode-cn.com/problems/average-of-levels-in-binary-tree/solution/er-cha-shu-de-ceng-ping-jun-zhi-by-leetcode/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''