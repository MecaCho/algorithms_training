# encoding=utf8


'''
810. Chalkboard XOR Game

We are given non-negative integers nums[i] which are written on a chalkboard.  Alice and Bob take turns erasing exactly one number from the chalkboard, with Alice starting first.  If erasing a number causes the bitwise XOR of all the elements of the chalkboard to become 0, then that player loses.  (Also, we'll say the bitwise XOR of one element is that element itself, and the bitwise XOR of no elements is 0.)

Also, if any player starts their turn with the bitwise XOR of all the elements of the chalkboard equal to 0, then that player wins.

Return True if and only if Alice wins the game, assuming both players play optimally.

Example:
Input: nums = [1, 1, 2]
Output: false
Explanation: 
Alice has two choices: erase 1 or erase 2. 
If she erases 1, the nums array becomes [1, 2]. The bitwise XOR of all the elements of the chalkboard is 1 XOR 2 = 3. Now Bob can remove any element he wants, because Alice will be the one to erase the last element and she will lose. 
If Alice erases 2 first, now nums becomes [1, 1]. The bitwise XOR of all the elements of the chalkboard is 1 XOR 1 = 0. Alice will lose.

Notes:

1 <= N <= 1000. 
0 <= nums[i] <= 2^16.

810. 黑板异或游戏

黑板上写着一个非负整数数组 nums[i] 。Alice 和 Bob 轮流从黑板上擦掉一个数字，Alice 先手。如果擦除一个数字后，剩余的所有数字按位异或运算得出的结果等于 0 的话，当前玩家游戏失败。 (另外，如果只剩一个数字，按位异或运算得到它本身；如果无数字剩余，按位异或运算结果为 0。）

并且，轮到某个玩家时，如果当前黑板上所有数字按位异或运算结果等于 0，这个玩家获胜。

假设两个玩家每步都使用最优解，当且仅当 Alice 获胜时返回 true。

 

示例：

输入: nums = [1, 1, 2]
输出: false
解释: 
Alice 有两个选择: 擦掉数字 1 或 2。
如果擦掉 1, 数组变成 [1, 2]。剩余数字按位异或得到 1 XOR 2 = 3。那么 Bob 可以擦掉任意数字，因为 Alice 会成为擦掉最后一个数字的人，她总是会输。
如果 Alice 擦掉 2，那么数组变成[1, 1]。剩余数字按位异或得到 1 XOR 1 = 0。Alice 仍然会输掉游戏。
 

提示：

1 <= N <= 1000
0 <= nums[i] <= 2^16
'''


class Solution(object):
    def xorGame(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) % 2 == 0:
            return True
        
        xorsum = reduce(xor, nums)
        return xorsum == 0


# solutions

