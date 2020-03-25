
import random
import time


def log_time(func):
    def wrap(*args):
        s_time = time.time()
        ret = func(*args)
        print(time.time() - s_time)
        return ret
    return wrap


quick_sort_lambda = lambda arr: arr if not arr else quick_sort_lambda([key for key in arr if key < arr[0]]) + [arr[0]] + quick_sort_lambda([key for key in arr if key > arr[0]])


def quick_sort(arr):
    if arr:
        left_arr, right_arr, mid_arr = [], [], []
        for key in arr:
            if key < arr[0]:
                left_arr.append(key)
            elif key > arr[0]:
                right_arr.append(key)
            else:
                mid_arr.append(key)
        # left_arr = [key for key in arr if key < arr[0]]
        # right_arr = [key for key in arr if key > arr[0]]
        return quick_sort(left_arr) + mid_arr + quick_sort(right_arr)
    return arr


@log_time
def log_quick_sort(arr):
    return quick_sort(arr)


class Solution(object):
    def quick_sort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def q_sort(arr):
            if not arr:
                return arr
            mid = arr[0]
            arr_left = []
            arr_right = []
            smaller = 0
            for ar in arr[1:]:
                if ar > mid:
                    arr_right.append(ar)
                else:
                    smaller += 1
                    arr_left.append(ar)
            print(smaller, mid)
            return q_sort(arr_left) + [mid] + q_sort(arr_right)
        return q_sort(nums)

if __name__ == '__main__':
        demo = Solution()
        print(demo.quick_sort([1,3,4,10,20, 3,9]))

        a = b = c = []
        c = ["abc"]
        print(a, b, c)
        samples = [random.randint(1, 100) for i in range(100)]
        print(log_quick_sort(samples))
        print(quick_sort_lambda(samples))
        print(quick_sort([1, 6, 10, 9, 7, 100, 100]))
