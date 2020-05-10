'''
5405. 形成两个异或相等数组的三元组数目
给你一个整数数组 arr 。

现需要从数组中取三个下标 i、j 和 k ，其中 (0 <= i < j <= k < arr.length) 。

a 和 b 定义如下：

a = arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1]
b = arr[j] ^ arr[j + 1] ^ ... ^ arr[k]
注意：^ 表示 按位异或 操作。

请返回能够令 a == b 成立的三元组 (i, j , k) 的数目。



示例 1：

输入：arr = [2,3,1,6,7]
输出：4
解释：满足题意的三元组分别是 (0,1,2), (0,2,2), (2,3,4) 以及 (2,4,4)
示例 2：

输入：arr = [1,1,1,1,1]
输出：10
示例 3：

输入：arr = [2,3]
输出：0
示例 4：

输入：arr = [1,3,5,7,9]
输出：3
示例 5：

输入：arr = [7,11,12,9,5,2,7,17,22]
输出：8


提示：

1 <= arr.length <= 300
1 <= arr[i] <= 10^8

5405. Count Triplets That Can Form Two Arrays of Equal XOR
Given an array of integers arr.

We want to select three indices i, j and k where (0 <= i < j <= k < arr.length).

Let's define a and b as follows:

a = arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1]
b = arr[j] ^ arr[j + 1] ^ ... ^ arr[k]
Note that ^ denotes the bitwise-xor operation.

Return the number of triplets (i, j and k) Where a == b.



Example 1:

Input: arr = [2,3,1,6,7]
Output: 4
Explanation: The triplets are (0,1,2), (0,2,2), (2,3,4) and (2,4,4)
Example 2:

Input: arr = [1,1,1,1,1]
Output: 10
Example 3:

Input: arr = [2,3]
Output: 0
Example 4:

Input: arr = [1,3,5,7,9]
Output: 3
Example 5:

Input: arr = [7,11,12,9,5,2,7,17,22]
Output: 8


Constraints:

1 <= arr.length <= 300
1 <= arr[i] <= 10^8
'''


class Solution(object):
    def countTriplets(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        xors = [0]
        for i in range(len(arr)):
            xors.append(xors[i ] ^arr[i])

        count = 0
        for i in range(len(arr)):
            for j in range( i +1, len(arr)):
                k = j
                while k < len(arr):
                    if xors[i] ^ xors[j] == xors[j] ^ xors[ k +1]:
                        count += 1
                    k += 1
        return count



class Solution0(object):
    def countTriplets(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        xors = []
        tmp = 0
        for i in range(len(arr)):
            tmp ^= arr[i]
            xors.append(tmp)
        xors.append(0)

        count = 0
        for i in range(len(arr)):
            for j in range( i +1, len(arr)):
                k = j
                while k < len(arr):
                    if xors[ i -1] ^ xors[ j -1] == xors[ j -1] ^ xors[k]:
                        # print(i, j, k)
                        count += 1
                    k += 1
        return count

# tips
'''
We are searching for sub-array of length ≥ 2 and we need to split it to 2 non-empty arrays so that the xor of the first array is equal to the xor of the second array. This is equivalent to searching for sub-array with xor = 0.

Keep the prefix xor of arr in another array, check the xor of all sub-arrays in O(n^2), if the xor of sub-array of length x is 0 add x-1 to the answer.
'''