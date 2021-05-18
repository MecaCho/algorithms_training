'''
5405. 形成两个异或相等数组的三元组数目
给你一个整数数组 arr 。

现需要从数组中取三个下标 i、j 和 k ，其中 (0 <= i < j <= k < arr.length) 。

a 和 b 定义如下：

a = arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1]
b = arr[j] ^ arr[j + 1] ^ ... ^ arr[k]
注意：^ 表示 按位异或 操作。

请返回能够令 a == b 成立的三元组 (i, j , k) 的数目。



示例 1：

输入：arr = [2,3,1,6,7]
输出：4
解释：满足题意的三元组分别是 (0,1,2), (0,2,2), (2,3,4) 以及 (2,4,4)
示例 2：

输入：arr = [1,1,1,1,1]
输出：10
示例 3：

输入：arr = [2,3]
输出：0
示例 4：

输入：arr = [1,3,5,7,9]
输出：3
示例 5：

输入：arr = [7,11,12,9,5,2,7,17,22]
输出：8


提示：

1 <= arr.length <= 300
1 <= arr[i] <= 10^8

5405. Count Triplets That Can Form Two Arrays of Equal XOR
Given an array of integers arr.

We want to select three indices i, j and k where (0 <= i < j <= k < arr.length).

Let's define a and b as follows:

a = arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1]
b = arr[j] ^ arr[j + 1] ^ ... ^ arr[k]
Note that ^ denotes the bitwise-xor operation.

Return the number of triplets (i, j and k) Where a == b.



Example 1:

Input: arr = [2,3,1,6,7]
Output: 4
Explanation: The triplets are (0,1,2), (0,2,2), (2,3,4) and (2,4,4)
Example 2:

Input: arr = [1,1,1,1,1]
Output: 10
Example 3:

Input: arr = [2,3]
Output: 0
Example 4:

Input: arr = [1,3,5,7,9]
Output: 3
Example 5:

Input: arr = [7,11,12,9,5,2,7,17,22]
Output: 8


Constraints:

1 <= arr.length <= 300
1 <= arr[i] <= 10^8
'''


