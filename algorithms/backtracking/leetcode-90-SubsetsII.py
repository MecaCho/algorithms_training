# encoding=utf8

'''
90. Subsets II

Given an integer array nums that may contain duplicates, return all possible 
subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
 

Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10

90. 子集 II
给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。

示例:

输入: [1,2,2]
输出:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]

90. Subsets II
Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
'''


class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        self.vals = []
        nums = sorted(nums)
        def backtrack(pre, new_c, k):
            if k > len(nums):
                return
            if len(new_c) == k:
                if new_c not in self.vals:
                    self.vals.append(new_c)
            for i in range(pre, len(nums)):
                backtrack(i+1, [nums[i]] + new_c, k+1)
        backtrack(0, [], 0)
        return self.vals


class Solution1(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        self.vals = []
        nums.sort()

        def bk(res, start):
            self.vals.append(res)

            pre = None
            for i in range(start, len(nums)):
                if pre is None or pre != nums[i]:
                    bk(res + [nums[i]], i + 1)
                pre = nums[i]
        bk([], 0)
        return self.vals


class Solution2(object):
    def subsetsWithDup(self, nums):
        self.vals = []
        nums.sort()

        def bk(res, start):
            self.vals.append(res)

            for i in range(start, len(nums)):
                if i == start or nums[i - 1] != nums[i]:
                    bk(res + [nums[i]], i + 1)

        bk([], 0)

        return self.vals



class Solution20210331(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.vals = []

        n = len(nums)
        nums.sort()
        def bk(start, tmp):
            self.vals.append(tmp)
            pre = None
            for i in range(start, n):
                if not pre or nums[i] != pre:
                    bk(i + 1, tmp + [nums[i]])
                    pre = nums[i]

        bk(0, [])
        return self.vals


if __name__ == '__main__':
    demo = Solution1()
    res = demo.subsetsWithDup([1,1,2,3])
    print(res)


# solutions

'''
前言
本题解基于「78. 子集的官方题解」，请读者在充分理解该题解后继续阅读。

方法一：迭代法实现子集枚举
思路

考虑数组 [1,2,2][1,2,2]，选择前两个数，或者第一、三个数，都会得到相同的子集。

也就是说，对于当前选择的数 xx，若前面有与其相同的数 yy，且没有选择 yy，此时包含 xx 的子集，必然会出现在包含 yy 的所有子集中。

我们可以通过判断这种情况，来避免生成重复的子集。代码实现时，可以先将数组排序；迭代时，若发现没有选择上一个数，且当前数字与上一个数相同，则可以跳过当前生成的子集。

代码

C++JavaGolangJavaScriptC

func subsetsWithDup(nums []int) (ans [][]int) {
    sort.Ints(nums)
    n := len(nums)
outer:
    for mask := 0; mask < 1<<n; mask++ {
        t := []int{}
        for i, v := range nums {
            if mask>>i&1 > 0 {
                if i > 0 && mask>>(i-1)&1 == 0 && v == nums[i-1] {
                    continue outer
                }
                t = append(t, v)
            }
        }
        ans = append(ans, append([]int(nil), t...))
    }
    return
}
复杂度分析

时间复杂度：O(n \times 2^n)O(n×2 
n
 )，其中 nn 是数组 \textit{nums}nums 的长度。排序的时间复杂度为 O(n \log n)O(nlogn)。一共 2^n2 
n
  个状态，每种状态需要 O(n)O(n) 的时间来构造子集，一共需要 O(n \times 2^n)O(n×2 
n
 ) 的时间来构造子集。由于在渐进意义上 O(n \log n)O(nlogn) 小于 O(n \times 2^n)O(n×2 
n
 )，故总的时间复杂度为 O(n \times 2^n)O(n×2 
n
 )。

空间复杂度：O(n)O(n)。即构造子集使用的临时数组 tt 的空间代价。

方法二：递归法实现子集枚举
思路

与方法一类似，在递归时，若发现没有选择上一个数，且当前数字与上一个数相同，则可以跳过当前生成的子集。

代码

C++JavaGolangJavaScript

func subsetsWithDup(nums []int) (ans [][]int) {
    sort.Ints(nums)
    t := []int{}
    var dfs func(bool, int)
    dfs = func(choosePre bool, cur int) {
        if cur == len(nums) {
            ans = append(ans, append([]int(nil), t...))
            return
        }
        dfs(false, cur+1)
        if !choosePre && cur > 0 && nums[cur-1] == nums[cur] {
            return
        }
        t = append(t, nums[cur])
        dfs(true, cur+1)
        t = t[:len(t)-1]
    }
    dfs(false, 0)
    return
}
C

int cmp(int* a, int* b) {
    return *a - *b;
}

int* t;
int tSize;

void dfs(bool choosePre, int cur, int* nums, int numSize, int** ret, int* returnSize, int** returnColumnSizes) {
    if (cur == numSize) {
        int* tmp = malloc(sizeof(int) * tSize);
        memcpy(tmp, t, sizeof(int) * tSize);
        ret[*returnSize] = tmp;
        (*returnColumnSizes)[(*returnSize)++] = tSize;
        return;
    }
    dfs(false, cur + 1, nums, numSize, ret, returnSize, returnColumnSizes);
    if (!choosePre && cur > 0 && nums[cur - 1] == nums[cur]) {
        return;
    }
    t[tSize++] = nums[cur];
    dfs(true, cur + 1, nums, numSize, ret, returnSize, returnColumnSizes);
    tSize--;
}

int** subsetsWithDup(int* nums, int numsSize, int* returnSize, int** returnColumnSizes) {
    qsort(nums, numsSize, sizeof(int), cmp);
    int n = numsSize;
    *returnSize = 0;
    *returnColumnSizes = malloc(sizeof(int) * (1 << n));
    int** ret = malloc(sizeof(int*) * (1 << n));
    t = malloc(sizeof(int) * n);
    dfs(false, 0, nums, n, ret, returnSize, returnColumnSizes);
    return ret;
}
复杂度分析

时间复杂度：O(n \times 2^n)O(n×2 
n
 )，其中 nn 是数组 \textit{nums}nums 的长度。排序的时间复杂度为 O(n \log n)O(nlogn)。最坏情况下 \textit{nums}nums 中无重复元素，需要枚举其所有 2^n2 
n
  个子集，每个子集加入答案时需要拷贝一份，耗时 O(n)O(n)，一共需要 O(n \times 2^n)+O(n)=O(n \times 2^n)O(n×2 
n
 )+O(n)=O(n×2 
n
 ) 的时间来构造子集。由于在渐进意义上 O(n \log n)O(nlogn) 小于 O(n \times 2^n)O(n×2 
n
 )，故总的时间复杂度为 O(n \times 2^n)O(n×2 
n
 )。

空间复杂度：O(n)O(n)。临时数组 \textit{t}t 的空间代价是 O(n)O(n)，递归时栈空间的代价为 O(n)O(n)。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/subsets-ii/solution/zi-ji-ii-by-leetcode-solution-7inq/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''

