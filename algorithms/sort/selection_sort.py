from algorithms.sort import base

@base.logFunc
def selection_sort(arr):
    for i in range(len(arr)):
        tmp = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[tmp]:
                tmp = j
        if tmp != i:
            arr[i], arr[tmp] = arr[tmp], arr[i]


if __name__ == '__main__':
    arr = [4, 5, 6, 3, 2, 1]
    selection_sort(arr)
    print(arr)
