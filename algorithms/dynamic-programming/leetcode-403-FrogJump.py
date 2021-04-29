# encoding=utf8

'''
403. Frog Jump

A frog is crossing a river. The river is divided into some number of units, and at each unit, there may or may not exist a stone. The frog can jump on a stone, but it must not jump into the water.

Given a list of stones' positions (in units) in sorted ascending order, determine if the frog can cross the river by landing on the last stone. Initially, the frog is on the first stone and assumes the first jump must be 1 unit.

If the frog's last jump was k units, its next jump must be either k - 1, k, or k + 1 units. The frog can only jump in the forward direction.

 

Example 1:

Input: stones = [0,1,3,5,6,8,12,17]
Output: true
Explanation: The frog can jump to the last stone by jumping 1 unit to the 2nd stone, then 2 units to the 3rd stone, then 2 units to the 4th stone, then 3 units to the 6th stone, 4 units to the 7th stone, and 5 units to the 8th stone.
Example 2:

Input: stones = [0,1,2,3,4,8,9,11]
Output: false
Explanation: There is no way to jump to the last stone as the gap between the 5th and 6th stone is too large.
 

Constraints:

2 <= stones.length <= 2000
0 <= stones[i] <= 231 - 1
stones[0] == 0

403. 青蛙过河
难度
困难

258





一只青蛙想要过河。 假定河流被等分为若干个单元格，并且在每一个单元格内都有可能放有一块石子（也有可能没有）。 青蛙可以跳上石子，但是不可以跳入水中。

给你石子的位置列表 stones（用单元格序号 升序 表示）， 请判定青蛙能否成功过河（即能否在最后一步跳至最后一块石子上）。

开始时， 青蛙默认已站在第一块石子上，并可以假定它第一步只能跳跃一个单位（即只能从单元格 1 跳至单元格 2 ）。

如果青蛙上一步跳跃了 k 个单位，那么它接下来的跳跃距离只能选择为 k - 1、k 或 k + 1 个单位。 另请注意，青蛙只能向前方（终点的方向）跳跃。

 

示例 1：

输入：stones = [0,1,3,5,6,8,12,17]
输出：true
解释：青蛙可以成功过河，按照如下方案跳跃：跳 1 个单位到第 2 块石子, 然后跳 2 个单位到第 3 块石子, 接着 跳 2 个单位到第 4 块石子, 然后跳 3 个单位到第 6 块石子, 跳 4 个单位到第 7 块石子, 最后，跳 5 个单位到第 8 个石子（即最后一块石子）。
示例 2：

输入：stones = [0,1,2,3,4,8,9,11]
输出：false
解释：这是因为第 5 和第 6 个石子之间的间距太大，没有可选的方案供青蛙跳跃过去。
 

提示：

2 <= stones.length <= 2000
0 <= stones[i] <= 231 - 1
stones[0] == 0
'''


class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        length = len(stones)
        dp = [[0 for i in range(length+1)] for _ in range(length)]
        dp[0][0] = 1
        if length < 2 or stones[1] != 1:
            return False

        for i in range(length):
            for j in range(i):
                k = stones[i] - stones[j]
                if k <= j + 1:
                    dp[i][k] = dp[j][k-1] or dp[j][k] or dp[j][k+1]
                    if i == length-1 and dp[i][k]:
                        return True
        return False


# solutions

