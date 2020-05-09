'''
1257. 最小公共区域
给你一些区域列表 regions ，每个列表的第一个区域都包含这个列表内所有其他区域。

很自然地，如果区域 X 包含区域 Y ，那么区域 X  比区域 Y 大。

给定两个区域 region1 和 region2 ，找到同时包含这两个区域的 最小 区域。

如果区域列表中 r1 包含 r2 和 r3 ，那么数据保证 r2 不会包含 r3 。

数据同样保证最小公共区域一定存在。



示例 1：

输入：
regions = [["Earth","North America","South America"],
["North America","United States","Canada"],
["United States","New York","Boston"],
["Canada","Ontario","Quebec"],
["South America","Brazil"]],
region1 = "Quebec",
region2 = "New York"
输出："North America"


提示：

2 <= regions.length <= 10^4
region1 != region2
所有字符串只包含英文字母和空格，且最多只有 20 个字母。

1257. Smallest Common Region
You are given some lists of regions where the first region of each list includes all other regions in that list.

Naturally, if a region X contains another region Y then X is bigger than Y. Also by definition a region X contains itself.

Given two regions region1, region2, find out the smallest region that contains both of them.

If you are given regions r1, r2 and r3 such that r1 includes r3, it is guaranteed there is no r2 such that r2 includes r3.

It's guaranteed the smallest region exists.



Example 1:

Input:
regions = [["Earth","North America","South America"],
["North America","United States","Canada"],
["United States","New York","Boston"],
["Canada","Ontario","Quebec"],
["South America","Brazil"]],
region1 = "Quebec",
region2 = "New York"
Output: "North America"


Constraints:

2 <= regions.length <= 10^4
region1 != region2
All strings consist of English letters and spaces with at most 20 letters.
'''


class Solution(object):
    def findSmallestRegion(self, regions, region1, region2):
        """
        :type regions: List[List[str]]
        :type region1: str
        :type region2: str
        :rtype: str
        """
        trees = {}
        for i in range(len(regions)):
            for r in regions[i][1:]:
                trees[r] = regions[i][0]

        parents = []
        while region1:
            parents.append(region1)
            region1 = trees.get(region1)

        while region2:
            if region2 in parents:
                return region2
            region2 = trees.get(region2)


# tips

'''
Try to model the problem as a graph problem.
The given graph is a tree.
The problem is reduced to finding the lowest common ancestor of two nodes in a tree.
'''

'''
最近公共祖先问题
定义
最近公共祖先问题（LCA：Lowest common ancestor），指的是在“树”中寻找某两个结点的最近的公共祖先。

解决方案
设两个结点为a、b。

1、求路径，有2种思路

求正向路径：一般需要使用DFS/BFS遍历树：从根结点出发，直到遇到目标结点，同时记录当前路径。如果是BST，那么路径是唯一确定的，可以不用搜索，直接用二分查找。
求反向路径：对树进行预处理，也使用DFS/BFS遍历树，使用哈希表建立“结点 => 父结点”的映射。然后从目标结点出发，一直追溯到根结点，同时记录路径。
2、寻找，也有2种思路

使用双指针遍历：路径从根结点开始两两比较，第一个不同点（表示分叉）的上一个点就是LCA。
使用集合（哈希表）标记：路径从a到根结点全部标记，再从b出发，遇到的第一个相同点就是LCA。
题型
236. 二叉树的最近公共祖先，模板题
235. 二叉搜索树的最近公共祖先，在二叉树基础上进一步变为BST
5109. 最小公共区域，不必再建树
160. 相交链表，链表也是树
本题题解（JavaScript语言）
本题中，输入已经是对树中父子关系、兄弟关系的描述，所以并不需要再建树。直接找出路径即可。

这里我使用Set标记法：

/**
 * 哈希表：记录父结点
 * 
 * 时间：128ms
 */
var findSmallestRegion = function (regions, x, y) {
  const parent = new Map() // 记录父结点
  for (const [p, ...children] of regions) {
    for (const child of children) {
      parent.set(child, p)
    }
  }

  // 标记x的路径
  const xx = new Set()
  xx.add(x)
  while (parent.has(x)) {
    x = parent.get(x)
    xx.add(x)
  }

  // 从y开始寻找共同祖先
  if (xx.has(y)) return y
  while (parent.has(y)) {
    y = parent.get(y)
    if (xx.has(y)) return y
  }
};

'''