'''

'''

import collections
d = collections.OrderedDict()

class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        length = len(cardPoints) - k
        if length <= 0:
            return sum(cardPoints)
        sum_ = sum(cardPoints[:length])
        res = sum_
        for i in range(1, len(cardPoints) - length +1):
            add = cardPoints[ i +length -1] - cardPoints[ i -1]
            sum_ += add
            print(i, sum_, add)
            res = min(res, sum_)
            # if add < 0:
            #     res += add
        print(sum(cardPoints), res)
        return sum(cardPoints) - res


if __name__ == '__main__':
    d[1].append(1)
    # d[1] = [1,2,3]
    print(d)