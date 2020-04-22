'''
716. 最大栈
设计一个最大栈，支持 push、pop、top、peekMax 和 popMax 操作。



push(x) -- 将元素 x 压入栈中。
pop() -- 移除栈顶元素并返回这个值。
top() -- 返回栈顶元素。
peekMax() -- 返回栈中最大元素。
popMax() -- 返回栈中最大的元素，并将其删除。如果有多个最大元素，只要删除最靠近栈顶的那个。


样例 1:

MaxStack stack = new MaxStack();
stack.push(5);
stack.push(1);
stack.push(5);
stack.top(); -> 5
stack.popMax(); -> 5
stack.top(); -> 1
stack.peekMax(); -> 5
stack.pop(); -> 1
stack.top(); -> 5


注释:

-1e7 <= x <= 1e7
操作次数不会超过 10000。
当栈为空的时候不会出现后四个操作。

716. Max Stack
Design a max stack that supports push, pop, top, peekMax and popMax.

push(x) -- Push element x onto stack.
pop() -- Remove the element on top of the stack and return it.
top() -- Get the element on the top.
peekMax() -- Retrieve the maximum element in the stack.
popMax() -- Retrieve the maximum element in the stack, and remove it. If you find more than one maximum elements, only remove the top-most one.
Example 1:
MaxStack stack = new MaxStack();
stack.push(5);
stack.push(1);
stack.push(5);
stack.top(); -> 5
stack.popMax(); -> 5
stack.top(); -> 1
stack.peekMax(); -> 5
stack.pop(); -> 1
stack.top(); -> 5
Note:
-1e7 <= x <= 1e7
Number of operations won't exceed 10000.
The last four operations won't be called when stack is empty.
'''



class MaxStack(object):

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
        # self.vals = sorted(self.vals)


    def pop(self):
        """
        :rtype: int
        """
        return self.vals.pop()


    def top(self):
        """
        :rtype: int
        """
        return self.vals[-1] if self.vals else None


    def peekMax(self):
        """
        :rtype: int
        """
        if self.vals:
            val = sorted(self.vals)[-1]
            return val
        return None


    def popMax(self):
        """
        :rtype: int
        """
        if self.vals:
            val = sorted(self.vals)[-1]
            # import copy
            # tmp = copy.deepcopy(self.vals[::-1])
            tmp = self.vals[::-1]
            tmp.remove(val)
            self.vals[:] = tmp[::-1]
            return val
        return None




# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()