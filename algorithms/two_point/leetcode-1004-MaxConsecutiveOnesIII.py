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



# solutions


'''
解题思路
重点：题意转换。把「最多可以把 K 个 0 变成 1，求仅包含 1 的最长子数组的长度」转换为 「找出一个最长的子数组，该子数组内最多允许有 K 个 0 」。
经过上面的题意转换，我们可知本题是求最大连续子区间，可以使用滑动窗口方法。滑动窗口的限制条件是：窗口内最多有 K 个 0。

可以使用我多次分享的滑动窗口模板解决，模板在代码之后。

代码思路：

使用 leftleft 和 rightright 两个指针，分别指向滑动窗口的左右边界。
rightright 主动右移：rightright 指针每次移动一步。当 A[right]A[right] 为 00，说明滑动窗口内增加了一个 00；
leftleft 被动右移：判断此时窗口内 00 的个数，如果超过了 KK，则 leftleft 指针被迫右移，直至窗口内的 00 的个数小于等于 KK 为止。
滑动窗口长度的最大值就是所求。
示例
以 A= [1,1,1,0,0,0,1,1,1,1,0], K = 2 为例，下面的动图演示了滑动窗口的两个指针的移动情况。



该动图对应的 PPT 在下面，可以点击逐步观看：


1 / 22

代码
提供 Python, C++, Java 三种代码可供阅读。

PythonC++Java

class Solution(object):
    def longestOnes(self, A, K):
        N = len(A)
        res = 0
        left, right = 0, 0
        zeros = 0 
        while right < N:
            if A[right] == 0:
                zeros += 1
            while zeros > K:
                if A[left] == 0:
                    zeros -= 1
                left += 1
            res = max(res, right - left + 1)
            right += 1
        return res
分享滑动窗口模板
《挑战程序设计竞赛》这本书中把滑动窗口叫做「虫取法」，我觉得非常生动形象。因为滑动窗口的两个指针移动的过程和虫子爬动的过程非常像：前脚不动，把后脚移动过来；后脚不动，把前脚向前移动。

我分享一个滑动窗口的模板，能解决大多数的滑动窗口问题：


def findSubArray(nums):
    N = len(nums) # 数组/字符串长度
    left, right = 0, 0 # 双指针，表示当前遍历的区间[left, right]，闭区间
    sums = 0 # 用于统计 子数组/子区间 是否有效，根据题目可能会改成求和/计数
    res = 0 # 保存最大的满足题目要求的 子数组/子串 长度
    while right < N: # 当右边的指针没有搜索到 数组/字符串 的结尾
        sums += nums[right] # 增加当前右边指针的数字/字符的求和/计数
        while 区间[left, right]不符合题意：# 此时需要一直移动左指针，直至找到一个符合题意的区间
            sums -= nums[left] # 移动左指针前需要从counter中减少left位置字符的求和/计数
            left += 1 # 真正的移动左指针，注意不能跟上面一行代码写反
        # 到 while 结束时，我们找到了一个符合题意要求的 子数组/子串
        res = max(res, right - left + 1) # 需要更新结果
        right += 1 # 移动右指针，去探索新的区间
    return res
滑动窗口中用到了左右两个指针，它们移动的思路是：以右指针作为驱动，拖着左指针向前走。右指针每次只移动一步，而左指针在内部 while 循环中每次可能移动多步。右指针是主动前移，探索未知的新区域；左指针是被迫移动，负责寻找满足题意的区间。

模板的整体思想是：

定义两个指针 left 和 right 分别指向区间的开头和结尾，注意是闭区间；定义 sums 用来统计该区间内的各个字符出现次数；
第一重 while 循环是为了判断 right 指针的位置是否超出了数组边界；当 right 每次到了新位置，需要增加 right 指针的求和/计数；
第二重 while 循环是让 left 指针向右移动到 [left, right] 区间符合题意的位置；当 left 每次移动到了新位置，需要减少 left 指针的求和/计数；
在第二重 while 循环之后，成功找到了一个符合题意的 [left, right] 区间，题目要求最大的区间长度，因此更新 res 为 max(res, 当前区间的长度) 。
right 指针每次向右移动一步，开始探索新的区间。
模板中的 sums 需要根据题目意思具体去修改，本题是求和题目因此把sums 定义成整数用于求和；如果是计数题目，就需要改成字典用于计数。当左右指针发生变化的时候，都需要更新 sums 。

另外一个需要根据题目去修改的是内层 while 循环的判断条件，即： 区间 [left, right][left,right] 不符合题意 。对于本题而言，就是该区间内的 0 的个数 超过了 2 。

刷题心得
2 月是滑动窗口月，基本上每个题目都可以直接套用滑动窗口模板。多做几遍就记住这个套路了。

作者：fuxuemingzhu
链接：https://leetcode-cn.com/problems/max-consecutive-ones-iii/solution/fen-xiang-hua-dong-chuang-kou-mo-ban-mia-f76z/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''

