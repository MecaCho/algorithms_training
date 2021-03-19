# encoding=utf8

'''
503. Next Greater Element II
Given a circular array (the next element of the last element is the first element of the array), print the Next Greater Number for every element. The Next Greater Number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, output -1 for this number.

Example 1:
Input: [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2;
The number 2 can't find next greater number;
The second 1's next greater number needs to search circularly, which is also 2.
Note: The length of given array won't exceed 10000.

503. 下一个更大元素 II
给定一个循环数组（最后一个元素的下一个元素是数组的第一个元素），输出每个元素的下一个更大元素。数字 x 的下一个更大的元素是按数组遍历顺序，这个数字之后的第一个比它更大的数，这意味着你应该循环地搜索它的下一个更大的数。如果不存在，则输出 -1。

示例 1:

输入: [1,2,1]
输出: [2,-1,2]
解释: 第一个 1 的下一个更大的数是 2；
数字 2 找不到下一个更大的数；
第二个 1 的下一个最大的数需要循环搜索，结果也是 2。
注意: 输入数组的长度不会超过 10000。

'''


class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        ret = [-1] * n
        stk = list()

        for i in range(n * 2 - 1):
            while stk and nums[stk[-1]] < nums[i % n]:
                ret[stk.pop()] = nums[i % n]
            stk.append(i % n)

        return ret



class Solution20210319(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res = [-1] * n
        stack = []

        for i in range(n*2):
            while stack and nums[stack[-1]] < nums[i%n]:
                res[stack.pop()] = nums[i%n]

            stack.append(i%n)

        return res




# solutions


'''
方法一：单调栈 + 循环数组
思路及算法

我们可以使用单调栈解决本题。单调栈中保存的是下标，从栈底到栈顶的下标在数组 \textit{nums}nums 中对应的值是单调不升的。

每次我们移动到数组中的一个新的位置 ii，我们就将当前单调栈中所有对应值小于 \textit{nums}[i]nums[i] 的下标弹出单调栈，这些值的下一个更大元素即为 \textit{nums}[i]nums[i]（证明很简单：如果有更靠前的更大元素，那么这些位置将被提前弹出栈）。随后我们将位置 ii 入栈。

但是注意到只遍历一次序列是不够的，例如序列 [2,3,1][2,3,1]，最后单调栈中将剩余 [3,1][3,1]，其中元素 [1][1] 的下一个更大元素还是不知道的。

一个朴素的思想是，我们可以把这个循环数组「拉直」，即复制该序列的前 n-1n−1 个元素拼接在原序列的后面。这样我们就可以将这个新序列当作普通序列，用上文的方法来处理。

而在本题中，我们不需要显性地将该循环数组「拉直」，而只需要在处理时对下标取模即可。

代码

C++JavaJavaScriptPython3GolangC

func nextGreaterElements(nums []int) []int {
    n := len(nums)
    ans := make([]int, n)
    for i := range ans {
        ans[i] = -1
    }
    stack := []int{}
    for i := 0; i < n*2-1; i++ {
        for len(stack) > 0 && nums[stack[len(stack)-1]] < nums[i%n] {
            ans[stack[len(stack)-1]] = nums[i%n]
            stack = stack[:len(stack)-1]
        }
        stack = append(stack, i%n)
    }
    return ans
}
复杂度分析

时间复杂度: O(n)O(n)，其中 nn 是序列的长度。我们需要遍历该数组中每个元素最多 22 次，每个元素出栈与入栈的总次数也不超过 44 次。

空间复杂度: O(n)O(n)，其中 nn 是序列的长度。空间复杂度主要取决于栈的大小，栈的大小至多为 2n-12n−1。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/next-greater-element-ii/solution/xia-yi-ge-geng-da-yuan-su-ii-by-leetcode-bwam/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''

