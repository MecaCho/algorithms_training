

'''
487. 最大连续1的个数 II
给定一个二进制数组，你可以最多将 1 个 0 翻转为 1，找出其中最大连续 1 的个数。

示例 1：

输入：[1,0,1,1,0]
输出：4
解释：翻转第一个 0 可以得到最长的连续 1。
     当翻转以后，最大连续 1 的个数为 4。


注：

输入数组只包含 0 和 1.
输入数组的长度为正整数，且不超过 10,000


进阶：
如果输入的数字是作为 无限流 逐个输入如何处理？换句话说，内存不能存储下所有从流中输入的数字。您可以有效地解决吗？

487. Max Consecutive Ones II
Given a binary array, find the maximum number of consecutive 1s in this array if you can flip at most one 0.

Example 1:
Input: [1,0,1,1,0]
Output: 4
Explanation: Flip the first zero will get the the maximum number of consecutive 1s.
    After flipping, the maximum number of consecutive 1s is 4.
Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000
Follow up:
What if the input numbers come in one by one as an infinite stream? In other words, you can't store all numbers coming from the stream as it's too large to hold in memory. Could you solve it efficiently?
'''


# golang

'''
func findMaxConsecutiveOnes(nums []int) int {
    if len(nums) < 2{
        return len(nums)
    }
    maxLength := 1

    i := -1
    lastZeroIndex := -1
    preLastZeroIndex := -1

    length := len(nums)

    for k := 0; k < length;k++{
        if nums[k] == 1{
            newLength := k - i
            if lastZeroIndex == i{
                newLength ++
            }
            if newLength > maxLength{
                maxLength = newLength
            }
        } else{
            preLastZeroIndex = lastZeroIndex
            lastZeroIndex = k
            if k <= 0 || nums[k-1] == 1{
                i = preLastZeroIndex
            } else{
                i = lastZeroIndex
            }
        }
    }
    if lastZeroIndex == -1{
        maxLength = length
    }
    return maxLength
}
'''

# solutions

