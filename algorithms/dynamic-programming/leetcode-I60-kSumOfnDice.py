
'''
面试题60. n个骰子的点数
把n个骰子扔在地上，所有骰子朝上一面的点数之和为s。输入n，打印出s的所有可能的值出现的概率。



你需要用一个浮点数数组返回答案，其中第 i 个元素代表这 n 个骰子所能掷出的点数集合中第 i 小的那个的概率。



示例 1:

输入: 1
输出: [0.16667,0.16667,0.16667,0.16667,0.16667,0.16667]
示例 2:

输入: 2
输出: [0.02778,0.05556,0.08333,0.11111,0.13889,0.16667,0.13889,0.11111,0.08333,0.05556,0.02778]


限制：

1 <= n <= 11
'''




class Solution(object):
    def twoSum(self, n):
        """
        :type n: int
        :rtype: List[float]
        """
        # f(n,s)=f(n-1,s-1)+f(n-1,s-2)+f(n-1,s-3)+f(n-1,s-4)+f(n-1,s-5)+f(n-1,s-6)
        # dp = [0, 1,1,1,1,1,1]
        # # dp = [[1 for i in range(6)] for j i range(n)]
        # # for i in range(n, 6*n+1):
        # for k in range(6*n, 6*n):
        #     dp.append(0)
        #     for j in range(6):
        #         if n - j:

        #         dp[k] += dp[k-j]
        self.hash_map = [[None for j in range(6*n+1)] for i in range(n+1)]
        def get_count(n, k):
            if k > 6*n or k < n:
                return 0
            if n <= 1:
                return 1
            tmp = self.hash_map[n][k]
            if tmp is not None:
                return tmp
            count = 0
            for i in range(1, 7, 1):
                count += get_count(n-1, k-i)
            self.hash_map[n][k] = count
            return count

        dp = [1 for _ in range(n)]
        for i in range(n, 6*n+1):
            dp.append(1)
            dp[i] = get_count(n, i)

        res = []
        for i in range(n, 6*n+1):
            res.append(dp[i]*(float(1)/6**n))
        return res

class Solution1(object):
    def twoSum(self, n):
        """
        :type n: int
        :rtype: List[float]
        """
        hash_map = {}
        def get_count(n, k):
            if k > 6*n or k < n:
                return 0
            if n <= 1:
                hash_map[(n, k)] = 1
                return 1
            # tmp = self.hash_map[n][k]
            # if (n, k) in hash_map:
                # return hash_map[(n, k)]
            count = 0
            for i in range(1, 7, 1):
                if (n-1, k-i) not in hash_map:
                    count += get_count(n-1, k-i)
                else:
                    count += hash_map[(n-1, k-i)]
            hash_map[(n, k)] = count
            return count
        print(hash_map)

        dp = [1 for _ in range(n)]
        for i in range(n, 6*n+1):
            dp.append(1)
            dp[i] = get_count(n, i)
        print(hash_map)

        res = []
        for i in range(n, 6*n+1):
            res.append(hash_map[(n, i)]*(float(1)/6**n))
        return res

'''
动态规划
解题思路
n个骰子，每个骰子6个面，总情况数为6^n6 
n
 。
设F(n,s)F(n,s)为当骰子数为n，和为s的情况数量。
当n=1时，F(1,s)=1,其中s=1,2,3,4,5,6当n=1时，F(1,s)=1,其中s=1,2,3,4,5,6
当n\ge2时，F(n,s)=F(n-1,s-1)+F(n-1,s-2)+F(n-1,s-3)+F(n-1,s-4)+F(n-1,s-5)+F(n-1,s-6)当n≥2时，F(n,s)=F(n−1,s−1)+F(n−1,s−2)+F(n−1,s−3)+F(n−1,s−4)+F(n−1,s−5)+F(n−1,s−6)
或者更准确的：F(n,s)=\sum_{d=1}^{min(6,s-n+1)} F(n-1,s-d)F(n,s)=∑ 
d=1
min(6,s−n+1)
​	
 F(n−1,s−d)，为了使得s-d\ge n-1s−d≥n−1

时间复杂度：O(n^2)O(n 
2
 )
空间复杂度：O((n+1)(6n+1))=O(n^2)O((n+1)(6n+1))=O(n 
2
 )
由于n\le 11n≤11，时间是不算长的
由于6^{11}=3627970566 
11
 =362797056没有超出int范围，故可以放心用int

最后概率为P(n,s)=\frac{F(n,s)}{6^n}P(n,s)= 
6 
n
 
F(n,s)
​	
 

代码
class Solution {
    public double[] twoSum(int n) {
        int [][]dp = new int[n+1][6*n+1];
        //边界条件
        for(int s=1;s<=6;s++)dp[1][s]=1;
        for(int i=2;i<=n;i++){
            for(int s=i;s<=6*i;s++){
                //求dp[i][s]
                for(int d=1;d<=6;d++){
                    if(s-d<i-1)break;//为0了
                    dp[i][s]+=dp[i-1][s-d];
                }
            }
        }
        double total = Math.pow((double)6,(double)n);
        double[] ans = new double[5*n+1];
        for(int i=n;i<=6*n;i++){
            ans[i-n]=((double)dp[n][i])/total;
        }
        return ans;
    }
}
'''