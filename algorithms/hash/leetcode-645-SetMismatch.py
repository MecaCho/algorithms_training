# encoding=utf8


'''
645. Set Mismatch
The set S originally contains numbers from 1 to n. But unfortunately, due to the data error, one of the numbers in the set got duplicated to another number in the set, which results in repetition of one number and loss of another number.

Given an array nums representing the data status of this set after the error. Your task is to firstly find the number occurs twice and then find the number that is missing. Return them in the form of an array.

Example 1:
Input: nums = [1,2,2,4]
Output: [2,3]
Note:
The given array size will in the range [2, 10000].
The given array's numbers won't have any order.

645. 错误的集合
集合 S 包含从1到 n 的整数。不幸的是，因为数据错误，导致集合里面某一个元素复制了成了集合里面的另外一个元素的值，导致集合丢失了一个整数并且有一个元素重复。

给定一个数组 nums 代表了集合 S 发生错误后的结果。你的任务是首先寻找到重复出现的整数，再找到丢失的整数，将它们以数组的形式返回。

示例 1:

输入: nums = [1,2,2,4]
输出: [2,3]
注意:

给定数组的长度范围是 [2, 10000]。
给定的数组是无序的。

'''


class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return [sum(nums) - sum(set(nums)), sum(range(1, len(nums)+1))-sum(set(nums))]
        # hash_map = collections.Counter(nums)
        # dul = None
        # los = None
        # for i in range(len(nums)):
        #     if i+1 not in hash_map:
        #         los = i+1
        #     elif hash_map[i+1] == 2:
        #         dul = i+1
        # return [dul, los]
        # return [k for k, v in hash_map.items() if v == 2]

        
        
