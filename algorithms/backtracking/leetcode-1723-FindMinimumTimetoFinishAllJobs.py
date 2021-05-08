# encoding=utf8

'''
1723. Find Minimum Time to Finish All Jobs

You are given an integer array jobs, where jobs[i] is the amount of time it takes to complete the ith job.

There are k workers that you can assign jobs to. Each job should be assigned to exactly one worker. The working time of a worker is the sum of the time it takes to complete all jobs assigned to them. Your goal is to devise an optimal assignment such that the maximum working time of any worker is minimized.

Return the minimum possible maximum working time of any assignment.

 

Example 1:

Input: jobs = [3,2,3], k = 3
Output: 3
Explanation: By assigning each person one job, the maximum time is 3.
Example 2:

Input: jobs = [1,2,4,7,8], k = 2
Output: 11
Explanation: Assign the jobs the following way:
Worker 1: 1, 2, 8 (working time = 1 + 2 + 8 = 11)
Worker 2: 4, 7 (working time = 4 + 7 = 11)
The maximum working time is 11.
 

Constraints:

1 <= k <= jobs.length <= 12
1 <= jobs[i] <= 107


1723. 完成所有工作的最短时间

给你一个整数数组 jobs ，其中 jobs[i] 是完成第 i 项工作要花费的时间。

请你将这些工作分配给 k 位工人。所有工作都应该分配给工人，且每项工作只能分配给一位工人。工人的 工作时间 是完成分配给他们的所有工作花费时间的总和。请你设计一套最佳的工作分配方案，使工人的 最大工作时间 得以 最小化 。

返回分配方案中尽可能 最小 的 最大工作时间 。

 

示例 1：

输入：jobs = [3,2,3], k = 3
输出：3
解释：给每位工人分配一项工作，最大工作时间是 3 。
示例 2：

输入：jobs = [1,2,4,7,8], k = 2
输出：11
解释：按下述方式分配工作：
1 号工人：1、2、8（工作时间 = 1 + 2 + 8 = 11）
2 号工人：4、7（工作时间 = 4 + 7 = 11）
最大工作时间是 11 。
 

提示：

1 <= k <= jobs.length <= 12
1 <= jobs[i] <= 107
'''


class Solution(object):
    def minimumTimeRequired(self, jobs, k):
        """
        :type jobs: List[int]
        :type k: int
        :rtype: int
        """
        self.res = float("inf")
        def assign(jobs, i, worker, max_):
            if i == len(jobs):
                self.res = min(self.res, max_)
                return
            s = set()
            for j in range(len(worker)):
                if worker[j] in s:
                    s.add(worker[j])
                    continue
                s.add(worker[j])
                if worker[j] + jobs[i] >= self.res:
                    continue
                worker[j] += jobs[i]
                assign(jobs, i+1, worker, max(worker[j], max_))
                worker[j] -= jobs[i]
        assign(jobs, 0, [0 for _ in range(k)], 0)    
        return self.res           

      
      
class Solution1(object):
    def minimumTimeRequired(self, jobs, k):
        """
        :type jobs: List[int]
        :type k: int
        :rtype: int
        """
        workers = [0]*k
        
        self.res = sys.maxsize

        def dfs(curr):
            if curr == len(jobs):
                self.res = min(self.res, max(workers))
                return
            
            seen = set()
            for i in range(k):
                if workers[i] in seen: 
                    continue 
                if workers[i] + jobs[curr] >= self.res: 
                    continue
                seen.add(workers[i])
                workers[i] += jobs[curr]
                dfs(curr+1)
                workers[i] -= jobs[curr]
        
        dfs(0)
        return self.res        
      
# golang solution

'''
import "sort"

func minimumTimeRequired(jobs []int, k int) int {
	n := len(jobs)
	sort.Sort(sort.Reverse(sort.IntSlice(jobs)))
	l, r := jobs[0], 0
	for _, v := range jobs {
		r += v
	}
	return l + sort.Search(r-l, func(limit int) bool {
		limit += l
		workloads := make([]int, k)
		var backtrack func(int) bool
		backtrack = func(idx int) bool {
			if idx == n {
				return true
			}
			cur := jobs[idx]
			for i := range workloads {
				if workloads[i]+cur <= limit {
					workloads[i] += cur
					if backtrack(idx + 1) {
						return true
					}
					workloads[i] -= cur
				}
				if workloads[i] == 0 || workloads[i]+cur == limit {
					break
				}
			}
			return false
		}
		return backtrack(0)
	})
}
'''

