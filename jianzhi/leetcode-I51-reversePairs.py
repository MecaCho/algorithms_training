
'''
面试题51. 数组中的逆序对
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组，求出这个数组中的逆序对的总数。



示例 1:

输入: [7,5,6,4]
输出: 5


限制：

0 <= 数组长度 <= 50000
'''


class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # count = 0
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[j] < nums[i]:
        #             count += 1
        # return count
        # self.count = 0
        # def quick_sort(arr):
        #     if len(arr) < 2:
        #         return arr
        #     left, right = [], []
        #     for ar in arr[1:]:
        #         if ar <= arr[0]:

        #             left.append(ar)
        #         else:
        #             self.count += 1
        #             right.append(ar)
        #     return quick_sort(left) + [arr[0]] + quick_sort(right)
        # quick_sort(nums)
        # return self.count
        self.count = 0
        def merge_sort(l, r):
            if r - l <= 1:
                return
            mid = ( l +r) // 2
            # print(l, r, mid)
            merge_sort(l, mid)
            merge_sort(mid, r)
            i, j = l, mid

            tmp = []
            while j < r and i < mid:
                if nums[i] > nums[j]:
                    self.count += mid - i
                    tmp.append(nums[j])
                    j += 1
                else:
                    tmp.append(nums[i])
                    i += 1
            while j < r:
                tmp.append(nums[j])
                j += 1
            while i < mid:
                tmp.append(nums[i])
                i += 1
            nums[l:r] = tmp
            return
        merge_sort(0, len(nums))
        return self.count
