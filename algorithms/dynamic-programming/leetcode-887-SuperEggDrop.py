# encoding=utf8

'''
887. Super Egg Drop
You are given K eggs, and you have access to a building with N floors from 1 to N. 

Each egg is identical in function, and if an egg breaks, you cannot drop it again.

You know that there exists a floor F with 0 <= F <= N such that any egg dropped at a floor higher than F will break, and any egg dropped at or below floor F will not break.

Each move, you may take an egg (if you have an unbroken one) and drop it from any floor X (with 1 <= X <= N). 

Your goal is to know with certainty what the value of F is.

What is the minimum number of moves that you need to know with certainty what F is, regardless of the initial value of F?

 

Example 1:

Input: K = 1, N = 2
Output: 2
Explanation: 
Drop the egg from floor 1.  If it breaks, we know with certainty that F = 0.
Otherwise, drop the egg from floor 2.  If it breaks, we know with certainty that F = 1.
If it didn't break, then we know with certainty F = 2.
Hence, we needed 2 moves in the worst case to know what F is with certainty.
Example 2:

Input: K = 2, N = 6
Output: 3
Example 3:

Input: K = 3, N = 14
Output: 4
 

Note:

1 <= K <= 100
1 <= N <= 10000

887. 鸡蛋掉落
你将获得 K 个鸡蛋，并可以使用一栋从 1 到 N  共有 N 层楼的建筑。

每个蛋的功能都是一样的，如果一个蛋碎了，你就不能再把它掉下去。

你知道存在楼层 F ，满足 0 <= F <= N 任何从高于 F 的楼层落下的鸡蛋都会碎，从 F 楼层或比它低的楼层落下的鸡蛋都不会破。

每次移动，你可以取一个鸡蛋（如果你有完整的鸡蛋）并把它从任一楼层 X 扔下（满足 1 <= X <= N）。

你的目标是确切地知道 F 的值是多少。

无论 F 的初始值如何，你确定 F 的值的最小移动次数是多少？

 

示例 1：

输入：K = 1, N = 2
输出：2
解释：
鸡蛋从 1 楼掉落。如果它碎了，我们肯定知道 F = 0 。
否则，鸡蛋从 2 楼掉落。如果它碎了，我们肯定知道 F = 1 。
如果它没碎，那么我们肯定知道 F = 2 。
因此，在最坏的情况下我们需要移动 2 次以确定 F 是多少。
示例 2：

输入：K = 2, N = 6
输出：3
示例 3：

输入：K = 3, N = 14
输出：4
 

提示：

1 <= K <= 100
1 <= N <= 10000
'''



# 递归，超时
class Solution0(object):
    def superEggDrop(self, K, N):
        """
        :type K: int
        :type N: int
        :rtype: int
        """
        # dp = [0] * (K + 1)
        # m = 0
        # while dp[K] < N:
        #     m += 1
        #     for k in range(K, 0, -1):
        #         dp[k] = dp[k - 1] + dp[k] + 1
        # return m

        hash_map = {}

        def dp(k, n):
            if k == 1 or n == 1 or n == 0:
                # print(n, k, n)
                # hash_map[(k, n)] = n
                return n
            res = n
            if (k, n) in hash_map:
                return hash_map[(k, n)]
            else:
                for x in range(n, 0, -1):
                    res = min(max(dp(k - 1, x - 1), dp(k, n - x)) + 1, res)
                # print(res, k, n)
                hash_map[(k, n)] = res
                return res

        return dp(K, N)


# 递归，二分法优化之后
class Solution2(object):
    def superEggDrop(self, K, N):
        """
        :type K: int
        :type N: int
        :rtype: int
        """

        hash_map = {}

        def dp(k, n):
            if k == 1 or n == 1 or n == 0:
                return n
            res = n
            if (k, n) in hash_map:
                return hash_map[(k, n)]
            else:
                l, r = 0, n
                broken, not_broken = n, n
                while l <= r:
                    mid = (l + r) / 2
                    broken = dp(k - 1, mid - 1)
                    not_broken = dp(k, n - mid)
                    if broken < not_broken:
                        l = mid + 1
                    elif broken > not_broken:
                        r = mid - 1
                    else:
                        break

                res = min(max(broken, not_broken) + 1, res)
                hash_map[(k, n)] = res
                return res

        return dp(K, N)


