# coding=utf-8
import sys

# str = raw_input()
# print str
print 'Hello,World!'


def most_common_k(nums, k):
    items = []
    counter = {}
    for i in range(len(nums)):
        if nums[k] in counter:
            counter[nums[i]] += 1
        else:
            items.append(nums[i])
            counter[nums[i]] = 1

            # counter map[key]value
            # {2:100, 3:10}
    k_values = sorted(counter.values(), reverse=True)[:k]

    res = []
    for i in range(len(items)):
        if counter[items[i]] >= k_values[-1]:
            res.append(items[i])

    return res

if __name__ == '__main__':
    nums = [1,2,3,4,1,2,2,1,1,1,4,1,1,1,2]
    res = most_common_k(nums, 3)
    print res

    import collections
    counter = collections.Counter(nums)
    res = counter.most_common(3)
    print res

