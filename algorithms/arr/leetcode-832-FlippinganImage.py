# encoding=utf8

'''
832. Flipping an Image
Given a binary matrix A, we want to flip the image horizontally, then invert it, and return the resulting image.

To flip an image horizontally means that each row of the image is reversed.  For example, flipping [1, 1, 0] horizontally results in [0, 1, 1].

To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0. For example, inverting [0, 1, 1] results in [1, 0, 0].

Example 1:

Input: [[1,1,0],[1,0,1],[0,0,0]]
Output: [[1,0,0],[0,1,0],[1,1,1]]
Explanation: First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]
Example 2:

Input: [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
Output: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
Explanation: First reverse each row: [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]].
Then invert the image: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
Notes:

1 <= A.length = A[0].length <= 20
0 <= A[i][j] <= 1


832. 翻转图像
给定一个二进制矩阵 A，我们想先水平翻转图像，然后反转图像并返回结果。

水平翻转图片就是将图片的每一行都进行翻转，即逆序。例如，水平翻转 [1, 1, 0] 的结果是 [0, 1, 1]。

反转图片的意思是图片中的 0 全部被 1 替换， 1 全部被 0 替换。例如，反转 [0, 1, 1] 的结果是 [1, 0, 0]。

示例 1:

输入: [[1,1,0],[1,0,1],[0,0,0]]
输出: [[1,0,0],[0,1,0],[1,1,1]]
解释: 首先翻转每一行: [[0,1,1],[1,0,1],[0,0,0]]；
     然后反转图片: [[1,0,0],[0,1,0],[1,1,1]]
示例 2:

输入: [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
输出: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
解释: 首先翻转每一行: [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]]；
     然后反转图片: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
说明:

1 <= A.length = A[0].length <= 20
0 <= A[i][j] <= 1
'''


class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        for i in range(len(A)):
            A[i] = [1-j for j in A[i][::-1]]

        return A


class Solution1(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """

        return [[1-j for j in A[i][::-1]] for i in range(len(A))]


# solutions

'''
方法一：模拟优化 + 双指针
最直观的做法是首先对矩阵 AA 的每一行进行水平翻转操作，然后对矩阵中的每个元素进行反转操作。该做法需要遍历矩阵两次。

是否可以只遍历矩阵一次就完成上述操作？答案是肯定的。

假设矩阵的行数和列数都是 nn，考虑列下标 \textit{left}left 和 \textit{right}right，其中 \textit{left}<\textit{right}left<right 且 \textit{left}+\textit{right}=n-1left+right=n−1，当 0 \le i<n0≤i<n 时，对第 ii 行进行水平翻转之后，A[i][\textit{left}]A[i][left] 和 A[i][\textit{right}]A[i][right] 的元素值会互换，进行反转之后，A[i][\textit{left}]A[i][left] 和 A[i][\textit{right}]A[i][right] 的元素值都会改变。

具体而言，考虑以下四种情况。

情况一：A[i][\textit{left}]=0,A[i][\textit{right}]=0A[i][left]=0,A[i][right]=0。对第 ii 行进行水平翻转之后，A[i][\textit{left}]=0,A[i][\textit{right}]=0A[i][left]=0,A[i][right]=0。进行反转之后，A[i][\textit{left}]=1,A[i][\textit{right}]=1A[i][left]=1,A[i][right]=1。

情况二：A[i][\textit{left}]=1,A[i][\textit{right}]=1A[i][left]=1,A[i][right]=1。对第 ii 行进行水平翻转之后，A[i][\textit{left}]=1,A[i][\textit{right}]=1A[i][left]=1,A[i][right]=1。进行反转之后，A[i][\textit{left}]=0,A[i][\textit{right}]=0A[i][left]=0,A[i][right]=0。

情况三：A[i][\textit{left}]=0,A[i][\textit{right}]=1A[i][left]=0,A[i][right]=1。对第 ii 行进行水平翻转之后，A[i][\textit{left}]=1,A[i][\textit{right}]=0A[i][left]=1,A[i][right]=0。进行反转之后，A[i][\textit{left}]=0,A[i][\textit{right}]=1A[i][left]=0,A[i][right]=1。

情况四：A[i][\textit{left}]=1,A[i][\textit{right}]=0A[i][left]=1,A[i][right]=0。对第 ii 行进行水平翻转之后，A[i][\textit{left}]=0,A[i][\textit{right}]=1A[i][left]=0,A[i][right]=1。进行反转之后，A[i][\textit{left}]=1,A[i][\textit{right}]=0A[i][left]=1,A[i][right]=0。

情况一和情况二是 A[i][\textit{left}]=A[i][\textit{right}]A[i][left]=A[i][right] 的情况。在进行水平翻转和反转之后，A[i][\textit{left}]A[i][left] 和 A[i][\textit{right}]A[i][right] 的元素值都发生了改变，即元素值被反转。

情况三和情况四是 A[i][\textit{left}]\ne A[i][\textit{right}]A[i][left] 

​	
 =A[i][right] 的情况。在进行水平翻转和反转之后，A[i][\textit{left}]A[i][left] 和 A[i][\textit{right}]A[i][right] 的元素值都发生了两次改变，恢复原状。

因此，可以遍历矩阵一次即完成水平翻转和反转。

遍历矩阵的每一行。对于矩阵的第 ii 行，初始化 \textit{left}=0left=0 和 \textit{right}=n-1right=n−1，进行如下操作：

当 \textit{left}<\textit{right}left<right 时，判断 A[i][\textit{left}]A[i][left] 和 A[i][\textit{right}]A[i][right] 是否相等，如果相等则对 A[i][\textit{left}]A[i][left] 和 A[i][\textit{right}]A[i][right] 的值进行反转，如果不相等则不进行任何操作；

将 \textit{left}left 的值加 11，将 \textit{right}right 的值减 11，重复上述操作，直到 \textit{left} \ge \textit{right}left≥right；

如果 nn 是奇数，则上述操作结束时，\textit{left}left 和 \textit{right}right 的值相等，都指向第 ii 行的中间元素，此时需要对中间元素的值进行反转。

JavaJavaScriptGolangPython3C++C

class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        n = len(A)
        for i in range(n):
            left, right = 0, n - 1
            while left < right:
                if A[i][left] == A[i][right]:
                    A[i][left] ^= 1
                    A[i][right] ^= 1
                left += 1
                right -= 1
            if left == right:
                A[i][left] ^= 1
        return A
复杂度分析

时间复杂度：O(n^2)O(n 
2
 )，其中 nn 是矩阵 AA 的行数和列数。需要遍历矩阵一次，进行翻转操作。

空间复杂度：O(1)O(1)。除了返回值以外，额外使用的空间为常数。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/flipping-an-image/solution/fan-zhuan-tu-xiang-by-leetcode-solution-yljd/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
