


'''
320. 列举单词的全部缩写
请你写出一个能够举单词全部缩写的函数。

注意：输出的顺序并不重要。

示例：

输入: "word"
输出:
["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]

320. Generalized Abbreviation
Write a function to generate the generalized abbreviations of a word.

Note: The order of the output does not matter.

Example:

Input: "word"
Output:
["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]
'''




class Solution(object):
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """

        self.vals = []
        def backtrack(i, new_word="", pre_num=0):
            if i == len(word):
                if pre_num:
                    new_word += str(pre_num)
                self.vals.append(new_word)
            else:
                if pre_num:
                    backtrack(i+1, new_word, pre_num+1)
                    backtrack(i+1, new_word+str(pre_num)+word[i], 0)
                else:
                    backtrack(i+1, new_word, pre_num+1)
                    backtrack(i+1, new_word+word[i], 0)


        backtrack(0, "", 0)
        return self.vals

        # self.vals = []
        # def backtrack(i, new_word=""):
        #     if i == len(word):
        #         self.vals.append(new_word)
        #     else:
        #         for j in range(i, len(word)):
        #             num = str(j-i) if j-i > 0 else ""
        #             backtrack(j+1, new_word + num + word[j])
        #         backtrack(len(word), new_word+str(len(word)-i))
        #         # for j in range(len(new_word)+1):
        #         #     backtrack(n+1, new_word[:j] + str(i+1) + new_word[j:])

        # backtrack(0, "")
        # return self.vals


        # res = [word]
        # for i in range(1, len(word)+1):
        #     num_s = str(i)
        #     for j in range(0, len(word)-i+1):

        #         new_word = list(word)
        #         new_word[j:j+i] = num_s
        #         res.append("".join(new_word))
        # return res
