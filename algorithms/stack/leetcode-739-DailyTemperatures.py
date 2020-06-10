'''
739. 每日温度
根据每日 气温 列表，请重新生成一个列表，对应位置的输出是需要再等待多久温度才会升高超过该日的天数。如果之后都不会升高，请在该位置用 0 来代替。

例如，给定一个列表 temperatures = [73, 74, 75, 71, 69, 72, 76, 73]，你的输出应该是 [1, 1, 4, 2, 1, 1, 0, 0]。

提示：气温 列表长度的范围是 [1, 30000]。每个气温的值的均为华氏度，都是在 [30, 100] 范围内的整数。

739. Daily Temperatures
Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100].
'''


class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        stack_t = []
        res = [0 for _ in T]
        for i, t in enumerate(T):
            while stack_t and t > stack_t[-1][1]:
                index, _ = stack_t.pop()
                res[index] = i - index
            stack_t.append((i, t))
        return res


# tips

'''
If the temperature is say, 70 today, then in the future a warmer temperature must be either 71, 72, 73, ..., 99, or 100. We could remember when all of them occur next.

'''


# solutions

'''
方法一：暴力
对于温度列表中的每个元素 T[i]，需要找到最小的下标 j，使得 i < j 且 T[i] < T[j]。

由于温度范围在 [30, 100] 之内，因此可以维护一个数组 next 记录每个温度第一次出现的下标。数组 next 中的元素初始化为无穷大，在遍历温度列表的过程中更新 next 的值。

反向遍历温度列表。对于每个元素 T[i]，在数组 next 中找到从 T[i] + 1 到 100 中每个温度第一次出现的下标，将其中的最小下标记为 warmerIndex，则 warmerIndex 为下一次温度比当天高的下标。如果 warmerIndex 不为无穷大，则 warmerIndex - i 即为下一次温度比当天高的等待天数，最后令 next[T[i]] = i。

为什么上述做法可以保证正确呢？因为遍历温度列表的方向是反向，当遍历到元素 T[i] 时，只有 T[i] 后面的元素被访问过，即对于任意 t，当 next[t] 不为无穷大时，一定存在 j 使得 T[j] == t 且 i < j。又由于遍历到温度列表中的每个元素时都会更新数组 next 中的对应温度的元素值，因此对于任意 t，当 next[t] 不为无穷大时，令 j = next[t]，则 j 是满足 T[j] == t 且 i < j 的最小下标。

JavaPython3C++Golang

func dailyTemperatures(T []int) []int {
    length := len(T)
    ans := make([]int, length)
    next := make([]int, 101)
    for i := 0; i < 101; i++ {
        next[i] = math.MaxInt32
    }
    for i := length - 1; i >= 0; i-- {
        warmerIndex := math.MaxInt32
        for t := T[i] + 1; t <= 100; t++ {
            if next[t] < warmerIndex {
                warmerIndex = next[t]
            }
        }
        if warmerIndex < math.MaxInt32 {
            ans[i] = warmerIndex - i
        }
        next[T[i]] = i
    }
    return ans
}
复杂度分析

时间复杂度：O(nm)O(nm)，其中 nn 是温度列表的长度，mm 是数组 next 的长度，在本题中温度不超过 100100，所以 mm 的值为 100100。反向遍历温度列表一遍，对于温度列表中的每个值，都要遍历数组 next 一遍。

空间复杂度：O(m)O(m)，其中 mm 是数组 next 的长度。除了返回值以外，需要维护长度为 mm 的数组 next 记录每个温度第一次出现的下标位置。

方法二：单调栈
可以维护一个存储下标的单调栈，从栈底到栈顶的下标对应的温度列表中的温度依次递减。如果一个下标在单调栈里，则表示尚未找到下一次温度更高的下标。

正向遍历温度列表。对于温度列表中的每个元素 T[i]，如果栈为空，则直接将 i 进栈，如果栈不为空，则比较栈顶元素 prevIndex 对应的温度 T[prevIndex] 和当前温度 T[i]，如果 T[i] > T[prevIndex]，则将 prevIndex 移除，并将 prevIndex 对应的等待天数赋为 i - prevIndex，重复上述操作直到栈为空或者栈顶元素对应的温度小于等于当前温度，然后将 i 进栈。

为什么可以在弹栈的时候更新 ans[prevIndex] 呢？因为在这种情况下，即将进栈的 i 对应的 T[i] 一定是 T[prevIndex] 右边第一个比它大的元素，试想如果 prevIndex 和 i 有比它大的元素，假设下标为 j，那么 prevIndex 一定会在下标 j 的那一轮被弹掉。

由于单调栈满足从栈底到栈顶元素对应的温度递减，因此每次有元素进栈时，会将温度更低的元素全部移除，并更新出栈元素对应的等待天数，这样可以确保等待天数一定是最小的。

以下用一个具体的例子帮助读者理解单调栈。对于温度列表 [73,74,75,71,69,72,76,73][73,74,75,71,69,72,76,73]，单调栈 \textit{stack}stack 的初始状态为空，答案 \textit{ans}ans 的初始状态是 [0,0,0,0,0,0,0,0][0,0,0,0,0,0,0,0]，按照以下步骤更新单调栈和答案，其中单调栈内的元素都是下标，括号内的数字表示下标在温度列表中对应的温度。

当 i=0i=0 时，单调栈为空，因此将 00 进栈。

\textit{stack}=[0(73)]stack=[0(73)]

\textit{ans}=[0,0,0,0,0,0,0,0]ans=[0,0,0,0,0,0,0,0]

当 i=1i=1 时，由于 7474 大于 7373，因此移除栈顶元素 00，赋值 ans[0]:=1-0ans[0]:=1−0，将 11 进栈。

\textit{stack}=[1(74)]stack=[1(74)]

\textit{ans}=[1,0,0,0,0,0,0,0]ans=[1,0,0,0,0,0,0,0]

当 i=2i=2 时，由于 7575 大于 7474，因此移除栈顶元素 11，赋值 ans[1]:=2-1ans[1]:=2−1，将 22 进栈。

\textit{stack}=[2(75)]stack=[2(75)]

\textit{ans}=[1,1,0,0,0,0,0,0]ans=[1,1,0,0,0,0,0,0]

当 i=3i=3 时，由于 7171 小于 7575，因此将 33 进栈。

\textit{stack}=[2(75),3(71)]stack=[2(75),3(71)]

\textit{ans}=[1,1,0,0,0,0,0,0]ans=[1,1,0,0,0,0,0,0]

当 i=4i=4 时，由于 6969 小于 7171，因此将 44 进栈。

\textit{stack}=[2(75),3(71),4(69)]stack=[2(75),3(71),4(69)]

\textit{ans}=[1,1,0,0,0,0,0,0]ans=[1,1,0,0,0,0,0,0]

当 i=5i=5 时，由于 7272 大于 6969 和 7171，因此依次移除栈顶元素 44 和 33，赋值 ans[4]:=5-4ans[4]:=5−4 和 ans[3]:=5-3ans[3]:=5−3，将 55 进栈。

\textit{stack}=[2(75),5(72)]stack=[2(75),5(72)]

\textit{ans}=[1,1,0,2,1,0,0,0]ans=[1,1,0,2,1,0,0,0]

当 i=6i=6 时，由于 7676 大于 7272 和 7575，因此依次移除栈顶元素 55 和 22，赋值 ans[5]:=6-5ans[5]:=6−5 和 ans[2]:=6-2ans[2]:=6−2，将 66 进栈。

\textit{stack}=[6(76)]stack=[6(76)]

\textit{ans}=[1,1,4,2,1,1,0,0]ans=[1,1,4,2,1,1,0,0]

当 i=7i=7 时，由于 7373 小于 7676，因此将 77 进栈。

\textit{stack}=[6(76),7(73)]stack=[6(76),7(73)]

\textit{ans}=[1,1,4,2,1,1,0,0]ans=[1,1,4,2,1,1,0,0]

JavaPython3C++Golang

func dailyTemperatures(T []int) []int {
    length := len(T)
    ans := make([]int, length)
    stack := []int{}
    for i := 0; i < length; i++ {
        temperature := T[i]
        for len(stack) > 0 && temperature > T[stack[len(stack)-1]] {
            prevIndex := stack[len(stack)-1]
            stack = stack[:len(stack)-1]
            ans[prevIndex] = i - prevIndex
        }
        stack = append(stack, i)
    }
    return ans
}
复杂度分析

时间复杂度：O(n)O(n)，其中 nn 是温度列表的长度。正向遍历温度列表一遍，对于温度列表中的每个下标，最多有一次进栈和出栈的操作。

空间复杂度：O(n)O(n)，其中 nn 是温度列表的长度。需要维护一个单调栈存储温度列表中的下标。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/daily-temperatures/solution/mei-ri-wen-du-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''

