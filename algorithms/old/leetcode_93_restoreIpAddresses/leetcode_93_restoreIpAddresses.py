class Solution(object):
    def is_num(self, num):
        return str(int(num)) == num and 0 <= int(num) <= 255

    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ret = []

        def backtrack(s, index=0, ip="", ret=[]):
            if index == 4:
                if not s:
                    ret.append(ip.strip("."))
                    return ret
                return
            for i in range(1, 4, 1):
                if i <= len(s) and s[:i] and self.is_num(s[:i]):
                    backtrack(s[i:], index + 1, ip + s[:i] + ".", ret)

        backtrack(s, 0, "", ret)
        return ret

if __name__ == '__main__':
    demo = Solution()
    print(demo.restoreIpAddresses("19200255"))