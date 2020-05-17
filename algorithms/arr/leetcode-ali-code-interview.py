#  /*
# 问题：给定一个m
# x
# n的矩阵，其中全是自然数，找出从左上角到右下角的所有路径中，路径内节点之和最小的路径。
# 只能向右或者向下移动
#
# Input:
# [
#     [1, 3, 1],
#     [1, 5, 1],
#     [4, 2, 1]
#     ]
# Output: 7
# 解释: 因为路径1→3→1→1→1
# 的和最小.
# * /
#
# / *
#
#
# * /

# dp[i][j] = min(min(dp[i][j-1], dp[i-1][j]) + arr[i][j], dp[i][j])

def get_min_sum_path(arr):
    if not arr:
        return None

    if not arr[0]:
        return sum(arr)

    dp = [[float("inf") for _ in range(len(arr[0]))] for _ in range(len(arr))]
    dp[0][0] = arr[0][0]
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if i == 0 and j != 0:
                dp[i][j] = dp[i][j - 1] + arr[i][j]
            if j == 0 and i != 0:
                dp[i][j] = dp[i - 1][j] + arr[i][j]

    print(dp)
    for i in range(1, len(arr)):
        for j in range(1, len(arr[0])):
            min_pre = min(dp[i][j - 1], dp[i - 1][j]) + arr[i][j]
            dp[i][j] = min(min_pre, dp[i][j])
    print(dp)
    return dp[-1][-1]

if __name__ == '__main__':
    res = get_min_sum_path([[1,2,3],[1,1,2],[1,3,4]])
    print(res)


