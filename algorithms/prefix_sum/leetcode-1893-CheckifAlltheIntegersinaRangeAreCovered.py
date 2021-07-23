# encoding=utf8

'''
1893. Check if All the Integers in a Range Are Covered
You are given a 2D integer array ranges and two integers left and right. Each ranges[i] = [starti, endi] represents an inclusive interval between starti and endi.

Return true if each integer in the inclusive range [left, right] is covered by at least one interval in ranges. Return false otherwise.

An integer x is covered by an interval ranges[i] = [starti, endi] if starti <= x <= endi.

 

Example 1:

Input: ranges = [[1,2],[3,4],[5,6]], left = 2, right = 5
Output: true
Explanation: Every integer between 2 and 5 is covered:
- 2 is covered by the first range.
- 3 and 4 are covered by the second range.
- 5 is covered by the third range.
Example 2:

Input: ranges = [[1,10],[10,20]], left = 21, right = 21
Output: false
Explanation: 21 is not covered by any range.
 

Constraints:

1 <= ranges.length <= 50
1 <= starti <= endi <= 50
1 <= left <= right <= 50


1893. 检查是否区域内所有整数都被覆盖
给你一个二维整数数组 ranges 和两个整数 left 和 right 。每个 ranges[i] = [starti, endi] 表示一个从 starti 到 endi 的 闭区间 。

如果闭区间 [left, right] 内每个整数都被 ranges 中 至少一个 区间覆盖，那么请你返回 true ，否则返回 false 。

已知区间 ranges[i] = [starti, endi] ，如果整数 x 满足 starti <= x <= endi ，那么我们称整数x 被覆盖了。

 

示例 1：

输入：ranges = [[1,2],[3,4],[5,6]], left = 2, right = 5
输出：true
解释：2 到 5 的每个整数都被覆盖了：
- 2 被第一个区间覆盖。
- 3 和 4 被第二个区间覆盖。
- 5 被第三个区间覆盖。
示例 2：

输入：ranges = [[1,10],[10,20]], left = 21, right = 21
输出：false
解释：21 没有被任何一个区间覆盖。
 

提示：

1 <= ranges.length <= 50
1 <= starti <= endi <= 50
1 <= left <= right <= 50
'''

class Solution(object):
    def isCovered(self, ranges, left, right):
        """
        :type ranges: List[List[int]]
        :type left: int
        :type right: int
        :rtype: bool
        """
        diff = [0]*52
        for l, r in ranges:
            diff[l] += 1
            diff[r+1] -= 1

        # print(diff)
        cur = 0
        for i in range(1, 51+1):
            cur += diff[i]
            # print(i, cur)
            if left <= i <= right and cur <= 0:
                return False

        return True

      
# solutions

