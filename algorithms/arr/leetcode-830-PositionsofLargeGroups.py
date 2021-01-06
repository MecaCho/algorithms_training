# encoding=utf8
'''
830. Positions of Large Groups
In a string s of lowercase letters, these letters form consecutive groups of the same character.

For example, a string like s = "abbxxxxzyy" has the groups "a", "bb", "xxxx", "z", and "yy".

A group is identified by an interval [start, end], where start and end denote the start and end indices (inclusive) of the group. In the above example, "xxxx" has the interval [3,6].

A group is considered large if it has 3 or more characters.

Return the intervals of every large group sorted in increasing order by start index.



Example 1:

Input: s = "abbxxxxzzy"
Output: [[3,6]]
Explanation: "xxxx" is the only large group with start index 3 and end index 6.
Example 2:

Input: s = "abc"
Output: []
Explanation: We have groups "a", "b", and "c", none of which are large groups.
Example 3:

Input: s = "abcdddeeeeaabbbcd"
Output: [[3,5],[6,9],[12,14]]
Explanation: The large groups are "ddd", "eeee", and "bbb".
Example 4:

Input: s = "aba"
Output: []


Constraints:

1 <= s.length <= 1000
s contains lower-case English letters only.


830. 较大分组的位置
在一个由小写字母构成的字符串 s 中，包含由一些连续的相同字符所构成的分组。

例如，在字符串 s = "abbxxxxzyy" 中，就含有 "a", "bb", "xxxx", "z" 和 "yy" 这样的一些分组。

分组可以用区间 [start, end] 表示，其中 start 和 end 分别表示该分组的起始和终止位置的下标。上例中的 "xxxx" 分组用区间表示为 [3,6] 。

我们称所有包含大于或等于三个连续字符的分组为 较大分组 。

找到每一个 较大分组 的区间，按起始位置下标递增顺序排序后，返回结果。



示例 1：

输入：s = "abbxxxxzzy"
输出：[[3,6]]
解释："xxxx" 是一个起始于 3 且终止于 6 的较大分组。
示例 2：

输入：s = "abc"
输出：[]
解释："a","b" 和 "c" 均不是符合要求的较大分组。
示例 3：

输入：s = "abcdddeeeeaabbbcd"
输出：[[3,5],[6,9],[12,14]]
解释：较大分组为 "ddd", "eeee" 和 "bbb"
示例 4：

输入：s = "aba"
输出：[]

提示：

1 <= s.length <= 1000
s 仅含小写英文字母
'''



class Solution(object):
    def largeGroupPositions(self, s):
        """
        :type s: str
        :rtype: List[List[int]]
        """
        res = []
        pre = None
        start = 0
        s += "#"
        for i, c in enumerate(s):
            if c != pre:
                if i - start >= 3:
                    res.append([start, i-1])
                start = i
            pre = c
        return res


# solution


'''
方法一：一次遍历
思路及解法

我们可以遍历该序列，并记录当前分组的长度。如果下一个字符与当前字符不同，或者已经枚举到字符串尾部，就说明当前字符为当前分组的尾部。每次找到当前分组的尾部时，如果该分组长度达到 33，我们就将其加入答案。

代码

C++JavaGolangCJavaScriptPython3

class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        ret = list()
        n, num = len(s), 1

        for i in range(n):
            if i == n - 1 or s[i] != s[i + 1]:
                if num >= 3:
                    ret.append([i - num + 1, i])
                num = 1
            else:
                num += 1
        
        return ret
复杂度分析

时间复杂度：O(n)O(n)，其中 nn 是字符串的长度。我们只需要遍历一次该数组。

空间复杂度：O(1)O(1)。我们只需要常数的空间来保存若干变量，注意返回值不计入空间复杂度。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/positions-of-large-groups/solution/jiao-da-fen-zu-de-wei-zhi-by-leetcode-so-fi3n/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
