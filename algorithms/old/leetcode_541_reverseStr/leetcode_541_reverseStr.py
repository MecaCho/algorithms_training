class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s = list(s)
        length = len(s)
        num = length / k + 1
        i = 0
        while i < num:
            if i % 2 == 0:
                tmp = s[i * k:min((i + 1) * k, length)]
                s[i * k:min((i + 1) * k, length)] = tmp[::-1]
            i += 1
        return "".join(s)

if __name__ == '__main__':
    demo = Solution()
    print demo.reverseStr("abcdefgh", 3)
