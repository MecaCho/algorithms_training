#
# class Solution(object):
#     def minSubArrayLen(self, s, nums):
#         """
#         :type s: int
#         :type nums: List[int]
#         :rtype: int
#         """
#         if sum(nums) < s:
#             return []
#         if sum(nums) == s:
#             return [len(nums)]
#         res = []
#         # print(nums)
#         for i in range(2, len(nums)):
#             j = 0
#             while j < len(nums ) - i +1:
#                 # print(nums[j:j+i])
#                 if sum(nums[j: j +i]) == s:
#                     res.append(i)
#                     j += i
#                 else:
#                     j += 1
#                 if len(res) >= 2:
#                     return res
#         return res
#     #         i = 0
#     #         j = 0
#     #         res = 0
#     #         cur_sum = 0
#     #         cur = []
#     #         while j < len(nums):
#     #             cur_sum += nums[j]
#     #             while cur_sum == s:
#     #                 if not res or j - i + 1 < res:
#     #                     res = j - i + 1
#     #                 cur_sum -= nums[i]
#     #                 i += 1
#     #             j += 1
#
#     #         return res
#
#     def minSumOfLengths(self, arr, target):
#         """
#         :type arr: List[int]
#         :type target: int
#         :rtype: int
#         """
#         res = []
#         vals = []
#         tmp = []
#         for i in range(len(arr)):
#             tmp.append(arr[i])
#             if arr[i] == target:
#                 res.append(i)
#                 if tmp[:-1]:
#                     vals.append(tmp[:-1])
#                 tmp = []
#             elif arr[i] > target:
#                 if tmp[:-1]:
#                     vals.append(tmp[:-1])
#                 tmp = []
#         if tmp:
#             vals.append(tmp)
#             # print(res, vals)
#         if len(res) > =2 :
#             return 2
#         if not vals:
#             return -1
#
#         ress = [1] if res else []
#         for val in vals:
#             new_res = self.minSubArrayLen(target, val)
#             if new_res:
#                 ress.extend(new_res)
#         # print(ress)
#         if len(ress) >= 2:
#             return sum(sorted(ress)[:2])
#         else:
#             return -1


def max_sub_arr1(arr):
  max_sum = 0
  cur = []
  cur_sum = 0
  res = []
  for i in range(len(arr)):
    if cur_sum < 0:
        cur = [arr[i]]
        cur_sum = arr[i]
    else:
        cur.append(arr[i])
        cur_sum += arr[i]
    if cur_sum > max_sum:
      max_sum = cur_sum
      res = cur[:]
  return res


def max_sub_arr(arr):
  max_sum = 0
  cur = []
  cur_sum = -float("inf")
  res = []
  for i in range(len(arr)):
    if cur_sum < 0:
        cur = [arr[i]]
    else:
        cur.append(arr[i])
    cur_sum = sum(cur)
    max_sum = max(max_sum, cur_sum)
    print(max_sum, cur, cur_sum)
    if cur_sum >= max_sum:
      max_sum = cur_sum
      res = cur[:]
  return res




if __name__ == '__main__':
    # demo = Solution()
    # arr = []
    # target = 0
    # res = demo.minSumOfLengths()
    res = max_sub_arr1([-1, -1, 2, -1, 1,9,-1,-2,1])
    print(res)