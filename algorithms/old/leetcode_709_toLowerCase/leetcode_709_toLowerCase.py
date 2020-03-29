class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        return "".join([chr(ord(i) + 32) if "A" <= i <= "Z" else i for i in str])


if __name__ == '__main__':
    demo = Solution()
    print demo.toLowerCase("Hello")