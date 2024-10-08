# encoding=utf8

'''
1035. Uncrossed Lines

We write the integers of nums1 and nums2 (in the order they are given) on two separate horizontal lines.

Now, we may draw connecting lines: a straight line connecting two numbers nums1[i] and nums2[j] such that:

nums1[i] == nums2[j];
The line we draw does not intersect any other connecting (non-horizontal) line.
Note that a connecting lines cannot intersect even at the endpoints: each number can only belong to one connecting line.

Return the maximum number of connecting lines we can draw in this way.

 

Example 1:


Input: nums1 = [1,4,2], nums2 = [1,2,4]
Output: 2
Explanation: We can draw 2 uncrossed lines as in the diagram.
We cannot draw 3 uncrossed lines, because the line from nums1[1]=4 to nums2[2]=4 will intersect the line from nums1[2]=2 to nums2[1]=2.
Example 2:

Input: nums1 = [2,5,1,2,5], nums2 = [10,5,2,1,5,2]
Output: 3
Example 3:

Input: nums1 = [1,3,7,1,7,5], nums2 = [1,9,2,5,1]
Output: 2
 

Note:

1 <= nums1.length <= 500
1 <= nums2.length <= 500
1 <= nums1[i], nums2[i] <= 2000

1035. 不相交的线

在两条独立的水平线上按给定的顺序写下 nums1 和 nums2 中的整数。

现在，可以绘制一些连接两个数字 nums1[i] 和 nums2[j] 的直线，这些直线需要同时满足满足：

 nums1[i] == nums2[j]
且绘制的直线不与任何其他连线（非水平线）相交。
请注意，连线即使在端点也不能相交：每个数字只能属于一条连线。

以这种方法绘制线条，并返回可以绘制的最大连线数。

 

示例 1：


输入：nums1 = [1,4,2], nums2 = [1,2,4]
输出：2
解释：可以画出两条不交叉的线，如上图所示。 
但无法画出第三条不相交的直线，因为从 nums1[1]=4 到 nums2[2]=4 的直线将与从 nums1[2]=2 到 nums2[1]=2 的直线相交。
示例 2：

输入：nums1 = [2,5,1,2,5], nums2 = [10,5,2,1,5,2]
输出：3
示例 3：

输入：nums1 = [1,3,7,1,7,5], nums2 = [1,9,2,5,1]
输出：2
 

提示：

1 <= nums1.length <= 500
1 <= nums2.length <= 500
1 <= nums1[i], nums2[i] <= 2000
'''


class Solution(object):
    def maxUncrossedLines(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        m, n = len(nums1), len(nums2)
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

        for i in range(1, m+1):
            for j in range(1, n+1):
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
            
        # print(dp)
        return dp[-1][-1]
       
       
# golang solution

'''
func maxUncrossedLines(nums1 []int, nums2 []int) int {
	m, n := len(nums1), len(nums2)
	dp := make([][]int, m+1)
	for i := 0; i < m+1; i++ {
		dp[i] = make([]int, n+1)
	}

    max := func(a, b int) int {
		if a > b {
			return a
		}
		return b
	}

	for i := 1; i < m+1; i++ {
		for j := 1; j < n+1; j++ {
			if nums1[i-1] == nums2[j-1] {
				dp[i][j] = dp[i-1][j-1] + 1
			} else {
				dp[i][j] = max(dp[i][j-1], dp[i-1][j])
			}
		}
	}
	return dp[m][n]
}
'''

# solutions

'''
方法一：动态规划
给定两个数组 \textit{nums}_1nums 
状态转移方程：

\textit{dp}[i][j] = \begin{cases} \textit{dp}[i-1][j-1]+1, & \textit{nums}_1[i-1]=\textit{nums}_2[j-1] \\ \max(\textit{dp}[i-1][j],\textit{dp}[i][j-1]), & \textit{nums}_1[i-1] \ne \textit{nums}_2[j-1] \end{cases}
dp[i][j]={ 
dp[i−1][j−1]+1,
max(dp[i−1][j],dp[i][j−1]),

 

最终计算得到 \textit{dp}[m][n]dp[m][n] 即为数组 \textit{nums}_1nums 
1
​	
  和 \textit{nums}_2nums 
2
​	
  的最长公共子序列的长度，即可以绘制的最大连线数。



JavaC#JavaScriptGolangPython3C++C

func maxUncrossedLines(nums1, nums2 []int) int {
    m, n := len(nums1), len(nums2)
    dp := make([][]int, m+1)
    for i := range dp {
        dp[i] = make([]int, n+1)
    }
    for i, v := range nums1 {
        for j, w := range nums2 {
            if v == w {
                dp[i+1][j+1] = dp[i][j] + 1
            } else {
                dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
            }
        }
    }
    return dp[m][n]
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}
复杂度分析

时间复杂度：O(mn)O(mn)，其中 mm 和 nn 分别是数组 \textit{nums}_1nums 
1
​	
  和 \textit{nums}_2nums 
2
​	
  的长度。二维数组 \textit{dp}dp 有 m+1m+1 行和 n+1n+1 列，需要对 \textit{dp}dp 中的每个元素进行计算。

空间复杂度：O(mn)O(mn)，其中 mm 和 nn 分别是数组 \textit{nums}_1nums 
1
​	
  和 \textit{nums}_2nums 
2
​	
  的长度。创建了 m+1m+1 行 n+1n+1 列的二维数组 \textit{dp}dp。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/uncrossed-lines/solution/bu-xiang-jiao-de-xian-by-leetcode-soluti-6tqz/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''

class Solution(object):
        def maxUncrossedLines(self, nums1, nums2):
                    """
                            :type nums1: List[int]
                                    :type nums2: List[int]
                                            :rtype: int
                                                    """
                                                            m, n = len(nums1), len(nums2)
                                                                    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

                                                                            for i in range(1, m+1):
                                                                                            for j in range(1, n+1):
                                                                                                                if nums1[i-1] == nums2[j-1]:
                                                                                                                                        dp[i][j] = dp[i-1][j-1] + 1
                                                                                                                                                        else:
                                                                                                                                                                                dp[i][j] = max(dp[i][j-1], dp[i-1][j])
                                                                                                                                                                                            
                                                                                                                                                                                                    # print(dp)
                                                                                                                                                                                                            return dp[-1][-1]
