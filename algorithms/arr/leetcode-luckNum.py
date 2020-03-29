


class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        import collections
        hash_map = collections.Counter(arr)
        for k, value in hash_map.items():
            if k == value:
                return k
        return -1

if __name__ == '__main__':
    demo = Solution()
    print(demo.findLucky([1,2,3,3,4,5,3]))