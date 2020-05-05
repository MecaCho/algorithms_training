'''
604. 迭代压缩字符串
对于一个压缩字符串，设计一个数据结构，它支持如下两种操作： next 和 hasNext。

给定的压缩字符串格式为：每个字母后面紧跟一个正整数，这个整数表示该字母在解压后的字符串里连续出现的次数。

next() - 如果压缩字符串仍然有字母未被解压，则返回下一个字母，否则返回一个空格。
hasNext() - 判断是否还有字母仍然没被解压。

注意：

请记得将你的类在 StringIterator 中 初始化 ，因为静态变量或类变量在多组测试数据中不会被自动清空。更多细节请访问 这里 。

示例：

StringIterator iterator = new StringIterator("L1e2t1C1o1d1e1");

iterator.next(); // 返回 'L'
iterator.next(); // 返回 'e'
iterator.next(); // 返回 'e'
iterator.next(); // 返回 't'
iterator.next(); // 返回 'C'
iterator.next(); // 返回 'o'
iterator.next(); // 返回 'd'
iterator.hasNext(); // 返回 true
iterator.next(); // 返回 'e'
iterator.hasNext(); // 返回 false
iterator.next(); // 返回 ' '

604. Design Compressed String Iterator
Design and implement a data structure for a compressed string iterator. It should support the following operations: next and hasNext.

The given compressed string will be in the form of each letter followed by a positive integer representing the number of this letter existing in the original uncompressed string.

next() - if the original string still has uncompressed characters, return the next letter; Otherwise return a white space.
hasNext() - Judge whether there is any letter needs to be uncompressed.

Note:
Please remember to RESET your class variables declared in StringIterator, as static/class variables are persisted across multiple test cases. Please see here for more details.

Example:

StringIterator iterator = new StringIterator("L1e2t1C1o1d1e1");

iterator.next(); // return 'L'
iterator.next(); // return 'e'
iterator.next(); // return 'e'
iterator.next(); // return 't'
iterator.next(); // return 'C'
iterator.next(); // return 'o'
iterator.next(); // return 'd'
iterator.hasNext(); // return true
iterator.next(); // return 'e'
iterator.hasNext(); // return false
iterator.next(); // return ' '

'''


class StringIterator(object):

    def __init__(self, compressedString):
        """
        :type compressedString: str
        """
        self.strs = [str(i) for i in re.split(r"[0-9]", compressedString) if i]
        self.ints = [int(j) for j in re.split(r"[a-zA-Z]", compressedString) if j]
        # self.vals = ""
        # # print(strs, ints)
        # for i in range(len(strs)):
        #     self.vals += strs[i] * ints[i]
        self.total = sum(self.ints) if self.ints else 0
        self.loc = 0


    def next(self):
        """
        :rtype: str
        """
        res = " "
        if self.total > 0:
            count = 0
            for i in range(len(self.strs)):
                count += self.ints[i]
                if self.loc < count:
                    res = self.strs[i]
                    break
        self.loc += 1
        self.total -= 1
        return res


    def hasNext(self):
        """
        :rtype: bool
        """
        return self.total > 0



# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
