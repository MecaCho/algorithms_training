# encoding=utf8

'''
959. Regions Cut By Slashes
In a N x N grid composed of 1 x 1 squares, each 1 x 1 square consists of a /, \, or blank space.  These characters divide the square into contiguous regions.

(Note that backslash characters are escaped, so a \ is represented as "\\".)

Return the number of regions.



Example 1:

Input:
[
  " /",
  "/ "
]
Output: 2
Explanation: The 2x2 grid is as follows:

Example 2:

Input:
[
  " /",
  "  "
]
Output: 1
Explanation: The 2x2 grid is as follows:

Example 3:

Input:
[
  "\\/",
  "/\\"
]
Output: 4
Explanation: (Recall that because \ characters are escaped, "\\/" refers to \/, and "/\\" refers to /\.)
The 2x2 grid is as follows:

Example 4:

Input:
[
  "/\\",
  "\\/"
]
Output: 5
Explanation: (Recall that because \ characters are escaped, "/\\" refers to /\, and "\\/" refers to \/.)
The 2x2 grid is as follows:

Example 5:

Input:
[
  "//",
  "/ "
]
Output: 3
Explanation: The 2x2 grid is as follows:



Note:

1 <= grid.length == grid[0].length <= 30
grid[i][j] is either '/', '\', or ' '.


959. 由斜杠划分区域
在由 1 x 1 方格组成的 N x N 网格 grid 中，每个 1 x 1 方块由 /、\ 或空格构成。这些字符会将方块划分为一些共边的区域。

（请注意，反斜杠字符是转义的，因此 \ 用 "\\" 表示。）。

返回区域的数目。



示例 1：

输入：
[
  " /",
  "/ "
]
输出：2
解释：2x2 网格如下：

示例 2：

输入：
[
  " /",
  "  "
]
输出：1
解释：2x2 网格如下：

示例 3：

输入：
[
  "\\/",
  "/\\"
]
输出：4
解释：（回想一下，因为 \ 字符是转义的，所以 "\\/" 表示 \/，而 "/\\" 表示 /\。）
2x2 网格如下：

示例 4：

输入：
[
  "/\\",
  "\\/"
]
输出：5
解释：（回想一下，因为 \ 字符是转义的，所以 "/\\" 表示 /\，而 "\\/" 表示 \/。）
2x2 网格如下：

示例 5：

输入：
[
  "//",
  "/ "
]
输出：3
解释：2x2 网格如下：



提示：

1 <= grid.length == grid[0].length <= 30
grid[i][j] 是 '/'、'\'、或 ' '。
'''



class Solution(object):
    def regionsBySlashes(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
        length = len(grid)
        p = {(i, j): (i, j) for j in range(length) for i in range(length)}

        for i in range(length+1):
            p[(i, 0)], p[(0, i)], p[(length, i)], p[(i, length)] = (0, 0), (0, 0), (0, 0), (0, 0)

        def find(x):
            px = p[x]
            if px != x:
                px = find(p[x])
            return px

        def union(x, y):
            px = find(x)
            py = find(y)
            if px != py:
                p[px] = py
                return False
            return True

        res = 1
        for i in range(length):
            for j in range(length):
                if grid[i][j] == "/":
                    if union((i+1, j), (i, j+1)):
                        res += 1
                elif grid[i][j] == "\\":
                    if union((i+1, j+1), (i, j)):
                        res += 1

        return res


# solutions

'''
方法一：并查集
我们沿着一个网格的两条对角线，能够将正方形切分成四个三角形。如果网格上的字符为 /，则右下角的两个三角形会与左上角的两个三角形分隔开；同理，如果字符为 \，则右上角的两个三角形会和左下角的两个三角形分隔开。

不难发现，如果将每个三角形看作为一张图上的节点，则网格中的一个共边区域，就相当于图中的一个连通分量。因此，不难想到利用并查集求解连通分量的数目。

设网格为 n \times nn×n 大小，则图中有 4n^24n 
2
  个节点，每个格子对应其中的 44 个节点。对于每个格子而言，考虑当前位置的字符：

如果为空格，则该格子对应的 44 个节点应当同属于同一区域，因此在它们之间各连接一条边；

如果为字符 /，则将左上角的两个格子连接一条边，并将右下角的两个格子连接一条边；

如果为字符 \，则将右上角的两个格子连接一条边，并将左下角的两个格子连接一条边。

到目前位置，我们只考虑了一个格子内部的情况。但同时，不难观察到下面两点：

一个格子中最下方的三角形，必然和下面的格子（如果存在）中最上方的三角形连通；

一个格子中最右方的三角形，必然和右边的格子（如果存在）中最左方的三角形连通。

因此，我们还需要根据上面两条规则，在相邻格子的相应三角形中间，再连接边。

最终，在构造出图后，利用并查集就可以求出连通分量的数目了。

具体实现方面，每个格子的 44 个节点按照上、右、下、左的顺序依次编号 00、11、22、33，每个节点可以根据格子所在的行和列以及节点在格子中的编号唯一地确定。

C++JavaJavaScriptGolangC

type unionFind struct {
    parent, size []int
    setCount     int // 当前连通分量数目
}

func newUnionFind(n int) *unionFind {
    parent := make([]int, n)
    size := make([]int, n)
    for i := range parent {
        parent[i] = i
        size[i] = 1
    }
    return &unionFind{parent, size, n}
}

func (uf *unionFind) find(x int) int {
    if uf.parent[x] != x {
        uf.parent[x] = uf.find(uf.parent[x])
    }
    return uf.parent[x]
}

func (uf *unionFind) union(x, y int) {
    fx, fy := uf.find(x), uf.find(y)
    if fx == fy {
        return
    }
    if uf.size[fx] < uf.size[fy] {
        fx, fy = fy, fx
    }
    uf.size[fx] += uf.size[fy]
    uf.parent[fy] = fx
    uf.setCount--
}

func regionsBySlashes(grid []string) int {
    n := len(grid)
    uf := newUnionFind(4 * n * n)
    for i := 0; i < n; i++ {
        for j := 0; j < n; j++ {
            idx := i*n + j
            if i < n-1 {
                bottom := idx + n
                uf.union(idx*4+2, bottom*4)
            }
            if j < n-1 {
                right := idx + 1
                uf.union(idx*4+1, right*4+3)
            }
            if grid[i][j] == '/' {
                uf.union(idx*4, idx*4+3)
                uf.union(idx*4+1, idx*4+2)
            } else if grid[i][j] == '\\' {
                uf.union(idx*4, idx*4+1)
                uf.union(idx*4+2, idx*4+3)
            } else {
                uf.union(idx*4, idx*4+1)
                uf.union(idx*4+1, idx*4+2)
                uf.union(idx*4+2, idx*4+3)
            }
        }
    }
    return uf.setCount
}
复杂度分析

时间复杂度：O(n^2\log n)O(n 
2
 logn)，其中 nn 是网格的边长。仅使用路径压缩的并查集的复杂度为 O(n^2\log n^2)=O(n^2\times 2\log n)=O(n^2\log n)O(n 
2
 logn 
2
 )=O(n 
2
 ×2logn)=O(n 
2
 logn)。

空间复杂度：O(n^2)O(n 
2
 )。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/regions-cut-by-slashes/solution/you-xie-gang-hua-fen-qu-yu-by-leetcode-s-ztob/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''

