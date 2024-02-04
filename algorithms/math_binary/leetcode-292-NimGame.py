# encoding=utf8

'''
292. Nim Game
You are playing the following Nim Game with your friend:

Initially, there is a heap of stones on the table.
You and your friend will alternate taking turns, and you go first.
On each turn, the person whose turn it is will remove 1 to 3 stones from the heap.
The one who removes the last stone is the winner.
Given n, the number of stones in the heap, return true if you can win the game assuming both you and your friend play optimally, otherwise return false.

 

Example 1:

Input: n = 4
Output: false
Explanation: These are the possible outcomes:
1. You remove 1 stone. Your friend removes 3 stones, including the last stone. Your friend wins.
2. You remove 2 stones. Your friend removes 2 stones, including the last stone. Your friend wins.
3. You remove 3 stones. Your friend removes the last stone. Your friend wins.
In all outcomes, your friend wins.
Example 2:

Input: n = 1
Output: true
Example 3:

Input: n = 2
Output: true
 

Constraints:

1 <= n <= 231 - 1

292. Nim 游戏
你和你的朋友，两个人一起玩 Nim 游戏：

桌子上有一堆石头。
你们轮流进行自己的回合，你作为先手。
每一回合，轮到的人拿掉 1 - 3 块石头。
拿掉最后一块石头的人就是获胜者。
假设你们每一步都是最优解。请编写一个函数，来判断你是否可以在给定石头数量为 n 的情况下赢得游戏。如果可以赢，返回 true；否则，返回 false 。

 

示例 1：

输入：n = 4
输出：false 
解释：如果堆中有 4 块石头，那么你永远不会赢得比赛；
     因为无论你拿走 1 块、2 块 还是 3 块石头，最后一块石头总是会被你的朋友拿走。
示例 2：

输入：n = 1
输出：true
示例 3：

输入：n = 2
输出：true
 

提示：

1 <= n <= 231 - 1
'''

class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n%4 != 0

      
# solutions

'''
方法一：数学推理
思路与算法

让我们考虑一些小例子。显而易见的是，如果石头堆中只有一块、两块、或是三块石头，那么在你的回合，你就可以把全部石子拿走，从而在游戏中取胜；
如果堆中恰好有四块石头，你就会失败。因为在这种情况下不管你取走多少石头，总会为你的对手留下几块，他可以将剩余的石头全部取完，从而他可以在游戏中打败你。
因此，要想获胜，在你的回合中，必须避免石头堆中的石子数为 4 的情况。

我们继续推理，假设当前堆里只剩下五块、六块、或是七块石头，你可以控制自己拿取的石头数，总是恰好给你的对手留下四块石头，使他输掉这场比赛。
但是如果石头堆里有八块石头，你就不可避免地会输掉，因为不管你从一堆石头中挑出一块、两块还是三块，你的对手都可以选择三块、两块或一块，
以确保在再一次轮到你的时候，你会面对四块石头。显然我们继续推理，可以看到它会以相同的模式不断重复 n = 4, 8, 12, 16, \ldotsn=4,8,12,16,…，
基本可以看出如果堆里的石头数目为 4 的倍数时，你一定会输掉游戏。

如果总的石头数目为 4 的倍数时，因为无论你取多少石头，对方总有对应的取法，让剩余的石头的数目继续为 4 的倍数。对于你或者你的对手取石头时，
显然最优的选择是当前己方取完石头后，让剩余的石头的数目为 4 的倍数。假设当前的石头数目为 xx，如果 xx 为 4 的倍数时，
则此时你必然会输掉游戏；如果 xx 不为 4 的倍数时，则此时你只需要取走 x \bmod 4xmod4 个石头时，则剩余的石头数目必然为 4 的倍数，从而对手会输掉游戏。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/nim-game/solution/nim-you-xi-by-leetcode-solution-95g8/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''

