

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
    demo = Merge()
    res = demo.merge_sort([1,2,4,6,9,199,100, 1000, 233,12,19])
    # merge(0, len(arr))
    print(res)
