# encoding=utf8

'''
1190. Reverse Substrings Between Each Pair of Parentheses

You are given a string s that consists of lower case English letters and brackets. 

Reverse the strings in each pair of matching parentheses, starting from the innermost one.

Your result should not contain any brackets.

 

Example 1:

Input: s = "(abcd)"
Output: "dcba"
Example 2:

Input: s = "(u(love)i)"
Output: "iloveu"
Explanation: The substring "love" is reversed first, then the whole string is reversed.
Example 3:

Input: s = "(ed(et(oc))el)"
Output: "leetcode"
Explanation: First, we reverse the substring "oc", then "etco", and finally, the whole string.
Example 4:

Input: s = "a(bcdefghijkl(mno)p)q"
Output: "apmnolkjihgfedcbq"
 

Constraints:

0 <= s.length <= 2000
s only contains lower case English characters and parentheses.
It's guaranteed that all parentheses are balanced.

1190. 反转每对括号间的子串

给出一个字符串 s（仅含有小写英文字母和括号）。

请你按照从括号内到外的顺序，逐层反转每对匹配括号中的字符串，并返回最终的结果。

注意，您的结果中 不应 包含任何括号。

 

示例 1：

输入：s = "(abcd)"
输出："dcba"
示例 2：

输入：s = "(u(love)i)"
输出："iloveu"
示例 3：

输入：s = "(ed(et(oc))el)"
输出："leetcode"
示例 4：

输入：s = "a(bcdefghijkl(mno)p)q"
输出："apmnolkjihgfedcbq"
 

提示：

0 <= s.length <= 2000
s 中只有小写英文字母和括号
我们确保所有括号都是成对出现的
'''


class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        while '(' in s:
            s = re.sub(r'\(([^()]*)\)', lambda x:x.group(1)[::-1], s)
        return s

# solutions

'''
方法一：栈
思路及算法

本题要求按照从括号内到外的顺序进行处理。如字符串 \texttt{(u(love)i)}(u(love)i)，首先处理内层括号，变为 \texttt{(uevoli)}(uevoli)，然后处理外层括号，变为 \texttt{iloveu}iloveu。

对于括号序列相关的题目，通用的解法是使用递归或栈。本题中我们将使用栈解决。

我们从左到右遍历该字符串，使用字符串 \textit{str}str 记录当前层所遍历到的小写英文字母。对于当前遍历的字符：

如果是左括号，将 \textit{str}str 插入到栈中，并将 \textit{str}str 置为空，进入下一层；

如果是右括号，则说明遍历完了当前层，需要将 \textit{str}str 反转，返回给上一层。具体地，将栈顶字符串弹出，然后将反转后的 \textit{str}str 拼接到栈顶字符串末尾，将结果赋值给 \textit{str}str。

如果是小写英文字母，将其加到 \textit{str}str 末尾。

注意到我们仅在遇到右括号时才进行字符串处理，这样可以保证我们是按照从括号内到外的顺序处理字符串。

代码

C++JavaC#JavaScriptGolangC

func reverseParentheses(s string) string {
    stack := [][]byte{}
    str := []byte{}
    for i := range s {
        if s[i] == '(' {
            stack = append(stack, str)
            str = []byte{}
        } else if s[i] == ')' {
            for j, n := 0, len(str); j < n/2; j++ {
                str[j], str[n-1-j] = str[n-1-j], str[j]
            }
            str = append(stack[len(stack)-1], str...)
            stack = stack[:len(stack)-1]
        } else {
            str = append(str, s[i])
        }
    }
    return string(str)
}
复杂度分析

时间复杂度：O(n^2)O(n 
2
 )，其中 nn 为字符串的长度。栈的最大深度为 O(n)O(n)，每一层处理的时间复杂度主要为反转的时间复杂度，为 O(n)O(n)，因此总时间复杂度为 O(n^2)O(n 
2
 )。

空间复杂度：O(n)O(n)，其中 nn 为字符串的长度。对于任意时刻，字符串中的任意一个字符至多只被栈中的一个位置包含一次。

方法二：预处理括号
思路及算法

我们可以将括号的反转理解为逆序地遍历括号，如下图：



第一步我们向右移动到左括号，此时我们跳跃到该左括号对应的右括号（进入了更深一层）；
第二到第三步我们在括号内部向左移动（完成了更深层的遍历）；
第四步我们向左移动到左括号，此时我们跳跃到该左括号对应的右括号（返回到上一层）；
第五步我们在括号外向右移动（继续遍历）。
读者们可以自行尝试模拟两层乃至多层括号嵌套的移动方案，规律可以从当前的单层括号中总结出来。

假设我们沿着某个方向移动，此时遇到了括号，那么我们只需要首先跳跃到该括号对应的另一个括号所在处，然后改变我们的移动方向即可。这个方案同时适用于遍历时进入更深一层，以及完成当前层的遍历后返回到上一层的方案。

在实际代码中，我们需要预处理出每一个括号对应的另一个括号所在的位置，这一部分我们可以使用栈解决。当我们预处理完成后，即可在线性时间内完成遍历，遍历的字符串顺序即为反转后的字符串。

代码

C++JavaC#JavaScriptGolangC

func reverseParentheses(s string) string {
    n := len(s)
    pair := make([]int, n)
    stack := []int{}
    for i, b := range s {
        if b == '(' {
            stack = append(stack, i)
        } else if b == ')' {
            j := stack[len(stack)-1]
            stack = stack[:len(stack)-1]
            pair[i], pair[j] = j, i
        }
    }

    ans := []byte{}
    for i, step := 0, 1; i < n; i += step {
        if s[i] == '(' || s[i] == ')' {
            i = pair[i]
            step = -step
        } else {
            ans = append(ans, s[i])
        }
    }
    return string(ans)
}
复杂度分析

时间复杂度：O(n)O(n)，其中 nn 为字符串的长度。预处理出括号的对应关系的序列的时间复杂度为 O(n)O(n)，遍历字符串的时间复杂度同样为 O(n)O(n)。

空间复杂度：O(n)O(n)，其中 nn 为字符串的长度。栈的大小不会超过 nn，以及我们需要 O(n)O(n) 的空间记录括号的对应关系。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/reverse-substrings-between-each-pair-of-parentheses/solution/fan-zhuan-mei-dui-gua-hao-jian-de-zi-chu-gwpv/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''