# 迭代，动态规划， 超时
class SolutionDP(object):
    def superEggDrop(self, K, N):
        """
        :type K: int
        :type N: int
        :rtype: int
        """
        # dp = [0] * (K + 1)
        # m = 0
        # while dp[K] < N:
        #     m += 1
        #     for k in range(K, 0, -1):
        #         dp[k] = dp[k - 1] + dp[k] + 1
        # return m

        hash_map = [[N for i in range(N+1)] for j in range(K+1)]
        for i in range(N+1):
            hash_map[1][i] = i
            hash_map[0][i] = 0
        for j in range(K+1):
            hash_map[j][0] = 0
        for k in range(2, K+1):
            for i in range(1, N+1):
                min_val = N
                for x in range(1, N+1):
                    min_val = min(max(hash_map[k - 1][x - 1], hash_map[k][i - x]) + 1, min_val)
                # print(res, k, n)
                hash_map[k][i] = min_val
        for i in range(K+1):
            print(hash_map[i])
        return hash_map[K][N]


# dp[k][m] = dp[k][m - 1] + dp[k - 1][m - 1] + 1

# dp[k][m - 1] 就是楼上的楼层数，因为鸡蛋个数 k 不变，也就是鸡蛋没碎，扔鸡蛋次数 m 减一；

# dp[k - 1][m - 1] 就是楼下的楼层数，因为鸡蛋个数 k 减一，也就是鸡蛋碎了，同时扔鸡蛋次数 m 减一。
class SolutionDP1(object):
    def superEggDrop(self, K, N):
        """
        :type K: int
        :type N: int
        :rtype: int
        """
        dp = [0] * (K + 1)
        m = 0
        while dp[K] < N:
            m += 1
            for k in range(K, 0, -1):
                dp[k] = dp[k - 1] + dp[k] + 1
        return m


'''
换个思路
上面的方法的思路，都还是顺着题目的思路的进行的，其实我们可以换一个思路来想：“求k个鸡蛋在m步内可以测出多少层”。我们令dp[k][m]表示k个鸡蛋在m步内可以测出的最多的层数，那么当我们在第X层扔鸡蛋的时候，就有两种情况：

鸡蛋碎了，我们少了一颗鸡蛋，也用掉了一步，此时测出N - X + dp[k-1][m-1]层，X和它上面的N-X层已经通过这次扔鸡蛋确定大于F；
鸡蛋没碎，鸡蛋的数量没有变，但是用掉了一步，剩余X + dp[k][m-1]，X层及其以下已经通过这次扔鸡蛋确定不会大于F；
也就是说，我们每一次扔鸡蛋，不仅仅确定了下一次扔鸡蛋的楼层的方向，也确定了另一半楼层与F的大小关系，所以在下面的关键代码中，使用的不再是max，而是加法（这里是重点）。评论里有人问到为什么是相加，其实这里有一个惯性思维的误区，上面的诸多解法中，往往求max的思路是“两种方式中较大的那一个结果”，其实这里的相加，不是鸡蛋碎了和没碎两种情况的相加，而是“本次扔之后可能测出来的层数 + 本次扔之前已经测出来的层数”。

class Solution {
    public int superEggDrop(int K, int N) {
        int[][] dp = new int[K + 1][N + 1];
        for (int m = 1; m <= N; m++) {
            dp[0][m] = 0; // zero egg
            for (int k = 1; k <= K; k++) {
                dp[k][m] = dp[k][m - 1] + dp[k - 1][m - 1] + 1;
                if (dp[k][m] >= N) {
                    return m;
                }
            }
        }
        return N;
    }
}
'''

