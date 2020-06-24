def binary_search(arr, target):
    i, j = 0, len(arr) - 1
    while i <= j:
        mid = (i + j) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            i = mid + 1
        else:
            j = mid - 1
    return i


def binary_search_left(arr, target):
    i, j = 0, len(arr) - 1
    while i < j:
        mid = (i + j) // 2
        if arr[mid] < target:
            i = mid + 1
        else:
            j = mid
    return i


def binary_search_right(arr, target):
    i, j = 0, len(arr) - 1
    while i < j:
        mid = (i + j) // 2 + 1
        if arr[mid] > target:
            j = mid - 1
        else:
            i = mid
    return j


if __name__ == '__main__':
    arr = [0, 1, 2, 3, 4, 5, 6, 6, 6, 7, 9, 10]
    target = 6
    res = binary_search(arr, target)
    print(res)

    res_l = binary_search_left(arr, 10)
    print(res_l)

    # arr = [1,1]
    res_r = binary_search_right(arr, 8)
    print(res_r)
