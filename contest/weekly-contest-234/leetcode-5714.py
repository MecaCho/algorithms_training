class Solution(object):
    def evaluate(self, s, knowledge):
        """
        :type s: str
        :type knowledge: List[List[str]]
        :rtype: str
        """
        # s = s.replace("(", "{").replace(")", "}")
        # return s.format(**dict({k[0]:k[1] for k in knowledge}))
        chars = []
        word_dict = {k[0]: k[1] for k in knowledge}
        res = ""
        print(word_dict)
        flag = True
        for i in range(len(s)):
            if s[i] == "(":
                chars = []
                flag = False
            elif s[i] == ")":
                word = "".join(chars)
                if word in word_dict:
                    res += word_dict[word]
                else:
                    res += "?"
                flag = True
            else:
                if flag:
                    res += s[i]
                else:
                    chars.append(s[i])

        return res


if __name__ == '__main__':
    demo = Solution()
    res = demo.evaluate("(name)is(age)yearsold", [["name","bob"],["age","two"]])

    print(res)
