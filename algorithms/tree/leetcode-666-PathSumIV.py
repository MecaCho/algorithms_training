


'''
666. 路径和 IV
对于一棵深度小于 5 的树，可以用一组三位十进制整数来表示。

对于每个整数：

百位上的数字表示这个节点的深度 D，1 <= D <= 4。
十位上的数字表示这个节点在当前层所在的位置 P， 1 <= P <= 8。位置编号与一棵满二叉树的位置编号相同。
个位上的数字表示这个节点的权值 V，0 <= V <= 9。
给定一个包含三位整数的升序数组，表示一棵深度小于 5 的二叉树，请你返回从根到所有叶子结点的路径之和。

样例 1:

输入: [113, 215, 221]
输出: 12
解释:
这棵树形状如下:
    3
   / \
  5   1

路径和 = (3 + 5) + (3 + 1) = 12.


样例 2:

输入: [113, 221]
输出: 4
解释:
这棵树形状如下:
    3
     \
      1

路径和 = (3 + 1) = 4.

666. Path Sum IV
If the depth of a tree is smaller than 5, then this tree can be represented by a list of three-digits integers.

For each integer in this list:

The hundreds digit represents the depth D of this node, 1 <= D <= 4.
The tens digit represents the position P of this node in the level it belongs to, 1 <= P <= 8. The position is the same as that in a full binary tree.
The units digit represents the value V of this node, 0 <= V <= 9.
Given a list of ascending three-digits integers representing a binary tree with the depth smaller than 5, you need to return the sum of all paths from the root towards the leaves.

It's guaranteed that the given list represents a valid connected binary tree.

Example 1:

Input: [113, 215, 221]
Output: 12
Explanation:
The tree that the list represents is:
    3
   / \
  5   1

The path sum is (3 + 5) + (3 + 1) = 12.


Example 2:

Input: [113, 221]
Output: 4
Explanation:
The tree that the list represents is:
    3
     \
      1

The path sum is (3 + 1) = 4.
'''


class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = self.right = None


class Solution(object):
    def pathSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        res = 0
        nodes = {}
        for num in nums:
            k = num / 10
            p = (k/10-1)*10 + (((k % 10) - 1) / 2+1)
            nodes[num/10] = num % 10
            if p in nodes:
                nodes[num/10] += nodes[p]
        for k, v in nodes.items():
            c = (k/10 + 1)*10 + (k % 10) * 2
            if c not in nodes and c-1 not in nodes:
                res += v
        return res


class Solution1(object):
    def pathSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        nodes = []
        locs = []
        for i in range(len(nums)):
            num = nums[i]
            seq = (num % 100) / 10
            deep = num / 100
            node = num%10
            if deep > 1:
                node = num%10 + nodes[deep-2][(seq-1)/2]

            if len(nodes) < deep:
                nodes.append([None for i in range(2**(deep-1))])
                nodes[deep-1][seq-1] = node
                locs.append([seq])
            else:

                nodes[deep-1][seq-1] = node
                locs[deep-1].append(seq)

        for i in range(len(nodes)):
            for j in locs[i]:
                if i == len(nodes) - 1 or (j*2 not in locs[i+1] and j*2 - 1 not in locs[i+1]):
                    res += nodes[i][j-1]
        return res


'''
方法一：转换成树 [Accepted]
将数组给定的数据构造一颗树。然后计算从根节点到每个叶子结点的路径之和，就得到答案。

算法：

分为两个步骤，构造树和遍历树。
在树的构造过程中，我们有深度、位置和权值这些信息，我们可以根据条件 pos - 1 < 2*(depth - 2) 来判断结点在右边还是左边。例如，当 depth = 4 时，pos 可取 1, 2, 3, 4, 5, 6, 7, 8，当 pos<=4 时，结点的位置在左边。
在遍历过程中，我们执行深度优先搜索的策略遍历树，并沿着我们所走过的路径记录当前和。每当我们到达一个叶结点 (node.left == null && node.right == null) 时，将该路径的和添加到答案中。
PythonJava
class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = self.right = None

class Solution(object):
    def pathSum(self, nums):
        self.ans = 0
        root = Node(nums[0] % 10)

        for x in nums[1:]:
            depth, pos, val = x/100, x/10 % 10, x % 10
            pos -= 1
            cur = root
            for d in xrange(depth - 2, -1, -1):
                if pos < 2**d:
                    cur.left = cur = cur.left or Node(val)
                else:
                    cur.right = cur = cur.right or Node(val)

                pos %= 2**d

        def dfs(node, running_sum = 0):
            if not node: return
            running_sum += node.val
            if not node.left and not node.right:
                self.ans += running_sum
            else:
                dfs(node.left, running_sum)
                dfs(node.right, running_sum)

        dfs(root)
        return self.ans
复杂度分析

时间复杂度：O(N)O(N)。其中 NN 是 nums 的长度。
空间复杂度：O(N)O(N)，深度优先搜索中隐式调用堆栈的大小。
方法二：直接遍历 [Accepted]
算法：
在方法 1 中，我们将在树上进行深度优先搜索。一个省时的想法是，我们根据等式 root = num / 10 = 10 * depth + pos 作为根节点的唯一标识符。则左子结点的标识符是 left = 10 * (depth + 1) + 2 * pos - 1，而右子节点则是 right = left + 1。

PythonJava
class Solution(object):
    def pathSum(self, nums):
        self.ans = 0
        values = {x / 10: x % 10 for x in nums}
        def dfs(node, running_sum = 0):
            if node not in values: return
            running_sum += values[node]
            depth, pos = divmod(node, 10)
            left = (depth + 1) * 10 + 2 * pos - 1
            right = left + 1

            if left not in values and right not in values:
                self.ans += running_sum
            else:
                dfs(left, running_sum)
                dfs(right, running_sum)

        dfs(nums[0] / 10)
        return self.ans
复杂度分析

时间复杂度：O(N)O(N)。
空间复杂度：O(N)O(N)，分析与方法 1 相同。

作者：LeetCode
链接：https://leetcode-cn.com/problems/path-sum-iv/solution/lu-jing-he-iv-by-leetcode/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''