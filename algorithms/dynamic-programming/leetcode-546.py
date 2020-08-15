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