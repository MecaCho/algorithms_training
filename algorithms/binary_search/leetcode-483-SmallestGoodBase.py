# encoding=utf8

'''
483. Smallest Good Base

Given an integer n represented as a string, return the smallest good base of n.

We call k >= 2 a good base of n, if all digits of n base k are 1's.

 

Example 1:

Input: n = "13"
Output: "3"
Explanation: 13 base 3 is 111.
Example 2:

Input: n = "4681"
Output: "8"
Explanation: 4681 base 8 is 11111.
Example 3:

Input: n = "1000000000000000000"
Output: "999999999999999999"
Explanation: 1000000000000000000 base 999999999999999999 is 11.
 

Constraints:

n is an integer in the range [3, 1018].
n does not contain any leading zeros.

483. 最小好进制

对于给定的整数 n, 如果n的k（k>=2）进制数的所有数位全为1，则称 k（k>=2）是 n 的一个好进制。

以字符串的形式给出 n, 以字符串的形式返回 n 的最小好进制。

 

示例 1：

输入："13"
输出："3"
解释：13 的 3 进制是 111。
示例 2：

输入："4681"
输出："8"
解释：4681 的 8 进制是 11111。
示例 3：

输入："1000000000000000000"
输出："999999999999999999"
解释：1000000000000000000 的 999999999999999999 进制是 11。
 

提示：

n的取值范围是 [3, 10^18]。
输入总是有效且没有前导 0。

'''

# golang solution

'''
func smallestGoodBase(n string) string {
    nVal, _ := strconv.Atoi(n)
    mMax := bits.Len(uint(nVal)) - 1
    for m := mMax; m > 1; m-- {
        k := int(math.Pow(float64(nVal), 1/float64(m)))
        mul, sum := 1, 1
        for i := 0; i < m; i++ {
            mul *= k
            sum += mul
        }
        if sum == nVal {
            return strconv.Itoa(k)
        }
    }
    return strconv.Itoa(nVal - 1)
}
'''
