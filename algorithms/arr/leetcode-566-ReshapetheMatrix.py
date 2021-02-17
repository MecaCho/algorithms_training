# encoding=utf8

'''
566. Reshape the Matrix
In MATLAB, there is a very useful function called 'reshape', which can reshape a matrix into a new one with different size but keep its original data.

You're given a matrix represented by a two-dimensional array, and two positive integers r and c representing the row number and column number of the wanted reshaped matrix, respectively.

The reshaped matrix need to be filled with all the elements of the original matrix in the same row-traversing order as they were.

If the 'reshape' operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.

Example 1:
Input:
nums =
[[1,2],
 [3,4]]
r = 1, c = 4
Output:
[[1,2,3,4]]
Explanation:
The row-traversing of nums is [1,2,3,4]. The new reshaped matrix is a 1 * 4 matrix, fill it row by row by using the previous list.
Example 2:
Input:
nums =
[[1,2],
 [3,4]]
r = 2, c = 4
Output:
[[1,2],
 [3,4]]
Explanation:
There is no way to reshape a 2 * 2 matrix to a 2 * 4 matrix. So output the original matrix.
Note:
The height and width of the given matrix is in range [1, 100].
The given r and c are all positive.


566. 重塑矩阵
在MATLAB中，有一个非常有用的函数 reshape，它可以将一个矩阵重塑为另一个大小不同的新矩阵，但保留其原始数据。

给出一个由二维数组表示的矩阵，以及两个正整数r和c，分别表示想要的重构的矩阵的行数和列数。

重构后的矩阵需要将原始矩阵的所有元素以相同的行遍历顺序填充。

如果具有给定参数的reshape操作是可行且合理的，则输出新的重塑矩阵；否则，输出原始矩阵。

示例 1:

输入:
nums =
[[1,2],
 [3,4]]
r = 1, c = 4
输出:
[[1,2,3,4]]
解释:
行遍历nums的结果是 [1,2,3,4]。新的矩阵是 1 * 4 矩阵, 用之前的元素值一行一行填充新矩阵。
示例 2:

输入:
nums =
[[1,2],
 [3,4]]
r = 2, c = 4
输出:
[[1,2],
 [3,4]]
解释:
没有办法将 2 * 2 矩阵转化为 2 * 4 矩阵。 所以输出原矩阵。
注意：

给定矩阵的宽和高范围在 [1, 100]。
给定的 r 和 c 都是正数。
'''



class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if not nums:
            return nums
        r0, c0 = len(nums), len(nums[0])
        if r*c != r0*c0:
            return nums

        res = []
        for i in range(r0):
            for j in range(c0):
                if not res or len(res[-1]) == 0 or len(res[-1]) == c:
                    res.append([nums[i][j]])
                else:
                    res[-1].append(nums[i][j])

        return res

# golang solution

'''
func matrixReshape(nums [][]int, r int, c int) [][]int {
	if len(nums) == 0 {
		return nums
	}

	r0, c0 := len(nums), len(nums[0])
	if r0*c0 != r*c {
		return nums
	}

	res := make([][]int, r)
	for i, num := range nums {
		for j, nu := range num {
			index := (i*c0 + j) / c
			fmt.Println(index, nu, i*c0 + j, c)
			res[index] = append(res[index], nu)
		}
	}
	return res

}
'''

# solutions

'''
方法一：二维数组的一维表示
思路与算法

对于一个行数为 mm，列数为 nn，行列下标都从 00 开始编号的二维数组，我们可以通过下面的方式，将其中的每个元素 (i, j)(i,j) 映射到整数域内，并且它们按照行优先的顺序一一对应着 [0, mn)[0,mn) 中的每一个整数。形象化地来说，我们把这个二维数组「排扁」成了一个一维数组。如果读者对机器学习有一定了解，可以知道这就是 \texttt{flatten}flatten 操作。

这样的映射即为：

(i, j) \to i \times n+j
(i,j)→i×n+j

同样地，我们可以将整数 xx 映射回其在矩阵中的下标，即

\begin{cases} i = x ~/~ n \\ j = x ~\%~ n \end{cases}
{ 
i=x / n
j=x % n
​	
 

其中 // 表示整数除法，\%% 表示取模运算。

那么题目需要我们做的事情相当于：

将二维数组 \textit{nums}nums 映射成一个一维数组；

将这个一维数组映射回 rr 行 cc 列的二维数组。

我们当然可以直接使用一个一维数组进行过渡，但我们也可以直接从二维数组 \textit{nums}nums 得到 rr 行 cc 列的重塑矩阵：

设 \textit{nums}nums 本身为 mm 行 nn 列，如果 mn \neq rcmn 

​	
 =rc，那么二者包含的元素个数不相同，因此无法进行重塑；

否则，对于 x \in [0, mn)x∈[0,mn)，第 xx 个元素在 \textit{nums}nums 中对应的下标为 (x ~/~ n, x~\%~ n)(x / n,x % n)，而在新的重塑矩阵中对应的下标为 (x ~/~ c, x~\%~ c)(x / c,x % c)。我们直接进行赋值即可。

代码

C++JavaPython3JavaScriptGolangC

func matrixReshape(nums [][]int, r int, c int) [][]int {
    n, m := len(nums), len(nums[0])
    if n*m != r*c {
        return nums
    }
    ans := make([][]int, r)
    for i := range ans {
        ans[i] = make([]int, c)
    }
    for i := 0; i < n*m; i++ {
        ans[i/c][i%c] = nums[i/m][i%m]
    }
    return ans
}
复杂度分析

时间复杂度：O(rc)O(rc)。这里的时间复杂度是在重塑矩阵成功的前提下的时间复杂度，否则当 mn \neq rcmn 

​	
 =rc 时，\texttt{C++}C++ 语言中返回的是原数组的一份拷贝，本质上需要的时间复杂度为 O(mn)O(mn)，而其余语言可以直接返回原数组的对象，需要的时间复杂度仅为 O(1)O(1)。

空间复杂度：O(1)O(1)。这里的空间复杂度不包含返回的重塑矩阵需要的空间。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/reshape-the-matrix/solution/zhong-su-ju-zhen-by-leetcode-solution-gt0g/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''


