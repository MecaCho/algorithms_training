# encoding=utf8

'''
989. Add to Array-Form of Integer
For a non-negative integer X, the array-form of X is an array of its digits in left to right order.  For example, if X = 1231, then the array form is [1,2,3,1].

Given the array-form A of a non-negative integer X, return the array-form of the integer X+K.



Example 1:

Input: A = [1,2,0,0], K = 34
Output: [1,2,3,4]
Explanation: 1200 + 34 = 1234
Example 2:

Input: A = [2,7,4], K = 181
Output: [4,5,5]
Explanation: 274 + 181 = 455
Example 3:

Input: A = [2,1,5], K = 806
Output: [1,0,2,1]
Explanation: 215 + 806 = 1021
Example 4:

Input: A = [9,9,9,9,9,9,9,9,9,9], K = 1
Output: [1,0,0,0,0,0,0,0,0,0,0]
Explanation: 9999999999 + 1 = 10000000000


Note：

1 <= A.length <= 10000
0 <= A[i] <= 9
0 <= K <= 10000
If A.length > 1, then A[0] != 0


989. 数组形式的整数加法
对于非负整数 X 而言，X 的数组形式是每位数字按从左到右的顺序形成的数组。例如，如果 X = 1231，那么其数组形式为 [1,2,3,1]。

给定非负整数 X 的数组形式 A，返回整数 X+K 的数组形式。



示例 1：

输入：A = [1,2,0,0], K = 34
输出：[1,2,3,4]
解释：1200 + 34 = 1234
示例 2：

输入：A = [2,7,4], K = 181
输出：[4,5,5]
解释：274 + 181 = 455
示例 3：

输入：A = [2,1,5], K = 806
输出：[1,0,2,1]
解释：215 + 806 = 1021
示例 4：

输入：A = [9,9,9,9,9,9,9,9,9,9], K = 1
输出：[1,0,0,0,0,0,0,0,0,0,0]
解释：9999999999 + 1 = 10000000000


提示：

1 <= A.length <= 10000
0 <= A[i] <= 9
0 <= K <= 10000
如果 A.length > 1，那么 A[0] != 0
'''


class Solution(object):
    def addToArrayForm(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        i = len(A) - 1
        pre = 0
        while i >= 0:
            num = K % 10
            K /= 10
            sum_ = pre + num + A[i]
            pre = sum_ / 10
            A[i] = sum_ % 10
            i -= 1
        if K > 0 or pre > 0:
            return [int(i) for i in list(str(K+pre))] + A
        return A


# solutions

'''
方法一：逐位相加
思路

让我们逐位将数字加在一起。例如计算 123+912123+912，我们从低位到高位依次计算 3+23+2、2+12+1 和 1+91+9。任何时候，若加法的结果大于等于 1010，把进位的 11 加入到下一位的计算中，所以最终结果为 10351035。

代码

C++JavaGolangCJavaScript

func addToArrayForm(A []int, K int) (ans []int) {
    for i := len(A) - 1; i >= 0; i-- {
        sum := A[i] + K%10
        K /= 10
        if sum >= 10 {
            K++
            sum -= 10
        }
        ans = append(ans, sum)
    }
    for ; K > 0; K /= 10 {
        ans = append(ans, K%10)
    }
    reverse(ans)
    return
}

func reverse(A []int) {
    for i, n := 0, len(A); i < n/2; i++ {
        A[i], A[n-1-i] = A[n-1-i], A[i]
    }
}
另一个思路是将整个加数 KK 加入数组表示的数的最低位。

上面的例子 123+912123+912，我们把它表示成 [1,2,3+912][1,2,3+912]。然后，我们计算 3+912=9153+912=915。55 留在当前这一位，将 910/10=91910/10=91 以进位的形式加入下一位。

然后，我们再重复这个过程，计算 [1,2+91,5][1,2+91,5]。我们得到 9393，33 留在当前位，将 90/10=990/10=9 以进位的形式加入下一位。继而又得到 [1+9,3,5][1+9,3,5]，重复这个过程之后，最终得到结果 [1,0,3,5][1,0,3,5]。

C++JavaGolangCJavaScript

func addToArrayForm(A []int, K int) (ans []int) {
    for i := len(A) - 1; i >= 0 || K > 0; i-- {
        if i >= 0 {
            K += A[i]
        }
        ans = append(ans, K%10)
        K /= 10
    }
    reverse(ans)
    return
}

func reverse(A []int) {
    for i, n := 0, len(A); i < n/2; i++ {
        A[i], A[n-1-i] = A[n-1-i], A[i]
    }
}
复杂度分析

时间复杂度：O(\max(n,\log K))O(max(n,logK))，其中 nn 为数组的长度。

空间复杂度：O(\max(n,\log K))O(max(n,logK))。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/add-to-array-form-of-integer/solution/shu-zu-xing-shi-de-zheng-shu-jia-fa-by-l-jljp/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''



