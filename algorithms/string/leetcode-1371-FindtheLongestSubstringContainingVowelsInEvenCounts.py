'''
1371. 每个元音包含偶数次的最长子字符串
给你一个字符串 s ，请你返回满足以下条件的最长子字符串的长度：每个元音字母，即 'a'，'e'，'i'，'o'，'u' ，在子字符串中都恰好出现了偶数次。



示例 1：

输入：s = "eleetminicoworoep"
输出：13
解释：最长子字符串是 "leetminicowor" ，它包含 e，i，o 各 2 个，以及 0 个 a，u 。
示例 2：

输入：s = "leetcodeisgreat"
输出：5
解释：最长子字符串是 "leetc" ，其中包含 2 个 e 。
示例 3：

输入：s = "bcbcbc"
输出：6
解释：这个示例中，字符串 "bcbcbc" 本身就是最长的，因为所有的元音 a，e，i，o，u 都出现了 0 次。


提示：

1 <= s.length <= 5 x 10^5
s 只包含小写英文字母。

1371. Find the Longest Substring Containing Vowels in Even Counts
Given the string s, return the size of the longest substring containing each vowel an even number of times. That is, 'a', 'e', 'i', 'o', and 'u' must appear an even number of times.



Example 1:

Input: s = "eleetminicoworoep"
Output: 13
Explanation: The longest substring is "leetminicowor" which contains two each of the vowels: e, i and o and zero of the vowels: a and u.
Example 2:

Input: s = "leetcodeisgreat"
Output: 5
Explanation: The longest substring is "leetc" which contains two e's.
Example 3:

Input: s = "bcbcbc"
Output: 6
Explanation: In this case, the given string "bcbcbc" is the longest because all vowels: a, e, i, o and u appear zero times.


Constraints:

1 <= s.length <= 5 x 10^5
s contains only lowercase English letters.
'''


class Solution(object):
    def findTheLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        status = [None for _ in range( 1<<5)]
        status[0] = 0
        a = "aeiou"
        hash_map = {a[i]: i for i in range(len(a))}
        init_statu = 0
        max_length = 0
        for i in range(len(s)):
            if s[i] in a:
                init_statu ^= 1 << hash_map[s[i]]

            if status[init_statu] is None:
                status[init_statu] = i + 1
            else:
                max_length = max(max_length, i+ 1 - status[init_statu])

        return max_length


# tips

'''
Represent the counts (odd or even) of vowels with a bitmask.

Precompute the prefix xor for the bitmask of vowels and then get the longest valid substring.
'''


# solutions


