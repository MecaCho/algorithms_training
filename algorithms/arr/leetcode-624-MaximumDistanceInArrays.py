# encoding=utf8

'''
624. 数组列表中的最大距离
给定 m 个数组，每个数组都已经按照升序排好序了。现在你需要从两个不同的数组中选择两个整数（每个数组选一个）并且计算它们的距离。两个整数 a 和 b 之间的距离定义为它们差的绝对值 |a-b| 。你的任务就是去找到最大距离

示例 1：

输入：
[[1,2,3],
 [4,5],
 [1,2,3]]
输出： 4
解释：
一种得到答案 4 的方法是从第一个数组或者第三个数组中选择 1，同时从第二个数组中选择 5 。


注意：

每个给定数组至少会有 1 个数字。列表中至少有两个非空数组。
所有 m 个数组中的数字总数目在范围 [2, 10000] 内。
m 个数组中所有整数的范围在 [-10000, 10000] 内。


624. Maximum Distance in Arrays
Given m arrays, and each array is sorted in ascending order. Now you can pick up two integers from two different arrays (each array picks one) and calculate the distance. We define the distance between two integers a and b to be their absolute difference |a-b|. Your task is to find the maximum distance.

Example 1:
Input:
[[1,2,3],
 [4,5],
 [1,2,3]]
Output: 4
Explanation:
One way to reach the maximum distance 4 is to pick 1 in the first or third array and pick 5 in the second array.
Note:
Each given array will have at least 1 number. There will be at least two non-empty arrays.
The total number of the integers in all the m arrays will be in the range of [2, 10000].
The integers in the m arrays will be in the range of [-10000, 10000].
'''


class Solution(object):
    def maxDistance(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """
        max_val = -float("inf")
        min_val = float("inf")
        res = 0
        for i in range(len(arrays)):
            vals = (min(arrays[i]), max(arrays[i]))
            res = max(res, max(vals[1] - min_val, max_val - vals[0]))
            max_val = vals[1] if vals[1] > max_val else max_val
            min_val = vals[0] if vals[0] < min_val else min_val
        return res


'''
方法一：枚举 [超出时间限制]
对于每一个数组，只有第一个元素（最小的元素）和最后一个元素（最大的元素）是有意义的，因此我们可以枚举选择的两个数组 m[i] 和 m[j]，随后计算出 m[i] 的第一个元素和 m[j] 的最后一个元素的差的绝对值，以及 m[i] 的最后一个元素和 m[j] 的第一个元素的差的绝对值。在这些绝对值中，找出最大的距离。

Java
public class Solution {
    public int maxDistance(int[][] list) {
        int res = 0;
        for (int i = 0; i < list.length - 1; i++) {
            for (int j = i + 1; j < list.length; j++) {
                res = Math.max(res, Math.abs(list[i][0] - list[j][list[j].length - 1]));
                res = Math.max(res, Math.abs(list[j][0] - list[i][list[i].length - 1]));
            }
        }
        return res;
    }
}
复杂度分析

时间复杂度：O(M^2)O(M 
2
 )，其中 MM 是数组的个数。我们需要使用二重循环来枚举 m[i] 和 m[j]。

空间复杂度；O(1)O(1)。

方法二：线性扫描
方法一告诉我们，当我们枚举了两个数组之后，只有这两个数组的最小值和最大值才是有意义的。同理，假设我们确定了第一个数要从第 i 个数组中选择，第二个数要从前 i - 1 个数组中选择，如果我们把前 i - 1 个数组看成一个大的数组，那么只有这 i - 1 个数组中的最小值和最大值才是有意义的。

因此我们找到了可以方法一中可以优化的地方。我们顺序扫描这 m 个数组，当扫描到第 i 个数组时，我们计算出 m[i] 中最小的元素和前 i - 1 个数组中最大的元素 max_val 的差的绝对值，以及 m[i] 中最大的元素和前 i - 1 个数组中最小的元素 min_val 的差的绝对值。在这之后，我们更新 min_val 和 max_val，使其变为前 i 个数组中最小和最大的元素。


1 / 8

Java
public class Solution {
    public int maxDistance(int[][] list) {
        int res = 0, min_val = list[0][0], max_val = list[0][list[0].length - 1];
        for (int i = 1; i < list.length; i++) {
            res = Math.max(res, Math.max(Math.abs(list[i][list[i].length - 1] - min_val), Math.abs(max_val - list[i][0])));
            min_val = Math.min(min_val, list[i][0]);
            max_val = Math.max(max_val, list[i][list[i].length - 1]);
        }
        return res;
    }
}
复杂度分析

时间复杂度：O(M)O(M)，其中 MM 是数组的个数。

空间复杂度：O(1)O(1)。

作者：LeetCode
链接：https://leetcode-cn.com/problems/maximum-distance-in-arrays/solution/shu-zu-lie-biao-zhong-de-zui-da-ju-chi-by-leetcode/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
