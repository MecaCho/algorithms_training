# encoding=UTF8


'''
778. Swim in Rising Water
On an N x N grid, each square grid[i][j] represents the elevation at that point (i,j).

Now rain starts to fall. At time t, the depth of the water everywhere is t. You can swim from a square to another 4-directionally adjacent square if and only if the elevation of both squares individually are at most t. You can swim infinite distance in zero time. Of course, you must stay within the boundaries of the grid during your swim.

You start at the top left square (0, 0). What is the least time until you can reach the bottom right square (N-1, N-1)?

Example 1:

Input: [[0,2],[1,3]]
Output: 3
Explanation:
At time 0, you are in grid location (0, 0).
You cannot go anywhere else because 4-directionally adjacent neighbors have a higher elevation than t = 0.

You cannot reach point (1, 1) until time 3.
When the depth of water is 3, we can swim anywhere inside the grid.
Example 2:

Input: [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
Output: 16
Explanation:
 0  1  2  3  4
24 23 22 21  5
12 13 14 15 16
11 17 18 19 20
10  9  8  7  6

The final route is marked in bold.
We need to wait until time 16 so that (0, 0) and (4, 4) are connected.
Note:

2 <= N <= 50.
grid[i][j] is a permutation of [0, ..., N*N - 1].



778. 水位上升的泳池中游泳
在一个 N x N 的坐标方格 grid 中，每一个方格的值 grid[i][j] 表示在位置 (i,j) 的平台高度。

现在开始下雨了。当时间为 t 时，此时雨水导致水池中任意位置的水位为 t 。你可以从一个平台游向四周相邻的任意一个平台，但是前提是此时水位必须同时淹没这两个平台。假定你可以瞬间移动无限距离，也就是默认在方格内部游动是不耗时的。当然，在你游泳的时候你必须待在坐标方格里面。

你从坐标方格的左上平台 (0，0) 出发。最少耗时多久你才能到达坐标方格的右下平台 (N-1, N-1)？



示例 1:

输入: [[0,2],[1,3]]
输出: 3
解释:
时间为0时，你位于坐标方格的位置为 (0, 0)。
此时你不能游向任意方向，因为四个相邻方向平台的高度都大于当前时间为 0 时的水位。

等时间到达 3 时，你才可以游向平台 (1, 1). 因为此时的水位是 3，坐标方格中的平台没有比水位 3 更高的，所以你可以游向坐标方格中的任意位置
示例2:

输入: [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
输出: 16
解释:
 0  1  2  3  4
24 23 22 21  5
12 13 14 15 16
11 17 18 19 20
10  9  8  7  6

最终的路线用加粗进行了标记。
我们必须等到时间为 16，此时才能保证平台 (0, 0) 和 (4, 4) 是连通的


提示:

2 <= N <= 50.
grid[i][j] 是 [0, ..., N*N - 1] 的排列。
'''


# solution

'''
class Dsu:
    def __init__(self,n):
        self.f=[i for i in range(n)]
        self.rank=[1]*n
    def find(self,x):
        if self.f[x]==x:
            return x
        else:
            self.f[x]=self.find(self.f[x])
            return self.f[x]
    def union(self,x,y):
        x,y=self.find(x),self.find(y)
        if self.rank[x]<=self.rank[y]:
            self.f[x]=y
        else:
            self.f[y]=x
        if self.rank[x]==self.rank[y] and x!=y:
            self.rank[y]+=1

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        edges=[]
        row,col=len(grid),len(grid[0])
        dsu=Dsu(row*col)
        for i in range(row):
            for j in range(col):
                if i<row-1:
                    edges.append([i*col+j,(i+1)*col+j,max(grid[i][j],grid[i+1][j])])
           
                if j<col-1:
                    edges.append([i*col+j,i*col+j+1,max(grid[i][j],grid[i][j+1])])
                    
        edges.sort(key=lambda x:x[-1])
        res=0
        for edge in edges:
            if dsu.find(edge[0])!=dsu.find(edge[1]):
                dsu.union(edge[0],edge[1])
                res=max(res,edge[-1])
            if dsu.find(0)==dsu.find(col*row-1):
                break
        return res

'''


# solutions

