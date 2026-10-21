# encoding=utf8


'''
3863. Minimum Operations to Sort a String
You are given a string s consisting of lowercase English letters.

In one operation, you can select any substring of s that is not the entire string and sort it in non-descending alphabetical order.

Return the minimum number of operations required to make s sorted in non-descending order. If it is not possible, return -1.

 

Example 1:

Input: s = "dog"
Output: 1
Explanation:
Sort substring "og" to "go".
Now, s = "dgo", which is sorted in ascending order. Thus, the answer is 1.

Example 2:

Input: s = "card"
Output: 2
Explanation:
Sort substring "car" to "acr", so s = "acrd".
Sort substring "rd" to "dr", making s = "acdr", which is sorted in ascending order. Thus, the answer is 2.

Example 3:

Input: s = "gf"
Output: -1
Explanation:
It is impossible to sort s under the given constraints. Thus, the answer is -1.

 

Constraints:

1 <= s.length <= 10^5
s consists of only lowercase English letters.


3863. 将一个字符串排序的最小操作次数
给你一个由小写英文字母组成的字符串 s。

在一次操作中，你可以选择 s 的任意 子字符串（但 不能 是整个字符串），并将其按 非降序字母顺序 进行 排序。

返回使 s 按 非降序 排列所需的 最小 操作次数。如果无法做到，则返回 -1。

 

示例 1：

输入：s = "dog"
输出：1
解释：
将子字符串 "og" 排序为 "go"。
现在，s = "dgo"，已按升序排列。因此，答案是 1。

示例 2：

输入：s = "card"
输出：2
解释：
将子字符串 "car" 排序为 "acr"，得到 s = "acrd"。
将子字符串 "rd" 排序为 "dr"，得到 s = "acdr"，已按升序排列。因此，答案是 2。

示例 3：

输入：s = "gf"
输出：-1
解释：
在给定提示下，无法对 s 进行排序。因此，答案是 -1。

 

提示：

1 <= s.length <= 10^5
s 仅由小写英文字母组成。
'''


class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)

        # 1. 若字符串已经是非降序排列，无需任何操作
        if all(s[i] <= s[i + 1] for i in range(n - 1)):
            return 0

        # 2. 长度为 2 且无序时，任何真子串长度均为 1，无法改变字符串顺序
        if n == 2:
            return -1

        mn = min(s)
        mx = max(s)

        # 3. 若最小字符已在首位，只需排序后缀 s[1:n]；若最大字符已在末位，只需排序前缀 s[0:n-1]
        if s[0] == mn or s[-1] == mx:
            return 1

        # 4. 若中间位置 s[1:n-1] 存在最小字符或最大字符：
        #    可先操作前缀/后缀将 mn 移到首位或 mx 移到末位，再操作一次完成整体排序
        if any(c == mn or c == mx for c in s[1:-1]):
            return 2

        # 5. 若首位是最大字符、末位是最小字符且中间不存在任何极值，最少需要 3 次操作
        return 3


# golang solution

'''
func minOperations(s string) int {
	n := len(s)

	sorted := true
	for i := 1; i < n; i++ {
		if s[i] < s[i-1] {
			sorted = false
			break
		}
	}
	if sorted {
		return 0
	}

	if n == 2 {
		return -1
	}

	mn, mx := s[0], s[0]
	for i := 1; i < n; i++ {
		if s[i] < mn {
			mn = s[i]
		}
		if s[i] > mx {
			mx = s[i]
		}
	}

	if s[0] == mn || s[n-1] == mx {
		return 1
	}

	for i := 1; i < n-1; i++ {
		if s[i] == mn || s[i] == mx {
			return 2
		}
	}

	return 3
}
'''

# solutions

'''
思路和算法：
1. 核心约束：
   - 每次操作只能选择一个真子串（不能是整个字符串 s，即子串长度 <= n - 1）进行非降序排序。
   - 设全串的最小字符为 mn = min(s)，最大字符为 mx = max(s)。
   - 排序完成后的最终字符串，其首位必须是 mn，末位必须是 mx。

2. 分类讨论（按最少操作步数依次判断）：
   - 情况 0（0 次操作）：
     若原字符串 s 已经是非降序，不需要进行任何操作，返回 0。
   - 情况 -1（无法完成）：
     若 n == 2 且未排序，由于不能选全串，合法的真子串长度只能为 1，排序单个字符不会产生任何变化，因此无法排序，返回 -1。
   - 情况 1（1 次操作）：
     单次操作无法同时覆盖 s[0] 和 s[n-1]，必然留下至少一个端点不被重排。
     * 若 s[0] == mn，我们可以直接选择后缀 s[1:n] 进行排序，首位 mn 保持不变，整体即可变成非降序；
     * 若 s[n-1] == mx，我们可以直接选择前缀 s[0:n-1] 进行排序，末位 mx 保持不变，整体即可变成非降序；
     因此，当且仅当 s[0] == mn 或 s[n-1] == mx 时，1 次操作可完成排序。
   - 情况 2（2 次操作）：
     若不满足情况 1，说明 s[0] != mn 且 s[n-1] != mx。
     要想在 2 次操作内排好，第 1 次操作必须能将 mn 移动到 s[0]，或者将 mx 移动到 s[n-1]：
     * 若中间位置 s[1:n-1] 存在某个字符等于 mn（记下标为 i，1 <= i < n - 1），我们可以先选择包含 s[0] 和 s[i] 的前缀真子串（如 s[0:i+1] 或 s[0:n-1]）进行排序，由于 mn 是该子串内的最小值，排序后 mn 将来到 s[0]；接着第 2 次操作对后缀 s[1:n] 排序即可；
     * 同理，若中间位置 s[1:n-1] 存在某个字符等于 mx，可以先选择包含该字符与末尾的后缀真子串进行排序，将 mx 移到末位 s[n-1]，再用第 2 次操作排序前缀 s[0:n-1]；
     因此，当中间部分 s[1:n-1] 存在 mn 或 mx 时，2 次操作即可完成。
   - 情况 3（3 次操作）：
     若上述情况均不满足，意味着：
     s[0] 是唯一的 mx，s[n-1] 是唯一的 mn，且中间位置不存在任何 mn 或 mx。
     * 此时任何真子串操作都无法在 1 步之内将 mn 移到 s[0] 或将 mx 移到 s[n-1]（若选前缀操作，子串内不含 mn；若选后缀操作，子串内不含 mx）；因此 2 次操作不可行。
     * 3 次操作必定可行：
       1. 先排序后缀 s[1:n]，将原本在 s[n-1] 的 mn 移到 s[1]；
       2. 再排序前缀 s[0:n-1]，将位于 s[1] 的 mn 移到首位 s[0]；
       3. 最后排序后缀 s[1:n]，完成整串排序。
     因此该情况下最少需要 3 次操作。

复杂度分析：
- 时间复杂度：O(n)，其中 n 为字符串 s 的长度。仅需线性扫描判断是否已有序、统计全局最小和最大字符并检查位置分布，耗时 O(n)。
- 空间复杂度：O(1)，仅需常数级别的额外变量。
'''

