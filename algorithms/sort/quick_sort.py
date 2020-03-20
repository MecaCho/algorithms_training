

class Solution(object):
    def quick_sort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def q_sort(arr):
            if not arr:
                return arr
            mid = arr[0]
            arr_left = []
            arr_right = []
            smaller = 0
            for ar in arr[1:]:
                if ar > mid:
                    arr_right.append(ar)
                else:
                    smaller += 1
                    arr_left.append(ar)
            print(smaller, mid)
            return q_sort(arr_left) + [mid] + q_sort(arr_right)
        return q_sort(nums)

if __name__ == '__main__':
        demo = Solution()
        print(demo.quick_sort([1,3,4,10,20, 3,9]))
