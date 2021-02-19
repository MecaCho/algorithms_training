# encoding=utf8


'''
1004. 最大连续1的个数 III
给定一个由若干 0 和 1 组成的数组 A，我们最多可以将 K 个值从 0 变成 1 。

返回仅包含 1 的最长（连续）子数组的长度。



示例 1：

输入：A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
输出：6
解释：
[1,1,1,0,0,1,1,1,1,1,1]
粗体数字从 0 翻转到 1，最长的子数组长度为 6。
示例 2：

输入：A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
输出：10
解释：
[0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
粗体数字从 0 翻转到 1，最长的子数组长度为 10。


提示：

1 <= A.length <= 20000
0 <= K <= A.length
A[i] 为 0 或 1

1004. Max Consecutive Ones III
Given an array A of 0s and 1s, we may change up to K values from 0 to 1.

Return the length of the longest (contiguous) subarray that contains only 1s.



Example 1:

Input: A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
Output: 6
Explanation:
[1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.
Example 2:

Input: A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
Output: 10
Explanation:
[0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.


Note:

1 <= A.length <= 20000
0 <= K <= A.length
A[i] is 0 or 1
'''

# golang

'''
func longestOnes(A []int, K int) int {

	if len(A) < K+1 {
		return len(A)
	}
	
	zeroIndexs := []int{}
    for i := 0; i < K+1;i++{
        zeroIndexs = append(zeroIndexs, -1)
    }
	maxLength := K

	i := -1
	lastZeroIndex := -1
	preLastZeroIndex := -1

	length := len(A)

	for k := 0; k < length; k++ {
		if A[k] == 1 {
			newLength := k - i
			if newLength > maxLength {
				maxLength = newLength
			}
		} else {
			zeroIndexs = zeroIndexs[1:K+1]
			zeroIndexs = append(zeroIndexs, k)
			
			preLastZeroIndex = zeroIndexs[0]
			lastZeroIndex = k
            i = preLastZeroIndex
		}
	}
	if lastZeroIndex == -1 {
		maxLength = length
	}
    newLength := length - 1 - i
    if newLength > maxLength {
        maxLength = newLength
    }
	return maxLength
}
'''

# tips

'''
One thing's for sure, we will only flip a zero if it extends an existing window of 1s. Otherwise, there's no point in doing it, right? Think Sliding Window!

Since we know this problem can be solved using the sliding window construct, we might as well focus in that direction for hints. Basically, in a given window, we can never have > K zeros, right?

We don't have a fixed size window in this case. The window size can grow and shrink depending upon the number of zeros we have (we don't actually have to flip the zeros here!).

The way to shrink or expand a window would be based on the number of zeros that can still be flipped and so on.

'''

# solution


class Solution(object):
    def longestOnes(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        l, r = 0, 0
        res = 0
        while r < len(A):
            if A[r] == 0:
                if K == 0:
                    while A[l] == 1:
                        l += 1
                    l += 1
                else:
                    K -= 1

            r += 1
            res = max(res, r - l)

        return res


