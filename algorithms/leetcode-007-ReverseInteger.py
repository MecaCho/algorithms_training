```Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-integer
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
```
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if -10< x < 10:
            return x
        res = int(str(x)[::-1].lstrip("0") if x > 0 else "-" + str(x)[:0:-1].lstrip("0"))
        if -2**31<res<2**31-1:
            return res
        return 0