# solutions

'''
It is easy to get TLE, so how should we cut some branches and speed up the searching process?
We use an array of length n to record the workload assigned to each worker.

The core idea is that assume at certain point of dfs searching,
we have the following workload for 10 workers,
workers = [10, 5, 5, 5, 5, 5, 5, 5, 5, 5]

if we want to assign the current task jobs[curr] to someone,
it makes no difference if we assign it to any worker whose current workload is 5.
Therefore we can use a set named seen to store searched workload such that we only search 5 once.

There is also another branch cutting step, if the total workload is already larger than self.res,
we can exit the dfs search, too.

Another trick is to reverse sort all the jobs so that we are more likely to exit earlier.

Two other similar questions are
https://leetcode.com/problems/matchsticks-to-square/
https://leetcode.com/problems/partition-to-k-equal-sum-subsets/

this question
class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        workers = [0]*k
        
        self.res = sys.maxsize
        # jobs.sort(reverse = True)
        def dfs(curr):
            if curr == len(jobs):
                self.res = min(self.res, max(workers))
                return
            
            seen = set() # record searched workload of workers
            for i in range(k):
                if workers[i] in seen: continue # if we have searched the workload of 5, skip it.
                if workers[i] + jobs[curr] >= self.res: continue # another branch cutting
                seen.add(workers[i])
                workers[i] += jobs[curr]
                dfs(curr+1)
                workers[i] -= jobs[curr]
        
        dfs(0)
        return self.res
473. Matchsticks to Square
https://leetcode.com/problems/partition-to-k-equal-sum-subsets/

class Solution:
    def makesquare(self, nums):
        if len(nums) < 4 or sum(nums) % 4 != 0 or max(nums) > sum(nums) // 4:
            return False
        target = sum(nums)//4

        nums.sort(reverse = True)
        edge = [0]*4

        def dfs(index):
            if index == len(nums):
                return True
            seen = [] # record the searched matchstick lengths
            for i in range(4):
                if edge[i] in seen: continue
                if edge[i] + nums[index] <= target:
                    seen.append(edge[i])
                    edge[i] += nums[index]
                    if dfs(index + 1):
                        return True
                    edge[i] -= nums[index]
            return False

        return dfs(0)
698. Partition to K Equal Sum Subsets
https://leetcode.com/problems/partition-to-k-equal-sum-subsets/

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if len(nums) < k or sum(nums) % k != 0 or max(nums) > sum(nums) // k:
            return False
        target = sum(nums)//k

        nums.sort(reverse = True)
        edge = [0]*k

        def dfs(index):
            if index == len(nums):
                return True
            seen = [] # record the searched summ
            for i in range(k):
                if edge[i] in seen: continue
                if edge[i] + nums[index] <= target:
                    seen.append(edge[i])
                    edge[i] += nums[index]
                    if dfs(index + 1):
                        return True
                    edge[i] -= nums[index]
            return False

        return dfs(0)
'''


# solutions