'''
方法一：前缀和 + 状态压缩
思路和算法

我们先来考虑暴力方法怎么做。最直观的方法无非就是枚举所有子串，遍历子串中的所有字符，统计元音字母出现的个数。如果符合条件，我们就更新答案，但这样肯定会因为超时而无法通过所有测试用例。

再回顾一下上面的操作，其实每个子串对应着一个区间，那么有什么方法可以在不重复遍历子串的前提下，快速求出这个区间里元音字母出现的次数呢？答案就是前缀和，对于一个区间，我们可以用两个前缀和的差值，得到其中某个字母的出现次数。

我们对每个元音字母维护一个前缀和，定义 \textit{pre}[i][k]pre[i][k] 表示在字符串前 ii 个字符中，第 kk 个元音字母一共出现的次数。假设我们需要求出 [l,r][l,r] 这个区间的子串是否满足条件，那么我们可以用 pre[r][k]-pre[l-1][k]pre[r][k]−pre[l−1][k]，在 O(1)O(1) 的时间得到第 kk 个元音字母出现的次数。对于每一个元音字母，我们都判断一下其是否出现偶数次即可。

我们利用前缀和优化了统计子串的时间复杂度，然而枚举所有子串的复杂度仍需要 O(n^2)O(n 
2
 )，不足以通过本题，还需要继续进行优化，避免枚举所有子串。我们考虑枚举字符串的每个位置 ii ，计算以它结尾的满足条件的最长字符串长度。其实我们要做的就是快速找到最小的 j \in [0,i)j∈[0,i)，满足 pre[i][k]-pre[j][k]pre[i][k]−pre[j][k]（即每一个元音字母出现的次数）均为偶数，那么以 ii 结尾的最长字符串 s[j+1,i]s[j+1,i] 长度就是 i-ji−j。

有经验的读者可能马上就想到了利用哈希表来优化查找的复杂度，但是单单利用前缀和，我们无法找到 ii 和 jj 相关的恒等式，像 1248. 统计优美子数组 这道题我们是能明确知道两个前缀的差值是恒定的。那难道就没办法了么？其实不然，这道题我们还有一个性质没有充分利用：我们需要找的子串中，每个元音字母都恰好出现了偶数次。

偶数这个条件其实告诉了我们，对于满足条件的子串而言，两个前缀和 pre[i][k]pre[i][k] 和 pre[j][k]pre[j][k] 的奇偶性一定是相同的，因为小学数学的知识告诉我们：奇数减奇数等于偶数，偶数减偶数等于偶数。因此我们可以对前缀和稍作修改，从维护元音字母出现的次数改作维护元音字母出现次数的奇偶性。这样我们只要实时维护每个元音字母出现的奇偶性，那么 s[j+1,i]s[j+1,i] 满足条件当且仅当对于所有的 kk，pre[i][k]pre[i][k] 和 pre[j][k]pre[j][k] 的奇偶性都相等，此时我们就可以利用哈希表存储每一种奇偶性（即考虑所有的元音字母）对应最早出现的位置，边遍历边更新答案。

题目做到这里基本上做完了，但是我们还可以进一步优化我们的编码方式，如果直接以每个元音字母出现次数的奇偶性为哈希表中的键，难免有些冗余，我们可能需要额外定义一个状态：

{
  a: cnta, // a 出现次数的奇偶性
  e: cnte, // e 出现次数的奇偶性
  i: cnti, // i 出现次数的奇偶性
  o: cnto, // o 出现次数的奇偶性
  u: cntu  // u 出现次数的奇偶性
}
将这么一个结构当作我们哈希表存储的键值，如果题目稍作修改扩大了字符集，那么维护起来可能会比较吃力。考虑到出现次数的奇偶性其实无非就两个值，00 代表出现了偶数次，11 代表出现了奇数次，我们可以将其压缩到一个二进制数中，第 kk 位的 00 或 11 代表了第 kk 个元音字母出现的奇偶性。举一个例子，假如到第 ii 个位置，u o i e a 出现的奇偶性分别为 1 1 0 0 1，那么我们就可以将其压成一个二进制数 (11001)_2=(25)_{10}(11001) 
2
​	
 =(25) 
10
​	
  作为它的状态。这样我们就可以将 55 个元音字母出现次数的奇偶性压缩到了一个二进制数中，且连续对应了二进制数的 [(00000)_2,(11111)_2][(00000) 
2
​	
 ,(11111) 
2
​	
 ] 的范围，转成十进制数即 [0,31][0,31]。因此我们也不再需要使用哈希表，直接用一个长度为 3232 的数组来存储对应状态出现的最早位置即可。

C++JavaScriptJavaC#Golang
class Solution {
public:
    int findTheLongestSubstring(string s) {
        int ans = 0, status = 0, n = s.length();
        vector<int> pos(1 << 5, -1);
        pos[0] = 0;
        for (int i = 0; i < n; ++i) {
            if (s[i] == 'a') {
                status ^= 1<<0;
            } else if (s[i] == 'e') {
                status ^= 1<<1;
            } else if (s[i] == 'i') {
                status ^= 1<<2;
            } else if (s[i] == 'o') {
                status ^= 1<<3;
            } else if (s[i] == 'u') {
                status ^= 1<<4;
            }
            if (~pos[status]) {
                ans = max(ans, i + 1 - pos[status]);
            } else {
                pos[status] = i + 1;
            }
        }
        return ans;
    }
};
复杂度分析

时间复杂度：O(n)O(n)，其中 nn 为字符串 ss 的长度。我们只需要遍历一遍字符串即可求得答案，因此时间复杂度为 O(n)O(n)。

空间复杂度：O(S)O(S)，其中 SS 表示元音字母压缩成一个状态数的最大值，在本题中 S = 32S=32。我们需要对应 SS 大小的空间来存放每个状态第一次出现的位置，因此需要 O(S)O(S) 的空间复杂度。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/solution/mei-ge-yuan-yin-bao-han-ou-shu-ci-de-zui-chang-z-2/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
