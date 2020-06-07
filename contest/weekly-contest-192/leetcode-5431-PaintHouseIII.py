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