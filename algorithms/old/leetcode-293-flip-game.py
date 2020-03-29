class Solution(object):
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        return ["".join([s[:i], "--", s[i + 2:]]) for i in xrange(0, len(s) - 1) if s[i] == "+" and s[i + 1] == "+"]
