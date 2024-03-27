# encoding=utf8

'''
2580. Count Ways to Group Overlapping Ranges

You are given a 2D integer array ranges where ranges[i] = [starti, endi] denotes that all integers between starti and endi (both inclusive) are contained in the ith range.

You are to split ranges into two (possibly empty) groups such that:

Each range belongs to exactly one group.
Any two overlapping ranges must belong to the same group.
Two ranges are said to be overlapping if there exists at least one integer that is present in both ranges.

For example, [1, 3] and [2, 5] are overlapping because 2 and 3 occur in both ranges.
Return the total number of ways to split ranges into two groups. Since the answer may be very large, return it modulo 109 + 7.

 

Example 1:

Input: ranges = [[6,10],[5,15]]
Output: 2
Explanation: 
The two ranges are overlapping, so they must be in the same group.
Thus, there are two possible ways:
- Put both the ranges together in group 1.
- Put both the ranges together in group 2.
Example 2:

Input: ranges = [[1,3],[10,20],[2,5],[4,8]]
Output: 4
Explanation: 
Ranges [1,3], and [2,5] are overlapping. So, they must be in the same group.
Again, ranges [2,5] and [4,8] are also overlapping. So, they must also be in the same group. 
Thus, there are four possible ways to group them:
- All the ranges in group 1.
- All the ranges in group 2.
- Ranges [1,3], [2,5], and [4,8] in group 1 and [10,20] in group 2.
- Ranges [1,3], [2,5], and [4,8] in group 2 and [10,20] in group 1.
 

Constraints:

1 <= ranges.length <= 105
ranges[i].length == 2
0 <= starti <= endi <= 109
'''

class Solution:
    def countWays(self, ranges: List[List[int]]) -> int:
        mod = 10**9+7
        ranges.sort(key=lambda k: k[0])
        pre_max = -1
        num = 0
        for l, r in ranges:
            print(l, r)
            if l > pre_max:
                num += 1
            pre_max = max(pre_max, r)
        return 2**num % mod

# tips

'''
题单：合并区间
练习 A
56. 合并区间
55. 跳跃游戏
2963. 统计好分割方案的数目 1985
2584. 分割数组使乘积互质 2159
2655. 寻找最大长度的未覆盖区间（会员题）
练习 B
45. 跳跃游戏 II
1024. 视频拼接 1746
1326. 灌溉花园的最少水龙头数目 1885
分类题单
滑动窗口（定长/不定长/多指针）https://leetcode.cn/circle/discuss/0viNMK/
二分算法（二分答案/最小化最大值/最大化最小值/第K小）https://leetcode.cn/circle/discuss/SqopEo/
单调栈（矩形系列/字典序最小/贡献法）https://leetcode.cn/circle/discuss/9oZFK9/
网格图（DFS/BFS/综合应用）https://leetcode.cn/circle/discuss/YiXPXW/
位运算（基础/性质/拆位/试填/恒等式/贪心/脑筋急转弯）https://leetcode.cn/circle/discuss/dHn9Vk/
图论算法（DFS/BFS/拓扑排序/最短路/最小生成树/二分图/基环树/欧拉路径）https://leetcode.cn/circle/discuss/01LUak/
动态规划（入门/背包/状态机/划分/区间/状压/数位/数据结构优化/树形/博弈/概率期望）https://leetcode.cn/circle/discuss/tXLS3i/


作者：灵茶山艾府
链接：https://leetcode.cn/problems/count-ways-to-group-overlapping-ranges/solutions/2147717/tiao-yue-you-xi-bian-xing-by-endlesschen-hatn/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''

