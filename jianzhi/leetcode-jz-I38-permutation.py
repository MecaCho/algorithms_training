
'''
面试题38. 字符串的排列
输入一个字符串，打印出该字符串中字符的所有排列。



你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。



示例:

输入：s = "abc"
输出：["abc","acb","bac","bca","cab","cba"]


限制：

1 <= s 的长度 <= 8
'''



class Solution(object):
    def permutation(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        self.res = []
        s_list = list(s)
        length = len(s_list)
        def dfs(vals, res):
            if not vals:
                self.res.append(res)
            else:
                for i in range(len(vals)):
                    tmp = vals[:i] + vals[i+1:]
                    dfs(tmp, res+vals[i])
        dfs(s_list, "")
        return list(set(self.res))
