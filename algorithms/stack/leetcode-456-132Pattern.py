# encoding=utf8


'''
456. 132 Pattern
Given an array of n integers nums, a 132 pattern is a subsequence of three integers nums[i], nums[j] and nums[k] such that i < j < k and nums[i] < nums[k] < nums[j].

Return true if there is a 132 pattern in nums, otherwise, return false.

Follow up: The O(n^2) is trivial, could you come up with the O(n logn) or the O(n) solution?



Example 1:

Input: nums = [1,2,3,4]
Output: false
Explanation: There is no 132 pattern in the sequence.
Example 2:

Input: nums = [3,1,4,2]
Output: true
Explanation: There is a 132 pattern in the sequence: [1, 4, 2].
Example 3:

Input: nums = [-1,3,2,0]
Output: true
Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].


Constraints:

n == nums.length
1 <= n <= 104
-109 <= nums[i] <= 109



456. 132模式
给你一个整数数组 nums ，数组中共有 n 个整数。132 模式的子序列 由三个整数 nums[i]、nums[j] 和 nums[k] 组成，并同时满足：i < j < k 和 nums[i] < nums[k] < nums[j] 。

如果 nums 中存在 132 模式的子序列 ，返回 true ；否则，返回 false 。



进阶：很容易想到时间复杂度为 O(n^2) 的解决方案，你可以设计一个时间复杂度为 O(n logn) 或 O(n) 的解决方案吗？



示例 1：

输入：nums = [1,2,3,4]
输出：false
解释：序列中不存在 132 模式的子序列。
示例 2：

输入：nums = [3,1,4,2]
输出：true
解释：序列中有 1 个 132 模式的子序列： [1, 4, 2] 。
示例 3：

输入：nums = [-1,3,2,0]
输出：true
解释：序列中有 3 个 132 模式的的子序列：[-1, 3, 2]、[-1, 3, 0] 和 [-1, 2, 0] 。


提示：

n == nums.length
1 <= n <= 104
-109 <= nums[i] <= 109
'''


class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        length = len(nums)
        mins = [nums[0]]
        for i in range(1, length):
            mins.append(min(nums[i], mins[-1]))

        stack = []
        for i in range(length-1, -1, -1):
            if nums[i] > mins[i]:
                while stack and stack[-1] <= mins[i]:
                    stack.pop()
                if stack and mins[i] < stack[-1] < nums[i]:
                    return True
                stack.append(nums[i])

        return False


# solutions


