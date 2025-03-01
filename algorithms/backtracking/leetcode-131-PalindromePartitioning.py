# encoding=utf8


'''
131. Palindrome Partitioning
Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

A palindrome string is a string that reads the same backward as forward.



Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
Example 2:

Input: s = "a"
Output: [["a"]]


Constraints:

1 <= s.length <= 16
s contains only lowercase English letters.


131. 分割回文串
给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。

返回 s 所有可能的分割方案。

示例:

输入: "aab"
输出:
[
  ["aa","b"],
  ["a","a","b"]
]
'''


class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """

        self.vals = []

        def bk(nums, temp):
            if not nums and temp[-1][::-1] == temp[-1]:
                self.vals.append(temp)
                return
            for i in range(len(nums)):
                if temp and temp[-1][::-1] != temp[-1]:
                    continue
                bk(nums[ i +1:], temp +["".join(nums[: i +1])])

        bk(list(s), [])
        return self.vals


class Solution1(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """

        def is_palindrome(s):
            i, j = 0, len(s) - 1
            while i <= j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        self.vals = []

        def bk(s, temp):
            if not s:
                self.vals.append(temp)
                return
            for i in range(len(s)):
                if is_palindrome(s[:i + 1]):
                    bk(s[i + 1:], temp + [s[:i + 1]])

        bk(s, [])
        return self.vals


