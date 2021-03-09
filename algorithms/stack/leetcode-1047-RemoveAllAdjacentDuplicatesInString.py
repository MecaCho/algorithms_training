# encoding=utf8

'''
1047. Remove All Adjacent Duplicates In String
Given a string S of lowercase letters, a duplicate removal consists of choosing two adjacent and equal letters, and removing them.

We repeatedly make duplicate removals on S until we no longer can.

Return the final string after all such duplicate removals have been made.  It is guaranteed the answer is unique.



Example 1:

Input: "abbaca"
Output: "ca"
Explanation:
For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".


Note:

1 <= S.length <= 20000
S consists only of English lowercase letters.


1047. 删除字符串中的所有相邻重复项
给出由小写字母组成的字符串 S，重复项删除操作会选择两个相邻且相同的字母，并删除它们。

在 S 上反复执行重复项删除操作，直到无法继续删除。

在完成所有重复项删除操作后返回最终的字符串。答案保证唯一。



示例：

输入："abbaca"
输出："ca"
解释：
例如，在 "abbaca" 中，我们可以删除 "bb" 由于两字母相邻且相同，这是此时唯一可以执行删除操作的重复项。之后我们得到字符串 "aaca"，其中又只有 "aa" 可以执行重复项删除操作，所以最后的字符串为 "ca"。


提示：

1 <= S.length <= 20000
S 仅由小写英文字母组成。
'''


class Solution(object):
    def removeDuplicates(self, S):
        """
        :type S: str
        :rtype: str
        """
        stack = []
        for i in range(len(S)):
            if not stack or stack[-1] != S[i]:
                stack.append(S[i])
            else:
                stack.pop()

        return "".join(stack)


# solutions

'''
方法一：栈
充分理解题意后，我们可以发现，当字符串中同时有多组相邻重复项时，我们无论是先删除哪一个，都不会影响最终的结果。因此我们可以从左向右顺次处理该字符串。

而消除一对相邻重复项可能会导致新的相邻重复项出现，如从字符串 \text{abba}abba 中删除 \text{bb}bb 会导致出现新的相邻重复项 \text{aa}aa 出现。因此我们需要保存当前还未被删除的字符。一种显而易见的数据结构呼之欲出：栈。我们只需要遍历该字符串，如果当前字符和栈顶字符相同，我们就贪心地将其消去，否则就将其入栈即可。

代码

在下面的 \texttt{C++}C++ 代码中，由于 \texttt{std::string}std::string 类本身就提供了类似「入栈」和「出栈」的接口，因此我们直接将需要被返回的字符串作为栈即可。对于其他的语言，如果字符串类没有提供相应的接口，则需要在遍历完成字符串后，使用栈中的字符显式地构造出需要被返回的字符串。

C++JavaJavaScriptPython3GolangC

class Solution:
    def removeDuplicates(self, S: str) -> str:
        stk = list()
        for ch in S:
            if stk and stk[-1] == ch:
                stk.pop()
            else:
                stk.append(ch)
        return "".join(stk)
复杂度分析

时间复杂度：O(n)O(n)，其中 nn 是字符串的长度。我们只需要遍历该字符串一次。

空间复杂度：O(n)O(n) 或 O(1)O(1)，取决于使用的语言提供的字符串类是否提供了类似「入栈」和「出栈」的接口。注意返回值不计入空间复杂度。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/remove-all-adjacent-duplicates-in-string/solution/shan-chu-zi-fu-chuan-zhong-de-suo-you-xi-4ohr/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
