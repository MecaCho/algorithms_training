



'''
271. 字符串的编码与解码
请你设计一个算法，可以将一个 字符串列表 编码成为一个 字符串。这个编码后的字符串是可以通过网络进行高效传送的，并且可以在接收端被解码回原来的字符串列表。

1 号机（发送方）有如下函数：

string encode(vector<string> strs) {
  // ... your code
  return encoded_string;
}
2 号机（接收方）有如下函数：

vector<string> decode(string s) {
  //... your code
  return strs;
}
1 号机（发送方）执行：

string encoded_string = encode(strs);
2 号机（接收方）执行：

vector<string> strs2 = decode(encoded_string);
此时，2 号机（接收方）的 strs2 需要和 1 号机（发送方）的 strs 相同。

请你来实现这个 encode 和 decode 方法。

注意：

因为字符串可能会包含 256 个合法 ascii 字符中的任何字符，所以您的算法必须要能够处理任何可能会出现的字符。
请勿使用 “类成员”、“全局变量” 或 “静态变量” 来存储这些状态，您的编码和解码算法应该是非状态依赖的。
请不要依赖任何方法库，例如 eval 又或者是 serialize 之类的方法。本题的宗旨是需要您自己实现 “编码” 和 “解码” 算法。


271. Encode and Decode Strings
Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

Machine 1 (sender) has the function:

string encode(vector<string> strs) {
  // ... your code
  return encoded_string;
}
Machine 2 (receiver) has the function:
vector<string> decode(string s) {
  //... your code
  return strs;
}
So Machine 1 does:

string encoded_string = encode(strs);
and Machine 2 does:

vector<string> strs2 = decode(encoded_string);
strs2 in Machine 2 should be the same as strs in Machine 1.

Implement the encode and decode methods.



Note:

The string may contain any possible characters out of 256 valid ascii characters. Your algorithm should be generalized enough to work on any possible characters.
Do not use class member/global/static variables to store states. Your encode and decode algorithms should be stateless.
Do not rely on any library method such as eval or serialize methods. You should implement your own encode/decode algorithm.
'''

import json

class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.

        :type strs: List[str]
        :rtype: str
        """
        # return ",".join(strs)
        return json.dumps(strs)

    def decode(self, s):
        """Decodes a single string to a list of strings.

        :type s: str
        :rtype: List[str]
        """
        # return s.split(",")
        return json.loads(s)

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))


'''
方法一：使用非 ASCII 码的分隔符
算法：

最简单的方法就是分隔符连接字符串。

而问题就是用什么作为分隔符？每个字符串可以包含 256 个有效的 ASCII 码字符。

可以使用非 ASCII 码的字符，例如 Python 中的 unichr(257) 和 Java 中的 Character.toString((char)257)（代表的是字符 ā）。



我们还是用了另一个非 ASCII 字符来识别字符为空的情况。

PythonJava

class Codec:
    def encode(self, strs):
        """Encodes a list of strings to a single string.
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0: 
            return unichr(258)
        
        # encode here is a workaround to fix BE CodecDriver error
        return unichr(257).join(x.encode('utf-8') for x in strs)
        

    def decode(self, s):
        """Decodes a single string to a list of strings.
        :type s: str
        :rtype: List[str]
        """
        if s == unichr(258): 
            return []
        return s.split(unichr(257))
复杂度分析

时间复杂度：均是 \mathcal{O}(N)O(N)，其中 NN 指的是字符串数组的大小。
空间复杂度：
encode：\mathcal{O}(1)O(1)，只用了一个字符串变量。
decode：\mathcal{O}(N)O(N)，使用了字符串数组。
方法二：分块编码
算法：

这种方法基于 HTTP v1.1 使用的编码，它不依赖于输入字符集，因此比方法一更具有通用性和有效性。

数据流被分成块，每个块前面都有其字节大小。

编码：



遍历字符串数组。
计算每个字符串的长度，并将长度大小转换为 4 个字节的字符串。
将长度信息的字符串添加到编码字符串的前面。
前面 4 个字节表示了编码字符串的长度。
后面跟这字符串本身。
返回编码后的字符串。
解码：



初始化指针 i = 0 在编码字符串上迭代，当 i < n：
读四个字节 s[i: i + 4]，代表的是字符串信息的长度，将 s[i: i + 4] 转化为整数 length。
移动指针 i += 4。
添加字符串到答案 s[i: i + length]。
移动指针 i += length。
返回解码后的字符串数组。
Python

class Codec:
    def len_to_str(self, x):
        """
        Encodes length of string to bytes string
        """
        x = len(x)
        bytes = [chr(x >> (i * 8) & 0xff) for i in range(4)]
        bytes.reverse()
        bytes_str = ''.join(bytes)
        return bytes_str
    
    def encode(self, strs):
        """Encodes a list of strings to a single string.
        :type strs: List[str]
        :rtype: str
        """
        # encode here is a workaround to fix BE CodecDriver error
        return ''.join(self.len_to_str(x) + x.encode('utf-8') for x in strs)
        
    def str_to_int(self, bytes_str):
        """
        Decodes bytes string to integer.
        """
        result = 0
        for ch in bytes_str:
            result = result * 256 + ord(ch)
        return result
    
    def decode(self, s):
        """Decodes a single string to a list of strings.
        :type s: str
        :rtype: List[str]
        """
        i, n = 0, len(s)
        output = []
        while i < n:
            length = self.str_to_int(s[i: i + 4])
            i += 4
            output.append(s[i: i + length])
            i += length
        return output
Java

public class Codec {
  // Encodes string length to bytes string
  public String intToString(String s) {
    int x = s.length();
    char[] bytes = new char[4];
    for(int i = 3; i > -1; --i) {
      bytes[3 - i] = (char) (x >> (i * 8) & 0xff);
    }
    return new String(bytes);
  }

  // Encodes a list of strings to a single string.
  public String encode(List<String> strs) {
    StringBuilder sb = new StringBuilder();
    for(String s: strs) {
      sb.append(intToString(s));
      sb.append(s);
    }
    return sb.toString();
  }

  // Decodes bytes string to integer
  public int stringToInt(String bytesStr) {
    int result = 0;
    for(char b : bytesStr.toCharArray())
      result = (result << 8) + (int)b;
    return result;
  }

  // Decodes a single string to a list of strings.
  public List<String> decode(String s) {
    int i = 0, n = s.length();
    List<String> output = new ArrayList();
    while (i < n) {
      int length = stringToInt(s.substring(i, i + 4));
      i += 4;
      output.add(s.substring(i, i + length));
      i += length;
    }
    return output;
  }
}
复杂度分析

时间复杂度：均是 \mathcal{O}(N)O(N)，其中 NN 指的是字符串数组的大小。
空间复杂度：
encode：\mathcal{O}(1)O(1)，只用了一个字符串变量。
decode：\mathcal{O}(N)O(N)，使用了字符串数组。

作者：LeetCode
链接：https://leetcode-cn.com/problems/encode-and-decode-strings/solution/zi-fu-chuan-de-bian-ma-yu-jie-ma-by-leetcode/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''