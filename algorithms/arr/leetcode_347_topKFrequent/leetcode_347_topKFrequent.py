class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        sum_dict = dict()
        for num in nums:
            if num in sum_dict:
                sum_dict[num] += 1
            else:
                sum_dict[num] = 1
        ret = []
        for key in sorted(sum_dict, key=sum_dict.__getitem__, reverse=True):
            if k > 0:
                ret.append(key)
                k -= 1
            else:
                break
        return ret


class Solution1(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from collections import Counter
        return [k[0] for k in Counter(nums).most_common(k)]

if __name__ == '__main__':
    test_list = [1, 1, 1, 2, 2, 3, 4, 5, 6, 9, 10]
    demo = Solution()

    print(demo.topKFrequent(test_list, 10))

    demo1 = Solution1()

    print(demo1.topKFrequent(test_list, 10))