'''
方法一：数学
下文将「按位异或运算」简称为「异或」。

根据游戏规则，轮到某个玩家时，如果当前黑板上所有数字异或结果等于 00，则当前玩家获胜。由于 \text{Alice}Alice 是先手，因此如果初始时黑板上所有数字异或结果等于 00，则 \text{Alice}Alice 获胜。

下面讨论初始时黑板上所有数字异或结果不等于 00 的情况。

由于两人交替擦除数字，且每次都恰好擦掉一个数字，因此对于这两人中的任意一人，其每次在擦除数字前，黑板上剩余数字的个数的奇偶性一定都是相同的。

这启发我们从数组 \textit{nums}nums 长度的奇偶性来讨论。如果 \textit{nums}nums 的长度是偶数，先手 \text{Alice}Alice 是否有可能失败呢？假设 \text{Alice}Alice 面临失败的状态，则只有一种情况，即无论擦掉哪一个数字，剩余所有数字的异或结果都等于 00。

下面证明这是不可能的。设数组 \textit{nums}nums 的长度为 nn，nn 是偶数，用 \oplus⊕ 表示异或，记 SS 为数组 \textit{nums}nums 的全部元素的异或结果，则有

S=\textit{nums}[0] \oplus \textit{nums}[1] \oplus \ldots \oplus \textit{nums}[n-1] \ne 0
S=nums[0]⊕nums[1]⊕…⊕nums[n−1] 

​	
 =0

记 S_iS 
i
​	
  为擦掉 \textit{nums}[i]nums[i] 之后，剩余所有数字的异或结果，则有

S_i \oplus \textit{nums}[i] = S
S 
i
​	
 ⊕nums[i]=S

等式两边同时异或 \textit{nums}[i]nums[i]，由于对任意整数 xx 都有 x \oplus x=0x⊕x=0，得

S_i = S \oplus \textit{nums}[i]
S 
i
​	
 =S⊕nums[i]

如果无论擦掉哪一个数字，剩余的所有数字异或结果都等于 00，即对任意 0 \le i<n0≤i<n，都有 S_i=0S 
i
​	
 =0。因此对所有的 S_iS 
i
​	
  异或结果也等于 00，即

S_0 \oplus S_1 \oplus \ldots \oplus S_{n-1} = 0
S 
0
​	
 ⊕S 
1
​	
 ⊕…⊕S 
n−1
​	
 =0

将 S_i=S \oplus \textit{nums}[i]S 
i
​	
 =S⊕nums[i] 代入上式，并根据异或运算的交换律和结合律化简，有

\begin{aligned} 0 &= S_0 \oplus S_1 \oplus \ldots \oplus S_{n-1} \\ &= (S \oplus \textit{nums}[0]) \oplus (S \oplus \textit{nums}[1]) \oplus \ldots \oplus (S \oplus \textit{nums}[n-1]) \\ &= (S \oplus S \oplus \ldots \oplus S) \oplus (\textit{nums}[0] \oplus \textit{nums}[1] \oplus \ldots \oplus \textit{nums}[n-1]) \\ &= 0 \oplus S \\ &= S \end{aligned}
0
​	
  
=S 
0
​	
 ⊕S 
1
​	
 ⊕…⊕S 
n−1
​	
 
=(S⊕nums[0])⊕(S⊕nums[1])⊕…⊕(S⊕nums[n−1])
=(S⊕S⊕…⊕S)⊕(nums[0]⊕nums[1]⊕…⊕nums[n−1])
=0⊕S
=S
​	
 

上述计算中，第 33 行的左边括号为 nn 个 SS 异或，由于 nn 是偶数，因此 nn 个 SS 异或的结果是 00。

根据上述计算，可以得到 S=0S=0，与实际情况 S \ne 0S 

​	
 =0 矛盾。

因此当数组的长度是偶数时，先手 \text{Alice}Alice 总能找到一个数字，在擦掉这个数字之后剩余的所有数字异或结果不等于 00。

在 \text{Alice}Alice 擦掉这个数字后，黑板上剩下奇数个数字，无论 \text{Bob}Bob 擦掉哪个数字，留给 \text{Alice}Alice 的一定是黑板上剩下偶数个数字，此时 \text{Alice}Alice 要么获胜，要么仍可以找到一个数字，在擦掉这个数字之后剩余的所有数字异或结果不等于 00，因此 \text{Alice}Alice 总能立于不败之地。

同理可得，当数组的长度是奇数时，\text{Alice}Alice 在擦掉一个数字之后，留给 \text{Bob}Bob 的一定是黑板上剩下偶数个数字，因此 \text{Bob}Bob 必胜。

综上所述，当且仅当以下两个条件至少满足一个时，\text{Alice}Alice 必胜：

数组 \textit{nums}nums 的全部元素的异或结果等于 00；

数组 \textit{nums}nums 的长度是偶数。

代码实现时，可以先判断数组 \textit{nums}nums 的长度是否是偶数，当长度是偶数时直接返回 \text{true}true，当长度是奇数时才需要遍历数组计算全部元素的异或结果。该实现方法在数组长度是偶数时只需要 O(1)O(1) 的时间即可得到答案。

JavaC#JavaScriptGolangPython3C++C

func xorGame(nums []int) bool {
    if len(nums)%2 == 0 {
        return true
    }
    xor := 0
    for _, num := range nums {
        xor ^= num
    }
    return xor == 0
}
复杂度分析

时间复杂度：O(n)O(n)，其中 nn 是数组 \textit{nums}nums 的长度。最坏情况下，需要遍历数组一次，计算全部元素的异或结果。

空间复杂度：O(1)O(1)。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/chalkboard-xor-game/solution/hei-ban-yi-huo-you-xi-by-leetcode-soluti-eb0c/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
