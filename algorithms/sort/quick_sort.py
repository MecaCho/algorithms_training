
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


# or each (unsorted) partition
# set first element as pivot
#   storeIndex = pivotIndex + 1
#   for i = pivotIndex + 1 to rightmostIndex
#     if element[i] < element[pivot]
#       swap(i, storeIndex); storeIndex++
#   swap(pivot, storeIndex - 1)


def quick_sort1(arr, left, right):
    print(arr, left, right)
    if right - left < 1:
        return
    val = arr[left]
    l, r = left, right
    while l < r:
        while l < r and arr[r] > val:
            r -= 1
        if l < r:
            arr[l] = arr[r]
        while l < r and arr[l] < val:
            l += 1
        if l < r:
            arr[r] = arr[l]
            r -= 1
    arr[l] = val
    quick_sort1(arr, left, l-1)
    quick_sort1(arr, l+1, right)
from algorithms.sort import base
import random
@base.logFunc
def quick_sort_new(arr):
    exchange = random.randint(1,10)
    arr[exchange], arr[0] = arr[0], arr[exchange]
    quick_sort2(arr, 0, len(arr)-1)

def quick_sort2(arr, left, right):
    if right - left < 1:
        return
    loc = left + 1
    val = arr[left]

    for i in range(left+1, right+1):
        if arr[i] < val:
            arr[i], arr[loc] = arr[loc], arr[i]
            loc += 1
    arr[left], arr[loc-1] = arr[loc-1], arr[left]

    quick_sort2(arr, left, loc-1)
    quick_sort2(arr, loc, right)

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

@base.logFunc
def sort_lib_python(arr):
    arr.sort()

if __name__ == '__main__':
        # demo = Solution()
        # print(demo.quick_sort([1,3,4,10,20, 3,9]))
        #
        # a = b = c = []
        # c = ["abc"]
        # print(a, b, c)
        # samples = [random.randint(1, 100) for i in range(100)]
        # print(log_quick_sort(samples))
        # print(quick_sort_lambda(samples))
        # print(quick_sort([1, 6, 10, 9, 7, 100, 100]))

        arr = [1,3,4,2, 100, 101, 99]
        quick_sort2(arr, 0, len(arr) - 1)
        print(arr)
        import random
        for num in [20, 100, 1000, 10000, 100000]:
            arr = [random.randint(0, 200) for i in range(num)]
            arr.sort()
            quick_sort_new(arr)
            res = arr == sorted(arr)
            if not res:
                print(arr, sorted(arr))
            assert res

            # print(res, arr)