'''
方法一：预处理 + 枚举
直观的想法就是枚举每个 00 的位置，把这个位置变成 11 ，统计它能把前后连成的最多的 11 的个数。考虑位置 i(0<i<n-1)i(0<i<n−1) ，从这个位置切开可以将整个数组（数组下标 [0,n-1][0,n−1]）分成三个部分：

[0,i-1][0,i−1]
[i,i][i,i]
[i+1,n-1][i+1,n−1]
则区间包含 ii 的最大连续 11 的个数就是由第一部分的数组末尾往前延伸最大的连续 11 的个数加上第三部分的数组开头往后延伸最大的连续 11 的个数再加上把第 ii 个位置变成 11 的总和。第一部分和第二部分我们都可以通过预处理数组来实现 O(1)O(1) 查询。

预处理 pre[i]pre[i] 数组表示以 ii 结尾往前延伸最大连续 11 的个数，则可以列出递推式：

\left\{\begin{matrix}pre[i-1]+1,nums[i]=1\\ 0,nums[i]=0\end{matrix}\right.
{ 
pre[i−1]+1,nums[i]=1
0,nums[i]=0
​	
 

预处理 suff[i]suff[i] 数组表示以 ii 开头往后延伸最大连续 11 的个数，则可以列出递推式：

\left\{\begin{matrix}suff[i+1]+1,nums[i]=1\\ 0,nums[i]=0\end{matrix}\right.
{ 
suff[i+1]+1,nums[i]=1
0,nums[i]=0
​	
 

则位置 ii 的答案就是pre[i-1]+1+suff[i+1]pre[i−1]+1+suff[i+1]

对于这一类最多改变一个位置的题都可以这么考虑，当然我们肯定还要统计原数组的最大连续 11 的个数，这个直接在我们预处理两个数组的时候就可以统计出来了，即 max_{i=0}^npre[i]max 
i=0
n
​	
 pre[i] 。

C++

class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int n=(int)nums.size(),ans=0;
        vector<int>pre(n,0),suff(n,0);
        for (int i=0;i<n;++i){
            if (i) pre[i]=pre[i-1];
            if (nums[i]) pre[i]++;
            else pre[i]=0;
            ans=max(ans,pre[i]);
        }
        for (int i=n-1;i>=0;--i){
            if (i<n-1) suff[i]=suff[i+1];
            if (nums[i]) suff[i]++;
            else suff[i]=0;
        }
        for (int i=0;i<n;++i)if(!nums[i]){
            int res=0;
            if (i>0) res+=pre[i-1];
            if (i<n-1) res+=suff[i+1];
            ans=max(ans,res+1);
        }
        return ans;
    }
};
复杂度分析

时间复杂度：O(n)O(n) ，预处理两个数组 O(n)O(n)， 最后统计答案也是 O(n)O(n) 。
空间复杂度：O(n)O(n)， 需要额外两个辅助数组。
方法二：动态规划
方法一其实没有办法解决进阶问题：如果输入的数字是作为无限流逐个输入如何处理？换句话说，内存不能存储下所有从流中输入的数字。您可以有效地解决吗？ 因为它需要预先知道所有的数，而我们如果用动态规划则可以有效解决进阶问题。

定义 dp[i][0]dp[i][0] 为考虑到以 ii 为结尾未使用操作将 [0,i][0,i] 某个 00 变成 11 的最大的连续 11 的个数，dp[i][1]dp[i][1] 为考虑到以 ii 为结尾使用操作将 [0,i][0,i] 某个 00 变成 11 的最大的连续 11 的个数。则我们可以列出转移式：

dp[i][0]=\left\{\begin{matrix} dp[i-1][0]+1,nums[i]=1\\ 0,nums[i]=0 \end{matrix}\right.
dp[i][0]={ 
dp[i−1][0]+1,nums[i]=1
0,nums[i]=0
​	
 

和

dp[i][1]=\left\{\begin{matrix} dp[i-1][1]+1,nums[i]=1\\ dp[i-1][0]+1,nums[i]=0 \end{matrix}\right.
dp[i][1]={ 
dp[i−1][1]+1,nums[i]=1
dp[i−1][0]+1,nums[i]=0
​	
 

解释一下，针对 dp[i][0]dp[i][0] ，如果当前位置是 00 ，由于未使用操作，所以肯定是 00，如果是 11，则从前一个位置未使用操作的状态转移过来即可。针对 dp[i][1]dp[i][1] ，如果当前位置是 00 ，则我们操作肯定是要用在这个位置，把它变成 11，所以只能从前一个未使用过操作的状态转移过来，如果是 11 ，则从前一个已经使用过操作的状态转移过来。

最后答案就是 max_{i=0}^{n-1}max(dp[i][0],dp[i][1])max 
i=0
n−1
​	
 max(dp[i][0],dp[i][1]) 。

到这里其实还并不能解决进阶问题，因为开 dpdp 数组仍然需要提前知道数组的大小，但是我们注意到每次转移只与前一个位置有关，所以我们并不需要开数组，只需要额外两个变量记录一下前一个位置的两个状态即可，这样我们就可以有效解决进阶的问题。

C++

class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int n=(int)nums.size(),ans=0,dp0=0,dp1=0;
        for (int i=0;i<n;++i){
            if (nums[i]){
                dp1++;
                dp0++;
            }
            else{
                dp1=dp0+1;
                dp0=0;
            }
            ans=max(ans,max(dp0,dp1));
        }
        return ans;
    }
};
复杂度分析

时间复杂度：由上面的转移式我们知道转移是O(1)O(1) 的，一共有 2n2n 个状态，所以时间复杂度为 O(n)O(n)。
空间复杂度：O(1)O(1) 。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/max-consecutive-ones-ii/solution/zui-da-lian-xu-1de-ge-shu-ii-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''