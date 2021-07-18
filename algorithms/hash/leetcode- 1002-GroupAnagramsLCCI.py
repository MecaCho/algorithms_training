# encoding=utf8

'''
面试题 10.02. Group Anagrams LCCI
Write a method to sort an array of strings so that all the anagrams are in the same group.

Note: This problem is slightly different from the original one the book.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Notes:

All inputs will be in lowercase.
The order of your output does not matter.

面试题 10.02. 变位词组
编写一种方法，对字符串数组进行排序，将所有变位词组合在一起。变位词是指字母相同，但排列不同的字符串。

注意：本题相对原题稍作修改

示例:

输入: ["eat", "tea", "tan", "ate", "nat", "bat"],
输出:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
说明：

所有输入均为小写字母。
不考虑答案输出的顺序。
'''

# solution

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        mp = collections.defaultdict(list)
        for st in strs:
            key = [0]*26
            for char in st:
                key[ord(char)-ord("a")] += 1
            d = tuple(key)
            mp[d].append(st)

        return mp.values()

      
# solutions

'''
前言
两个字符串互为变位词，当且仅当两个字符串包含的字母相同。同一组变位词中的字符串具备相同点，可以使用相同点作为一组变位词的标志，使用哈希表存储每一组变位词，哈希表的键为一组变位词的标志，哈希表的值为一组变位词列表。

遍历每个字符串，对于每个字符串，得到该字符串所在的一组变位词的标志，将当前字符串加入该组变位词的列表中。遍历全部字符串之后，哈希表中的每个键值对即为一组变位词。

以下的两种方法分别使用排序和计数作为哈希表的键。

方法一：排序
由于互为变位词的两个字符串包含的字母相同，因此对两个字符串分别进行排序之后得到的字符串一定是相同的，故可以将排序之后的字符串作为哈希表的键。

JavaC#JavaScriptGolangC++Python3

func groupAnagrams(strs []string) [][]string {
    mp := map[string][]string{}
    for _, str := range strs {
        s := []byte(str)
        sort.Slice(s, func(i, j int) bool { return s[i] < s[j] })
        sortedStr := string(s)
        mp[sortedStr] = append(mp[sortedStr], str)
    }
    ans := make([][]string, 0, len(mp))
    for _, v := range mp {
        ans = append(ans, v)
    }
    return ans
}
复杂度分析

时间复杂度：O(nk \log k)O(nklogk)，其中 nn 是 \textit{strs}strs 中的字符串的数量，kk 是 \textit{strs}strs 中的字符串的的最大长度。需要遍历 nn 个字符串，对于每个字符串，需要 O(k \log k)O(klogk) 的时间进行排序以及 O(1)O(1) 的时间更新哈希表，因此总时间复杂度是 O(nk \log k)O(nklogk)。

空间复杂度：O(nk)O(nk)，其中 nn 是 \textit{strs}strs 中的字符串的数量，kk 是 \textit{strs}strs 中的字符串的的最大长度。需要用哈希表存储全部字符串。

方法二：计数
由于互为变位词的两个字符串包含的字母相同，因此两个字符串中的相同字母出现的次数一定是相同的，故可以将每个字母出现的次数使用字符串表示，作为哈希表的键。

由于字符串只包含小写字母，因此对于每个字符串，可以使用长度为 2626 的数组记录每个字母出现的次数。需要注意的是，在使用数组作为哈希表的键时，不同语言的支持程度不同，因此不同语言的实现方式也不同。

JavaC#JavaScriptGolangC++Python3

func groupAnagrams(strs []string) [][]string {
    mp := map[[26]int][]string{}
    for _, str := range strs {
        cnt := [26]int{}
        for _, b := range str {
            cnt[b-'a']++
        }
        mp[cnt] = append(mp[cnt], str)
    }
    ans := make([][]string, 0, len(mp))
    for _, v := range mp {
        ans = append(ans, v)
    }
    return ans
}
复杂度分析

时间复杂度：O(n(k+|\Sigma|))O(n(k+∣Σ∣))，其中 nn 是 \textit{strs}strs 中的字符串的数量，kk 是 \textit{strs}strs 中的字符串的的最大长度，\SigmaΣ 是字符集，在本题中字符集为所有小写字母，|\Sigma|=26∣Σ∣=26。需要遍历 nn 个字符串，对于每个字符串，需要 O(k)O(k) 的时间计算每个字母出现的次数，O(|\Sigma|)O(∣Σ∣) 的时间生成哈希表的键，以及 O(1)O(1) 的时间更新哈希表，因此总时间复杂度是 O(n(k+|\Sigma|))O(n(k+∣Σ∣))。

空间复杂度：O(n(k+|\Sigma|))O(n(k+∣Σ∣))，其中 nn 是 \textit{strs}strs 中的字符串的数量，kk 是 \textit{strs}strs 中的字符串的最大长度，\SigmaΣ 是字符集，在本题中字符集为所有小写字母，|\Sigma|=26∣Σ∣=26。需要用哈希表存储全部字符串，而记录每个字符串中每个字母出现次数的数组需要的空间为 O(|\Sigma|)O(∣Σ∣)，在渐进意义下小于 O(n(k+|\Sigma|))O(n(k+∣Σ∣))，可以忽略不计。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/group-anagrams-lcci/solution/bian-wei-ci-zu-by-leetcode-solution-g2a8/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''

