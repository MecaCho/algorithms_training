# encoding=utf8


'''
781. Rabbits in Forest
In a forest, each rabbit has some color. Some subset of rabbits (possibly all of them) tell you how many other rabbits have the same color as them. Those answers are placed in an array.

Return the minimum number of rabbits that could be in the forest.

Examples:
Input: answers = [1, 1, 2]
Output: 5
Explanation:
The two rabbits that answered "1" could both be the same color, say red.
The rabbit than answered "2" can't be red or the answers would be inconsistent.
Say the rabbit that answered "2" was blue.
Then there should be 2 other blue rabbits in the forest that didn't answer into the array.
The smallest possible number of rabbits in the forest is therefore 5: 3 that answered plus 2 that didn't.

Input: answers = [10, 10, 10]
Output: 11

Input: answers = []
Output: 0
Note:

answers will have length at most 1000.
Each answers[i] will be an integer in the range [0, 999].


781. 森林中的兔子
森林中，每个兔子都有颜色。其中一些兔子（可能是全部）告诉你还有多少其他的兔子和自己有相同的颜色。我们将这些回答放在 answers 数组里。

返回森林中兔子的最少数量。

示例:
输入: answers = [1, 1, 2]
输出: 5
解释:
两只回答了 "1" 的兔子可能有相同的颜色，设为红色。
之后回答了 "2" 的兔子不会是红色，否则他们的回答会相互矛盾。
设回答了 "2" 的兔子为蓝色。
此外，森林中还应有另外 2 只蓝色兔子的回答没有包含在数组中。
因此森林中兔子的最少数量是 5: 3 只回答的和 2 只没有回答的。

输入: answers = [10, 10, 10]
输出: 11

输入: answers = []
输出: 0
说明:

answers 的长度最大为1000。
answers[i] 是在 [0, 999] 范围内的整数。
'''


class Solution(object):
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        counter = {}
        res = 0
        for i in range(len(answers)):
            if answers[i] not in counter or counter[answers[i]] == 0:
                res += 1 + answers[i]
                counter[answers[i]] = answers[i]
            else:
                counter[answers[i]] -= 1

        return res

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = Counter(answers)
        res = sum((x + y) // (y + 1) * (y + 1) for y, x in count.items())
        return res


# solutions


'''
方法一：贪心
思路

两只相同颜色的兔子看到的其他同色兔子数必然是相同的。反之，若两只兔子看到的其他同色兔子数不同，那么这两只兔子颜色也不同。

因此，将 \textit{answers}answers 中值相同的元素分为一组，对于每一组，计算出兔子的最少数量，然后将所有组的计算结果累加，就是最终的答案。

例如，现在有 1313 只兔子回答 55。假设其中有一只红色的兔子，那么森林中必然有 66 只红兔子。再假设其中还有一只蓝色的兔子，同样的道理森林中必然有 66 只蓝兔子。为了最小化可能的兔子数量，我们假设这 1212 只兔子都在这 1313 只兔子中。那么还有一只额外的兔子回答 55，这只兔子只能是其他的颜色，这一颜色的兔子也有 66 只。因此这种情况下最少会有 1818 只兔子。

一般地，如果有 xx 只兔子都回答 yy，则至少有 \lceil\dfrac{x}{y+1}\rceil⌈ 
y+1
x
​	
 ⌉ 种不同的颜色，且每种颜色有 y+1y+1 只兔子，因此兔子数至少为

\lceil\dfrac{x}{y+1}\rceil\cdot(y+1)
⌈ 
y+1
x
​	
 ⌉⋅(y+1)

我们可以用哈希表统计 \textit{answers}answers 中各个元素的出现次数，对每个元素套用上述公式计算，并将计算结果累加，即为最终答案。

代码

C++JavaGolangJavaScriptPython3C

func numRabbits(answers []int) (ans int) {
    count := map[int]int{}
    for _, y := range answers {
        count[y]++
    }
    for y, x := range count {
        ans += (x + y) / (y + 1) * (y + 1)
    }
    return
}
复杂度分析

时间复杂度：O(n)O(n)，其中 nn 是数组 \textit{answers}answers 的长度。

空间复杂度：O(n)O(n)。最坏情况下，哈希表中含有 nn 个元素。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/rabbits-in-forest/solution/sen-lin-zhong-de-tu-zi-by-leetcode-solut-kvla/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''

