# encoding=utf8

'''
49. 字母异位词分组
给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。

示例:

输入: ["eat", "tea", "tan", "ate", "nat", "bat"]
输出:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
说明：

所有输入均为小写字母。
不考虑答案输出的顺序。

49. Group Anagrams
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
'''


import collections

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hash_map = collections.defaultdict(list)
        for word in strs:
            # key = "".join(sorted(word))
            key = tuple(sorted(word))
            hash_map[key].append(word)
        return hash_map.values()


class Solution20201214(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        word_dict = collections.defaultdict(list)
        for i in range(len(strs)):
            word_dict[tuple(sorted(strs[i]))].append(strs[i])

        return [l for l in word_dict.values()]


# golang

'''
func groupAnagrams(strs []string) [][]string {
	hashMap := make(map[string][]string, 0)
	for _, val := range strs {
		vals := strings.Split(val, "")
		sort.Strings(vals)
		key := strings.Join(vals, "")
		v, ok := hashMap[key]
        if ok {
			v = append(v, val)
			hashMap[key] = v
		}else{
            hashMap[key] = []string{val}
        }
	}

	res := [][]string{}

	for _, v := range hashMap {
		res = append(res, v)
	}
	return res
}
'''

'''
方法一：排序数组分类
思路

当且仅当它们的排序字符串相等时，两个字符串是字母异位词。

算法

维护一个映射 ans : {String -> List}，其中每个键 \text{K}K 是一个排序字符串，每个值是初始输入的字符串列表，排序后等于 \text{K}K。

在 Java 中，我们将键存储为字符串，例如，code。 在 Python 中，我们将键存储为散列化元组，例如，('c', 'o', 'd', 'e')。



JavaPython

class Solution(object):
    def groupAnagrams(self, strs):
        ans = collections.defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return ans.values()
复杂度分析

时间复杂度：O(NK \log K)O(NKlogK)，其中 NN 是 strs 的长度，而 KK 是 strs 中字符串的最大长度。当我们遍历每个字符串时，外部循环具有的复杂度为 O(N)O(N)。然后，我们在 O(K \log K)O(KlogK) 的时间内对每个字符串排序。

空间复杂度：O(NK)O(NK)，排序存储在 ans 中的全部信息内容。

方法二：按计数分类
思路

当且仅当它们的字符计数（每个字符的出现次数）相同时，两个字符串是字母异位词。

算法

我们可以将每个字符串 \text{s}s 转换为字符数 \text{count}count，由26个非负整数组成，表示 \text{a}a，\text{b}b，\text{c}c 的数量等。我们使用这些计数作为哈希映射的基础。

在 Java 中，我们的字符数 count 的散列化表示将是一个用 **＃** 字符分隔的字符串。 例如，abbccc 将表示为 ＃1＃2＃3＃0＃0＃0 ...＃0，其中总共有26个条目。 在 python 中，表示将是一个计数的元组。 例如，abbccc 将表示为 (1,2,3,0,0，...，0)，其中总共有 26 个条目。



JavaPython

class Solution:
    def groupAnagrams(strs):
        ans = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return ans.values()
复杂度分析

时间复杂度：O(NK)O(NK)，其中 NN 是 strs 的长度，而 KK 是 strs 中字符串的最大长度。计算每个字符串的字符串大小是线性的，我们统计每个字符串。

空间复杂度：O(NK)O(NK)，排序存储在 ans 中的全部信息内容。

作者：LeetCode
链接：https://leetcode-cn.com/problems/group-anagrams/solution/zi-mu-yi-wei-ci-fen-zu-by-leetcode/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''