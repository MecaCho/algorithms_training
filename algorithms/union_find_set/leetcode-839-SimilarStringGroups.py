# encoding=utf8


'''
839. Similar String Groups
Two strings X and Y are similar if we can swap two letters (in different positions) of X, so that it equals Y. Also two strings X and Y are similar if they are equal.

For example, "tars" and "rats" are similar (swapping at positions 0 and 2), and "rats" and "arts" are similar, but "star" is not similar to "tars", "rats", or "arts".

Together, these form two connected groups by similarity: {"tars", "rats", "arts"} and {"star"}.  Notice that "tars" and "arts" are in the same group even though they are not similar.  Formally, each group is such that a word is in the group if and only if it is similar to at least one other word in the group.

We are given a list strs of strings where every string in strs is an anagram of every other string in strs. How many groups are there?



Example 1:

Input: strs = ["tars","rats","arts","star"]
Output: 2
Example 2:

Input: strs = ["omv","ovm"]
Output: 1


Constraints:

1 <= strs.length <= 100
1 <= strs[i].length <= 1000
sum(strs[i].length) <= 2 * 104
strs[i] consists of lowercase letters only.
All words in strs have the same length and are anagrams of each other.


839. 相似字符串组
如果交换字符串 X 中的两个不同位置的字母，使得它和字符串 Y 相等，那么称 X 和 Y 两个字符串相似。如果这两个字符串本身是相等的，那它们也是相似的。

例如，"tars" 和 "rats" 是相似的 (交换 0 与 2 的位置)； "rats" 和 "arts" 也是相似的，但是 "star" 不与 "tars"，"rats"，或 "arts" 相似。

总之，它们通过相似性形成了两个关联组：{"tars", "rats", "arts"} 和 {"star"}。注意，"tars" 和 "arts" 是在同一组中，即使它们并不相似。形式上，对每个组而言，要确定一个单词在组中，只需要这个词和该组中至少一个单词相似。

给你一个字符串列表 strs。列表中的每个字符串都是 strs 中其它所有字符串的一个字母异位词。请问 strs 中有多少个相似字符串组？



示例 1：

输入：strs = ["tars","rats","arts","star"]
输出：2
示例 2：

输入：strs = ["omv","ovm"]
输出：1


提示：

1 <= strs.length <= 100
1 <= strs[i].length <= 1000
sum(strs[i].length) <= 2 * 104
strs[i] 只包含小写字母。
strs 中的所有单词都具有相同的长度，且是彼此的字母异位词。


备注：

      字母异位词（anagram），一种把某个字符串的字母的位置（顺序）加以改换所形成的新词。
'''


class Solution(object):
    def numSimilarGroups(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        n = len(strs)
        self.p = [i for i in range(n)]

        def check(a, b):
            l = zip(a, b)
            num = 0
            for x, y in l:
                if x != y:
                    num += 1
                if num > 2:
                    return False
            return True

        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                self.p[px] = py
                return False
            return True

        def find(x):
            px = self.p[x]
            if px != x:
                self.p[x] = find(self.p[px])
            return self.p[x]

        for i in range(n):
            for j in range(i + 1, n):
                if check(strs[i], strs[j]):
                    union(i, j)
        # print(self.p)

        return sum([1 if i == self.p[i] else 0 for i in range(n)])

# solutions

'''
方法一：并查集
思路及解法

我们把每一个字符串看作点，字符串之间是否相似看作边，那么可以发现本题询问的是给定的图中有多少连通分量。于是可以想到使用并查集维护节点间的连通性。

我们枚举给定序列中的任意一对字符串，检查其是否具有相似性，如果相似，那么我们就将这对字符串相连。

在实际代码中，我们可以首先判断当前这对字符串是否已经连通，如果没有连通，我们再检查它们是否具有相似性，可以优化一定的时间复杂度的常数。

代码

C++JavaJavaScriptPython3GolangC

class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        n = len(strs)
        f = list(range(n))

        def find(x: int) -> int:
            if f[x] == x:
                return x
            f[x] = find(f[x])
            return f[x]
        
        def check(a: str, b: str) -> bool:
            num = 0
            for ac, bc in zip(a, b):
                if ac != bc:
                    num += 1
                    if num > 2:
                        return False
            return True
        
        for i in range(n):
            for j in range(i + 1, n):
                fi, fj = find(i), find(j)
                if fi == fj:
                    continue
                if check(strs[i], strs[j]):
                    f[fi] = fj
        
        ret = sum(1 for i in range(n) if f[i] == i)
        return ret
复杂度分析

时间复杂度：O(n^2m + n \log n))O(n 
2
 m+nlogn))，其中 nn 是字符串的数量。我们需要 O(n^2)O(n 
2
 ) 地枚举任意一对字符串之间的关系，对于任意一对字符串，我们需要 O(m)O(m) 的时间检查字符串是否相同。在最坏情况下我们需要对并查集执行 O(n)O(n) 次合并，合并的均摊时间复杂度 O(\log n)O(logn)。综上，总的时间复杂度为 O(n^2m + n \log n))O(n 
2
 m+nlogn))

空间复杂度：O(n)O(n)，其中 nn 是字符串的数量。并查集需要 O(n)O(n) 的空间。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/similar-string-groups/solution/xiang-si-zi-fu-chuan-zu-by-leetcode-solu-8jt9/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''

