# encoding=utf8

'''
3723. Maximize Sum of Squares of Digits
You are given two positive integers num and sum.

A positive integer n is good if it satisfies both of the following:

The number of digits in n is exactly num.
The sum of digits in n is exactly sum.
The score of a good integer n is the sum of the squares of digits in n.

Return a string denoting the good integer n that achieves the maximum score. If there are multiple possible integers, return the maximum one. If no such integer exists, return an empty string.

 

Example 1:

Input: num = 2, sum = 3
Output: "30"
Explanation:
There are 3 good integers: 12, 21, and 30.
- The score of 12 is 1^2 + 2^2 = 5.
- The score of 21 is 2^2 + 1^2 = 5.
- The score of 30 is 3^2 + 0^2 = 9.
The maximum score is 9, which is achieved by the good integer 30. Therefore, the answer is "30".

Example 2:

Input: num = 2, sum = 17
Output: "98"
Explanation:
There are 2 good integers: 89 and 98.
- The score of 89 is 8^2 + 9^2 = 145.
- The score of 98 is 9^2 + 8^2 = 145.
The maximum score is 145. The maximum good integer that achieves this score is 98. Therefore, the answer is "98".

Example 3:

Input: num = 1, sum = 10
Output: ""
Explanation:
There are no integers that have exactly 1 digit and whose digits sum to 10. Therefore, the answer is "".

 

Constraints:

1 <= num <= 2 * 10^5
1 <= sum <= 2 * 10^6


3723. 数位平方和的最大值
给你两个 正 整数 num 和 sum 。

如果一个正整数 n 满足以下两个条件，则称其为 好整数 ：
- n 的位数 恰好 为 num 。
- n 的各位数字之和 恰好 为 sum 。

一个 好整数 n 的 分数 定义为 n 的各位数字的平方和。

返回一个 字符串 ，表示能获得 最大 分数 的 好整数 n 。如果有多个可能的整数，返回 最大 的那个。如果不存在这样的整数，返回一个空字符串。

 

示例 1:

输入: num = 2, sum = 3
输出: "30"
解释:
有 3 个好整数：12、21 和 30。
- 12 的分数是 1^2 + 2^2 = 5 。
- 21 的分数是 2^2 + 1^2 = 5 。
- 30 的分数是 3^2 + 0^2 = 9 。
最大分数是 9，由好整数 30 获得。因此，答案是 "30" 。

示例 2:

输入: num = 2, sum = 17
输出: "98"
解释:
有两个好整数：89 和 98。
- 89 的分数是 8^2 + 9^2 = 145 。
- 98 的分数是 9^2 + 8^2 = 145 。
最大分数是 145。获得此分数的最大好整数是 98。因此，答案是 "98" 。

示例 3:

输入: num = 1, sum = 10
输出: ""
解释:
不存在恰好有 1 位数字且各位数字之和为 10 的整数。因此，答案是 "" 。

 

提示:

1 <= num <= 2 * 10^5
1 <= sum <= 2 * 10^6
'''


class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if num * 9 < sum:
            return ""

        k, s = divmod(sum, 9)
        ans = "9" * k
        if s > 0:
            ans += str(s)
        if len(ans) < num:
            ans += "0" * (num - len(ans))

        return ans


# golang solution

'''
import "strings"

func maxSumOfSquares(num int, sum int) string {
	if num*9 < sum {
		return ""
	}

	k, s := sum/9, sum%9
	var sb strings.Builder
	sb.Grow(num)
	sb.WriteString(strings.Repeat("9", k))
	if s > 0 {
		sb.WriteByte(byte('0' + s))
	}
	if rem := num - sb.Len(); rem > 0 {
		sb.WriteString(strings.Repeat("0", rem))
	}
	return sb.String()
}
'''


