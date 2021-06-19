# encoding=utf8

'''
1239. Maximum Length of a Concatenated String with Unique Characters

Given an array of strings arr. String s is a concatenation of a sub-sequence of arr which have unique characters.

Return the maximum possible length of s.

 

Example 1:

Input: arr = ["un","iq","ue"]
Output: 4
Explanation: All possible concatenations are "","un","iq","ue","uniq" and "ique".
Maximum length is 4.
Example 2:

Input: arr = ["cha","r","act","ers"]
Output: 6
Explanation: Possible solutions are "chaers" and "acters".
Example 3:

Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
Output: 26
 

Constraints:

1 <= arr.length <= 16
1 <= arr[i].length <= 26
arr[i] contains only lower case English letters.

1239. 串联字符串的最大长度

给定一个字符串数组 arr，字符串 s 是将 arr 某一子序列字符串连接所得的字符串，如果 s 中的每一个字符都只出现过一次，那么它就是一个可行解。

请返回所有可行解 s 中最长长度。

 

示例 1：

输入：arr = ["un","iq","ue"]
输出：4
解释：所有可能的串联组合是 "","un","iq","ue","uniq" 和 "ique"，最大长度为 4。
示例 2：

输入：arr = ["cha","r","act","ers"]
输出：6
解释：可能的解答有 "chaers" 和 "acters"。
示例 3：

输入：arr = ["abcdefghijklmnopqrstuvwxyz"]
输出：26
 

提示：

1 <= arr.length <= 16
1 <= arr[i].length <= 26
arr[i] 中只含有小写英文字母
'''

# golang solution

'''
func maxLength(arr []string) int {
    masks := []int{}
outer:
    for _, s := range arr {
        mask := 0
        for _, ch := range s {
            ch -= 'a'
            if mask>>ch&1 > 0 { // 若 mask 已有 ch，则说明 s 含有重复字母，无法构成可行解
                continue outer
            }
            mask |= 1 << ch // 将 ch 加入 mask 中
        }
        masks = append(masks, mask)
    }
    fmt.Println(masks)

    var ans int
    var backtrack func(int, int)
    backtrack = func(pos, mask int) {
        if pos == len(masks) {
            ans = max(ans, bits.OnesCount(uint(mask)))
            return
        }
        if mask&masks[pos] == 0 { // mask 和 masks[pos] 无公共元素
            backtrack(pos+1, mask|masks[pos])
        }
        backtrack(pos+1, mask)
    }
    backtrack(0, 0)
    return ans
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}

'''

