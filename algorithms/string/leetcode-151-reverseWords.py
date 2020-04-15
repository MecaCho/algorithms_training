'''

151. Reverse Words in a String
Given an input string, reverse the string word by word.

 

Example 1:

Input: "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: "  hello world!  "
Output: "world! hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
Example 3:

Input: "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
 

Note:

A word is defined as a sequence of non-space characters.
Input string may contain leading or trailing spaces. However, your reversed string should not contain leading or trailing spaces.
You need to reduce multiple spaces between two words to a single space in the reversed string.
 

Follow up:

For C programmers, try to solve it in-place in O(1) extra space.

151. 翻转字符串里的单词
给定一个字符串，逐个翻转字符串中的每个单词。

 

示例 1：

输入: "the sky is blue"
输出: "blue is sky the"
示例 2：

输入: "  hello world!  "
输出: "world! hello"
解释: 输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
示例 3：

输入: "a good   example"
输出: "example good a"
解释: 如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。
 

说明：

无空格字符构成一个单词。
输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。
 

进阶：

请选用 C 语言的用户尝试使用 O(1) 额外空间复杂度的原地解法。
'''


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return " ".join([i for i in s.strip().split(" ")[::-1] if i])


'''
方法一：使用语言特性
思路和算法

很多语言对字符串提供了 split（拆分），reverse（翻转）和 join（连接）等方法，因此我们可以简单的调用内置的 API 完成操作：

使用 split 将字符串按空格分割成字符串数组；
使用 reverse 将字符串数组进行反转；
使用 join 方法将字符串数组拼成一个字符串。


Python3JavaJavaScript
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(reversed(s.split()))
复杂度分析

时间复杂度：O(N)O(N)，其中 N 为输入字符串的长度。

空间复杂度：O(N)O(N)，用来存储字符串分割之后的结果。

方法二：自行编写对应的函数
思路和算法

我们也可以不使用语言中的 API，而是自己编写对应的函数。在不同语言中，这些函数实现是不一样的，主要的差别是有些语言的字符串不可变（如 Java 和 Python)，有些语言的字符串可变（如 C++)。

对于字符串不可变的语言，首先得把字符串转化成其他可变的数据结构，同时还需要在转化的过程中去除空格。



对于字符串可变的语言，就不需要再额外开辟空间了，直接在字符串上原地实现。在这种情况下，反转字符和去除空格可以一起完成。



Python3JavaC++
class Solution:
    def trim_spaces(self, s: str) -> list:
        left, right = 0, len(s) - 1
        # 去掉字符串开头的空白字符
        while left <= right and s[left] == ' ':
            left += 1
        
        # 去掉字符串末尾的空白字符
        while left <= right and s[right] == ' ':
            right -= 1
        
        # 将字符串间多余的空白字符去除
        output = []
        while left <= right:
            if s[left] != ' ':
                output.append(s[left])
            elif output[-1] != ' ':
                output.append(s[left])
            left += 1
        
        return output
            
    def reverse(self, l: list, left: int, right: int) -> None:
        while left < right:
            l[left], l[right] = l[right], l[left]
            left, right = left + 1, right - 1
            
    def reverse_each_word(self, l: list) -> None:
        n = len(l)
        start = end = 0
        
        while start < n:
            # 循环至单词的末尾
            while end < n and l[end] != ' ':
                end += 1
            # 翻转单词
            self.reverse(l, start, end - 1)
            # 更新start，去找下一个单词
            start = end + 1
            end += 1
                
    def reverseWords(self, s: str) -> str:
        l = self.trim_spaces(s)
        
        # 翻转字符串
        self.reverse(l, 0, len(l) - 1)
        
        # 翻转每个单词
        self.reverse_each_word(l)
        
        return ''.join(l)
复杂度分析

时间复杂度：O(N)O(N)，其中 N 为输入字符串的长度。

空间复杂度：Java 和 Python 的方法需要 O(N)O(N) 的空间来存储字符串，而 C++ 方法只需要 O(1) 的额外空间来存放若干变量。

方法三：双端队列
思路和算法

由于双端队列支持从队列头部插入的方法，因此我们可以沿着字符串一个一个单词处理，然后将单词压入队列的头部，再将队列转成字符串即可。



Python3JavaC++
class Solution:
    def reverseWords(self, s: str) -> str:
        left, right = 0, len(s) - 1
        # 去掉字符串开头的空白字符
        while left <= right and s[left] == ' ':
            left += 1
        
        # 去掉字符串末尾的空白字符
        while left <= right and s[right] == ' ':
            right -= 1
            
        d, word = collections.deque(), []
        # 将单词 push 到队列的头部
        while left <= right:
            if s[left] == ' ' and word:
                d.appendleft(''.join(word))
                word = []
            elif s[left] != ' ':
                word.append(s[left])
            left += 1
        d.appendleft(''.join(word))
        
        return ' '.join(d)
复杂度分析

时间复杂度：O(N)O(N)，其中 N 为输入字符串的长度。

空间复杂度：O(N)O(N)，双端队列存储单词需要 O(N)O(N) 的空间。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/reverse-words-in-a-string/solution/fan-zhuan-zi-fu-chuan-li-de-dan-ci-by-leetcode-sol/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''