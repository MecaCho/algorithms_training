
'''
面试题 03.02. 栈的最小值
请设计一个栈，除了常规栈支持的pop与push函数以外，还支持min函数，该函数返回栈元素中的最小值。执行push、pop和min操作的时间复杂度必须为O(1)。


示例：

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.getMin();   --> 返回 -2.

面试题 03.02. Min Stack LCCI
How would you design a stack which, in addition to push and pop, has a function min which returns the minimum element? Push, pop and min should all operate in 0(1) time.

Example:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> return -3.
minStack.pop();
minStack.top();      --> return 0.
minStack.getMin();   --> return -2.
'''





class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.vals = []


    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.vals.append(x)


    def pop(self):
        """
        :rtype: None
        """
        self.vals.pop()



    def top(self):
        """
        :rtype: int
        """
        return self.vals[-1] if self.vals else None



    def getMin(self):
        """
        :rtype: int
        """
        return min(self.vals) if self.vals else None



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


# 双栈
class MinStack1(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.vals = []
        self.min_vals = [float("inf")]


    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.vals.append(x)
        if x <= self.min_vals[-1]:
            self.min_vals.append(x)


    def pop(self):
        """
        :rtype: None
        """
        val = self.vals.pop()
        if val == self.min_vals[-1]:
            self.min_vals.pop()



    def top(self):
        """
        :rtype: int
        """
        return self.vals[-1] if self.vals else None



    def getMin(self):
        """
        :rtype: int
        """
        return self.min_vals[-1] if len(self.min_vals) > 1 else None



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

