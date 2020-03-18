'''
1085. Sum of Digits in the Minimum Number
Given an array A of positive integers, let S be the sum of the digits of the minimal element of A.

Return 0 if S is odd, otherwise return 1.

 

Example 1:

Input: [34,23,1,24,75,33,54,8]
Output: 0
Explanation: 
The minimal element is 1, and the sum of those digits is S = 1 which is odd, so the answer is 0.
Example 2:

Input: [99,77,33,66,55]
Output: 1
Explanation: 
The minimal element is 33, and the sum of those digits is S = 3 + 3 = 6 which is even, so the answer is 1.
 

Note:

1 <= A.length <= 100
1 <= A[i].length <= 100

1085. 最小元素各数位之和
给你一个正整数的数组 A。

然后计算 S，使其等于数组 A 当中最小的那个元素各个数位上数字之和。

最后，假如 S 所得计算结果是 奇数 的请你返回 0，否则请返回 1。

 

示例 1:

输入：[34,23,1,24,75,33,54,8]
输出：0
解释：
最小元素为 1，该元素各个数位上的数字之和 S = 1，是奇数所以答案为 0。
示例 2：

输入：[99,77,33,66,55]
输出：1
解释：
最小元素为 33，该元素各个数位上的数字之和 S = 3 + 3 = 6，是偶数所以答案为 1。
 

提示：

1 <= A.length <= 100
1 <= A[i].length <= 100
'''

class Solution(object):
    def sumOfDigits(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        min_A = min(A)
        res = 0
        while min_A:
            res += min_A % 10
            min_A /= 10
        return abs(res % 2 - 1)
