
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