'''
文字解析
注意题目中的重要信息：假定你可以 瞬间移动 无限距离，游动不耗时。当前这个问题就转换成为：找一个时刻 t，使得这个二维网格上数值 小于等于 t 的部分，存在一条从左上角到右下角的路径。即：经过了时间 t 以后，可以瞬间从左上角（坐标 [0, 0]）游到右下角（坐标 [N - 1, N - 1]）。

方法一：二分查找 + 遍历
根据题目中的描述：

如果等待的时间 t 越少，网格上可以游泳的部分就越少，存在从左上角到右下角的一条路径的可能性越小；
如果等待的时间 t 越多，网格上可以游泳的部分就越多，存在从左上角到右下角的一条路径的可能性越大。


这是本问题具有的 单调性。因此可以使用二分查找定位到最短等待时间。具体来说：在区间 [0, N * N - 1] 里猜一个整数，针对这个整数从起点（左上角）开始做一次深度优先遍历或者广度优先遍历。

当小于等于该数值时，如果存在一条从左上角到右下角的路径，说明答案可能是这个数值，也可能更小；
当小于等于该数值时，如果不存在一条从左上角到右下角的路径，说明答案一定比这个数值更大。
按照这种方式不断缩小搜索的区间，最终找到最少等待时间。

参考代码 1：

说明：选项卡一使用深度优先遍历，选项卡二使用广度优先遍历。

JavaJava

public class Solution {

    private int N;

    public static final int[][] DIRECTIONS = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

    public int swimInWater(int[][] grid) {
        this.N = grid.length;

        int left = 0;
        int right = N * N - 1;
        while (left < right) {
            // left + right 不会溢出
            int mid = (left + right) / 2;
            boolean[][] visited = new boolean[N][N];
            if (grid[0][0] <= mid && dfs(grid, 0, 0, visited, mid)) {
                // mid 可以，尝试 mid 小一点是不是也可以呢？下一轮搜索的区间 [left, mid]
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        return left;
    }

    /**
     * 使用深度优先遍历得到从 (x, y) 开始向四个方向的所有小于等于 threshold 且与 (x, y) 连通的结点
     *
     * @param grid
     * @param x
     * @param y
     * @param visited
     * @param threshold
     * @return
     */
    private boolean dfs(int[][] grid, int x, int y, boolean[][] visited, int threshold) {
        visited[x][y] = true;
        for (int[] direction : DIRECTIONS) {
            int newX = x + direction[0];
            int newY = y + direction[1];
            if (inArea(newX, newY) && !visited[newX][newY] && grid[newX][newY] <= threshold) {
                if (newX == N - 1 && newY == N - 1) {
                    return true;
                }

                if (dfs(grid, newX, newY, visited, threshold)) {
                    return true;
                }
            }
        }
        return false;
    }

    private boolean inArea(int x, int y) {
        return x >= 0 && x < N && y >= 0 && y < N;
    }
}
复杂度分析：

时间复杂度：O(N^2 \log N)O(N 
2
 logN)。
其中 NN 是方格的边长。最差情况下进行 \log N^2logN 
2
  次二分查找，每一次二分查找最差情况下要遍历所有单元格一次，时间复杂度为 O(N^2)O(N 
2
 )。总的时间复杂度为 O(N^2 \log N^2) = O(2N^2 \log N) = O(N^2 \log N)O(N 
2
 logN 
2
 )=O(2N 
2
 logN)=O(N 
2
 logN)；
空间复杂度：O(N^2)O(N 
2
 )。
数组 visited 的大小为 N^2N 
2
  ，如果使用深度优先遍历，须要使用的栈的大小最多为 N^2N 
2
  ，如果使用广度优先遍历，须要使用的栈的大小最多为 N^2N 
2
 。
关于连通性的问题，如果只问结果，不问具体怎么连起来的，还可以考虑使用并查集。

方法二：并查集
由于题目要我们找的是最少等待时间，可以模拟下雨的过程，把网格抽象成一个无权图，每经过一个时刻，就考虑此时和雨水高度相等的单元格，考虑这个单元格的上、下、左、右、四个方向，并且高度更低的单元格，把它们在并查集中进行合并。



参考代码 2：

Java

public class Solution {

    private int N;

    public static final int[][] DIRECTIONS = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

    public int swimInWater(int[][] grid) {
        this.N = grid.length;

        int len = N * N;
        // 下标：方格的高度，值：对应在方格中的坐标
        int[] index = new int[len];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                index[grid[i][j]] = getIndex(i, j);
            }
        }

        UnionFind unionFind = new UnionFind(len);
        for (int i = 0; i < len; i++) {
            int x = index[i] / N;
            int y = index[i] % N;

            for (int[] direction : DIRECTIONS) {
                int newX = x + direction[0];
                int newY = y + direction[1];
                if (inArea(newX, newY) && grid[newX][newY] <= i) {
                    unionFind.union(index[i], getIndex(newX, newY));
                }

                if (unionFind.isConnected(0, len - 1)) {
                    return i;
                }
            }
        }
        return -1;
    }

    private int getIndex(int x, int y) {
        return x * N + y;
    }

    private boolean inArea(int x, int y) {
        return x >= 0 && x < N && y >= 0 && y < N;
    }

    private class UnionFind {

        private int[] parent;

        public UnionFind(int n) {
            this.parent = new int[n];
            for (int i = 0; i < n; i++) {
                parent[i] = i;
            }
        }

        public int root(int x) {
            while (x != parent[x]) {
                parent[x] = parent[parent[x]];
                x = parent[x];
            }
            return x;
        }

        public boolean isConnected(int x, int y) {
            return root(x) == root(y);
        }

        public void union(int p, int q) {
            if (isConnected(p, q)) {
                return;
            }
            parent[root(p)] = root(q);
        }
    }
}
复杂度分析

时间复杂度：O(N^2 \log N)O(N 
2
 logN)，其中 NN 是方格的边长，计数排序 O(N^2)O(N 
2
 )，合并四周、检查起点和终点是否同属于一个连通分量 O(\log N^2)O(logN 
2
 )，总的时间复杂度为 O(N^2 + N^2\log N^2) = O(N^2 + 2N^2 \log N) = O(N^2 \log N)O(N 
2
 +N 
2
 logN 
2
 )=O(N 
2
 +2N 
2
 logN)=O(N 
2
 logN)；
空间复杂度：O(N^2)O(N 
2
 )，数组 index 的长度，并查集底层的长度均为 N^2N 
2
 。
方法三：Dijkstra 算法
注意这个问题求的是从一个源点到目标顶点的最短路径，并且这条路径上的边没有负数（这一点非常重要，单元格的高度大于等于 00），符合 Dijkstra 算法的应用场景。为此我们可以把问题抽象成一个带权有向图，权值是有向边指向的顶点的高度。如下图所示：



Dijkstra 算法是应用很广泛的求解 没有负权边 的单源最短路径算法，《算法（第 4 版）》对这个算法做了详细的介绍，大家还可以阅读这本书的配套英文教程的 4.4 Shortest Paths 进行学习。没有负权边是应用 Dijkstra 算法的前提，也是理解 Dijkstra 算法执行流程的关键。

Dijkstra 算法应用在示例 2 寻找最短路径的过程如下图所示：



参考代码 3：

Java

import java.util.Arrays;
import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.Queue;

public class Solution {

    // Dijkstra 算法（应用前提：没有负权边，找单源最短路径）

    public int swimInWater(int[][] grid) {
        int n = grid.length;

        Queue<int[]> minHeap = new PriorityQueue<>(Comparator.comparingInt(o -> grid[o[0]][o[1]]));
        minHeap.offer(new int[]{0, 0});

        boolean[][] visited = new boolean[n][n];
        // distTo[i][j] 表示：到顶点 [i, j] 须要等待的最少的时间
        int[][] distTo = new int[n][n];
        for (int[] row : distTo) {
            Arrays.fill(row, n * n);
        }
        distTo[0][0] = grid[0][0];

        int[][] directions = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        while (!minHeap.isEmpty()) {
            // 找最短的边
            int[] front = minHeap.poll();
            int currentX = front[0];
            int currentY = front[1];
            if (visited[currentX][currentY]) {
                continue;
            }

            // 确定最短路径顶点
            visited[currentX][currentY] = true;
            if (currentX == n - 1 && currentY == n - 1) {
                return distTo[n - 1][n - 1];
            }

            // 更新
            for (int[] direction : directions) {
                int newX = currentX + direction[0];
                int newY = currentY + direction[1];
                if (inArea(newX, newY, n) && !visited[newX][newY] &&
                        Math.max(distTo[currentX][currentY], grid[newX][newY]) < distTo[newX][newY]) {
                    distTo[newX][newY] = Math.max(distTo[currentX][currentY], grid[newX][newY]);
                    minHeap.offer(new int[]{newX, newY});
                }
            }
        }
        return -1;
    }

    private boolean inArea(int x, int y, int n) {
        return x >= 0 && x < n && y >= 0 && y < n;
    }
}
复杂度分析：

时间复杂度：O(N^2 \log N)O(N 
2
 logN)。
使用了优先队列的 Dijkstra 算法的时间复杂度是 O(E \log E)O(ElogE) ，这里 EE 是边数，至多是顶点数的 44 倍，顶点数为 N^2N 
2
 ，因此 O(E \log E) = O(4N^2 \log N^2) = O(N^2 \log N)O(ElogE)=O(4N 
2
 logN 
2
 )=O(N 
2
 logN)；
空间复杂度：O(N^2)O(N 
2
 )。
数组 visited 、distTo 的大小为 O(N^2)O(N 
2
 )，优先队列中保存的边的总数也是 N^2N 
2
  级别的。

作者：LeetCode
链接：https://leetcode-cn.com/problems/swim-in-rising-water/solution/shui-wei-shang-sheng-de-yong-chi-zhong-y-862o/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''

# solutions golang

'''
方法一：堆（优先队列）
根据题意，假设在时间 tt 时能够到达方格 (i,j)(i,j)，那么对于一个与之相邻的方格 (i',j')(i 
′
 ,j 
′
 )：

