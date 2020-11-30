'''
767. Reorganize String
Given a string S, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.

If possible, output any possible result.  If not possible, return the empty string.

Example 1:

Input: S = "aab"
Output: "aba"
Example 2:

Input: S = "aaab"
Output: ""
Note:

S will consist of lowercase letters and have length in range [1, 500].


767. 重构字符串
给定一个字符串S，检查是否能重新排布其中的字母，使得两相邻的字符不同。

若可行，输出任意可行的结果。若不可行，返回空字符串。

示例 1:

输入: S = "aab"
输出: "aba"
示例 2:

输入: S = "aaab"
输出: ""
注意:

S 只包含小写字母并且长度在[1, 500]区间内。
'''



class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        import collections
        import heapq
        counter = collections.Counter(S)

        if not S or max(counter.values()) > (len(S) / 2):
            return ""

        hq = []
        for k, v in counter.items():
            hq.append((-v, k))
        heapq.heapify(hq)

        res = ""
        pre = ()
        while hq:
            count, value = heapq.heappop(hq)
            res += value
            if pre and pre[0] < 0:
                heapq.heappush(hq, pre)
            pre = (count+1, value)
        return res


if __name__ == '__main__':
    cases = ["aaaa", "", "aabb", "aabc", "aac", "aabbcc", "abcdefgjdfk", "abcaabhfjsdhfhs"]
    for case in cases:
        demo = Solution()
        res = demo.reorganizeString(case)
        print(res)
