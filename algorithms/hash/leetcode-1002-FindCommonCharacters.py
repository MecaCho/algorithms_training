'''
1002. Find Common Characters
Given an array A of strings made only from lowercase letters, return a list of all characters that show up in all strings within the list (including duplicates).  For example, if a character occurs 3 times in all strings but not 4 times, you need to include that character three times in the final answer.

You may return the answer in any order.



Example 1:

Input: ["bella","label","roller"]
Output: ["e","l","l"]
Example 2:

Input: ["cool","lock","cook"]
Output: ["c","o"]


Note:

1 <= A.length <= 100
1 <= A[i].length <= 100
A[i][j] is a lowercase letter

1002. 查找常用字符
给定仅有小写字母组成的字符串数组 A，返回列表中的每个字符串中都显示的全部字符（包括重复字符）组成的列表。例如，如果一个字符在每个字符串中出现 3 次，但不是 4 次，则需要在最终答案中包含该字符 3 次。

你可以按任意顺序返回答案。



示例 1：

输入：["bella","label","roller"]
输出：["e","l","l"]
示例 2：

输入：["cool","lock","cook"]
输出：["c","o"]


提示：

1 <= A.length <= 100
1 <= A[i].length <= 100
A[i][j] 是小写字母
'''



class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        res = ""
        if not A:
            return list(res)

        start = set(A[0])
        # print(start)
        for key in start:
            min_num = min(a.count(key) for a in A)

            res += min_num*key

        return list(res)


# solution

'''
方法一：计数
思路与算法

根据题目的要求，如果字符 cc 在所有字符串中均出现了 kk 次及以上，那么最终答案中需要包含 kk 个 cc。因此，我们可以使用 \textit{minfreq}[c]minfreq[c] 存储字符 cc 在所有字符串中出现次数的最小值。

我们可以依次遍历每一个字符串。当我们遍历到字符串 ss 时，我们使用 \textit{freq}[c]freq[c] 统计 ss 中每一个字符 cc 出现的次数。在统计完成之后，我们再将每一个 \textit{minfreq}[c]minfreq[c] 更新为其本身与 \textit{freq}[c]freq[c] 的较小值。这样一来，当我们遍历完所有字符串后，\textit{minfreq}[c]minfreq[c] 就存储了字符 cc 在所有字符串中出现次数的最小值。

由于题目保证了所有的字符均为小写字母，因此我们可以用长度为 2626 的数组分别表示 \textit{minfreq}minfreq 以及 \textit{freq}freq。

在构造最终的答案时，我们遍历所有的小写字母 cc，并将 \textit{minfreq}[c]minfreq[c] 个 cc 添加进答案数组即可。

代码

C++JavaPython3GolangC

class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        minfreq = [float("inf")] * 26
        for word in A:
            freq = [0] * 26
            for ch in word:
                freq[ord(ch) - ord("a")] += 1
            for i in range(26):
                minfreq[i] = min(minfreq[i], freq[i])
        
        ans = list()
        for i in range(26):
            ans.extend([chr(i + ord("a"))] * minfreq[i])
        return ans
复杂度分析

时间复杂度：O(n(m+|\Sigma|))O(n(m+∣Σ∣))，其中 nn 是数组 AA 的长度（即字符串的数目），mm 是字符串的平均长度，\SigmaΣ 为字符集，在本题中字符集为所有小写字母，|\Sigma|=26∣Σ∣=26。

遍历所有字符串并计算 \textit{freq}freq 的时间复杂度为 O(nm)O(nm)；
使用 \textit{freq}freq 更新 \textit{minfreq}minfreq 的时间复杂度为 O(n|\Sigma|)O(n∣Σ∣)；
由于最终答案包含的字符个数不会超过最短的字符串长度，因此构造最终答案的时间复杂度为 O(m+|\Sigma|)O(m+∣Σ∣)。这一项在渐进意义上小于前二者，可以忽略。
空间复杂度：O(|\Sigma|)O(∣Σ∣)，这里只计算存储答案之外的空间。我们使用了数组 \textit{freq}freq 和 \textit{minfreq}minfreq，它们的长度均为 |\Sigma|∣Σ∣。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/find-common-characters/solution/cha-zhao-chang-yong-zi-fu-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''