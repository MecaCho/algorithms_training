# encoding=utf8


'''
539. Minimum Time Difference
Given a list of 24-hour clock time points in "HH:MM" format, return the minimum minutes difference between any two time-points in the list.
 

Example 1:

Input: timePoints = ["23:59","00:00"]
Output: 1
Example 2:

Input: timePoints = ["00:00","23:59","00:00"]
Output: 0
 

Constraints:

2 <= timePoints <= 2 * 104
timePoints[i] is in the format "HH:MM".
'''


class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        if len(timePoints) > 1440:
            return 0
        mins = [int(timePoints[i].split(":")[0])*60 + int(timePoints[i].split(":")[1]) for i in range(len(timePoints))]
        mins.sort()
        min_dif = 1440
        for i in range(1, len(mins)):
            if mins[i] - mins[i-1] < min_dif:
                min_dif = mins[i] - mins[i-1]

        return min(min_dif, mins[0] + 1440 - mins[-1])
        


