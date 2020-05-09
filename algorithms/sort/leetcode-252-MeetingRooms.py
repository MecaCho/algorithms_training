
'''
252. 会议室
给定一个会议时间安排的数组，每个会议时间都会包括开始和结束的时间 [[s1,e1],[s2,e2],...] (si < ei)，请你判断一个人是否能够参加这里面的全部会议。

示例 1:

输入: [[0,30],[5,10],[15,20]]
输出: false
示例 2:

输入: [[7,10],[2,4]]
输出: true

252. Meeting Rooms
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.

Example 1:

Input: [[0,30],[5,10],[15,20]]
Output: false
Example 2:

Input: [[7,10],[2,4]]
Output: true
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
'''




class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        intervals = sorted(intervals)
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i-1][1]:
                return False
        return True

'''
方法一：暴力法
最简单的方法是将数组中的会议全部两两比较，判断它们是否有冲突（即它们的时间是否有交叠）。若一个会议开始时另一个会议依然没有结束，则它们存在交叠。

class Solution {

  public boolean canAttendMeetings(int[][] intervals) {
    for (int i = 0; i < intervals.length; i++) {
      for (int j = i + 1; j < intervals.length; j++) {
        if (overlap(intervals[i], intervals[j]))
          return false;
      }
    }
    return true;
  }

  public static boolean overlap(int[] i1, int[] i2) {
    return ((i1[0] >= i2[0] && i1[0] < i2[1]) || (i2[0] >= i1[0] && i2[0] < i1[1]));
  }
}
交叠的情况

可以更简洁地编写上述代码中的交叠条件。考虑两个不交叠的会议。前面的会议在后面的会议开始之前结束。因此，两次会议的 最小 结束时间（即前面会议的结束时间）小于或等于两次会议的 最大 开始时间（即后面会议的开始时间)。



图 1. 两个不交叠的会议



图 2. 两个交叠的会议

因此可以这样重写：

public static boolean overlap(int[] i1, int[] i2) {
    return (Math.min(i1[1], i2[1]) >
            Math.max(i1[0], i2[0]));
}
复杂度分析

时间复杂度 : O(n^2)O(n 
2
 ) 。我们对每两个会议都进行了比较。
空间复杂度 : O(1)O(1) 。没有使用额外空间。
方法二：排序
思路是按照开始时间对会议进行排序。接着依次遍历会议，检查它是否在下个会议开始前结束。

class Solution {

  public boolean canAttendMeetings(int[][] intervals) {
    Arrays.sort(intervals, new Comparator<int[]>() {
      public int compare(int[] i1, int[] i2) {
        return i1[0] - i2[0];
      }
    });

    for (int i = 0; i < intervals.length - 1; i++) {
      if (intervals[i][1] > intervals[i + 1][0])
        return false;
    }
    return true;
  }
}
复杂度分析

时间复杂度 : O(n \log n)O(nlogn) 。时间复杂度由排序决定。一旦排序完成，只需要 O(n)O(n) 的时间来判断交叠。
空间复杂度 : O(1)O(1)。没有使用额外空间。

作者：LeetCode
链接：https://leetcode-cn.com/problems/meeting-rooms/solution/hui-yi-shi-by-leetcode/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
