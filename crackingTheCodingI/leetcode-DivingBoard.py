'''
面试题 16.11. Diving Board LCCI
You are building a diving board by placing a bunch of planks of wood end-to-end. There are two types of planks, one of length shorter and one of length longer. You must use exactly K planks of wood. Write a method to generate all possible lengths for the diving board.

return all lengths in non-decreasing order.

Example:

Input:
shorter = 1
longer = 2
k = 3
Output:  {3,4,5,6}
Note:

0 < shorter <= longer
0 <= k <= 100000


面试题 16.11. 跳水板
你正在使用一堆木板建造跳水板。有两种类型的木板，其中长度较短的木板长度为shorter，长度较长的木板长度为longer。你必须正好使用k块木板。编写一个方法，生成跳水板所有可能的长度。

返回的长度需要从小到大排列。

示例：

输入：
shorter = 1
longer = 2
k = 3
输出： {3,4,5,6}
提示：

0 < shorter <= longer
0 <= k <= 100000
'''


class Solution(object):
    def divingBoard(self, shorter, longer, k):
        """
        :type shorter: int
        :type longer: int
        :type k: int
        :rtype: List[int]
        """
        # res = {}
        # print(res)
        if k == 0:
            return []
        return range(shorter*k, longer*k+1, longer-shorter) if longer > shorter else [longer*k]
        # return [longer*i + shorter*(k-i) for i in range(k+1)] if k > 0 else []


# golang

'''
func divingBoard(shorter int, longer int, k int) []int {
    res := []int{}
    if k == 0{
        return res
    }
    if shorter == longer{
        res = append(res, shorter*k)
        return res
    }
    for i := shorter*k;i <= longer*k; i += (longer-shorter){
        res = append(res, i)
    }
    return res
}
'''