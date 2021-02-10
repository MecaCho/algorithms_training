# encoding=utf8

'''
567. Permutation in String
Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.



Example 1:

Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input:s1= "ab" s2 = "eidboaoo"
Output: False


Constraints:

The input strings only contain lower case letters.
The length of both given strings is in range [1, 10,000].


567. 字符串的排列
给定两个字符串 s1 和 s2，写一个函数来判断 s2 是否包含 s1 的排列。

换句话说，第一个字符串的排列之一是第二个字符串的子串。

示例1:

输入: s1 = "ab" s2 = "eidbaooo"
输出: True
解释: s2 包含 s1 的排列之一 ("ba").


示例2:

输入: s1= "ab" s2 = "eidboaoo"
输出: False


注意：

输入的字符串只包含小写字母
两个字符串的长度都在 [1, 10,000] 之间
'''




class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        counter1, counter2 = [0]*26,[0]*26
        i = 0
        length_s1 = len(s1)
        if length_s1 > len(s2):
            return False
        while i < len(s1):
            counter1[ord(s1[i]) - ord("a")] += 1
            counter2[ord(s2[i]) - ord("a")] += 1
            i += 1
        if counter2 == counter1:
            return True

        # print(counter1, counter2)
        while i < len(s2):
            counter2[ord(s2[i]) - ord("a")] += 1
            counter2[ord(s2[i-length_s1]) - ord("a")] -= 1
            if counter2 == counter1:
                return True
            # print(counter1, counter2)
            i += 1

        return False


# solutions