如果 \textit{grid}[i'][j'] \le \textit{grid}[i][j]grid[i 
′
 ][j 
′
 ]≤grid[i][j]，说明 (i',j')(i 
′
 ,j 
′
 ) 处的高度更低，故在时间 tt 也能够到达 (i',j')(i 
′
 ,j 
′
 )；
否则，若 \textit{grid}[i'][j'] > \textit{grid}[i][j]grid[i 
′
 ][j 
′
 ]>grid[i][j]，则需要至少等到 \textit{grid}[i'][j']grid[i 
′
 ][j 
′
 ] 时刻才能够到达 (i',j')(i 
′
 ,j 
′
 )。
因此，我们从原点出发，每一步试图多访问一个方格，并记录访问到该方格的最短时间。当进行下一步时，考虑从已访问方格能到达的所有方格，并选择其中高度最低的那个方格进行下一次访问。这一迭代的步骤类似于利用 \text{Dijkstra}Dijkstra 算法求解最短路径的过程。

为了维护从已访问方格能到达的所有方格，并能从中取出最小值，我们使用堆（优先队列）来维护这些信息。

C++JavaGolang

type entry struct{ i, j, val int }
type hp []entry

func (h hp) Len() int            { return len(h) }
func (h hp) Less(i, j int) bool  { return h[i].val < h[j].val }
func (h hp) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *hp) Push(v interface{}) { *h = append(*h, v.(entry)) }
func (h *hp) Pop() interface{}   { a := *h; v := a[len(a)-1]; *h = a[:len(a)-1]; return v }

