'''
5431. 给房子涂色 III
在一个小城市里，有 m 个房子排成一排，你需要给每个房子涂上 n 种颜色之一（颜色编号为 1 到 n ）。有的房子去年夏天已经涂过颜色了，所以这些房子不需要被重新涂色。

我们将连续相同颜色尽可能多的房子称为一个街区。（比方说 houses = [1,2,2,3,3,2,1,1] ，它包含 5 个街区  [{1}, {2,2}, {3,3}, {2}, {1,1}] 。）

给你一个数组 houses ，一个 m * n 的矩阵 cost 和一个整数 target ，其中：

houses[i]：是第 i 个房子的颜色，0 表示这个房子还没有被涂色。
cost[i][j]：是将第 i 个房子涂成颜色 j+1 的花费。
请你返回房子涂色方案的最小总花费，使得每个房子都被涂色后，恰好组成 target 个街区。如果没有可用的涂色方案，请返回 -1 。



示例 1：

输入：houses = [0,0,0,0,0], cost = [[1,10],[10,1],[10,1],[1,10],[5,1]], m = 5, n = 2, target = 3
输出：9
解释：房子涂色方案为 [1,2,2,1,1]
此方案包含 target = 3 个街区，分别是 [{1}, {2,2}, {1,1}]。
涂色的总花费为 (1 + 1 + 1 + 1 + 5) = 9。
示例 2：

输入：houses = [0,2,1,2,0], cost = [[1,10],[10,1],[10,1],[1,10],[5,1]], m = 5, n = 2, target = 3
输出：11
解释：有的房子已经被涂色了，在此基础上涂色方案为 [2,2,1,2,2]
此方案包含 target = 3 个街区，分别是 [{2,2}, {1}, {2,2}]。
给第一个和最后一个房子涂色的花费为 (10 + 1) = 11。
示例 3：

输入：houses = [0,0,0,0,0], cost = [[1,10],[10,1],[1,10],[10,1],[1,10]], m = 5, n = 2, target = 5
输出：5
示例 4：

输入：houses = [3,1,2,3], cost = [[1,1,1],[1,1,1],[1,1,1],[1,1,1]], m = 4, n = 3, target = 3
输出：-1
解释：房子已经被涂色并组成了 4 个街区，分别是 [{3},{1},{2},{3}] ，无法形成 target = 3 个街区。


提示：

m == houses.length == cost.length
n == cost[i].length
1 <= m <= 100
1 <= n <= 20
1 <= target <= m
0 <= houses[i] <= n
1 <= cost[i][j] <= 10^4


5431. Paint House III
There is a row of m houses in a small city, each house must be painted with one of the n colors (labeled from 1 to n), some houses that has been painted last summer should not be painted again.

A neighborhood is a maximal group of continuous houses that are painted with the same color. (For example: houses = [1,2,2,3,3,2,1,1] contains 5 neighborhoods  [{1}, {2,2}, {3,3}, {2}, {1,1}]).

Given an array houses, an m * n matrix cost and an integer target where:

houses[i]: is the color of the house i, 0 if the house is not painted yet.
cost[i][j]: is the cost of paint the house i with the color j+1.
Return the minimum cost of painting all the remaining houses in such a way that there are exactly target neighborhoods, if not possible return -1.



Example 1:

Input: houses = [0,0,0,0,0], cost = [[1,10],[10,1],[10,1],[1,10],[5,1]], m = 5, n = 2, target = 3
Output: 9
Explanation: Paint houses of this way [1,2,2,1,1]
This array contains target = 3 neighborhoods, [{1}, {2,2}, {1,1}].
Cost of paint all houses (1 + 1 + 1 + 1 + 5) = 9.
Example 2:

Input: houses = [0,2,1,2,0], cost = [[1,10],[10,1],[10,1],[1,10],[5,1]], m = 5, n = 2, target = 3
Output: 11
Explanation: Some houses are already painted, Paint the houses of this way [2,2,1,2,2]
This array contains target = 3 neighborhoods, [{2,2}, {1}, {2,2}].
Cost of paint the first and last house (10 + 1) = 11.
Example 3:

Input: houses = [0,0,0,0,0], cost = [[1,10],[10,1],[1,10],[10,1],[1,10]], m = 5, n = 2, target = 5
Output: 5
Example 4:

Input: houses = [3,1,2,3], cost = [[1,1,1],[1,1,1],[1,1,1],[1,1,1]], m = 4, n = 3, target = 3
Output: -1
Explanation: Houses are already painted with a total of 4 neighborhoods [{3},{1},{2},{3}] different of target = 3.


Constraints:

m == houses.length == cost.length
n == cost[i].length
1 <= m <= 100
1 <= n <= 20
1 <= target <= m
0 <= houses[i] <= n
1 <= cost[i][j] <= 10^4
'''


