
'''
1426. 数元素
给你一个整数数组 arr， 对于元素 x ，只有当 x + 1 也在数组 arr 里时，才能记为 1 个数。

如果数组 arr 里有重复的数，每个重复的数单独计算。



示例 1：

输入：arr = [1,2,3]
输出：2
解释：1 和 2 被计算次数因为 2 和 3 在数组 arr 里。
示例 2：

输入：arr = [1,1,3,3,5,5,7,7]
输出：0
解释：所有的数都不算, 因为数组里没有 2、4、6、8。
示例 3：

输入：arr = [1,3,2,3,5,0]
输出：3
解释：0、1、2 被计算了因为 1、2、3 在数组里。
示例 4：

输入：arr = [1,1,2,2]
输出：2
解释：两个 1 被计算了因为有 2 在数组里。


提示：

1 <= arr.length <= 1000
0 <= arr[i] <= 1000

1426. Counting Elements
Given an integer array arr, count how many elements x there are, such that x + 1 is also in arr.

If there're duplicates in arr, count them seperately.



Example 1:

Input: arr = [1,2,3]
Output: 2
Explanation: 1 and 2 are counted cause 2 and 3 are in arr.
Example 2:

Input: arr = [1,1,3,3,5,5,7,7]
Output: 0
Explanation: No numbers are counted, cause there's no 2, 4, 6, or 8 in arr.
Example 3:

Input: arr = [1,3,2,3,5,0]
Output: 3
Explanation: 0, 1 and 2 are counted cause 1, 2 and 3 are in arr.
Example 4:

Input: arr = [1,1,2,2]
Output: 2
Explanation: Two 1s are counted cause 2 is in arr.
Example 5:

Input: arr = [1,1,2]
Output: 2
Explanation: Both 1s are counted because 2 is in the array.


Constraints:

1 <= arr.length <= 1000
0 <= arr[i] <= 1000
'''



class Solution(object):
    def countElements(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        hash_map = defaultdict(int)
        count = 0
        for i in range(len(arr)):
            hash_map[arr[i]] += 1
        for k, v in hash_map.items():
            if k + 1 in hash_map:
                count += v
        return count


class Solution1(object):
    def countElements(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        # return sum(k + 1 in set(arr) for k in arr)
        return len([i  for i in arr if i+1 in set(arr)])

# tips

'''
Use hashset to store all elements.
Loop again to count all valid elements.
'''