'''
LCP 14. 切分数组
给定一个整数数组 nums ，小李想将 nums 切割成若干个非空子数组，使得每个子数组最左边的数和最右边的数的最大公约数大于 1 。为了减少他的工作量，请求出最少可以切成多少个子数组。

示例 1：

输入：nums = [2,3,3,2,3,3]

输出：2

解释：最优切割为 [2,3,3,2] 和 [3,3] 。第一个子数组头尾数字的最大公约数为 2 ，第二个子数组头尾数字的最大公约数为 3 。

示例 2：

输入：nums = [2,3,5,7]

输出：4

解释：只有一种可行的切割：[2], [3], [5], [7]

限制：

1 <= nums.length <= 10^5
2 <= nums[i] <= 10^6
'''


max_num = 1000000
min_factor = [1] * (max_num + 1)
p = 2

# O(M loglog M)
while (p <= max_num):
    i = p
    while i * p <= max_num:
        if min_factor[i * p] == 1:
            min_factor[i * p] = p
        i += 1

    p += 1
    while p <= max_num:
        if min_factor[p] == 1:
            break

        p += 1

class Solution():
    def splitArray(self, nums):
        f = {}
        n = len(nums)

        x = nums[0]
        INF = 100000000
        while True:
            if min_factor[x] == 1:
                f[x] = 1
                break

            f[min_factor[x]] = 1
            x //= min_factor[x]

        min_prev = 1
        for i in range(1, n):
            x = nums[i]

            min_cur = INF
            while True:
                if min_factor[x] == 1:
                    f[x] = min(f.get(x, INF), min_prev + 1)
                    min_cur = min(min_cur, f[x])
                    break

                f[min_factor[x]] = min(f.get(min_factor[x], INF), min_prev + 1)
                min_cur = min(min_cur, f[min_factor[x]])
                x //= min_factor[x]

            min_prev = min_cur

        return min_prev


'''
题意概述：
将数组切分成若干个子数组，使得每个子数组最左边和最右边数字的最大公约数大于 1，求解最少能切成多少个子数组。

题解：
素数筛 + DP

一个比较直观的解法是（下标从 0 开始）：

f[i] = \min\{f[j] + 1 | 0 \leq j < i - 1\ \&\&\ gcd(nums[j+1], nums[i]) > 1\}\\ Answer=f[n - 1]
f[i]=min{f[j]+1∣0≤j<i−1 && gcd(nums[j+1],nums[i])>1}
Answer=f[n−1]

但这个解法是 O(n^2)O(n 
2
 ) 的，我们在这个想法基础上进行优化。

我们需要重新给出 f[i]f[i] 的定义：f[i]f[i] 代表这个数组新增一个质数 ii 后的最少分组数。例如对于数组 [2,5,3] ，我们有 f[2] = 1, f[3] = 3, f[5] = 2f[2]=1,f[3]=3,f[5]=2, 在插入一个新的数 6 后，对于当前数组 [2,5,3,6] ，我们有 f[2] = 1, f[3] = 2, f[5] = 2f[2]=1,f[3]=2,f[5]=2 。

于是我们在遍历整个数组时，只要对每次遍历到的数做质因数分解，假设当前分解得到的质数为 pp ，上一次遍历的最好结果为 prevprev ，就可以做如下更新：

f[p] = \min(f[p], prev + 1)
f[p]=min(f[p],prev+1)

其含义为当前这个数要么跟之前的某个数组成一个子数组，要么单独成一组。这样遍历下去就能高效求得答案了。

由于需要知道每个 nums[i]nums[i] 的所有质因子，我们需要一种方法将 nums[i]nums[i] 快速因子分解。我们用素数筛提前预处理 1 \sim 10^61∼10 
6
  内任意数字 kk 的最小质因子 min\_prime\_factor[k]min_prime_factor[k] 。获得 nums[i]nums[i] 所有质因子的方法为：

x=nums[i]x=nums[i]

获取 min\_prime\_factor[x]min_prime_factor[x] 为 xx 当前的最小质因子

x = x / min\_prime\_factor[x]x=x/min_prime_factor[x]

如果 x=1x=1，退出，否则回到步骤 2

c++python
class Solution {
public:
    int min_prime[1000010], prime[100010];
    int g[1000010];
    int splitArray(vector<int>& nums) {
        int n = nums.size(), m = 2;
        for(int i = 0; i < n; i++)
            m = max(m, nums[i]);
        for(int i = 2; i <= m; i++) {
            if(!min_prime[i]) {
                prime[++prime[0]] = i;
                min_prime[i] = i;
            }
            for(int j = 1; j <= prime[0]; j++) {
                if(i > m / prime[j]) break;
                min_prime[i * prime[j]] = prime[j];
                if(i % prime[j] == 0) break;
            }
        }
        for(int j = 1; j <= prime[0]; j++) g[prime[j]] = n;
        for(int x = nums[0]; x > 1; x /= min_prime[x])
            g[min_prime[x]] = 0;
        int ans = 1;
        for(int i = 0; i < n; i++) {
            ans = i + 1;
            for(int x = nums[i]; x > 1; x /= min_prime[x])
                ans = min(g[min_prime[x]] + 1, ans);
            if(i == n - 1) break;
            for(int x = nums[i + 1]; x > 1; x /= min_prime[x])
                g[min_prime[x]] = min(g[min_prime[x]], ans);
        }
        return ans;
    }
};
复杂度分析
时间复杂度：O(N\log M + M)O(NlogM+M)。

其中 M=\max_{0 \leq i < N - 1}(nums[i])M=max 
0≤i<N−1
​	
 (nums[i]) 。

对于每个数，需要遍历他所有质因子，并在此过程中进行 DP 状态转移，所以需将每个数不断除以它的最大质因子，此处的时间复杂度为 O(N\log M)O(NlogM)。

预处理 1\sim 10^61∼10 
6
  以内每个数最大质因子的时间复杂度为 O(M)O(M) 。

空间复杂度：O(M)O(M)。

预处理过程中求出所有质因子需要一个长度为 O(M)O(M) 的数组，同时，状态转移时需要在这些质因子上做DP转移，若不做特殊优化，此处也需要一个长度为 O(M)O(M) 的转移数组 gg 。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/qie-fen-shu-zu/solution/qie-fen-shu-zu-zhi-shu-shai-dp-by-leetcode-solutio/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''