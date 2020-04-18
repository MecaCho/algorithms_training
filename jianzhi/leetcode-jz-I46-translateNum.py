
'''
面试题46. 把数字翻译成字符串
给定一个数字，我们按照如下规则把它翻译为字符串：0 翻译成 “a” ，1 翻译成 “b”，……，11 翻译成 “l”，……，25 翻译成 “z”。一个数字可能有多个翻译。请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。



示例 1:

输入: 12258
输出: 5
解释: 12258有5种不同的翻译，分别是"bccfi", "bwfi", "bczi", "mcfi"和"mzi"


提示：

0 <= num < 231
'''


class Solution(object):
    def translateNum(self, num):
        """
        :type num: int
        :rtype: int
        """
        self.res_list = []
        vals = [int(i) for i in str(num)]
        a_num = ord("a")
        def dfs(s=None, res=""):
            if not s:
                self.res_list.append(res)
            else:
                tmp = s.pop(0)
                dfs(s[:], res+chr(a_num+tmp))
                if s:
                    tmp = tmp*10 + s.pop(0)
                    if 10 <= tmp <=25:
                        dfs(s[:], res+chr(a_num+tmp))
        dfs(vals, "")
        return len(self.res_list)


# 动态规划
class Solution1(object):
    def translateNum(self, num):
        """
        :type num: int
        :rtype: int
        """

        num_list = [i for i in str(num)]
        dp = [1 for i in range(len(num_list))]
        for i in range(1, len(num_list)):
            if 10 <= int(num_list[i - 1]) * 10 + int(num_list[i]) <= 25:
                dp[i] = dp[i - 1] + dp[i - 2]
            else:
                dp[i] = dp[i - 1]
        # print(dp)
        return dp[-1]
        # self.res_list = []
        # vals = [int(i) for i in str(num)]
        # a_num = ord("a")
        # def dfs(s=None, res=""):
        #     if not s:
        #         self.res_list.append(res)
        #     else:
        #         tmp = s.pop(0)
        #         dfs(s[:], res+chr(a_num+tmp))
        #         if s:
        #             tmp = tmp*10 + s.pop(0)
        #             if 10 <= tmp <=25:
        #                 dfs(s[:], res+chr(a_num+tmp))
        # dfs(vals, "")
        # return len(self.res_list)
