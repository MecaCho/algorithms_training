'''
557. Reverse Words in a String III
Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Note: In the string, each word is separated by single space and there will not be any extra space in the string.

557. 反转字符串中的单词 III
给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。



示例：

输入："Let's take LeetCode contest"
输出："s'teL ekat edoCteeL tsetnoc"


提示：

在字符串中，每个单词由单个空格分隔，并且字符串中不会有任何额外的空格。

'''


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return " ".join([i[::-1] for i in s.split(" ")])

# solution

'''
方法一：使用额外空间
思路与算法

开辟一个新字符串。然后从头到尾遍历原字符串，直到找到空格为止，此时找到了一个单词，并能得到单词的起止位置。随后，根据单词的起止位置，可以将该单词逆序放到新字符串当中。如此循环多次，直到遍历完原字符串，就能得到翻转后的结果。

代码

C++JavaJavaScriptCGolang

func reverseWords(s string) string {
    length := len(s)
    ret := []byte{}
    for i := 0; i < length; {
        start := i
        for i < length && s[i] != ' ' {
            i++
        }
        for p := start; p < i; p++ {
            ret = append(ret, s[start + i - 1 - p])
        }
        for i < length && s[i] == ' ' {
            i++
            ret = append(ret, ' ')
        }
    }
    return string(ret)
}
复杂度分析

时间复杂度：O(N)O(N)，其中 NN 为字符串的长度。原字符串中的每个字符都会在 O(1)O(1) 的时间内放入新字符串中。

空间复杂度：O(N)O(N)。我们开辟了与原字符串等大的空间。

方法二：原地解法
思路与算法

此题也可以直接在原字符串上进行操作，避免额外的空间开销。当找到一个单词的时候，我们交换字符串第一个字符与倒数第一个字符，随后交换第二个字符与倒数第二个字符…… 如此反复，就可以在原空间上翻转单词。

需要注意的是，原地算法在某些语言（比如 Java，JavaScript）中不适用，因为在这些语言中 String 类型是一个不可变的类型。

代码

C++C

class Solution {
public: 
    string reverseWords(string s) {
        int length = s.length();
        int i = 0;
        while (i < length) {
            int start = i;
            while (i < length && s[i] != ' ') {
                i++;
            }

            int left = start, right = i - 1;
            while (left < right) {
                swap(s[left], s[right]);
                left++;
                right--;
            }
            while (i < length && s[i] == ' ') {
                i++;
            }
        }
        return s;
    }
};
复杂度分析

时间复杂度：O(N)O(N)。字符串中的每个字符要么在 O(1)O(1) 的时间内被交换到相应的位置，要么因为是空格而保持不动。

空间复杂度：O(1)O(1)。因为不需要开辟额外的数组。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/reverse-words-in-a-string-iii/solution/fan-zhuan-zi-fu-chuan-zhong-de-dan-ci-iii-by-lee-2/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
