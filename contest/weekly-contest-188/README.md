

# num 1 solutions

## T1

```
class Solution {
public:
    vector<string> buildArray(vector<int>& a, int n) {
        int m = a.size();
        int cur = 0;
        vector<string> ret;
        vector<int> tmp;
        set<int> H(a.begin(), a.end());
        for (int i = 1; i <= n; ++ i)
        {
            ret.push_back("Push");
            tmp.push_back(i);
            if (!H.count(i))
            {
                ret.push_back("Pop");
                tmp.pop_back();
            }
            if (tmp.size() == a.size()) break;
        }
        return ret;
    }
};
```

# T2

```
class Solution {
public:
    int countTriplets(vector<int>& a) {
        int n = a.size();
        vector<int> s(n+1);
        for (int i = 1; i <= n; ++ i)
            s[i] = s[i-1]^a[i-1];
        int ret = 0;
        for (int i = 1; i <= n; ++ i)
            for (int j = i+1; j <= n; ++ j)
                for (int k = j; k <= n; ++ k)
                {
                    if ((s[j-1]^s[i-1]) == (s[k]^s[j-1])) ret ++;
                }
        return ret;
    }
};
```

python
```
class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        pre = 0
        cnt = collections.defaultdict(list)
        cnt[0].append(-1)
        res = 0

        for i, a in enumerate(arr):
            pre ^= a
            for p in cnt[pre]:
                res += i - p - 1
            cnt[pre].append(i)

        return res
```

# T3

```
class Solution {
public:
    int minTime(int n, vector<vector<int>>& edges, vector<bool>& hasApple) {
        vector<vector<int>> v(n);
        for (auto e : edges)
        {
            int x=  e[0], y = e[1];
            v[x].push_back(y);
            v[y].push_back(x);
        }
        vector<int> sz(n);
        function<void(int,int)> dfs = [&](int x, int pre)
        {
            sz[x] = hasApple[x];
            for (auto y : v[x])
            {
                if (y == pre) continue;
                dfs(y, x);
                sz[x] += sz[y];
            }
        };
        dfs(0, -1);

        int ret = 0;
        function<void(int,int)> dfs2 = [&](int x, int pre)
        {
            for (auto y : v[x])
            {
                if (y == pre) continue;
                if (sz[y])
                {
                    ret += 2;
                    dfs2(y, x);
                }
            }
        };
        dfs2(0, -1);

        return ret;
    }
};
```

# T4

```
int f[15][55][55];
int s[55][55];
const int MOD = 1000000007;

class Solution {
public:
    int ways(vector<string>& g, int k) {
        int n = g.size(), m = g[0].size();
        for (int i = 0; i <= k; ++ i)
            for (int x = 0; x <= n; ++ x)
                for (int y = 0; y <= m; ++ y)
                {
                    f[i][x][y] = 0;
                    s[x][y] = 0;
                }
        for (int x = 1; x <= n; ++ x)
            for (int y = 1; y <= m; ++ y)
            {
                s[x][y] = s[x-1][y]+s[x][y-1]-s[x-1][y-1]+(g[x-1][y-1] == 'A');
            }
        auto calc = [&](int x1, int x2, int y1, int y2)
        {
            return s[x2+1][y2+1]-s[x2+1][y1]-s[x1][y2+1]+s[x1][y1];
        };
        f[0][0][0] = 1;
        for (int i = 0; i < k; ++ i)
            for (int x = 0; x < n; ++ x)
                for (int y = 0; y < m; ++ y)
                {
                    for (int xx = x+1; xx <= n; ++ xx)
                    {
                        if (calc(x, xx-1, y, m-1))
                            (f[i+1][xx][y] += f[i][x][y]) %= MOD;
                    }
                    for (int yy = y+1; yy <= m; ++ yy)
                    {
                        if (calc(x, n-1, y, yy-1))
                            (f[i+1][x][yy] += f[i][x][y]) %= MOD;
                    }
                }
        int ret = 0;
        for (int x = 0; x < n; ++ x)
            for (int y = 0; y < m; ++ y)
                if (calc(x, n-1, y, m-1))
                    (ret += f[k-1][x][y]) %= MOD;
        return ret;
    }
};
```

