'''
546. 移除盒子
给出一些不同颜色的盒子，盒子的颜色由数字表示，即不同的数字表示不同的颜色。
你将经过若干轮操作去去掉盒子，直到所有的盒子都去掉为止。每一轮你可以移除具有相同颜色的连续 k 个盒子（k >= 1），这样一轮之后你将得到 k*k 个积分。
当你将所有盒子都去掉之后，求你能获得的最大积分和。



示例：

输入：boxes = [1,3,2,2,2,3,4,3,1]
输出：23
解释：
[1, 3, 2, 2, 2, 3, 4, 3, 1]
----> [1, 3, 3, 4, 3, 1] (3*3=9 分)
----> [1, 3, 3, 3, 1] (1*1=1 分)
----> [1, 1] (3*3=9 分)
----> [] (2*2=4 分)


提示：

1 <= boxes.length <= 100
1 <= boxes[i] <= 100

546. Remove Boxes
Given several boxes with different colors represented by different positive numbers.
You may experience several rounds to remove boxes until there is no box left. Each time you can choose some continuous boxes with the same color (composed of k boxes, k >= 1), remove them and get k*k points.
Find the maximum points you can get.



Example 1:

Input: boxes = [1,3,2,2,2,3,4,3,1]
Output: 23
Explanation:
[1, 3, 2, 2, 2, 3, 4, 3, 1]
----> [1, 3, 3, 4, 3, 1] (3*3=9 points)
----> [1, 3, 3, 3, 1] (1*1=1 points)
----> [1, 1] (3*3=9 points)
----> [] (2*2=4 points)


Constraints:

1 <= boxes.length <= 100
1 <= boxes[i] <= 100

'''


import functools
class Solution(object):
    def removeBoxes(self, boxes):
        """
        :type boxes: List[int]
        :rtype: int
        """
        @functools.lru_cache()
        def dp(l, r, k):
            if l > r:
                return 0
            while l < r and boxes[r] == boxes[r-1]:
                r -= 1
                k += 1

            dp_l_r_k = dp(l, r-1, 0) + (k+1)*(k+1)

            for i in range(l, r):
                if boxes[i] == boxes[r]:
                    dp_l_r_k = max(dp_l_r_k, dp(i+1, r-1, 0)+dp(l, i, k+1))

            return dp_l_r_k

        return dp(0, len(boxes) - 1, 0)



class Solution1(object):
    def removeBoxes(self, boxes):
        """
        :type boxes: List[int]
        :rtype: int
        """
        # import functools
        dp_map = {}
        def dp(l, r, k):
            if l > r:
                return 0
            while l < r and boxes[r] == boxes[r-1]:
                r -= 1
                k += 1

            if (l, r, k) in dp_map:
                return dp_map[(l, r, k)]

            dp_l_r_k = dp(l, r-1, 0) + (k+1)*(k+1)

            for i in range(l, r):
                if boxes[i] == boxes[r]:
                    dp_l_r_k = max(dp_l_r_k, dp(i+1, r-1, 0)+dp(l, i, k+1))
            dp_map[(l, r, k)] = dp_l_r_k
            return dp_l_r_k

        return dp(0, len(boxes) - 1, 0)




# solutions

