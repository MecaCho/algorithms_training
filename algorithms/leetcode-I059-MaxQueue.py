'''


面试题59 - II. 队列的最大值
请定义一个队列并实现函数 max_value 得到队列里的最大值，要求函数max_value、push_back 和 pop_front 的时间复杂度都是O(1)。

若队列为空，pop_front 和 max_value 需要返回 -1

示例 1：

输入: 
["MaxQueue","push_back","push_back","max_value","pop_front","max_value"]
[[],[1],[2],[],[],[]]
输出: [null,null,null,2,1,2]
示例 2：

输入: 
["MaxQueue","pop_front","max_value"]
[[],[],[]]
输出: [null,-1,-1]
 

限制：

1 <= push_back,pop_front,max_value的总操作数 <= 10000
1 <= value <= 10^5
'''

class MaxQueue(object):

    def __init__(self):
        self.max_v = None
        self.values = []


    def max_value(self):
        """
        :rtype: int
        """
        
        if not self.values:
            return -1
        return self.max_v


    def push_back(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.values.append(value)
        if self.max_v is None or value > self.max_v:
            self.max_v = value


    def pop_front(self):
        """
        :rtype: int
        """
        # if not self.values:
            # return -1
        value = -1
        if self.values:
            value = self.values[0]
            self.values.remove(value)
            if value == self.max_v:
                self.max_v = max(self.values) if self.values else -1
        return value



# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()

作者：qiuwenqi
链接：https://leetcode-cn.com/problems/dui-lie-de-zui-da-zhi-lcof/solution/python-dui-lie-de-zui-da-zhi-by-qiuwenqi/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
