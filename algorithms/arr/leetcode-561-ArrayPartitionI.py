# encoding=utf8


'''
561. Array Partition I
Given an integer array nums of 2n integers, group these integers into n pairs (a1, b1), (a2, b2), ..., (an, bn) such that the sum of min(ai, bi) for all i is maximized. Return the maximized sum.



Example 1:

Input: nums = [1,4,3,2]
Output: 4
Explanation: All possible pairings (ignoring the ordering of elements) are:
1. (1, 4), (2, 3) -> min(1, 4) + min(2, 3) = 1 + 2 = 3
2. (1, 3), (2, 4) -> min(1, 3) + min(2, 4) = 1 + 2 = 3
3. (1, 2), (3, 4) -> min(1, 2) + min(3, 4) = 1 + 3 = 4
So the maximum possible sum is 4.
Example 2:

Input: nums = [6,2,6,5,1,2]
Output: 9
Explanation: The optimal pairing is (2, 1), (2, 5), (6, 6). min(2, 1) + min(2, 5) + min(6, 6) = 1 + 2 + 6 = 9.


Constraints:

1 <= n <= 104
nums.length == 2 * n
-104 <= nums[i] <= 104


561. 数组拆分 I
给定长度为 2n 的整数数组 nums ，你的任务是将这些数分成 n 对, 例如 (a1, b1), (a2, b2), ..., (an, bn) ，使得从 1 到 n 的 min(ai, bi) 总和最大。

返回该 最大总和 。



示例 1：

输入：nums = [1,4,3,2]
输出：4
解释：所有可能的分法（忽略元素顺序）为：
1. (1, 4), (2, 3) -> min(1, 4) + min(2, 3) = 1 + 2 = 3
2. (1, 3), (2, 4) -> min(1, 3) + min(2, 4) = 1 + 2 = 3
3. (1, 2), (3, 4) -> min(1, 2) + min(3, 4) = 1 + 3 = 4
所以最大总和为 4
示例 2：

输入：nums = [6,2,6,5,1,2]
输出：9
解释：最优的分法为 (2, 1), (2, 5), (6, 6). min(2, 1) + min(2, 5) + min(6, 6) = 1 + 2 + 6 = 9


提示：

1 <= n <= 104
nums.length == 2 * n
-104 <= nums[i] <= 104
'''


class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(sorted(nums)[::2])



# solutions

'''
方法一：排序
思路与算法

不失一般性，我们令每一组 (a_i, b_i)(a 
i
​	
 ,b 
i
​	
 ) 满足 a_i \leq b_ia 
i
​	
 ≤b 
i
​	
 （若不满足，交换二者即可），这样我们需要求得的总和

\sum_{i=1}^n \min(a_i, b_i)
i=1
∑
n
​	
 min(a 
i
​	
 ,b 
i
​	
 )

就等于所有 a_ia 
i
​	
  的和

\sum_{i=1}^n a_i \tag{1}
i=1
∑
n
​	
 a 
i
​	
 (1)

接下来，我们将所有的 (a_i, b_i)(a 
i
​	
 ,b 
i
​	
 ) 按照升序排序，使得 a_1 \leq a_2 \leq \cdots \leq a_na 
1
​	
 ≤a 
2
​	
 ≤⋯≤a 
n
​	
 。这样一来，对于任意的 a_ja 
j
​	
 

它不大于 a_{j+1}, a_{j+2}, \cdots, a_na 
j+1
​	
 ,a 
j+2
​	
 ,⋯,a 
n
​	
 ；

它不大于 b_jb 
j
​	
 ；

由于 a_i \leq b_ia 
i
​	
 ≤b 
i
​	
  对于任意的 ii 恒成立，因此它不大于 b_{j+1}, b_{j+2}, \cdots, b_nb 
j+1
​	
 ,b 
j+2
​	
 ,⋯,b 
n
​	
 。

由于 a_ja 
j
​	
  不大于 \{a\}{a} 中的 n-jn−j 个元素，也不大于 \{b\}{b} 中的 n-j+1n−j+1 个元素，而这些元素都是从 \textit{nums}nums 中而来的，因此 a_ja 
j
​	
  在数组 \textit{nums}nums 中「从大到小」至少排在第 (n-j) + (n-j+1) + 1 = 2(n-j+1)(n−j)+(n−j+1)+1=2(n−j+1) 个位置，也就是「从小到大」至多排在第 2n - 2(n-j+1) + 1 = 2(j-1) + 12n−2(n−j+1)+1=2(j−1)+1 个位置，这里位置的编号从 11 开始，即

a_j \leq c_{2(j-1)+1}
a 
j
​	
 ≤c 
2(j−1)+1
​	
 

其中数组 cc 是将数组 \textit{nums}nums 升序排序得到的结果，代入 (1)(1) 式即可得到

\sum_{i=1}^n a_i \leq \sum_{i=1}^n c_{2(i-1)+1} \tag{2}
i=1
∑
n
​	
 a 
i
​	
 ≤ 
i=1
∑
n
​	
 c 
2(i−1)+1
​	
 (2)

另一方面，令 (a_1, b_1) = (c_1, c_2), (a_2, b_2) = (c_3, c_4), \cdots, (a_n, b_n) = (c_{2n-1}, c_{2n})(a 
1
​	
 ,b 
1
​	
 )=(c 
1
​	
 ,c 
2
​	
 ),(a 
2
​	
 ,b 
2
​	
 )=(c 
3
​	
 ,c 
4
​	
 ),⋯,(a 
n
​	
 ,b 
n
​	
 )=(c 
2n−1
​	
 ,c 
2n
​	
 )，此时每一组 (a_i, b_i)(a 
i
​	
 ,b 
i
​	
 ) 都满足 a_i \leq b_ia 
i
​	
 ≤b 
i
​	
  的要求，并且有 a_1 \leq a_2 \leq \cdots \leq a_na 
1
​	
 ≤a 
2
​	
 ≤⋯≤a 
n
​	
 ，此时

\sum_{i=1}^n a_i = \sum_{i=1}^n c_{2(i-1)+1}
i=1
∑
n
​	
 a 
i
​	
 = 
i=1
∑
n
​	
 c 
2(i−1)+1
​	
 

即 (2)(2) 式的等号是可满足的。因此所要求得的最大总和即为

\sum_{i=1}^n c_{2(i-1)+1}
i=1
∑
n
​	
 c 
2(i−1)+1
​	
 

代码

需要注意大部分语言的数组编号是从 00（而不是上文中的 11）开始的。

C++JavaPython3JavaScriptGolangC

func arrayPairSum(nums []int) (ans int) {
    sort.Ints(nums)
    for i := 0; i < len(nums); i += 2 {
        ans += nums[i]
    }
    return
}
复杂度分析

时间复杂度：O(n\log n)O(nlogn)，即为对数组 \textit{nums}nums 进行排序的时间复杂度。

空间复杂度：O(\log n)O(logn)，即为排序需要使用的栈空间。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/array-partition-i/solution/shu-zu-chai-fen-i-by-leetcode-solution-9m9y/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
