'''
1122. Relative Sort Array
Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.

Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2.  Elements that don't appear in arr2 should be placed at the end of arr1 in ascending order.



Example 1:

Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
Output: [2,2,2,1,4,3,3,9,6,7,19]


Constraints:

arr1.length, arr2.length <= 1000
0 <= arr1[i], arr2[i] <= 1000
Each arr2[i] is distinct.
Each arr2[i] is in arr1.

1122. 数组的相对排序
给你两个数组，arr1 和 arr2，

arr2 中的元素各不相同
arr2 中的每个元素都出现在 arr1 中
对 arr1 中的元素进行排序，使 arr1 中项的相对顺序和 arr2 中的相对顺序相同。未在 arr2 中出现过的元素需要按照升序放在 arr1 的末尾。



示例：

输入：arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
输出：[2,2,2,1,4,3,3,9,6,7,19]


提示：

arr1.length, arr2.length <= 1000
0 <= arr1[i], arr2[i] <= 1000
arr2 中的元素 arr2[i] 各不相同
arr2 中的每个元素 arr2[i] 都出现在 arr1 中
'''


class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        return sorted(arr1, key=(arr2+sorted(set(arr1) - set(arr2))).index)


# solution

'''
方法一：自定义排序
一种容易想到的方法是使用排序并自定义比较函数。

由于数组 \textit{arr}_2arr 
2
​	
  规定了比较顺序，因此我们可以使用哈希表对该顺序进行映射：即对于数组 \textit{arr}_2arr 
2
​	
  中的第 ii 个元素，我们将 (\textit{arr}_2[i], i)(arr 
2
​	
 [i],i) 这一键值对放入哈希表 \textit{rank}rank 中，就可以很方便地对数组 \textit{arr}_1arr 
1
​	
  中的元素进行比较。

比较函数的写法有很多种，例如我们可以使用最基础的比较方法，对于元素 xx 和 yy：

如果 xx 和 yy 都出现在哈希表中，那么比较它们对应的值 \textit{rank}[x]rank[x] 和 \textit{rank}[y]rank[y]；

如果 xx 和 yy 都没有出现在哈希表中，那么比较它们本身；

对于剩余的情况，出现在哈希表中的那个元素较小。

C++GolangC

func relativeSortArray(arr1 []int, arr2 []int) []int {
    rank := map[int]int{}
    for i, v := range arr2 {
        rank[v] = i
    }
    sort.Slice(arr1, func(i, j int) bool {
        x, y := arr1[i], arr1[j]
        rankX, hasX := rank[x]
        rankY, hasY := rank[y]
        if hasX && hasY {
            return rankX < rankY
        }
        if hasX || hasY {
            return hasX
        }
        return x < y
    })
    return arr1
}
很多语言支持对「元组」进行排序，即依次比较元组中每一个对应位置的元素，直到比较出大小关系为止。因此，对于元素 xx，如果它出现在哈希表中，我们使用二元组 (0, \textit{rank}[x])(0,rank[x])；如果它没有出现在哈希表中，我们使用二元组 (1, x)(1,x)，就可以得到正确的排序结果。

C++Python3

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        def mycmp(x: int) -> (int, int):
            return (0, rank[x]) if x in rank else (1, x)
        
        rank = {x: i for i, x in enumerate(arr2)}
        arr1.sort(key=mycmp)
        return arr1
此外，由于题目中给定的元素都是正数，因此我们可以用 \textit{rank}[x]-nrank[x]−n 和 xx 分别代替 (0, \textit{rank}[x])(0,rank[x]) 和 (1, x)(1,x)，其中 nn 是数组 \textit{arr}_2arr 
2
​	
  的长度（同时也是哈希表 \textit{rank}rank 的大小）。这样做的正确性在于，\textit{rank}[x]-nrank[x]−n 一定是负数，而 xx 一定是正数。

C++Python3GolangC

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        def mycmp(x: int) -> (int, int):
            return rank[x] if x in rank else x
        
        n = len(arr2)
        rank = {x: i - n for i, x in enumerate(arr2)}
        arr1.sort(key=mycmp)
        return arr1
复杂度分析

时间复杂度：O(m \log m + n)O(mlogm+n)，其中 mm 和 nn 分别是数组 \textit{arr}_1arr 
1
​	
  和 \textit{arr}_2arr 
2
​	
  的长度。构造哈希表 \textit{rank}rank 的时间复杂度为 O(n)O(n)，排序的时间复杂度为 O(m \log m)O(mlogm)。

空间复杂度：O(\log m + n)O(logm+n)，哈希表 \textit{rank}rank 需要的空间为 O(n)O(n)，排序需要的栈空间为 O(\log m)O(logm)。

方法二：计数排序
思路与算法

注意到本题中元素的范围为 [0, 1000][0,1000]，这个范围不是很大，我们也可以考虑不基于比较的排序，例如「计数排序」。

具体地，我们使用一个长度为 10011001（下标从 00 到 10001000）的数组 \textit{frequency}frequency，记录每一个元素在数组 \textit{arr}_1arr 
1
​	
  中出现的次数。随后我们遍历数组 \textit{arr}_2arr 
2
​	
 ，当遍历到元素 xx 时，我们将 \textit{frequency}[x]frequency[x] 个 xx 加入答案中，并将 \textit{frequency}[x]frequency[x] 清零。当遍历结束后，所有在 \textit{arr}_2arr 
2
​	
  中出现过的元素就已经有序了。

此时还剩下没有在 \textit{arr}_2arr 
2
​	
  中出现过的元素，因此我们还需要对整个数组 \textit{frequency}frequency 进行一次遍历。当遍历到元素 xx 时，如果 \textit{frequency}[x]frequency[x] 不为 00，我们就将 \textit{frequency}[x]frequency[x] 个 xx 加入答案中。

细节

我们可以对空间复杂度进行一个小优化。实际上，我们不需要使用长度为 10011001 的数组，而是可以找出数组 \textit{arr}_1arr 
1
​	
  中的最大值 \textit{upper}upper，使用长度为 \textit{upper}+1upper+1 的数组即可。

代码

C++JavaPython3GolangC

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        upper = max(arr1)
        frequency = [0] * (upper + 1)
        for x in arr1:
            frequency[x] += 1
        
        ans = list()
        for x in arr2:
            ans.extend([x] * frequency[x])
            frequency[x] = 0
        for x in range(upper + 1):
            if frequency[x] > 0:
                ans.extend([x] * frequency[x])
        return ans
复杂度分析

时间复杂度：O(m + n + \textit{upper})O(m+n+upper)，其中 mm 和 nn 分别是数组 \textit{arr}_1arr 
1
​	
  和 \textit{arr}_2arr 
2
​	
  的长度，\textit{upper}upper 是数组 \textit{arr}_1arr 
1
​	
  中的最大值，在本题中 \textit{upper}upper 不会超过 10001000。遍历数组 \textit{arr}_2arr 
2
​	
  的时间复杂度为 O(n)O(n)，遍历数组 \textit{frequency}frequency 的时间复杂度为 O(\textit{upper})O(upper)，而在遍历的过程中，我们一共需要 O(m)O(m) 的时间得到答案数组。

空间复杂度：O(\textit{upper})O(upper)，即为数组 \textit{frequency}frequency 需要使用的空间。注意到与方法一不同的是，方法二的代码使用了额外的空间（而不是直接覆盖数组 \textit{arr}_1arr 
1
​	
 ）存放答案，但我们一般不将存储返回答案的数组计入空间复杂度，并且在我们得到数组 \textit{frequency}frequency 之后，实际上也是可以将返回答案覆盖在数组 \textit{arr}_1arr 
1
​	
  上的。如果在面试中遇到了本题，这些细节都可以和面试官进行确认。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/relative-sort-array/solution/shu-zu-de-xiang-dui-pai-xu-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''