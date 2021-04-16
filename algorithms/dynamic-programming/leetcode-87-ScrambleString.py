# encoding=utf8

'''
87. Scramble String
We can scramble a string s to get a string t using the following algorithm:

If the length of the string is 1, stop.
If the length of the string is > 1, do the following:
Split the string into two non-empty substrings at a random index, i.e., if the string is s, divide it to x and y where s = x + y.
Randomly decide to swap the two substrings or to keep them in the same order. i.e., after this step, s may become s = x + y or s = y + x.
Apply step 1 recursively on each of the two substrings x and y.
Given two strings s1 and s2 of the same length, return true if s2 is a scrambled string of s1, otherwise, return false.



Example 1:

Input: s1 = "great", s2 = "rgeat"
Output: true
Explanation: One possible scenario applied on s1 is:
"great" --> "gr/eat" // divide at random index.
"gr/eat" --> "gr/eat" // random decision is not to swap the two substrings and keep them in order.
"gr/eat" --> "g/r / e/at" // apply the same algorithm recursively on both substrings. divide at ranom index each of them.
"g/r / e/at" --> "r/g / e/at" // random decision was to swap the first substring and to keep the second substring in the same order.
"r/g / e/at" --> "r/g / e/ a/t" // again apply the algorithm recursively, divide "at" to "a/t".
"r/g / e/ a/t" --> "r/g / e/ a/t" // random decision is to keep both substrings in the same order.
The algorithm stops now and the result string is "rgeat" which is s2.
As there is one possible scenario that led s1 to be scrambled to s2, we return true.
Example 2:

Input: s1 = "abcde", s2 = "caebd"
Output: false
Example 3:

Input: s1 = "a", s2 = "a"
Output: true


Constraints:

s1.length == s2.length
1 <= s1.length <= 30
s1 and s2 consist of lower-case English letters.


87. 扰乱字符串
使用下面描述的算法可以扰乱字符串 s 得到字符串 t ：
如果字符串的长度为 1 ，算法停止
如果字符串的长度 > 1 ，执行下述步骤：
在一个随机下标处将字符串分割成两个非空的子字符串。即，如果已知字符串 s ，则可以将其分成两个子字符串 x 和 y ，且满足 s = x + y 。
随机 决定是要「交换两个子字符串」还是要「保持这两个子字符串的顺序不变」。即，在执行这一步骤之后，s 可能是 s = x + y 或者 s = y + x 。
在 x 和 y 这两个子字符串上继续从步骤 1 开始递归执行此算法。
给你两个 长度相等 的字符串 s1 和 s2，判断 s2 是否是 s1 的扰乱字符串。如果是，返回 true ；否则，返回 false 。



示例 1：

输入：s1 = "great", s2 = "rgeat"
输出：true
解释：s1 上可能发生的一种情形是：
"great" --> "gr/eat" // 在一个随机下标处分割得到两个子字符串
"gr/eat" --> "gr/eat" // 随机决定：「保持这两个子字符串的顺序不变」
"gr/eat" --> "g/r / e/at" // 在子字符串上递归执行此算法。两个子字符串分别在随机下标处进行一轮分割
"g/r / e/at" --> "r/g / e/at" // 随机决定：第一组「交换两个子字符串」，第二组「保持这两个子字符串的顺序不变」
"r/g / e/at" --> "r/g / e/ a/t" // 继续递归执行此算法，将 "at" 分割得到 "a/t"
"r/g / e/ a/t" --> "r/g / e/ a/t" // 随机决定：「保持这两个子字符串的顺序不变」
算法终止，结果字符串和 s2 相同，都是 "rgeat"
这是一种能够扰乱 s1 得到 s2 的情形，可以认为 s2 是 s1 的扰乱字符串，返回 true
示例 2：

输入：s1 = "abcde", s2 = "caebd"
输出：false
示例 3：

输入：s1 = "a", s2 = "a"
输出：true


提示：

s1.length == s2.length
1 <= s1.length <= 30
s1 和 s2 由小写英文字母组成
'''

