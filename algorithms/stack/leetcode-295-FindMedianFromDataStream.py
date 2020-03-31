'''

295. 数据流的中位数
中位数是有序列表中间的数。如果列表长度是偶数，中位数则是中间两个数的平均值。

例如，

[2,3,4] 的中位数是 3

[2,3] 的中位数是 (2 + 3) / 2 = 2.5

设计一个支持以下两种操作的数据结构：

void addNum(int num) - 从数据流中添加一个整数到数据结构中。
double findMedian() - 返回目前所有元素的中位数。
示例：

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3) 
findMedian() -> 2
进阶:

如果数据流中所有整数都在 0 到 100 范围内，你将如何优化你的算法？
如果数据流中 99% 的整数都在 0 到 100 范围内，你将如何优化你的算法？

295. Find Median from Data Stream
Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

For example,
[2,3,4], the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.
 

Example:

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3) 
findMedian() -> 2
 

Follow up:

If all integer numbers from the stream are between 0 and 100, how would you optimize it?
If 99% of all integer numbers from the stream are between 0 and 100, how would you optimize it?
'''



class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.arr = []
        self.count = 0


    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        i = 0
        j = len(self.arr) - 1
        while i <= j:
            mid = (i + j ) /2
            if num > self.arr[mid]:
                i = mid + 1
            else:
                j = mid - 1
        self.count += 1
        self.arr = self.arr[:i] + [num] + self.arr[i:]


    def findMedian(self):
        """
        :rtype: float
        """
        if not self.arr:
            return 0
        if self.count % 2 ==0:
            # print(self.arr[self.count/2], self.arr[self.count/2-1])
            return float((self.arr[self.count / 2] + self.arr[self.count / 2 - 1])) / 2
        return self.arr[self.count / 2]



        # Your MedianFinder object will be instantiated and called as such:
        # obj = MedianFinder()
        # obj.addNum(num)
        # param_2 = obj.findMedian()
