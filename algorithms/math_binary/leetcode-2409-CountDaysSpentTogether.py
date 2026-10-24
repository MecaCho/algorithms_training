# encoding=utf8


'''
2409. Count Days Spent Together
Alice and Bob are traveling to Rome for separate business meetings.

You are given 4 strings arriveAlice, leaveAlice, arriveBob, and leaveBob. Alice will be in the city from the dates arriveAlice to leaveAlice (inclusive), while Bob will be in the city from the dates arriveBob to leaveBob (inclusive). Each will be a 5-character string in the format "MM-DD", corresponding to the month and day of the date.

Return the total number of days that Alice and Bob are in Rome together.

You can assume that all dates occur in the same calendar year, which is not a leap year. Note that the number of days per month can be represented as: [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31].

 

Example 1:

Input: arriveAlice = "08-15", leaveAlice = "08-18", arriveBob = "08-16", leaveBob = "08-19"
Output: 3
Explanation: Alice will be in Rome from August 15 to August 18. Bob will be in Rome from August 16 to August 19. They are both in Rome together on August 16th, 17th, and 18th, so the answer is 3.

Example 2:

Input: arriveAlice = "10-01", leaveAlice = "10-31", arriveBob = "11-01", leaveBob = "12-31"
Output: 0
Explanation: There is no day when Alice and Bob are in Rome together, so we return 0.

 

Constraints:

All dates are provided in the format "MM-DD".
Alice and Bob's arrival dates are earlier than or equal to their leaving dates.
The given dates are valid dates of a non-leap year.


2409. 统计共同度过的日子数
Alice 和 Bob 计划分别去罗马开会。

给你四个字符串 arriveAlice ，leaveAlice ，arriveBob 和 leaveBob 。Alice 会在日期 arriveAlice 到 leaveAlice 之间在城市里（日期为闭区间），而 Bob 在日期 arriveBob 到 leaveBob 之间在城市里（日期为闭区间）。每个字符串都包含 5 个字符，格式为 "MM-DD" ，对应着一个日期的月和日。

请你返回 Alice 和 Bob 同时在罗马的天数。

你可以假设所有日期都在 同一个 自然年，而且 不是 闰年。每个月份的天数分别为：[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 。

 

示例 1：

输入：arriveAlice = "08-15", leaveAlice = "08-18", arriveBob = "08-16", leaveBob = "08-19"
输出：3
解释：Alice 从 8 月 15 号到 8 月 18 号在罗马。Bob 从 8 月 16 号到 8 月 19 号在罗马，他们同时在罗马的日期为 8 月 16、17 和 18 号。所以答案为 3 。

示例 2：

输入：arriveAlice = "10-01", leaveAlice = "10-31", arriveBob = "11-01", leaveBob = "12-31"
输出：0
解释：Alice 和 Bob 没有同时在罗马的日子，所以我们返回 0 。

 

提示：

所有日期的格式均为 "MM-DD" 。
Alice 和 Bob 的到达日期都 早于或等于 他们的离开日期。
题目测试用例所给出的日期均为 非闰年 的有效日期。
'''


class Solution:
    def countDaysTogether(
        self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str
    ) -> int:
        days = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

        def to_day_of_year(date: str) -> int:
            m = int(date[:2])
            d = int(date[3:])
            return sum(days[: m - 1]) + d

        start = max(to_day_of_year(arriveAlice), to_day_of_year(arriveBob))
        end = min(to_day_of_year(leaveAlice), to_day_of_year(leaveBob))
        return max(0, end - start + 1)


# golang solution

'''
func countDaysTogether(arriveAlice string, leaveAlice string, arriveBob string, leaveBob string) int {
	days := []int{31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31}

	toDayOfYear := func(s string) int {
		m := int(s[0]-'0')*10 + int(s[1]-'0')
		d := int(s[3]-'0')*10 + int(s[4]-'0')
		res := 0
		for i := 0; i < m-1; i++ {
			res += days[i]
		}
		res += d
		return res
	}

	startAlice := toDayOfYear(arriveAlice)
	endAlice := toDayOfYear(leaveAlice)
	startBob := toDayOfYear(arriveBob)
	endBob := toDayOfYear(leaveBob)

	start := startAlice
	if startBob > start {
		start = startBob
	}
	end := endAlice
	if endBob < end {
		end = endBob
	}

	if end < start {
		return 0
	}
	return end - start + 1
}
'''

# solutions

'''
思路和算法：
1. 日期转换为一年中的天数（序号）：
   - 题目给定的是非闰年的日期格式 "MM-DD"；
   - 每个月份的天数给定为 [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]；
   - 对于给定的字符串 "MM-DD"，提取出月份 m 和日期 d，将前 m - 1 个月的天数累加再加上日 d，即可将其映射为一年中的第几天（范围在 1 到 365 之间）。

2. 区间交集计算：
   - Alice 在罗马的区间为 [startAlice, endAlice]；
   - Bob 在罗马的区间为 [startBob, endBob]；
   - 两人同时在罗马的日期对应于两个闭区间的交集：
     * 交集的起始日期为 start = max(startAlice, startBob)；
     * 交集的结束日期为 end = min(endAlice, endBob)；
   - 若 end < start，说明两人在罗马的日期没有重叠，返回 0；
   - 否则，交集天数为 end - start + 1。

复杂度分析：
- 时间复杂度：O(1)，日期字符串长度固定为 5，月份至多为 12，所有计算均为常数级别的基本算术运算。
- 空间复杂度：O(1)，仅需常数级别的额外变量存储月份天数表及日序号。
'''