type pair struct{ x, y int }
var dirs = []pair{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}

func swimInWater(grid [][]int) (ans int) {
    n := len(grid)
    vis := make([][]bool, n)
    for i := range vis {
        vis[i] = make([]bool, n)
    }
    vis[0][0] = true
    h := &hp{{0, 0, grid[0][0]}}
    for {
        e := heap.Pop(h).(entry)
        ans = max(ans, e.val)
        if e.i == n-1 && e.j == n-1 {
            return
        }
        for _, d := range dirs {
            if x, y := e.i+d.x, e.j+d.y; 0 <= x && x < n && 0 <= y && y < n && !vis[x][y] {
                vis[x][y] = true
                heap.Push(h, entry{x, y, grid[x][y]})
            }
        }
    }
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}
复杂度分析

时间复杂度：O(n^2\log n)O(n 
2
 logn)，其中 nn 为网格的边长。每个方格至多会被加入优先队列 44 次，故循环执行次数为 O(4n^2)=O(n^2)O(4n 
2
 )=O(n 
2
 )，同时每次循环要从至多 O(n^2)O(n 
2
 ) 的位置中取最小值，故单次循环的代价为 O(\log n^2)=O(2\log n)=O(\log n)O(logn 
2
 )=O(2logn)=O(logn)。

空间复杂度：O(n^2)O(n 
2
 )。

方法二：二分查找
考虑这样一个问题：给定一个整数 \textit{threshold}threshold，是否存在一个路径，使得能在 \textit{threshold}threshold 时间内从起点到达终点？

这一问题的解法是很直观的：我们执行广度优先搜索，并只去访问那些高度不超过 \textit{threshold}threshold 的方格。最终，如果能访问到终点，说明存在这样一种路径。

如果能在 \textit{threshold}threshold 时间内从起点到达终点，则一定也能在 \textit{threshold}+1threshold+1 的时间内从起点到达终点。因此，我们可以通过二分查找的方式，寻找最小可能的 \textit{threshold}threshold。

C++JavaGolangCJavaScript

type pair struct{ x, y int }
var dirs = []pair{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}

