# encoding=utf8

'''
689. Maximum Sum of 3 Non-Overlapping Subarrays
Given an integer array nums and an integer k, find three non-overlapping subarrays of length k with maximum sum and return them.

Return the result as a list of indices representing the starting position of each interval (0-indexed). If there are multiple answers, return the lexicographically smallest one.

 

Example 1:

Input: nums = [1,2,1,2,6,7,5,1], k = 2
Output: [0,3,5]
Explanation: Subarrays [1, 2], [2, 6], [7, 5] correspond to the starting indices [0, 3, 5].
We could have also taken [2, 1], but an answer of [1, 3, 5] would be lexicographically larger.
Example 2:

Input: nums = [1,2,1,2,1,2,1,2,1], k = 2
Output: [0,2,4]
 

Constraints:

1 <= nums.length <= 2 * 104
1 <= nums[i] < 216
1 <= k <= floor(nums.length / 3)


'''

# golang solution

'''
func maxSumOfThreeSubarrays(nums []int, k int) []int {
    var ans []int
    var sum1, maxSum1, maxSum1Idx int
    var sum2, maxSum12, maxSum12Idx1, maxSum12Idx2 int
    var sum3, maxTotal int
    for i := k * 2; i < len(nums); i++ {
        sum1 += nums[i-k*2]
        sum2 += nums[i-k]
        sum3 += nums[i]
        if i >= k*3-1 {
            if sum1 > maxSum1 {
                maxSum1 = sum1
                maxSum1Idx = i - k*3 + 1
            }
            if maxSum1+sum2 > maxSum12 {
                maxSum12 = maxSum1 + sum2
                maxSum12Idx1, maxSum12Idx2 = maxSum1Idx, i-k*2+1
            }
            if maxSum12+sum3 > maxTotal {
                maxTotal = maxSum12 + sum3
                ans = []int{maxSum12Idx1, maxSum12Idx2, i - k + 1}
            }
            sum1 -= nums[i-k*3+1]
            sum2 -= nums[i-k*2+1]
            sum3 -= nums[i-k+1]
        }
    }
    return ans
}
'''

