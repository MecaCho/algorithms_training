class Solution(object):
    def maxDotProduct(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        # if not nums1 or not nums2:
        #     return 0
        # if len(nums1) == 1:
        #     return max([num*nums1[0] for num in nums2])
        # if len(nums2) == 1:
        #     return max([num*nums2[0] for num in nums1])
        # res = self.maxDotProduct(nums1, nums2[:-1])
        # if nums1[-1] * nums2[-1] > 0:
        #     return res + nums1[-1] * nums2[-1]
        # return res
        dp = [[[-float("inf"), -float("inf")] for _ in range(len(nums2))] for _ in range(len(nums1))]
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                dp[i][j][0] = max(max(dp[i - 1][j - 1]), dp[i][j][0])
                dp[i][j][1] = max(max(dp[i - 1][j - 1]) + nums1[i] * nums2[j], dp[i][j][1])
        return max(dp[-1][-1])



#     testcases

# [2,1,-2,5]
# [3,0,-6]
# [3,-2]
# [2,-6,7]
# [-1,-1]
# [1,1]
# [-5,3,-5,-3,1]
# [-2,4,2,5,-5]

