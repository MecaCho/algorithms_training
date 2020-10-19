'''
844. Backspace String Compare
Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".
Example 2:

Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".
Example 3:

Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".
Example 4:

Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".
Note:

1 <= S.length <= 200
1 <= T.length <= 200
S and T only contain lowercase letters and '#' characters.
Follow up:

Can you solve it in O(N) time and O(1) space?

844. 比较含退格的字符串
给定 S 和 T 两个字符串，当它们分别被输入到空白的文本编辑器后，判断二者是否相等，并返回结果。 # 代表退格字符。

注意：如果对空文本输入退格字符，文本继续为空。



示例 1：

输入：S = "ab#c", T = "ad#c"
输出：true
解释：S 和 T 都会变成 “ac”。
示例 2：

输入：S = "ab##", T = "c#d#"
输出：true
解释：S 和 T 都会变成 “”。
示例 3：

输入：S = "a##c", T = "#a#c"
输出：true
解释：S 和 T 都会变成 “c”。
示例 4：

输入：S = "a#c", T = "b"
输出：false
解释：S 会变成 “c”，但 T 仍然是 “b”。


提示：

1 <= S.length <= 200
1 <= T.length <= 200
S 和 T 只含有小写字母以及字符 '#'。


进阶：

你可以用 O(N) 的时间复杂度和 O(1) 的空间复杂度解决该问题吗？
'''


class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """

        def get_real(s):
            stack = []
            for i in range(len(s)):
                if s[i] == "#":
                    if stack and stack[-1] != "#":
                        stack.pop()
                else:
                    stack.append(s[i])
            return "".join(stack)

        return get_real(S) == get_real(T)


# solutions

'''
方法一：重构字符串
思路及算法

最容易想到的方法是将给定的字符串中的退格符和应当被删除的字符都去除，还原给定字符串的一般形式。然后直接比较两字符串是否相等即可。

具体地，我们用栈处理遍历过程，每次我们遍历到一个字符：

如果它是退格符，那么我们将栈顶弹出；

如果它是普通字符，那么我们将其压入栈中。

代码

C++JavaGolangPython3C

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def build(s: str) -> str:
            ret = list()
            for ch in s:
                if ch != "#":
                    ret.append(ch)
                elif ret:
                    ret.pop()
            return "".join(ret)
        
        return build(S) == build(T)
复杂度分析

时间复杂度：O(N+M)O(N+M)，其中 NN 和 MM 分别为字符串 SS 和 TT 的长度。我们需要遍历两字符串各一次。

空间复杂度：O(N+M)O(N+M)，其中 NN 和 MM 分别为字符串 SS 和 TT 的长度。主要为还原出的字符串的开销。

方法二：双指针
思路及算法

一个字符是否会被删掉，只取决于该字符后面的退格符，而与该字符前面的退格符无关。因此当我们逆序地遍历字符串，就可以立即确定当前字符是否会被删掉。

具体地，我们定义 \textit{skip}skip 表示当前待删除的字符的数量。每次我们遍历到一个字符：

若该字符为退格符，则我们需要多删除一个普通字符，我们让 \textit{skip}skip 加 11；

若该字符为普通字符：

若 \textit{skip}skip 为 00，则说明当前字符不需要删去；

若 \textit{skip}skip 不为 00，则说明当前字符需要删去，我们让 \textit{skip}skip 减 11。

这样，我们定义两个指针，分别指向两字符串的末尾。每次我们让两指针逆序地遍历两字符串，直到两字符串能够各自确定一个字符，然后将这两个字符进行比较。重复这一过程直到找到的两个字符不相等，或遍历完字符串为止。



代码

C++JavaGolangPython3C

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        i, j = len(S) - 1, len(T) - 1
        skipS = skipT = 0

        while i >= 0 or j >= 0:
            while i >= 0:
                if S[i] == "#":
                    skipS += 1
                    i -= 1
                elif skipS > 0:
                    skipS -= 1
                    i -= 1
                else:
                    break
            while j >= 0:
                if T[j] == "#":
                    skipT += 1
                    j -= 1
                elif skipT > 0:
                    skipT -= 1
                    j -= 1
                else:
                    break
            if i >= 0 and j >= 0:
                if S[i] != T[j]:
                    return False
            elif i >= 0 or j >= 0:
                return False
            i -= 1
            j -= 1
        
        return True
复杂度分析

时间复杂度：O(N+M)O(N+M)，其中 NN 和 MM 分别为字符串 SS 和 TT 的长度。我们需要遍历两字符串各一次。

空间复杂度：O(1)O(1)。对于每个字符串，我们只需要定义一个指针和一个计数器即可。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/backspace-string-compare/solution/bi-jiao-han-tui-ge-de-zi-fu-chuan-by-leetcode-solu/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''