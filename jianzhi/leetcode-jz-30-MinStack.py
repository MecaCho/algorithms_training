
'''
面试题30. 包含min函数的栈
定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的 min 函数在该栈中，调用 min、push 及 pop 的时间复杂度都是 O(1)。



示例:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.min();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.min();   --> 返回 -2.


提示：

各函数的调用总次数不超过 20000 次


注意：本题与主站 155 题相同：https://leetcode-cn.com/problems/min-stack/
'''



class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.items = []
        self.mins = []


    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.items.append(x)
        if not self.mins or x <= self.mins[-1]:
            self.mins.append(x)


    def pop(self):
        """
        :rtype: None
        """
        if not self.items:
            return None
        res = self.items.pop()
        if res == self.mins[-1]:
            self.mins.pop()
        return res


    def top(self):
        """
        :rtype: int
        """
        if not self.items:
            return None
        return self.items[-1]



    def min(self):
        """
        :rtype: int
        """
        return self.mins[-1] if self.mins else None



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()
