class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        num = int(*re.findall("^[\-\+]?\d+", str.strip(" ")))
        return min(2**31 -1, max(-2**31, num))
