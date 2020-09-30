'''
LCP 19. 秋叶收藏集
小扣出去秋游，途中收集了一些红叶和黄叶，他利用这些叶子初步整理了一份秋叶收藏集 leaves， 字符串 leaves 仅包含小写字符 r 和 y， 其中字符 r 表示一片红叶，字符 y 表示一片黄叶。
出于美观整齐的考虑，小扣想要将收藏集中树叶的排列调整成「红、黄、红」三部分。每部分树叶数量可以不相等，但均需大于等于 1。每次调整操作，小扣可以将一片红叶替换成黄叶或者将一片黄叶替换成红叶。请问小扣最少需要多少次调整操作才能将秋叶收藏集调整完毕。

示例 1：

输入：leaves = "rrryyyrryyyrr"

输出：2

解释：调整两次，将中间的两片红叶替换成黄叶，得到 "rrryyyyyyyyrr"

示例 2：

输入：leaves = "ryr"

输出：0

解释：已符合要求，不需要额外操作

提示：

3 <= leaves.length <= 10^5
leaves 中只包含字符 'r' 和字符 'y'
'''


class Solution(object):
    def minimumOperations(self, leaves):
        """
        :type leaves: str
        :rtype: int
        """
        length = len(leaves)
        # rrrr, ry, ryr
        dp = [[float("inf")] * length, [float("inf")] * length, [float("inf")] * length]

        dp[0][0] = 1 if leaves[0] == "y" else 0
        for i in range(1, length):
            if leaves[i] == "y":
                dp[0][i] = dp[0][i - 1] + 1
                dp[1][i] = min(dp[0][i - 1], dp[1][i - 1])
                dp[2][i] = min(dp[1][i - 1], dp[2][i - 1]) + 1
            else:
                dp[0][i] = dp[0][i - 1]
                dp[1][i] = min(dp[0][i - 1], dp[1][i - 1]) + 1
                dp[2][i] = min(dp[1][i - 1], dp[2][i - 1])

        return dp[2][-1]