'''

/*
* 补充题目：一次可以移除具有相同颜色的连续盒子，是每次只能移除一个滑窗，而不是一次移除同一种颜色所有地方
* 设dp[l][r][k]
  起始下标l(以0开始)，结束下标r，k表示在下标r后面紧接着有k个元素值和boxes[r]相同，的最大积分和
* 比如[l,l+1,···,r-1,r,值同r，值同r，值同r]
  这里有3个元素和boxes[r]相同，即k==3，那么dp[l][r][3]=dp[l][r-1][0]+4*4
  因为有3个和[r]相同，即可以消除4个所以加上4*4
** 得到初始化条件dp[l][r][k]=dp[l][r-1][0]+(k+1)*(k+1)
* 但是有可能在boxes[l]~boxes[r-1]中也存在和boxes[r]相同值的元素，有可能获得更大的积分和
  比如[l,l+1,···,i,···,r-1,r,值同r，值同r，值同r]，假设boxes[i]==boxes[r]
  那么可能先移除boxes[i+1]~boxes[r-1]，这样就能使原来的dp[l][r][3]的k=3变的更大，但是r变得更小，但是积分和更大
  因此就需要在boxes[l]~boxes[r-1]中找到boxes[i]==boxes[r]
** 这样子先移除boxes[i+1]~boxes[r-1]，这一部分的最大积分和是dp[i+1][r-1][0]
  移除之后是[l,l+1,···,i,值同i(原来是r)，值同i(原来是r+1)，值同i(原来是r+2)，值同i(原来是r+3)]
  剩下这部分是dp[l][i][k+1]
** 总和起来就是dp[l][r][k]=max(dp[l][r][k],dp[i+1][r-1][0]+dp[l][i][k+1])
* 最后的答案就是dp[0][boxes.size()-1][0]
*/
class Solution {
    int dp[100][100][100];
public:
    int removeBoxes(vector<int>& boxes) {
        int size=boxes.size();
        memset(dp,0,sizeof(dp));
        return get_dp(boxes,0,size-1,0);
    }
    int get_dp(vector<int> &boxes,int l,int r,int k)
    {
        if (l>r)
            return 0;
        //记忆化
        if (dp[l][r][k]!=0)
            return dp[l][r][k];
        //尽可能的缩小r可以让递归剪枝
        while (l<r && boxes.at(r)==boxes.at(r-1))
        {
            --r;
            ++k;
        }
        dp[l][r][k]=get_dp(boxes,l,r-1,0)+(k+1)*(k+1);
        for (int i=l;i<r;++i)
            if (boxes.at(i)==boxes.at(r))
                dp[l][r][k]=max(dp[l][r][k],get_dp(boxes,i+1,r-1,0)+get_dp(boxes,l,i,k+1));
        return dp[l][r][k];
    }
};
'''


# solutions

