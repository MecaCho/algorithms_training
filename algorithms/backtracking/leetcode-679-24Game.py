# encoding=utf8

'''
679. 24 Game

You have 4 cards each containing a number from 1 to 9. You need to judge whether they could operated through *, /, +, -, (, ) to get the value of 24.

Example 1:
Input: [4, 1, 8, 7]
Output: True
Explanation: (8-4) * (7-1) = 24
Example 2:
Input: [1, 2, 1, 2]
Output: False
Note:
The division operator / represents real division, not integer division. For example, 4 / (1 - 2/3) = 12.
Every operation done is between two numbers. In particular, we cannot use - as a unary operator. For example, with [1, 1, 1, 1] as input, the expression -1 - 1 - 1 - 1 is not allowed.
You cannot concatenate numbers together. For example, if the input is [1, 2, 1, 2], we cannot write this as 12 + 12.

679. 24 点游戏

你有 4 张写有 1 到 9 数字的牌。你需要判断是否能通过 *，/，+，-，(，) 的运算得到 24。

示例 1:

输入: [4, 1, 8, 7]
输出: True
解释: (8-4) * (7-1) = 24
示例 2:

输入: [1, 2, 1, 2]
输出: False
注意:

除法运算符 / 表示实数除法，而不是整数除法。例如 4 / (1 - 2/3) = 12 。
每个运算符对两个数进行运算。特别是我们不能用 - 作为一元运算符。例如，[1, 1, 1, 1] 作为输入时，表达式 -1 - 1 - 1 - 1 是不允许的。
你不能将数字连接在一起。例如，输入为 [1, 2, 1, 2] 时，不能写成 12 + 12 。
'''



class Solution(object):
    def judgePoint24(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        EPSILON = 1e-6
        add = lambda x,y:x+y
        ops = [lambda x,y:x+y, lambda x,y:x*y,lambda x,y:x-y,lambda x,y:float(x)/y]


        def solve(nums):
            if not nums:
                return False
            if len(nums) == 1:
                return abs(nums[0] - 24) < EPSILON
            for i, x in enumerate(nums):
                for j, y in enumerate(nums):
                    if i != j:
                        newNums = list()
                        for k, z in enumerate(nums):
                            if k != i and k != j:
                                newNums.append(z)
                        for k,op in enumerate(ops):
                            if k < 2 and i > j:
                                continue
                            if k == 3:
                                if abs(y) < EPSILON:
                                    continue
                            newNums.append(op(x,y))
                            if solve(newNums):
                                return True
                            newNums.pop()
            return False

        return solve(nums)


# solution

'''
方法一：回溯
一共有 44 个数和 33 个运算操作，因此可能性非常有限。一共有多少种可能性呢？

首先从 44 个数字中有序地选出 22 个数字，共有 4 \times 3=124×3=12 种选法，并选择加、减、乘、除 44 种运算操作之一，用得到的结果取代选出的 22 个数字，剩下 33 个数字。

然后在剩下的 33 个数字中有序地选出 22 个数字，共有 3 \times 2=63×2=6 种选法，并选择 44 种运算操作之一，用得到的结果取代选出的 22 个数字，剩下 22 个数字。

最后剩下 22 个数字，有 22 种不同的顺序，并选择 44 种运算操作之一。

因此，一共有 12 \times 4 \times 6 \times 4 \times 2 \times 4=921612×4×6×4×2×4=9216 种不同的可能性。

可以通过回溯的方法遍历所有不同的可能性。具体做法是，使用一个列表存储目前的全部数字，每次从列表中选出 22 个数字，再选择一种运算操作，用计算得到的结果取代选出的 22 个数字，这样列表中的数字就减少了 11 个。重复上述步骤，直到列表中只剩下 11 个数字，这个数字就是一种可能性的结果，如果结果等于 2424，则说明可以通过运算得到 2424。如果所有的可能性的结果都不等于 2424，则说明无法通过运算得到 2424。

实现时，有一些细节需要注意。

除法运算为实数除法，因此结果为浮点数，列表中存储的数字也都是浮点数。在判断结果是否等于 2424 时应考虑精度误差，这道题中，误差小于 10^{-6}10 
−6
  可以认为是相等。

进行除法运算时，除数不能为 00，如果遇到除数为 00 的情况，则这种可能性可以直接排除。由于列表中存储的数字是浮点数，因此判断除数是否为 00 时应考虑精度误差，这道题中，当一个数字的绝对值小于 10^{-6}10 
−6
  时，可以认为该数字等于 00。

还有一个可以优化的点。

加法和乘法都满足交换律，因此如果选择的运算操作是加法或乘法，则对于选出的 22 个数字不需要考虑不同的顺序，在遇到第二种顺序时可以不进行运算，直接跳过。
JavaC++CPython3Golang

const (
    TARGET = 24
    EPSILON = 1e-6
    ADD, MULTIPLY, SUBTRACT, DIVIDE = 0, 1, 2, 3
)

func judgePoint24(nums []int) bool {
    list := []float64{}
    for _, num := range nums {
        list = append(list, float64(num))
    }
    return solve(list)
}

func solve(list []float64) bool {
    if len(list) == 0 {
        return false
    }
    if len(list) == 1 {
        return abs(list[0] - TARGET) < EPSILON
    }
    size := len(list)
    for i := 0; i < size; i++ {
        for j := 0; j < size; j++ {
            if i != j {
                list2 := []float64{}
                for k := 0; k < size; k++ {
                    if k != i && k != j {
                        list2 = append(list2, list[k])
                    }
                }
                for k := 0; k < 4; k++ {
                    if k < 2 && i < j {
                        continue
                    }
                    switch k {
                    case ADD:
                        list2 = append(list2, list[i] + list[j])
                    case MULTIPLY:
                        list2 = append(list2, list[i] * list[j])
                    case SUBTRACT:
                        list2 = append(list2, list[i] - list[j])
                    case DIVIDE:
                        if abs(list[j]) < EPSILON {
                            continue
                        } else {
                            list2 = append(list2, list[i] / list[j])
                        }
                    }
                    if solve(list2) {
                        return true
                    }
                    list2 = list2[:len(list2) - 1]
                }
            }
        }
    }
    return false
}

func abs(x float64) float64 {
    if x < 0 {
        return -x
    }
    return x
}
复杂度分析

时间复杂度：O(1)O(1)。一共有 92169216 种可能性，对于每种可能性，各项操作的时间复杂度都是 O(1)O(1)，因此总时间复杂度是 O(1)O(1)。

空间复杂度：O(1)O(1)。空间复杂度取决于递归调用层数与存储中间状态的列表，因为一共有 44 个数，所以递归调用的层数最多为 44，存储中间状态的列表最多包含 44 个元素，因此空间复杂度为常数。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/24-game/solution/24-dian-you-xi-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
