# encoding=utf8

'''
170. 两数之和 III - 数据结构设计
设计并实现一个 TwoSum 的类，使该类需要支持 add 和 find 的操作。

add 操作 -  对内部数据结构增加一个数。
find 操作 - 寻找内部数据结构中是否存在一对整数，使得两数之和与给定的数相等。

示例 1:

add(1); add(3); add(5);
find(4) -> true
find(7) -> false
示例 2:

add(3); add(1); add(2);
find(3) -> true
find(6) -> false

170. Two Sum III - Data structure design
Design and implement a TwoSum class. It should support the following operations: add and find.

add - Add the number to an internal data structure.
find - Find if there exists any pair of numbers which sum is equal to the value.

Example 1:

add(1); add(3); add(5);
find(4) -> true
find(7) -> false
Example 2:

add(3); add(1); add(2);
find(3) -> true
find(6) -> false
'''





class TwoSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.vals = []


    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: None
        """
        self.vals.append(number)


    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        hash_map = {}
        for val in self.vals:
            if val in hash_map:
                return True
            hash_map[value-val] = val
        return False





# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
