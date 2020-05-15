
# coding=utf-8
def find_max_p(s):
    hash_map = {}
    for i in range(len(s)):
        if s[i] not in hash_map:
            hash_map[s[i]] = 1
        else:
            hash_map[s[i]] += 1

    res = 0
    flag = False
    for k, v in hash_map.items():
        if v % 2 == 0:
            res += v
        else:
            res += v - 1
            flag = True

    res = res if not flag else res + 1

    return res

def get_min_coins(coins, amount):

    res = -1
    dp = [float("inf") for _ in range(amount +1)]
    for i in range(len(coins)):
        dp[coins[i]] = 1
        for j in range(amount +1):
            # dp.append(0)
            if j- coins[i] >= 0:
                dp[j] = min(dp[j - coins[i]] + 1, dp[j])
    print(dp)
    return dp[-1] if dp[-1] != float("inf") else -1


if __name__ == "__main__":
    res = find_max_p("abcccccdgsfdgshfgds")
    print(res)

    res = get_min_coins([1, 2, 5], 11)
    print(res)
    res = get_min_coins([2], 3)
    print(res)
