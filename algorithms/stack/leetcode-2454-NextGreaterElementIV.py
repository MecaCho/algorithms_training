# encoding=utf8

'''
2454. Next Greater Element IV

You are given a 0-indexed array of non-negative integers nums. For each integer in nums, you must find its respective second greater integer.

The second greater integer of nums[i] is nums[j] such that:

j > i
nums[j] > nums[i]
There exists exactly one index k such that nums[k] > nums[i] and i < k < j.
If there is no such nums[j], the second greater integer is considered to be -1.

For example, in the array [1, 2, 4, 3], the second greater integer of 1 is 4, 2 is 3, and that of 3 and 4 is -1.
Return an integer array answer, where answer[i] is the second greater integer of nums[i].

 

Example 1:

Input: nums = [2,4,0,9,6]
Output: [9,6,6,-1,-1]
Explanation:
0th index: 4 is the first integer greater than 2, and 9 is the second integer greater than 2, to the right of 2.
1st index: 9 is the first, and 6 is the second integer greater than 4, to the right of 4.
2nd index: 9 is the first, and 6 is the second integer greater than 0, to the right of 0.
3rd index: There is no integer greater than 9 to its right, so the second greater integer is considered to be -1.
4th index: There is no integer greater than 6 to its right, so the second greater integer is considered to be -1.
Thus, we return [9,6,6,-1,-1].
Example 2:

Input: nums = [3,3]
Output: [-1,-1]
Explanation:
We return [-1,-1] since neither integer has any integer greater than it.
 

Constraints:

1 <= nums.length <= 105
0 <= nums[i] <= 109
'''


'''
单调栈
739. 每日温度（单调栈模板题）
1475. 商品折扣后的最终价格
496. 下一个更大元素 I
503. 下一个更大元素 II
1019. 链表中的下一个更大节点 1571
901. 股票价格跨度 1709
1124. 表现良好的最长时间段 1908
456. 132 模式 ~2000
2866. 美丽塔 II 2072
2454. 下一个更大元素 IV 2175
2289. 使数组按非递减顺序排列 2482
2832. 每个元素为最大值的最大范围（会员题）

矩形系列
84. 柱状图中最大的矩形
85. 最大矩形
1504. 统计全 1 子矩形 1845

字典序最小
316. 去除重复字母
316 扩展：重复个数不超过 limit
402. 移掉 K 位数字 ~1800
1673. 找出最具竞争力的子序列 1802
321. 拼接最大数

贡献法
907. 子数组的最小值之和 1976
2104. 子数组范围和（最大值-最小值） O(n)\mathcal{O}(n)O(n) 做法 ~2000
1856. 子数组最小乘积的最大值 2051
2818. 操作使得分最大 2397
2281. 巫师的总力量和（最小值*和） 2621

'''
