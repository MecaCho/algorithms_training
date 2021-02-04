# encoding=utf8


'''
514. Freedom Trail
In the video game Fallout 4, the quest "Road to Freedom" requires players to reach a metal dial called the "Freedom Trail Ring", and use the dial to spell a specific keyword in order to open the door.

Given a string ring, which represents the code engraved on the outer ring and another string key, which represents the keyword needs to be spelled. You need to find the minimum number of steps in order to spell all the characters in the keyword.

Initially, the first character of the ring is aligned at 12:00 direction. You need to spell all the characters in the string key one by one by rotating the ring clockwise or anticlockwise to make each character of the string key aligned at 12:00 direction and then by pressing the center button.

At the stage of rotating the ring to spell the key character key[i]:

You can rotate the ring clockwise or anticlockwise one place, which counts as 1 step. The final purpose of the rotation is to align one of the string ring's characters at the 12:00 direction, where this character must equal to the character key[i].
If the character key[i] has been aligned at the 12:00 direction, you need to press the center button to spell, which also counts as 1 step. After the pressing, you could begin to spell the next character in the key (next stage), otherwise, you've finished all the spelling.
Example:



Input: ring = "godding", key = "gd"
Output: 4
Explanation:
For the first key character 'g', since it is already in place, we just need 1 step to spell this character.
For the second key character 'd', we need to rotate the ring "godding" anticlockwise by two steps to make it become "ddinggo".
Also, we need 1 more step for spelling.
So the final output is 4.
Note:

Length of both ring and key will be in range 1 to 100.
There are only lowercase letters in both strings and might be some duplcate characters in both strings.
It's guaranteed that string key could always be spelled by rotating the string ring.

514. 自由之路
视频游戏“辐射4”中，任务“通向自由”要求玩家到达名为“Freedom Trail Ring”的金属表盘，并使用表盘拼写特定关键词才能开门。

给定一个字符串 ring，表示刻在外环上的编码；给定另一个字符串 key，表示需要拼写的关键词。您需要算出能够拼写关键词中所有字符的最少步数。

最初，ring 的第一个字符与12:00方向对齐。您需要顺时针或逆时针旋转 ring 以使 key 的一个字符在 12:00 方向对齐，然后按下中心按钮，以此逐个拼写完 key 中的所有字符。

旋转 ring 拼出 key 字符 key[i] 的阶段中：

您可以将 ring 顺时针或逆时针旋转一个位置，计为1步。旋转的最终目的是将字符串 ring 的一个字符与 12:00 方向对齐，并且这个字符必须等于字符 key[i] 。
如果字符 key[i] 已经对齐到12:00方向，您需要按下中心按钮进行拼写，这也将算作 1 步。按完之后，您可以开始拼写 key 的下一个字符（下一阶段）, 直至完成所有拼写。
示例：





输入: ring = "godding", key = "gd"
输出: 4
解释:
 对于 key 的第一个字符 'g'，已经在正确的位置, 我们只需要1步来拼写这个字符。
 对于 key 的第二个字符 'd'，我们需要逆时针旋转 ring "godding" 2步使它变成 "ddinggo"。
 当然, 我们还需要1步进行拼写。
 因此最终的输出是 4。
提示：

ring 和 key 的字符串长度取值范围均为 1 至 100；
两个字符串中都只有小写字符，并且均可能存在重复字符；
字符串 key 一定可以由字符串 ring 旋转拼出。
'''


import collections


class Solution(object):
    def findRotateSteps(self, ring, key):
        """
        :type ring: str
        :type key: str
        :rtype: int
        """
        dic = collections.defaultdict(list)
        for i, ch in enumerate(ring):
            dic[ch].append(i)
        N = len(ring)

        dp = [(0, 0)]

        for char in key:
            dp = [
                min([(1 + pre_cost + min(abs(pos - pre_pos), N - abs(pos - pre_pos)), pos) for pre_cost, pre_pos in dp])
                for pos in dic[char]]
        return min(dp)[0]



# solutions

