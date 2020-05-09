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

'''