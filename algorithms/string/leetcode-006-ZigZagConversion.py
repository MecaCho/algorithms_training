# encoding=utf8


'''
6. ZigZag Conversion
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I


6. Z 字形变换
将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。

比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：

L   C   I   R
E T O E S I I G
E   D   H   N
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。

请你实现这个将字符串进行指定行数变换的函数：

string convert(string s, int numRows);
示例 1:

输入: s = "LEETCODEISHIRING", numRows = 3
输出: "LCIRETOESIIGEDHN"
示例 2:

输入: s = "LEETCODEISHIRING", numRows = 4
输出: "LDREOEIIECIHNTSG"
解释:

L     D     R
E   O E   I I
E C   I H   N
T     S     G


'''


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        index = 0
        length = len(s)
        ret = ""
        if length < 3 or numRows ==1 or length <= numRows:
            return s
        numcCol = length / (numRows*2 -2) + 1
        numCols = (numRows-1) * numcCol + 1
        aList = [[" " for i in range(numCols)] for j in range(numRows)]
        for i in range(numCols):
            for j in range(numRows):
                if (i % (numRows-1))==0 or (i + j)%(numRows -1)==0:
                    if index < length and aList[j][i] == " ":
                        aList[j][i] = s[index]
                        index += 1

        # print(aList)
        for i in range(numRows):
            for j in range(numCols):
                if aList[i][j] != " ":
                    ret += aList[i][j] 
        return ret


class Solution0(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s

        L = [''] * numRows
        index, step = 0, 1

        for x in s:
            L[index] += x
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
            index += step

        return ''.join(L)
'''
Note also that the copies are shallow; nested structures are not copied. This often haunts new Python programmers; consider:

>>> lists = [[]] * 3
>>> lists
[[], [], []]
>>> lists[0].append(3)
>>> lists
[[3], [3], [3]]
What has happened is that [[]] is a one-element list containing an empty list, so all three elements of [[]] * 3 are (pointers to) this single empty list. Modifying any of the elements of lists modifies this single list. You can create a list of different lists this way:

>>>
>>> lists = [[] for i in range(3)]
>>> lists[0].append(3)
>>> lists[1].append(5)
>>> lists[2].append(7)
>>> lists
[[3], [5], [7]]
'''

# solution

'''
方法一：按行排序
思路

通过从左向右迭代字符串，我们可以轻松地确定字符位于 Z 字形图案中的哪一行。

算法

我们可以使用 \text{min}( \text{numRows}, \text{len}(s))min(numRows,len(s)) 个列表来表示 Z 字形图案中的非空行。

从左到右迭代 ss，将每个字符添加到合适的行。可以使用当前行和当前方向这两个变量对合适的行进行跟踪。

只有当我们向上移动到最上面的行或向下移动到最下面的行时，当前方向才会发生改变。

C++Java

class Solution {
public:
    string convert(string s, int numRows) {

        if (numRows == 1) return s;

        vector<string> rows(min(numRows, int(s.size())));
        int curRow = 0;
        bool goingDown = false;

        for (char c : s) {
            rows[curRow] += c;
            if (curRow == 0 || curRow == numRows - 1) goingDown = !goingDown;
            curRow += goingDown ? 1 : -1;
        }

        string ret;
        for (string row : rows) ret += row;
        return ret;
    }
};
复杂度分析

时间复杂度：O(n)O(n)，其中 n == \text{len}(s)n==len(s)
空间复杂度：O(n)O(n)
方法二：按行访问
思路

按照与逐行读取 Z 字形图案相同的顺序访问字符串。

算法

首先访问 行 0 中的所有字符，接着访问 行 1，然后 行 2，依此类推...

对于所有整数 kk，

行 00 中的字符位于索引 k \; (2 \cdot \text{numRows} - 2)k(2⋅numRows−2) 处;
行 \text{numRows}-1numRows−1 中的字符位于索引 k \; (2 \cdot \text{numRows} - 2) + \text{numRows} - 1k(2⋅numRows−2)+numRows−1 处;
内部的 行 ii 中的字符位于索引 k \; (2 \cdot \text{numRows}-2)+ik(2⋅numRows−2)+i 以及 (k+1)(2 \cdot \text{numRows}-2)- i(k+1)(2⋅numRows−2)−i 处;
C++Java

class Solution {
public:
    string convert(string s, int numRows) {

        if (numRows == 1) return s;

        string ret;
        int n = s.size();
        int cycleLen = 2 * numRows - 2;

        for (int i = 0; i < numRows; i++) {
            for (int j = 0; j + i < n; j += cycleLen) {
                ret += s[j + i];
                if (i != 0 && i != numRows - 1 && j + cycleLen - i < n)
                    ret += s[j + cycleLen - i];
            }
        }
        return ret;
    }
};
复杂度分析

时间复杂度：O(n)O(n)，其中 n == \text{len}(s)n==len(s)。每个索引被访问一次。
空间复杂度：O(n)O(n)。对于 C++ 实现，如果返回字符串不被视为额外空间，则复杂度为 O(1)O(1)。

'''

