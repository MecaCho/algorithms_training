# encoding=utf8

class Solution(object):
    def reinitializePermutation(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 如果 i % 2 == 0 ，那么 arr[i] = perm[i / 2]
        # 如果 i % 2 == 1 ，那么 arr[i] = perm[n / 2 + (i - 1) / 2]
        perm = [i for i in range(n)]
        arr = [i for i in range(n)]
        count = 0
        while 1:
            for i in range(n):
                if i % 2 == 0:
                    arr[i] = perm[i / 2]
                else:
                    arr[i] = perm[n / 2 + (i - 1) / 2]
            print(arr, perm)
            count += 1
            if arr == [i for i in range(n)]:
                return count
            perm = arr[:]


import re


if __name__ == '__main__':
    demo = Solution()
    res = demo.reinitializePermutation(6)
    print res
