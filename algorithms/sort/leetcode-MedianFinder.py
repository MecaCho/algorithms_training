'''
面试题41. 数据流中的中位数
如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。

例如，

[2,3,4] 的中位数是 3

[2,3] 的中位数是 (2 + 3) / 2 = 2.5

设计一个支持以下两种操作的数据结构：

void addNum(int num) - 从数据流中添加一个整数到数据结构中。
double findMedian() - 返回目前所有元素的中位数。
示例 1：

输入：
["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"]
[[],[1],[2],[],[3],[]]
输出：[null,null,null,1.50000,null,2.00000]
示例 2：

输入：
["MedianFinder","addNum","findMedian","addNum","findMedian"]
[[],[2],[],[3],[]]
输出：[null,null,2.00000,null,2.50000]


限制：

最多会对 addNum、findMedia进行 50000 次调用。
注意：本题与主站 295 题相同：https://leetcode-cn.com/problems/find-median-from-data-stream/
'''


class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.vals = []


    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        self.vals.append(num)




    def findMedian(self):
        """
        :rtype: float
        """
        if not self.vals:
            return None
        self.vals = sorted(self.vals)
        length = len(self.vals)
        mid = length // 2
        if length % 2 == 1:
            return self.vals[length//2]
        else:
            return float(self.vals[mid] + self.vals[mid -1]) / 2



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