# python3
'''
class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        @cache
        def dfs(i1: int, i2: int, length: int) -> bool:
            """
            第一个字符串从 i1 开始，第二个字符串从 i2 开始，子串的长度为 length，是否和谐
            """

            # 判断两个子串是否相等
            if s1[i1:i1 + length] == s2[i2:i2 + length]:
                return True

            # 判断是否存在字符 c 在两个子串中出现的次数不同
            if Counter(s1[i1:i1 + length]) != Counter(s2[i2:i2 + length]):
                return False

            # 枚举分割位置
            for i in range(1, length):
                # 不交换的情况
                if dfs(i1, i2, i) and dfs(i1 + i, i2 + i, length - i):
                    return True
                # 交换的情况
                if dfs(i1, i2 + length - i, i) and dfs(i1 + i, i2, length - i):
                    return True

            return False

        ans = dfs(0, 0, len(s1))
        dfs.cache_clear()
        return ans
'''

from functools import lru_cache
from collections import Counter
class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """

        @lru_cache()
        def dfs(i1, i2, length):
            """
            第一个字符串从 i1 开始，第二个字符串从 i2 开始，子串的长度为 length，是否和谐
            """

            # 判断两个子串是否相等
            if s1[i1:i1 + length] == s2[i2:i2 + length]:
                return True

            # 判断是否存在字符 c 在两个子串中出现的次数不同
            if Counter(s1[i1:i1 + length]) != Counter(s2[i2:i2 + length]):
                return False

            # 枚举分割位置
            for i in range(1, length):
                # 不交换的情况
                if dfs(i1, i2, i) and dfs(i1 + i, i2 + i, length - i):
                    return True
                # 交换的情况
                if dfs(i1, i2 + length - i, i) and dfs(i1 + i, i2, length - i):
                    return True

            return False

        ans = dfs(0, 0, len(s1))
        dfs.cache_clear()
        return ans


# solutions

'''
方法一：动态规划
思路与算法

显然「扰乱字符串」的关系是具有对称性的，即如果 s_1s 
1
​	
  是 s_2s 
2
​	
  的扰乱字符串，那么 s_2s 
2
​	
  也是 s_1s 
1
​	
  的扰乱字符串。为了叙述方便，我们称这种情况下，s_1s 
1
​	
  和 s_2s 
2
​	
  是「和谐」的。

那么如何判断 s_1s 
1
​	
  和 s_2s 
2
​	
  是否「和谐」呢？我们首先可以想到几个简单的判断方法：

如果 s_1 = s_2s 
1
​	
 =s 
2
​	
 ，那么它们是「和谐」的；

如果 s_1s 
1
​	
  和 s_2s 
2
​	
  的长度不同，那么它们一定不是「和谐」的；

如果 s_1s 
1
​	
  中某个字符 cc 出现了 x_1x 
1
​	
  次，而 cc 在 s_2s 
2
​	
  中出现了 x_2x 
2
​	
  次，且 x_1 \neq x_2x 
1
​	
  

​	
 =x 
2
​	
 ，那么它们一定不是「和谐」的。这是因为任意操作都不会改变一个字符串中的字符种类以及数量。

那么对于剩下的情况，我们该如何判断呢？我们可以从 s_1s 
1
​	
  的分割方法入手。假设 s_1s 
1
​	
  作为根节点时被分割成了 l(s_1)l(s 
1
​	
 ) 以及 r(s_1)r(s 
1
​	
 ) 两个子串，那么：

如果 l(s_1)l(s 
1
​	
 ) 和 r(s_1)r(s 
1
​	
 ) 没有被交换，那么 s_2s 
2
​	
  需要存在一种分割方法 s_2 = l(s_2) + r(s_2)s 
2
​	
 =l(s 
2
​	
 )+r(s 
2
​	
 )，使得 l(s_1)l(s 
1
​	
 ) 和 l(s_2)l(s 
2
​	
 ) 是「和谐」的，并且 r(s_1)r(s 
1
​	
 ) 和 r(s_2)r(s 
2
​	
 ) 也是「和谐」的；

如果 l(s_1)l(s 
1
​	
 ) 和 r(s_1)r(s 
1
​	
 ) 被交换了，那么 s_2s 
2
​	
  需要存在一种分割方法 s_2 = l(s_2) + r(s_2)s 
2
​	
 =l(s 
2
​	
 )+r(s 
2
​	
 )，使得 l(s_1)l(s 
1
​	
 ) 和 r(s_2)r(s 
2
​	
 ) 是「和谐」的，并且 r(s_1)r(s 
1
​	
 ) 和 l(s_2)l(s 
2
​	
 ) 也是「和谐」的。



这样一来，我们就把原本需要解决的问题划分成了两个本质相同，但规模更小的子问题，因此可以考虑使用动态规划解决。

设 f(s_1, s_2)f(s 
1
​	
 ,s 
2
​	
 ) 表示 s_1s 
1
​	
  和 s_2s 
2
​	
  是否「和谐」，那么我们可以写出状态转移方程：

f(s_1, s_2) = \begin{cases} \text{True}, & \quad s_1=s_2 \\ \text{False}, & \quad 存在某个字符~c，它在~s_1~和~s_2~中的出现次数不同 \\ \end{cases}
f(s 
1
​	
 ,s 
2
​	
 )={ 
True,
False,
​	
  
s 
1
​	
 =s 
2
​	
 
存在某个字符 c，它在 s 
1
​	
  和 s 
2
​	
  中的出现次数不同
​	
 

因为题目保证给定的原始字符串的长度相同，因此我们只需要判断上面的两种情况。如果 s_1s 
1
​	
  和 s_2s 
2
​	
  不符合这两种情况，那么我们需要枚举分割点。

设 s_1s 
1
​	
  和 s_2s 
2
​	
  的长度为 nn，我们用 s_1(x, y)s 
1
​	
 (x,y) 表示从 s_1s 
1
​	
  从第 xx 个字符（从 00 开始编号）开始，长度为 yy 的子串。由于分割出的两个字符串不能为空串，那么其中一个字符串就是 s_1(0, i)s 
1
​	
 (0,i)，另一个字符串是 s_1(i, n-i)s 
1
​	
 (i,n−i)。

对于 l(s_1)l(s 
1
​	
 ) 和 r(s_1)r(s 
1
​	
 ) 没有被交换的情况，s_2s 
2
​	
  同样需要被分为 s_2(0, i)s 
2
​	
 (0,i) 以及 s_2(i, n-i)s 
2
​	
 (i,n−i)，否则长度不同的字符串是不可能「和谐」的。因此我们可以写出状态转移方程：

f(s_1, s_2) = \bigvee_{i=1}^{n-1} \big( f(s_1(0, i), s_2(0, i)) \wedge f(s_1(i, n-i), s_2(i, n-i)) \big)
f(s 
1
​	
 ,s 
2
​	
 )= 
i=1
⋁
n−1
​	
 (f(s 
1
​	
 (0,i),s 
2
​	
 (0,i))∧f(s 
1
​	
 (i,n−i),s 
2
​	
 (i,n−i)))

其中 \wedge∧ 表示与运算，即 s_1s 
1
​	
  和 s_2s 
2
​	
  分割出的两对字符串都要是「和谐」的；\vee∨ 表示或运算，即只要有一种满足要求的分割方法，s_1s 
1
​	
  和 s_2s 
2
​	
  就是和谐的。

对于 l(s_1)l(s 
1
​	
 ) 和 r(s_1)r(s 
1
​	
 ) 被交换的情况，s_2s 
2
​	
  需要被分为 s_2(0, n-i)s 
2
​	
 (0,n−i) 以及 s_2(n-i, i)s 
2
​	
 (n−i,i)，这样对应的长度才会相同。因此我们可以写出状态转移方程：

f(s_1, s_2) = \bigvee_{i=1}^{n-1} \big( f(s_1(0, i), s_2(n-i, i)) \wedge f(s_1(i, n-i), s_2(0, n-i)) \big)
f(s 
1
​	
 ,s 
2
​	
 )= 
i=1
⋁
n−1
​	
 (f(s 
1
​	
 (0,i),s 
2
​	
 (n−i,i))∧f(s 
1
​	
 (i,n−i),s 
2
​	
 (0,n−i)))

我们将上面两种状态转移方程用 \vee∨ 或运算拼在一起，即可得到最终的状态转移方程。

细节

细节部分比较长，希望读者仔细阅读，否则写出来的代码可能会较为复杂，或者使用较多不必要的空间。

在进行状态转移时，我们需要先计算出较短的字符串对应的 ff 值，再去转移计算出较长的字符串对应的 ff 值，这是因为我们需要保证在计算 f(s_1, s_2)f(s 
1
​	
 ,s 
2
​	
 ) 时，所有它们的子串对应的状态都需要被计算过。因此，如果我们使用常规的动态规划方法编写代码，可能会受到计算顺序的困扰，使得代码冗长。

而我们可以考虑使用「记忆化搜索」自顶向下地进行动态规划，这样我们只需要用题目中给定的两个原始字符串开始，递归地计算所有的 ff 值，而无需考虑计算顺序。

由于我们使用记忆化搜索，因此我们需要把 s_1s 
1
​	
  和 s_2s 
2
​	
  作为参数传入记忆化搜索使用的递归函数。这样一来，在递归传递参数的过程中，会使用到大量字符串的切片、拷贝等操作，使得时空复杂度不那么优。本题中，由于给定原始字符串的长度不超过 3030，因此不会产生太大的影响，但我们还是要尽可能对代码进行优化。

一种通用的优化方法是，我们将状态变更为 f(i_1, i_2, \textit{length})f(i 
1
​	
 ,i 
2
​	
 ,length)，表示第一个字符串是原始字符串从第 i_1i 
1
​	
  个字符开始，长度为 \textit{length}length 的子串，第二个字符串是原始字符串从第 i_2i 
2
​	
  个字符开始，长度为 \textit{length}length 的子串。可以发现，我们只是改变了表达 s_1s 
1
​	
  和 s_2s 
2
​	
  的方式，但此时我们只需要在递归时传递三个整数类型的变量，省去了字符串的操作；

代码

C++JavaPython3GolangCJavaScript

func isScramble(s1, s2 string) bool {
    n := len(s1)
    dp := make([][][]int8, n)
    for i := range dp {
        dp[i] = make([][]int8, n)
        for j := range dp[i] {
            dp[i][j] = make([]int8, n+1)
            for k := range dp[i][j] {
                dp[i][j][k] = -1
            }
        }
    }

    // 第一个字符串从 i1 开始，第二个字符串从 i2 开始，子串的长度为 length
    // 和谐返回 1，不和谐返回 0
    var dfs func(i1, i2, length int) int8
    dfs = func(i1, i2, length int) (res int8) {
        d := &dp[i1][i2][length]
        if *d != -1 {
            return *d
        }
        defer func() { *d = res }()

        // 判断两个子串是否相等
        x, y := s1[i1:i1+length], s2[i2:i2+length]
        if x == y {
            return 1
        }

        // 判断是否存在字符 c 在两个子串中出现的次数不同
        freq := [26]int{}
        for i, ch := range x {
            freq[ch-'a']++
            freq[y[i]-'a']--
        }
        for _, f := range freq[:] {
            if f != 0 {
                return 0
            }
        }

        // 枚举分割位置
        for i := 1; i < length; i++ {
            // 不交换的情况
            if dfs(i1, i2, i) == 1 && dfs(i1+i, i2+i, length-i) == 1 {
                return 1
            }
            // 交换的情况
            if dfs(i1, i2+length-i, i) == 1 && dfs(i1+i, i2, length-i) == 1 {
                return 1
            }
        }

        return 0
    }
    return dfs(0, 0, n) == 1
}
复杂度分析

时间复杂度：O(n^4)O(n 
4
 )，其中 nn 是给定的原始字符串的长度。动态规划中的状态 f(i_1, i_2, \textit{length})f(i 
1
​	
 ,i 
2
​	
 ,length) 有 33 个维度，对于每一个状态，我们需要 O(n)O(n) 枚举分割位置，因此总时间复杂度为 O(n^4)O(n 
4
 )。

空间复杂度：O(n^3)O(n 
3
 )，即为存储所有动态规划状态需要的空间。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/scramble-string/solution/rao-luan-zi-fu-chuan-by-leetcode-solutio-8r9t/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