func swimInWater(grid [][]int) (ans int) {
    n := len(grid)
    return sort.Search(n*n-1, func(threshold int) bool {
        if threshold < grid[0][0] {
            return false
        }
        vis := make([][]bool, n)
        for i := range vis {
            vis[i] = make([]bool, n)
        }
        vis[0][0] = true
        queue := []pair{{}}
        for len(queue) > 0 {
            p := queue[0]
            queue = queue[1:]
            for _, d := range dirs {
                if x, y := p.x+d.x, p.y+d.y; 0 <= x && x < n && 0 <= y && y < n && !vis[x][y] && grid[x][y] <= threshold {
                    vis[x][y] = true
                    queue = append(queue, pair{x, y})
                }
            }
        }
        return vis[n-1][n-1]
    })
}
复杂度分析

时间复杂度：O(n^2\log n)O(n 
2
 logn)。对于任何一个给定的 \textit{threshold}threshold 而言，需要 O(n^2)O(n 
2
 ) 的时间内执行广度优先搜索。同时，二分查找的上下边界分别为 n^2-1n 
2
 −1 和 00，故二分查找的次数为 O(\log n^2)=O(2\log n)=O(\log n)O(logn 
2
 )=O(2logn)=O(logn)。

空间复杂度：O(n^2)O(n 
2
 )。

方法三：并查集
依然考虑同样的问题：给定一个整数 \textit{threshold}threshold，是否存在一个路径，使得能在 \textit{threshold}threshold 时间内从起点到达终点？

我们将每个方格看做图中的顶点。由于任意时刻都不能到达高度高于 \textit{threshold}threshold 的方格，因此对于两个相邻的方格而言，当且仅当它们的高度都不超过 \textit{threshold}threshold 时，才在这两个顶点之间连接一条边。因此，能否从起点到达终点，就等价于对应的顶点在图中是否连通。

为了判断是否连通，可以使用并查集来维护节点之间的连通关系。

我们当然也能通过二分查找的方式来找到最小可能的 \textit{threshold}threshold。但是如果使用二分查找，每次判断 \textit{threshold}threshold 是否符合条件时，都要耗费大量的时间重新构建并查集，导致复杂度还不如前一种做法。

如果我们是从小到大依次考虑 \textit{threshold}threshold，那么每次考虑一个新值时，只需要在上一个阶段的图中，添加几条新边而已，而无需重新构建整张图。

具体而言，我们维护每个高度值对应的方块位置，当考虑 \textit{threshold}threshold 时，我们首先找出对应的方块位置，然后对于每个与之相邻的方块，如果相邻的方块的高度值不超过 \textit{threshold}threshold，就在两个方块之间连接一条边。当所有相邻方块都被考虑完毕时，再判断起点和终点是否连通。

C++JavaGolangCJavaScript

type unionFind struct {
    parent, size []int
}

func newUnionFind(n int) *unionFind {
    parent := make([]int, n)
    size := make([]int, n)
    for i := range parent {
        parent[i] = i
        size[i] = 1
    }
    return &unionFind{parent, size}
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
}

func (uf *unionFind) inSameSet(x, y int) bool {
    return uf.find(x) == uf.find(y)
}

type pair struct{ x, y int }
var dirs = []pair{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}

func swimInWater(grid [][]int) (ans int) {
    n := len(grid)
    pos := make([]pair, n*n)
    for i, row := range grid {
        for j, h := range row {
            pos[h] = pair{i, j} // 存储每个平台高度对应的位置
        }
    }

    uf := newUnionFind(n * n)
    for threshold := 0; ; threshold++ {
        p := pos[threshold]
        for _, d := range dirs {
            if x, y := p.x+d.x, p.y+d.y; 0 <= x && x < n && 0 <= y && y < n && grid[x][y] <= threshold {
                uf.union(x*n+y, p.x*n+p.y)
            }
        }
        if uf.inSameSet(0, n*n-1) {
            return threshold
        }
    }
}
复杂度分析

时间复杂度：O(n^2\log n)O(n 
2
 logn)。外层循环至多执行 O(n^2)O(n 
2
 ) 次，每次循环至多添加 44 条边，而添加每条边的代价为 O(\log n^2)=O(2\log n)=O(\log n)O(logn 
2
 )=O(2logn)=O(logn)，判断起点和终点是否连通的代价为 O(\log n^2)=O(2\log n)=O(\log n)O(logn 
2
 )=O(2logn)=O(logn)。

空间复杂度：O(n^2)O(n 
2
 )。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/swim-in-rising-water/solution/shui-wei-shang-sheng-de-yong-chi-zhong-y-xm9i/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
