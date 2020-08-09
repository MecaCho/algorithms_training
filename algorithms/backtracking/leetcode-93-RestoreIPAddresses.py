'''
93. Restore IP Addresses
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

A valid IP address consists of exactly four integers (each integer is between 0 and 255) separated by single points.

Example:

Input: "25525511135"
Output: ["255.255.11.135", "255.255.111.35"]

93. 复原IP地址
给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。

有效的 IP 地址正好由四个整数（每个整数位于 0 到 255 之间组成），整数之间用 '.' 分隔。

示例:

输入: "25525511135"
输出: ["255.255.11.135", "255.255.111.35"]

'''

class Solution(object):
    def is_num(self, num):
        return str(int(num)) == num and 0 <= int(num) <= 255

    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ret = []

        def dfs(s, index=0, ip="", ret=[]):
            if index == 4:
                if not s:
                    ret.append(ip.strip("."))
                    return ret
                return
            for i in xrange(1, 4, 1):
                if i <= len(s) and s[:i] and self.is_num(s[:i]):
                    dfs(s[i:], index + 1, ip + s[:i] + ".", ret)

        dfs(s, 0, "", ret)
        return ret

if __name__ == '__main__':
    demo = Solution()
    print(demo.restoreIpAddresses("19200255"))