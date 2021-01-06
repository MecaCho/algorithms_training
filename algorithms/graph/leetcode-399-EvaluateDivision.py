# encoding=utf8

'''
399. Evaluate Division
You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.

You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.

Return the answers to all queries. If a single answer cannot be determined, return -1.0.

Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.



Example 1:

Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
Explanation:
Given: a / b = 2.0, b / c = 3.0
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
Example 2:

Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
Output: [3.75000,0.40000,5.00000,0.20000]
Example 3:

Input: equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
Output: [0.50000,2.00000,-1.00000,-1.00000]


Constraints:

1 <= equations.length <= 20
equations[i].length == 2
1 <= Ai.length, Bi.length <= 5
values.length == equations.length
0.0 < values[i] <= 20.0
1 <= queries.length <= 20
queries[i].length == 2
1 <= Cj.length, Dj.length <= 5
Ai, Bi, Cj, Dj consist of lower case English letters and digits.


399. 除法求值
给你一个变量对数组 equations 和一个实数值数组 values 作为已知条件，其中 equations[i] = [Ai, Bi] 和 values[i] 共同表示等式 Ai / Bi = values[i] 。每个 Ai 或 Bi 是一个表示单个变量的字符串。

另有一些以数组 queries 表示的问题，其中 queries[j] = [Cj, Dj] 表示第 j 个问题，请你根据已知条件找出 Cj / Dj = ? 的结果作为答案。

返回 所有问题的答案 。如果存在某个无法确定的答案，则用 -1.0 替代这个答案。



注意：输入总是有效的。你可以假设除法运算中不会出现除数为 0 的情况，且不存在任何矛盾的结果。



示例 1：

输入：equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
输出：[6.00000,0.50000,-1.00000,1.00000,-1.00000]
解释：
条件：a / b = 2.0, b / c = 3.0
问题：a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
结果：[6.0, 0.5, -1.0, 1.0, -1.0 ]
示例 2：

输入：equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
输出：[3.75000,0.40000,5.00000,0.20000]
示例 3：

输入：equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
输出：[0.50000,2.00000,-1.00000,-1.00000]


提示：

1 <= equations.length <= 20
equations[i].length == 2
1 <= Ai.length, Bi.length <= 5
values.length == equations.length
0.0 < values[i] <= 20.0
1 <= queries.length <= 20
queries[i].length == 2
1 <= Cj.length, Dj.length <= 5
Ai, Bi, Cj, Dj 由小写英文字母与数字组成
'''


# golang solution

'''
func calcEquation(equations [][]string, values []float64, queries [][]string) []float64 {
    id := map[string]int{}
    for _, eq := range equations {
        a, b := eq[0], eq[1]
        if _, has := id[a]; !has {
            id[a] = len(id)
        }
        if _, has := id[b]; !has {
            id[b] = len(id)
        }
    }

    // 建图
    graph := make([][]float64, len(id))
    for i := range graph {
        graph[i] = make([]float64, len(id))
    }
    for i, eq := range equations {
        v, w := id[eq[0]], id[eq[1]]
        graph[v][w] = values[i]
        graph[w][v] = 1 / values[i]
    }

    // 执行 Floyd 算法
    for k := range graph {
        for i := range graph {
            for j := range graph {
                if graph[i][k] > 0 && graph[k][j] > 0 {
                    graph[i][j] = graph[i][k] * graph[k][j]
                }
            }
        }
    }

    ans := make([]float64, len(queries))
    for i, q := range queries {
        start, hasS := id[q[0]]
        end, hasE := id[q[1]]
        if !hasS || !hasE || graph[start][end] == 0 {
            ans[i] = -1
        } else {
            ans[i] = graph[start][end]
        }
    }
    return ans

}
'''


# solutions

