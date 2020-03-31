'''
341. 扁平化嵌套列表迭代器
给你一个嵌套的整型列表。请你设计一个迭代器，使其能够遍历这个整型列表中的所有整数。

列表中的每一项或者为一个整数，或者是另一个列表。其中列表的元素也可能是整数或是其他列表。

 

示例 1:

输入: [[1,1],2,[1,1]]
输出: [1,1,2,1,1]
解释: 通过重复调用 next 直到 hasNext 返回 false，next 返回的元素的顺序应该是: [1,1,2,1,1]。
示例 2:

输入: [1,[4,[6]]]
输出: [1,4,6]
解释: 通过重复调用 next 直到 hasNext 返回 false，next 返回的元素的顺序应该是: [1,4,6]。

341. Flatten Nested List Iterator
Given a nested list of integers, implement an iterator to flatten it.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Example 1:

Input: [[1,1],2,[1,1]]
Output: [1,1,2,1,1]
Explanation: By calling next repeatedly until hasNext returns false, 
             the order of elements returned by next should be: [1,1,2,1,1].
Example 2:

Input: [1,[4,[6]]]
Output: [1,4,6]
Explanation: By calling next repeatedly until hasNext returns false, 
             the order of elements returned by next should be: [1,4,6].
'''



# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        # def travelsal(arr, res=None):
        #     if not arr:
        #         return res
        #     for ar in arr:
        #         if isinstance(ar, int):
        #             res.append(ar)
        #         elif isinstance(ar, list):
        #             res = res + travelsal(ar, res)
        #     return res
        # print(travelsal(nestedList, []))
        # self.vals = travelsal(nestedList, [])
        # print(self.vals)
        self.vals = nestedList[::-1]


    def next(self):
        """
        :rtype: int
        """
        # print(self.vals)
        res = self.vals.pop()
        if res.isInteger:
            return res
        return res.getList()[0]


    def hasNext(self):
        """
        :rtype: bool
        """
        while len(self.vals) > 0 and not self.vals[-1].isInteger():
            add_vals = self.vals.pop()
            if len(add_vals.getList()) > 0:
                self.vals += add_vals.getList()[::-1]
        return True if self.vals else False


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())


def travelsal(arr, res=None):
    if not arr:
        return res
    for ar in arr:
        if isinstance(ar, int):
            res.append(ar)
        elif isinstance(ar, list):
            res = res + travelsal(ar, res)
    return res

if __name__ == '__main__':
    res = travelsal([1,2,3, [1,2,3]], [])
    print(res)
    print(travelsal([[1,1],2,[1,1]], []))