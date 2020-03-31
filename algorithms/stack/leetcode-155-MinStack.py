'''
155. 最小栈
设计一个支持 push，pop，top 操作，并能在常数时间内检索到最小元素的栈。

push(x) -- 将元素 x 推入栈中。
pop() -- 删除栈顶的元素。
top() -- 获取栈顶元素。
getMin() -- 检索栈中的最小元素。
示例:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.getMin();   --> 返回 -2.

155. Min Stack
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
 

Example:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
'''





class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.items = []


    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.items.append(x)


    def pop(self):
        """
        :rtype: None
        """
        if not self.items:
            return None
        return self.items.pop()


    def top(self):
        """
        :rtype: int
        """
        if not self.items:
            return None
        return self.items[-1]



    def getMin(self):
        """
        :rtype: int
        """
        return min(self.items)



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
