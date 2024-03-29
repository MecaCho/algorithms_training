# encoding=utf8

'''
233. Number of Digit One
Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.

Example:

Input: 13
Output: 6
Explanation: Digit 1 occurred in the following numbers: 1, 10, 11, 12, 13.

233. 数字 1 的个数
给定一个整数 n，计算所有小于等于 n 的非负整数中数字 1 出现的个数。

示例:

输入: 13
输出: 6
解释: 数字 1 出现在以下数字中: 1, 10, 11, 12, 13 。
'''



class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        i = 1
        while i <= n:

            divider = i * 10
            count += (n / divider) * i + min(max((n % divider) - i + 1, 0), i)
            i *= 10

        return count

# golang solution

'''
func countDigitOne(n int) int {
    min := func(a, b int) int{
        if a < b {
            return a
        }
        return b
    }

    max := func(a, b int) int {
        if a > b {
            return a
        }
        return b
    }
    
    res := 0
    for k, mulk := 0, 1; n >= mulk; k++ {
        res += (n/(mulk*10))*mulk + min(max(n%(mulk*10)-mulk+1, 0), mulk)
        mulk *= 10
    }
    return res
}

'''

# solutions


'''
方法一 暴力 【超时】
思路

直接照着题目的描述模拟就可以了。

算法

将 ii 从 11 遍历到 nn：
将 ii 转成字符串，数 \text{'1'}’1’ 的个数
将每个字符串里 \text{'1'}’1’ 的个数累加到变量 countr
返回 countr
C++
int countDigitOne(int n)
{
    int countr = 0;
    for (int i = 1; i <= n; i++) {
        string str = to_string(i);
        countr += count(str.begin(), str.end(), '1');
    }
    return countr;
}
复杂度分析

时间复杂度：O(n*log_{10}(n))O(n∗log 
10
​	
 (n))

从 11 遍历到 nn
每次遍历中，我们把整数转成字符串去数 \text{'1'}’1’ 的个数，这个过程会花费 mm 的时间，其中 mm 为字符串的长度，其最大值为 log_{10}(n)log 
10
​	
 (n)。
空间复杂度：需要申请 O(log_{10}(n))O(log 
10
​	
 (n)) 个额外的空间来存储 countr 和整数转换成的字符串 \text{str}str。

方法二 数学法 【通过】
思路

在方法一中，我们手动计算了每个数中 \text{'1'}’1’ 的个数，但这种计算是非常慢。因此，我们需要找到 \text{'1'}’1’ 在这些数中出现的规律。然后我们就能利用这个规律来形成数学公式解决问题了。

考虑 \text{'1'}’1’ 在 个位，十位，百位，... 出现的情况，我们可以做出以下的分析：



由上图所示，我们可以观察到每 1010 个数，个位上的 \text{'1'}’1’ 就会出现一次。同样的，每 100100 个数，十位上的 \text{'1'}’1’ 就会出现一次。这个规律可以用 (n/(i*10))*i(n/(i∗10))∗i 公式来表示。

同时，如果十位上的数是 \text{'1'}’1’，那么最后 \text{'1'}’1’ 的数量要加上 x+1x+1，其中 xx 是个位上的数值。如果十位上的数大于 \text{'1'}’1’，那么十位上为 \text{'1'}’1’ 的所有的数都是符合要求的，这时候最后 \text{'1'}’1’ 的数量要加 1010。

这个规律可以用公式 {\min(\max((\text{n mod (i*10)} )-i+1,0),i)}min(max((n mod (i*10))−i+1,0),i) 来表示。

我们来看一个例子吧，有一个数 n = 1234n=1234。

个位上 \text{'1'}’1’ 的数量 = 1234/101234/10 (对应 1,11,21,...1221) + \min(4,1)min(4,1) (对应 1231) = 124124

十位上 \text{'1'}’1’ 的数量 = (1234/100)*10(1234/100)∗10 (对应 10,11,12,...,110,111,...1919) + \min(21, 10)min(21,10) (对应 1210,1211,...1219) = 130130

百位上 \text{'1'}’1’ 的数量 = (1234/1000)*100(1234/1000)∗100 (对应 100,101,102,...,199) + \min(135, 100)min(135,100) (对应1100,1101...1199) = 200200

千位上 \text{'1'}’1’ 的数量 = (1234/10000)*10000(1234/10000)∗10000 + \min(235, 1000)min(235,1000) (对应1000,1001,...1234) = 235235

因此，总数 = 124+130+200+235 = 689124+130+200+235=689。

算法

将 ii 从 11 遍历到 nn，每次遍历 ii 扩大 1010 倍：
(n/(i*10))*i(n/(i∗10))∗i 表示 (i*10)(i∗10) 位上 \text{'1'}’1’ 的个数。
{\min(\max((\text{n mod (i*10)} )-i+1,0),i)}min(max((n mod (i*10))−i+1,0),i) 表示需要额外数的 (i*10)(i∗10) 位上 \text{'1'}’1’ 的个数。
C++
int countDigitOne(int n)
{
    int countr = 0;
    for (long long i = 1; i <= n; i *= 10) {
        long long divider = i * 10;
        countr += (n / divider) * i + min(max(n % divider - i + 1, 0LL), i);
    }
    return countr;
}
复杂度分析

时间复杂度：O(log_{10}(n))O(log 
10
​	
 (n))

遍历的次数等于 nn 转成字符串后字符串的长度，其值为 log_{10}(n)log 
10
​	
 (n)。
空间复杂度：只需要 O(1)O(1) 的额外空间。

作者：LeetCode
链接：https://leetcode-cn.com/problems/number-of-digit-one/solution/shu-zi-1-de-ge-shu-by-leetcode/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