class Solution(object):
    def minCost(self, houses, cost, m, n, target):
        """
        :type houses: List[int]
        :type cost: List[List[int]]
        :type m: int
        :type n: int
        :type target: int
        :rtype: int
        """
        if len(set(houses)) > target:
            return -1
        dp = [[[float("inf") for _ in range(target)] for _ in range(n)] for _ in range(m)]
        for k in range(n):
            if houses[0] == 0:
                dp[0][k][0] = cost[0][k]
        if houses[0] != 0:
            dp[0][houses[0 ] -1][0] = 0

        for i in range(1, m):
            for j in range(n):
                for k in range(target):
                    if houses[i] != 0 and houses[i] - 1 != j:
                        break
                    tmp = []
                    for kk in range(n):
                        if kk != j and k - 1 < target and k > 0:
                            tmp.append(dp[ i -1][kk][ k -1])
                    tmp.append(dp[ i -1][j][k])
                    cur_cost = cost[i][j]
                    if houses[i] != 0:
                        cur_cost = 0
                    dp[i][j][k] = min(tmp) + cur_cost

        res = float("inf")
        for i in range(n):
            res = min(res, dp[ m -1][i][target -1])
        return res if res != float("inf") else -1

# golang

'''
func minCost(houses []int, cost [][]int, m int, n int, target int) int {
	dp := [][][]int{}
	for i:= 0; i < m; i++{
		dp = append(dp, [][]int{})
		for j:= 0; j < n; j++{

			dp[i] = append(dp[i], []int{})

			for k := 0; k < target; k++{
				dp[i][j] = append(dp[i][j], math.MaxInt64)
			}
		}
	}

    for j := 0; j < n; j++{
        if houses[0] == 0{
            dp[0][j][0] = cost[0][j]
        }else{
            dp[0][houses[0]-1][0] = 0
        }
    }
	
	for i := 1; i < m; i++{
		for j:= 0; j < n; j++{
			for k:= 0; k < target;k++{
				if houses[i] != 0 && houses[i] - 1 != j{
					break
				}
				minVal := dp[i-1][j][k]
				for kk := 0; kk < n; kk++{
					if kk != j && k > 0 && k-1 < target{
						if dp[i-1][kk][k-1] < minVal{
							minVal = dp[i-1][kk][k-1]
						}
					}
				}
				curCost := cost[i][j]
				if houses[i] != 0{
					curCost = 0
				}
                if minVal != math.MaxInt64{
                    dp[i][j][k] = minVal + curCost
                }
				
			}
		}
	}
	
	res := -1
	for i := 0; i < n; i++{
		if res == -1 || dp[m-1][i][target-1] < res{
			res = dp[m-1][i][target-1]
		}
	}
    
    if res >= math.MaxInt64{
		return -1
	}
	
	return res
}
'''

# tips

'''
Use Dynamic programming.

Define dp[i][j][k] as the minimum cost where we have k neighborhoods in the first i houses and the i-th house is painted with the color j.
'''


# solutions

