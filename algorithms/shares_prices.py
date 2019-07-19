

def max_profit(arr):
    min_price = arr[0]
    profit = 0
    for i in arr:
        min_price = min(i, min_price)
        profit = max(i-min_price, profit)
    return profit

def dur_pfofit(arr):
    seg = len(arr)
    max_profit_ = 0
    for i in xrange(1, seg):
        max_profit_ = max(max_profit(arr[:i])+max_profit(arr[i:]), max_profit_)
    return max_profit_


if __name__ == "__main__":
    print max_profit([10,30,60,100,80,60,90])