'''
方法一：动态规划
定义 \textit{dp}[i][j]dp[i][j] 表示从前往后拼写出 \textit{key}key 的第 ii 个字符， \textit{ring}ring 的第 jj 个字符与 12:0012:00 方向对齐的最少步数（下标均从 00 开始）。

显然，只有当字符串 \textit{ring}ring 的第 jj 个字符需要和 \textit{key}key 的第 ii 个字符相同时才能拼写出 \textit{key}key 的第 ii 个字符，因此对于 \textit{key}key 的第 ii 个字符，需要考虑计算的 \textit{ring}ring 的第 jj 个字符只有 \textit{key}[i]key[i] 在 \textit{ring}ring 中出现的下标集合。我们对每个字符维护一个位置数组 \textit{pos}[i]pos[i]，表示字符 ii 在 \textit{ring}ring 中出现的位置集合，用来加速计算转移的过程。

对于状态 \textit{dp}[i][j]dp[i][j]，需要枚举上一次与 12:0012:00 方向对齐的位置 kk，因此可以列出如下的转移方程：

\textit{dp}[i][j]=\min_{k \in pos[key[i-1]]}\{dp[i-1][k]+\min\{\text{abs}(j-k),n-\text{abs}(j-k)\}+1\}
dp[i][j]= 
k∈pos[key[i−1]]
min
​	
 {dp[i−1][k]+min{abs(j−k),n−abs(j−k)}+1}

其中 \min\{\text{abs}(j-k),n-\text{abs}(j-k)\}+1min{abs(j−k),n−abs(j−k)}+1 表示在当前第 kk 个字符与 12:0012:00 方向对齐时第 jj 个字符旋转到 12:0012:00 方向并按下拼写的最少步数。

最后答案即为 \min_{i=0}^{n-1}\{\textit{dp}[m-1][i]\}min 
i=0
n−1
​	
 {dp[m−1][i]}。

这样的做法需要开辟 O(mn)O(mn) 的空间来存放 \textit{dp}dp 值。考虑到每次转移状态 \textit{dp}[i][]dp[i][] 只会从 \textit{dp}[i-1][]dp[i−1][] 转移过来，因此我们可以利用滚动数组优化第一维的空间复杂度，有能力的读者可以尝试实现。下面只给出最朴素的 O(mn)O(mn) 空间复杂度的实现。

C++JavaJavaScriptGolangC

func findRotateSteps(ring string, key string) int {
    const inf = math.MaxInt64 / 2
    n, m := len(ring), len(key)
    pos := [26][]int{}
    for i, c := range ring {
        pos[c-'a'] = append(pos[c-'a'], i)
    }
    dp := make([][]int, m)
    for i := range dp {
        dp[i] = make([]int, n)
        for j := range dp[i] {
            dp[i][j] = inf
        }
    }
    for _, p := range pos[key[0]-'a'] {
        dp[0][p] = min(p, n-p) + 1
    }
    for i := 1; i < m; i++ {
        for _, j := range pos[key[i]-'a'] {
            for _, k := range pos[key[i-1]-'a'] {
                dp[i][j] = min(dp[i][j], dp[i-1][k]+min(abs(j-k), n-abs(j-k))+1)
            }
        }
    }
    return min(dp[m-1]...)
}

func min(a ...int) int {
    res := a[0]
    for _, v := range a[1:] {
        if v < res {
            res = v
        }
    }
    return res
}

func abs(x int) int {
    if x < 0 {
        return -x
    }
    return x
}
复杂度分析

时间复杂度：O(mn^2)O(mn 
2
 )，其中 mm 为字符串 \textit{key}key 的长度，nn 为字符串 \textit{ring}ring 的长度。一共有 O(mn)O(mn) 个状态要计算，每次转移的时间复杂度为 O(n)O(n)，因此时间复杂度为 O(mn^2)O(mn 
2
 )。
由于维护了位置数组 \textit{pos}pos 加速了状态的计算与转移，因此 O(mn^2)O(mn 
2
 ) 是一个较松的上界，很多情况下的时间复杂度都会低于 O(mn^2)O(mn 
2
 )。

空间复杂度：O(mn)O(mn)。需要使用 O(mn)O(mn) 的空间来存放 \textit{dp}dp 数组，以及使用 O(n)O(n) 的空间来存放 \textit{pos}pos 数组，因此总空间复杂度为 O(mn)O(mn)。如果利用滚动数组，则可以将 \textit{dp}dp 数组的空间复杂度降低到 O(n)O(n)，总空间复杂度降低到 O(n)O(n)。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/freedom-trail/solution/zi-you-zhi-lu-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
