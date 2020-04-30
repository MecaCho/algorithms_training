'''
面试题 16.02. 单词频率
设计一个方法，找出任意指定单词在一本书中的出现频率。

你的实现应该支持如下操作：

WordsFrequency(book)构造函数，参数为字符串数组构成的一本书
get(word)查询指定单词在数中出现的频率
示例：

WordsFrequency wordsFrequency = new WordsFrequency({"i", "have", "an", "apple", "he", "have", "a", "pen"});
wordsFrequency.get("you"); //返回0，"you"没有出现过
wordsFrequency.get("have"); //返回2，"have"出现2次
wordsFrequency.get("an"); //返回1
wordsFrequency.get("apple"); //返回1
wordsFrequency.get("pen"); //返回1
提示：

book[i]中只包含小写字母
1 <= book.length <= 100000
1 <= book[i].length <= 10
get函数的调用次数不会超过100000

面试题 16.02. Words Frequency LCCI
Design a method to find the frequency of occurrences of any given word in a book. What if we were running this algorithm multiple times?

You should implement following methods:

WordsFrequency(book) constructor, parameter is a array of strings, representing the book.
get(word) get the frequency of word in the book.
Example:

WordsFrequency wordsFrequency = new WordsFrequency({"i", "have", "an", "apple", "he", "have", "a", "pen"});
wordsFrequency.get("you"); //returns 0，"you" is not in the book
wordsFrequency.get("have"); //returns 2，"have" occurs twice in the book
wordsFrequency.get("an"); //returns 1
wordsFrequency.get("apple"); //returns 1
wordsFrequency.get("pen"); //returns 1
Note:

There are only lowercase letters in book[i].
1 <= book.length <= 100000
1 <= book[i].length <= 10
get function will not be called more than 100000 times.
'''







class WordsFrequency(object):

    def __init__(self, book):
        """
        :type book: List[str]
        """
        import collections
        self.hash_map = collections.defaultdict(int)
        for i in range(len(book)):
            self.hash_map[book[i]] += 1


    def get(self, word):
        """
        :type word: str
        :rtype: int
        """
        return self.hash_map.get(word, 0)



# Your WordsFrequency object will be instantiated and called as such:
# obj = WordsFrequency(book)
# param_1 = obj.get(word)
