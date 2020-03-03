
面试题 10.01. Sorted Merge LCCI
You are given two sorted arrays, A and B, where A has a large enough buffer at the end to hold B. Write a method to merge B into A in sorted order.

Initially the number of elements in A and B are m and n respectively.

Example:

Input:
A = [1,2,3,0,0,0], m = 3
B = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
    
面试题 10.01. 合并排序的数组
给定两个排序后的数组 A 和 B，其中 A 的末端有足够的缓冲空间容纳 B。 编写一个方法，将 B 合并入 A 并排序。

初始化 A 和 B 的元素数量分别为 m 和 n。

示例:

输入:
A = [1,2,3,0,0,0], m = 3
B = [2,5,6],       n = 3

输出: [1,2,2,3,5,6]

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
            a_val, b_val = A[pa] if pa != -1 else None, B[pb] if pb != -1 else None
            if a_val is None:
                A[cur] = b_val
                pb -= 1
            elif b_val is None:
                A[cur] = a_val
                pa -= 1
            elif a_val > b_val:
                A[cur] = a_val
                pa -= 1
            else:
                A[cur] = b_val
                pb -= 1
            cur -= 1
```
```
