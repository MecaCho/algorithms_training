
'''
1243. 数组变换
首先，给你一个初始数组 arr。然后，每天你都要根据前一天的数组生成一个新的数组。

第 i 天所生成的数组，是由你对第 i-1 天的数组进行如下操作所得的：

假如一个元素小于它的左右邻居，那么该元素自增 1。
假如一个元素大于它的左右邻居，那么该元素自减 1。
首、尾元素 永不 改变。
过些时日，你会发现数组将会不再发生变化，请返回最终所得到的数组。



示例 1：

输入：[6,2,3,4]
输出：[6,3,3,4]
解释：
第一天，数组从 [6,2,3,4] 变为 [6,3,3,4]。
无法再对该数组进行更多操作。
示例 2：

输入：[1,6,3,4,3,5]
输出：[1,4,4,4,4,5]
解释：
第一天，数组从 [1,6,3,4,3,5] 变为 [1,5,4,3,4,5]。
第二天，数组从 [1,5,4,3,4,5] 变为 [1,4,4,4,4,5]。
无法再对该数组进行更多操作。


提示：

1 <= arr.length <= 100
1 <= arr[i] <= 100

1243. Array Transformation
Given an initial array arr, every day you produce a new array using the array of the previous day.

On the i-th day, you do the following operations on the array of day i-1 to produce the array of day i:

If an element is smaller than both its left neighbor and its right neighbor, then this element is incremented.
If an element is bigger than both its left neighbor and its right neighbor, then this element is decremented.
The first and last elements never change.
After some days, the array does not change. Return that final array.



Example 1:

Input: arr = [6,2,3,4]
Output: [6,3,3,4]
Explanation:
On the first day, the array is changed from [6,2,3,4] to [6,3,3,4].
No more operations can be done to this array.
Example 2:

Input: arr = [1,6,3,4,3,5]
Output: [1,4,4,4,4,5]
Explanation:
On the first day, the array is changed from [1,6,3,4,3,5] to [1,5,4,3,4,5].
On the second day, the array is changed from [1,5,4,3,4,5] to [1,4,4,4,4,5].
No more operations can be done to this array.


Constraints:

1 <= arr.length <= 100
1 <= arr[i] <= 100
'''






class Solution(object):
    def transformArray(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        import copy
        self.arr = arr
        def adjust():
            flag = 0
            tmp = copy.deepcopy(self.arr)
            for i in range(1, len(self.arr)-1):
                if self.arr[i] < self.arr[i-1] and self.arr[i] < self.arr[i+1]:
                    tmp[i] += 1
                    flag = 1
                elif self.arr[i] > self.arr[i-1] and self.arr[i] > self.arr[i+1]:
                    tmp[i] -= 1
                    flag = 1
            self.arr[:] = tmp
            return flag
        ad = adjust()
        while ad:
            ad = adjust()
        return self.arr


class Solution1(object):
    def transformArray(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        import copy
        self.arr = arr
        def adjust():
            # flag = 0
            # tmp = copy.deepcopy(self.arr)
            change = []
            for i in range(1, len(self.arr)-1):
                if self.arr[i] < self.arr[i-1] and self.arr[i] < self.arr[i+1]:
                    # tmp[i] += 1
                    # flag = 1
                    change.append((i, 1))
                elif self.arr[i] > self.arr[i-1] and self.arr[i] > self.arr[i+1]:
                    # tmp[i] -= 1
                    # flag = 1
                    change.append((i, -1))
            for index, add in change:
                self.arr[index] += add
            # self.arr[:] = tmp
            return True if change else False
        ad = adjust()
        # print(ad)
        while ad:
            # print(ad)
            ad = adjust()
        return self.arr