'''
方法一：动态规划
思路与算法

我们很容易陷入这样一个错误的思路：用 f(l, r)f(l,r) 来表示移除区间 [l, r][l,r] 内所有的盒子能得到的最大积分，然后去探索某一种移除盒子的策略来进行状态转移。而实际上，我们并不能直接使用起始节点和结束节点决定最大分数，因为这个分数并不只依赖于子序列，也依赖于之前的移动对当前数组的影响，这可能让最终的子序列不是一个连续的子串。比如 \{ 3, 4, 2, 4, 4 \}{3,4,2,4,4}，如果先把 22 移除，33 个 44 会合并在一起，对答案的贡献是 3^2 = 93 
2
 =9，如果先移除左右两边的 44 再移除 22 这里 33 个 44 的贡献就是 1^2 + 2^2 = 51 
2
 +2 
2
 =5，最优的办法当然是先取走 22，但是这样剩下的 33 个 44 其实并不是原串的某个连续子串。

那么正确的思路是什么呢？

我们可以换一种思路，用 f(l, r, k)f(l,r,k) 表示移除区间 [l, r][l,r] 的元素 a_l, a_{l + 1}, a_{l + 2} \cdots a_ra 
l
​	
 ,a 
l+1
​	
 ,a 
l+2
​	
 ⋯a 
r
​	
 加上该区间右边等于 a_ra 
r
​	
  的 kk 个元素组成的这个序列的最大积分。例如序列 \{ 6, 3, 6, 5, 6, 7, 6, 6, 8, 6 \}{6,3,6,5,6,7,6,6,8,6}，l = 1l=1（下标从 11 开始），r = 5r=5，那么 f(l, r, 3)f(l,r,3) 对应的元素就是 \{ {\color{red}[6, 3, 6, 5, 6]}, 7, {\color{red}6}, {\color{red}6}, 8, {\color{red}6} \}{[6,3,6,5,6],7,6,6,8,6} 中标记为红色的部分。f(l, r, k)f(l,r,k) 的定义是移除这个红色的序列获得的最大积分。请注意此时我们约定 77 和 88 已经先被移除，所以在这个状态下我们可以认为最后四个 66 是连续的，也就是说实际上待删除的序列是这样的：\{ [6, 3, 6, 5, 6], 6, 6, 6 \}{[6,3,6,5,6],6,6,6}，此时我们可以有这样一些策略来移除盒子：

\{ {\color{orange}[6, 3, 6, 5}, {\color{red} 6]}, 7, {\color{red}6, 6}, 8, {\color{red}6} \}{[6,3,6,5,6],7,6,6,8,6}，删除后面的四个 66，再删除前面的这个区间，这样获得的分数为 f(1, 4, 0) + 4^2f(1,4,0)+4 
2
 
\{ {\color{orange}[6, 3}, {\color{red}6]}, [5], {\color{red} 6}, 7, {\color{red}6, 6}, 8, {\color{red}6} \}{[6,3,6],[5],6,7,6,6,8,6}，删除一个单独的 a_4a 
4
​	
 （即 55），分数是 f(4, 4, 0)f(4,4,0)；然后问题就变成了删除区间 [1, 3][1,3] 以及这个区间后面和 a_3a 
3
​	
  相同的 44 个数，分数是 f(1, 3, 4)f(1,3,4)；这样获得的分数是 f(1, 3, 4) + f(4, 4, 0)f(1,3,4)+f(4,4,0)
\{ {\color{orange}[ }{\color{red}6]},[3, 6, 5], {\color{red} 6}, 7, {\color{red}6, 6}, 8, {\color{red}6} \}{[6],[3,6,5],6,7,6,6,8,6}，删除 a_2a 
2
​	
 、a_3a 
3
​	
 、a_4a 
4
​	
 ，分数为 f(2, 4, 0)f(2,4,0)；之后再删除区间 [1, 1][1,1] 和这个区间后和 a_1a 
1
​	
  相同的 44 个数，分数是 f(1, 1, 4)f(1,1,4)；这样获得的分数是 f(1, 1, 4) + f(2, 4, 0)f(1,1,4)+f(2,4,0)
这个就是我们转移的时候使用的策略，我们可以推导出这样的动态规划转移方程：

f(l, r, k) = \max \left\{ f(l, r - 1, 0) + (k + 1)^2, \max_{i = l}^{r - 1} \{ [f(l, i, k + 1) + f(i + 1, r - 1, 0)] \times { \color{red} \epsilon (a_i == a_r)} \} \right\}
f(l,r,k)=max{f(l,r−1,0)+(k+1) 
2
 , 
i=l
max
r−1
​	
 {[f(l,i,k+1)+f(i+1,r−1,0)]×ϵ(a 
i
​	
 ==a 
r
​	
 )}}

f(l, r - 1, 0) + (k + 1)^2f(l,r−1,0)+(k+1) 
2
  代表我们把 a_ra 
r
​	
  和后面的 kk 个数一起删除，再删除 [l, r - 1][l,r−1] 这个区间。也就是说，当我们删除 f(l, r, k)f(l,r,k) 对应的数字的时候，我们可以考虑先删除 a_ra 
r
​	
  和后面 kk 个与 a_ra 
r
​	
  相等的数，即一共 k + 1k+1 个数，得分为 (k+1)^2(k+1) 
2
 ，再删除 [l, r - 1][l,r−1] 这个区间，由于第 r - 1r−1 个位置后面所有的数字都删除了，所以这里不用继续考虑后面的数字中和 a_{r - 1}a 
r−1
​	
  相等的那些数字，所以这里的分数是 f(l, r - 1, 0)f(l,r−1,0)。

[f(l, i, k + 1) + f(i + 1, r - 1, 0)] \times { \color{red} \epsilon (a_i == a_r)}[f(l,i,k+1)+f(i+1,r−1,0)]×ϵ(a 
i
​	
 ==a 
r
​	
 ) 代表当 a_i (l \leq i < r)a 
i
​	
 (l≤i<r) 等于 a_ra 
r
​	
  的时候，考虑先删掉 [i + 1, r - 1][i+1,r−1] 这个区间，然后再删除 [l, i][l,i] 区间和后面的 k + 1k+1 个和 a_ra 
r
​	
  相等的数构成的序列，其中 \epsilon(x)ϵ(x) 为选择函数：

\epsilon(x) = \left \{ \begin{aligned} & 1 ,& x == {\rm True} & \\ & 0 ,& x == {\rm False} \end{aligned} \right .
ϵ(x)={ 
​	
  
1,
0,
​	
  
x==True
x==False
​	
  
 

这里我们只考虑和 a_ra 
r
​	
  相等的 a_ia 
i
​	
 ，因为一个序列 \{ a_l \cdots a_i \cdots a_r, x, x, x \}{a 
l
​	
 ⋯a 
i
​	
 ⋯a 
r
​	
 ,x,x,x}，当 a_r = xa 
r
​	
 =x 时，我们可以考虑先删除 [i, r - 1][i,r−1] 这个区间的元素，即 a_i, a_{i + 1}, \cdots, a_{r - 1}a 
i
​	
 ,a 
i+1
​	
 ,⋯,a 
r−1
​	
 ，我们把这些元素单独拿出来考虑，即不用考虑 r - 1r−1 后面和 a_{r - 1}a 
r−1
​	
  相等的元素（因为 a_ra 
r
​	
  和后面等于它的数字会在下一步中删除，而 a_{r}a 
r
​	
  后面其他的数字已经被删除），故这里的分数为 f(i, r - 1, 0)f(i,r−1,0)；接着这个问题就变成了删除区间 [l, i][l,i] 和 a_ra 
r
​	
  以及 a_ra 
r
​	
  后方和它相等的 kk 个数，因为 a_i = a_ra 
i
​	
 =a 
r
​	
 ，所以这个问题就是 [l, i][l,i] 区间和它的后方和 a_ia 
i
​	
  相等的 k + 1k+1 个数，这里的分数是 f(l, i, k + 1)f(l,i,k+1)。

这样我们就可以计算出 f(1, n, 0)f(1,n,0) 的值，即为答案。

我们不难写出这样的代码：

C++

class Solution {
public:
    int dp[100][100][100];

    int removeBoxes(vector<int>& boxes) {
        memset(dp, 0, sizeof dp);
        return calculatePoints(boxes, 0, boxes.size() - 1, 0);
    }

    int calculatePoints(vector<int>& boxes, int l, int r, int k) {
        if (l > r) return 0;
        if (dp[l][r][k] != 0) return dp[l][r][k];
        dp[l][r][k] = calculatePoints(boxes, l, r - 1, 0) + (k + 1) * (k + 1);
        for (int i = l; i < r; i++) {
            if (boxes[i] == boxes[r]) {
                dp[l][r][k] = max(dp[l][r][k], calculatePoints(boxes, l, i, k + 1) + calculatePoints(boxes, i + 1, r - 1, 0));
            }
        }
        return dp[l][r][k];
    }
};
在这份代码中，我们把 f(l, r, k)f(l,r,k) 初始化成 f(l, r - 1, 0) + (k + 1)^2f(l,r−1,0)+(k+1) 
2
 。我们可以做一个小小的优化。假设当前区间是这样的：\{ a_l, a_{l + 1} \cdots x, x, x, a_{r}, x, y, x, x \cdots \}{a 
l
​	
 ,a 
l+1
​	
 ⋯x,x,x,a 
r
​	
 ,x,y,x,x⋯}，此时如果 a_r = xa 
r
​	
 =x，那么初始化的时候 f(l, r, k) = f(l, r - 1, 0) + (k + 1)^2f(l,r,k)=f(l,r−1,0)+(k+1) 
2
 ，接下来的循环从 ll 到 r - 1r−1。我们观察到其实 a_ra 
r
​	
  前面还有若干个连续的和 a_ra 
r
​	
  相等的数，这些数可以和 a_ra 
r
​	
  及后面的 xx 作为一个整体，在这里我们可以初始化 f(l, r, k) = f(l, r - 3, 0) + (k + 3)^2f(l,r,k)=f(l,r−3,0)+(k+3) 
2
 。为什么可以这样初始化呢？这样初始化相当于把前面 33 个 xx 和 a_ra 
r
​	
  和后面的一坨 xx 捆绑到了一起，因为分开计算一定是没有合并计算优的，因为当 k >= 0k>=0 的时候 (k + 1 + 1 + 1) ^2 > (k + 1)^2 + (1 + 1) ^ 2 > (k + 1)^2 + 1^2 + 1^2(k+1+1+1) 
2
 >(k+1) 
2
 +(1+1) 
2
 >(k+1) 
2
 +1 
2
 +1 
2
 。

下面是优化的代码。

代码

C++JavaGolangC

func removeBoxes(boxes []int) int {
    dp := [100][100][100]int{}
    var calculatePoints func(boxes []int, l, r, k int) int
    calculatePoints = func(boxes []int, l, r, k int) int {
        if l > r {
            return 0
        }
        if dp[l][r][k] != 0 {
            return dp[l][r][k]
        }
        for r > l && boxes[r] == boxes[r - 1] {
            r--
            k++
        }
        dp[l][r][k] = calculatePoints(boxes, l, r - 1, 0) + (k + 1) * (k + 1)
        for i := l; i < r; i++ {
            if boxes[i] == boxes[r] {
                dp[l][r][k] = max(dp[l][r][k], calculatePoints(boxes, l, i, k + 1) + calculatePoints(boxes, i + 1, r - 1, 0))
            }
        }
        return dp[l][r][k]
    }
    return calculatePoints(boxes, 0, len(boxes) - 1, 0)
}

func max(x, y int) int {
    if x > y {
        return x
    }
    return y
}

复杂度分析

时间复杂度：O(n^4)O(n 
4
 )。最坏情况下每个 f(l, r, k)f(l,r,k) 被计算一次，每次状态转移需要 O(n)O(n) 的时间复杂度。
空间复杂度：O(n^3)O(n 
3
 )。\rm dpdp 数组的空间代价是 O(n^3)O(n 
3
 )，递归使用栈空间的代价为 O(n)O(n)。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/remove-boxes/solution/yi-chu-he-zi-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''