# encoding=utf8


'''
374. Guess Number Higher or Lower

We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API int guess(int num), which returns 3 possible results:

-1: The number I picked is lower than your guess (i.e. pick < num).
1: The number I picked is higher than your guess (i.e. pick > num).
0: The number I picked is equal to your guess (i.e. pick == num).
Return the number that I picked.

 

Example 1:

Input: n = 10, pick = 6
Output: 6
Example 2:

Input: n = 1, pick = 1
Output: 1
Example 3:

Input: n = 2, pick = 1
Output: 1
Example 4:

Input: n = 2, pick = 2
Output: 2
 

Constraints:

1 <= n <= 231 - 1
1 <= pick <= n

374. 猜数字大小

猜数字游戏的规则如下：

每轮游戏，我都会从 1 到 n 随机选择一个数字。 请你猜选出的是哪个数字。
如果你猜错了，我会告诉你，你猜测的数字比我选出的数字是大了还是小了。
你可以通过调用一个预先定义好的接口 int guess(int num) 来获取猜测结果，返回值一共有 3 种可能的情况（-1，1 或 0）：

-1：我选出的数字比你猜的数字小 pick < num
1：我选出的数字比你猜的数字大 pick > num
0：我选出的数字和你猜的数字一样。恭喜！你猜对了！pick == num
返回我选出的数字。

 

示例 1：

输入：n = 10, pick = 6
输出：6
示例 2：

输入：n = 1, pick = 1
输出：1
示例 3：

输入：n = 2, pick = 1
输出：1
示例 4：

输入：n = 2, pick = 2
输出：2
 

提示：

1 <= n <= 231 - 1
1 <= pick <= n
'''


# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 1, n
        while l < r:
            mid = (l+r)/2
            res = guess(mid)
            if res == 0:
                return mid
            elif res > 0:
                l = mid + 1
            else:
                r = mid - 1
        return l


# golang solution

'''
/** 
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is lower than the guess number
 *			      1 if num is higher than the guess number
 *               otherwise return 0
 * func guess(num int) int;
 */

func guessNumber(n int) int {
    return sort.Search(n, func(i int) bool {
		return guess(i) <= 0
	})
}
'''



# solutions

'''
方法一：二分查找
记选出的数字为 \textit{pick}pick，猜测的数字为 xx。根据题目描述，若 \texttt{guess}(x)\le 0guess(x)≤0 则说明 x\ge\textit{pick}x≥pick，否则 x<\textit{pick}x<pick。

根据这一性质我们可以使用二分查找来求出答案 \textit{pick}pick。

二分时，记当前区间为 [\textit{left},\textit{right}][left,right]，初始时 \textit{left}=1left=1，\textit{right}=nright=n。记区间中间元素为 \textit{mid}mid，若有 \texttt{guess}(mid)\le 0guess(mid)≤0 则说明 \textit{pick} \in [\textit{left},\textit{mid}]pick∈[left,mid]，否则 \textit{pick} \in [\textit{mid}+1,\textit{right}]pick∈[mid+1,right]。当区间左右端点相同时，则说明我们找到了答案，退出循环。

C++JavaC#GolangJavaScriptCPython3

class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n
        while left < right:
            mid = (left + right) // 2
            if guess(mid) <= 0:
                right = mid   # 答案在区间 [left, mid] 中
            else:
                left = mid + 1   # 答案在区间 [mid+1, right] 中
        
        # 此时有 left == right，区间缩为一个点，即为答案
        return left
复杂度分析

时间复杂度：O(\log n)O(logn)。时间复杂度即为二分的次数，每次二分我们将区间的长度减小一半，直至区间长度为 11 时二分终止，而区间初始长度为 nn，因此二分次数为 O(\log n)O(logn)。

空间复杂度：O(1)O(1)。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/guess-number-higher-or-lower/solution/cai-shu-zi-da-xiao-by-leetcode-solution-qdzu/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''

