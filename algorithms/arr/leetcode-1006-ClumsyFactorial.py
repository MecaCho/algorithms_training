# encoding=utf8

'''
1006. Clumsy Factorial
Normally, the factorial of a positive integer n is the product of all positive integers less than or equal to n.  For example, factorial(10) = 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1.

We instead make a clumsy factorial: using the integers in decreasing order, we swap out the multiply operations for a fixed rotation of operations: multiply (*), divide (/), add (+) and subtract (-) in this order.

For example, clumsy(10) = 10 * 9 / 8 + 7 - 6 * 5 / 4 + 3 - 2 * 1.  However, these operations are still applied using the usual order of operations of arithmetic: we do all multiplication and division steps before any addition or subtraction steps, and multiplication and division steps are processed left to right.

Additionally, the division that we use is floor division such that 10 * 9 / 8 equals 11.  This guarantees the result is an integer.

Implement the clumsy function as defined above: given an integer N, it returns the clumsy factorial of N.



Example 1:

Input: 4
Output: 7
Explanation: 7 = 4 * 3 / 2 + 1
Example 2:

Input: 10
Output: 12
Explanation: 12 = 10 * 9 / 8 + 7 - 6 * 5 / 4 + 3 - 2 * 1


Note:

1 <= N <= 10000
-2^31 <= answer <= 2^31 - 1  (The answer is guaranteed to fit within a 32-bit integer.)


1006. 笨阶乘
通常，正整数 n 的阶乘是所有小于或等于 n 的正整数的乘积。例如，factorial(10) = 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1。

相反，我们设计了一个笨阶乘 clumsy：在整数的递减序列中，我们以一个固定顺序的操作符序列来依次替换原有的乘法操作符：乘法(*)，除法(/)，加法(+)和减法(-)。

例如，clumsy(10) = 10 * 9 / 8 + 7 - 6 * 5 / 4 + 3 - 2 * 1。然而，这些运算仍然使用通常的算术运算顺序：我们在任何加、减步骤之前执行所有的乘法和除法步骤，并且按从左到右处理乘法和除法步骤。

另外，我们使用的除法是地板除法（floor division），所以 10 * 9 / 8 等于 11。这保证结果是一个整数。

实现上面定义的笨函数：给定一个整数 N，它返回 N 的笨阶乘。



示例 1：

输入：4
输出：7
解释：7 = 4 * 3 / 2 + 1
示例 2：

输入：10
输出：12
解释：12 = 10 * 9 / 8 + 7 - 6 * 5 / 4 + 3 - 2 * 1


提示：

1 <= N <= 10000
-2^31 <= answer <= 2^31 - 1  （答案保证符合 32 位整数。）
'''


class Solution(object):
    def clumsy(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N == 1:
            return 1
        elif N == 2:
            return 2
        elif N == 3:
            return 6
        elif N == 4:
            return 7

        if N % 4 == 0:
            return N + 1
        elif N % 4 <= 2:
            return N + 2
        else:
            return N - 1


class Solutionxxx(object):
    def clumsy(self, N):
        """
        :type N: int
        :rtype: int
        """
        def cal_unit(k):
            nums = [i for i in range(k, k-4, -1) if i > 0]
            print(k, nums)
            if not nums:
                return 0
            if len(nums) == 1:
                return nums[0]
            elif len(nums) == 2:
                return - nums[0] * nums[1]
            elif len(nums) == 3:
                return - (nums[0] * nums[1] / nums[2])
            else:
                return - (nums[0] * nums[1] / nums[2]) + nums[3]

        res = (N * (N-1) / (N-2) + (N-3)) if N > 4 else 0
        self.vals = []
        for i in range(N-4, -1, -4):
            val = cal_unit(i)
            if i == N:
                res += val
            else:
                res -= val
            self.vals.append(val)
        print(i, self.vals)
        res += cal_unit(i)
        return res


if __name__ == '__main__':
    demo = Solution()
    res = demo.clumsy(100)
    print res
