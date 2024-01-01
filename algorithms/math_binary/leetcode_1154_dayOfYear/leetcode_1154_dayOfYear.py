# encoding=utf8

'''
1154. Day of the Year
Given a string date representing a Gregorian calendar date formatted as YYYY-MM-DD, return the day number of the year.

 

Example 1:

Input: date = "2019-01-09"
Output: 9
Explanation: Given date is the 9th day of the year in 2019.
Example 2:

Input: date = "2019-02-10"
Output: 41
Example 3:

Input: date = "2003-03-01"
Output: 60
Example 4:

Input: date = "2004-03-01"
Output: 61
 

Constraints:

date.length == 10
date[4] == date[7] == '-', and all other date[i]'s are digits
date represents a calendar date between Jan 1st, 1900 and Dec 31, 2019.
'''

# golang 

'''
func dayOfYear(date string) int {
	year, _ := strconv.Atoi(date[:4])
	month, _ := strconv.Atoi(date[5:7])
	day, _ := strconv.Atoi(date[8:10])

    // fmt.Println(year, month, day)

	days := []int{31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31}
	if (year % 4 == 0 && year%100 != 0) || (year % 400 == 0){
		days[1] ++
	}
	
	res := 0
	for i := 0; i < month-1;i++{
		res += days[i]
	}
	res += day
	return res
}
'''

class Solution(object):
    def dayOfYear(self, date):
        """
        :type date: str
        :rtype: int
        """
        import time
        time_ = time.strptime(date, "%Y-%m-%d")
        print time_.tm_yday
        print time.strptime(str(date), "%Y-%m-%d").tm_yday
        return time_

if __name__ == '__main__':
    demo = Solution()
    demo.dayOfYear("2019-08-10")
