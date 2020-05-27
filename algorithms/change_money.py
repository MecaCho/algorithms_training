from functools import wraps

arr = [10, 5, 2, 1]

N = 5

def change(arr, n):
    ret = []
    for i in arr:
        while n >= i:
            ret.append(i)
            n = n-i
    if n == 0:
        return ret

def fac(n):
    if n == 1:
        return 1
    if n == 0:
        return 1
    if n < 0:
        return 0
    if n == 2:
        return 2
    if n== 3:
        return 2
    else:
        return fac(n-2)+fac(n-5)+fac(n-10)+fac(n-1)


def solution(arr, ret):
    ret_ = []
    for i in ret:
        pass

def solution_itoor(n, arr):
    import itertools
    ret = 0
    for i in xrange(1,n+1):
        sub_list = itertools.combinations_with_replacement(arr, i)
        for sub in sub_list:
            # print sub
            if sum(sub) == n:
                ret += 1
    return ret


if __name__ == "__main__":
    # print change(arr, N)
    # for i in xrange(10):
    #     print i,fac(i)
    # print fac(N)
    # print solution_itoor(N, arr)

    '''
    1 1
    2 11 2
    3 111 21
    4 1111 211 22
    5 11111 221 2111 5
    6 111111 51 42 33
    7 111111 61 52 43
    '''

    a = []
    def change(a=None):
        a = [1,2,3]
        return a
    change(a)
    print(a)
