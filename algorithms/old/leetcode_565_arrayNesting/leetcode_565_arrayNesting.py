class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = 0
        visited = [0]*len(nums)
        for i in xrange(len(nums)):
            ans = 0
            k = i
            while k < len(nums) and not visited[k]:
                visited[k] = 1
                k = nums[k]
                ans += 1
            ret = max(ans, ret)
        return ret

if __name__ == '__main__':
    demo = Solution()
    assert demo.arrayNesting([5, 4, 0, 3, 1, 6, 2]) == 4
