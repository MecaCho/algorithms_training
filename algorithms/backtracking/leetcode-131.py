'''
131. 分割回文串
给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。

返回 s 所有可能的分割方案。

示例:

输入: "aab"
输出:
[
  ["aa","b"],
  ["a","a","b"]
]

 131. Palindrome Partitioning
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

Example:

Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]
'''


class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """

        self.vals = []

        def bk(nums, temp):
            if not nums and temp[-1][::-1] == temp[-1]:
                self.vals.append(temp)
                return
            for i in range(len(nums)):
                if temp and temp[-1][::-1] != temp[-1]:
                    continue
                bk(nums[ i +1:], temp +["".join(nums[: i +1])])

        bk(list(s), [])
        return self.vals


class Solution1(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """

        def is_palindrome(s):
            i, j = 0, len(s) - 1
            while i <= j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        self.vals = []

        def bk(s, temp):
            if not s:
                self.vals.append(temp)
                return
            for i in range(len(s)):
                if is_palindrome(s[:i + 1]):
                    bk(s[i + 1:], temp + [s[:i + 1]])

        bk(s, [])
        return self.vals


class Solution2(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        def is_palindrome(i, j):
            print(i, j)
            while i <= j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        self.vals = []

        def bk(temp, start):
            if start >= len(s):
                self.vals.append(temp)
                return
            for i in range(len(s) - start):
                # print(is_palindrome(start, start+i), start, start+i)
                if is_palindrome(start, start+i):
                    # print(start, start+i, [s[:i + 1]], True)
                    bk(temp + [s[start:start+i+1]], start+i+1)

        bk([], 0)
        return self.vals


class Solution3(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        return [[s[:i]] + rest
            for i in xrange(1, len(s)+1)
            if s[:i] == s[i-1::-1]
            for rest in self.partition(s[i:])] or [[]]


class Solution4(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """

        return [[s[:i]] + rest
            for i in range(1, len(s)+1)
            if s[:i] == s[i-1::-1]
            for rest in self.partition(s[i:])] or [[]]


class Solution5(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        if not s:
            return [[]]
        res = []
        for i in range(1, len(s)+1):
            for per in self.partition(s[i:]):
                if s[:i] == s[i-1::-1]:
                    res.append(s[:i]+per)
        return res

        # return [[s[:i]] + rest
        #         for i in range(1, len(s) + 1)
        #         if s[:i] == s[i - 1::-1]
        #         for rest in self.partition(s[i:])] or [[]]

if __name__ == '__main__':
    demo = Solution2()
    res = demo.partition("aab")
    print(res)