
class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = []
        right = []
        sum_0 = 0
        sum_1 = 0
        for i in range(len(s)):
            if s[i] == "0":
                sum_0 += 1
            left.append(sum_0)
            if s[len(s) - 1 - i] == "1":
                sum_1 += 1
            right.append(sum_1)
        max_count = 0
        # print(left, right)
        for i in range(len(s ) -1):
            sum_ = left[i] + right[len(s) - 2 - i]
            max_count = max(max_count, sum_)
        return max_count
