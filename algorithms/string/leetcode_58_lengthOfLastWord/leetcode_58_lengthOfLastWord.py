class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.strip().split(" ")[-1])


if __name__ == '__main__':
    demo = Solution()
    print(demo.lengthOfLastWord("abc Hello jjfkd "))