'''
方法一：记忆化搜索 + 二分查找
思路及算法

最直接的想法是使用深度优先搜索的方式尝试所有跳跃方案，直到我们找到一组可行解为止。但是不加优化的该算法的时间复杂度在最坏情况下是指数级的，因此考虑优化。

注意到当青蛙每次能够跳跃的距离仅取决于青蛙的「上一次跳跃距离」。而青蛙此后能否到达终点，只和它「现在所处的石子编号」以及「上一次跳跃距离」有关。因此我们可以将这两个维度综合记录为一个状态。使用记忆化搜索的方式优化时间复杂度。

具体地，当青蛙位于第 ii 个石子，上次跳跃距离为 \textit{lastDis}lastDis 时，它当前能够跳跃的距离范围为 [\textit{lastDis}-1,\textit{lastDis}+1][lastDis−1,lastDis+1]。我们需要分别判断这三个距离对应的三个位置是否存在石子。注意到给定的石子列表为升序，所以我们可以利用二分查找来优化查找石子的时间复杂度。每次我们找到了符合要求的位置，我们就尝试进行一次递归搜索即可。

为了优化编码，我们可以认为青蛙的初始状态为：「现在所处的石子编号」为 00（石子从 00 开始编号），「上一次跳跃距离」为 00（这样可以保证青蛙的第一次跳跃距离为 11）。

代码

C++JavaJavaScriptGolangC

func canCross(stones []int) bool {
    n := len(stones)
    dp := make([]map[int]bool, n-1)
    for i := range dp {
        dp[i] = map[int]bool{}
    }
    var dfs func(int, int) bool
    dfs = func(i, lastDis int) (res bool) {
        if i == n-1 {
            return true
        }
        if res, has := dp[i][lastDis]; has {
            return res
        }
        defer func() { dp[i][lastDis] = res }()
        for curDis := lastDis - 1; curDis <= lastDis+1; curDis++ {
            if curDis > 0 {
                j := sort.SearchInts(stones, curDis+stones[i])
                if j != n && stones[j] == curDis+stones[i] && dfs(j, curDis) {
                    return true
                }
            }
        }
        return false
    }
    return dfs(0, 0)
}
复杂度分析

时间复杂度：O(n^2\log n)O(n 
2
 logn)，其中 nn 是石子的数量。因为青蛙仅能在石子间跳跃，且不能向后方（起点的方向）跳跃，而第 ii 个石子后方只有 i-1i−1 个石子，因此在任意位置，青蛙的「上一次跳跃距离」至多只有 O(n)O(n) 种，状态总数为 O(n^2)O(n 
2
 )。最坏情况下我们要遍历每一个状态，每次我们需要 O(\log n)O(logn) 的时间查找指定位置的石子是否存在，相乘即可得到最终时间复杂度。

空间复杂度：O(n^2)O(n 
2
 )，其中 nn 是石子的数量。最坏情况下我们需要记录全部 O(n^2)O(n 
2
 ) 个状态。

方法二：动态规划
思路及算法

我们也可以使用动态规划的方法，令 \textit{dp}[i][k]dp[i][k] 表示青蛙能否达到「现在所处的石子编号」为 ii 且「上一次跳跃距离」为 kk 的状态。

这样我们可以写出状态转移方程：

\textit{dp}[i][k] = \textit{dp}[j][k - 1] \bigvee \textit{dp}[j][k] \bigvee \textit{dp}[j][k + 1]
dp[i][k]=dp[j][k−1]⋁dp[j][k]⋁dp[j][k+1]

式中 jj 代表了青蛙的「上一次所在的石子编号」，满足 stones[i] - stones[j] = kstones[i]−stones[j]=k。

和方法一相同，状态转移的初始条件为 \textit{dp}[0][0] = \text{true}dp[0][0]=true，表示：「现在所处的石子编号」为 00（石子从 00 开始编号），「上一次跳跃距离」为 00（这样可以保证青蛙的第一次跳跃距离为 11）。当我们找到一个 \textit{dp}[n-1][k]dp[n−1][k] 为真时，我们就知道青蛙可以到达终点（第 n-1n−1 个石子）。

具体地，对于第 ii 个石子，我们首先枚举所有的 jj（即上一次所在的石子编号），那么「上一次跳跃距离」kk 即为 stones[i] - stones[j]stones[i]−stones[j]。如果在第 jj 个石子上，青蛙的「上一次跳跃距离」可以为 k-1,k,k+1k−1,k,k+1 三者之一，那么我们此时的方案即为合法方案。因此我们只需要检查 \textit{dp}[j][k - 1], \textit{dp}[j][k], \textit{dp}[j][k + 1]dp[j][k−1],dp[j][k],dp[j][k+1] 是否有至少一个为真即可。

优化

为了优化程序运行速度，我们还将推出两个结论，并做出优化：

「现在所处的石子编号」为 ii 时，「上一次跳跃距离」kk 必定满足 k \leq ik≤i。
当青蛙位于第 00 个石子上时，青蛙的上一次跳跃距离限定为 00，之后每次跳跃，青蛙所在的石子编号至少增加 11，而每次跳跃距离至多增加 11。
跳跃 mm 次后，青蛙「现在所处的石子编号」i \geq mi≥m，「上一次跳跃距离」k \leq mk≤m，因此 k\leq ik≤i。
这样我们可以将状态数约束在 O(n^2)O(n 
2
 )。
我们可以从后向前枚举「上一次所在的石子编号」jj，当「上一次跳跃距离」kk 超过了 j+1j+1 时，我们即可以停止跳跃，因为在第 jj 个石子上我们至多只能跳出 j+1j+1 的距离。
当第 ii 个石子与第 i-1i−1 个石子距离超过 ii 时，青蛙必定无法到达终点。
由结论 11 可知，当青蛙到达第 i-1i−1 个石子时，它的「上一次跳跃距离」至多为 i-1i−1，因此青蛙在第 ii 个石子上最远只能跳出 ii 的距离。
而距离第 i-1i−1 个石子最近的石子即为第 ii 个石子，它们的距离超过了青蛙当前能跳出的最远距离，因此青蛙无路可跳。
因此我们可以提前检查是否有相邻的石子不满足条件，如果有，我们可以提前返回 \text{false}false。
代码

C++JavaGolangC

func canCross(stones []int) bool {
    n := len(stones)
    dp := make([][]bool, n)
    for i := range dp {
        dp[i] = make([]bool, n)
    }
    dp[0][0] = true
    for i := 1; i < n; i++ {
        if stones[i]-stones[i-1] > i {
            return false
        }
    }
    for i := 1; i < n; i++ {
        for j := i - 1; j >= 0; j-- {
            k := stones[i] - stones[j]
            if k > j+1 {
                break
            }
            dp[i][k] = dp[j][k-1] || dp[j][k] || dp[j][k+1]
            if i == n-1 && dp[i][k] {
                return true
            }
        }
    }
    return false
}
JavaScript

var canCross = function(stones) {
    const n = stones.length;
    const dp = new Array(n).fill(0).map(() => new Array(n).fill(0));
    dp[0][0] = true;
    for (let i = 1; i < n; ++i) {
        if (stones[i] - stones[i - 1] > i) {
            return false;
        }
    }
    for (let i = 1; i < n; ++i) {
        for (let j = i - 1; j >= 0; --j) {
            const k = stones[i] - stones[j];
            if (k > j + 1) {
                break;
            }
            dp[i][k] = dp[j][k - 1] || dp[j][k] || dp[j][k + 1];
            if (i === n - 1 && dp[i][k]) {
                return true;
            }
        }
    }
    return false;
};
复杂度分析

时间复杂度：O(n^2)O(n 
2
 )，其中 nn 是石子的数量。因为青蛙仅能在石子间跳跃，且不能向后方（起点的方向）跳跃，而第 ii 个石子后方只有 i-1i−1 个石子，因此在任意位置，青蛙的「上一次跳跃距离」至多只有 nn 种，状态总数为 n^2n 
2
 。最坏情况下我们要遍历每一个状态，每次我们只需要 O(1)O(1) 的时间计算当前状态是否可达，相乘即可得到最终时间复杂度。

空间复杂度：O(n^2)O(n 
2
 )，其中 nn 是石子的数量。我们需要记录全部 n^2n 
2
  个状态。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/frog-jump/solution/qing-wa-guo-he-by-leetcode-solution-mbuo/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''

