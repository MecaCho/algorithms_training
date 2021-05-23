# encoding=utf8


'''
1707. Maximum XOR With an Element From Array

You are given an array nums consisting of non-negative integers. You are also given a queries array, where queries[i] = [xi, mi].

The answer to the ith query is the maximum bitwise XOR value of xi and any element of nums that does not exceed mi. In other words, the answer is max(nums[j] XOR xi) for all j such that nums[j] <= mi. If all elements in nums are larger than mi, then the answer is -1.

Return an integer array answer where answer.length == queries.length and answer[i] is the answer to the ith query.

 

Example 1:

Input: nums = [0,1,2,3,4], queries = [[3,1],[1,3],[5,6]]
Output: [3,3,7]
Explanation:
1) 0 and 1 are the only two integers not greater than 1. 0 XOR 3 = 3 and 1 XOR 3 = 2. The larger of the two is 3.
2) 1 XOR 2 = 3.
3) 5 XOR 2 = 7.
Example 2:

Input: nums = [5,2,4,6,6,3], queries = [[12,4],[8,1],[6,3]]
Output: [15,-1,5]
 

Constraints:

1 <= nums.length, queries.length <= 105
queries[i].length == 2
0 <= nums[j], xi, mi <= 109

1707. 与数组中元素的最大异或值

给你一个由非负整数组成的数组 nums 。另有一个查询数组 queries ，其中 queries[i] = [xi, mi] 。

第 i 个查询的答案是 xi 和任何 nums 数组中不超过 mi 的元素按位异或（XOR）得到的最大值。换句话说，答案是 max(nums[j] XOR xi) ，其中所有 j 均满足 nums[j] <= mi 。如果 nums 中的所有元素都大于 mi，最终答案就是 -1 。

返回一个整数数组 answer 作为查询的答案，其中 answer.length == queries.length 且 answer[i] 是第 i 个查询的答案。

 

示例 1：

输入：nums = [0,1,2,3,4], queries = [[3,1],[1,3],[5,6]]
输出：[3,3,7]
解释：
1) 0 和 1 是仅有的两个不超过 1 的整数。0 XOR 3 = 3 而 1 XOR 3 = 2 。二者中的更大值是 3 。
2) 1 XOR 2 = 3.
3) 5 XOR 2 = 7.
示例 2：

输入：nums = [5,2,4,6,6,3], queries = [[12,4],[8,1],[6,3]]
输出：[15,-1,5]
 

提示：

1 <= nums.length, queries.length <= 105
queries[i].length == 2
0 <= nums[j], xi, mi <= 109
'''


class Trie(object):
    L = 30

    def __init__(self):
        self.left = None
        self.right = None
        self.min_value = float("inf")

    def insert(self, val):
        node = self
        node.min_value = min(node.min_value, val)
        for i in range(Trie.L, -1, -1):
            bit = (val >> i) & 1
            if bit == 0:
                if not node.left:
                    node.left = Trie()
                node = node.left
            else:
                if not node.right:
                    node.right = Trie()
                node = node.right
            node.min_value = min(node.min_value, val)
    
    def getMaxXorWithLimit(self, val, limit):
        node = self
        if node.min_value > limit:
            return -1
        
        ans = 0
        for i in range(Trie.L, -1, -1):
            bit = (val >> i) & 1
            check = False
            if bit == 0:
                if node.right and node.right.min_value <= limit:
                    node = node.right
                    check = True
                else:
                    node = node.left
            else:
                if node.left and node.left.min_value <= limit:
                    node = node.left
                    check = True
                else:
                    node = node.right
            if check:
                ans |= 1 << i
        return ans

class Solution(object):
    def maximizeXor(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        t = Trie()
        for val in nums:
            t.insert(val)
        
        q = len(queries)
        ans = [0] * q
        for i, (x, m) in enumerate(queries):
            ans[i] = t.getMaxXorWithLimit(x, m)
        
        return ans
      
