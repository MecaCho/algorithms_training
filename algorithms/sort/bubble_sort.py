from algorithms.sort import base

@base.logFunc
def bubble_sort(arr):
    for i in range(len(arr)):

        # 提前退出冒泡循环的标志位
        flag = False

        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                # 表示有数据交换
                flag = True
        # 没有数据交换，提前退出
        if not flag:
            break
    return arr


if __name__ == '__main__':
    arr = [3, 5, 4, 1, 2, 6, 1, 2, 3]
    # arr = [1,3,2]
    res = bubble_sort(arr)
    print(arr)
    # print(res)
