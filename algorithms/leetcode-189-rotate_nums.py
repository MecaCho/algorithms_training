class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        return nums[len(nums) - k:] + nums[0:len(nums) - k]

if __name__ == '__main__':
    demo = Solution()
    print(demo.rotate([1,2,3,4,5,6,7], 3))
