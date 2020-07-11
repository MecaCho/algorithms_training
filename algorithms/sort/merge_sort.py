
'''
面试题51. 数组中的逆序对
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组，求出这个数组中的逆序对的总数。



示例 1:

输入: [7,5,6,4]
输出: 5


限制：

0 <= 数组长度 <= 50000


'''
class Merge(object):

    def merge_sort(self, arr):
        self.arr = arr
        self.count = 0
        def merge(l, r):
            if r - l <= 1:
                return
            mid = (l + r) // 2
            merge(l, mid)
            merge(mid, r)
            i = l
            j = mid
            tmp = []
            print(i, j, mid, self.arr, l, r)
            while i < mid or j < r:
                if i >= mid:
                    tmp.extend(self.arr[j:r])
                    break
                if j >= r:
                    tmp.extend(self.arr[i:mid])
                    break
                if self.arr[i] <= self.arr[j]:
                    tmp.append(self.arr[i])
                    i += 1
                else:
                    self.count += j - mid + 1
                    tmp.append(self.arr[j])
                    j += 1
            self.arr[l:r] = tmp
            return
        merge(0, len(self.arr))
        return self.arr, self.count

# if __name__ == '__main__':
#     l = [1, 2, 4, 5, 1, 1, 1]
#     def j(l, step):
#         if len(l) < 2:
#             return len(l)
#         for i in range(1, len(l)):
#             max_length = l[i] + i
#             if max_length > len(l):
#                 new_l = l[:i]
#                 step += j(new_l, 0)
#         print(l, step)
#         return step
#     res = j(l, 0)
#     print(res)

if __name__ == '__main__':
    # demo = Merge()
    # res = demo.merge_sort([1,2,4,6,9,199,100, 1000, 233,12,19])
    # # merge(0, len(arr))
    # print(res)

    def merge_sort(arr):
        if len(arr) < 2:
            return arr
        mid = len(arr) // 2
        print(arr[:mid], mid, arr[mid:])
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])
        new_arr = []
        while left or right:
            print(left, right)
            while left and right:
                print(left, right)
                if left[0] < right[0]:
                    new_arr.append(left.pop(0))
                else:
                    new_arr.append(right.pop(0))
            if left:
                new_arr.extend(left)
                break
            if right:
                new_arr.extend(right)
                break
        return new_arr

    def merge_sort_indexs(arr):
        if len(arr) < 2:
            return arr
        mid = len(arr) // 2
        # print(arr[:mid], mid, arr[mid:])
        left = merge_sort_indexs(arr[:mid])
        right = merge_sort_indexs(arr[mid:])
        new_arr = []
        while left or right:
            while left and right:
                if left[0][1] > right[0][1]:
                    larger[left[0][0]] += len(right)
                    new_arr.append(left.pop(0))
                else:
                    # larger[right[0][0]] += len(left)
                    new_arr.append(right.pop(0))
            if left:
                new_arr.extend(left)
                break
            if right:
                new_arr.extend(right)
                break
        return new_arr
    # arr = [1,2,4,6,9,199,100, 1000, 233,12,19,1,2,2,2,2]
    arr = [1,3,2,5]
    larger = [0 for _ in arr]
    new_arr = []
    for i, v in enumerate(arr):
        new_arr.append((i, v))
    res = merge_sort_indexs(new_arr)

    print(larger)
    print(res)
