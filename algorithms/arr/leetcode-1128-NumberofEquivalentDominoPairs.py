# encoding=utf8

'''
1128. Number of Equivalent Domino Pairs
Given a list of dominoes, dominoes[i] = [a, b] is equivalent to dominoes[j] = [c, d] if and only if either (a==c and b==d), or (a==d and b==c) - that is, one domino can be rotated to be equal to another domino.

Return the number of pairs (i, j) for which 0 <= i < j < dominoes.length, and dominoes[i] is equivalent to dominoes[j].



Example 1:

Input: dominoes = [[1,2],[2,1],[3,4],[5,6]]
Output: 1


Constraints:

1 <= dominoes.length <= 40000
1 <= dominoes[i][j] <= 9


1128. 等价多米诺骨牌对的数量
给你一个由一些多米诺骨牌组成的列表 dominoes。

如果其中某一张多米诺骨牌可以通过旋转 0 度或 180 度得到另一张多米诺骨牌，我们就认为这两张牌是等价的。

形式上，dominoes[i] = [a, b] 和 dominoes[j] = [c, d] 等价的前提是 a==c 且 b==d，或是 a==d 且 b==c。

在 0 <= i < j < dominoes.length 的前提下，找出满足 dominoes[i] 和 dominoes[j] 等价的骨牌对 (i, j) 的数量。



示例：

输入：dominoes = [[1,2],[2,1],[3,4],[5,6]]
输出：1


提示：

1 <= dominoes.length <= 40000
1 <= dominoes[i][j] <= 9
'''


class Solution(object):
    def numEquivDominoPairs(self, dominoes):
        """
        :type dominoes: List[List[int]]
        :rtype: int
        """
        nums = [0]*100
        res = 0
        for x, y in dominoes:
            val = x*10 + y if x > y else y*10 + x
            # if nums[val] > 0:
            res += nums[val]
            nums[val] += 1

        return res


# solutions

'''
方法一：二元组表示 + 计数
思路及解法

本题中我们需要统计所有等价的多米诺骨牌，其中多米诺骨牌使用二元对代表，「等价」的定义是，在允许翻转两个二元对的的情况下，使它们的元素一一对应相等。

于是我们不妨直接让每一个二元对都变为指定的格式，即第一维必须不大于第二维。这样两个二元对「等价」当且仅当两个二元对完全相同。

注意到二元对中的元素均不大于 99，因此我们可以将每一个二元对拼接成一个两位的正整数，即 (x, y) \to 10x + y(x,y)→10x+y。这样就无需使用哈希表统计元素数量，而直接使用长度为 100100 的数组即可。

代码

C++JavaJavaScriptGolangCPython3

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        num = [0] * 100
        ret = 0
        for x, y in dominoes:
            val = (x * 10 + y if x <= y else y * 10 + x)
            ret += num[val]
            num[val] += 1
        return ret
复杂度分析

时间复杂度：O(n)O(n)，其中 nn 是多米诺骨牌的数量。我们至多只需要遍历一次该数组。

空间复杂度：O(1)O(1)，我们只需要常数的空间存储若干变量。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/number-of-equivalent-domino-pairs/solution/deng-jie-duo-mi-nuo-gu-pai-dui-de-shu-li-yjlz/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
