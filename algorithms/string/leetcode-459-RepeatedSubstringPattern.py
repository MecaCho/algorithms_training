'''
459. Repeated Substring Pattern
Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.



Example 1:

Input: "abab"
Output: True
Explanation: It's the substring "ab" twice.
Example 2:

Input: "aba"
Output: False
Example 3:

Input: "abcabcabcabc"
Output: True
Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)

459. 重复的子字符串
给定一个非空的字符串，判断它是否可以由它的一个子串重复多次构成。给定的字符串只含有小写英文字母，并且长度不超过10000。

示例 1:

输入: "abab"

输出: True

解释: 可由子字符串 "ab" 重复两次构成。
示例 2:

输入: "aba"

输出: False
示例 3:

输入: "abcabcabcabc"

输出: True

解释: 可由子字符串 "abc" 重复四次构成。 (或者子字符串 "abcabc" 重复两次构成。)

'''


class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return s in (s+s)[1:-1]


# solutions

'''
方法一：枚举
思路与算法

如果一个长度为 nn 的字符串 ss 可以由它的一个长度为 n'n 
′
  的子串 s's 
′
  重复多次构成，那么：

nn 一定是 n'n 
′
  的倍数；

s's 
′
  一定是 ss 的前缀；

对于任意的 i \in [n', n)i∈[n 
′
 ,n)，有 s[i] = s[i-n']s[i]=s[i−n 
′
 ]。

也就是说，ss 中长度为 n'n 
′
  的前缀就是 s's 
′
 ，并且在这之后的每一个位置上的字符 s[i]s[i]，都需要与它之前的第 n'n 
′
  个字符 s[i-n']s[i−n 
′
 ] 相同。

因此，我们可以从小到大枚举 n'n 
′
 ，并对字符串 ss 进行遍历，进行上述的判断。注意到一个小优化是，因为子串至少需要重复一次，所以 n'n 
′
  不会大于 nn 的一半，我们只需要在 [1, \frac{n}{2}][1, 
2
n
​	
 ] 的范围内枚举 n'n 
′
  即可。

代码

C++JavaPython3GolangC

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        for i in range(1, n // 2 + 1):
            if n % i == 0:
                if all(s[j] == s[j - i] for j in range(i, n)):
                    return True
        return False
复杂度分析

时间复杂度：O(n^2)O(n 
2
 )，其中 nn 是字符串 ss 的长度。枚举 ii 的时间复杂度为 O(n)O(n)，遍历 ss 的时间复杂度为 O(n)O(n)，相乘即为总时间复杂度。

空间复杂度：O(1)O(1)。

方法二：字符串匹配
思路与算法

我们可以把字符串 ss 写成

s's' \cdots s's'
s 
′
 s 
′
 ⋯s 
′
 s 
′
 

的形式，总计 \frac{n}{n'} 
n 
′
 
n
​	
  个 s's 
′
 。但我们如何在不枚举 n'n 
′
  的情况下，判断 ss 是否能写成上述的形式呢？

如果我们移除字符串 ss 的前 n'n 
′
  个字符（即一个完整的 s's 
′
 ），再将这些字符保持顺序添加到剩余字符串的末尾，那么得到的字符串仍然是 ss。由于 1 \leq n' < n1≤n 
′
 <n，那么如果将两个 ss 连在一起，并移除第一个和最后一个字符，那么得到的字符串一定包含 ss，即 ss 是它的一个子串。

因此我们可以考虑这种方法：我们将两个 ss 连在一起，并移除第一个和最后一个字符。如果 ss 是该字符串的子串，那么 ss 就满足题目要求。

注意到我们证明的是如果 ss 满足题目要求，那么 ss 有这样的性质，而我们使用的方法却是如果 ss 有这样的性质，那么 ss 满足题目要求。因此，只证明了充分性是远远不够的，我们还需要证明必要性。

题解区的很多题解都忽略了这一点，但它是非常重要的。

证明需要使用一些同余运算的小技巧，可以见方法三之后的「正确性证明」部分。这里先假设我们已经完成了证明，这样就可以使用非常简短的代码完成本题。在下面的代码中，我们可以从位置 11 开始查询，并希望查询结果不为位置 nn，这与移除字符串的第一个和最后一个字符是等价的。

代码

C++JavaPython3C

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return (s + s).find(s, 1) != len(s)
复杂度分析

由于我们使用了语言自带的字符串查找函数，因此这里不深入分析其时空复杂度。

方法三：KMP 算法
思路与算法

在方法二中，我们使用了语言自带的字符串查找函数。同样我们也可以自己实现这个函数，例如使用比较经典的 KMP 算法。

读者需要注意以下几点：

KMP 算法虽然有着良好的理论时间复杂度上限，但大部分语言自带的字符串查找函数并不是用 KMP 算法实现的。这是因为在实现 API 时，我们需要在平均时间复杂度和最坏时间复杂度二者之间权衡。普通的暴力匹配算法以及优化的 BM 算法拥有比 KMP 算法更为优秀的平均时间复杂度；

学习 KMP 算法时，一定要理解其本质。如果放弃阅读晦涩难懂的材料（即使大部分讲解 KMP 算法的材料都包含大量的图，但图毕竟只能描述特殊而非一般情况）而是直接去阅读代码，是永远无法学会 KMP 算法的。读者甚至无法理解 KMP 算法关键代码中的任意一行。

由于本题就是在一个字符串中查询另一个字符串是否出现，可以直接套用 KMP 算法。因此这里对 KMP 算法本身不再赘述。读者可以自行查阅资料进行学习。这里留了三个思考题，读者可以在学习完毕后尝试回答这三个问题，检验自己的学习成果：

设查询串的的长度为 nn，模式串的长度为 mm，我们需要判断模式串是否为查询串的子串。那么使用 KMP 算法处理该问题时的时间复杂度是多少？在分析时间复杂度时使用了哪一种分析方法？

如果有多个查询串，平均长度为 nn，数量为 kk，那么总时间复杂度是多少？

在 KMP 算法中，对于模式串，我们需要预处理出一个 \textit{fail}fail 数组（有时也称为 \textit{next}next 数组、\piπ 数组等）。这个数组到底表示了什么？

代码

C++JavaPython3GolangC

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        def kmp(query: str, pattern: str) -> bool:
            n, m = len(query), len(pattern)
            fail = [-1] * m
            for i in range(1, m):
                j = fail[i - 1]
                while j != -1 and pattern[j + 1] != pattern[i]:
                    j = fail[j]
                if pattern[j + 1] == pattern[i]:
                    fail[i] = j + 1
            match = -1
            for i in range(1, n - 1):
                while match != -1 and pattern[match + 1] != query[i]:
                    match = fail[match]
                if pattern[match + 1] == query[i]:
                    match += 1
                    if match == m - 1:
                        return True
            return False
        
        return kmp(s + s, s)
复杂度分析

时间复杂度：O(n)O(n)，其中 nn 是字符串 ss 的长度。

空间复杂度：O(n)O(n)。

正确性证明
一方面，如果长度为 nn 的字符串 ss 是字符串 t=s+st=s+s 的子串，并且 ss 在 tt 中的起始位置不为 00 或 nn，那么 ss 就满足题目的要求。证明过程如下：

我们设 ss 在 tt 中的起始位置为 ii，i \in (0, n)i∈(0,n)。也就是说，tt 中从位置 ii 开始的 nn 个连续的字符，恰好就是字符串 ss。那么我们有：

s[0:n-1] = t[i:n+i-1]
s[0:n−1]=t[i:n+i−1]

由于 tt 是由两个 ss 拼接而成的，我们可以将 t[i:n+i-1]t[i:n+i−1] 分成位置 n-1n−1 左侧和右侧两部分：

\left \{ \begin{aligned} s[0:n-i-1] &= t[i:n-1] \\ s[n-i:n-1] &= t[n:n+i-1] = t[0:i-1] \end{aligned} \right.
{ 
s[0:n−i−1]
s[n−i:n−1]
​	
  
=t[i:n−1]
=t[n:n+i−1]=t[0:i−1]
​	
 

每一部分都可以对应回 ss：

\left \{ \begin{aligned} s[0:n-i-1] &= s[i:n-1] \\ s[n-i:n-1] &= s[0:i-1] \end{aligned} \right.
{ 
s[0:n−i−1]
s[n−i:n−1]
​	
  
=s[i:n−1]
=s[0:i−1]
​	
 

这说明，ss 是一个「可旋转」的字符串：将 ss 的前 ii 个字符保持顺序，移动到 ss 的末尾，得到的新字符串与 ss 相同。也就是说，在模 nn 的意义下，

s[j] = s[j+i]
s[j]=s[j+i]

对于任意的 jj 恒成立。

「在模 nn 的意义下」可以理解为，所有的加法运算的结果都需要对 nn 取模，使得结果保持在 [0, n)[0,n) 中，这样加法就自带了「旋转」的效果。

如果我们不断地连写这个等式：

s[j] = s[j+i] = s[j+2i] = s[j+3i] = \cdots
s[j]=s[j+i]=s[j+2i]=s[j+3i]=⋯

那么所有满足 j_0 = j + k \cdot ij 
0
​	
 =j+k⋅i 的位置 j_0j 
0
​	
  都有 s[j] = s[j_0]s[j]=s[j 
0
​	
 ]，jj 和 j_0j 
0
​	
  在模 ii 的意义下等价。由于我们已经在模 nn 的意义下讨论这个问题，因此 jj 和 j_0j 
0
​	
  在模 \mathrm{gcd}(n, i)gcd(n,i) 的意义下等价，其中 \mathrm{gcd}gcd 表示最大公约数。也就是说，字符串 ss 中的两个位置如果在模 \mathrm{gcd}(n, i)gcd(n,i) 的意义下等价，那么它们对应的字符必然是相同的。

由于 \mathrm{gcd}(n, i)gcd(n,i) 一定是 nn 的约数，那么字符串 ss 一定可以由其长度为 \mathrm{gcd}(n, i)gcd(n,i) 的前缀重复 \frac{n}{\mathrm{gcd}(n, i)} 
gcd(n,i)
n
​	
  次构成。

另一方面，如果 ss 满足题目的要求，那么 ss 包含若干个「部分」，t=s+st=s+s 包含两倍数量的「部分」，因此 ss 显然是 tt 的子串，并且起始位置可以不为 00 或 nn：我们只需要选择 tt 中第一个「部分」的起始位置即可。

综上所述，我们证明了：长度为 nn 的字符串 ss 是字符串 t=s+st=s+s 的子串，并且 ss 在 tt 中的起始位置不为 00 或 nn，当且仅当 ss 满足题目的要求。因此，

思考题答案
设查询串的的长度为 nn，模式串的长度为 mm，我们需要判断模式串是否为查询串的子串。那么使用 KMP 算法处理该问题时的时间复杂度是多少？在分析时间复杂度时使用了哪一种分析方法？

时间复杂度为 O(n+m)O(n+m)，用到了均摊分析（摊还分析）的方法。

具体地，无论在预处理过程还是查询过程中，虽然匹配失败时，指针会不断地根据 \textit{fail}fail 数组向左回退，看似时间复杂度会很高。但考虑匹配成功时，指针会向右移动一个位置，这一部分对应的时间复杂度为 O(n+m)O(n+m)。又因为向左移动的次数不会超过向右移动的次数，因此总时间复杂度仍然为 O(n+m)O(n+m)。

如果有多个查询串，平均长度为 nn，数量为 kk，那么总时间复杂度是多少？

时间复杂度为 O(nk+m)O(nk+m)。模式串只需要预处理一次。
在 KMP 算法中，对于模式串，我们需要预处理出一个 \textit{fail}fail 数组（有时也称为 \textit{next}next 数组、\piπ 数组等）。这个数组到底表示了什么？

\textit{fail}[i]fail[i] 等于满足下述要求的 xx 的最大值：s[0:i]s[0:i] 具有长度为 x+1x+1 的完全相同的前缀和后缀。这也是 KMP 算法最重要的一部分。
方法四：优化的 KMP 算法
思路与算法

如果读者能够看懂「正确性证明」和「思考题答案」这两部分，那么一定已经发现了方法三中的 KMP 算法有可以优化的地方。即：

在「正确性证明」部分，如果我们设 ii 为最小的起始位置，那么一定有 \mathrm{gcd}(n, i) = igcd(n,i)=i，即 nn 是 ii 的倍数。这说明字符串 ss 是由长度为 ii 的前缀重复 \frac{n}{i} 
i
n
​	
  次构成；

由于 \textit{fail}[n-1]fail[n−1] 表示 ss 具有长度为 \textit{fail}[n-1]+1fail[n−1]+1 的完全相同的（且最长的）前缀和后缀。那么对于满足题目要求的字符串，一定有 \textit{fail}[n-1] = n-i-1fail[n−1]=n−i−1，即 i = n - \textit{fail}[n-1] - 1i=n−fail[n−1]−1；

对于不满足题目要求的字符串，nn 一定不是 n - \textit{fail}[n-1] - 1n−fail[n−1]−1 的倍数。

上述所有的结论都可以很容易地使用反证法证出。

因此，我们在预处理出 \textit{fail}fail 数组后，只需要判断 nn 是否为 n - \textit{fail}[n-1] - 1n−fail[n−1]−1 的倍数即可。

代码

C++JavaPython3GolangC

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        def kmp(pattern: str) -> bool:
            n = len(pattern)
            fail = [-1] * n
            for i in range(1, n):
                j = fail[i - 1]
                while j != -1 and pattern[j + 1] != pattern[i]:
                    j = fail[j]
                if pattern[j + 1] == pattern[i]:
                    fail[i] = j + 1
            return fail[n - 1] != -1 and n % (n - fail[n - 1] - 1) == 0
        
        return kmp(s)
复杂度分析

时间复杂度：O(n)O(n)，其中 nn 是字符串 ss 的长度。

空间复杂度：O(n)O(n)。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/repeated-substring-pattern/solution/zhong-fu-de-zi-zi-fu-chuan-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''