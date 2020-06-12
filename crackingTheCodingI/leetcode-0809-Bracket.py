'''
面试题 08.09. 括号
括号。设计一种算法，打印n对括号的所有合法的（例如，开闭一一对应）组合。

说明：解集不能包含重复的子集。

例如，给出 n = 3，生成结果为：

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

面试题 08.09. Bracket LCCI
Implement an algorithm to print all valid (e.g., properly opened and closed) combinations of n pairs of parentheses.

Note: The result set should not contain duplicated subsets.

For example, given n = 3, the result should be:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
'''



class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # self.vals = []

        # def bk(res, l, r):
        #     # print(res, l, r)
        #     if l == 0 and r == 0:

        #         val = "".join(res)
        #         self.vals.append(val)
        #     else:
        #         new_res = res[:]
        #         if l > 0:
        #             bk(new_res+["("], l-1, r)
        #         if r > l and r > 0:
        #             bk(new_res + [")"], l, r-1)

        # bk([], n, n)

        # return self.vals

        if n == 0:
            return []
        if n == 1:
            return ["()"]

        vals = self.generateParenthesis(n-1)

        res = []
        for i in range(len(vals)):
            for j in range(len(vals[i])):
                new_p = vals[i][:j] + "()" + vals[i][j:]
                if new_p not in res:
                    res.append(new_p)

        return res

# tips

'''
尝试简单构建法。
假设我们有编写两对括号的所有有效方法。怎么用这个来得到编写三对括号的所有有效方法？
我们可以通过向两对括号的列表中添加第三对括号来生成三对括号的组合。我们要在其前面、周围、后面添加第三对括号。即()、()、()。这样有效吗？
前面提示给出的解法存在的问题在于可能有重复的值。我们可以通过使用散列表来消除这种情况。
或者，可以考虑通过移动字符串并在每个步骤添加左侧和右侧的括号来完成此操作。这会消除重复吗？如何知道能否添加左侧或右侧的括号？

在每一步添加一个左或右括号将消除重复。每个子字符串在每一步都是各不相同的。因此，总字符串将是独一无二的。
我们可以通过计算左、右括号数保证这个字符串是有效的。添加一个左括号，直到括号的总数成对，这样字符串总是有效的。只要count(left parens) <= count(right parens)，就可以添加一个右括号。
'''