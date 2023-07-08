# encoding=utf8

'''
167. 两数之和 II - 输入有序数组
给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。

函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。

说明:

返回的下标值（index1 和 index2）不是从零开始的。
你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。
示例:

输入: numbers = [2, 7, 11, 15], target = 9
输出: [1,2]
解释: 2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。

167. Two Sum II - Input array is sorted
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Note:

Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.
Example:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
'''


class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i, j = 0, len(numbers) -1
        while i <= j:
            sum_tmp = numbers[i] + numbers[j]
            if sum_tmp == target:
                return [i+1, j+1]
            elif sum_tmp > target:
                j -= 1
            else:
                i += 1
        return []


# golang solution

'''
func twoSum(numbers []int, target int) []int {
    
    i, j := 0, len(numbers) - 1
    for i < j {
        tmpSum := numbers[i] + numbers[j]
        if tmpSum == target{
            return []int{i+1, j+1}
        } else if tmpSum < target{
            i++
        }else{
            j--
        }
    }
    return []int{}
    
}
'''

# solution

'''
# two-pointer
def twoSum1(self, numbers, target):
    l, r = 0, len(numbers)-1
    while l < r:
        s = numbers[l] + numbers[r]
        if s == target:
            return [l+1, r+1]
        elif s < target:
            l += 1
        else:
            r -= 1
 
# dictionary           
def twoSum2(self, numbers, target):
    dic = {}
    for i, num in enumerate(numbers):
        if target-num in dic:
            return [dic[target-num]+1, i+1]
        dic[num] = i
 
# binary search        
def twoSum(self, numbers, target):
    for i in xrange(len(numbers)):
        l, r = i+1, len(numbers)-1
        tmp = target - numbers[i]
        while l <= r:
            mid = l + (r-l)//2
            if numbers[mid] == tmp:
                return [i+1, mid+1]
            elif numbers[mid] < tmp:
                l = mid+1
            else:
                r = mid-1
'''

# solution

'''
方法 1：双指针
算法

我们可以使用 两数之和 的解法在 O(n^2)O(n 
2
 ) 时间 O(1)O(1) 空间暴力解决，也可以用哈希表在 O(n)O(n) 时间和 O(n)O(n) 空间内解决。然而，这两种方法都没有用到输入数组已经排序的性质，我们可以做得更好。

我们使用两个指针，初始分别位于第一个元素和最后一个元素位置，比较这两个元素之和与目标值的大小。如果和等于目标值，我们发现了这个唯一解。如果比目标值小，我们将较小元素指针增加一。如果比目标值大，我们将较大指针减小一。移动指针后重复上述比较知道找到答案。

假设 [... , a, b, c, ... , d, e, f, …][...,a,b,c,...,d,e,f,…] 是已经升序排列的输入数组，并且元素 b, eb,e 是唯一解。因为我们从左到右移动较小指针，从右到左移动较大指针，总有某个时刻存在一个指针移动到 bb 或 ee 的位置。不妨假设小指针县移动到了元素 bb ，这是两个元素的和一定比目标值大，根据我们的算法，我们会向左移动较大指针直至获得结果。

C++
class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int low = 0, high = numbers.size() - 1;
        while (low < high) {
            int sum = numbers[low] + numbers[high];
            if (sum == target)
                return {low + 1, high + 1};
            else if (sum < target)
                ++low;
            else
                --high;
        }
        return {-1, -1};
    }
};
是否需要考虑 numbers[low] + numbers[high]numbers[low]+numbers[high] 溢出呢？答案是不需要。因为即使两个元素之和溢出了，因为只存在唯一解，所以一定会先访问到答案。

复杂度分析

时间复杂度：O(n)O(n)。每个元素最多被访问一次，共有 nn 个元素。
空间复杂度：O(1)O(1)。只是用了两个指针。

'''
