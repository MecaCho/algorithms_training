# encoding=utf8

'''
1310. XOR Queries of a Subarray

Given the array arr of positive integers and the array queries where queries[i] = [Li, Ri], for each query i compute the XOR of elements from Li to Ri (that is, arr[Li] xor arr[Li+1] xor ... xor arr[Ri] ). Return an array containing the result for the given queries.
 

Example 1:

Input: arr = [1,3,4,8], queries = [[0,1],[1,2],[0,3],[3,3]]
Output: [2,7,14,8] 
Explanation: 
The binary representation of the elements in the array are:
1 = 0001 
3 = 0011 
4 = 0100 
8 = 1000 
The XOR values for queries are:
[0,1] = 1 xor 3 = 2 
[1,2] = 3 xor 4 = 7 
[0,3] = 1 xor 3 xor 4 xor 8 = 14 
[3,3] = 8
Example 2:

Input: arr = [4,8,2,10], queries = [[2,3],[1,3],[0,0],[0,3]]
Output: [8,0,4,4]
 

Constraints:

1 <= arr.length <= 3 * 10^4
1 <= arr[i] <= 10^9
1 <= queries.length <= 3 * 10^4
queries[i].length == 2
0 <= queries[i][0] <= queries[i][1] < arr.length


1310. 子数组异或查询

有一个正整数数组 arr，现给你一个对应的查询数组 queries，其中 queries[i] = [Li, Ri]。

对于每个查询 i，请你计算从 Li 到 Ri 的 XOR 值（即 arr[Li] xor arr[Li+1] xor ... xor arr[Ri]）作为本次查询的结果。

并返回一个包含给定查询 queries 所有结果的数组。

 

示例 1：

输入：arr = [1,3,4,8], queries = [[0,1],[1,2],[0,3],[3,3]]
输出：[2,7,14,8] 
解释：
数组中元素的二进制表示形式是：
1 = 0001 
3 = 0011 
4 = 0100 
8 = 1000 
查询的 XOR 值为：
[0,1] = 1 xor 3 = 2 
[1,2] = 3 xor 4 = 7 
[0,3] = 1 xor 3 xor 4 xor 8 = 14 
[3,3] = 8
示例 2：

输入：arr = [4,8,2,10], queries = [[2,3],[1,3],[0,0],[0,3]]
输出：[8,0,4,4]
 

提示：

1 <= arr.length <= 3 * 10^4
1 <= arr[i] <= 10^9
1 <= queries.length <= 3 * 10^4
queries[i].length == 2
0 <= queries[i][0] <= queries[i][1] < arr.length
'''