'''
当然这个还可以利用堆，排序，hash，线段树，位运算等等很多。
接下来介绍四种参考
但是差分数组思想是最强的，功能不止于此。
暴力和优化版本标记数组只需要布尔型即可。

因为以下解法申请空间在52长度内，空间复杂度O(1)，而且第二层for循环都是对52空间内修改，故时间复杂度为O(n)，.

解法1：暴力
在每个节点起始位置和终点位置之间的flag标记为true，代表该点已经被包含。
当我们查询时，如果查询left与right之间只要有一点为false，返回flase


class Solution {
    public boolean isCovered(int[][] ranges, int left, int right) {
        boolean[] flag = new boolean[51];
        for(int[] range : ranges){
            for(int i = range[0]; i <= range[1];i++){
                flag[i] = true;
            }
        }
        for(int i = left; i <= right; i++){
            if(flag[i] == false) return false;
        }
        return true;
    }
}
暴力的时间复杂度是O(51n) = O(n)，同理空间复杂度O(1)。

方法2：基于排序
如将区间的起始点从小到达排序，然后每次比较，如果拿到的区间[l,r]，left在区间内，即 l <= left <= r，那么可知，[left,r]便已经被覆盖，接下来只需接续检查剩余空白部分，让left = r + 1, 如果最后left可以超过right，则区间全部被覆盖。为true。


class Solution {
    public boolean isCovered(int[][] ranges, int left, int right) {
        Arrays.sort(ranges, (a1, a2) -> a1[0] - a2[0]);
        for(int[] range: ranges) {
            int l = range[0];
            int r = range[1];
            if(l <= left && left <= r) {
                left = r + 1;
            }
        }
        return left > right;
    }
}
时间复杂度为排序算法的复杂度度 O(nlog(n))。空间复杂度，由于java7之后数组排序采用DualPrivotQuicksort代替原来快排，规模小时为插入排序，规模大时为快速排序，快速排序中，性能较为优越稳定的是随机化快排，比其他挖坑填数，取中值，或者基础快排正常情况下是2倍到4倍，属于越大越明显。所以空间复杂度O(logn)。

但是我们还可以继续优化

解法3：优化 只标记[left,right]
因为我们是查询left与right之间的点是否完全包含在原数组表示区间中，那么我们只需要关心
[left,right]上这一段即可。我们只标记[left,right]区间即可，
以[left,right]为基准思考，每当从二维数组中拿到一个区间[l,r]，
我们只需要标记[left,right]与[l,r]的交集部分。如果没有交集不标记。
如果l比left还小，我们没必要从l开始标记，从left标记。
如果r比right还大，我们没必要标记到r，只要标记到right即可。
故只需要定义两个变量：
L = Math.max(l,left);
R = Math.min(r,right);
看下图理解：
拿到的区间如果长度小，变为以下五种情况， 那么L，R满足 L <= R，才能标记，否则
不能标记，如果拿到区间长，同理，这里只是画一下示意。

L 为left,l的较大值， R 为right，r的较小值 打钩为可标记
这便是取交集思想

让拿到的区间，从左到右相对于[left,right] 进行滑动即可。


class Solution {
    public boolean isCovered(int[][] ranges, int left, int right) {
        boolean[] flag = new boolean[51];
        for(int[] range : ranges){
            int L = Math.max(range[0],left);
            int R = Math.min(range[1],right);
            for(int i = L; i <= R; i++){
                flag[i] = true;
            }
        }
        for(int i = left; i <= right; i++){
            if(flag[i] == false) return false;
        }
        return true;
    }
}
因为遍历过程中，我们需要对L，R之间进行修改，但是[L,R]区间是小于或等于[left,right]区间的，
每次在区间内做修改，故时间复杂度为O(n(left - right + 1))也等同O(n)，因为宽度最大为常数51
故时间复杂度 O(n)。
空间复杂度O(1)。

解法4：差分数组
差分数组diff表示相邻格之间，是否被覆盖的变化量。
diff[i]++,代表在i位置上有新的覆盖
若覆盖到j结束了呢？此时j依然是覆盖，但是j+1不在覆盖状态，所以在j+1处 -1；
即diff[j+1]--;
当我们把差分数组求前缀和，就很直观把这种变化量转化为不变的，可以理解的。
前缀和sum[i]的大小，就代表被覆盖次数，接下来用图展示；

如有四个需要加入的区间 1，2，3，4；加入之后 all为加入之后区间图覆盖图，但是看不出了每个点被覆盖几次，但是差分前缀和可以做到，接下来继续了解。



我们定义diff差分数组，由上定义可知，在起始下标+1，在终止下标之后-1；当加入（1）和（2）之后，差分数组黄色区域为被覆盖部分，但是从差分数组看不出来，只是示意标出来，



接下来继续同理加入(3) 和 (4)；由于(4)的是最后结束，-1没有位置，所以差分数组定义时候必须多定义一个，int[52]



接下来就是最关键，最熟悉对差分数组求前缀和。sum，发现在覆盖的地方，都是正数，而没有覆盖的地方为0，如果要查询 [2,5]，直接将[2,5]区间与sum逐个对比，看sun是否大于0，如果发现不大于0，一定出现了空白，没有覆盖，



而我们从前缀和数组可以看出，每一个位大小代表被覆盖几次，比如[1,2]区域都是2，因为我们在加入时候 (1)和(2)正是在这个地方重复覆盖，

所以差分数组前缀和不仅能查询是否被覆盖，还能查询某一区间被覆盖几次。

class Solution {
    public boolean isCovered(int[][] ranges, int left, int right) {
        int[] diff = new int[52];
        //对差分数组进行处理
        for(int i = 0; i < ranges.length; i++){
            diff[ranges[i][0]]++;
            diff[ranges[i][1]+1]--;
        }
        //根据差分数组处理前缀和，为理解方便单独定义sum，可以原地做
        int[] sum = new int[52];
        for(int i = 1; i <= 51; i++){
            sum[i] = sum[i-1] + diff[i];
        }
        //从left到right判断是否满足sum > 0
        for(int i = left; i <= right; i++){
            if(sum[i] <= 0) return false;
        }
        return true;
    }
}

作者：LaoGanMaIsEverything
链接：https://leetcode-cn.com/problems/check-if-all-the-integers-in-a-range-are-covered/solution/yi-ti-san-jie-bao-li-you-hua-chai-fen-by-w7xv/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
