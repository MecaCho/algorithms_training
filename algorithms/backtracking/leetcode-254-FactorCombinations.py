
'''
254. 因子的组合
整数可以被看作是其因子的乘积。

例如：

8 = 2 x 2 x 2;
  = 2 x 4.
请实现一个函数，该函数接收一个整数 n 并返回该整数所有的因子组合。

注意：

你可以假定 n 为永远为正数。
因子必须大于 1 并且小于 n。
示例 1：

输入: 1
输出: []
示例 2：

输入: 37
输出: []
示例 3：

输入: 12
输出:
[
  [2, 6],
  [2, 2, 3],
  [3, 4]
]
示例 4:

输入: 32
输出:
[
  [2, 16],
  [2, 2, 8],
  [2, 2, 2, 4],
  [2, 2, 2, 2, 2],
  [2, 4, 4],
  [4, 8]
]

254. Factor Combinations
Numbers can be regarded as product of its factors. For example,

8 = 2 x 2 x 2;
  = 2 x 4.
Write a function that takes an integer n and return all possible combinations of its factors.

Note:

You may assume that n is always positive.
Factors should be greater than 1 and less than n.
Example 1:

Input: 1
Output: []
Example 2:

Input: 37
Output:[]
Example 3:

Input: 12
Output:
[
  [2, 6],
  [2, 2, 3],
  [3, 4]
]
Example 4:

Input: 32
Output:
[
  [2, 16],
  [2, 2, 8],
  [2, 2, 2, 4],
  [2, 2, 2, 2, 2],
  [2, 4, 4],
  [4, 8]
]
'''


class Solution(object):
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        factors = []
        for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0:
                factors.append(i)
                factors.append(n/i)
                res.append([i, n/i])

        if not factors:
            return res
        for factor in factors:
            vals = self.getFactors(factor)
            for val in vals:
                new_item = sorted(val + [n/factor])
                if new_item not in res:
                    res.append(new_item)

        return res


# golang

'''
func getFactors(n int) [][]int {
	res := [][]int{}
	factors := []int{}
	for i := 2; i < int(math.Sqrt(float64(n)))+1; i++ {
		if n%i == 0 {
			factors = append(factors, i, n/i)
			item := []int{i, n / i}
			res = append(res, item)
		}
	}
	sort.Ints(factors)

	if len(factors) == 0 {
		return res
	}

	for i := range factors {

		vals := getFactors(factors[i])

		for j := range vals {

			new_item := vals[j]
			new_item = append(new_item, n/factors[i])
			sort.Ints(new_item)
			flag := false
			for _, v := range res {
				if reflect.DeepEqual(v, new_item) {
					flag = true
				}
			}
			if !flag {
				res = append(res, new_item)
			}
		}
	}

	return res
}
'''