class Solution2(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        def is_palindrome(i, j):
            print(i, j)
            while i <= j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        self.vals = []

        def bk(temp, start):
            if start >= len(s):
                self.vals.append(temp)
                return
            for i in range(len(s) - start):
                # print(is_palindrome(start, start+i), start, start+i)
                if is_palindrome(start, start+i):
                    # print(start, start+i, [s[:i + 1]], True)
                    bk(temp + [s[start:start+i+1]], start+i+1)

        bk([], 0)
        return self.vals


class Solution3(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        return [[s[:i]] + rest
            for i in xrange(1, len(s)+1)
            if s[:i] == s[i-1::-1]
            for rest in self.partition(s[i:])] or [[]]


class Solution4(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """

        return [[s[:i]] + rest
            for i in range(1, len(s)+1)
            if s[:i] == s[i-1::-1]
            for rest in self.partition(s[i:])] or [[]]


class Solution5(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        if not s:
            return [[]]
        res = []
        for i in range(1, len(s)+1):
            for per in self.partition(s[i:]):
                if s[:i] == s[i-1::-1]:
                    res.append(s[:i]+per)
        return res

        # return [[s[:i]] + rest
        #         for i in range(1, len(s) + 1)
        #         if s[:i] == s[i - 1::-1]
        #         for rest in self.partition(s[i:])] or [[]]

if __name__ == '__main__':
    demo = Solution2()
    res = demo.partition("aab")
    print(res)


# solution

'''
方法一：回溯 + 动态规划预处理
思路与算法

由于需要求出字符串 ss 的所有分割方案，因此我们考虑使用搜索 + 回溯的方法枚举所有可能的分割方法并进行判断。

假设我们当前搜索到字符串的第 ii 个字符，且 s[0..i-1]s[0..i−1] 位置的所有字符已经被分割成若干个回文串，并且分割结果被放入了答案数组 \textit{ans}ans 中，那么我们就需要枚举下一个回文串的右边界 jj，使得 s[i..j]s[i..j] 是一个回文串。

因此，我们可以从 ii 开始，从小到大依次枚举 jj。对于当前枚举的 jj 值，我们使用双指针的方法判断 s[i..j]s[i..j] 是否为回文串：如果 s[i..j]s[i..j] 是回文串，那么就将其加入答案数组 \textit{ans}ans 中，并以 j+1j+1 作为新的 ii 进行下一层搜索，并在未来的回溯时将 s[i..j]s[i..j] 从 \textit{ans}ans 中移除。

如果我们已经搜索完了字符串的最后一个字符，那么就找到了一种满足要求的分割方法。

细节

当我们在判断 s[i..j]s[i..j] 是否为回文串时，常规的方法是使用双指针分别指向 ii 和 jj，每次判断两个指针指向的字符是否相同，直到两个指针相遇。然而这种方法会产生重复计算，例如下面这个例子：

当 s = \texttt{aaba}s=aaba 时，对于前 22 个字符 \texttt{aa}aa，我们有 22 种分割方法 [\texttt{aa}][aa] 和 [\texttt{a}, \texttt{a}][a,a]，当我们每一次搜索到字符串的第 i=2i=2 个字符 \texttt{b}b 时，都需要对于每个 s[i..j]s[i..j] 使用双指针判断其是否为回文串，这就产生了重复计算。

因此，我们可以将字符串 ss 的每个子串 s[i..j]s[i..j] 是否为回文串预处理出来，使用动态规划即可。设 f(i, j)f(i,j) 表示 s[i..j]s[i..j] 是否为回文串，那么有状态转移方程：

f(i, j) = \begin{cases} \texttt{True}, & \quad i \geq j \\ f(i+1,j-1) \wedge (s[i]=s[j]), & \quad \text{otherwise} \end{cases}
f(i,j)={ 
True,
f(i+1,j−1)∧(s[i]=s[j]),
​	
  
i≥j
otherwise
​	
 

其中 \wedge∧ 表示逻辑与运算，即 s[i..j]s[i..j] 为回文串，当且仅当其为空串（i>ji>j），其长度为 11（i=ji=j），或者首尾字符相同且 s[i+1..j-1]s[i+1..j−1] 为回文串。

预处理完成之后，我们只需要 O(1)O(1) 的时间就可以判断任意 s[i..j]s[i..j] 是否为回文串了。

代码

C++JavaPython3JavaScriptGolangC

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        f = [[True] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                f[i][j] = (s[i] == s[j]) and f[i + 1][j - 1]

        ret = list()
        ans = list()

        def dfs(i: int):
            if i == n:
                ret.append(ans[:])
                return
            
            for j in range(i, n):
                if f[i][j]:
                    ans.append(s[i:j+1])
                    dfs(j + 1)
                    ans.pop()

        dfs(0)
        return ret
复杂度分析

时间复杂度：O(n \cdot 2^n)O(n⋅2 
n
 )，其中 nn 是字符串 ss 的长度。在最坏情况下，ss 包含 nn 个完全相同的字符，因此它的任意一种划分方法都满足要求。而长度为 nn 的字符串的划分方案数为 2^{n-1}=O(2^n)2 
n−1
 =O(2 
n
 )，每一种划分方法需要 O(n)O(n) 的时间求出对应的划分结果并放入答案，因此总时间复杂度为 O(n \cdot 2^n)O(n⋅2 
n
 )。尽管动态规划预处理需要 O(n^2)O(n 
2
 ) 的时间，但在渐进意义下小于 O(n \cdot 2^n)O(n⋅2 
n
 )，因此可以忽略。

空间复杂度：O(n^2)O(n 
2
 )，这里不计算返回答案占用的空间。数组 ff 需要使用的空间为 O(n^2)O(n 
2
 )，而在回溯的过程中，我们需要使用 O(n)O(n) 的栈空间以及 O(n)O(n) 的用来存储当前字符串分割方法的空间。由于 O(n)O(n) 在渐进意义下小于 O(n^2)O(n 
2
 )，因此空间复杂度为 O(n^2)O(n 
2
 )。

方法二：回溯 + 记忆化搜索
思路与算法

方法一中的动态规划预处理计算出了任意的 s[i..j]s[i..j] 是否为回文串，我们也可以将这一步改为记忆化搜索。

代码

C++JavaPython3JavaScriptGolangC

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)

        ret = list()
        ans = list()

        @cache
        def isPalindrome(i: int, j: int) -> int:
            if i >= j:
                return 1
            return isPalindrome(i + 1, j - 1) if s[i] == s[j] else -1

        def dfs(i: int):
            if i == n:
                ret.append(ans[:])
                return
            
            for j in range(i, n):
                if isPalindrome(i, j) == 1:
                    ans.append(s[i:j+1])
                    dfs(j + 1)
                    ans.pop()

        dfs(0)
        isPalindrome.cache_clear()
        return ret
复杂度分析

时间复杂度：O(n \cdot 2^n)O(n⋅2 
n
 )，其中 nn 是字符串 ss 的长度，与方法一相同。

空间复杂度：O(n^2)O(n 
2
 )，与方法一相同。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/palindrome-partitioning/solution/fen-ge-hui-wen-chuan-by-leetcode-solutio-6jkv/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
