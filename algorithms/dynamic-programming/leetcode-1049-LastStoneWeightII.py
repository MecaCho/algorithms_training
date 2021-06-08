# encoding=utf8

'''
1049. Last Stone Weight II

You are given an array of integers stones where stones[i] is the weight of the ith stone.

We are playing a game with the stones. On each turn, we choose any two stones and smash them together. Suppose the stones have weights x and y with x <= y. The result of this smash is:

If x == y, both stones are destroyed, and
If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
At the end of the game, there is at most one stone left.

Return the smallest possible weight of the left stone. If there are no stones left, return 0.

 

Example 1:

Input: stones = [2,7,4,1,8,1]
Output: 1
Explanation:
We can combine 2 and 4 to get 2, so the array converts to [2,7,1,8,1] then,
we can combine 7 and 8 to get 1, so the array converts to [2,1,1,1] then,
we can combine 2 and 1 to get 1, so the array converts to [1,1,1] then,
we can combine 1 and 1 to get 0, so the array converts to [1], then that's the optimal value.
Example 2:

Input: stones = [31,26,33,21,40]
Output: 5
Example 3:

Input: stones = [1,2]
Output: 1
 

Constraints:

1 <= stones.length <= 30
1 <= stones[i] <= 100

1049. 最后一块石头的重量 II

有一堆石头，用整数数组 stones 表示。其中 stones[i] 表示第 i 块石头的重量。

每一回合，从中选出任意两块石头，然后将它们一起粉碎。假设石头的重量分别为 x 和 y，且 x <= y。那么粉碎的可能结果如下：

如果 x == y，那么两块石头都会被完全粉碎；
如果 x != y，那么重量为 x 的石头将会完全粉碎，而重量为 y 的石头新重量为 y-x。
最后，最多只会剩下一块 石头。返回此石头 最小的可能重量 。如果没有石头剩下，就返回 0。

 

示例 1：

输入：stones = [2,7,4,1,8,1]
输出：1
解释：
组合 2 和 4，得到 2，所以数组转化为 [2,7,1,8,1]，
组合 7 和 8，得到 1，所以数组转化为 [2,1,1,1]，
组合 2 和 1，得到 1，所以数组转化为 [1,1,1]，
组合 1 和 1，得到 0，所以数组转化为 [1]，这就是最优值。
示例 2：

输入：stones = [31,26,33,21,40]
输出：5
示例 3：

输入：stones = [1,2]
输出：1
 

提示：

1 <= stones.length <= 30
1 <= stones[i] <= 100
'''

class Solution(object):
    def lastStoneWeightII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        sum_stones = sum(stones)
        dp = [0]*(sum_stones/2+1)
        for i in range(len(stones)):
            for j in range(sum_stones/2, stones[i]-1, -1):
                dp[j] = max(dp[j], dp[j-stones[i]]+stones[i])

        return sum_stones - 2*dp[sum_stones/2]

       
# solutions

'''
解题思路
和昨天的每日一题有点像494. 目标和
两个石头相撞，大的减小的，数组里面的数字有的前面是 “ + ” 有的是 “ - ”，相当于就是给这个数组，每个数字前面加上符号。
(sum - neg) - neg = sum - 2 * neg 需要找出 neg 最接近sum/2 的值 ，即背包容量sum/2 ，求得是包内装最大的物品。
dp数组 表示的是在有i件商品背包容量为j前提下，能装物品的最大值

初始状态：dp[0][0] = 0; 当背包为0 ，能装进去的最大为0
如果可以装下，可选择装不装下，判断大小：dp[i][j] = Math.max(dp[i-1][j] , dp[i-1][j - x] + x);

代码

class Solution {
    public int lastStoneWeightII(int[] stones) {        
        int n = stones.length , sum = 0;
        for(int i = 0; i < n; i++){
            sum += stones[i];
        }
        int l = sum/2 ;
        //dp 表示的是在有i件商品背包容量为j前提下，能装物品的最大值
        int[][] dp = new int[n + 1][l+1];
        // dp[0][0] = 0; 当背包为0 ，能装进去的最大为0

        for(int i = 1 ; i < n + 1; i++){
            int x =  stones[i-1];
            for(int j = 0; j < l + 1; j++ ){
                if(j < stones[i - 1]){
                    dp[i][j] = dp[i-1][j];
                }else{
                    //如果可以装下，可选择装不装下，判断大小
                    dp[i][j] = Math.max(dp[i-1][j] , dp[i-1][j - x] + x);
                }
            }
        }

        return Math.abs(sum - dp[n][l] * 2);

    }
}


作者：xue-you-yong-de-ben-mao
链接：https://leetcode-cn.com/problems/last-stone-weight-ii/solution/1049-zui-hou-yi-kuai-shi-tou-de-zhong-li-vfx7/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''

# tips

'''
Think of the final answer as a sum of weights with + or - sign symbols infront of each weight. Actually, all sums with 1 of each sign symbol are possible.

Use dynamic programming: for every possible sum with N stones, those sums +x or -x is possible with N+1 stones, where x is the value of the newest stone. (This overcounts sums that are all positive or all negative, but those don't matter.)
'''