'''
方法一：二分查找 + 回溯 + 剪枝
思路及算法

在本题中，我们很难直接计算出完成所有工作的最短时间。而注意到，当完成所有工作的最短时间已经确定为 \textit{limit}limit 时，如果存在可行的方案，那么对于任意长于 \textit{limit}limit 的最短时间，都一定也存在可行的方案。因此我们可以考虑使用二分查找的方法寻找最小的存在可行方案的 \textit{limit}limit 值。

当完成所有工作的最短时间已经确定为 \textit{limit}limit 时，我们可以利用回溯的方式来寻找方案。

一个朴素的方案是，开辟一个大小为 kk 的数组 \textit{workloads}workloads，\textit{workloads}[i]workloads[i] 表示第 ii 个工人的当前已经被分配的工作量，然后我们利用一个递归函数 \text{backtrack}(i)backtrack(i) 递归地枚举第 ii 个任务的分配方案，过程中实时地更新 \textit{workloads}workloads 数组。具体地，函数中我们检查每一个工人 jj 当前已经被分配的工作量，如果被分配的工作量 \textit{workloads}[j]workloads[j] 与当前工作的工作量 \textit{jobs}[i]jobs[i] 之和不超过 \textit{limit}limit 的限制，我们即可以将该工作分配给工人 jj，然后计算下一个工作 jobs[i+1]jobs[i+1] 的分配方案。过程中一旦我们找到了一个可行方案，我们即可以返回 \text{true}true，而无需枚举完所有的方案。

朴素的方案中，\text{backtrack}backtrack 函数的效率可能十分低下，有可能需要枚举完所有的分配方案才能得到答案，因此我们提出几个优化措施：

缩小二分查找的上下限，下限为所有工作中的最大工作量，上限为所有工作的工作量之和。
每一个工作都必须被分配，因此必然有一个工人承接了工作量最大的工作；
在最坏情况下，只有一个工人，他必须承接所有工作。
优先分配工作量大的工作。
感性地理解，如果要求将小石子和大石块放入玻璃瓶中，优先放入大石块更容易使得工作变得简单。
在搜索过程中，优先分配工作量小的工作会使得工作量大的工作更有可能最后无法被分配。
当工人 ii 还没被分配工作时，我们不给工人 i+1i+1 分配工作。
如果当前工人 ii 和 i+1i+1 都没有被分配工作，那么我们将工作先分配给任何一个人都没有区别，如果分配给工人 ii 不能成功完成分配任务，那么分配给工人 i+1i+1 也一样无法完成。
当我们将工作 ii 分配给工人 jj，使得工人 jj 的工作量恰好达到 \textit{limit}limit，且计算分配下一个工作的递归函数返回了 \text{false}false，此时即无需尝试将工作 ii 分配给其他工人，直接返回 \text{false}false 即可。
常规逻辑下，递归函数返回了 \text{false}false，那么我们需要尝试将工作 ii 分配给其他工人，假设分配给了工人 j'j 
′
 ，那么此时工人 j'j 
′
  的工作量必定不多于工人 jj 的工作量；
如果存在一个方案使得分配给工人 j'j 
′
  能够成功完成分配任务，那么此时必然有一个或一组工作 i'i 
′
  取代了工作 ii 被分配给工人 jj，否则我们可以直接将工作 ii 移交给工人 jj，仍然能成功完成分配任务。而我们知道工作 i'i 
′
  的总工作量不会超过工作 ii，因此我们可以直接交换工作 ii 与工作 i'i 
′
 ，仍然能成功完成分配任务。这与假设不符，可知不存在这样一个满足条件的工人 j'j 
′
 。
代码

C++JavaC#JavaScriptGolangC

func minimumTimeRequired(jobs []int, k int) int {
    n := len(jobs)
    sort.Sort(sort.Reverse(sort.IntSlice(jobs)))
    l, r := jobs[0], 0
    for _, v := range jobs {
        r += v
    }
    return l + sort.Search(r-l, func(limit int) bool {
        limit += l
        workloads := make([]int, k)
        var backtrack func(int) bool
        backtrack = func(idx int) bool {
            if idx == n {
                return true
            }
            cur := jobs[idx]
            for i := range workloads {
                if workloads[i]+cur <= limit {
                    workloads[i] += cur
                    if backtrack(idx + 1) {
                        return true
                    }
                    workloads[i] -= cur
                }
                // 如果当前工人未被分配工作，那么下一个工人也必然未被分配工作
                // 或者当前工作恰能使该工人的工作量达到了上限
                // 这两种情况下我们无需尝试继续分配工作
                if workloads[i] == 0 || workloads[i]+cur == limit {
                    break
                }
            }
            return false
        }
        return backtrack(0)
    })
}
复杂度分析

时间复杂度：O(n \log n + \log (S-M) \times n!)O(nlogn+log(S−M)×n!)，其中 nn 是数组 \textit{jobs}jobs 的长度，SS 是数组 \textit{jobs}jobs 的元素之和，MM 是数组 \textit{jobs}jobs 中元素的最大值。最坏情况下每次二分需要遍历所有分配方案的排列，但经过一系列优化后，实际上可以规避掉绝大部分不必要的计算。

空间复杂度：O(n)O(n)。空间复杂度主要取决于递归的栈空间的消耗，而递归至多有 nn 层。

方法二：动态规划 + 状态压缩
思路及算法

按照朴素的思路，我们按顺序给每一个工人安排工作，注意到当我们给第 ii 个工人分配工作的时候，能够选择的分配方案仅和前 i-1i−1 个人被分配的工作有关。因此我们考虑使用动态规划解决本题，只需要记录已经被分配了工作的工人数量，以及已经被分配的工作是哪些即可。

因为工作数量较少，我们可以使用状态压缩的方式来表示已经被分配的工作是哪些。具体地，假设有 nn 个工作需要被分配，我们就使用一个 nn 位的二进制整数来表示哪些工作已经被分配，哪些工作尚未被分配，如果该二进制整数的第 ii 位为 11，那么第 ii 个工作已经被分配，否则第 ii 个工作尚未被分配。如有 33 个工作需要被分配，那么 5=(101)_25=(101) 
2
​	
  即代表 第 00 和第 22 个工作已经被分配，第 11 个工作还未被分配。

这样我们可以写出状态方程：f[i][j]f[i][j] 表示给前 ii 个人分配工作，工作的分配情况为 jj 时，完成所有工作的最短时间。注意这里的 jj 是一个二进制整数，表示了工作的分配情况。实际上我们也可以将 jj 看作一个集合，包含了已经被分配的工作。

那么我们可以写出状态转移方程：

f[i][j] = \min_{j'\in j}\{ \max(f[i-1][\complement_{j}j'], \textit{sum}[j'])\}
f[i][j]= 
j 
′
 ∈j
min
​	
 {max(f[i−1][∁ 
j
​	
 j 
′
 ],sum[j 
′
 ])}

式中 \textit{sum}[j']sum[j 
′
 ] 表示集合 j'j 
′
  中的工作的总工作量，\complement_{j}j'∁ 
j
​	
 j 
′
  表示集合 jj 中子集 j'j 
′
  的补集。状态转移方程的含义为，我们枚举 jj 的每一个子集 j'j 
′
 ，让其作为分配给工人 ii 的工作，这样我们需要给前 i-1i−1 个人分配 \complement_{j}j'∁ 
j
​	
 j 
′
  的工作。

在实际代码中，我们首先预处理出 \textit{sum}sum 数组，然后初始化 f[0][j]=sum[j]f[0][j]=sum[j]，最终答案即为 f[k-1][2^n-1]f[k−1][2 
n
 −1]（表示给全部 kk 个工人分配全部 nn 个工作，完成所有工作的最短时间）。

代码

C++JavaC#JavaScriptGolangC

func minimumTimeRequired(jobs []int, k int) int {
    n := len(jobs)
    m := 1 << n
    sum := make([]int, m)
    for i := 1; i < m; i++ {
        x := bits.TrailingZeros(uint(i))
        y := i ^ 1<<x
        sum[i] = sum[y] + jobs[x]
    }

    dp := make([][]int, k)
    for i := range dp {
        dp[i] = make([]int, m)
    }
    for i, s := range sum {
        dp[0][i] = s
    }

    for i := 1; i < k; i++ {
        for j := 0; j < (1 << n); j++ {
            minn := math.MaxInt64
            for x := j; x > 0; x = (x - 1) & j {
                minn = min(minn, max(dp[i-1][j-x], sum[x]))
            }
            dp[i][j] = minn
        }
    }
    return dp[k-1][(1<<n)-1]
}

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}
复杂度分析

时间复杂度：O(n\times 3^n)O(n×3 
n
 )，其中 nn 是数组 \textit{jobs}jobs 的长度。我们需要 O(2^n)O(2 
n
 ) 的时间预处理 \textit{sum}sum 数组。动态规划中共有 O(n \times 2^n)O(n×2 
n
 ) 种状态，将每个状态看作集合，大小为 kk 的集合有 n \times C_n^kn×C 
n
k
​	
  个，其转移个数为 2^k2 
k
 ，根据二项式定理有

\sum_{k=0}^nC_n^k2^k=\sum_{k=0}^nC_n^k2^k1^{n-k}=(2+1)^n=3^n
k=0
∑
n
​	
 C 
n
k
​	
 2 
k
 = 
k=0
∑
n
​	
 C 
n
k
​	
 2 
k
 1 
n−k
 =(2+1) 
n
 =3 
n
 

因此动态规划的时间复杂度为 O(n \times 3^n)O(n×3 
n
 )，故总时间复杂度为 O(n\times 3^n)O(n×3 
n
 )。

空间复杂度：O(n\times 2^{n})O(n×2 
n
 )。我们需要保存动态规划的每一个状态。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/find-minimum-time-to-finish-all-jobs/solution/wan-cheng-suo-you-gong-zuo-de-zui-duan-s-hrhu/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
