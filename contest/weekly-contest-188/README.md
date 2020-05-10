

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