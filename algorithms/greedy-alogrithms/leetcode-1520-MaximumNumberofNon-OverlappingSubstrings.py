# encoding=utf8

'''
1520. Maximum Number of Non-Overlapping Substrings
Given a string s of lowercase letters, you need to find the maximum number of non-empty substrings of s that meet the following conditions:

The substrings do not overlap, that is for any two substrings s[i..j] and s[x..y], either j < x or i > y is true.
A substring that contains a certain character c must also contain all occurrences of c.
Find the maximum number of substrings that meet the above conditions. If there are multiple solutions with the same number of substrings, return the one with minimum total length. It can be shown that there exists a unique solution of minimum total length.

Notice that you can return the substrings in any order.

 

Example 1:

Input: s = "adefaddaccc"
Output: ["e","f","ccc"]
Explanation: The following are all the possible substrings that meet the conditions:
[
  "adefaddaccc"
  "adefadda",
  "ef",
  "e",
  "f",
  "ccc",
]
If we choose the first string, we cannot choose anything else and we'd get only 1. If we choose "adefadda", we are left with "ccc" which is the only one that doesn't overlap, thus obtaining 2 substrings. Notice also, that it's not optimal to choose "ef" since it can be split into two. Therefore, the optimal way is to choose ["e","f","ccc"] which gives us 3 substrings. No other solution of the same number of substrings exist.

Example 2:

Input: s = "abbaccd"
Output: ["d","bb","cc"]
Explanation: Notice that while the set of substrings ["d","abba","cc"] also has length 3, it's considered incorrect since it has larger total length.

 

Constraints:

1 <= s.length <= 10^5
s contains only lowercase English letters.


1520. 最多的不重叠子字符串
给你一个只包含小写字母的字符串 s ，你需要找到 s 中最多数目的非空子字符串，满足如下条件：

1. 这些字符串之间互不重叠，也就是说对于任意两个子字符串 s[i..j] 和 s[x..y] ，要么 j < x 要么 i > y 。
2. 如果一个子字符串包含字符 char ，那么 s 中所有 char 字符都应该在这个子字符串中。

请你找到满足上述条件的最多子字符串数目。如果有多个解法有相同的子字符串数目，请返回这些子字符串总长度最小的一个解。可以证明最小总长度解是唯一的。

请注意，你可以以 任意 顺序返回最优解的子字符串。

 

示例 1：

输入：s = "adefaddaccc"
输出：["e","f","ccc"]
解释：下面为所有满足第二个条件的子字符串：
[
  "adefaddaccc",
  "adefadda",
  "ef",
  "e",
  "f",
  "ccc",
]
如果我们选择第一个字符串，那么我们无法再选择其他任何字符串，所以答案为 1 。如果我们选择 "adefadda" ，剩下子字符串中我们只可以选择 "ccc" ，它是唯一不重叠的子字符串，所以答案为 2 。同时我们可以发现，选择 "ef" 不是最优的，因为它可以被拆分成 2 个子字符串。所以最优解是选择 ["e","f","ccc"] ，答案为 3 。不存在别的相同数目子字符串解。

示例 2：

输入：s = "abbaccd"
输出：["d","bb","cc"]
解释：注意到解 ["d","abba","cc"] 答案也为 3 ，但它不是最优解，因为它的总长度更长。

 

提示：

1 <= s.length <= 10^5
s 只包含小写英文字母。
'''


class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        first = [-1] * 26
        last = [-1] * 26

        for i, ch in enumerate(s):
            idx = ord(ch) - ord('a')
            if first[idx] == -1:
                first[idx] = i
            last[idx] = i

        intervals = []
        # 以每个字符的首次出现位置作为子串的起始左边界，寻找满足条件的最小合法区间
        for c in range(26):
            if first[c] == -1:
                continue
            l = first[c]
            r = last[c]
            valid = True
            i = l
            while i <= r:
                idx = ord(s[i]) - ord('a')
                # 如果当前子串内的字符在更早的位置出现过，则以 l 开头的子串必定包含更早位置，说明该 l 不能作为合法起始
                if first[idx] < l:
                    valid = False
                    break
                r = max(r, last[idx])
                i += 1
            if valid:
                intervals.append((l, r))

        # 经典区间调度贪心策略：按右端点升序排序，右端点相同按长度升序排序
        intervals.sort(key=lambda x: (x[1], x[1] - x[0]))

        ans = []
        prev_end = -1
        for l, r in intervals:
            if l > prev_end:
                ans.append(s[l : r + 1])
                prev_end = r

        return ans


# golang solution

