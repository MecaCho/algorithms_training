

class Solution(object):
    def combinationSum(self, nums, target):
        self.vals = []
        nums = sorted(nums)
        def dfs(path, start, target):
            if target < 0:
                return
            if target == 0:
                self.vals.append(path)
                return
            for i in range(start, len(nums)):
                if nums[i] in path:
                    continue
                dfs(path+[nums[i]], i, target - nums[i])
        dfs([], 0, target)
        return len(self.vals), self.vals


def get_pairs(arr, target):
    hash_map = {}
    res = []
    for i in range(len(arr)):
        if arr[i] in hash_map:
            res.append([arr[i], hash_map[arr[i]]])
        else:
            hash_map[target- arr[i]] = arr[i]
    return res

def new_sum_of_target(arr, target):
    arr.sort()
    max_sum = arr[-1] + arr[-2]
    min_sum = arr[0] + arr[1]
    i = 0
    j = len(arr) - 1
    sum_ = 0
    res = []
    vals = []

    def bk(res, target):
        # print(res, target)
        if target > max_sum or target < min_sum or target <= 0:
            return
        new_res = []
        new_arr = [arr[i] for i in range(len(arr)) if arr[i] not in res]
        pairs = get_pairs(new_arr, target)
        for p in pairs:
            tmp = sorted(res + p)
            if tmp not in vals:
                vals.append(tmp)
            new_res.append(tmp)

        for res in new_res:
            for i in range(len(res)):
                tmp = res[:i] + res[i+1:]

                bk(tmp, res[i])

    bk([], target)

    return len(vals), vals

if __name__ == '__main__':
    demo = Solution()
    # arr = [10,5, 0, -1000, 15, -1]

    # (4, [[0, 5, 10], [0, 15], [5, 10], [15]])

    arr = [1,2,3]
    target = 32

    # 1, 3, 5, 2, 4, 6, 10, 100

    res = demo.combinationSum(arr, target)
    print(res)

    res1 = new_sum_of_target(arr, target)
    print(res)