'''
前言
由于本题中 nn 的最大值可以到 1500015000，因此对于一个满足 132132 模式的三元组下标 (i, j, k)(i,j,k)，枚举其中的 22 个下标时间复杂度为 O(n^2)O(n 
2
 )，很容易超出时间限制。

因此我们可以考虑枚举其中的 11 个下标，并使用合适的数据结构维护另外的 22 个下标的可能值。

方法一：枚举 33
思路与算法

枚举 33 是容易想到并且也是最容易实现的。由于 33 是模式中的最大值，并且其出现在 11 和 22 的中间，因此我们只需要从左到右枚举 33 的下标 jj，那么：

由于 11 是模式中的最小值，因此我们在枚举 jj 的同时，维护数组 aa 中左侧元素 a[0..j-1]a[0..j−1] 的最小值，即为 11 对应的元素 a[i]a[i]。需要注意的是，只有 a[i] < a[j]a[i]<a[j] 时，a[i]a[i] 才能作为 11 对应的元素；

由于 22 是模式中的次小值，因此我们可以使用一个有序集合（例如平衡树）维护数组 aa 中右侧元素 a[j+1..n-1]a[j+1..n−1] 中的所有值。当我们确定了 a[i]a[i] 和 a[j]a[j] 之后，只需要在有序集合中查询严格比 a[i]a[i] 大的那个最小的元素，即为 a[k]a[k]。需要注意的是，只有 a[k] < a[j]a[k]<a[j] 时，a[k]a[k] 才能作为 33 对应的元素。

代码

下面的 \texttt{Python}Python 代码需要手动导入 \texttt{sortedcontainers}sortedcontainers 库。

C++JavaPython3Golang

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False
        
        # 左侧最小值
        left_min = nums[0]
        # 右侧所有元素
        right_all = SortedList(nums[2:])
        
        for j in range(1, n - 1):
            if left_min < nums[j]:
                index = right_all.bisect_right(left_min)
                if index < len(right_all) and right_all[index] < nums[j]:
                    return True
            left_min = min(left_min, nums[j])
            right_all.remove(nums[j + 1])

        return False
复杂度分析

时间复杂度：O(n \log n)O(nlogn)。在初始化时，我们需要 O(n \log n)O(nlogn) 的时间将数组元素 a[2..n-1]a[2..n−1] 加入有序集合中。在枚举 jj 时，维护左侧元素最小值的时间复杂度为 O(1)O(1)，将 a[j+1]a[j+1] 从有序集合中删除的时间复杂度为 O(\log n)O(logn)，总共需要枚举的次数为 O(n)O(n)，因此总时间复杂度为 O(n \log n)O(nlogn)。

空间复杂度：O(n)O(n)，即为有序集合存储右侧所有元素需要使用的空间。

方法二：枚举 11
思路与算法

如果我们从左到右枚举 11 的下标 ii，那么 j, kj,k 的下标范围都是减少的，这样就不利于对它们进行维护。因此我们可以考虑从右到左枚举 ii。

那么我们应该如何维护 j, kj,k 呢？在 132132 模式中，如果 1<21<2 并且 2<32<3，那么根据传递性，1<31<3 也是成立的，那么我们可以使用下面的方法进行维护：

我们使用一种数据结构维护所有遍历过的元素，它们作为 22 的候选元素。每当我们遍历到一个新的元素时，就将其加入数据结构中；

在遍历到一个新的元素的同时，我们可以考虑其是否可以作为 33。如果它作为 33，那么数据结构中所有严格小于它的元素都可以作为 22，我们将这些元素全部从数据结构中移除，并且使用一个变量维护所有被移除的元素的最大值。这些被移除的元素都是可以真正作为 22 的，并且元素的值越大，那么我们之后找到 11 的机会也就越大。

那么这个「数据结构」是什么样的数据结构呢？我们尝试提取出它进行的操作：

它需要支持添加一个元素；

它需要支持移除所有严格小于给定阈值的所有元素；

上面两步操作是「依次进行」的，即我们先用给定的阈值移除元素，再将该阈值加入数据结构中。

这就是「单调栈」。在单调栈中，从栈底到栈顶的元素是严格单调递减的。当给定阈值 xx 时，我们只需要不断地弹出栈顶的元素，直到栈为空或者 xx 严格小于栈顶元素。此时我们再将 xx 入栈，这样就维护了栈的单调性。

因此，我们可以使用单调栈作为维护 22 的数据结构，并给出下面的算法：

我们用单调栈维护所有可以作为 22 的候选元素。初始时，单调栈中只有唯一的元素 \textit{a}[n-1]a[n−1]。我们还需要使用一个变量 \textit{max\_k}max_k 记录所有可以真正作为 22 的元素的最大值；

随后我们从 n-2n−2 开始从右到左枚举元素 a[i]a[i]：

首先我们判断 a[i]a[i] 是否可以作为 11。如果 a[i] < \textit{max\_k}a[i]<max_k，那么它就可以作为 11，我们就找到了一组满足 132132 模式的三元组；

随后我们判断 a[i]a[i] 是否可以作为 33，以此找出哪些可以真正作为 22 的元素。我们将 a[i]a[i] 不断地与单调栈栈顶的元素进行比较，如果 a[i]a[i] 较大，那么栈顶元素可以真正作为 22，将其弹出并更新 \textit{max\_k}max_k；

最后我们将 a[i]a[i] 作为 22 的候选元素放入单调栈中。这里可以进行一个优化，即如果 a[i] \leq \textit{max\_k}a[i]≤max_k，那么我们也没有必要将 a[i]a[i] 放入栈中，因为即使它在未来被弹出，也不会将 \textit{max\_k}max_k 更新为更大的值。

在枚举完所有的元素后，如果仍未找到满足 132132 模式的三元组，那就说明其不存在。

代码

C++JavaPython3JavaScriptGolangC

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        candidate_k = [nums[n - 1]]
        max_k = float("-inf")

        for i in range(n - 2, -1, -1):
            if nums[i] < max_k:
                return True
            while candidate_k and nums[i] > candidate_k[-1]:
                max_k = candidate_k[-1]
                candidate_k.pop()
            if nums[i] > max_k:
                candidate_k.append(nums[i])

        return False
复杂度分析

时间复杂度：O(n)O(n)，枚举 ii 的次数为 O(n)O(n)，由于每一个元素最多被加入和弹出单调栈各一次，因此操作单调栈的时间复杂度一共为 O(n)O(n)，总时间复杂度为 O(n)O(n)。

空间复杂度：O(n)O(n)，即为单调栈需要使用的空间。

方法三：枚举 22
说明

方法三思路难度较大，需要在单调栈上进行二分查找。建议读者在完全理解方法二之后，再尝试阅读该方法。

思路与算法

当我们枚举 22 的下标 kk 时，与方法二相反，从左到右进行枚举的方法是十分合理的：在枚举的过程中，i, ji,j 的下标范围都是增加的。

由于我们需要保证 1<21<2 并且 2<32<3，那么我们需要维护一系列尽可能小的元素作为 11 的候选元素，并且维护一系列尽可能大的元素作为 33 的候选元素。

我们可以分情况进行讨论，假设当前有一个小元素 x_ix 
i
​	
  以及一个大元素 x_jx 
j
​	
  表示一个二元组，而我们当前遍历到了一个新的元素 x=a[k]x=a[k]，那么：

如果 x > x_jx>x 
j
​	
 ，那么让 xx 作为 33 显然是比 x_jx 
j
​	
  作为 33 更优，因此我们可以用 xx 替代 x_jx 
j
​	
 ；

如果 x < x_ix<x 
i
​	
 ，那么让 xx 作为 11 显然是比 x_ix 
i
​	
  作为 33 更优，然而我们必须要满足 132132 模式中的顺序，即 11 出现在 33 之前，这里如果我们简单地用 xx 替代 x_ix 
i
​	
 ，那么 x_i=xx 
i
​	
 =x 作为 11 是出现在 x_jx 
j
​	
  作为 33 之后的，这并不满足要求。因此我们需要为 xx 找一个新的元素作为 33。由于我们还没有遍历到后面的元素，因此可以简单地将 xx 同时看作一个二元组的 x_ix 
i
​	
  和 x_jx 
j
​	
 ；

对于其它的情况，x_i \leq x \leq x_jx 
i
​	
 ≤x≤x 
j
​	
 ，xx 无论作为 11 还是 33 都没有当前二元组对应的要优，因此我们可以不用考虑 xx 作为 11 或者 33 的情况。

这样一来，与方法二类似，我们使用两个单调递减的单调栈维护一系列二元组 (x_i, x_j)(x 
i
​	
 ,x 
j
​	
 )，表示一个可以选择的 1-31−3 区间，并且从栈底到栈顶 x_ix 
i
​	
  和 x_jx 
j
​	
  分别严格单调递减，因为根据上面的讨论，我们只有在 x < x_ix<x 
i
​	
  时才会增加一个新的二元组。

然而与方法二不同的是，如果我们想让 xx 作为 22，那么我们并不知道到底应该选择单调栈中的哪个 1-31−3 区间，因此我们只能根据单调性进行二分查找：

对于单调栈中的 x_ix 
i
​	
 ，我们需要找出第一个满足 x_i < xx 
i
​	
 <x 的位置 \textit{idx}_iidx 
i
​	
 ，这样从该位置到栈顶的所有二元组都满足 x_i < xx 
i
​	
 <x；

对于单调栈中的 x_jx 
j
​	
 ，我们需要找出最后一个满足 x_j > xx 
j
​	
 >x 的位置 \textit{idx}_jidx 
j
​	
 ，这样从栈底到该位置的所有二元组都满足 x_j > xx 
j
​	
 >x；

如果 \textit{idx}_iidx 
i
​	
  和 \textit{idx}_jidx 
j
​	
  都存在，并且 \textit{idx}_i \leq \textit{idx}_jidx 
i
​	
 ≤idx 
j
​	
 ，那么就存在至少一个二元组 (x_i, x_j)(x 
i
​	
 ,x 
j
​	
 ) 满足 x_i < x < x_jx 
i
​	
 <x<x 
j
​	
 ，xx 就可以作为 22，我们就找到了一组满足 132132 模式的三元组。

在枚举完所有的元素后，如果仍未找到满足 132132 模式的三元组，那就说明其不存在。

代码

需要注意的是，我们是在单调递减的栈上进行二分查找，因此大部分语言都需要实现一个自定义比较函数，或者将栈中的元素取相反数后再使用默认的比较函数。

C++JavaPython3JavaScriptGolangC

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        candidate_i, candidate_j = [-nums[0]], [-nums[0]]

        for v in nums[1:]:
            idx_i = bisect.bisect_right(candidate_i, -v)
            idx_j = bisect.bisect_left(candidate_j, -v)
            if idx_i < idx_j:
                return True

            if v < -candidate_i[-1]:
                candidate_i.append(-v)
                candidate_j.append(-v)
            elif v > -candidate_j[-1]:
                last_i = -candidate_i[-1]
                while candidate_j and v > -candidate_j[-1]:
                    candidate_i.pop()
                    candidate_j.pop()
                candidate_i.append(-last_i)
                candidate_j.append(-v)

        return False
复杂度分析

时间复杂度：O(n \log n)O(nlogn)，枚举 ii 的次数为 O(n)O(n)，由于每一个元素最多被加入和弹出单调栈各一次，因此操作单调栈的时间复杂度一共为 O(n)O(n)。二分查找的单次时间为 O(\log n)O(logn)，一共为 O(n \log n)O(nlogn)，总时间复杂度为 O(n \log n)O(nlogn)。

空间复杂度：O(n)O(n)，即为单调栈需要使用的空间。

结语
在上面的三种方法中，方法二的时间复杂度为 O(n)O(n)，最优秀。而剩余的两种时间复杂度为 O(n \log n)O(nlogn) 的方法中，方法一相较于方法三，无论从理解还是代码编写层面来说都更容易一些。那么为什么还要介绍方法三呢？这里我们可以发现方法一和方法二的不足：

方法一需要提前知道整个数组，否则就无法使用有序集合维护右侧元素了；

方法二是从后向前遍历的，本质上也同样需要提前知道整个数组。

而方法三是从前向后遍历的，并且维护的数据结构不依赖于后续未知的元素，因此如果数组是以「数据流」的形式给出的，那么方法三是唯一可以继续使用的方法。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/132-pattern/solution/132mo-shi-by-leetcode-solution-ye89/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