class Solution(object):
    def xorQueries(self, arr, queries):
        """
        :type arr: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        xors = [0]
        for i in range(len(arr)):
            xors.append(xors[-1] ^ arr[i])

        res = []
        for l, r in queries:
            res.append(xors[l]^xors[r+1])

        return res

      
 # solutions
 
 '''
 方法一：前缀异或
朴素的想法是，对每个查询，计算数组中的对应下标范围内的元素的异或结果。每个查询的计算时间取决于查询对应的下标范围的长度。如果数组 \textit{arr}arr 的长度为 nn，数组 \textit{queries}queries 的长度为 mm（即有 mm 个查询），则最坏情况下每个查询都需要 O(n)O(n) 的时间计算结果，总时间复杂度是 O(nm)O(nm)，会超出时间限制，因此必须优化。

由于有 mm 个查询，对于每个查询都要计算结果，因此应该优化每个查询的计算时间。理想情况下，每个查询的计算时间应该为 O(1)O(1)。为了将每个查询的计算时间从 O(n)O(n) 优化到 O(1)O(1)，需要计算数组的前缀异或。

定义长度为 n+1n+1 的数组 \textit{xors}xors。令 \textit{xors}[0]=0xors[0]=0，对于 0 \le i<n0≤i<n，\textit{xors}[i+1]=\textit{xors}[i] \oplus \textit{arr}[i]xors[i+1]=xors[i]⊕arr[i]，其中 \oplus⊕ 是异或运算符。当 1 \le i \le n1≤i≤n 时，\textit{xors}[i]xors[i] 为从 \textit{arr}[0]arr[0] 到 \textit{arr}[i-1]arr[i−1] 的元素的异或运算结果：

\textit{xors}[i]=\textit{arr}[0] \oplus \ldots \oplus \textit{arr}[i-1]
xors[i]=arr[0]⊕…⊕arr[i−1]

对于查询 [\textit{left},\textit{right}](\textit{left} \le \textit{right})[left,right](left≤right)，用 Q(\textit{left},\textit{right})Q(left,right) 表示该查询的结果。

当 \textit{left}=0left=0 时，Q(\textit{left},\textit{right})=\textit{xors}[\textit{right}+1]Q(left,right)=xors[right+1]。

当 \textit{left}>0left>0 时，Q(\textit{left},\textit{right})Q(left,right) 的计算如下：

\begin{aligned} & \quad ~ Q(\textit{left},\textit{right}) \\ &= \textit{arr}[\textit{left}] \oplus \ldots \oplus \textit{arr}[\textit{right}] \\ &= (\textit{arr}[0] \oplus \ldots \oplus \textit{arr}[\textit{left}-1]) \oplus (\textit{arr}[0] \oplus \ldots \oplus \textit{arr}[\textit{left}-1]) \oplus (\textit{arr}[\textit{left}] \oplus \ldots \oplus \textit{arr}[\textit{right}]) \\ &= (\textit{arr}[0] \oplus \ldots \oplus \textit{arr}[\textit{left}-1]) \oplus (\textit{arr}[0] \oplus \ldots \oplus \textit{arr}[\textit{right}]) \\ &= \textit{xors}[\textit{left}] \oplus \textit{xors}[\textit{right}+1] \end{aligned}
​	
  
 Q(left,right)
=arr[left]⊕…⊕arr[right]
=(arr[0]⊕…⊕arr[left−1])⊕(arr[0]⊕…⊕arr[left−1])⊕(arr[left]⊕…⊕arr[right])
=(arr[0]⊕…⊕arr[left−1])⊕(arr[0]⊕…⊕arr[right])
=xors[left]⊕xors[right+1]
​	
 

上述计算用到了异或运算的结合律，以及异或运算的性质 x \oplus x=0x⊕x=0。

当 \textit{left}=0left=0 时，\textit{xors}[\textit{left}]=0xors[left]=0，因此 Q(\textit{left},\textit{right})=\textit{xors}[\textit{left}] \oplus \textit{xors}[\textit{right}+1]Q(left,right)=xors[left]⊕xors[right+1] 也成立。

因此对任意 0 \le \textit{left} \le \textit{right}<n0≤left≤right<n，都有 Q(\textit{left},\textit{right})=\textit{xors}[\textit{left}] \oplus \textit{xors}[\textit{right}+1]Q(left,right)=xors[left]⊕xors[right+1]，即可在 O(1)O(1) 的时间内完成一个查询的计算。

根据上述分析，这道题可以分两步求解。

计算前缀异或数组 \textit{xors}xors；

计算每个查询的结果，第 ii 个查询的结果为 \textit{xors}[\textit{queries}[i][0]] \oplus \textit{xors}[\textit{queries}[i][1]+1]xors[queries[i][0]]⊕xors[queries[i][1]+1]。

JavaC#JavaScriptGolangC++CPython3

func xorQueries(arr []int, queries [][]int) []int {
    xors := make([]int, len(arr)+1)
    for i, v := range arr {
        xors[i+1] = xors[i] ^ v
    }
    ans := make([]int, len(queries))
    for i, q := range queries {
        ans[i] = xors[q[0]] ^ xors[q[1]+1]
    }
    return ans
}
复杂度分析

时间复杂度：O(n+m)O(n+m)，其中 nn 是数组 \textit{arr}arr 的长度，mm 是数组 \textit{queries}queries 的长度。需要遍历数组 \textit{arr}arr 一次，计算前缀异或数组的每个元素值，然后对每个查询分别使用 O(1)O(1) 的时间计算查询结果。

空间复杂度：O(n)O(n)，其中 nn 是数组 \textit{arr}arr 的长度。需要创建长度为 n+1n+1 的前缀异或数组，注意返回值不计入空间复杂度。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/xor-queries-of-a-subarray/solution/zi-shu-zu-yi-huo-cha-xun-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
 '''
