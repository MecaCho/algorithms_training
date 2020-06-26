from algorithms.sort import base

@base.logFunc
def insert_sort(arr):
    if len(arr) < 2:
        return
    for i in range(1, len(arr)):

        val = arr[i]

        j = i - 1
        # 查找插入的位置
        while j >= 0:
            # 数据移动
            if val < arr[j]:
                arr[j+1] = arr[j]
            else:
                break
            j -= 1
        # 插入数据
        arr[j+1] = val


if __name__ == '__main__':
    # arr = [4,5,6,1,3,2]
    # insert_sort(arr)
    # print(arr)

    import random

    for num in [1, 10, 100, 1000, 10000, 100000]:
        arr = [random.randint(0, 200) for i in range(num)]
        insert_sort(arr)
        res = arr == sorted(arr)
        if not res:
            print(arr, sorted(arr))
        assert res