# solution
'''
方法一：动态规划
思路与算法

由于我们想要将收藏集中树叶的排列调整成「红、黄、红」三部分，因此我们可以用 33 个状态分别表示其中的每一部分，即状态 00 和状态 22 分别表示前面和后面的红色部分，状态 11 表示黄色部分。

此时，我们就可以尝试使用动态规划解决本题了。我们用 f[i][j]f[i][j] 表示对于第 00 片到第 ii 片叶子（记为 \textit{leaves}[0..i]leaves[0..i]）进行调整操作，并且第 ii 片叶子处于状态 jj 时的最小操作次数。在推导状态转移方程时，我们可以分别对于每一种状态进行分析。

当 j=0j=0 时，我们需要将第 ii 片叶子变成红色，并且第 i-1i−1 片叶子也只能处于 j=0j=0 的状态（因为没有编号更小的状态了），因此有状态转移方程：

f[i][0] = f[i-1][0] + \text{isYellow}(i)
f[i][0]=f[i−1][0]+isYellow(i)

其中 \text{isYellow}(i)isYellow(i) 为示性函数，当第 ii 片叶子为黄色时为 11，红色时为 00。

当 j=1j=1 时，我们需要将第 ii 片叶子变成黄色，而第 i-1i−1 片叶子既可以处于 j=1j=1 的状态，也可以处于 j=0j=0 的状态，我们选择其中的较小值，因此有状态转移方程：

f[i][1] = \min \{ f[i-1][0], f[i-1][1] \} + \text{isRed}(i)
f[i][1]=min{f[i−1][0],f[i−1][1]}+isRed(i)

其中 \text{isRed}(i)isRed(i) 为示性函数，当第 ii 片叶子为红色时为 11，黄色时为 00。

当 j=2j=2 时，我们需要将第 ii 片叶子变成红色，而第 i-1i−1 片叶子即可以处于 j=2j=2 的状态，也可以处于 j=1j=1 的状态（注意这里不能处于 j=0j=0 的状态，因为每一种状态包含的叶子数量必须至少为 11），我们选择其中的较小值，因此有状态转移方程：

f[i][2] = \min \{ f[i-1][1], f[i-1][2] \} + \text{isYellow}(i)
f[i][2]=min{f[i−1][1],f[i−1][2]}+isYellow(i)

最终的答案即为 f[n-1][2]f[n−1][2]，其中 nn 是字符串 \textit{leaves}leaves 的长度，也就是树叶的总数。

细节

由于 因为每一种状态包含的叶子数量必须至少为 11，因此不仅需要特别注意 j=2j=2 时的状态转移方程，还需要考虑每个状态本身是否是符合要求的。对于状态 f[i][j]f[i][j] 而言，它包含了 \textit{leaves}[0..i]leaves[0..i] 共 i+1i+1 片叶子以及 j+1j+1 个状态，因此 叶子的数量必须大于等于状态的数量，即满足 i \geq ji≥j。这样一来，所有 i < ji<j 的状态 f[i][j]f[i][j] 都是不符合要求的。观察上面的状态转移方程，我们在每一步转移时都是取最小值，因此我们可以将所有不符合要求的状态置为一个极大值（例如 n+1n+1 或整数类型的上限等）。

同时需要注意的是，当 i=0i=0 时，f[i][..]f[i][..] 会从 f[i-1][..]f[i−1][..] 转移而来，但后者是没有意义的，因此我们需要对 f[i][..]f[i][..] 进行特殊处理。由于当 i=0i=0 时，jj 也只能为 00，因此我们有：

f[0][0] = \text{isYellow}(0)
f[0][0]=isYellow(0)

作为唯一的边界条件。

代码

C++JavaPython3GolangC

class Solution:
    def minimumOperations(self, leaves: str) -> int:
        n = len(leaves)
        f = [[0, 0, 0] for _ in range(n)]
        f[0][0] = int(leaves[0] == "y")
        f[0][1] = f[0][2] = f[1][2] = float("inf")

        for i in range(1, n):
            isRed = int(leaves[i] == "r")
            isYellow = int(leaves[i] == "y")
            f[i][0] = f[i - 1][0] + isYellow
            f[i][1] = min(f[i - 1][0], f[i - 1][1]) + isRed
            if i >= 2:
                f[i][2] = min(f[i - 1][1], f[i - 1][2]) + isYellow
        
        return f[n - 1][2]
复杂度分析

时间复杂度：O(n)O(n)，其中 nn 是字符串 \textit{leaves}leaves 的长度。

空间复杂度：O(n)O(n)。

可以使用「降维」优化，用三个变量代替状态数组，即可将空间复杂度降低到 O(1)O(1)。具体操作留给读者自行实现。
方法二：前缀和 + 动态规划
思路与算法

我们也可以尝试从整体的角度考虑这个问题。

假设我们希望将 \textit{leaves}[0..x]leaves[0..x]，\textit{leaves}[x+1..y]leaves[x+1..y] 以及 \textit{leaves}[y+1..n-1]leaves[y+1..n−1] 分别作为每一部分，那么需要的操作次数为：

\sum_{i=0}^x \text{isYellow}(i) + \sum_{i=x+1}^y \text{isRed}(i) + \sum_{i=y+1}^{n-1} \text{isYellow}(i)
i=0
∑
x
​	
 isYellow(i)+ 
i=x+1
∑
y
​	
 isRed(i)+ 
i=y+1
∑
n−1
​	
 isYellow(i)

如果我们枚举 xx 和 yy，并且使用前缀和的思路快速计算出上面的三项累加和，那么时间复杂度为 O(n^2)O(n 
2
 )，无法通过本题。因此我们可以考虑枚举一个位置（例如 yy）并找出可以使得上述累加和达到最小值的 xx。

我们用 \textit{pre}_Rpre 
R
​	
  表示 \text{isRed}isRed 的前缀和，\textit{pre}_Ypre 
Y
​	
  表示 \text{isYellow}isYellow 的前缀和。当我们枚举 yy 时，分别考虑这三项累加和：

第一项即为 \textit{pre}_Y(x)pre 
Y
​	
 (x)；

第二项可以进行拆分，即为 \textit{pre}_R(y) - \textit{pre}_R(x)pre 
R
​	
 (y)−pre 
R
​	
 (x)；

第三项也可以进行拆分，即为 \textit{pre}_Y(n-1) - \textit{pre}_Y(y)pre 
Y
​	
 (n−1)−pre 
Y
​	
 (y)。

那么上述的累加和可以写成：

\textit{pre}_Y(n-1) + \big( \textit{pre}_Y(x) - \textit{pre}_R(x) \big) - \big( \textit{pre}_Y(y) - \textit{pre}_R(y) \big)
pre 
Y
​	
 (n−1)+(pre 
Y
​	
 (x)−pre 
R
​	
 (x))−(pre 
Y
​	
 (y)−pre 
R
​	
 (y))

其中 \textit{pre}_Y(n-1)pre 
Y
​	
 (n−1) 是定值，\textit{pre}_Y(x) - \textit{pre}_R(x)pre 
Y
​	
 (x)−pre 
R
​	
 (x) 与 yy 无关，\textit{pre}_Y(y) - \textit{pre}_R(y)pre 
Y
​	
 (y)−pre 
R
​	
 (y) 与 yy 相关。

因此，当我们枚举 yy 时，我们只要选择最小的 \textit{pre}_Y(x) - \textit{pre}_R(x)pre 
Y
​	
 (x)−pre 
R
​	
 (x) 即可。这个最小值可以在枚举 yy 的同时进行记录。

细节

上述方法只需要预处理出 \textit{pre}_Rpre 
R
​	
  和 \textit{pre}_Ypre 
Y
​	
  即可，但还有更加方便的方法。我们可以注意到：

\textit{pre}_Y(i) + \textit{pre}_R(i) \equiv i+1
pre 
Y
​	
 (i)+pre 
R
​	
 (i)≡i+1

恒成立，因此有：

\begin{aligned} \textit{pre}_Y(x) - \textit{pre}_R(x) &= \textit{pre}_Y(x) - (x+1 - \textit{pre}_Y(x)) \\ &= 2 \cdot \textit{pre}_Y(x) - (x+1) \end{aligned}
pre 
Y
​	
 (x)−pre 
R
​	
 (x)
​	
  
=pre 
Y
​	
 (x)−(x+1−pre 
Y
​	
 (x))
=2⋅pre 
Y
​	
 (x)−(x+1)
​	
 

令 g(x) = 2 \cdot \textit{pre}_Y(x) - (x+1)g(x)=2⋅pre 
Y
​	
 (x)−(x+1)，累加和可以继续改写成：

\textit{pre}_Y(n-1) + g(x) - g(y)
pre 
Y
​	
 (n−1)+g(x)−g(y)

并且 gg 有递推式：

\begin{aligned} g(x+1)-g(x) &= \big( 2 \cdot \textit{pre}_Y(x+1) - (x+2) \big) - \big( 2 \cdot \textit{pre}_Y(x) - (x+1) \big) \\ &= 2 \cdot \big( \textit{pre}_Y(x+1) - \textit{pre}_Y(x) \big) -1 \\ &= 2 \cdot \text{isYellow}(x+1) - 1 \end{aligned}
g(x+1)−g(x)
​	
  
=(2⋅pre 
Y
​	
 (x+1)−(x+2))−(2⋅pre 
Y
​	
 (x)−(x+1))
=2⋅(pre 
Y
​	
 (x+1)−pre 
Y
​	
 (x))−1
=2⋅isYellow(x+1)−1
​	
 

因此我们只需要在枚举 yy 的同时计算 gg 值即可，并且 \textit{pre}_Y(n-1)pre 
Y
​	
 (n−1) 这一常数项可以留在最后再累加，它就等于：

\textit{pre}_Y(n-1) = \frac{g(n-1) + n}{2}
pre 
Y
​	
 (n−1)= 
2
g(n−1)+n
​	
 

代码

C++JavaPython3GolangC

class Solution:
    def minimumOperations(self, leaves: str) -> int:
        n = len(leaves)
        g = (1 if leaves[0] == "y" else -1)
        gmin = g
        ans = float("inf")

        for i in range(1, n):
            isYellow = int(leaves[i] == "y")
            g += 2 * isYellow - 1
            if i != n - 1:
                ans = min(ans, gmin - g)
            gmin = min(gmin, g)
        
        return ans + (g + n) // 2
复杂度分析

时间复杂度：O(n)O(n)，其中 nn 是字符串 \textit{leaves}leaves 的长度。

空间复杂度：O(1)O(1)。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/UlBDOe/solution/qiu-xie-shou-cang-ji-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

思路
动态规划

使用 3 个 dp 数组记录状态

dp[0][i] 代表从头开始全部修改成红色（纯红）需要修改几次
dp[1][i] 代表从头开始是红色，然后现在是黄色（红黄），需要修改几次
dp[2][i] 代表从头开始是红色，然后变成黄色，又变成红色（红黄红），需要修改几次
根据 i 是红是黄，判断转移情况

dp[0][i] 就很简单，如果是黄的，就比之前加一
dp[1][i] 可以从上一个纯红状态变化过来，也可以从上一个本身状态变化过来
dp[2][i] 可以从上一个红黄状态变化过来，也可以从上一个本身状态变化过来
所以最后要求的答案即：dp[2].back()

答题
C++

    int minimumOperations(string leaves) {
        vector<vector<int>> dp(3, vector<int>(leaves.size(), 0));

        for (int i = 0; i < leaves.size(); i++) {
            if (i < 1) {
                dp[0][i] = (leaves[i] != 'r');
            }
            else {
                dp[0][i] = dp[0][i - 1] + (leaves[i] != 'r');
            }
            
            if (i < 1) {
                dp[1][i] = dp[0][i];
            }
            else {
                dp[1][i] = min(dp[0][i - 1] + (leaves[i] != 'y'), dp[1][i - 1] + (leaves[i] != 'y'));
            }

            if (i < 2) {
                dp[2][i] = dp[1][i];
            }
            else {
                dp[2][i] = min(dp[1][i - 1] + (leaves[i] != 'r'), dp[2][i - 1] + (leaves[i] != 'r'));
            }
        }

        return dp[2].back();
    }


作者：ikaruga
链接：https://leetcode-cn.com/problems/UlBDOe/solution/ulbdoe-by-ikaruga/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

'''

