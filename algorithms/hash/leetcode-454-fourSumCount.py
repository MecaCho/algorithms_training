'''
454. 4Sum II
Given four lists A, B, C, D of integer values, compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.

To make problem a bit easier, all A, B, C, D have same length of N where 0 ≤ N ≤ 500. All integers are in the range of -228 to 228 - 1 and the result is guaranteed to be at most 231 - 1.

Example:

Input:
A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]

Output:
2

Explanation:
The two tuples are:
1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0

454. 四数相加 II
给定四个包含整数的数组列表 A , B , C , D ,计算有多少个元组 (i, j, k, l) ，使得 A[i] + B[j] + C[k] + D[l] = 0。

为了使问题简单化，所有的 A, B, C, D 具有相同的长度 N，且 0 ≤ N ≤ 500 。所有整数的范围在 -228 到 228 - 1 之间，最终结果不会超过 231 - 1 。

例如:

输入:
A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]

输出:
2

解释:
两个元组如下:
1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0

'''



class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        hash_map = {}
        for a in A:
            for b in B:
                key = a + b
                if key not in hash_map:
                    hash_map[key] = 1
                else:
                    hash_map[key] += 1
        count = 0
        for c in C:
            for d in D:
                key = -( c +d)
                if key in hash_map:
                    count += hash_map[key]
        return count


# solutions

'''
方法一：分组 + 哈希表
思路与算法

我们可以将四个数组分成两部分，AA 和 BB 为一组，CC 和 DD 为另外一组。

对于 AA 和 BB，我们使用二重循环对它们进行遍历，得到所有 A[i]+B[j]A[i]+B[j] 的值并存入哈希映射中。对于哈希映射中的每个键值对，每个键表示一种 A[i]+B[j]A[i]+B[j]，对应的值为 A[i]+B[j]A[i]+B[j] 出现的次数。

对于 CC 和 DD，我们同样使用二重循环对它们进行遍历。当遍历到 C[k]+D[l]C[k]+D[l] 时，如果 -(C[k]+D[l])−(C[k]+D[l]) 出现在哈希映射中，那么将 -(C[k]+D[l])−(C[k]+D[l]) 对应的值累加进答案中。

最终即可得到满足 A[i]+B[j]+C[k]+D[l]=0A[i]+B[j]+C[k]+D[l]=0 的四元组数目。

代码

C++JavaPython3JavaScriptGolangC

class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        countAB = collections.Counter(u + v for u in A for v in B)
        ans = 0
        for u in C:
            for v in D:
                if -u - v in countAB:
                    ans += countAB[-u - v]
        return ans
复杂度分析

时间复杂度：O(n^2)O(n 
2
 )。我们使用了两次二重循环，时间复杂度均为 O(n^2)O(n 
2
 )。在循环中对哈希映射进行的修改以及查询操作的期望时间复杂度均为 O(1)O(1)，因此总时间复杂度为 O(n^2)O(n 
2
 )。

空间复杂度：O(n^2)O(n 
2
 )，即为哈希映射需要使用的空间。在最坏的情况下，A[i]+B[j]A[i]+B[j] 的值均不相同，因此值的个数为 n^2n 
2
 ，也就需要 O(n^2)O(n 
2
 ) 的空间。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/4sum-ii/solution/si-shu-xiang-jia-ii-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''