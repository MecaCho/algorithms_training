'''

面试题 03.01. 三合一
三合一。描述如何只用一个数组来实现三个栈。

你应该实现push(stackNum, value)、pop(stackNum)、isEmpty(stackNum)、peek(stackNum)方法。stackNum表示栈下标，value表示压入的值。

构造函数会传入一个stackSize参数，代表每个栈的大小。

示例1:

 输入：
["TripleInOne", "push", "push", "pop", "pop", "pop", "isEmpty"]
[[1], [0, 1], [0, 2], [0], [0], [0], [0]]
 输出：
[null, null, null, 1, -1, -1, true]
说明：当栈为空时`pop, peek`返回-1，当栈满时`push`不压入元素。
示例2:

 输入：
["TripleInOne", "push", "push", "push", "pop", "pop", "pop", "peek"]
[[2], [0, 1], [0, 2], [0, 3], [0], [0], [0], [0]]
 输出：
[null, null, null, null, 2, 1, -1, -1]

面试题 03.01. Three in One LCCI
Describe how you could use a single array to implement three stacks.

Yout should implement push(stackNum, value)、pop(stackNum)、isEmpty(stackNum)、peek(stackNum) methods. stackNum is the index of the stack. value is the value that pushed to the stack.

The constructor requires a stackSize parameter, which represents the size of each stack.

Example1:

 Input: 
["TripleInOne", "push", "push", "pop", "pop", "pop", "isEmpty"]
[[1], [0, 1], [0, 2], [0], [0], [0], [0]]
 Output: 
[null, null, null, 1, -1, -1, true]
Explanation: When the stack is empty, `pop, peek` return -1. When the stack is full, `push` does nothing.
Example2:

 Input: 
["TripleInOne", "push", "push", "push", "pop", "pop", "pop", "peek"]
[[2], [0, 1], [0, 2], [0, 3], [0], [0], [0], [0]]
 Output: 
[null, null, null, null, 2, 1, -1, -1]
'''





class TripleInOne(object):

    def __init__(self, stackSize):
        """
        :type stackSize: int
        """
        self.vals = [[], [], []]
        self.stack_size = stackSize


    def push(self, stackNum, value):
        """
        :type stackNum: int
        :type value: int
        :rtype: None
        """
        new_stack = self.vals[stackNum]
        # print(new_stack)
        new_stack.append(value)
        if len(new_stack) > self.stack_size:
            new_stack[:] = new_stack[:self.stack_size]

        self.vals[stackNum] = new_stack

    def pop(self, stackNum):
        """
        :type stackNum: int
        :rtype: int
        """
        # print(self.vals[stackNum])
        return self.vals[stackNum].pop() if self.vals[stackNum] else -1


    def peek(self, stackNum):
        """
        :type stackNum: int
        :rtype: int
        """
        return self.vals[stackNum][-1] if self.vals[stackNum] else -1


    def isEmpty(self, stackNum):
        """
        :type stackNum: int
        :rtype: bool
        """
        # print(self.vals[stackNum])
        return True if not self.vals[stackNum] else False



        # Your TripleInOne object will be instantiated and called as such:
        # obj = TripleInOne(stackSize)
        # obj.push(stackNum,value)
        # param_2 = obj.pop(stackNum)
        # param_3 = obj.peek(stackNum)
        # param_4 = obj.isEmpty(stackNum)
