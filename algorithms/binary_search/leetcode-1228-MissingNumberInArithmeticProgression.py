'''
1228. 等差数列中缺失的数字
有一个数组，其中的值符合等差数列的数值规律，也就是说：

在 0 <= i < arr.length - 1 的前提下，arr[i+1] - arr[i] 的值都相等。
我们会从该数组中删除一个 既不是第一个 也 不是最后一个的值，得到一个新的数组  arr。

给你这个缺值的数组 arr，请你帮忙找出被删除的那个数。



示例 1：

输入：arr = [5,7,11,13]
输出：9
解释：原来的数组是 [5,7,9,11,13]。
示例 2：

输入：arr = [15,13,12]
输出：14
解释：原来的数组是 [15,14,13,12]。


提示：

3 <= arr.length <= 1000
0 <= arr[i] <= 10^5

1228. Missing Number In Arithmetic Progression
In some array arr, the values were in arithmetic progression: the values arr[i+1] - arr[i] are all equal for every 0 <= i < arr.length - 1.

Then, a value from arr was removed that was not the first or last value in the array.

Return the removed value.



Example 1:

Input: arr = [5,7,11,13]
Output: 9
Explanation: The previous array was [5,7,9,11,13].
Example 2:

Input: arr = [15,13,12]
Output: 14
Explanation: The previous array was [15,14,13,12].


Constraints:

3 <= arr.length <= 1000
0 <= arr[i] <= 10^5
'''


class Solution(object):
    def missingNumber(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        if arr[-1] < arr[0]:
            arr = arr[::-1]
        a = min(arr[1] - arr[0], arr[-1] - arr[-2])
        if a == 0:
            return arr[0]

        num = (arr[-1] - arr[0]) / a + 1
        # print(a, num)
        sum_ = (arr[0] + arr[-1]) * num / 2

        return sum_ - sum(arr)
