# encoding=utf8


'''
16. 3Sum Closest
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

16. 最接近的三数之和
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.

与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).

'''


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        length = len(nums)
        if length <=3:
            return sum(nums)
            
        nums = sorted(nums)

        result_list = [nums[0] , nums[1] , nums[2]]
        closer = abs(nums[0] + nums[1] + nums[2] - target)
        for i in range(length):
            j = i + 1
            k = length - 1
            
            while j < k:
                new_sum = nums[i] + nums[j] + nums[k]
                if abs(new_sum - target) < closer:
                    closer = abs(new_sum - target)
                    result_list = [nums[i], nums[j], nums[k]]

                if new_sum - target == 0:
                    return sum([nums[i], nums[j], nums[k]])
                
                if new_sum - target > 0:
                    # if nums[k] > 0:
                    k -=1
                if new_sum - target < 0:
                    j += 1


        return sum(result_list)


# solutions

'''
本题与 15. 三数之和 非常类似，可以使用「双指针」的方法来解决。但基于题解的独立性，这里还是会从零开始讲解。

方法一：排序 + 双指针
思路与算法

题目要求找到与目标值 \textit{target}target 最接近的三元组，这里的「最接近」即为差值的绝对值最小。我们可以考虑直接使用三重循环枚举三元组，找出与目标值最接近的作为答案，时间复杂度为 O(N^3)O(N 3)。然而本题的 NN 最大为 10001000，会超出时间限制。

那么如何进行优化呢？我们首先考虑枚举第一个元素 aa，对于剩下的两个元素 bb 和 cc，我们希望它们的和最接近 \textit{target} - atarget−a。对于 bb 和 cc，如果它们在原数组中枚举的范围（既包括下标的范围，也包括元素值的范围）没有任何规律可言，那么我们还是只能使用两重循环来枚举所有的可能情况。因此，我们可以考虑对整个数组进行升序排序，这样一来：

假设数组的长度为 nn，我们先枚举 aa，它在数组中的位置为 ii；

为了防止重复枚举，我们在位置 [i+1, n)[i+1,n) 的范围内枚举 bb 和 cc。

当我们知道了 bb 和 cc 可以枚举的下标范围，并且知道这一范围对应的数组元素是有序（升序）的，那么我们是否可以对枚举的过程进行优化呢？

答案是可以的。借助双指针，我们就可以对枚举的过程进行优化。我们用 p_bp b
​	
  和 p_cp c
​	
  分别表示指向 bb 和 cc 的指针，初始时，p_bp 
b
​	
  指向位置 i+1i+1，即左边界；p_cp 
c
​	
  指向位置 n-1n−1，即右边界。在每一步枚举的过程中，我们用 a+b+ca+b+c 来更新答案，并且：

如果 a+b+c \geq \textit{target}a+b+c≥target，那么就将 p_cp 
c
​	
  向左移动一个位置；

如果 a+b+c < \textit{target}a+b+c<target，那么就将 p_bp 
b
​	
  向右移动一个位置。

这是为什么呢？我们对 a+b+c \geq \textit{target}a+b+c≥target 的情况进行一个详细的分析：

如果 a+b+c \geq \textit{target}a+b+c≥target，并且我们知道 p_bp 
b
​	
  到 p_cp 
c
​	
  这个范围内的所有数是按照升序排序的，那么如果 p_cp 
c
​	
  不变而 p_bp 
b
​	
  向右移动，那么 a+b+ca+b+c 的值就会不断地增加，显然就不会成为最接近 \textit{target}target 的值了。因此，我们可以知道在固定了 p_cp 
c
​	
  的情况下，此时的 p_bp 
b
​	
  就可以得到一个最接近 \textit{target}target 的值，那么我们以后就不用再考虑 p_cp 
c
​	
  了，就可以将 p_cp 
c
​	
  向左移动一个位置。

同样地，在 a+b+c < \textit{target}a+b+c<target 时：

如果 a+b+c < \textit{target}a+b+c<target，并且我们知道 p_bp 
b
​	
  到 p_cp 
c
​	
  这个范围内的所有数是按照升序排序的，那么如果 p_bp 
b
​	
  不变而 p_cp 
c
​	
  向左移动，那么 a+b+ca+b+c 的值就会不断地减小，显然就不会成为最接近 \textit{target}target 的值了。因此，我们可以知道在固定了 p_bp 
b
​	
  的情况下，此时的 p_cp 
c
​	
  就可以得到一个最接近 \textit{target}target 的值，那么我们以后就不用再考虑 p_bp 
b
​	
  了，就可以将 p_bp 
b
​	
  向右移动一个位置。

实际上，p_bp 
b
​	
  和 p_cp 
c
​	
  就表示了我们当前可以选择的数的范围，而每一次枚举的过程中，我们尝试边界上的两个元素，根据它们与 \textit{target}target 的值的关系，选择「抛弃」左边界的元素还是右边界的元素，从而减少了枚举的范围。这种思路与 11. 盛最多水的容器 中的双指针解法也是类似的。

小优化

本题也有一些可以减少运行时间（但不会减少时间复杂度）的小优化。当我们枚举到恰好等于 \textit{target}target 的 a+b+ca+b+c 时，可以直接返回 \textit{target}target 作为答案，因为不会有再比这个更接近的值了。

另一个优化与 15. 三数之和的官方题解 中提到的类似。当我们枚举 a, b, ca,b,c 中任意元素并移动指针时，可以直接将其移动到下一个与这次枚举到的不相同的元素，减少枚举的次数。

C++JavaPython3GolangC

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        best = 10**7
        
        # 根据差值的绝对值来更新答案
        def update(cur):
            nonlocal best
            if abs(cur - target) < abs(best - target):
                best = cur
        
        # 枚举 a
        for i in range(n):
            # 保证和上一次枚举的元素不相等
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # 使用双指针枚举 b 和 c
            j, k = i + 1, n - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                # 如果和为 target 直接返回答案
                if s == target:
                    return target
                update(s)
                if s > target:
                    # 如果和大于 target，移动 c 对应的指针
                    k0 = k - 1
                    # 移动到下一个不相等的元素
                    while j < k0 and nums[k0] == nums[k]:
                        k0 -= 1
                    k = k0
                else:
                    # 如果和小于 target，移动 b 对应的指针
                    j0 = j + 1
                    # 移动到下一个不相等的元素
                    while j0 < k and nums[j0] == nums[j]:
                        j0 += 1
                    j = j0

        return best
复杂度分析

时间复杂度：O(N^2)O(N 2)，其中 NN 是数组 \textit{nums}nums 的长度。我们首先需要 O(N \log N)O(NlogN) 的时间对数组进行排序，随后在枚举的过程中，使用一重循环 O(N)O(N) 枚举 aa，双指针 O(N)O(N) 枚举 bb 和 cc，故一共是 O(N^2)O(N 
2)。

空间复杂度：O(\log N)O(logN)。排序需要使用 O(\log N)O(logN) 的空间。然而我们修改了输入的数组 \textit{nums}nums，在实际情况下不一定允许，因此也可以看成使用了一个额外的数组存储了 \textit{nums}nums 的副本并进行排序，此时空间复杂度为 O(N)O(N)。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/3sum-closest/solution/zui-jie-jin-de-san-shu-zhi-he-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
