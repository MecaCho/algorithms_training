
'''
面试题66. 构建乘积数组
给定一个数组 A[0,1,…,n-1]，请构建一个数组 B[0,1,…,n-1]，其中 B 中的元素 B[i]=A[0]×A[1]×…×A[i-1]×A[i+1]×…×A[n-1]。不能使用除法。



示例:

输入: [1,2,3,4,5]
输出: [120,60,40,30,24]


提示：

所有元素乘积之和不会溢出 32 位整数
a.length <= 100000
'''



class Solution(object):
    def constructArr(self, a):
        """
        :type a: List[int]
        :rtype: List[int]
        """
        left = []
        base = 1
        for num in a:
            left.append(base)
            base *= num

        right = []
        base = 1
        for i in range(len(a ) -1, -1, -1):
            right.append(base)
            base *= a[i]
        print(left, right)

        length = len(a) - 1
        return [right[length - i ] *left[i] for i in range(length +1)]

