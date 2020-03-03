### 解题思路
此处撰写解题思路

### 代码

```python
class Solution(object):
    def merge(self, A, m, B, n):
        """
        :type A: List[int]
        :type m: int
        :type B: List[int]
        :type n: int
        :rtype: None Do not return anything, modify A in-place instead.
        """
        pa, pb = m - 1, n - 1
        cur = m + n -1
        while pa >= 0 or pb >= 0:
            # a_val, b_val = A[pa] if pa != -1 else None, B[pb] if pb != -1 else None
            # if pa >= 0:
            #     a_val = A[pa]
            # if pb >= 0:
            #     b_val = B[pb]
            if pa == -1:
                A[cur] = B[pb]
                pb -= 1
            elif pb == -1:
                A[cur] = A[pa]
                pa -= 1
            elif A[pa] > B[pb]:
                A[cur] = A[pa]
                pa -= 1
            else:
                A[cur] = B[pb]
                pb -= 1
            cur -= 1
```