'''
方法一：滑动窗口
由于排列不会改变字符串中每个字符的个数，所以只有当两个字符串每个字符的个数均相等时，一个字符串才是另一个字符串的排列。

根据这一性质，记 s_1s 
1
​	
  的长度为 nn，我们可以遍历 s_2s 
2
​	
  中的每个长度为 nn 的子串，判断子串和 s_1s 
1
​	
  中每个字符的个数是否相等，若相等则说明该子串是 s_1s 
1
​	
  的一个排列。

使用两个数组 \textit{cnt}_1cnt 
1
​	
  和 \textit{cnt}_2cnt 
2
​	
 ，\textit{cnt}_1cnt 
1
​	
  统计 s_1s 
1
​	
  中各个字符的个数，\textit{cnt}_2cnt 
2
​	
  统计当前遍历的子串中各个字符的个数。

由于需要遍历的子串长度均为 nn，我们可以使用一个固定长度为 nn 的滑动窗口来维护 \textit{cnt}_2cnt 
2
​	
 ：滑动窗口每向右滑动一次，就多统计一次进入窗口的字符，少统计一次离开窗口的字符。然后，判断 \textit{cnt}_1cnt 
1
​	
  是否与 \textit{cnt}_2cnt 
2
​	
  相等，若相等则意味着 s_1s 
1
​	
  的排列之一是 s_2s 
2
​	
  的子串。

C++JavaGolangCJavaScript

func checkInclusion(s1, s2 string) bool {
    n, m := len(s1), len(s2)
    if n > m {
        return false
    }
    var cnt1, cnt2 [26]int
    for i, ch := range s1 {
        cnt1[ch-'a']++
        cnt2[s2[i]-'a']++
    }
    if cnt1 == cnt2 {
        return true
    }
    for i := n; i < m; i++ {
        cnt2[s2[i]-'a']++
        cnt2[s2[i-n]-'a']--
        if cnt1 == cnt2 {
            return true
        }
    }
    return false
}
优化

注意到每次窗口滑动时，只统计了一进一出两个字符，却比较了整个 \textit{cnt}_1cnt 
1
​	
  和 \textit{cnt}_2cnt 
2
​	
  数组。

从这个角度出发，我们可以用一个变量 \textit{diff}diff 来记录 \textit{cnt}_1cnt 
1
​	
  与 \textit{cnt}_2cnt 
2
​	
  的不同值的个数，这样判断 \textit{cnt}_1cnt 
1
​	
  和 \textit{cnt}_2cnt 
2
​	
  是否相等就转换成了判断 \textit{diff}diff 是否为 00.

每次窗口滑动，记一进一出两个字符为 xx 和 yy.

若 x=yx=y 则对 \textit{cnt}_2cnt 
2
​	
  无影响，可以直接跳过。

若 x\ne yx 

​	
 =y，对于字符 xx，在修改 \textit{cnt}_2cnt 
2
​	
  之前若有 \textit{cnt}_2[x]=\textit{cnt}_1[x]cnt 
2
​	
 [x]=cnt 
1
​	
 [x]，则将 \textit{diff}diff 加一；在修改 \textit{cnt}_2cnt 
2
​	
  之后若有 \textit{cnt}_2[x]=\textit{cnt}_1[x]cnt 
2
​	
 [x]=cnt 
1
​	
 [x]，则将 \textit{diff}diff 减一。字符 yy 同理。

此外，为简化上述逻辑，我们可以只用一个数组 \textit{cnt}cnt，其中 \textit{cnt}[x]=\textit{cnt}_2[x]-\textit{cnt}_1[x]cnt[x]=cnt 
2
​	
 [x]−cnt 
1
​	
 [x]，将 \textit{cnt}_1[x]cnt 
1
​	
 [x] 与 \textit{cnt}_2[x]cnt 
2
​	
 [x] 的比较替换成 \textit{cnt}[x]cnt[x] 与 00 的比较。

C++JavaGolangCJavaScript

func checkInclusion(s1, s2 string) bool {
    n, m := len(s1), len(s2)
    if n > m {
        return false
    }
    cnt := [26]int{}
    for i, ch := range s1 {
        cnt[ch-'a']--
        cnt[s2[i]-'a']++
    }
    diff := 0
    for _, c := range cnt[:] {
        if c != 0 {
            diff++
        }
    }
    if diff == 0 {
        return true
    }
    for i := n; i < m; i++ {
        x, y := s2[i]-'a', s2[i-n]-'a'
        if x == y {
            continue
        }
        if cnt[x] == 0 {
            diff++
        }
        cnt[x]++
        if cnt[x] == 0 {
            diff--
        }
        if cnt[y] == 0 {
            diff++
        }
        cnt[y]--
        if cnt[y] == 0 {
            diff--
        }
        if diff == 0 {
            return true
        }
    }
    return false
}
复杂度分析

时间复杂度：O(n+m+|\Sigma|)O(n+m+∣Σ∣)，其中 nn 是字符串 s_1s 
1
​	
  的长度，mm 是字符串 s_2s 
2
​	
  的长度，\SigmaΣ 是字符集，这道题中的字符集是小写字母，|\Sigma|=26∣Σ∣=26。

空间复杂度：O(|\Sigma|)O(∣Σ∣)。

方法二：双指针
回顾方法一的思路，我们在保证区间长度为 nn 的情况下，去考察是否存在一个区间使得 \textit{cnt}cnt 的值全为 00。

反过来，还可以在保证 \textit{cnt}cnt 的值不为正的情况下，去考察是否存在一个区间，其长度恰好为 nn。

初始时，仅统计 s_1s 
1
​	
  中的字符，则 \textit{cnt}cnt 的值均不为正，且元素值之和为 -n−n。

然后用两个指针 \textit{left}left 和 \textit{right}right 表示考察的区间 [\textit{left},\textit{right}][left,right]。\textit{right}right 每向右移动一次，就统计一次进入区间的字符 xx。为保证 \textit{cnt}cnt 的值不为正，若此时 \textit{cnt}[x]>0cnt[x]>0，则向右移动左指针，减少离开区间的字符的 \textit{cnt}cnt 值直到 \textit{cnt}[x] \le 0cnt[x]≤0。

注意到 [\textit{left},\textit{right}][left,right] 的长度每增加 11，\textit{cnt}cnt 的元素值之和就增加 11。当 [\textit{left},\textit{right}][left,right] 的长度恰好为 nn 时，就意味着 \textit{cnt}cnt 的元素值之和为 00。由于 \textit{cnt}cnt 的值不为正，元素值之和为 00 就意味着所有元素均为 00，这样我们就找到了一个目标子串。

C++JavaGolangCJavaScript

func checkInclusion(s1, s2 string) bool {
    n, m := len(s1), len(s2)
    if n > m {
        return false
    }
    cnt := [26]int{}
    for _, ch := range s1 {
        cnt[ch-'a']--
    }
    left := 0
    for right, ch := range s2 {
        x := ch - 'a'
        cnt[x]++
        for cnt[x] > 0 {
            cnt[s2[left]-'a']--
            left++
        }
        if right-left+1 == n {
            return true
        }
    }
    return false
}
复杂度分析

时间复杂度：O(n+m+|\Sigma|)O(n+m+∣Σ∣)。双指针遍历 s_2s 
2
​	
  时，由于 \textit{left}left 和 \textit{right}right 都只会向右移动，故这一部分的复杂度是 O(m)O(m)。

空间复杂度：O(|\Sigma|)O(∣Σ∣)。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/permutation-in-string/solution/zi-fu-chuan-de-pai-lie-by-leetcode-solut-7k7u/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
