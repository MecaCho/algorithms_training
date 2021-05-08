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
