
def check(pushed, poped):
    stack = []
    k = 0
    for i in range(len(pushed)):
        stack.append(pushed[i])
        # print(stack)
        while stack and poped[k] == stack[-1]:
            stack.pop()
            k += 1
    print(stack, k)



if __name__ == '__main__':
    check([1,2,3,4,5], [4,5,2,3,1])

    class Count(object):
        def get_count(self, arr):
            self.count = 0

            def quick_sort(arr):
                if len(arr) < 2:
                    return arr
                left, right = [], []
                for ar in arr[1:]:
                    if ar < arr[0]:
                        self.count += 1
                        left.append(ar)
                    else:
                        right.append(ar)
                return quick_sort(left) + [arr[0]] + quick_sort(right)

            res = quick_sort(arr)
            print(self.count, res)
            return self.count
    demo = Count()
    demo.get_count([1,2,3,5,1,6,9,4,199,12,19,99])
