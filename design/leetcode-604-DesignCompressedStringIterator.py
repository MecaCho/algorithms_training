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


'''
方法 1：解压缩字符串 [Time Limit Exceeded]
算法

在这种方法中，我们将字符串预处理。我们假设已经将 compressedStringcompressedString 解压缩到 resres 字符串构造器中，为了求得 resres 中的解压字符串，我们遍历一遍 compressedStringcompressedString，一旦遇到一个字符，我们找到它后面的数字。然后我们就可以得到当前解压字符的两个元素（字符和次数）。

现在我们看看 next() 和 hasNext() 操作具体是怎么实现的：

next()：我们首先检车压缩字符串是否还有没解压的字符，如果没有了，那么 hasNext() 函数返回 False ，next() 函数返回 ' ' 。否则我们用指针 ptrptr 返回一个字符， ptrptr 指向的是下一个待返回的字符。在返回字符之前我们要在 resres 中更新 ptrptr 指针。

hasNext()： 如果 ptrptr 指向的地方超过了 resres 数组最后一个位置，说明没有更多的待解压字符，我们返回 False，否则返回 True。

Java
public class StringIterator {
    StringBuilder res=new StringBuilder();
    int ptr=0;
    public StringIterator(String s) {
        int i = 0;
        while (i < s.length()) {
                char ch = s.charAt(i++);
                int num = 0;
                while (i < s.length() && Character.isDigit(s.charAt(i))) {
                    num = num * 10 + s.charAt(i) - '0';
                    i++;
                }
                for (int j = 0; j < num; j++)
                    res.append(ch);
        }
    }
    public char next() {
        if (!hasNext())
            return ' ';
        return res.charAt(ptr++);
    }
    public boolean hasNext() {
        return ptr!=res.length();
    }
}
表现分析

我们预处理了解压缩后的字符串，所以需要空间为 O(m)O(m)，这里 mm 是解压缩后字符串的长度。

预处理的时间复杂度是 O(m)O(m)，因为解压缩后字符串的长度是 mm。

一旦预处理过程完成后，操作 next() 和 hasNexts() 的时间复杂度都是 O(1)O(1)。

这个方法可以很轻易地扩展更多操作，比方说 previous()，last()，find() 和 hasPrevious() 等等，而且由于这些操作都可以基于一个索引进行，所以时间复杂度都是 O(1)O(1) 的。

由于预处理完成后，next() 操作只需要 O(1)O(1) 的时间，如果有大量的 next() 操作，这个方法的优势非常明显。但是如果有大量的 hasNext() 操作，这个方法的优势不明显，因为预处理总是要被执行的。

这个方法的一个潜在问题是如果未解压字符串你的长度非常大，那么可能会导致内存溢出的问题。

方法 2：预处理 [Accepted]
算法

这个方法中，我们首先将 compressedStringcompressedString 中的字母和后面的重复次数分别保存在 charschars 和 numsnums 数组中。我们使用正则表达式来完成这个过程。

正则表达式是一串特殊的字符串，它通过一些匹配模式，找到需要匹配的字符串或者一系列字符串，它可以被用在搜索、编辑和修改文字和数据等等方面。

用正则表达式进行分割字符和数字可以在预处理过程中完成，我们来看看 next() 和 hasNext() 操作分别如何完成。

next()：每次执行 next() 操作时，首先我们使用函数 hasNext() 检查是否还有没解压的字符，如果没有了，我们返回 ' '。我们通过 ptrptr 记录 compressedStringcompressedString 中需要返回的下一个字符。如果有剩余未解压字符，我们返回 ptrptr 当前指向的字符，我们同时减少 nums[ptr]nums[ptr] 条目，表示当前待解压的字符数目减少一个。如果 nums[ptr]nums[ptr] 变成了 0 ，表示当前字符已经完全被解压了，我们就将 ptrptr 指向下一个字母。

hasNext()：执行 hasNext() 时，我们只需要检查 ptrptr 是否超出了 charschars 数组的范围，如果超出了，说明compressedStringcompressedString 中没有更多字符了，此时我们返回 False，否则我们返回 True。

Java
import java.util.regex.Pattern;
public class StringIterator {
    int ptr = 0;
    String[] chars;int[] nums;
    public StringIterator(String compressedString) {
        nums = Arrays.stream(compressedString.substring(1).split("[a-zA-Z]+")).mapToInt(Integer::parseInt).toArray();;
        chars = compressedString.split("[0-9]+");
    }
    public char next() {
        if (!hasNext())
            return ' ';
        nums[ptr]--;
        char res=chars[ptr].charAt(0);
        if(nums[ptr]==0)
            ptr++;
        return res;
    }
    public boolean hasNext() {
        return ptr != chars.length;
    }
}
表现分析

保存预处理结果的空间为 O(n)O(n)，这里 nn 是压缩字符串的长度。 numsnums 数组和 charschars 数组都包含 nn 个元素。

预处理过程需要 O(n)O(n) 的时间。所以如果大部分时间在执行 hasNext() 操作，这个预处理方法也会没有优势。

一旦预处理操作完成， hasNext() 和 next() 只需要 O(1)O(1) 的时间。

这个方法可以扩展到 previous() 和 hasPrevious() 操作，但需要在当前的实现上进行一些简单的修改。

方法 3：需求计算 [Accepted]
算法

在这个方法中，我们不使用正则表达式来找到 compressedStringcompressedString 中每一个部分，我们也不做任何形式的预处理，当一个操作被执行的时候，我们才去执行相应的操作获得对应的结果。所以操作是根据需要进行的。

我们来看一下这个方法的具体实现：

next()：我们使用一个全局 ptrptr 记录 compressedStringcompressedString 中下一个要生成的字符，我们还使用 numnum 记录当前字符剩余的数目。一旦 next() 操作被执行，我们首先检查是否还有没被解压的字符，如果没有，我们返回 ' ' ，否则我们检查当前字符是否还有剩余数目，如果有我们减少当前字符剩余数目并直接返回当前字符。如果没有剩余数目了，我们更新 ptrptr 指向 compressedStringcompressedString 中下一个字符并从 compressedStringcompressedString 中获取当前字符的数目，然后更新 numnum。这个数字可以通过数值方法获得。

hasNext()：如果 ptrptr 指向的下标超过了 compressedStringcompressedString 的范围，这表示已经没有更多未解压字符，我们返回 False，否则返回 True 表示还有未解压字符。

Java
public class StringIterator {
    String res;
    int ptr = 0, num = 0;
    char ch = ' ';
    public StringIterator(String s) {
        res = s;
    }
    public char next() {
        if (!hasNext())
            return ' ';
        if (num == 0) {
            ch = res.charAt(ptr++);
            while (ptr < res.length() && Character.isDigit(res.charAt(ptr))) {
                num = num * 10 + res.charAt(ptr++) - '0';
            }
        }
        num--;
        return ch;
    }
    public boolean hasNext() {
        return ptr != res.length() || num != 0;
    }
}
表现分析

由于没有进行预处理，所以只需要常数的空间。

执行 next() 操作的时间复杂度为 O(1)O(1)。

执行 hasNexts() 的时间复杂度是 O(1)O(1)。

由于不需要预处理，hasNext() 只需要 O(1)O(1) 的时间，如果有大量的 hasNext() 操作，这个方法优势非常明显。

这个方法可以扩展包括 previous() 和 hasPrevious()，但是需要一些额外的变量。

作者：LeetCode
链接：https://leetcode-cn.com/problems/design-compressed-string-iterator/solution/die-dai-ya-suo-zi-fu-chuan-by-leetcode/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''