# atrticles

```
[5404] 用栈操作构建数组
题目思考
这道题反其道行之, 给了目标数组, 让推导出操作序列
看上去只有两种情况: 在目标数组, 和不在目标数组
目标数组是递增的, 是否可以利用这一点?
解决方案
思路
存当前应该 push 的下标 cur
遍历目标数组
如果当前值 t 恰好等于 cur, 那么直接加个 push 操作, 同时更新下标为 t+1
否则对于[cur,t)之间的元素, 都应该一个 push 一个 pop 让它们进下 stack 就走..之后也不要忘了 push t, 以及更新下标
复杂度
时间复杂度 O(N): 需要遍历 target 数组
空间复杂度 O(1): 只使用了几个变量
代码
Python 3


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res = []
        cur = 1
        for t in target:
            if t != cur:
                # t一定大于cur
                res.extend(['Push', 'Pop'] * (t - cur))
            res.append('Push')
            cur = t + 1
        return res
[5405] 形成两个异或相等数组的三元组数目
题目思考
题目很直白, 直接暴力三重循环可以吗?
是否可以通过预处理进行优化?
解决方案
思路
直接三重循环的做法很直白, 但其复杂度过高 (python 3 需要 5000ms...), 这里就忽略了
这里提供一种预处理的方法 (python 3 使用这种方法只需要 196ms):
先拿到所有区间的异或结果
将结果存入字典中作为 key
字典的 value 也是一个字典, key 是区间起始下标, value 是区间结束下标集合
这样可以只需遍历每个起始下标 s 对应的终点下标 e 集合, 如果 e+1 也在当前字典中, 那么 res 就加上 e+1 对应的终点下标集合长度
复杂度
时间复杂度 O(N^2): 预处理需要 O(N^2), 求结果也是 O(N^2)
空间复杂度 O(N^2): 字典中存了 O(N^2)的下标元素
代码
Python 3
class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        d = collections.defaultdict(dict)
        # 预处理字典 {a:{s:[e1,e2,...]}}
        for i in range(n):
            a = 0
            for j in range(i, n):
                a^=arr[j]
                if i not in d[a]:
                    d[a][i] = []
                d[a][i].append(j)
        res = 0
        # 这里虽然表面是三重循环
        # 但实际k*s才相当于原先的数组元素数目N
        # 所以复杂度还是O(N^2)
        for k in d:
            for s in d[k]:
                for e in d[k][s]:
                    if e+1 in d[k]:
                        res+=len(d[k][e+1])

        return res
[5406] 收集树上所有苹果的最少时间
题目思考
这道题要用什么思路呢? 贪心? DFS? BFS?
仔细观察示例图和结果, 是否有什么发现?
解决方案
思路
要收集到所有苹果, 充要条件是每个有苹果的节点都要走一遍
对于那些本身没有苹果, 且子树没有苹果的节点, 完全不需要走到它们
所以如果能够统计出所有自身或者子树有苹果的节点, 然后把这些节点都走一遍, 就是最优方案
假设节点数为 n, 由于题目是个树, 所以这些节点构成的路径数目是 n-1, 最优情况就是每个路径走 2 次, 一来一回, 结果就是 2*(n-1)
如何求自身或者子树有苹果的节点呢? 可以想到使用递归, 结果返回当前节点及子树是否有苹果, 然后逐层上去即可
复杂度
时间复杂度 O(N): 初始化路径和递归各需要遍历每个节点一次
空间复杂度 O(N): 使用了一个字典, 字典元素总数为节点数目, 还有递归的栈的消耗
代码
Python 3

class Solution:
    def minTime(self, n: int, edges: List[List[int]],
                hasApple: List[bool]) -> int:
        # 初始化路径
        maps = collections.defaultdict(list)
        for e in edges:
            maps[e[0]].append(e[1])

        def dfs(i):
            selfOrChildHasApple = hasApple[i]
            for nex in maps[i]:
                selfOrChildHasApple |= dfs(nex)
            if not selfOrChildHasApple:
                # 从字典中移除自身或子树都没有苹果的节点
                del maps[i]
            return selfOrChildHasApple

        dfs(0)
        # 字典个数即为最终有效节点的个数
        # 但是有可能有效节点为0, 所以需要max一下
        return max(0, 2 * (len(maps) - 1))
[5407] 切披萨的方案数
题目思考
注意到这道题的数据规模很小, 是不是可以利用多个状态记忆化搜索或动态规划?
状态的选择: 每次分出去的都是上面或者左边的, 是否可以利用这一点?
可否通过一些预处理来加速运算呢?
解决方案
思路
记忆化搜索/动态规划
memo[r,c,p]表示矩形[(r,c), (rows-1, cols-1)]分给 p 个人的方案数
那么 memo[r,c,p] = sum(memo[nexr, c, p-1]) + sum(r, nexc, p-1) (r+1<=nexr<rows, c+1<=nexc<colsm, 且[r, nexr)以及[c, nexc]之间的部分要有苹果分给当前的人)
至于怎么求[r, nexr)以及[c, nexc]之间的部分要有苹果分给当前的人, 如果每次递归的时候都重新计算, 那太慢了大概率会超时吧..这部分完全可以事先预处理求得
所以额外定义几个字典, rightcnt/downcnt/cnt 分别表示当前坐标右边一行, 下边一列, 以及右下矩形的苹果数目, 右下矩形的苹果数目可以用于剪枝, 当数目<所需人数时直接返回 0 即可
复杂度
时间复杂度 O(rows*cols*k*(rows+cols))): 需要搜索 rows*cols*k 个状态, 而且搜索时要对接下来的 r 或者 c 求和, 根据本题数据量, 就是 50*50*10*100, 还算可以接受(如果有更优解欢迎指出 🤩)
空间复杂度 O(rows*cols*k): memo 的元素个数
代码
Python 3
class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        mod = 10**9 + 7
        memo = {}
        rightdowncnt = collections.defaultdict(int)
        downcnt = collections.defaultdict(int)
        rightcnt = collections.defaultdict(int)
        rows, cols = len(pizza), len(pizza[0])
        # 预处理, 求三种cnt字典
        for c in range(cols):
            for r in range(rows)[::-1]:
                downcnt[r, c] = 1 if pizza[r][c] == 'A' else 0
                downcnt[r, c] += downcnt[r + 1, c]
        for r in range(rows):
            for c in range(cols)[::-1]:
                rightcnt[r, c] = 1 if pizza[r][c] == 'A' else 0
                rightcnt[r, c] += rightcnt[r, c + 1]
        for r in range(rows)[::-1]:
            for c in range(cols)[::-1]:
                rightdowncnt[r, c] = 1 if pizza[r][c] == 'A' else 0
                rightdowncnt[r,
                             c] += rightdowncnt[r + 1, c] + rightcnt[r, c + 1]

        def dfs(r, c, p):
            # 递归出口
            if r == rows or c == cols:
                return 0
            if (r, c, p) not in memo:
                if rightdowncnt[r, c] < p:
                    # 剪枝
                    memo[r, c, p] = 0
                elif p == 1:
                    # 只有1人时方案数只能为1
                    memo[r, c, p] = 1
                else:
                    sm = 0
                    cnt = 0
                    # 状态转移, 求接下来所有可能的方案数之和
                    # 注意取模
                    for nexr in range(r+1, rows):
                        cnt += rightcnt[nexr-1, c]
                        if cnt > 0:
                            sm = (sm + dfs(nexr, c, p - 1)) % mod
                    cnt = 0
                    for nexc in range(c+1, cols):
                        cnt += downcnt[r, nexc-1]
                        if cnt > 0:
                            sm = (sm + dfs(r, nexc, p - 1)) % mod
                    memo[r, c, p] = sm
            return memo[r, c, p]

        res = dfs(0, 0, k)
        return res

作者：suibianfahui
链接：https://leetcode-cn.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor/solution/di-188-chang-zhou-sai-ti-jie-by-suibianfahui-2/
```