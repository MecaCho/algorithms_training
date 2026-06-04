'''
346. Moving Average from Data Stream
Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

Example:

MovingAverage m = new MovingAverage(3);
m.next(1) = 1
m.next(10) = (1 + 10) / 2
m.next(3) = (1 + 10 + 3) / 3
m.next(5) = (10 + 3 + 5) / 3


346. 数据流中的移动平均值
给定一个整数数据流和一个窗口大小，根据该滑动窗口的大小，计算其所有整数的移动平均值。

示例:

MovingAverage m = new MovingAverage(3);
m.next(1) = 1
m.next(10) = (1 + 10) / 2
m.next(3) = (1 + 10 + 3) / 3
m.next(5) = (10 + 3 + 5) / 3
'''



class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.size = size
        self.values = []


    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        if len(self.values) < self.size:
            self.values.append(val)
        else:
            self.values.remove(self.values[0])
            self.values.append(val)
        return sum(self.values) / float(len(self.values))




        # Your MovingAverage object will be instantiated and called as such:
        # obj = MovingAverage(size)
        # param_1 = obj.next(val)
