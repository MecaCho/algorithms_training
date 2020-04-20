import re
import heapq


def words_reverse1(sentence):
    recompile = re.compile(r'[a-zA-Z]+-?[a-zA-Z]+|[a-zA-Z]+')
    word_list = recompile.findall(sentence)
    d_list = recompile.split(sentence)
    # print d_list

    ret = []
    if d_list:
        for i in range(len(d_list)):
            if i < len(word_list):
                ret.append(word_list[i])
            ret.append(d_list[i])
    else:
        ret = word_list

    return "".join([word[::-1] for word in ret])


def words_reverse(sentence):
    # print {i:i for i in range(10)}
    print("Sentence : ", sentence)
    temp = []
    # print "Test : ", "".join([key if not key.isalnum() else temp[::-1] for key in sentence])
    reversed_word = lambda key: key[::-1]

    # def reversed_word(i):
    #
    #     if key.isalnum:

    # print reversed_word("abc")
    print("Test : ", "".join([key if not key.isalnum() else
                              reversed_word(key) for i, key in enumerate(sentence)]))

    # [key if not key.isalnum else key for key in sentence]

    # temp = []
    ret = []
    for word in sentence:
        if word.isalnum():
            # heapq.heappush(word)
            temp.append(word)
        else:
            # ret.append(heapq.heappop())
            ret.append("".join(temp[::-1]))
            ret.append(word)
            temp = []
    ret.append("".join(temp[::-1]))
    return "".join(ret)


if __name__ == '__main__':
    # print words_reverse("This is a test words")
    # print words_reverse("This")
    # print words_reverse("hello,world!")
    # print words_reverse("I love you.")
    # print words_reverse("")
    # print words_reverse("#$^%^&&")
    # print words_reverse("fdfdf     vfdvfd   ....vdf")

    sentence = "Ti   .,. is a ///test,,,"
    # print reduce(lambda x, y: x + y if not y.isalnum() else y + x, sentence)

    # print reduce(lambda x, y: x*10 + y, [1, 2, 3, 4, 5])

    # "".join()

    tmp = []
    # print "abc$".isalnum()
    # print ".....: ", reduce(lambda x, y: x[-1].append(y) if y.isalnum() and x[-1][-1].isalnum() else x.append(y), sentence)
    # print reduce(lambda x, y:[x])
    # print int(float("inf"))




