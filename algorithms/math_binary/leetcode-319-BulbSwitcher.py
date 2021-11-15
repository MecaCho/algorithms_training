# encoding=utf8

'''
319. Bulb Switcher
There are n bulbs that are initially off. You first turn on all the bulbs, then you turn off every second bulb.

On the third round, you toggle every third bulb (turning on if it's off or turning off if it's on). For the ith round, you toggle every i bulb. For the nth round, you only toggle the last bulb.

Return the number of bulbs that are on after n rounds.

 

Example 1:


Input: n = 3
Output: 1
Explanation: At first, the three bulbs are [off, off, off].
After the first round, the three bulbs are [on, on, on].
After the second round, the three bulbs are [on, off, on].
After the third round, the three bulbs are [on, off, off]. 
So you should return 1 because there is only one bulb is on.
Example 2:

Input: n = 0
Output: 0
Example 3:

Input: n = 1
Output: 1
 

Constraints:

0 <= n <= 109

319. 灯泡开关
初始时有 n 个灯泡处于关闭状态。第一轮，你将会打开所有灯泡。接下来的第二轮，你将会每两个灯泡关闭一个。

第三轮，你每三个灯泡就切换一个灯泡的开关（即，打开变关闭，关闭变打开）。第 i 轮，你每 i 个灯泡就切换一个灯泡的开关。直到第 n 轮，你只需要切换最后一个灯泡的开关。

找出并返回 n 轮后有多少个亮着的灯泡。

 

示例 1：



输入：n = 3
输出：1 
解释：
初始时, 灯泡状态 [关闭, 关闭, 关闭].
第一轮后, 灯泡状态 [开启, 开启, 开启].
第二轮后, 灯泡状态 [开启, 关闭, 开启].
第三轮后, 灯泡状态 [开启, 关闭, 关闭]. 

你应该返回 1，因为只有一个灯泡还亮着。
示例 2：

输入：n = 0
输出：0
示例 3：

输入：n = 1
输出：1
 

提示：

0 <= n <= 109 
'''

class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        return int(sqrt(n+0.5))
        
# solutions

'''
因此，对于第 kk 个灯泡，它被切换的次数恰好就是 kk 的约数个数。如果 kk 有偶数个约数，那么最终第 kk 个灯泡的状态为暗；如果 kk 有奇数个约数，那么最终第 kk 个灯泡的状态为亮。

对于 kk 而言，如果它有约数 xx，那么一定有约数
 。因此只要当 x^2 \neq kx 约数都是「成对」出现的。这就说明，只有当 kk 是「完全平方数」时，它才会有奇数个约数，否则一定有偶数个约数。

因此我们只需要找出 1, 2, \cdots, n1,2,⋯,n 中的完全平方数的个数即可

'''