'''
import "sort"

func maxNumOfSubstrings(s string) []string {
	first := make([]int, 26)
	last := make([]int, 26)
	for i := range first {
		first[i] = -1
		last[i] = -1
	}

	for i := 0; i < len(s); i++ {
		idx := int(s[i] - 'a')
		if first[idx] == -1 {
			first[idx] = i
		}
		last[idx] = i
	}

	type interval struct {
		l, r int
	}
	var intervals []interval

	// 枚举每个字符作为区间的左端点候选
	for c := 0; c < 26; c++ {
		if first[c] == -1 {
			continue
		}
		l := first[c]
		r := last[c]
		valid := true
		for i := l; i <= r; i++ {
			idx := int(s[i] - 'a')
			if first[idx] < l {
				valid = false
				break
			}
			if last[idx] > r {
				r = last[idx]
			}
		}
		if valid {
			intervals = append(intervals, interval{l, r})
		}
	}

	// 贪心区间调度：右端点越小越优；相同右端点取区间更短者
	sort.Slice(intervals, func(i, j int) bool {
		if intervals[i].r != intervals[j].r {
			return intervals[i].r < intervals[j].r
		}
		return (intervals[i].r - intervals[i].l) < (intervals[j].r - intervals[j].l)
	})

	var ans []string
	prevEnd := -1
	for _, inter := range intervals {
		if inter.l > prevEnd {
			ans = append(ans, s[inter.l:inter.r+1])
			prevEnd = inter.r
		}
	}

	return ans
}
'''

# solutions

'''
思路和算法：

方法：扩展合法区间 + 贪心区间调度（Interval Scheduling）

1. 合法子字符串的结构性质：
   - 条件一：子字符串互不重叠。
   - 条件二：如果子字符串包含字符 c，则字符串 s 中所有字符 c 必须完全落在该子字符串内部。
   
   由此可知：对于子字符串内包含的任意字符 ch，子字符串的左边界必须 <= first[ch]，右边界必须 >= last[ch]。
   如果一个极小子串是合法的，它的左端点必须是某个字符 ch 的首次出现位置 first[ch]。
   （若左端点不是某个字符的首次出现，则去掉该字符并不影响其他字符是否完整包含，不是最小合法子串）。

2. 预处理与区间扩展：
   - 记录 26 个小写英文字母在 s 中的首次出现下标 first[c] 和最后出现下标 last[c]。
   - 对每个在 s 中出现过的字符 c，以其首次出现位置 l = first[c] 作为左端点，初设右端点 r = last[c]。
   - 从 l 扫描到 r：
     - 若字符 s[i] 的首次出现位置 first[s[i]] < l，说明任何包含 c 和 s[i] 的合法子串都必须扩展到 first[s[i]] <= l 之前，即以当前 l 开头不可能构成一个向左不延伸的极小合法子串，故该 l 无效，直接退出。
     - 若 first[s[i]] >= l，则需要把右端点扩展为 max(r, last[s[i]])。
   - 若扫描完成且无上述冲突，则 [l, r] 是一个以 l 为起点的极小合法子串。
   - 候选合法区间的数量至多为 26 个。

3. 区间包含关系与贪心选择：
   - 注意到任意两个合法区间 A 和 B 之间只可能有两种关系：要么完全不相交（互斥），要么其中一个被另一个完全包含（嵌套）。
   - 因为如果它们部分相交（比如 l_A < l_B <= r_A < r_B），由于 s[l_B] 落在 A 内，根据条件二，s[l_B] 的最后出现位置必须在 A 内，即 r_B <= r_A，产生矛盾。
   - 当区间嵌套时（B 严格包含在 A 内部），选择较小的区间 B 总是优于较大的区间 A，因为 B 占用的范围更小，既留给其他子串更多空间，又让总长度更小。
   - 于是问题完全转化为经典的无重叠区间调度问题：
     将候选区间按右端点 r 从小到大排序（若 r 相同，按长度从小到大排序），依次贪心选取与前一个选取区间不重叠的区间。

复杂度分析：
- 时间复杂度：O(n * Σ + Σ log Σ)，其中 n 为字符串 s 的长度，字符集大小 Σ = 26。统计字符首末位置耗时 O(n)；扩展最多 26 个区间，每个区间扩展最多扫描 n 个字符，耗时 O(n * Σ)；排序和贪心选择耗时 O(Σ log Σ)。总时间复杂度为线性 O(n)。
- 空间复杂度：O(Σ)，记录 26 个字符的首末位置及候选区间，额外空间为常数级 O(1)（或严格为 O(Σ)）。
'''

