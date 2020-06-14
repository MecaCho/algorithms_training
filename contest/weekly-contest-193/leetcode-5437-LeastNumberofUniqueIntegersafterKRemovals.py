'''
5437. 不同整数的最少数目
给你一个整数数组 arr 和一个整数 k 。现需要从数组中恰好移除 k 个元素，请找出移除后数组中不同整数的最少数目。



示例 1：

输入：arr = [5,5,4], k = 1
输出：1
解释：移除 1 个 4 ，数组中只剩下 5 一种整数。
示例 2：

输入：arr = [4,3,1,1,3,3,2], k = 3
输出：2
解释：先移除 4、2 ，然后再移除两个 1 中的任意 1 个或者三个 3 中的任意 1 个，最后剩下 1 和 3 两种整数。


提示：

1 <= arr.length <= 10^5
1 <= arr[i] <= 10^9
0 <= k <= arr.length

5437. Least Number of Unique Integers after K Removals
Given an array of integers arr and an integer k. Find the least number of unique integers after removing exactly k elements.



Example 1:

Input: arr = [5,5,4], k = 1
Output: 1
Explanation: Remove the single 4, only 5 is left.
Example 2:
Input: arr = [4,3,1,1,3,3,2], k = 3
Output: 2
Explanation: Remove 4, 2 and either one of the two 1s or three 3s. 1 and 3 will be left.


Constraints:

1 <= arr.length <= 10^5
1 <= arr[i] <= 10^9
0 <= k <= arr.length
'''

import collections


class Solution(object):
    def findLeastNumOfUniqueInts(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        d = collections.Counter(arr)
        values = sorted(d.values())
        count = len(values)
        for i in range(len(values)):
            val = values[i]
            if k >= val:
                k -= val
                count -= 1
            else:
                break
        return count

# golang

'''
func findLeastNumOfUniqueInts(arr []int, k int) int {
    length := len(arr)
    hashMap := make(map[int]int, length)
    for i := range arr{
        hashMap[arr[i]]++
    }

    values := []int{}
    for _, v := range hashMap{
        values = append(values, v)
    }

    sort.Ints(values)
    // fmt.Println(values)

    count := len(values)
    for i := range values{
        if k >= values[i] {
            k -= values[i]
            count --
        }else{
            break
        }
    }
    return count
}
'''

# tips

'''
Use a map to count the frequencies of the numbers in the array.

An optimal strategy is to remove the numbers with the smallest count first.
'''