class Solution(object):
    def countTriplets(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        xors = [0]
        for i in range(len(arr)):
            xors.append(xors[i ] ^arr[i])

        count = 0
        for i in range(len(arr)):
            for j in range( i +1, len(arr)):
                k = j
                while k < len(arr):
                    if xors[i] ^ xors[j] == xors[j] ^ xors[ k +1]:
                        count += 1
                    k += 1
        return count



class Solution0(object):
    def countTriplets(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        xors = []
        tmp = 0
        for i in range(len(arr)):
            tmp ^= arr[i]
            xors.append(tmp)
        xors.append(0)

        count = 0
        for i in range(len(arr)):
            for j in range( i +1, len(arr)):
                k = j
                while k < len(arr):
                    if xors[ i -1] ^ xors[ j -1] == xors[ j -1] ^ xors[k]:
                        # print(i, j, k)
                        count += 1
                    k += 1
        return count
    
# solutions

class Solution20210518(object):
    def countTriplets(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        xors = [0]
        for ar in arr:
            xors.append(ar^xors[-1])

        res = 0
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                if xors[i] == xors[j+1]:
                    res += j-i

        return res



# tips
'''
We are searching for sub-array of length ≥ 2 and we need to split it to 2 non-empty arrays so that the xor of the first array is equal to the xor of the second array. This is equivalent to searching for sub-array with xor = 0.

Keep the prefix xor of arr in another array, check the xor of all sub-arrays in O(n^2), if the xor of sub-array of length x is 0 add x-1 to the answer.
'''

# solutions


'''
前言
用 \oplus⊕ 表示按位异或运算。

定义长度为 nn 的数组 \textit{arr}arr 的异或前缀和

S_i = \begin{cases} 0,&i=0\\ \textit{arr}_0\oplus\textit{arr}_1\oplus\cdots\oplus\textit{arr}_{i-1},&1\le i\le n \end{cases}

 

由该定义可得

S_i = \begin{cases} 0,&i=0\\ S_{i-1}\oplus\textit{arr}_{i-1},&1\le i\le n \end{cases}

  
i=0
1≤i≤n
​	
 

这是一个关于 S_iS 
i
​	
  的递推式，根据该递推式我们可以用 O(n)O(n) 的时间得到数组 \textit{arr}arr 的异或前缀和数组。

对于两个下标不同的异或前缀和 S_iS 
i
​	
  和 S_jS 
j
​	
 ，设 0<i<j0<i<j，有

S_i\oplus S_j=(\textit{arr}_0\oplus\textit{arr}_1\oplus\cdots\oplus\textit{arr}_{i-1})\oplus(\textit{arr}_0\oplus\textit{arr}_1\oplus\cdots\oplus\textit{arr}_{i-1}\oplus\textit{arr}_i\oplus\cdots\oplus\textit{arr}_{j-1}）


由于异或运算满足结合律和交换律，且任意数异或自身等于 00，上式可化简为

S_i\oplus S_j=\textit{arr}_i\oplus\cdots\oplus\textit{arr}_{j-1}

​	
 

从而，数组 \textit{arr}arr 的子区间 [i,j][i,j] 的元素异或和为可表示为

​	
 

因此问题中的 aa 和 bb 可表示为

\begin{aligned} &a=S_i\oplus S_{j}\\ &b=S_j\oplus S_{k+1} \end{aligned}
 

方法一：三重循环
计算数组 \textit{arr}arr 的异或前缀和 SS，枚举符合 0\le i<j\le k<n0≤i<j≤k<n 的下标 ii，jj 和 kk，统计满足等式 S_i=S_{k+1}S 
i
​	
 =S 
k+1
​	
  的三元组个数。

C++JavaC#GolangPython3JavaScriptC

func countTriplets(arr []int) (ans int) {
    n := len(arr)
    s := make([]int, n+1)
    for i, val := range arr {
        s[i+1] = s[i] ^ val
    }
    for i := 0; i < n; i++ {
        for j := i + 1; j < n; j++ {
            for k := j; k < n; k++ {
                if s[i] == s[k+1] {
                    ans++
                }
            }
        }
    }
    return
}
复杂度分析

时间复杂度：O(n^3)O(n 
3
 )，其中 nn 是数组 \textit{arr}arr 的长度。

空间复杂度：O(n)O(n)。

方法二：二重循环
当等式 S_i=S_{k+1}S 
i
​	
 =S 
k+1
​	
  成立时，[i+1, k][i+1,k] 的范围内的任意 jj 都是符合要求的，对应的三元组个数为 k-ik−i。因此我们只需枚举下标 ii 和 kk。

代码

C++JavaC#GolangPython3JavaScriptC

func countTriplets(arr []int) (ans int) {
    n := len(arr)
    s := make([]int, n+1)
    for i, val := range arr {
        s[i+1] = s[i] ^ val
    }
    for i := 0; i < n; i++ {
        for k := i + 1; k < n; k++ {
            if s[i] == s[k+1] {
                ans += k - i
            }
        }
    }
    return
}
复杂度分析

时间复杂度：O(n^2)O(n 
2
 )，其中 nn 是数组 \textit{arr}arr 的长度。

空间复杂度：O(n)O(n)。

方法三：哈希表（一重循环）
对于下标 kk，若下标 i=i_1,i_2,\cdots,i_mi=i 

  时均满足 S_i=S_{k+1}S 
i
​	
 =S 
k+1
​	
 ，根据方法二，这些二元组 (i_1,k),(i_2,k),\cdots,(i_m,k)(i 
1
​	
 ,k),(i 
2
​	
 ,k),⋯,(i 
m
​	
 ,k) 对答案的贡献之和为

(k-i_1)+(k-i_2)+\cdots+(k-i_m)=m\cdot k-(i_1+i_2+\cdots+i_m)


也就是说，当遍历下标 kk 时，我们需要知道所有满足 S_i=S_{k+1}S 
i
​	
 =S 
k+1
​	
  的

下标 ii 的出现次数 mm
下标 ii 之和
这可以借助两个哈希表来做到，在遍历下标 kk 的同时，一个哈希表统计 S_kS 
k
​	
  的出现次数，另一个哈希表统计值为 S_kS 
k
​	
  的下标之和。

C++JavaC#GolangPython3JavaScriptC

func countTriplets(arr []int) (ans int) {
    n := len(arr)
    s := make([]int, n+1)
    for i, v := range arr {
        s[i+1] = s[i] ^ v
    }
    cnt := map[int]int{}
    total := map[int]int{}
    for k := 0; k < n; k++ {
        if m, has := cnt[s[k+1]]; has {
            ans += m*k - total[s[k+1]]
        }
        cnt[s[k]]++
        total[s[k]] += k
    }
    return
}
优化

我们可以在计算异或前缀和的同时计算答案，从而做到仅遍历 \textit{arr}arr 一次就计算出答案。

C++JavaC#GolangPython3JavaScriptC

func countTriplets(arr []int) (ans int) {
    cnt := map[int]int{}
    total := map[int]int{}
    s := 0
    for k, val := range arr {
        if m, has := cnt[s^val]; has {
            ans += m*k - total[s^val]
        }
        cnt[s]++
        total[s] += k
        s ^= val
    }
    return
}
复杂度分析

时间复杂度：O(n)O(n)，其中 nn 是数组 \textit{arr}arr 的长度。

空间复杂度：O(n)O(n)。我们需要使用 O(n)O(n) 的空间存储两个哈希表。

'''
