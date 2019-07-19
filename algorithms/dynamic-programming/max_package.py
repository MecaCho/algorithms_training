items = [2, 2, 6, 5, 4]
prices = [6, 3, 5, 4, 6]

def find_max(n=10):
    item_num = len(items)
    dp = [[0]*item_num] * item_num
    for i in xrange(item_num):
        if i < min_item:
            return 0
        elif i == min_item:
            return min_profit
        else:
            pass
