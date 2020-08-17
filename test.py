
import collections


class Solution(object):
    def countSubTrees(self, n, edges, labels):
        """
        :type n: int
        :type edges: List[List[int]]
        :type labels: str
        :rtype: List[int]
        """
        res = [1 for _ in range(n)]
        p = collections.defaultdict(list)
        for k, v in edges:
            p[v].append(k)


        return res



if __name__ == '__main__':
    n = 4
    ed = [[0, 2], [0, 3], [1, 2]]
    l = "aeed"
    res = demo.countSubTrees(n, ed, l)
    print(res)
    assert res == [1,1,2,1]
#     [2,1,1,1,1,1,1]
# [4,2,1,1]
# [3,2,1,1,1]
# [1,2,1,1,2,1]
# [6,5,4,1,3,2,1]


# 7
# [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]]
# "abaedcd"
# 4
# [[0,1],[1,2],[0,3]]
# "bbbb"
# 5
# [[0,1],[0,2],[1,3],[0,4]]
# "aabab"
# 6
# [[0,1],[0,2],[1,3],[3,4],[4,5]]
# "cbabaa"
# 7
# [[0,1],[1,2],[2,3],[3,4],[4,5],[5,6]]
# "aaabaaa"
# 4
# [[0,2],[0,3],[1,2]]
# "aeed"
# 25
# [[4,0],[5,4],[12,5],[3,12],[18,3],[10,18],[8,5],[16,8],[14,16],[13,16],[9,13],[22,9],[2,5],[6,2],[1,6],[11,1],[15,
# 11],[20,11],[7,20],[19,1],[17,19],[23,19],[24,2],[21,24]]
# "hcheiavadwjctaortvpsflssg"
