# encoding=utf8


'''
395. 至少有K个重复字符的最长子串
找到给定字符串（由小写字符组成）中的最长子串 T ， 要求 T 中的每一字符出现次数都不少于 k 。输出 T 的长度。

示例 1:

输入:
s = "aaabb", k = 3

输出:
3

最长子串为 "aaa" ，其中 'a' 重复了 3 次。
示例 2:

输入:
s = "ababbc", k = 2

输出:
5

最长子串为 "ababb" ，其中 'a' 重复了 2 次， 'b' 重复了 3 次。

395. Longest Substring with At Least K Repeating Characters
Find the length of the longest substring T of a given string (consists of lowercase letters only) such that every character in T appears no less than k times.

Example 1:

Input:
s = "aaabb", k = 3

Output:
3

The longest substring is "aaa", as 'a' is repeated 3 times.
Example 2:

Input:
s = "ababbc", k = 2

Output:
5

The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.
'''



class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if len(s) < k:
            return 0
        min_count_char = min(set(s), key=s.count)
        if s.count(min_count_char) >= k:
            return len(s)
        # print(min_count_char)
        return max([self.longestSubstring(split_s, k) for split_s in s.split(min_count_char)])



class Solution20210227(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if not s:
            return 0

        for c in set(s):
            if s.count(c) < k:
                return max(self.longestSubstring(sub_s, k) for sub_s in s.split(c))
        return len(s)


# solutions


'''
方法一：分治
对于字符串 ss，如果存在某个字符 \textit{ch}ch，它的出现次数大于 00 且小于 kk，则任何包含 \textit{ch}ch 的子串都不可能满足要求。也就是说，我们将字符串按照 \textit{ch}ch 切分成若干段，则满足要求的最长子串一定出现在某个被切分的段内，而不能跨越一个或多个段。因此，可以考虑分治的方式求解本题。

C++JavaJavaScriptGolangC

func longestSubstring(s string, k int) (ans int) {
    if s == "" {
        return
    }

    cnt := [26]int{}
    for _, ch := range s {
        cnt[ch-'a']++
    }

    var split byte
    for i, c := range cnt[:] {
        if 0 < c && c < k {
            split = 'a' + byte(i)
            break
        }
    }
    if split == 0 {
        return len(s)
    }

    for _, subStr := range strings.Split(s, string(split)) {
        ans = max(ans, longestSubstring(subStr, k))
    }
    return
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}
复杂度分析

时间复杂度：O(N\cdot |\Sigma|)O(N⋅∣Σ∣)，其中 NN 为字符串的长度，\SigmaΣ 为字符集，本题中字符串仅包含小写字母，因此 |\Sigma| = 26∣Σ∣=26。由于每次递归调用都会完全去除某个字符，因此递归深度最多为 |\Sigma|∣Σ∣。

空间复杂度：O(|\Sigma|^2)O(∣Σ∣ 
2
 )。递归的深度为 O(|\Sigma|)O(∣Σ∣)，每层递归需要开辟 O(|\Sigma|)O(∣Σ∣) 的额外空间。

方法二：滑动窗口
我们枚举最长子串中的字符种类数目，它最小为 11，最大为 |\Sigma|∣Σ∣（字符集的大小，本题中为 2626）。

对于给定的字符种类数量 tt，我们维护滑动窗口的左右边界 l,rl,r、滑动窗口内部每个字符出现的次数 \textit{cnt}cnt，以及滑动窗口内的字符种类数目 \textit{total}total。当 \textit{total} > ttotal>t 时，我们不断地右移左边界 ll，并对应地更新 \textit{cnt}cnt 以及 \textit{total}total，直到 \textit{total} \le ttotal≤t 为止。这样，对于任何一个右边界 rr，我们都能找到最小的 ll（记为 l_{min}l 
min
​	
 ），使得 s[l_{min}...r]s[l 
min
​	
 ...r] 之间的字符种类数目不多于 tt。

对于任何一组 l_{min}, rl 
min
​	
 ,r 而言，如果 s[l_{min}...r]s[l 
min
​	
 ...r] 之间存在某个出现次数小于 kk （且不为 00，下文不再特殊说明）的字符，我们可以断定：对于任何 l' \in (l_{min}, r)l 
′
 ∈(l 
min
​	
 ,r) 而言，s[l'...r]s[l 
′
 ...r] 依然不可能是满足题意的子串，因为：

要么该字符的出现次数降为 00，此时子串内虽然少了一个出现次数小于 kk 的字符，但字符种类数目也随之小于 tt 了；
要么该字符的出现次数降为非 00 整数，此时该字符的出现次数依然小于 kk。
根据上面的结论，我们发现：当限定字符种类数目为 tt 时，满足题意的最长子串，就一定出自某个 s[l_{min}...r]s[l 
min
​	
 ...r]。因此，在滑动窗口的维护过程中，就可以直接得到最长子串的大小。

此外还剩下一个细节：如何判断某个子串内的字符是否都出现了至少 kk 次？我们当然可以每次遍历 \textit{cnt}cnt 数组，但是这会带来 O(|\Sigma|)O(∣Σ∣) 的额外开销。

我们可以维护一个计数器 \textit{less}less，代表当前出现次数小于 kk 的字符的数量。注意到：每次移动滑动窗口的边界时，只会让某个字符的出现次数加一或者减一。对于移动右边界 ll 的情况而言：

当某个字符的出现次数从 00 增加到 11 时，将 \textit{less}less 加一；

当某个字符的出现次数从 k-1k−1 增加到 kk 时，将 \textit{less}less 减一。

对于移动左边界的情形，讨论是类似的。

通过维护额外的计数器 \textit{less}less，我们无需遍历 \textit{cnt}cnt 数组，就能知道每个字符是否都出现了至少 kk 次，同时可以在每次循环时，在常数时间内更新计数器的取值。读者可以自行思考 k=1k=1 时的处理逻辑。

C++JavaJavaScriptGolangC

func longestSubstring(s string, k int) (ans int) {
    for t := 1; t <= 26; t++ {
        cnt := [26]int{}
        total := 0
        lessK := 0
        l := 0
        for r, ch := range s {
            ch -= 'a'
            if cnt[ch] == 0 {
                total++
                lessK++
            }
            cnt[ch]++
            if cnt[ch] == k {
                lessK--
            }

            for total > t {
                ch := s[l] - 'a'
                if cnt[ch] == k {
                    lessK++
                }
                cnt[ch]--
                if cnt[ch] == 0 {
                    total--
                    lessK--
                }
                l++
            }
            if lessK == 0 {
                ans = max(ans, r-l+1)
            }
        }
    }
    return ans
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}
复杂度分析

时间复杂度：O(N \cdot |\Sigma| + |\Sigma|^2)O(N⋅∣Σ∣+∣Σ∣ 
2
 )，其中 NN 为字符串的长度，\SigmaΣ 为字符集，本题中字符串仅包含小写字母，因此 |\Sigma| = 26∣Σ∣=26。我们需要遍历所有可能的 tt，共 |\Sigma|∣Σ∣ 种可能性；内层循环中滑动窗口的复杂度为 O(N)O(N)，且初始时需要 O(|\Sigma|)O(∣Σ∣) 的时间初始化 \textit{cnt}cnt 数组。

空间复杂度：O(|\Sigma|)O(∣Σ∣)。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/longest-substring-with-at-least-k-repeating-characters/solution/zhi-shao-you-kge-zhong-fu-zi-fu-de-zui-c-o6ww/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