'''
方法一：广度优先搜索
我们可以将整个问题建模成一张图：给定图中的一些点（变量），以及某些边的权值（两个变量的比值），试对任意两点（两个变量）求出其路径长（两个变量的比值）。

因此，我们首先需要遍历 \textit{equations}equations 数组，找出其中所有不同的字符串，并通过哈希表将每个不同的字符串映射成整数。

在构建完图之后，对于任何一个查询，就可以从起点出发，通过广度优先搜索的方式，不断更新起点与当前点之间的路径长度，直到搜索到终点为止。

C++JavaGolang

func calcEquation(equations [][]string, values []float64, queries [][]string) []float64 {
    // 给方程组中的每个变量编号
    id := map[string]int{}
    for _, eq := range equations {
        a, b := eq[0], eq[1]
        if _, has := id[a]; !has {
            id[a] = len(id)
        }
        if _, has := id[b]; !has {
            id[b] = len(id)
        }
    }

    // 建图
    type edge struct {
        to     int
        weight float64
    }
    graph := make([][]edge, len(id))
    for i, eq := range equations {
        v, w := id[eq[0]], id[eq[1]]
        graph[v] = append(graph[v], edge{w, values[i]})
        graph[w] = append(graph[w], edge{v, 1 / values[i]})
    }

    bfs := func(start, end int) float64 {
        ratios := make([]float64, len(graph))
        ratios[start] = 1
        queue := []int{start}
        for len(queue) > 0 {
            v := queue[0]
            queue = queue[1:]
            if v == end {
                return ratios[v]
            }
            for _, e := range graph[v] {
                if w := e.to; ratios[w] == 0 {
                    ratios[w] = ratios[v] * e.weight
                    queue = append(queue, w)
                }
            }
        }
        return -1
    }

    ans := make([]float64, len(queries))
    for i, q := range queries {
        start, hasS := id[q[0]]
        end, hasE := id[q[1]]
        if !hasS || !hasE {
            ans[i] = -1
        } else {
            ans[i] = bfs(start, end)
        }
    }
    return ans
}
复杂度分析

时间复杂度：O(ML+Q\cdot(L+M))O(ML+Q⋅(L+M))，其中 MM 为边的数量，QQ 为询问的数量，LL 为字符串的平均长度。构建图时，需要处理 MM 条边，每条边都涉及到 O(L)O(L) 的字符串比较；处理查询时，每次查询首先要进行一次 O(L)O(L) 的比较，然后至多遍历 O(M)O(M) 条边。

空间复杂度：O(NL+M)O(NL+M)，其中 NN 为点的数量，MM 为边的数量，LL 为字符串的平均长度。为了将每个字符串映射到整数，需要开辟空间为 O(NL)O(NL) 的哈希表；随后，需要花费 O(M)O(M) 的空间存储每条边的权重；处理查询时，还需要 O(N)O(N) 的空间维护访问队列。最终，总的复杂度为 O(NL+M+N) = O(NL+M)O(NL+M+N)=O(NL+M)。

方法二：\text{Floyd}Floyd 算法
对于查询数量很多的情形，如果为每次查询都独立搜索一次，则效率会变低。为此，我们不妨对图先做一定的预处理，随后就可以在较短的时间内回答每个查询。

在本题中，我们可以使用 \text{Floyd}Floyd 算法，预先计算出任意两点之间的距离。

C++JavaGolang

func calcEquation(equations [][]string, values []float64, queries [][]string) []float64 {
    // 给方程组中的每个变量编号
    id := map[string]int{}
    for _, eq := range equations {
        a, b := eq[0], eq[1]
        if _, has := id[a]; !has {
            id[a] = len(id)
        }
        if _, has := id[b]; !has {
            id[b] = len(id)
        }
    }

    // 建图
    graph := make([][]float64, len(id))
    for i := range graph {
        graph[i] = make([]float64, len(id))
    }
    for i, eq := range equations {
        v, w := id[eq[0]], id[eq[1]]
        graph[v][w] = values[i]
        graph[w][v] = 1 / values[i]
    }

    // 执行 Floyd 算法
    for k := range graph {
        for i := range graph {
            for j := range graph {
                if graph[i][k] > 0 && graph[k][j] > 0 {
                    graph[i][j] = graph[i][k] * graph[k][j]
                }
            }
        }
    }

    ans := make([]float64, len(queries))
    for i, q := range queries {
        start, hasS := id[q[0]]
        end, hasE := id[q[1]]
        if !hasS || !hasE || graph[start][end] == 0 {
            ans[i] = -1
        } else {
            ans[i] = graph[start][end]
        }
    }
    return ans
}
复杂度分析

时间复杂度：O(ML+N^3+QL)O(ML+N 
3
 +QL)。构建图需要 O(ML)O(ML) 的时间；\text{Floyd}Floyd 算法需要 O(N^3)O(N 
3
 ) 的时间；处理查询时，单次查询只需要 O(L)O(L) 的字符串比较以及常数时间的额外操作。

空间复杂度：O(NL+N^2)O(NL+N 
2
 )。

方法三：带权并查集
我们还可以考虑以并查集的方式存储节点之间的关系。设节点 xx 的值（即对应变量的取值）为 v[x]v[x]。对于任意两点 x, yx,y，假设它们在并查集中具有共同的父亲 ff，且 v[x]/v[f] = a, v[y]/v[f]=bv[x]/v[f]=a,v[y]/v[f]=b，则 v[x]/v[y]=a/bv[x]/v[y]=a/b。

在观察到这一点后，就不难利用并查集的思想解决此题。对于每个节点 xx 而言，除了维护其父亲 f[x]f[x] 之外，还要维护其权值 ww，其中「权值」定义为节点 xx 的取值与父亲 f[x]f[x] 的取值之间的比值。换言之，我们有

w[x] = \frac{v[x]}{v[f[x]]}
w[x]= 
v[f[x]]
v[x]
​	
 

下面，我们对并查集的两种操作的实现细节做出讨论。

当查询节点 xx 父亲时，如果 f[x] \ne xf[x] 

​	
 =x，我们需要先找到 f[x]f[x] 的父亲 \textit{father}father，并将 f[x]f[x] 更新为 \textit{father}father。此时，我们有

\begin{aligned} w[x] &\leftarrow \frac{v[x]}{v[\textit{father}]} \\ &= \frac{v[x]}{v[f[x]]} \cdot \frac{v[f[x]]}{v[\textit{father}]} \\ &= w[i] \cdot w[f[x]] \end{aligned}
w[x]
​	
  
← 
v[father]
v[x]
​	
 
= 
v[f[x]]
v[x]
​	
 ⋅ 
v[father]
v[f[x]]
​	
 
=w[i]⋅w[f[x]]
​	
 

也就是说，我们要将 w[x]w[x] 更新为 w[x] \cdot w[f[x]]w[x]⋅w[f[x]]。

当合并两个节点 x,yx,y 时，我们首先找到两者的父亲 f_x, f_yf 
x
​	
 ,f 
y
​	
 ，并将 f[f_x]f[f 
x
​	
 ] 更新为 f_yf 
y
​	
 。此时，我们有

\begin{aligned} w[f_x] &\leftarrow \frac{v[f_x]}{v[f_y]} \\ &= \frac{v[x]/w[x]}{v[y]/w[y]} \\ &= \frac{v[x]}{v[y]} \cdot \frac{w[y]}{w[x]} \end{aligned}
w[f 
x
​	
 ]
​	
  
← 
v[f 
y
​	
 ]
v[f 
x
​	
 ]
​	
 
= 
v[y]/w[y]
v[x]/w[x]
​	
 
= 
v[y]
v[x]
​	
 ⋅ 
w[x]
w[y]
​	
 
​	
 

也就是说，当在已有的图中添加一条方程式 \frac{v[x]}{v[y]}=k 
v[y]
v[x]
​	
 =k 时，需要将 w[f_x]w[f 
x
​	
 ] 更新为 k\cdot \frac{w[y]}{w[x]}k⋅ 
w[x]
w[y]
​	
 。

C++JavaGolang

func calcEquation(equations [][]string, values []float64, queries [][]string) []float64 {
    // 给方程组中的每个变量编号
    id := map[string]int{}
    for _, eq := range equations {
        a, b := eq[0], eq[1]
        if _, has := id[a]; !has {
            id[a] = len(id)
        }
        if _, has := id[b]; !has {
            id[b] = len(id)
        }
    }

    fa := make([]int, len(id))
    w := make([]float64, len(id))
    for i := range fa {
        fa[i] = i
        w[i] = 1
    }
    var find func(int) int
    find = func(x int) int {
        if fa[x] != x {
            f := find(fa[x])
            w[x] *= w[fa[x]]
            fa[x] = f
        }
        return fa[x]
    }
    merge := func(from, to int, val float64) {
        fFrom, fTo := find(from), find(to)
        w[fFrom] = val * w[to] / w[from]
        fa[fFrom] = fTo
    }

    for i, eq := range equations {
        merge(id[eq[0]], id[eq[1]], values[i])
    }

    ans := make([]float64, len(queries))
    for i, q := range queries {
        start, hasS := id[q[0]]
        end, hasE := id[q[1]]
        if hasS && hasE && find(start) == find(end) {
            ans[i] = w[start] / w[end]
        } else {
            ans[i] = -1
        }
    }
    return ans
}
复杂度分析

时间复杂度：O(ML+N+M\log N+Q\cdot(L+\log N))O(ML+N+MlogN+Q⋅(L+logN))。构建图需要 O(ML)O(ML) 的时间；初始化并查集需要 O(N)O(N) 的初始化时间；构建并查集的单次操作复杂度为 O(\log N)O(logN)，共需 O(M\log N)O(MlogN) 的时间；每个查询需要 O(L)O(L) 的字符串比较以及 O(\log N)O(logN) 的查询。

空间复杂度：O(NL)O(NL)。哈希表需要 O(NL)O(NL) 的空间，并查集需要 O(N)O(N) 的空间。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/evaluate-division/solution/chu-fa-qiu-zhi-by-leetcode-solution-8nxb/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