'''
前言
为了叙述方便，我们令所有的变量都从 00 开始编号，即：

房子的编号为 [0, m-1][0,m−1]；
颜色的编号为 [0, n-1][0,n−1]，如果房子没有涂上颜色，那么记为 -1−1；
街区的编号为 [0, \textit{target}-1][0,target−1]。
方法一：动态规划
思路与算法

我们可以使用动态规划解决本题。

设 \textit{dp}(i,j,k)dp(i,j,k) 表示将 [0, i][0,i] 的房子都涂上颜色，最末尾的第 ii 个房子的颜色为 jj，并且它属于第 kk 个街区时，需要的最少花费。

在进行状态转移时，我们需要考虑「第 i-1i−1 个房子的颜色」，这关系到「花费」以及「街区数量」的计算，因此我们还需要对其进行枚举。

设第 i-1i−1 个房子的颜色为 j_0j 
0
​	
 ，我们可以分类讨论出不同情况下的状态转移方程：

如果 \textit{houses}[i] \neq -1houses[i] 

​	
 =−1，说明第 ii 个房子已经涂过颜色了。由于我们不能重复涂色，那么必须有 \textit{houses}[i] = jhouses[i]=j。我们可以写出在 \textit{houses}[i] \neq jhouses[i] 

​	
 =j 时的状态转移方程：

\textit{dp}(i, j, k) = \infty, \quad 如果~\textit{houses}[i] \neq -1~并且~\textit{houses}[i] \neq j
dp(i,j,k)=∞,如果 houses[i] 

​	
 =−1 并且 houses[i] 

​	
 =j

这里我们用极大值 \infty∞ 表示不满足要求的状态，由于我们需要求出的是最少花费，因此极大值不会对状态转移产生影响。

当 \textit{houses}[i] = jhouses[i]=j 时，如果 j=j_0j=j 
0
​	
 ，那么第 i-1i−1 个房子和第 ii 个房子属于同一个街区，状态转移方程为：

\textit{dp}(i, j, k) = \textit{dp}(i-1, j, k), \quad 如果~ \textit{houses}[i] = j
dp(i,j,k)=dp(i−1,j,k),如果 houses[i]=j

如果 j \neq j_0j 

​	
 =j 
0
​	
 ，那么它们属于不同的街区，状态转移方程为：

\textit{dp}(i, j, k) = \min_{j_0 \neq j} \textit{dp}(i-1,j_0, k-1), \quad 如果~ \textit{houses}[i] = j
dp(i,j,k)= 
j 
0
​	
  

​	
 =j
min
​	
 dp(i−1,j 
0
​	
 ,k−1),如果 houses[i]=j

如果 \textit{houses}[i] = -1houses[i]=−1，说明我们需要将第 ii 个房子涂成颜色 jj，花费为 \textit{cost}[i][j]cost[i][j]。

此外的状态转移与上一类情况类似。如果 j = j_0j=j 
0
​	
 ，那么状态转移方程为：

\textit{dp}(i, j, k) = \textit{dp}(i-1, j, k) + \textit{cost}[i][j], \quad 如果~\textit{houses}[i]=-1
dp(i,j,k)=dp(i−1,j,k)+cost[i][j],如果 houses[i]=−1

如果 j \neq j_0j 

​	
 =j 
0
​	
 ，那么状态转移方程为：

\textit{dp}(i, j, k) = \min_{j_0 \neq j} \textit{dp}(i-1,j_0, k-1) + \textit{cost}[i][j], \quad 如果~\textit{houses}[i]=-1
dp(i,j,k)= 
j 
0
​	
  

​	
 =j
min
​	
 dp(i−1,j 
0
​	
 ,k−1)+cost[i][j],如果 houses[i]=−1

最终的答案即为 \min\limits_{j} \textit{dp}(m-1, j, \textit{target} - 1) 
j
min
​	
 dp(m−1,j,target−1)。

细节

以下的细节有助于写出更简洁的代码：

我们可以将所有的状态初始化为 \infty∞。在进行状态转移时，我们是选择转移中的最小值，因此 \infty∞ 不会产生影响；

两类情况下的状态转移方程十分类似，因此我们可以先不去管 \textit{cost}[i][j]cost[i][j] 的部分，在求出 \textit{dp}(i, j, k)dp(i,j,k) 的最小值之后，如果发现 \textit{houses}[i]=-1houses[i]=−1，再加上 \textit{cost}[i][j]cost[i][j] 即可；

当 k=0k=0 时，不能从包含 k-1k−1 的状态转移而来；

当 i=0i=0 时，第 00 个房子之前没有房子，因此 kk 也必须为 00。此时状态转移方程为：

\textit{dp}(0, j, 0) = \left\{ \begin{aligned} & \infty, && 如果~\textit{houses}[i] \neq -1 ~并且~\textit{houses}[i] \neq j \\ & 0, && 如果~\textit{houses}[i] \neq -1 ~并且~\textit{houses}[i] = j \\ & \textit{cost}[i][j], && 如果~\textit{houses}[i]=-1 \end{aligned} \right.
dp(0,j,0)= 
⎩
⎪
⎪
⎨
⎪
⎪
⎧
​	
  
​	
  
∞,
0,
cost[i][j],
​	
  
​	
  
如果 houses[i] 

​	
 =−1 并且 houses[i] 

​	
 =j
如果 houses[i] 

​	
 =−1 并且 houses[i]=j
如果 houses[i]=−1
​	
 

当 i=0i=0 且 k \neq 0k 

​	
 =0 时，\textit{dp}(0, j, k) = \inftydp(0,j,k)=∞。

代码

C++JavaC#Python3JavaScriptGolangC

class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        # 将颜色调整为从 0 开始编号，没有被涂色标记为 -1
        houses = [c - 1 for c in houses]

        # dp 所有元素初始化为极大值
        dp = [[[float("inf")] * target for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if houses[i] != -1 and houses[i] != j:
                    continue
                
                for k in range(target):
                    for j0 in range(n):
                        if j == j0:
                            if i == 0:
                                if k == 0:
                                    dp[i][j][k] = 0
                            else:
                                dp[i][j][k] = min(dp[i][j][k], dp[i - 1][j][k])
                        elif i > 0 and k > 0:
                            dp[i][j][k] = min(dp[i][j][k], dp[i - 1][j0][k - 1])

                    if dp[i][j][k] != float("inf") and houses[i] == -1:
                        dp[i][j][k] += cost[i][j]

        ans = min(dp[m - 1][j][target - 1] for j in range(n))
        return -1 if ans == float("inf") else ans
复杂度分析

时间复杂度：O(m\cdot n^2\cdot \textit{target})O(m⋅n 
2
 ⋅target)。状态的数量为 O(m\cdot n\cdot \textit{target})O(m⋅n⋅target)，每个状态需要 O(n)O(n) 的时间枚举 j_0j 
0
​	
 ，因此总时间复杂度为 O(m\cdot n^2\cdot \textit{target})O(m⋅n 
2
 ⋅target)。

空间复杂度：O(m \cdot n \cdot \textit{target})O(m⋅n⋅target)，即为状态的数量。

注意到 \textit{dp}(i,j,k)dp(i,j,k) 只会从 \textit{dp}(i-1, \cdots, \cdots)dp(i−1,⋯,⋯) 转移而来，因此我们可以使用滚动数组对空间复杂度进行优化，即使用两个大小为 n \cdot \textit{target}n⋅target 的数组 \textit{dp}_1dp 
1
​	
 , \textit{dp}_2dp 
2
​	
 ，将 dp(0,j,k)dp(0,j,k) 的值存储在 \textit{dp}_1dp 
1
​	
  中，将 dp(1,j,k)dp(1,j,k) 的值存储在 \textit{dp}_2dp 
2
​	
  中，将 dp(2,j,k)dp(2,j,k) 的值存储在 \textit{dp}_1dp 
1
​	
  中，将 dp(3,j,k)dp(3,j,k) 的值存储在 \textit{dp}_2dp 
2
​	
  中，以此类推。这样优化后的空间复杂度为 O(n\cdot \textit{target})O(n⋅target)。

方法二：动态规划 + 优化
思路与算法

在方法一中，我们分类讨论出了五种不同的状态转移方程，其中有三种是可以在 O(1)O(1) 的时间进行状态转移的，而剩余的两种需要枚举 j_0j 
0
​	
 ，只能在 O(n)O(n) 的时间进行转移，即：

\textit{dp}(i, j, k) = \min_{j_0 \neq j} \textit{dp}(i-1,j_0, k-1), \quad 如果~ \textit{houses}[i] = j
dp(i,j,k)= 
j 
0
​	
  

​	
 =j
min
​	
 dp(i−1,j 
0
​	
 ,k−1),如果 houses[i]=j

以及：

\textit{dp}(i, j, k) = \min_{j_0 \neq j} \textit{dp}(i-1,j_0, k-1) + \textit{cost}[i][j], \quad 如果~\textit{houses}[i]=-1
dp(i,j,k)= 
j 
0
​	
  

​	
 =j
min
​	
 dp(i−1,j 
0
​	
 ,k−1)+cost[i][j],如果 houses[i]=−1

如果我们能将它们优化至 O(1)O(1)，那么整个动态规划的时间复杂度也可以从 O(m\cdot n^2\cdot \textit{target})O(m⋅n 
2
 ⋅target) 优化至 O(m \cdot n \cdot \textit{target})O(m⋅n⋅target)。

我们可以令 \textit{best}(i, k) = (\textit{first}, \textit{first\_idx}, \textit{second})best(i,k)=(first,first_idx,second)，表示所有的状态 dp(i, j, k)dp(i,j,k) 中的最小值为 \textit{first}first，取到最小值对应的 jj 值为 \textit{first\_idx}first_idx，次小值为 \textit{second}second。这里 jj 可以在 [0, n)[0,n) 中任意选择，但我们只记录最大值和次大值，以及最大值对应的 jj。

这样做的好处在于我们可以快速地求出原先需要 O(n)O(n) 的时间才能求出的：

\min_{j_0 \neq j} \textit{dp}(i-1,j_0, k-1)
j 
0
​	
  

​	
 =j
min
​	
 dp(i−1,j 
0
​	
 ,k−1)

这一项。即：

我们取出 \textit{best}(i - 1, k - 1)best(i−1,k−1)，它包含的三个值为 (\textit{first}, \textit{first\_idx}, \textit{second})(first,first_idx,second)；

如果 j = \textit{first\_idx}j=first_idx，那么 \textit{dp}(i, j, k) = \textit{second}dp(i,j,k)=second；

如果 j \neq \textit{first\_idx}j 

​	
 =first_idx，那么 \textit{dp}(i, j, k) = \textit{first}dp(i,j,k)=first。

这样做的正确性通过 \min\limits_{j_0 \neq j} \textit{dp}(i-1,j_0, k-1) 
j 
0
​	
  

​	
 =j
min
​	
 dp(i−1,j 
0
​	
 ,k−1) 本身的定义就能体现。

那么如何求出 \textit{best}(i, k)best(i,k) 呢？我们可以给每一个 \textit{best}(i, k)best(i,k) 赋予初始值 (\infty, -1, \infty)(∞,−1,∞)，每次我们计算出 \textit{dp}(i, j, k)dp(i,j,k) 时，使用其更新 \textit{best}(i, k)best(i,k) 即可。

代码

方法二的代码较为复杂，主要的原因在于我们需要将方法一中的 O(n)O(n) 枚举 j_0j 
0
​	
  的循环删除，并且需要保持方法一中的边界条件不变。

C++JavaC#Python3GolangCJavaScript

class Entry:
    def __init__(self):
        self.first = float("inf")
        self.first_idx = -1
        self.second = float("inf")

class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        # 将颜色调整为从 0 开始编号，没有被涂色标记为 -1
        houses = [c - 1 for c in houses]

        # dp 所有元素初始化为极大值
        dp = [[[float("inf")] * target for _ in range(n)] for _ in range(m)]
        best = [[Entry() for _ in range(target)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if houses[i] != -1 and houses[i] != j:
                    continue
                
                for k in range(target):
                    if i == 0:
                        if k == 0:
                            dp[i][j][k] = 0
                    else:
                        dp[i][j][k] = dp[i - 1][j][k]
                        if k > 0:
                            # 使用 best(i-1,k-1) 直接得到 dp(i,j,k) 的值
                            info = best[i - 1][k - 1]
                            dp[i][j][k] = min(dp[i][j][k], (info.second if j == info.first_idx else info.first))

                    if dp[i][j][k] != float("inf") and houses[i] == -1:
                        dp[i][j][k] += cost[i][j]
                    
                    # 用 dp(i,j,k) 更新 best(i,k)
                    info = best[i][k]
                    if dp[i][j][k] < info.first:
                        info.second = info.first
                        info.first = dp[i][j][k]
                        info.first_idx = j
                    elif dp[i][j][k] < info.second:
                        info.second = dp[i][j][k]

        ans = min(dp[m - 1][j][target - 1] for j in range(n))
        return -1 if ans == float("inf") else ans
复杂度分析

时间复杂度：O(m\cdot n\cdot \textit{target})O(m⋅n⋅target)。状态的数量为 O(m\cdot n\cdot \textit{target})O(m⋅n⋅target)，每个状态只需要 O(1)O(1) 的时间进行计算，同时需要 O(1)O(1) 的时间来更新 \textit{best}best，因此总时间复杂度为 O(m\cdot n\cdot \textit{target})O(m⋅n⋅target)。

空间复杂度：O(m\cdot n \cdot \textit{target})O(m⋅n⋅target)，即为状态的数量。除此之外，我们需要 O(m \cdot \textit{target})O(m⋅target) 的空间存储 \textit{best}best，但其在渐进意义下小于前者，因此可以忽略。

与方法一相同，我们也可以将空间复杂度优化至 O(n\cdot \textit{target})O(n⋅target)。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/paint-house-iii/solution/fen-shua-fang-zi-iii-by-leetcode-solutio-powb/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