# 大神解析
'''
一、解析题目
题目是这样：你面前有一栋从 1 到 N 共 N 层的楼，然后给你 K 个鸡蛋（K 至少为 1）。现在确定这栋楼存在楼层 0 <= F <= N，在这层楼将鸡蛋扔下去，鸡蛋恰好没摔碎（高于 F 的楼层都会碎，低于 F 的楼层都不会碎）。现在问你，最坏情况下，你至少要扔几次鸡蛋，才能确定这个楼层 F 呢？

也就是让你找摔不碎鸡蛋的最高楼层 F，但什么叫「最坏情况」下「至少」要扔几次呢？我们分别举个例子就明白了。

比方说现在先不管鸡蛋个数的限制，有 7 层楼，你怎么去找鸡蛋恰好摔碎的那层楼？

最原始的方式就是线性扫描：我先在 1 楼扔一下，没碎，我再去 2 楼扔一下，没碎，我再去 3 楼……

以这种策略，最坏情况应该就是我试到第 7 层鸡蛋也没碎（F = 7），也就是我扔了 7 次鸡蛋。

先在你应该理解什么叫做「最坏情况」下了，鸡蛋破碎一定发生在搜索区间穷尽时，不会说你在第 1 层摔一下鸡蛋就碎了，这是你运气好，不是最坏情况。

现在再来理解一下什么叫「至少」要扔几次。依然不考虑鸡蛋个数限制，同样是 7 层楼，我们可以优化策略。

最好的策略是使用二分查找思路，我先去第 (1 + 7) / 2 = 4 层扔一下：

如果碎了说明 F 小于 4，我就去第 (1 + 3) / 2 = 2 层试……

如果没碎说明 F 大于等于 4，我就去第 (5 + 7) / 2 = 6 层试……

以这种策略，最坏情况应该是试到第 7 层鸡蛋还没碎（F = 7），或者鸡蛋一直碎到第 1 层（F = 0）。然而无论那种最坏情况，只需要试 log7 向上取整等于 3 次，比刚才尝试 7 次要少，这就是所谓的至少要扔几次。

PS：这有点像 Big O 表示法计算​算法的复杂度。

实际上，如果不限制鸡蛋个数的话，二分思路显然可以得到最少尝试的次数，但问题是，现在给你了鸡蛋个数的限制 K，直接使用二分思路就不行了。

比如说只给你 1 个鸡蛋，7 层楼，你敢用二分吗？你直接去第 4 层扔一下，如果鸡蛋没碎还好，但如果碎了你就没有鸡蛋继续测试了，无法确定鸡蛋恰好摔不碎的楼层 F 了。这种情况下只能用线性扫描的方法，算法返回结果应该是 7。

有的读者也许会有这种想法：二分查找排除楼层的速度无疑是最快的，那干脆先用二分查找，等到只剩 1 个鸡蛋的时候再执行线性扫描，这样得到的结果是不是就是最少的扔鸡蛋次数呢？

很遗憾，并不是，比如说把楼层变高一些，100 层，给你 2 个鸡蛋，你在 50 层扔一下，碎了，那就只能线性扫描 1～49 层了，最坏情况下要扔 50 次。

如果不要「二分」，变成「五分」「十分」都会大幅减少最坏情况下的尝试次数。比方说第一个鸡蛋每隔十层楼扔，在哪里碎了第二个鸡蛋一个个线性扫描，总共不会超过 20 次​。

最优解其实是 14 次。最优策略非常多，而且并没有什么规律可言。

说了这么多废话，就是确保大家理解了题目的意思，而且认识到这个题目确实复杂，就连我们手算都不容易，如何用算法解决呢？

二、思路分析
对动态规划问题，直接套我们以前多次强调的框架即可：这个问题有什么「状态」，有什么「选择」，然后穷举。

「状态」很明显，就是当前拥有的鸡蛋数 K 和需要测试的楼层数 N。随着测试的进行，鸡蛋个数可能减少，楼层的搜索范围会减小，这就是状态的变化。

「选择」其实就是去选择哪层楼扔鸡蛋。回顾刚才的线性扫描和二分思路，二分查找每次选择到楼层区间的中间去扔鸡蛋，而线性扫描选择一层层向上测试。不同的选择会造成状态的转移。

现在明确了「状态」和「选择」，动态规划的基本思路就形成了：肯定是个二维的 dp 数组或者带有两个状态参数的 dp 函数来表示状态转移；外加一个 for 循环来遍历所有选择，择最优的选择更新状态：

# 当前状态为 K 个鸡蛋，面对 N 层楼
# 返回这个状态下的最优结果
def dp(K, N):
    int res
    for 1 <= i <= N:
        res = min(res, 这次在第 i 层楼扔鸡蛋)
    return res
这段伪码还没有展示递归和状态转移，不过大致的算法框架已经完成了。

我们选择在第 i 层楼扔了鸡蛋之后，可能出现两种情况：鸡蛋碎了，鸡蛋没碎。注意，这时候状态转移就来了：

如果鸡蛋碎了，那么鸡蛋的个数 K 应该减一，搜索的楼层区间应该从 [1..N] 变为 [1..i-1] 共 i-1 层楼；

如果鸡蛋没碎，那么鸡蛋的个数 K 不变，搜索的楼层区间应该从 [1..N] 变为 [i+1..N] 共 N-i 层楼。



PS：细心的读者可能会问，在第i层楼扔鸡蛋如果没碎，楼层的搜索区间缩小至上面的楼层，是不是应该包含第i层楼呀？不必，因为已经包含了。开头说了 F 是可以等于 0 的，向上递归后，第i层楼其实就相当于第 0 层，可以被取到，所以说并没有错误。

因为我们要求的是最坏情况下扔鸡蛋的次数，所以鸡蛋在第 i 层楼碎没碎，取决于那种情况的结果更大：

def dp(K, N):
    for 1 <= i <= N:
        # 最坏情况下的最少扔鸡蛋次数
        res = min(res, 
                  max( 
                        dp(K - 1, i - 1), # 碎
                        dp(K, N - i)      # 没碎
                     ) + 1 # 在第 i 楼扔了一次
                 )
    return res
递归的 base case 很容易理解：当楼层数 N 等于 0 时，显然不需要扔鸡蛋；当鸡蛋数 K 为 1 时，显然只能线性扫描所有楼层：

def dp(K, N):
    if K == 1: return N
    if N == 0: return 0
    ...
至此，其实这道题就解决了！只要添加一个备忘录消除重叠子问题即可：

def superEggDrop(K: int, N: int):

    memo = dict()
    def dp(K, N) -> int:
        # base case
        if K == 1: return N
        if N == 0: return 0
        # 避免重复计算
        if (K, N) in memo:
            return memo[(K, N)]

        res = float('INF')
        # 穷举所有可能的选择
        for i in range(1, N + 1):
            res = min(res, 
                      max(
                            dp(K, N - i), 
                            dp(K - 1, i - 1)
                         ) + 1
                  )
        # 记入备忘录
        memo[(K, N)] = res
        return res
    
    return dp(K, N)
这个算法的时间复杂度是多少呢？动态规划算法的时间复杂度就是子问题个数 × 函数本身的复杂度。

函数本身的复杂度就是忽略递归部分的复杂度，这里 dp 函数中有一个 for 循环，所以函数本身的复杂度是 O(N)。

子问题个数也就是不同状态组合的总数，显然是两个状态的乘积，也就是 O(KN)。

所以算法的总时间复杂度是 O(K*N^2), 空间复杂度 O(KN)。

三、疑难解答
这个问题很复杂，但是算法代码却十分简洁，这就是动态规划的特性，穷举加备忘录/DP table 优化，真的没啥新意。

首先，有读者可能不理解代码中为什么用一个 for 循环遍历楼层 [1..N]，也许会把这个逻辑和之前探讨的线性扫描混为一谈。其实不是的，这只是在做一次「选择」。

比方说你有 2 个鸡蛋，面对 10 层楼，你这次选择去哪一层楼扔呢？不知道，那就把这 10 层楼全试一遍。至于下次怎么选择不用你操心，有正确的状态转移，递归会算出每个选择的代价，我们取最优的那个就是最优解。

另外，这个问题还有更好的解法，比如修改代码中的 for 循环为二分搜索，可以将时间复杂度降为 O(K*N*logN)；再改进动态规划解法可以进一步降为 O(KN)；使用数学方法解决，时间复杂度达到最优 O(K*logN)，空间复杂度达到 O(1)。

二分的解法也有点误导性，你很可能以为它跟我们之前讨论的二分思路扔鸡蛋有关系，实际上没有半毛钱关系。能用二分搜索是因为状态转移方程的函数图像具有单调性，这里就不展开以上解法了。我觉得吧，我们这种解法就够了：找状态，做选择，足够清晰易懂，可流程化，可举一反三。掌握这套框架学有余力的话，再去考虑那些奇技淫巧也不迟。

进阶解法
上篇文章聊了高楼扔鸡蛋问题，讲了一种效率不是很高，但是较为容易理解的动态规划解法。后台很多读者问如何更高效地解决这个问题，今天就谈两种思路，来优化一下这个问题，分别是二分查找优化和重新定义状态转移。

如果还不知道高楼扔鸡蛋问题的读者可以看下「经典动态规划：高楼扔鸡蛋」，那篇文章详解了题目的含义和基本的动态规划解题思路，请确保理解前文，因为今天的优化都是基于这个基本解法的。

二分搜索的优化思路也许是我们可以尽力尝试写出的，而修改状态转移的解法可能是不容易想到的，可以借此见识一下动态规划算法设计的玄妙，当做思维拓展。

二分搜索优化
之前提到过这个解法，核心是因为状态转移方程的单调性，这里可以具体展开看看。

首先简述一下原始动态规划的思路：

1、暴力穷举尝试在所有楼层 1 <= i <= N 扔鸡蛋，每次选择尝试次数最少的那一层；

2、每次扔鸡蛋有两种可能，要么碎，要么没碎；

3、如果鸡蛋碎了，F 应该在第 i 层下面，否则，F 应该在第 i 层上面；

4、鸡蛋是碎了还是没碎，取决于哪种情况下尝试次数更多，因为我们想求的是最坏情况下的结果。

核心的状态转移代码是这段：

# 当前状态为 K 个鸡蛋，面对 N 层楼
# 返回这个状态下的最优结果
def dp(K, N):
    for 1 <= i <= N:
        # 最坏情况下的最少扔鸡蛋次数
        res = min(res, 
                  max( 
                        dp(K - 1, i - 1), # 碎
                        dp(K, N - i)      # 没碎
                     ) + 1 # 在第 i 楼扔了一次
                 )
    return res
这个 for 循环就是下面这个状态转移方程的具体代码实现：

dp(K, N) = \min_{0 <= i <= N}\{\max\{dp(K - 1, i - 1), dp(K, N - i)\} + 1\}
dp(K,N)= 
0<=i<=N
min
​	
 {max{dp(K−1,i−1),dp(K,N−i)}+1}

如果能够理解这个状态转移方程，那么就很容易理解二分查找的优化思路。

首先我们根据 dp(K, N) 数组的定义（有 K 个鸡蛋面对 N 层楼，最少需要扔几次），很容易知道 K 固定时，这个函数随着 N 的增加一定是单调递增的，无论你策略多聪明，楼层增加测试次数一定要增加。

那么注意 dp(K - 1, i - 1) 和 dp(K, N - i) 这两个函数，其中 i 是从 1 到 N 单增的，如果我们固定 K 和 N，把这两个函数看做关于 i 的函数，前者随着 i 的增加应该也是单调递增的，而后者随着 i 的增加应该是单调递减的：



这时候求二者的较大值，再求这些最大值之中的最小值，其实就是求这两条直线交点，也就是红色折线的最低点嘛。

我们前文「二分查找只能用来查找元素吗」讲过，二分查找的运用很广泛，形如下面这种形式的 for 循环代码：

for (int i = 0; i < n; i++) {
    if (isOK(i))
        return i;
}
都很有可能可以运用二分查找来优化线性搜索的复杂度，回顾这两个 dp 函数的曲线，我们要找的最低点其实就是这种情况：

for (int i = 1; i <= N; i++) {
    if (dp(K - 1, i - 1) == dp(K, N - i))
        return dp(K, N - i);
}
熟悉二分搜索的同学肯定敏感地想到了，这不就是相当于求 Valley（山谷）值嘛，可以用二分查找来快速寻找这个点的，直接看代码吧，整体的思路还是一样，只是加快了搜索速度：

def superEggDrop(self, K: int, N: int) -> int:
        
    memo = dict()
    def dp(K, N):
        if K == 1: return N
        if N == 0: return 0
        if (K, N) in memo:
            return memo[(K, N)]
                            
        # for 1 <= i <= N:
        #     res = min(res, 
        #             max( 
        #                 dp(K - 1, i - 1), 
        #                 dp(K, N - i)      
        #                 ) + 1 
        #             )

        res = float('INF')
        # 用二分搜索代替线性搜索
        lo, hi = 1, N
        while lo <= hi:
            mid = (lo + hi) // 2
            broken = dp(K - 1, mid - 1) # 碎
            not_broken = dp(K, N - mid) # 没碎
            # res = min(max(碎，没碎) + 1)
            if broken > not_broken:
                hi = mid - 1
                res = min(res, broken + 1)
            else:
                lo = mid + 1
                res = min(res, not_broken + 1)

        memo[(K, N)] = res
        return res
    
    return dp(K, N)
这个算法的时间复杂度是多少呢？动态规划算法的时间复杂度就是子问题个数 × 函数本身的复杂度。

函数本身的复杂度就是忽略递归部分的复杂度，这里 dp 函数中用了一个二分搜索，所以函数本身的复杂度是 O(logN)。

子问题个数也就是不同状态组合的总数，显然是两个状态的乘积，也就是 O(KN)。

所以算法的总时间复杂度是 O(K*N*logN), 空间复杂度 O(KN)。效率上比之前的算法 O(KN^2) 要高效一些。

重新定义状态转移
前文「不同定义有不同解法」就提过，找动态规划的状态转移本就是见仁见智，比较玄学的事情，不同的状态定义可以衍生出不同的解法，其解法和复杂程度都可能有巨大差异。这里就是一个很好的例子。

再回顾一下我们之前定义的 dp 数组含义：

def dp(k, n) -> int
# 当前状态为 k 个鸡蛋，面对 n 层楼
# 返回这个状态下最少的扔鸡蛋次数
用 dp 数组表示的话也是一样的：

dp[k][n] = m
# 当前状态为 k 个鸡蛋，面对 n 层楼
# 这个状态下最少的扔鸡蛋次数为 m
按照这个定义，就是确定当前的鸡蛋个数和面对的楼层数，就知道最小扔鸡蛋次数。最终我们想要的答案就是 dp(K, N) 的结果。

这种思路下，肯定要穷举所有可能的扔法的，用二分搜索优化也只是做了「剪枝」，减小了搜索空间，但本质思路没有变，还是穷举。

现在，我们稍微修改 dp 数组的定义，确定当前的鸡蛋个数和最多允许的扔鸡蛋次数，就知道能够确定 F 的最高楼层数。具体来说是这个意思：

dp[k][m] = n
# 当前有 k 个鸡蛋，可以尝试扔 m 次鸡蛋
# 这个状态下，最坏情况下最多能确切测试一栋 n 层的楼

# 比如说 dp[1][7] = 7 表示：
# 现在有 1 个鸡蛋，允许你扔 7 次;
# 这个状态下最多给你 7 层楼，
# 使得你可以确定楼层 F 使得鸡蛋恰好摔不碎
# （一层一层线性探查嘛）
这其实就是我们原始思路的一个「反向」版本，我们先不管这种思路的状态转移怎么写，先来思考一下这种定义之下，最终想求的答案是什么？

我们最终要求的其实是扔鸡蛋次数 m，但是这时候 m 在状态之中而不是 dp 数组的结果，可以这样处理：

int superEggDrop(int K, int N) {

    int m = 0;
    while (dp[K][m] < N) {
        m++;
        // 状态转移...
    }
    return m;
}
题目不是给你 K 鸡蛋，N 层楼，让你求最坏情况下最少的测试次数 m 吗？while 循环结束的条件是 dp[K][m] == N，也就是给你 K 个鸡蛋，测试 m 次，最坏情况下最多能测试 N 层楼。

注意看这两段描述，是完全一样的！所以说这样组织代码是正确的，关键就是状态转移方程怎么找呢？还得从我们原始的思路开始讲。之前的解法配了这样图帮助大家理解状态转移思路：



这个图描述的仅仅是某一个楼层 i，原始解法还得线性或者二分扫描所有楼层，要求最大值、最小值。但是现在这种 dp 定义根本不需要这些了，基于下面两个事实：

1、无论你在哪层楼扔鸡蛋，鸡蛋只可能摔碎或者没摔碎，碎了的话就测楼下，没碎的话就测楼上。

2、无论你上楼还是下楼，总的楼层数 = 楼上的楼层数 + 楼下的楼层数 + 1（当前这层楼）。

根据这个特点，可以写出下面的状态转移方程：

dp[k][m] = dp[k][m - 1] + dp[k - 1][m - 1] + 1

dp[k][m - 1] 就是楼上的楼层数，因为鸡蛋个数 k 不变，也就是鸡蛋没碎，扔鸡蛋次数 m 减一；

dp[k - 1][m - 1] 就是楼下的楼层数，因为鸡蛋个数 k 减一，也就是鸡蛋碎了，同时扔鸡蛋次数 m 减一。

PS：这个 m 为什么要减一而不是加一？之前定义得很清楚，这个 m 是一个允许的次数上界，而不是扔了几次。



至此，整个思路就完成了，只要把状态转移方程填进框架即可：

int superEggDrop(int K, int N) {
    // m 最多不会超过 N 次（线性扫描）
    int[][] dp = new int[K + 1][N + 1];
    // base case:
    // dp[0][..] = 0
    // dp[..][0] = 0
    // Java 默认初始化数组都为 0
    int m = 0;
    while (dp[K][m] < N) {
        m++;
        for (int k = 1; k <= K; k++)
            dp[k][m] = dp[k][m - 1] + dp[k - 1][m - 1] + 1;
    }
    return m;
}
如果你还觉得这段代码有点难以理解，其实它就等同于这样写：

for (int m = 1; dp[K][m] < N; m++)
    for (int k = 1; k <= K; k++)
        dp[k][m] = dp[k][m - 1] + dp[k - 1][m - 1] + 1;
看到这种代码形式就熟悉多了吧，因为我们要求的不是 dp 数组里的值，而是某个符合条件的索引 m，所以用 while 循环来找到这个 m 而已。

这个算法的时间复杂度是多少？很明显就是两个嵌套循环的复杂度 O(KN)。

另外注意到 dp[m][k] 转移只和左边和左上的两个状态有关，所以很容易优化成一维 dp 数组，这里就不写了。

还可以再优化
再往下就要用一些数学方法了，不具体展开，就简单提一下思路吧。

在刚才的思路之上，注意函数 dp(m, k) 是随着 m 单增的，因为鸡蛋个数 k 不变时，允许的测试次数越多，可测试的楼层就越高。

这里又可以借助二分搜索算法快速逼近 dp[K][m] == N 这个终止条件，时间复杂度进一步下降为 O(KlogN)，我们可以设 g(k, m) =……

算了算了，打住吧。我觉得我们能够写出 O(K*N*logN) 的二分优化算法就行了，后面的这些解法呢，听个响鼓个掌就行了，把欲望限制在能力的范围之内才能拥有快乐！

不过可以肯定的是，根据二分搜索代替线性扫描 m 的取值，代码的大致框架肯定是修改穷举 m 的 for 循环：

// 把线性搜索改成二分搜索
// for (int m = 1; dp[K][m] < N; m++)
int lo = 1, hi = N;
while (lo < hi) {
    int mid = (lo + hi) / 2;
    if (... < N) {
        lo = ...
    } else {
        hi = ...
    }
    
    for (int k = 1; k <= K; k++)
        // 状态转移方程
}
简单总结一下吧，第一个二分优化是利用了 dp 函数的单调性，用二分查找技巧快速搜索答案；第二种优化是巧妙地修改了状态转移方程，简化了求解了流程，但相应的，解题逻辑比较难以想到；后续还可以用一些数学方法和二分搜索进一步优化第二种解法，不过看了看镜子中的发量，算了。

作者：labuladong
链接：https://leetcode-cn.com/problems/super-egg-drop/solution/ji-ben-dong-tai-gui-hua-jie-fa-by-labuladong/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''

if __name__ == '__main__':
    demo = Solution1()
    print(demo.superEggDrop(2, 100))
