def find_same_items(list1, list2):
    if not list1 or not list2:
        return []
    i, j, ret = 0, 0, []
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            ret.append(list1[i])
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            i += 1
        elif list2[j] < list1[i]:
            j += 1

    return ret


if __name__ == '__main__':
    import math
    # math.gcd()
    import collections

    deck = [1,2,3,4,1]
    dict_num = collections.Counter(deck)
    print(dict_num.elements())
    print(dict_num.values())
    print(dict_num, dict_num.values())
    # math.gcd([10,5,10])
    # print(find_same_items([1, 2, 3, 4, 9], [3, 4, 5, 9, 10]))
    # print(find_same_items([], [3, 4, 5, 9, 10]))
    # print(find_same_items([10], [3, 4, 5, 9, 10]))