class Solution1(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return [sum(nums) - sum(set(nums)), sum(range(1, len(nums)+1))-sum(set(nums))]


# solutions

'''
https://leetcode.com/articles/set-mismatch/
'''

# solutions

'''
方法一：排序
将数组排序之后，比较每对相邻的元素，即可找到错误的集合。

寻找重复的数字较为简单，如果相邻的两个元素相等，则该元素为重复的数字。

寻找丢失的数字相对复杂，可能有以下两种情况：

如果丢失的数字大于 11 且小于 nn，则一定存在相邻的两个元素的差等于 22，这两个元素之间的值即为丢失的数字；

如果丢失的数字是 11 或 nn，则需要另外判断。

为了寻找丢失的数字，需要在遍历已排序数组的同时记录上一个元素，然后计算当前元素与上一个元素的差。考虑到丢失的数字可能是 11，因此需要将上一个元素初始化为 00。

当丢失的数字小于 nn 时，通过计算当前元素与上一个元素的差，即可得到丢失的数字；

如果 \textit{nums}[n-1] \ne nnums[n−1] 

​
 =n，则丢失的数字是 nn。

JavaC#C++CJavaScriptGolang

func findErrorNums(nums []int) []int {
    ans := make([]int, 2)
    sort.Ints(nums)
    pre := 0
    for _, v := range nums {
        if v == pre {
            ans[0] = v
        } else if v-pre > 1 {
            ans[1] = pre + 1
        }
        pre = v
    }
    n := len(nums)
    if nums[n-1] != n {
        ans[1] = n
    }
    return ans
}
复杂度分析

时间复杂度：O(n \log n)O(nlogn)，其中 nn 是数组 \textit{nums}nums 的长度。排序需要 O(n \log n)O(nlogn) 的时间，遍历数组找到错误的集合需要 O(n)O(n) 的时间，因此总时间复杂度是 O(n \log n)O(nlogn)。

空间复杂度：O(\log n)O(logn)，其中 nn 是数组 \textit{nums}nums 的长度。排序需要 O(\log n)O(logn) 的空间。

方法二：哈希表
重复的数字在数组中出现 22 次，丢失的数字在数组中出现 00 次，其余的每个数字在数组中出现 11 次。因此可以使用哈希表记录每个元素在数组中出现的次数，然后遍历从 11 到 nn 的每个数字，分别找到出现 22 次和出现 00 次的数字，即为重复的数字和丢失的数字。

JavaC#C++CJavaScriptGolang

func findErrorNums(nums []int) []int {
    cnt := map[int]int{}
    for _, v := range nums {
        cnt[v]++
    }
    ans := make([]int, 2)
    for i := 1; i <= len(nums); i++ {
        if c := cnt[i]; c == 2 {
            ans[0] = i
        } else if c == 0 {
            ans[1] = i
        }
    }
    return ans
}
复杂度分析

时间复杂度：O(n)O(n)，其中 nn 是数组 \textit{nums}nums 的长度。需要遍历数组并填入哈希表，然后遍历从 11 到 nn 的每个数寻找错误的集合。

空间复杂度：O(n)O(n)，其中 nn 是数组 \textit{nums}nums 的长度。需要创建大小为 O(n)O(n) 的哈希表。

方法三：位运算
使用位运算，可以达到 O(n)O(n) 的时间复杂度和 O(1)O(1) 的空间复杂度。

重复的数字在数组中出现 22 次，丢失的数字在数组中出现 00 次，其余的每个数字在数组中出现 11 次。由此可见，重复的数字和丢失的数字的出现次数的奇偶性相同，且和其余的每个数字的出现次数的奇偶性不同。如果在数组的 nn 个数字后面再添加从 11 到 nn 的每个数字，得到 2n2n 个数字，则在 2n2n 个数字中，重复的数字出现 33 次，丢失的数字出现 11 次，其余的每个数字出现 22 次。根据出现次数的奇偶性，可以使用异或运算求解。

用 xx 和 yy 分别表示重复的数字和丢失的数字。考虑上述 2n2n 个数字的异或运算结果 \textit{xor}xor，由于异或运算 \oplus⊕ 满足交换律和结合律，且对任何数字 aa 都满足 a \oplus a = 0a⊕a=0 和 0 \oplus a = a0⊕a=a，因此 \textit{xor} = x \oplus x \oplus x \oplus y = x \oplus yxor=x⊕x⊕x⊕y=x⊕y，即 xx 和 yy 的异或运算的结果。

由于 x \ne yx 

​
 =y，因此 \textit{xor} \ne 0xor 

​
 =0，令 \textit{lowbit} = \textit{xor}~\&~(-\textit{xor})lowbit=xor & (−xor)，则 \textit{lowbit}lowbit 为 xx 和 yy 的二进制表示中的最低不同位，可以用 \textit{lowbit}lowbit 区分 xx 和 yy。

得到 \textit{lowbit}lowbit 之后，可以将上述 2n2n 个数字分成两组，第一组的每个数字 aa 都满足 a~\&~\textit{lowbit} = 0a & lowbit=0，第二组的每个数字 bb 都满足 b~\&~\textit{lowbit} \ne 0b & lowbit 

​
 =0。

创建两个变量 \textit{num}_1num 
1
​
  和 \textit{num}_2num 
2
​
 ，初始值都为 00，然后再次遍历上述 2n2n 个数字，对于每个数字 aa，如果 a~\&~\textit{lowbit} = 0a & lowbit=0，则令 \textit{num}_1 = \textit{num}_1 \oplus anum 
1
​
 =num 
1
​
 ⊕a，否则令 \textit{num}_2 = \textit{num}_2 \oplus anum 
2
​
 =num 
2
​
 ⊕a。

遍历结束之后，\textit{num}_1num 
1
​
  为第一组的全部数字的异或结果，\textit{num}_2num 
2
​
  为第二组的全部数字的异或结果。由于同一个数字只可能出现在其中的一组，且除了 xx 和 yy 以外，每个数字一定在其中的一组出现 22 次，因此 \textit{num}_1num 
1
​
  和 \textit{num}_2num 
2
​
  分别对应 xx 和 yy 中的一个数字，但是具体对应哪个数还未知。

为了知道 \textit{num}_1num 
1
​
  和 \textit{num}_2num 
2
​
  分别对应 xx 和 yy 中的哪一个数字，只需要再次遍历数组 \textit{nums}nums 即可。如果数组中存在元素等于 \textit{num}_1num 
1
​
 ，则有 x=\textit{num}_1x=num 
1
​
  和 y=\textit{num}_2y=num 
2
​
 ，否则有 x=\textit{num}_2x=num 
2
​
  和 y=\textit{num}_1y=num 
1
​
 。

JavaC#C++CJavaScriptGolang

func findErrorNums(nums []int) []int {
    xor := 0
    for _, v := range nums {
        xor ^= v
    }
    n := len(nums)
    for i := 1; i <= n; i++ {
        xor ^= i
    }
    lowbit := xor & -xor
    num1, num2 := 0, 0
    for _, v := range nums {
        if v&lowbit == 0 {
            num1 ^= v
        } else {
            num2 ^= v
        }
    }
    for i := 1; i <= n; i++ {
        if i&lowbit == 0 {
            num1 ^= i
        } else {
            num2 ^= i
        }
    }
    for _, v := range nums {
        if v == num1 {
            return []int{num1, num2}
        }
    }
    return []int{num2, num1}
}
复杂度分析

时间复杂度：O(n)O(n)，其中 nn 是数组 \textit{nums}nums 的长度。整个过程需要对数组 \textit{nums}nums 遍历 33 次，以及遍历从 11 到 nn 的每个数 22 次。

空间复杂度：O(1)O(1)。只需要常数的额外空间。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/set-mismatch/solution/cuo-wu-de-ji-he-by-leetcode-solution-1ea4/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
